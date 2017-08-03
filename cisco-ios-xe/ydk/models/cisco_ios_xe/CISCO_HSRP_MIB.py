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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Hsrpstate(Enum):
    """
    Hsrpstate

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



class CiscoHsrpMib(Entity):
    """
    
    
    .. attribute:: chsrpglobalconfig
    
    	
    	**type**\:   :py:class:`Chsrpglobalconfig <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CiscoHsrpMib.Chsrpglobalconfig>`
    
    .. attribute:: chsrpgrptable
    
    	A table containing information on each HSRP group for each interface
    	**type**\:   :py:class:`Chsrpgrptable <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CiscoHsrpMib.Chsrpgrptable>`
    
    

    """

    _prefix = 'CISCO-HSRP-MIB'
    _revision = '2010-09-06'

    def __init__(self):
        super(CiscoHsrpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-HSRP-MIB"
        self.yang_parent_name = "CISCO-HSRP-MIB"

        self.chsrpglobalconfig = CiscoHsrpMib.Chsrpglobalconfig()
        self.chsrpglobalconfig.parent = self
        self._children_name_map["chsrpglobalconfig"] = "cHsrpGlobalConfig"
        self._children_yang_names.add("cHsrpGlobalConfig")

        self.chsrpgrptable = CiscoHsrpMib.Chsrpgrptable()
        self.chsrpgrptable.parent = self
        self._children_name_map["chsrpgrptable"] = "cHsrpGrpTable"
        self._children_yang_names.add("cHsrpGrpTable")


    class Chsrpglobalconfig(Entity):
        """
        
        
        .. attribute:: chsrpconfigtimeout
        
        	The amount of time in minutes a row in cHsrpGrpTable can remain in a state other than active before being timed out
        	**type**\:  int
        
        	**range:** 1..60
        
        	**units**\: minutes
        
        

        """

        _prefix = 'CISCO-HSRP-MIB'
        _revision = '2010-09-06'

        def __init__(self):
            super(CiscoHsrpMib.Chsrpglobalconfig, self).__init__()

            self.yang_name = "cHsrpGlobalConfig"
            self.yang_parent_name = "CISCO-HSRP-MIB"

            self.chsrpconfigtimeout = YLeaf(YType.uint32, "cHsrpConfigTimeout")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("chsrpconfigtimeout") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoHsrpMib.Chsrpglobalconfig, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoHsrpMib.Chsrpglobalconfig, self).__setattr__(name, value)

        def has_data(self):
            return self.chsrpconfigtimeout.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.chsrpconfigtimeout.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cHsrpGlobalConfig" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-HSRP-MIB:CISCO-HSRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.chsrpconfigtimeout.is_set or self.chsrpconfigtimeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.chsrpconfigtimeout.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cHsrpConfigTimeout"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cHsrpConfigTimeout"):
                self.chsrpconfigtimeout = value
                self.chsrpconfigtimeout.value_namespace = name_space
                self.chsrpconfigtimeout.value_namespace_prefix = name_space_prefix


    class Chsrpgrptable(Entity):
        """
        A table containing information on each HSRP group
        for each interface.
        
        .. attribute:: chsrpgrpentry
        
        	Information about an HSRP group. Management applications use cHsrpGrpRowStatus to control entry modification, creation and deletion.  Setting cHsrpGrpRowStatus to 'active' causes the router to communicate using HSRP.  The value of cHsrpGrpRowStatus may be set to 'destroy' at any time.  Entries may not be created via SNMP without explicitly  setting cHsrpGrpRowStatus to either 'createAndGo' or  'createAndWait'.  Entries can be created and modified via the management  protocol or by the device's local management interface.  A management application wishing to create an entry should choose the ifIndex of the interface which is to be added as part of an HSRP group. Also, a cHsrpGrpNumber should be chosen. A group number is unique only amongst the groups  on a particular interface. The value of the group number appears in packets which are transmitted and received on a  LAN segment to which the router is connected. The application must select the group number as explained in the description for cHsrpGrpNumber.  If the row is not active, and a local management interface command modifies that row, the row may transition to active state.  A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout  period can be changed by setting cHsrpConfigTimeout
        	**type**\: list of    :py:class:`Chsrpgrpentry <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-MIB'
        _revision = '2010-09-06'

        def __init__(self):
            super(CiscoHsrpMib.Chsrpgrptable, self).__init__()

            self.yang_name = "cHsrpGrpTable"
            self.yang_parent_name = "CISCO-HSRP-MIB"

            self.chsrpgrpentry = YList(self)

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
                        super(CiscoHsrpMib.Chsrpgrptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoHsrpMib.Chsrpgrptable, self).__setattr__(name, value)


        class Chsrpgrpentry(Entity):
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
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: chsrpgrpnumber  <key>
            
            	This object along with the ifIndex of a particular interface uniquely identifies an HSRP group.  Group numbers 0,1 and 2 are the only valid group numbers for TokenRing interfaces. For other media types, numbers range from 0 to 255. Each interface has its own set of group numbers. There's no relationship between the groups configured on different interfaces. Using a group number on one interface doesn't preclude using the same group number on a different interface. For example, there can be a group 1 on an Ethernet and a group 1 on Token Ring. More details can be found from RFC 2281
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: chsrpgrpactiverouter
            
            	Ip Address of the currently active router for this group
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: chsrpgrpauth
            
            	This is an unencrypted authentication string which is carried in all HSRP messages. An authentication string mismatch prevents a router interface from learning the designated IP address or HSRP timer values from other HSRP\-enabled routers with the same group number.  The function of this object is not to supply any sort of security\-like authentication but rather to confirm that what's happening is what's intended. In other words, this is meant for sanity checking only
            	**type**\:  str
            
            	**length:** 0..8
            
            .. attribute:: chsrpgrpconfiguredhellotime
            
            	If cHsrpGrpUseConfiguredTimers is true, cHsrpGrpConfiguredHelloTime is used when this router is an active router. Otherwise, the Hellotime learned from the current active router is used. All routers on a particular LAN segment must use the same Hellotime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: chsrpgrpconfiguredholdtime
            
            	If cHsrpGrpUseConfiguredTimers is true, cHsrpGrpConfiguredHoldTime is used when this router is an active router. Otherwise, the Holdtime learned from the current active router is used. All routers on a particular LAN segment should use the same Holdtime. Also, the Holdtime should be at least three times the value of the Hellotime and must be greater than the Hellotime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: chsrpgrpentryrowstatus
            
            	The control that allows modification, creation, and deletion of entries.  For detailed rules see the DESCRIPTION for cHsrpGrpEntry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: chsrpgrpipnone
            
            	This object specifies the disable HSRP IPv4 virtual IP address
            	**type**\:  bool
            
            .. attribute:: chsrpgrplearnedhellotime
            
            	If the Hellotime is not configured on a router, it can be learned from the Hello messages from active router, provided the Hello message is authenticated. If the Hellotime is not learned from a Hello message from the active router and it is not manually configured, a default value of 3 seconds is recommended
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: chsrpgrplearnedholdtime
            
            	If the Holdtime is not configured on a router, it can be learned from the Hello message from the active router. Holdtime should be learned only if the Hello message is authenticated. If the Holdtime is not learned and it is not manually configured, a default value of 10 seconds is  recommended
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: chsrpgrppreempt
            
            	This object, if TRUE, indicates that the current router should attempt to overthrow a lower priority active router and attempt to become the active router. If this object is FALSE, the router will become the active router only if there is no such router (or if an active router fails)
            	**type**\:  bool
            
            .. attribute:: chsrpgrppreemptdelay
            
            	This delay is the time difference between a router power up and the time it can actually start preempting the currently active router.  When a router first comes up, it doesn't have a complete routing table. If it's configured to preempt, then it will become the Active router, but it will not be able to provide adequate routing services. The solution to this is to allow for a configurable delay before the router actually preempts the currently active router
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**units**\: seconds
            
            .. attribute:: chsrpgrppriority
            
            	The cHsrpGrpPriority helps to select the active and the standby routers. The router with the highest priority is selected as the active router. In the priority range of 0 to 255, 0 is the lowest priority and 255 is the highest priority.  If two (or more) routers in a group have the same priority, the one with the highest ip address of the interface is the active router. When the active router fails to send a Hello message within a configurable period of time, the standby router with the highest priority becomes the active router.  A router with highest priority will only attempt to overthrow a lower priority active router if it is configured to preempt.  But, if there is more than one router which is not active, the highest priority non\-active router becomes the standby router
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: chsrpgrpstandbyrouter
            
            	Ip Address of the currently standby router for this group
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: chsrpgrpstandbystate
            
            	The current HSRP state of this group on this interface
            	**type**\:   :py:class:`Hsrpstate <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.Hsrpstate>`
            
            .. attribute:: chsrpgrpuseconfiguredtimers
            
            	HSRP routers learn a group's Hellotime or Holdtime from hello messages.  The Hellotime is used to determine the frequency of generating hello messages when this router becomes the active or standby router. The Holdtime is the interval between the receipt of a Hello message and the presumption that the sending router has failed.  If this object is TRUE, the cHsrpGrpConfiguredHelloTime and cHsrpGrpConfiguredHoldTime will be used. If it is FALSE, the Hellotime and Holdtime values are learned
            	**type**\:  bool
            
            .. attribute:: chsrpgrpuseconfigvirtualipaddr
            
            	If this object is TRUE, cHsrpGrpVirtualIpAddr was a configured one. Otherwise, it indicates that  cHsrpGrpVirtualIpAddr was a learned one
            	**type**\:  bool
            
            .. attribute:: chsrpgrpvirtualipaddr
            
            	This is the primary virtual IP address used by this group.  If this address is configured (i.e a non zero ip address), this value is used. Otherwise, the agent will attempt to discover the virtual address through a discovery process (which scans the hello messages)
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: chsrpgrpvirtualmacaddr
            
            	Mac Addresses used are as specified in RFC 2281. For ethernet and fddi interfaces, a MAC address will be in the range 00\:00\:0c\:07\:ac\:00 through 00\:00\:0c\:07\:ac\:ff. The last octet is the hexadecimal equivalent of cHsrpGrpNumber (0\-255).  Some Ethernet and FDDI interfaces allow a unicast MAC address for each HSRP group. Certain Ethernet chipsets(LANCE Ethernet, VGANYLAN and QUICC Ethernet) only support a single Unicast Mac Address. In this case, only one HSRP group is allowed.  For TokenRing interfaces, the following three MAC  addresses are permitted (functional addresses)\:              C0\:00\:00\:01\:00\:00              C0\:00\:00\:02\:00\:00              C0\:00\:00\:04\:00\:00
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            

            """

            _prefix = 'CISCO-HSRP-MIB'
            _revision = '2010-09-06'

            def __init__(self):
                super(CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry, self).__init__()

                self.yang_name = "cHsrpGrpEntry"
                self.yang_parent_name = "cHsrpGrpTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.chsrpgrpnumber = YLeaf(YType.uint32, "cHsrpGrpNumber")

                self.chsrpgrpactiverouter = YLeaf(YType.str, "cHsrpGrpActiveRouter")

                self.chsrpgrpauth = YLeaf(YType.str, "cHsrpGrpAuth")

                self.chsrpgrpconfiguredhellotime = YLeaf(YType.uint32, "cHsrpGrpConfiguredHelloTime")

                self.chsrpgrpconfiguredholdtime = YLeaf(YType.uint32, "cHsrpGrpConfiguredHoldTime")

                self.chsrpgrpentryrowstatus = YLeaf(YType.enumeration, "cHsrpGrpEntryRowStatus")

                self.chsrpgrpipnone = YLeaf(YType.boolean, "cHsrpGrpIpNone")

                self.chsrpgrplearnedhellotime = YLeaf(YType.uint32, "cHsrpGrpLearnedHelloTime")

                self.chsrpgrplearnedholdtime = YLeaf(YType.uint32, "cHsrpGrpLearnedHoldTime")

                self.chsrpgrppreempt = YLeaf(YType.boolean, "cHsrpGrpPreempt")

                self.chsrpgrppreemptdelay = YLeaf(YType.uint32, "cHsrpGrpPreemptDelay")

                self.chsrpgrppriority = YLeaf(YType.uint32, "cHsrpGrpPriority")

                self.chsrpgrpstandbyrouter = YLeaf(YType.str, "cHsrpGrpStandbyRouter")

                self.chsrpgrpstandbystate = YLeaf(YType.enumeration, "cHsrpGrpStandbyState")

                self.chsrpgrpuseconfiguredtimers = YLeaf(YType.boolean, "cHsrpGrpUseConfiguredTimers")

                self.chsrpgrpuseconfigvirtualipaddr = YLeaf(YType.boolean, "cHsrpGrpUseConfigVirtualIpAddr")

                self.chsrpgrpvirtualipaddr = YLeaf(YType.str, "cHsrpGrpVirtualIpAddr")

                self.chsrpgrpvirtualmacaddr = YLeaf(YType.str, "cHsrpGrpVirtualMacAddr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "chsrpgrpnumber",
                                "chsrpgrpactiverouter",
                                "chsrpgrpauth",
                                "chsrpgrpconfiguredhellotime",
                                "chsrpgrpconfiguredholdtime",
                                "chsrpgrpentryrowstatus",
                                "chsrpgrpipnone",
                                "chsrpgrplearnedhellotime",
                                "chsrpgrplearnedholdtime",
                                "chsrpgrppreempt",
                                "chsrpgrppreemptdelay",
                                "chsrpgrppriority",
                                "chsrpgrpstandbyrouter",
                                "chsrpgrpstandbystate",
                                "chsrpgrpuseconfiguredtimers",
                                "chsrpgrpuseconfigvirtualipaddr",
                                "chsrpgrpvirtualipaddr",
                                "chsrpgrpvirtualmacaddr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.chsrpgrpnumber.is_set or
                    self.chsrpgrpactiverouter.is_set or
                    self.chsrpgrpauth.is_set or
                    self.chsrpgrpconfiguredhellotime.is_set or
                    self.chsrpgrpconfiguredholdtime.is_set or
                    self.chsrpgrpentryrowstatus.is_set or
                    self.chsrpgrpipnone.is_set or
                    self.chsrpgrplearnedhellotime.is_set or
                    self.chsrpgrplearnedholdtime.is_set or
                    self.chsrpgrppreempt.is_set or
                    self.chsrpgrppreemptdelay.is_set or
                    self.chsrpgrppriority.is_set or
                    self.chsrpgrpstandbyrouter.is_set or
                    self.chsrpgrpstandbystate.is_set or
                    self.chsrpgrpuseconfiguredtimers.is_set or
                    self.chsrpgrpuseconfigvirtualipaddr.is_set or
                    self.chsrpgrpvirtualipaddr.is_set or
                    self.chsrpgrpvirtualmacaddr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.chsrpgrpnumber.yfilter != YFilter.not_set or
                    self.chsrpgrpactiverouter.yfilter != YFilter.not_set or
                    self.chsrpgrpauth.yfilter != YFilter.not_set or
                    self.chsrpgrpconfiguredhellotime.yfilter != YFilter.not_set or
                    self.chsrpgrpconfiguredholdtime.yfilter != YFilter.not_set or
                    self.chsrpgrpentryrowstatus.yfilter != YFilter.not_set or
                    self.chsrpgrpipnone.yfilter != YFilter.not_set or
                    self.chsrpgrplearnedhellotime.yfilter != YFilter.not_set or
                    self.chsrpgrplearnedholdtime.yfilter != YFilter.not_set or
                    self.chsrpgrppreempt.yfilter != YFilter.not_set or
                    self.chsrpgrppreemptdelay.yfilter != YFilter.not_set or
                    self.chsrpgrppriority.yfilter != YFilter.not_set or
                    self.chsrpgrpstandbyrouter.yfilter != YFilter.not_set or
                    self.chsrpgrpstandbystate.yfilter != YFilter.not_set or
                    self.chsrpgrpuseconfiguredtimers.yfilter != YFilter.not_set or
                    self.chsrpgrpuseconfigvirtualipaddr.yfilter != YFilter.not_set or
                    self.chsrpgrpvirtualipaddr.yfilter != YFilter.not_set or
                    self.chsrpgrpvirtualmacaddr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cHsrpGrpEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[cHsrpGrpNumber='" + self.chsrpgrpnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-HSRP-MIB:CISCO-HSRP-MIB/cHsrpGrpTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.chsrpgrpnumber.is_set or self.chsrpgrpnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpnumber.get_name_leafdata())
                if (self.chsrpgrpactiverouter.is_set or self.chsrpgrpactiverouter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpactiverouter.get_name_leafdata())
                if (self.chsrpgrpauth.is_set or self.chsrpgrpauth.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpauth.get_name_leafdata())
                if (self.chsrpgrpconfiguredhellotime.is_set or self.chsrpgrpconfiguredhellotime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpconfiguredhellotime.get_name_leafdata())
                if (self.chsrpgrpconfiguredholdtime.is_set or self.chsrpgrpconfiguredholdtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpconfiguredholdtime.get_name_leafdata())
                if (self.chsrpgrpentryrowstatus.is_set or self.chsrpgrpentryrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpentryrowstatus.get_name_leafdata())
                if (self.chsrpgrpipnone.is_set or self.chsrpgrpipnone.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpipnone.get_name_leafdata())
                if (self.chsrpgrplearnedhellotime.is_set or self.chsrpgrplearnedhellotime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrplearnedhellotime.get_name_leafdata())
                if (self.chsrpgrplearnedholdtime.is_set or self.chsrpgrplearnedholdtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrplearnedholdtime.get_name_leafdata())
                if (self.chsrpgrppreempt.is_set or self.chsrpgrppreempt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrppreempt.get_name_leafdata())
                if (self.chsrpgrppreemptdelay.is_set or self.chsrpgrppreemptdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrppreemptdelay.get_name_leafdata())
                if (self.chsrpgrppriority.is_set or self.chsrpgrppriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrppriority.get_name_leafdata())
                if (self.chsrpgrpstandbyrouter.is_set or self.chsrpgrpstandbyrouter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpstandbyrouter.get_name_leafdata())
                if (self.chsrpgrpstandbystate.is_set or self.chsrpgrpstandbystate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpstandbystate.get_name_leafdata())
                if (self.chsrpgrpuseconfiguredtimers.is_set or self.chsrpgrpuseconfiguredtimers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpuseconfiguredtimers.get_name_leafdata())
                if (self.chsrpgrpuseconfigvirtualipaddr.is_set or self.chsrpgrpuseconfigvirtualipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpuseconfigvirtualipaddr.get_name_leafdata())
                if (self.chsrpgrpvirtualipaddr.is_set or self.chsrpgrpvirtualipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpvirtualipaddr.get_name_leafdata())
                if (self.chsrpgrpvirtualmacaddr.is_set or self.chsrpgrpvirtualmacaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpvirtualmacaddr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cHsrpGrpNumber" or name == "cHsrpGrpActiveRouter" or name == "cHsrpGrpAuth" or name == "cHsrpGrpConfiguredHelloTime" or name == "cHsrpGrpConfiguredHoldTime" or name == "cHsrpGrpEntryRowStatus" or name == "cHsrpGrpIpNone" or name == "cHsrpGrpLearnedHelloTime" or name == "cHsrpGrpLearnedHoldTime" or name == "cHsrpGrpPreempt" or name == "cHsrpGrpPreemptDelay" or name == "cHsrpGrpPriority" or name == "cHsrpGrpStandbyRouter" or name == "cHsrpGrpStandbyState" or name == "cHsrpGrpUseConfiguredTimers" or name == "cHsrpGrpUseConfigVirtualIpAddr" or name == "cHsrpGrpVirtualIpAddr" or name == "cHsrpGrpVirtualMacAddr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpNumber"):
                    self.chsrpgrpnumber = value
                    self.chsrpgrpnumber.value_namespace = name_space
                    self.chsrpgrpnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpActiveRouter"):
                    self.chsrpgrpactiverouter = value
                    self.chsrpgrpactiverouter.value_namespace = name_space
                    self.chsrpgrpactiverouter.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpAuth"):
                    self.chsrpgrpauth = value
                    self.chsrpgrpauth.value_namespace = name_space
                    self.chsrpgrpauth.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpConfiguredHelloTime"):
                    self.chsrpgrpconfiguredhellotime = value
                    self.chsrpgrpconfiguredhellotime.value_namespace = name_space
                    self.chsrpgrpconfiguredhellotime.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpConfiguredHoldTime"):
                    self.chsrpgrpconfiguredholdtime = value
                    self.chsrpgrpconfiguredholdtime.value_namespace = name_space
                    self.chsrpgrpconfiguredholdtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpEntryRowStatus"):
                    self.chsrpgrpentryrowstatus = value
                    self.chsrpgrpentryrowstatus.value_namespace = name_space
                    self.chsrpgrpentryrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpIpNone"):
                    self.chsrpgrpipnone = value
                    self.chsrpgrpipnone.value_namespace = name_space
                    self.chsrpgrpipnone.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpLearnedHelloTime"):
                    self.chsrpgrplearnedhellotime = value
                    self.chsrpgrplearnedhellotime.value_namespace = name_space
                    self.chsrpgrplearnedhellotime.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpLearnedHoldTime"):
                    self.chsrpgrplearnedholdtime = value
                    self.chsrpgrplearnedholdtime.value_namespace = name_space
                    self.chsrpgrplearnedholdtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpPreempt"):
                    self.chsrpgrppreempt = value
                    self.chsrpgrppreempt.value_namespace = name_space
                    self.chsrpgrppreempt.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpPreemptDelay"):
                    self.chsrpgrppreemptdelay = value
                    self.chsrpgrppreemptdelay.value_namespace = name_space
                    self.chsrpgrppreemptdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpPriority"):
                    self.chsrpgrppriority = value
                    self.chsrpgrppriority.value_namespace = name_space
                    self.chsrpgrppriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpStandbyRouter"):
                    self.chsrpgrpstandbyrouter = value
                    self.chsrpgrpstandbyrouter.value_namespace = name_space
                    self.chsrpgrpstandbyrouter.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpStandbyState"):
                    self.chsrpgrpstandbystate = value
                    self.chsrpgrpstandbystate.value_namespace = name_space
                    self.chsrpgrpstandbystate.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpUseConfiguredTimers"):
                    self.chsrpgrpuseconfiguredtimers = value
                    self.chsrpgrpuseconfiguredtimers.value_namespace = name_space
                    self.chsrpgrpuseconfiguredtimers.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpUseConfigVirtualIpAddr"):
                    self.chsrpgrpuseconfigvirtualipaddr = value
                    self.chsrpgrpuseconfigvirtualipaddr.value_namespace = name_space
                    self.chsrpgrpuseconfigvirtualipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpVirtualIpAddr"):
                    self.chsrpgrpvirtualipaddr = value
                    self.chsrpgrpvirtualipaddr.value_namespace = name_space
                    self.chsrpgrpvirtualipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpVirtualMacAddr"):
                    self.chsrpgrpvirtualmacaddr = value
                    self.chsrpgrpvirtualmacaddr.value_namespace = name_space
                    self.chsrpgrpvirtualmacaddr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.chsrpgrpentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.chsrpgrpentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cHsrpGrpTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-HSRP-MIB:CISCO-HSRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cHsrpGrpEntry"):
                for c in self.chsrpgrpentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.chsrpgrpentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cHsrpGrpEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.chsrpglobalconfig is not None and self.chsrpglobalconfig.has_data()) or
            (self.chsrpgrptable is not None and self.chsrpgrptable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.chsrpglobalconfig is not None and self.chsrpglobalconfig.has_operation()) or
            (self.chsrpgrptable is not None and self.chsrpgrptable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-HSRP-MIB:CISCO-HSRP-MIB" + path_buffer

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

        if (child_yang_name == "cHsrpGlobalConfig"):
            if (self.chsrpglobalconfig is None):
                self.chsrpglobalconfig = CiscoHsrpMib.Chsrpglobalconfig()
                self.chsrpglobalconfig.parent = self
                self._children_name_map["chsrpglobalconfig"] = "cHsrpGlobalConfig"
            return self.chsrpglobalconfig

        if (child_yang_name == "cHsrpGrpTable"):
            if (self.chsrpgrptable is None):
                self.chsrpgrptable = CiscoHsrpMib.Chsrpgrptable()
                self.chsrpgrptable.parent = self
                self._children_name_map["chsrpgrptable"] = "cHsrpGrpTable"
            return self.chsrpgrptable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cHsrpGlobalConfig" or name == "cHsrpGrpTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoHsrpMib()
        return self._top_entity

