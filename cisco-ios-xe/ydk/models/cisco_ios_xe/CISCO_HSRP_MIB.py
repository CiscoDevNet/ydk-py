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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class HsrpstateEnum(Enum):
    """
    HsrpstateEnum

    The current state of the HSRP protocol for a given

    HSRP group entry.

    .. data:: initial = 1

    .. data:: learn = 2

    .. data:: listen = 3

    .. data:: speak = 4

    .. data:: standby = 5

    .. data:: active = 6

    """

    initial = 1

    learn = 2

    listen = 3

    speak = 4

    standby = 5

    active = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_MIB as meta
        return meta._meta_table['HsrpstateEnum']



class CiscoHsrpMib(object):
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
        self.chsrpglobalconfig = CiscoHsrpMib.Chsrpglobalconfig()
        self.chsrpglobalconfig.parent = self
        self.chsrpgrptable = CiscoHsrpMib.Chsrpgrptable()
        self.chsrpgrptable.parent = self


    class Chsrpglobalconfig(object):
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
            self.parent = None
            self.chsrpconfigtimeout = None

        @property
        def _common_path(self):

            return '/CISCO-HSRP-MIB:CISCO-HSRP-MIB/CISCO-HSRP-MIB:cHsrpGlobalConfig'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.chsrpconfigtimeout is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_MIB as meta
            return meta._meta_table['CiscoHsrpMib.Chsrpglobalconfig']['meta_info']


    class Chsrpgrptable(object):
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
            self.parent = None
            self.chsrpgrpentry = YList()
            self.chsrpgrpentry.parent = self
            self.chsrpgrpentry.name = 'chsrpgrpentry'


        class Chsrpgrpentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
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
            	**type**\:   :py:class:`HsrpstateEnum <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.HsrpstateEnum>`
            
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
                self.parent = None
                self.ifindex = None
                self.chsrpgrpnumber = None
                self.chsrpgrpactiverouter = None
                self.chsrpgrpauth = None
                self.chsrpgrpconfiguredhellotime = None
                self.chsrpgrpconfiguredholdtime = None
                self.chsrpgrpentryrowstatus = None
                self.chsrpgrpipnone = None
                self.chsrpgrplearnedhellotime = None
                self.chsrpgrplearnedholdtime = None
                self.chsrpgrppreempt = None
                self.chsrpgrppreemptdelay = None
                self.chsrpgrppriority = None
                self.chsrpgrpstandbyrouter = None
                self.chsrpgrpstandbystate = None
                self.chsrpgrpuseconfiguredtimers = None
                self.chsrpgrpuseconfigvirtualipaddr = None
                self.chsrpgrpvirtualipaddr = None
                self.chsrpgrpvirtualmacaddr = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.chsrpgrpnumber is None:
                    raise YPYModelError('Key property chsrpgrpnumber is None')

                return '/CISCO-HSRP-MIB:CISCO-HSRP-MIB/CISCO-HSRP-MIB:cHsrpGrpTable/CISCO-HSRP-MIB:cHsrpGrpEntry[CISCO-HSRP-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-HSRP-MIB:cHsrpGrpNumber = ' + str(self.chsrpgrpnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.chsrpgrpnumber is not None:
                    return True

                if self.chsrpgrpactiverouter is not None:
                    return True

                if self.chsrpgrpauth is not None:
                    return True

                if self.chsrpgrpconfiguredhellotime is not None:
                    return True

                if self.chsrpgrpconfiguredholdtime is not None:
                    return True

                if self.chsrpgrpentryrowstatus is not None:
                    return True

                if self.chsrpgrpipnone is not None:
                    return True

                if self.chsrpgrplearnedhellotime is not None:
                    return True

                if self.chsrpgrplearnedholdtime is not None:
                    return True

                if self.chsrpgrppreempt is not None:
                    return True

                if self.chsrpgrppreemptdelay is not None:
                    return True

                if self.chsrpgrppriority is not None:
                    return True

                if self.chsrpgrpstandbyrouter is not None:
                    return True

                if self.chsrpgrpstandbystate is not None:
                    return True

                if self.chsrpgrpuseconfiguredtimers is not None:
                    return True

                if self.chsrpgrpuseconfigvirtualipaddr is not None:
                    return True

                if self.chsrpgrpvirtualipaddr is not None:
                    return True

                if self.chsrpgrpvirtualmacaddr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_MIB as meta
                return meta._meta_table['CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-HSRP-MIB:CISCO-HSRP-MIB/CISCO-HSRP-MIB:cHsrpGrpTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.chsrpgrpentry is not None:
                for child_ref in self.chsrpgrpentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_MIB as meta
            return meta._meta_table['CiscoHsrpMib.Chsrpgrptable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-HSRP-MIB:CISCO-HSRP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.chsrpglobalconfig is not None and self.chsrpglobalconfig._has_data():
            return True

        if self.chsrpgrptable is not None and self.chsrpgrptable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_MIB as meta
        return meta._meta_table['CiscoHsrpMib']['meta_info']


