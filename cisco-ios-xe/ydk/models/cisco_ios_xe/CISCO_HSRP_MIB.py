""" CISCO_HSRP_MIB 

The MIB module provides a means to monitor and configure
the Cisco IOS proprietary Hot Standby Router Protocol
(HSRP). Cisco HSRP protocol is defined in RFC2281.

Terminology\:

HSRP is a protocol used amoung a group of routers for the
purpose of selecting an 'active router' and a 'standby
router'.

An 'active router' is the router of choice for routing
packets.

A 'standby router' is a router that takes over the routing
duties when an active router fails, or when preset
conditions have been met.

An 'HSRP group' or a 'standby group' is a set of routers
which communicate using HSRP. An HSRP group has a group MAC
address and a group Virtual IP address. These are the
designated addresses. The active router assumes (i.e.
inherits) these group addresses.

'Hello' messages are sent to indicate that a router is
running and is capable of becoming the active or standby
router.

'Hellotime' is the interval between successive HSRP Hello
messages from a given router.

'Holdtime' is the interval between the receipt of a Hello
message and the presumption that the sending router has
failed.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class HsrpState(Enum):
    """
    HsrpState (Enum Class)

    The current state of the HSRP protocol for a given

    HSRP group entry.

    .. data:: initial = 1

    .. data:: learn = 2

    .. data:: listen = 3

    .. data:: speak = 4

    .. data:: standby = 5

    .. data:: active = 6

    """

    initial = Enum.YLeaf(1, "initial")

    learn = Enum.YLeaf(2, "learn")

    listen = Enum.YLeaf(3, "listen")

    speak = Enum.YLeaf(4, "speak")

    standby = Enum.YLeaf(5, "standby")

    active = Enum.YLeaf(6, "active")



class CISCOHSRPMIB(Entity):
    """
    
    
    .. attribute:: chsrpglobalconfig
    
    	
    	**type**\:  :py:class:`CHsrpGlobalConfig <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CISCOHSRPMIB.CHsrpGlobalConfig>`
    
    	**config**\: False
    
    .. attribute:: chsrpgrptable
    
    	A table containing information on each HSRP group for each interface
    	**type**\:  :py:class:`CHsrpGrpTable <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CISCOHSRPMIB.CHsrpGrpTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-HSRP-MIB'
    _revision = '2010-09-06'

    def __init__(self):
        super(CISCOHSRPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-HSRP-MIB"
        self.yang_parent_name = "CISCO-HSRP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cHsrpGlobalConfig", ("chsrpglobalconfig", CISCOHSRPMIB.CHsrpGlobalConfig)), ("cHsrpGrpTable", ("chsrpgrptable", CISCOHSRPMIB.CHsrpGrpTable))])
        self._leafs = OrderedDict()

        self.chsrpglobalconfig = CISCOHSRPMIB.CHsrpGlobalConfig()
        self.chsrpglobalconfig.parent = self
        self._children_name_map["chsrpglobalconfig"] = "cHsrpGlobalConfig"

        self.chsrpgrptable = CISCOHSRPMIB.CHsrpGrpTable()
        self.chsrpgrptable.parent = self
        self._children_name_map["chsrpgrptable"] = "cHsrpGrpTable"
        self._segment_path = lambda: "CISCO-HSRP-MIB:CISCO-HSRP-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOHSRPMIB, [], name, value)


    class CHsrpGlobalConfig(Entity):
        """
        
        
        .. attribute:: chsrpconfigtimeout
        
        	The amount of time in minutes a row in cHsrpGrpTable can remain in a state other than active before being timed out
        	**type**\: int
        
        	**range:** 1..60
        
        	**config**\: False
        
        	**units**\: minutes
        
        

        """

        _prefix = 'CISCO-HSRP-MIB'
        _revision = '2010-09-06'

        def __init__(self):
            super(CISCOHSRPMIB.CHsrpGlobalConfig, self).__init__()

            self.yang_name = "cHsrpGlobalConfig"
            self.yang_parent_name = "CISCO-HSRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('chsrpconfigtimeout', (YLeaf(YType.uint32, 'cHsrpConfigTimeout'), ['int'])),
            ])
            self.chsrpconfigtimeout = None
            self._segment_path = lambda: "cHsrpGlobalConfig"
            self._absolute_path = lambda: "CISCO-HSRP-MIB:CISCO-HSRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOHSRPMIB.CHsrpGlobalConfig, [u'chsrpconfigtimeout'], name, value)



    class CHsrpGrpTable(Entity):
        """
        A table containing information on each HSRP group
        for each interface.
        
        .. attribute:: chsrpgrpentry
        
        	Information about an HSRP group. Management applications use cHsrpGrpRowStatus to control entry modification, creation and deletion.  Setting cHsrpGrpRowStatus to 'active' causes the router to communicate using HSRP.  The value of cHsrpGrpRowStatus may be set to 'destroy' at any time.  Entries may not be created via SNMP without explicitly  setting cHsrpGrpRowStatus to either 'createAndGo' or  'createAndWait'.  Entries can be created and modified via the management  protocol or by the device's local management interface.  A management application wishing to create an entry should choose the ifIndex of the interface which is to be added as part of an HSRP group. Also, a cHsrpGrpNumber should be chosen. A group number is unique only amongst the groups  on a particular interface. The value of the group number appears in packets which are transmitted and received on a  LAN segment to which the router is connected. The application must select the group number as explained in the description for cHsrpGrpNumber.  If the row is not active, and a local management interface command modifies that row, the row may transition to active state.  A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout  period can be changed by setting cHsrpConfigTimeout
        	**type**\: list of  		 :py:class:`CHsrpGrpEntry <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CISCOHSRPMIB.CHsrpGrpTable.CHsrpGrpEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-HSRP-MIB'
        _revision = '2010-09-06'

        def __init__(self):
            super(CISCOHSRPMIB.CHsrpGrpTable, self).__init__()

            self.yang_name = "cHsrpGrpTable"
            self.yang_parent_name = "CISCO-HSRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cHsrpGrpEntry", ("chsrpgrpentry", CISCOHSRPMIB.CHsrpGrpTable.CHsrpGrpEntry))])
            self._leafs = OrderedDict()

            self.chsrpgrpentry = YList(self)
            self._segment_path = lambda: "cHsrpGrpTable"
            self._absolute_path = lambda: "CISCO-HSRP-MIB:CISCO-HSRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOHSRPMIB.CHsrpGrpTable, [], name, value)


        class CHsrpGrpEntry(Entity):
            """
            Information about an HSRP group. Management applications
            use cHsrpGrpRowStatus to control entry modification,
            creation and deletion.
            
            Setting cHsrpGrpRowStatus to 'active' causes the router to
            communicate using HSRP.
            
            The value of cHsrpGrpRowStatus may be set to 'destroy' at
            any time.
            
            Entries may not be created via SNMP without explicitly 
            setting cHsrpGrpRowStatus to either 'createAndGo' or 
            'createAndWait'.
            
            Entries can be created and modified via the management 
            protocol or by the device's local management interface.
            
            A management application wishing to create an entry should
            choose the ifIndex of the interface which is to be added
            as part of an HSRP group. Also, a cHsrpGrpNumber should
            be chosen. A group number is unique only amongst the groups 
            on a particular interface. The value of the group number
            appears in packets which are transmitted and received on a 
            LAN segment to which the router is connected. The application
            must select the group number as explained in the description
            for cHsrpGrpNumber.
            
            If the row is not active, and a local management interface
            command modifies that row, the row may transition to active
            state.
            
            A row which is not in active state will timeout after a
            configurable period (five minutes by default). This timeout 
            period can be changed by setting cHsrpConfigTimeout.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: chsrpgrpnumber  (key)
            
            	This object along with the ifIndex of a particular interface uniquely identifies an HSRP group.  Group numbers 0,1 and 2 are the only valid group numbers for TokenRing interfaces. For other media types, numbers range from 0 to 255. Each interface has its own set of group numbers. There's no relationship between the groups configured on different interfaces. Using a group number on one interface doesn't preclude using the same group number on a different interface. For example, there can be a group 1 on an Ethernet and a group 1 on Token Ring. More details can be found from RFC 2281
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: chsrpgrpauth
            
            	This is an unencrypted authentication string which is carried in all HSRP messages. An authentication string mismatch prevents a router interface from learning the designated IP address or HSRP timer values from other HSRP\-enabled routers with the same group number.  The function of this object is not to supply any sort of security\-like authentication but rather to confirm that what's happening is what's intended. In other words, this is meant for sanity checking only
            	**type**\: str
            
            	**length:** 0..8
            
            	**config**\: False
            
            .. attribute:: chsrpgrppriority
            
            	The cHsrpGrpPriority helps to select the active and the standby routers. The router with the highest priority is selected as the active router. In the priority range of 0 to 255, 0 is the lowest priority and 255 is the highest priority.  If two (or more) routers in a group have the same priority, the one with the highest ip address of the interface is the active router. When the active router fails to send a Hello message within a configurable period of time, the standby router with the highest priority becomes the active router.  A router with highest priority will only attempt to overthrow a lower priority active router if it is configured to preempt.  But, if there is more than one router which is not active, the highest priority non\-active router becomes the standby router
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: chsrpgrppreempt
            
            	This object, if TRUE, indicates that the current router should attempt to overthrow a lower priority active router and attempt to become the active router. If this object is FALSE, the router will become the active router only if there is no such router (or if an active router fails)
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: chsrpgrppreemptdelay
            
            	This delay is the time difference between a router power up and the time it can actually start preempting the currently active router.  When a router first comes up, it doesn't have a complete routing table. If it's configured to preempt, then it will become the Active router, but it will not be able to provide adequate routing services. The solution to this is to allow for a configurable delay before the router actually preempts the currently active router
            	**type**\: int
            
            	**range:** 0..3600
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: chsrpgrpuseconfiguredtimers
            
            	HSRP routers learn a group's Hellotime or Holdtime from hello messages.  The Hellotime is used to determine the frequency of generating hello messages when this router becomes the active or standby router. The Holdtime is the interval between the receipt of a Hello message and the presumption that the sending router has failed.  If this object is TRUE, the cHsrpGrpConfiguredHelloTime and cHsrpGrpConfiguredHoldTime will be used. If it is FALSE, the Hellotime and Holdtime values are learned
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: chsrpgrpconfiguredhellotime
            
            	If cHsrpGrpUseConfiguredTimers is true, cHsrpGrpConfiguredHelloTime is used when this router is an active router. Otherwise, the Hellotime learned from the current active router is used. All routers on a particular LAN segment must use the same Hellotime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: chsrpgrpconfiguredholdtime
            
            	If cHsrpGrpUseConfiguredTimers is true, cHsrpGrpConfiguredHoldTime is used when this router is an active router. Otherwise, the Holdtime learned from the current active router is used. All routers on a particular LAN segment should use the same Holdtime. Also, the Holdtime should be at least three times the value of the Hellotime and must be greater than the Hellotime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: chsrpgrplearnedhellotime
            
            	If the Hellotime is not configured on a router, it can be learned from the Hello messages from active router, provided the Hello message is authenticated. If the Hellotime is not learned from a Hello message from the active router and it is not manually configured, a default value of 3 seconds is recommended
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: chsrpgrplearnedholdtime
            
            	If the Holdtime is not configured on a router, it can be learned from the Hello message from the active router. Holdtime should be learned only if the Hello message is authenticated. If the Holdtime is not learned and it is not manually configured, a default value of 10 seconds is  recommended
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: chsrpgrpvirtualipaddr
            
            	This is the primary virtual IP address used by this group.  If this address is configured (i.e a non zero ip address), this value is used. Otherwise, the agent will attempt to discover the virtual address through a discovery process (which scans the hello messages)
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: chsrpgrpuseconfigvirtualipaddr
            
            	If this object is TRUE, cHsrpGrpVirtualIpAddr was a configured one. Otherwise, it indicates that  cHsrpGrpVirtualIpAddr was a learned one
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: chsrpgrpactiverouter
            
            	Ip Address of the currently active router for this group
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: chsrpgrpstandbyrouter
            
            	Ip Address of the currently standby router for this group
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: chsrpgrpstandbystate
            
            	The current HSRP state of this group on this interface
            	**type**\:  :py:class:`HsrpState <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.HsrpState>`
            
            	**config**\: False
            
            .. attribute:: chsrpgrpvirtualmacaddr
            
            	Mac Addresses used are as specified in RFC 2281. For ethernet and fddi interfaces, a MAC address will be in the range 00\:00\:0c\:07\:ac\:00 through 00\:00\:0c\:07\:ac\:ff. The last octet is the hexadecimal equivalent of cHsrpGrpNumber (0\-255).  Some Ethernet and FDDI interfaces allow a unicast MAC address for each HSRP group. Certain Ethernet chipsets(LANCE Ethernet, VGANYLAN and QUICC Ethernet) only support a single Unicast Mac Address. In this case, only one HSRP group is allowed.  For TokenRing interfaces, the following three MAC  addresses are permitted (functional addresses)\:              C0\:00\:00\:01\:00\:00              C0\:00\:00\:02\:00\:00              C0\:00\:00\:04\:00\:00
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: chsrpgrpentryrowstatus
            
            	The control that allows modification, creation, and deletion of entries.  For detailed rules see the DESCRIPTION for cHsrpGrpEntry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: chsrpgrpipnone
            
            	This object specifies the disable HSRP IPv4 virtual IP address
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-HSRP-MIB'
            _revision = '2010-09-06'

            def __init__(self):
                super(CISCOHSRPMIB.CHsrpGrpTable.CHsrpGrpEntry, self).__init__()

                self.yang_name = "cHsrpGrpEntry"
                self.yang_parent_name = "cHsrpGrpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','chsrpgrpnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('chsrpgrpnumber', (YLeaf(YType.uint32, 'cHsrpGrpNumber'), ['int'])),
                    ('chsrpgrpauth', (YLeaf(YType.str, 'cHsrpGrpAuth'), ['str'])),
                    ('chsrpgrppriority', (YLeaf(YType.uint32, 'cHsrpGrpPriority'), ['int'])),
                    ('chsrpgrppreempt', (YLeaf(YType.boolean, 'cHsrpGrpPreempt'), ['bool'])),
                    ('chsrpgrppreemptdelay', (YLeaf(YType.uint32, 'cHsrpGrpPreemptDelay'), ['int'])),
                    ('chsrpgrpuseconfiguredtimers', (YLeaf(YType.boolean, 'cHsrpGrpUseConfiguredTimers'), ['bool'])),
                    ('chsrpgrpconfiguredhellotime', (YLeaf(YType.uint32, 'cHsrpGrpConfiguredHelloTime'), ['int'])),
                    ('chsrpgrpconfiguredholdtime', (YLeaf(YType.uint32, 'cHsrpGrpConfiguredHoldTime'), ['int'])),
                    ('chsrpgrplearnedhellotime', (YLeaf(YType.uint32, 'cHsrpGrpLearnedHelloTime'), ['int'])),
                    ('chsrpgrplearnedholdtime', (YLeaf(YType.uint32, 'cHsrpGrpLearnedHoldTime'), ['int'])),
                    ('chsrpgrpvirtualipaddr', (YLeaf(YType.str, 'cHsrpGrpVirtualIpAddr'), ['str'])),
                    ('chsrpgrpuseconfigvirtualipaddr', (YLeaf(YType.boolean, 'cHsrpGrpUseConfigVirtualIpAddr'), ['bool'])),
                    ('chsrpgrpactiverouter', (YLeaf(YType.str, 'cHsrpGrpActiveRouter'), ['str'])),
                    ('chsrpgrpstandbyrouter', (YLeaf(YType.str, 'cHsrpGrpStandbyRouter'), ['str'])),
                    ('chsrpgrpstandbystate', (YLeaf(YType.enumeration, 'cHsrpGrpStandbyState'), [('ydk.models.cisco_ios_xe.CISCO_HSRP_MIB', 'HsrpState', '')])),
                    ('chsrpgrpvirtualmacaddr', (YLeaf(YType.str, 'cHsrpGrpVirtualMacAddr'), ['str'])),
                    ('chsrpgrpentryrowstatus', (YLeaf(YType.enumeration, 'cHsrpGrpEntryRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('chsrpgrpipnone', (YLeaf(YType.boolean, 'cHsrpGrpIpNone'), ['bool'])),
                ])
                self.ifindex = None
                self.chsrpgrpnumber = None
                self.chsrpgrpauth = None
                self.chsrpgrppriority = None
                self.chsrpgrppreempt = None
                self.chsrpgrppreemptdelay = None
                self.chsrpgrpuseconfiguredtimers = None
                self.chsrpgrpconfiguredhellotime = None
                self.chsrpgrpconfiguredholdtime = None
                self.chsrpgrplearnedhellotime = None
                self.chsrpgrplearnedholdtime = None
                self.chsrpgrpvirtualipaddr = None
                self.chsrpgrpuseconfigvirtualipaddr = None
                self.chsrpgrpactiverouter = None
                self.chsrpgrpstandbyrouter = None
                self.chsrpgrpstandbystate = None
                self.chsrpgrpvirtualmacaddr = None
                self.chsrpgrpentryrowstatus = None
                self.chsrpgrpipnone = None
                self._segment_path = lambda: "cHsrpGrpEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cHsrpGrpNumber='" + str(self.chsrpgrpnumber) + "']"
                self._absolute_path = lambda: "CISCO-HSRP-MIB:CISCO-HSRP-MIB/cHsrpGrpTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOHSRPMIB.CHsrpGrpTable.CHsrpGrpEntry, [u'ifindex', u'chsrpgrpnumber', u'chsrpgrpauth', u'chsrpgrppriority', u'chsrpgrppreempt', u'chsrpgrppreemptdelay', u'chsrpgrpuseconfiguredtimers', u'chsrpgrpconfiguredhellotime', u'chsrpgrpconfiguredholdtime', u'chsrpgrplearnedhellotime', u'chsrpgrplearnedholdtime', u'chsrpgrpvirtualipaddr', u'chsrpgrpuseconfigvirtualipaddr', u'chsrpgrpactiverouter', u'chsrpgrpstandbyrouter', u'chsrpgrpstandbystate', u'chsrpgrpvirtualmacaddr', u'chsrpgrpentryrowstatus', u'chsrpgrpipnone'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOHSRPMIB()
        return self._top_entity



