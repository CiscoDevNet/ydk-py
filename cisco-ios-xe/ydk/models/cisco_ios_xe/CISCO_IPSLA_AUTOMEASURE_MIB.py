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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIPSLAAUTOMEASUREMIB(Entity):
    """
    
    
    .. attribute:: cipslaautogrouptable
    
    	A table that contains IP SLA auto measure group definitions
    	**type**\:  :py:class:`Cipslaautogrouptable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CISCOIPSLAAUTOMEASUREMIB.Cipslaautogrouptable>`
    
    .. attribute:: cipslaautogroupdesttable
    
    	A table contains the list of destination IP addresses and ports associated to the auto measure group destination name
    	**type**\:  :py:class:`Cipslaautogroupdesttable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupdesttable>`
    
    .. attribute:: cipslareacttable
    
    	A table that contains reaction configurations for templates. Each conceptual row in cipslaReactTable corresponds  to a reaction configured for one template.  Each template can have multiple reactions and hence there can be  multiple rows for a particular template. Different template types can have different reactions. The reaction type is  specified as cipslaReactVar based upon template type as some  reaction types are applicable just for specific template types
    	**type**\:  :py:class:`Cipslareacttable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CISCOIPSLAAUTOMEASUREMIB.Cipslareacttable>`
    
    .. attribute:: cipslaautogroupschedtable
    
    	A table of group scheduling definitions
    	**type**\:  :py:class:`Cipslaautogroupschedtable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupschedtable>`
    
    

    """

    _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
    _revision = '2007-06-13'

    def __init__(self):
        super(CISCOIPSLAAUTOMEASUREMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSLA-AUTOMEASURE-MIB"
        self.yang_parent_name = "CISCO-IPSLA-AUTOMEASURE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cipslaAutoGroupTable", ("cipslaautogrouptable", CISCOIPSLAAUTOMEASUREMIB.Cipslaautogrouptable)), ("cipslaAutoGroupDestTable", ("cipslaautogroupdesttable", CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupdesttable)), ("cipslaReactTable", ("cipslareacttable", CISCOIPSLAAUTOMEASUREMIB.Cipslareacttable)), ("cipslaAutoGroupSchedTable", ("cipslaautogroupschedtable", CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupschedtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cipslaautogrouptable = CISCOIPSLAAUTOMEASUREMIB.Cipslaautogrouptable()
        self.cipslaautogrouptable.parent = self
        self._children_name_map["cipslaautogrouptable"] = "cipslaAutoGroupTable"
        self._children_yang_names.add("cipslaAutoGroupTable")

        self.cipslaautogroupdesttable = CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupdesttable()
        self.cipslaautogroupdesttable.parent = self
        self._children_name_map["cipslaautogroupdesttable"] = "cipslaAutoGroupDestTable"
        self._children_yang_names.add("cipslaAutoGroupDestTable")

        self.cipslareacttable = CISCOIPSLAAUTOMEASUREMIB.Cipslareacttable()
        self.cipslareacttable.parent = self
        self._children_name_map["cipslareacttable"] = "cipslaReactTable"
        self._children_yang_names.add("cipslaReactTable")

        self.cipslaautogroupschedtable = CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupschedtable()
        self.cipslaautogroupschedtable.parent = self
        self._children_name_map["cipslaautogroupschedtable"] = "cipslaAutoGroupSchedTable"
        self._children_yang_names.add("cipslaAutoGroupSchedTable")
        self._segment_path = lambda: "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB"


    class Cipslaautogrouptable(Entity):
        """
        A table that contains IP SLA auto measure group definitions.
        
        .. attribute:: cipslaautogroupentry
        
        	An entry containing the configurations for a particular auto measure group
        	**type**\: list of  		 :py:class:`Cipslaautogroupentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CISCOIPSLAAUTOMEASUREMIB.Cipslaautogrouptable.Cipslaautogroupentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            super(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogrouptable, self).__init__()

            self.yang_name = "cipslaAutoGroupTable"
            self.yang_parent_name = "CISCO-IPSLA-AUTOMEASURE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipslaAutoGroupEntry", ("cipslaautogroupentry", CISCOIPSLAAUTOMEASUREMIB.Cipslaautogrouptable.Cipslaautogroupentry))])
            self._leafs = OrderedDict()

            self.cipslaautogroupentry = YList(self)
            self._segment_path = lambda: "cipslaAutoGroupTable"
            self._absolute_path = lambda: "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogrouptable, [], name, value)


        class Cipslaautogroupentry(Entity):
            """
            An entry containing the configurations for a particular
            auto measure group.
            
            .. attribute:: cipslaautogroupname  (key)
            
            	A group name which is used by a management application to identify the group
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cipslaautogroupdescription
            
            	This field is used to provide description for the group
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: cipslaautogroupdestinationname
            
            	This object refers to the cipslaAutoGroupDestName in cipslaAutoGroupDestTable. If the name entered  is not present in cipslaAutoGroupDestTable, then when  group is scheduled, no ip sla operations will be created
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: cipslaautogroupaddestport
            
            	This object represents the destination port number for auto discovery use
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipslaautogroupopertemplatename
            
            	A string which is used by a management application to identify the template which is associated with the group. Depends on cipslaAutoGroupOperType, this object refers to cipslaIcmpEchoTmplName in cipslaIcmpEchoTmplTable, or cipslaUdpEchoTmplName in cipslaUdpEchoTmplTable, or cipslaTcpConnTmplName in cipslaTcpConnTmplTable, or cipslaIcmpJitterTmplName in cipslaIcmpJitterTmplTable, or ciscoIpSlaUdpJitterTmplName in ciscoIpSlaUdpJitterTmplTable
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: cipslaautogroupschedulerid
            
            	This object refers to the cipslaAutoGroupSchedId in cipslaAutoGroupSchedTable, and is used to schedule  this group
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: cipslaautogroupqosenable
            
            	When this object is set to true, QoS is enabled for this group and this group is linked to policy map. The  restriction is that after QoS is enabled, it can not be  disabled for this group
            	**type**\: bool
            
            .. attribute:: cipslaautogroupopertype
            
            	This object specifies the type of IP SLA operation. When operation type is not ICMP jitter, then  cipslaAutoGroupOperTemplateName must be specified
            	**type**\:  :py:class:`IpSlaOperType <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.IpSlaOperType>`
            
            .. attribute:: cipslaautogroupdestipadenable
            
            	When this object is set to true, destination IP address is populated through auto\-discovery
            	**type**\: bool
            
            .. attribute:: cipslaautogroupadmeasureretry
            
            	This object specifies number of measurement retries to be attempted for the discovered end point after the  connection to the end point is broken. If there is no  re\-registration message received, the end point will be  in inactive state.  When the value of cipslaAutoGroupDestIPADEnable is  'false', the value of this object has no effect
            	**type**\: int
            
            	**range:** 1..65536
            
            .. attribute:: cipslaautogroupaddestipageout
            
            	This object represents the ageout time for the discovered end point.  If the end point becomes inactive for the period  of ageout time, the end point will be removed from the  discovered end point list.  When the value of cipslaAutoGroupDestIPADEnable is  'false', the value of this object has no effect
            	**type**\: int
            
            	**range:** 0..65536
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupstoragetype
            
            	The storage type of this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslaautogrouprowstatus
            
            	The status of the conceptual group control row.  When the status is active, the other writable objects may be modified unless the scheduler with name  specified by cipslaAutoGroupSchedulerId is scheduled
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                super(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogrouptable.Cipslaautogroupentry, self).__init__()

                self.yang_name = "cipslaAutoGroupEntry"
                self.yang_parent_name = "cipslaAutoGroupTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslaautogroupname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslaautogroupname', YLeaf(YType.str, 'cipslaAutoGroupName')),
                    ('cipslaautogroupdescription', YLeaf(YType.str, 'cipslaAutoGroupDescription')),
                    ('cipslaautogroupdestinationname', YLeaf(YType.str, 'cipslaAutoGroupDestinationName')),
                    ('cipslaautogroupaddestport', YLeaf(YType.uint16, 'cipslaAutoGroupADDestPort')),
                    ('cipslaautogroupopertemplatename', YLeaf(YType.str, 'cipslaAutoGroupOperTemplateName')),
                    ('cipslaautogroupschedulerid', YLeaf(YType.str, 'cipslaAutoGroupSchedulerId')),
                    ('cipslaautogroupqosenable', YLeaf(YType.boolean, 'cipslaAutoGroupQoSEnable')),
                    ('cipslaautogroupopertype', YLeaf(YType.enumeration, 'cipslaAutoGroupOperType')),
                    ('cipslaautogroupdestipadenable', YLeaf(YType.boolean, 'cipslaAutoGroupDestIPADEnable')),
                    ('cipslaautogroupadmeasureretry', YLeaf(YType.uint32, 'cipslaAutoGroupADMeasureRetry')),
                    ('cipslaautogroupaddestipageout', YLeaf(YType.uint32, 'cipslaAutoGroupADDestIPAgeout')),
                    ('cipslaautogroupstoragetype', YLeaf(YType.enumeration, 'cipslaAutoGroupStorageType')),
                    ('cipslaautogrouprowstatus', YLeaf(YType.enumeration, 'cipslaAutoGroupRowStatus')),
                ])
                self.cipslaautogroupname = None
                self.cipslaautogroupdescription = None
                self.cipslaautogroupdestinationname = None
                self.cipslaautogroupaddestport = None
                self.cipslaautogroupopertemplatename = None
                self.cipslaautogroupschedulerid = None
                self.cipslaautogroupqosenable = None
                self.cipslaautogroupopertype = None
                self.cipslaautogroupdestipadenable = None
                self.cipslaautogroupadmeasureretry = None
                self.cipslaautogroupaddestipageout = None
                self.cipslaautogroupstoragetype = None
                self.cipslaautogrouprowstatus = None
                self._segment_path = lambda: "cipslaAutoGroupEntry" + "[cipslaAutoGroupName='" + str(self.cipslaautogroupname) + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/cipslaAutoGroupTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogrouptable.Cipslaautogroupentry, ['cipslaautogroupname', 'cipslaautogroupdescription', 'cipslaautogroupdestinationname', 'cipslaautogroupaddestport', 'cipslaautogroupopertemplatename', 'cipslaautogroupschedulerid', 'cipslaautogroupqosenable', 'cipslaautogroupopertype', 'cipslaautogroupdestipadenable', 'cipslaautogroupadmeasureretry', 'cipslaautogroupaddestipageout', 'cipslaautogroupstoragetype', 'cipslaautogrouprowstatus'], name, value)


    class Cipslaautogroupdesttable(Entity):
        """
        A table contains the list of destination IP
        addresses and ports associated to the auto measure
        group destination name.
        
        .. attribute:: cipslaautogroupdestentry
        
        	An entry containing the destination IP addresses and port configurations associated to auto measure group destination name
        	**type**\: list of  		 :py:class:`Cipslaautogroupdestentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupdesttable.Cipslaautogroupdestentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            super(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupdesttable, self).__init__()

            self.yang_name = "cipslaAutoGroupDestTable"
            self.yang_parent_name = "CISCO-IPSLA-AUTOMEASURE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipslaAutoGroupDestEntry", ("cipslaautogroupdestentry", CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupdesttable.Cipslaautogroupdestentry))])
            self._leafs = OrderedDict()

            self.cipslaautogroupdestentry = YList(self)
            self._segment_path = lambda: "cipslaAutoGroupDestTable"
            self._absolute_path = lambda: "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupdesttable, [], name, value)


        class Cipslaautogroupdestentry(Entity):
            """
            An entry containing the destination IP addresses
            and port configurations associated to auto measure
            group destination name.
            
            .. attribute:: cipslaautogroupdestname  (key)
            
            	This is the name for an auto measure group destination
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cipslaautogroupdestipaddrtype  (key)
            
            	The type of the internet address of a destination for an auto measure group
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cipslaautogroupdestipaddr  (key)
            
            	The internet address of a destination for an auto measure group. The type of this address is determined by the value of cipslaAutoGroupDestIpAddrType
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cipslaautogroupdestport  (key)
            
            	This object represents the destination port number. For ICMP echo and ICMP jitter, the suggested value is  '0'
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cipslaautogroupdeststoragetype
            
            	The storage type of this conceptual row.  By default the entry will be saved into non\-volatile memory
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslaautogroupdestrowstatus
            
            	The status of the conceptual destination table control row. No other objects in this row need to be set before this object can become active.  During 'destroy', when cipslaAutoGroupDestIpAddr is specified  as '0.0.0.0' and cipslaAutoGroupDestPort is specified as '0',  then all the rows with same cipslaAutoGroupDestName will be  deleted
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                super(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupdesttable.Cipslaautogroupdestentry, self).__init__()

                self.yang_name = "cipslaAutoGroupDestEntry"
                self.yang_parent_name = "cipslaAutoGroupDestTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslaautogroupdestname','cipslaautogroupdestipaddrtype','cipslaautogroupdestipaddr','cipslaautogroupdestport']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslaautogroupdestname', YLeaf(YType.str, 'cipslaAutoGroupDestName')),
                    ('cipslaautogroupdestipaddrtype', YLeaf(YType.enumeration, 'cipslaAutoGroupDestIpAddrType')),
                    ('cipslaautogroupdestipaddr', YLeaf(YType.str, 'cipslaAutoGroupDestIpAddr')),
                    ('cipslaautogroupdestport', YLeaf(YType.uint16, 'cipslaAutoGroupDestPort')),
                    ('cipslaautogroupdeststoragetype', YLeaf(YType.enumeration, 'cipslaAutoGroupDestStorageType')),
                    ('cipslaautogroupdestrowstatus', YLeaf(YType.enumeration, 'cipslaAutoGroupDestRowStatus')),
                ])
                self.cipslaautogroupdestname = None
                self.cipslaautogroupdestipaddrtype = None
                self.cipslaautogroupdestipaddr = None
                self.cipslaautogroupdestport = None
                self.cipslaautogroupdeststoragetype = None
                self.cipslaautogroupdestrowstatus = None
                self._segment_path = lambda: "cipslaAutoGroupDestEntry" + "[cipslaAutoGroupDestName='" + str(self.cipslaautogroupdestname) + "']" + "[cipslaAutoGroupDestIpAddrType='" + str(self.cipslaautogroupdestipaddrtype) + "']" + "[cipslaAutoGroupDestIpAddr='" + str(self.cipslaautogroupdestipaddr) + "']" + "[cipslaAutoGroupDestPort='" + str(self.cipslaautogroupdestport) + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/cipslaAutoGroupDestTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupdesttable.Cipslaautogroupdestentry, ['cipslaautogroupdestname', 'cipslaautogroupdestipaddrtype', 'cipslaautogroupdestipaddr', 'cipslaautogroupdestport', 'cipslaautogroupdeststoragetype', 'cipslaautogroupdestrowstatus'], name, value)


    class Cipslareacttable(Entity):
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
        	**type**\: list of  		 :py:class:`Cipslareactentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CISCOIPSLAAUTOMEASUREMIB.Cipslareacttable.Cipslareactentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            super(CISCOIPSLAAUTOMEASUREMIB.Cipslareacttable, self).__init__()

            self.yang_name = "cipslaReactTable"
            self.yang_parent_name = "CISCO-IPSLA-AUTOMEASURE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipslaReactEntry", ("cipslareactentry", CISCOIPSLAAUTOMEASUREMIB.Cipslareacttable.Cipslareactentry))])
            self._leafs = OrderedDict()

            self.cipslareactentry = YList(self)
            self._segment_path = lambda: "cipslaReactTable"
            self._absolute_path = lambda: "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAAUTOMEASUREMIB.Cipslareacttable, [], name, value)


        class Cipslareactentry(Entity):
            """
            A base list of objects that define a conceptual reaction
            configuration control row.
            
            .. attribute:: cipslaautogroupopertype  (key)
            
            	
            	**type**\:  :py:class:`IpSlaOperType <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.IpSlaOperType>`
            
            .. attribute:: cipslareactconfigindex  (key)
            
            	This object along with cipslaAutoGroupOperType and cipslaAutoGroupOperTemplateName identifies a particular reaction\-configuration for one IP SLA  template.  This number is persistent across reboots
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipslaautogroupopertemplatename  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..64
            
            	**refers to**\:  :py:class:`cipslaautogroupopertemplatename <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CISCOIPSLAAUTOMEASUREMIB.Cipslaautogrouptable.Cipslaautogroupentry>`
            
            .. attribute:: cipslareactvar
            
            	This object specifies the type of reaction configured for an IP SLA template. Default value is 'rtt' for ICMP echo, UDP echo and TCP connect. Default value is 'jitterAvg' for UDP jitter and  ICMP jitter.  The reaction types 'rtt', 'timeout', 'connectionLoss' and 'verifyError' can be configured for all template types.  The reaction types 'jitterSDAvg', 'jitterDSAvg', 'jitterAvg',  'packetLateArrival', 'packetOutOfSequence',  'maxOfPositiveSD', 'maxOfNegativeSD', 'maxOfPositiveDS' 'maxOfNegativeDS', 'mos' and 'icpif' can be configured for  UDP jitter and ICMP jitter types only.  The reaction types 'packetLossDS', 'packetLossSD' and  'packetMIA' can be configured for UDP jitter type only.  The reaction types 'successivePacketLoss', 'maxOfLatencyDS',  'maxOfLatencySD', 'latencyDSAvg', 'latencySDAvg' and  'packetLoss' can be configured for ICMP jitter type only
            	**type**\:  :py:class:`IpSlaReactVar <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.IpSlaReactVar>`
            
            .. attribute:: cipslareactthresholdtype
            
            	This object specifies the conditions under which a notification ( trap ) is sent. The rttMonReactOccurred object defined in rttMonReactTable in CISCO\-RTTMON\-MIB will change accordingly\:  never(1)       \- rttMonReactOccurred is never set  immediate(2)   \- rttMonReactOccurred is set to 'true' when the                  value of parameter for which reaction is                  configured ( e.g rtt, jitterAvg, packetLossSD,                  mos etc ) violates the threshold.                  Conversely, rttMonReactOccurred is set to 'false'                  when the parameter ( e.g rtt, jitterAvg,                  packetLossSD, mos etc ) is below the threshold                  limits.  consecutive(3) \- rttMonReactOccurred is set to true when the value                  of parameter for which reaction is configured                  ( e.g rtt, jitterAvg, packetLossSD, mos etc )                  violates the threshold for configured consecutive                  times.                  Conversely, rttMonReactOccurred is set to false                  when the value of parameter ( e.g rtt, jitterAvg                  packetLossSD, mos etc ) is below the threshold                  limits for the same number of consecutive                  operations.  xOfy(4)        \- rttMonReactOccurred is set to true when x                  ( as specified by cipslaReactThresholdCountX )                  out of the last y ( as specified by                  cipslaReacthresholdCountY ) times the value of                  parameter for which the reaction is configured                  ( e.g rtt, jitterAvg, packetLossSD, mos etc )                  violates the threshold.                  Conversely, it is set to false when x, out of the                  last y times the value of parameter                  ( e.g rtt, jitterAvg, packetLossSD, mos ) is                  below the threshold limits.                  NOTE\: If x > y, this will never                       generate a reaction.  average(5)    \- rttMonReactOccurred is set to true when the                 average ( cipslaReactThresholdCountX times )                 value of parameter for which reaction is                  configured ( e.g rtt, jitterAvg, packetLossSD,                 mos etc ) violates the threshold condition.                 Conversely, it is set to false when the                 average value of parameter ( e.g rtt, jitterAvg,                 packetLossSD, mos etc ) is below the threshold                 limits.  If this value is changed by a management station, rttMonReactOccurred is set to false, but no reaction is generated if the prior value of rttMonReactOccurred was true
            	**type**\:  :py:class:`Cipslareactthresholdtype <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CISCOIPSLAAUTOMEASUREMIB.Cipslareacttable.Cipslareactentry.Cipslareactthresholdtype>`
            
            .. attribute:: cipslareactactiontype
            
            	Specifies what type, if any, of reaction to generate if one of the watched (reaction\-configuration ) conditions is satisfied\:  none(1)                \- no reaction is generated notificationOnly(2)    \- a notification is generated
            	**type**\:  :py:class:`Cipslareactactiontype <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CISCOIPSLAAUTOMEASUREMIB.Cipslareacttable.Cipslareactentry.Cipslareactactiontype>`
            
            .. attribute:: cipslareactthresholdrising
            
            	This object defines the higher threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) rises above this limit and if the condition specified in cipslaReactThresholdType is satisfied, a notification is  generated.  Default value of cipslaReactThresholdRising for    'rtt' is 5000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 5000.    'maxOfLatencySD' is 5000.    'latencyDSAvg' is 5000.    'latencySDAvg' is 5000.    'packetLoss' is 10000.  This object is not applicable if the cipslaReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError' default value of  cipslaReactThresholdRising will be 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipslareactthresholdfalling
            
            	This object defines a lower threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) falls below this limit and if the condition specified in cipslaReactThresholdType is satisfied, a notification  is generated. This object value can not bigger than cipslaReactThresholdRising value.  Default value of cipslaReactThresholdFalling    'rtt' is 3000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 3000.    'maxOfLatencySD' is 3000.    'latencyDSAvg' is 3000.    'latencySDAvg' is 3000.    'packetLoss' is 10000.  This object is not applicable if the cipslaReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError', default value of cipslaReactThresholdFalling will be 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipslareactthresholdcountx
            
            	If cipslaReactThresholdType value is 'xOfy', this object defines the 'x' value.  If cipslaReactThresholdType value is 'consecutive' this object defines the number of consecutive occurrences that needs threshold violation before setting  cipslaReactOccurred as true.  If cipslaReactThresholdType value is 'average' this object defines the number of samples that needs be considered for calculating average.  This object has no meaning if cipslaReactThresholdType has value of 'never' and 'immediate'
            	**type**\: int
            
            	**range:** 1..16
            
            .. attribute:: cipslareactthresholdcounty
            
            	This object defines the 'y' value of the xOfy condition if cipslaReactThresholdType is 'xOfy'. The default for the  'y' value is 5.  For other values of cipslaReactThresholdType, this object is not applicable
            	**type**\: int
            
            	**range:** 1..16
            
            .. attribute:: cipslareactstoragetype
            
            	The storage type of this conceptual row.  By default the entry will be saved into non\-volatile memory
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslareactrowstatus
            
            	This objects indicates the status of the conceptual Reaction Control Row.   When this object moves to active state, the conceptual row  is monitored and notifications are generated when threshold  violation takes place.  In order for this object to become active cipslaReactVar must be defined. All other objects assume default values.  When the  status is active, the following objects in that row can be  modified.  cipslaReactThresholdType,  cipslaReactActionType,  cipslaReactThresholdRising,  cipslaReactThresholdFalling,  cipslaReactThresholdCountX,  cipslaReactThresholdCountY,  cipslaReactStorageType  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' no reaction configuration would exist. The reaction configuration for the template is  removed
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                super(CISCOIPSLAAUTOMEASUREMIB.Cipslareacttable.Cipslareactentry, self).__init__()

                self.yang_name = "cipslaReactEntry"
                self.yang_parent_name = "cipslaReactTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslaautogroupopertype','cipslareactconfigindex','cipslaautogroupopertemplatename']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslaautogroupopertype', YLeaf(YType.enumeration, 'cipslaAutoGroupOperType')),
                    ('cipslareactconfigindex', YLeaf(YType.uint32, 'cipslaReactConfigIndex')),
                    ('cipslaautogroupopertemplatename', YLeaf(YType.str, 'cipslaAutoGroupOperTemplateName')),
                    ('cipslareactvar', YLeaf(YType.enumeration, 'cipslaReactVar')),
                    ('cipslareactthresholdtype', YLeaf(YType.enumeration, 'cipslaReactThresholdType')),
                    ('cipslareactactiontype', YLeaf(YType.enumeration, 'cipslaReactActionType')),
                    ('cipslareactthresholdrising', YLeaf(YType.uint32, 'cipslaReactThresholdRising')),
                    ('cipslareactthresholdfalling', YLeaf(YType.uint32, 'cipslaReactThresholdFalling')),
                    ('cipslareactthresholdcountx', YLeaf(YType.uint32, 'cipslaReactThresholdCountX')),
                    ('cipslareactthresholdcounty', YLeaf(YType.uint32, 'cipslaReactThresholdCountY')),
                    ('cipslareactstoragetype', YLeaf(YType.enumeration, 'cipslaReactStorageType')),
                    ('cipslareactrowstatus', YLeaf(YType.enumeration, 'cipslaReactRowStatus')),
                ])
                self.cipslaautogroupopertype = None
                self.cipslareactconfigindex = None
                self.cipslaautogroupopertemplatename = None
                self.cipslareactvar = None
                self.cipslareactthresholdtype = None
                self.cipslareactactiontype = None
                self.cipslareactthresholdrising = None
                self.cipslareactthresholdfalling = None
                self.cipslareactthresholdcountx = None
                self.cipslareactthresholdcounty = None
                self.cipslareactstoragetype = None
                self.cipslareactrowstatus = None
                self._segment_path = lambda: "cipslaReactEntry" + "[cipslaAutoGroupOperType='" + str(self.cipslaautogroupopertype) + "']" + "[cipslaReactConfigIndex='" + str(self.cipslareactconfigindex) + "']" + "[cipslaAutoGroupOperTemplateName='" + str(self.cipslaautogroupopertemplatename) + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/cipslaReactTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAAUTOMEASUREMIB.Cipslareacttable.Cipslareactentry, ['cipslaautogroupopertype', 'cipslareactconfigindex', 'cipslaautogroupopertemplatename', 'cipslareactvar', 'cipslareactthresholdtype', 'cipslareactactiontype', 'cipslareactthresholdrising', 'cipslareactthresholdfalling', 'cipslareactthresholdcountx', 'cipslareactthresholdcounty', 'cipslareactstoragetype', 'cipslareactrowstatus'], name, value)

            class Cipslareactactiontype(Enum):
                """
                Cipslareactactiontype (Enum Class)

                Specifies what type, if any, of reaction to

                generate if one of the watched

                (reaction\-configuration ) conditions is satisfied\:

                none(1)                \- no reaction is generated

                notificationOnly(2)    \- a notification is generated

                .. data:: none = 1

                .. data:: notificationOnly = 2

                """

                none = Enum.YLeaf(1, "none")

                notificationOnly = Enum.YLeaf(2, "notificationOnly")


            class Cipslareactthresholdtype(Enum):
                """
                Cipslareactthresholdtype (Enum Class)

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

                never = Enum.YLeaf(1, "never")

                immediate = Enum.YLeaf(2, "immediate")

                consecutive = Enum.YLeaf(3, "consecutive")

                xOfy = Enum.YLeaf(4, "xOfy")

                average = Enum.YLeaf(5, "average")



    class Cipslaautogroupschedtable(Entity):
        """
        A table of group scheduling definitions.
        
        .. attribute:: cipslaautogroupschedentry
        
        	A list of objects that define specific configuration for group scheduling
        	**type**\: list of  		 :py:class:`Cipslaautogroupschedentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupschedtable.Cipslaautogroupschedentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            super(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupschedtable, self).__init__()

            self.yang_name = "cipslaAutoGroupSchedTable"
            self.yang_parent_name = "CISCO-IPSLA-AUTOMEASURE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cipslaAutoGroupSchedEntry", ("cipslaautogroupschedentry", CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupschedtable.Cipslaautogroupschedentry))])
            self._leafs = OrderedDict()

            self.cipslaautogroupschedentry = YList(self)
            self._segment_path = lambda: "cipslaAutoGroupSchedTable"
            self._absolute_path = lambda: "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupschedtable, [], name, value)


        class Cipslaautogroupschedentry(Entity):
            """
            A list of objects that define specific configuration for
            group scheduling.
            
            .. attribute:: cipslaautogroupschedid  (key)
            
            	This string uniquely identifies a row in the cipslaAutoGroupSchedTable
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cipslaautogroupschedperiod
            
            	Specifies the time duration between initiating two IP SLA operations generated via the auto measure group
            	**type**\: int
            
            	**range:** 100..99000
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedinterval
            
            	Specifies the duration between initiating each RTT operation for one IP SLA operation generated via the auto  measure group.  The value of this object is only effective when both cipslaAutoGroupSchedMaxInterval and  cipslaAutoGroupSchedMinInterval have zero values
            	**type**\: int
            
            	**range:** 1..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedlife
            
            	This object specifies the life of all the operations that are getting group scheduled. This value will be placed into cipslaAutoGroupSchedRttLife object when this conceptual control row becomes 'active'.  The value 2147483647 has a special meaning. When this object is set to 2147483647, the rttMonCtrlOperRttLife object for all the operations will not decrement, and thus the life time of the  operation will never end
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedageout
            
            	This object specifies the ageout value of the operations that are getting group scheduled. This value will be placed into rttMonSchedAdminConceptRowAgeout object for each of the operations in the group when this conceptual control row becomes  'active'.  When this value is set to zero, the operations will never ageout
            	**type**\: int
            
            	**range:** 0..2073600
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedmaxinterval
            
            	Specifies the max duration between initiating each RTT operation for one IP SLA operation in the group
            	**type**\: int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedmininterval
            
            	Specifies the min duration between initiating each RTT operation for one IP SLA operation in the group.  The value of this object should be lower than the value of cipslaAutoGroupSchedMaxInterval
            	**type**\: int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedstarttime
            
            	This is the time in seconds after which the operations of the associated groups  will take transition to active state. When set to the value other than '1' (pending), then all  objects in this row cannot be modified
            	**type**\: int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedstoragetype
            
            	The storage type of this conceptual row.  By default the entry will be saved into non\-volatile memory
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cipslaautogroupschedrowstatus
            
            	The status of the conceptual group schedule control row.  When the status is active and the value of  cipslaAutoGroupSchedStartTime is '1', the other writable  objects may be modified.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' it will stop all the  operations which had been group scheduled by it earlier,  before destroying the group schedule control row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                super(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupschedtable.Cipslaautogroupschedentry, self).__init__()

                self.yang_name = "cipslaAutoGroupSchedEntry"
                self.yang_parent_name = "cipslaAutoGroupSchedTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cipslaautogroupschedid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cipslaautogroupschedid', YLeaf(YType.str, 'cipslaAutoGroupSchedId')),
                    ('cipslaautogroupschedperiod', YLeaf(YType.uint32, 'cipslaAutoGroupSchedPeriod')),
                    ('cipslaautogroupschedinterval', YLeaf(YType.uint32, 'cipslaAutoGroupSchedInterval')),
                    ('cipslaautogroupschedlife', YLeaf(YType.uint32, 'cipslaAutoGroupSchedLife')),
                    ('cipslaautogroupschedageout', YLeaf(YType.uint32, 'cipslaAutoGroupSchedAgeout')),
                    ('cipslaautogroupschedmaxinterval', YLeaf(YType.uint32, 'cipslaAutoGroupSchedMaxInterval')),
                    ('cipslaautogroupschedmininterval', YLeaf(YType.uint32, 'cipslaAutoGroupSchedMinInterval')),
                    ('cipslaautogroupschedstarttime', YLeaf(YType.uint32, 'cipslaAutoGroupSchedStartTime')),
                    ('cipslaautogroupschedstoragetype', YLeaf(YType.enumeration, 'cipslaAutoGroupSchedStorageType')),
                    ('cipslaautogroupschedrowstatus', YLeaf(YType.enumeration, 'cipslaAutoGroupSchedRowStatus')),
                ])
                self.cipslaautogroupschedid = None
                self.cipslaautogroupschedperiod = None
                self.cipslaautogroupschedinterval = None
                self.cipslaautogroupschedlife = None
                self.cipslaautogroupschedageout = None
                self.cipslaautogroupschedmaxinterval = None
                self.cipslaautogroupschedmininterval = None
                self.cipslaautogroupschedstarttime = None
                self.cipslaautogroupschedstoragetype = None
                self.cipslaautogroupschedrowstatus = None
                self._segment_path = lambda: "cipslaAutoGroupSchedEntry" + "[cipslaAutoGroupSchedId='" + str(self.cipslaautogroupschedid) + "']"
                self._absolute_path = lambda: "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/cipslaAutoGroupSchedTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPSLAAUTOMEASUREMIB.Cipslaautogroupschedtable.Cipslaautogroupschedentry, ['cipslaautogroupschedid', 'cipslaautogroupschedperiod', 'cipslaautogroupschedinterval', 'cipslaautogroupschedlife', 'cipslaautogroupschedageout', 'cipslaautogroupschedmaxinterval', 'cipslaautogroupschedmininterval', 'cipslaautogroupschedstarttime', 'cipslaautogroupschedstoragetype', 'cipslaautogroupschedrowstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIPSLAAUTOMEASUREMIB()
        return self._top_entity

