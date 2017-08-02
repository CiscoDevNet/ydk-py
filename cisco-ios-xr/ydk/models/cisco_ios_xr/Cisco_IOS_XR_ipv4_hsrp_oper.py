""" Cisco_IOS_XR_ipv4_hsrp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-hsrp package operational data.

This module contains definitions
for the following management objects\:
  hsrp\: HSRP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class HsrpBAf(Enum):
    """
    HsrpBAf

    Hsrp b af

    .. data:: ipv4 = 0

    	IPv4 Address Family

    .. data:: ipv6 = 1

    	IPv6 Address Family

    .. data:: count = 2

    	The number of supported address families

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")

    count = Enum.YLeaf(2, "count")


class HsrpBfdSessionState(Enum):
    """
    HsrpBfdSessionState

    Hsrp bfd session state

    .. data:: bfd_state_none = 0

    	None

    .. data:: bfd_state_inactive = 1

    	Inactive

    .. data:: bfd_state_up = 2

    	Up

    .. data:: bfd_state_down = 3

    	Down

    """

    bfd_state_none = Enum.YLeaf(0, "bfd-state-none")

    bfd_state_inactive = Enum.YLeaf(1, "bfd-state-inactive")

    bfd_state_up = Enum.YLeaf(2, "bfd-state-up")

    bfd_state_down = Enum.YLeaf(3, "bfd-state-down")


class HsrpStateChangeReason(Enum):
    """
    HsrpStateChangeReason

    Hsrp state change reason

    .. data:: state_change_bfd_down = 0

    	BFD session down

    .. data:: state_change_vip_learnt = 1

    	Virtual IP learnt

    .. data:: state_change_interface_ip = 2

    	Interface IP update

    .. data:: state_change_delay_timer = 3

    	Delay timer expired

    .. data:: state_change_startup = 4

    	Ready on startup

    .. data:: state_change_shutdown = 5

    	HSRP shut down

    .. data:: state_change_interface_up = 6

    	Interface Up update

    .. data:: state_change_interface_down = 7

    	Interface Down update

    .. data:: state_change_active_timer = 8

    	Active timer expired

    .. data:: state_change_standby_timer = 9

    	Standby timer expired

    .. data:: state_change_resign = 10

    	Resign received

    .. data:: state_change_coup = 11

    	Coup received

    .. data:: state_change_higher_priority_speak = 12

    	Higher priority speak received

    .. data:: state_change_higher_priority_standby = 13

    	Higher priority standby received

    .. data:: state_change_lower_priority_standby = 14

    	Lower priority standby received

    .. data:: state_change_higher_priority_active = 15

    	Higher priority active received

    .. data:: state_change_lower_priority_active = 16

    	Lower priority active received

    .. data:: state_change_virtual_ip_configured = 17

    	Virtual IP configured

    .. data:: state_change_virtual_ip_lost = 18

    	Virtual IP lost

    .. data:: state_change_recovered_from_checkpoint = 19

    	Recovered from checkpoint

    .. data:: state_change_mac_update = 20

    	MAC address update

    .. data:: state_change_admin = 21

    	Forwarder Admin state change

    .. data:: state_change_parent = 22

    	MGO parent change

    .. data:: state_change_chkpt_update = 23

    	Checkpoint update from Primary HSRP instance

    .. data:: state_change_issu_resync = 24

    	Resync following ISSU primary event

    .. data:: state_change_max = 25

    	Maximum reason in enumeration

    """

    state_change_bfd_down = Enum.YLeaf(0, "state-change-bfd-down")

    state_change_vip_learnt = Enum.YLeaf(1, "state-change-vip-learnt")

    state_change_interface_ip = Enum.YLeaf(2, "state-change-interface-ip")

    state_change_delay_timer = Enum.YLeaf(3, "state-change-delay-timer")

    state_change_startup = Enum.YLeaf(4, "state-change-startup")

    state_change_shutdown = Enum.YLeaf(5, "state-change-shutdown")

    state_change_interface_up = Enum.YLeaf(6, "state-change-interface-up")

    state_change_interface_down = Enum.YLeaf(7, "state-change-interface-down")

    state_change_active_timer = Enum.YLeaf(8, "state-change-active-timer")

    state_change_standby_timer = Enum.YLeaf(9, "state-change-standby-timer")

    state_change_resign = Enum.YLeaf(10, "state-change-resign")

    state_change_coup = Enum.YLeaf(11, "state-change-coup")

    state_change_higher_priority_speak = Enum.YLeaf(12, "state-change-higher-priority-speak")

    state_change_higher_priority_standby = Enum.YLeaf(13, "state-change-higher-priority-standby")

    state_change_lower_priority_standby = Enum.YLeaf(14, "state-change-lower-priority-standby")

    state_change_higher_priority_active = Enum.YLeaf(15, "state-change-higher-priority-active")

    state_change_lower_priority_active = Enum.YLeaf(16, "state-change-lower-priority-active")

    state_change_virtual_ip_configured = Enum.YLeaf(17, "state-change-virtual-ip-configured")

    state_change_virtual_ip_lost = Enum.YLeaf(18, "state-change-virtual-ip-lost")

    state_change_recovered_from_checkpoint = Enum.YLeaf(19, "state-change-recovered-from-checkpoint")

    state_change_mac_update = Enum.YLeaf(20, "state-change-mac-update")

    state_change_admin = Enum.YLeaf(21, "state-change-admin")

    state_change_parent = Enum.YLeaf(22, "state-change-parent")

    state_change_chkpt_update = Enum.YLeaf(23, "state-change-chkpt-update")

    state_change_issu_resync = Enum.YLeaf(24, "state-change-issu-resync")

    state_change_max = Enum.YLeaf(25, "state-change-max")


class HsrpVmacState(Enum):
    """
    HsrpVmacState

    Hsrp vmac state

    .. data:: stored = 0

    	VMAC stored locally

    .. data:: reserved = 1

    	VMAC reserved in mac table

    .. data:: active = 2

    	VMAC active in mac table

    .. data:: reserving = 3

    	VMAC not yet reserved in mac table

    """

    stored = Enum.YLeaf(0, "stored")

    reserved = Enum.YLeaf(1, "reserved")

    active = Enum.YLeaf(2, "active")

    reserving = Enum.YLeaf(3, "reserving")


class StandbyGrpState(Enum):
    """
    StandbyGrpState

    Standby grp state

    .. data:: state_initial = 1

    	Initial

    .. data:: state_learn = 2

    	Learn

    .. data:: state_listen = 3

    	Listen

    .. data:: state_speak = 4

    	Speak

    .. data:: state_standby = 5

    	Standby

    .. data:: state_active = 6

    	Active

    """

    state_initial = Enum.YLeaf(1, "state-initial")

    state_learn = Enum.YLeaf(2, "state-learn")

    state_listen = Enum.YLeaf(3, "state-listen")

    state_speak = Enum.YLeaf(4, "state-speak")

    state_standby = Enum.YLeaf(5, "state-standby")

    state_active = Enum.YLeaf(6, "state-active")



class Hsrp(Entity):
    """
    HSRP operational data
    
    .. attribute:: bfd_sessions
    
    	The table of HSRP BFD Sessions
    	**type**\:   :py:class:`BfdSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.BfdSessions>`
    
    .. attribute:: ipv4
    
    	IPv4 HSRP information
    	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4>`
    
    .. attribute:: ipv6
    
    	IPv6 HSRP information
    	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6>`
    
    .. attribute:: mgo_sessions
    
    	HSRP MGO session table
    	**type**\:   :py:class:`MgoSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.MgoSessions>`
    
    .. attribute:: summary
    
    	HSRP summary statistics
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Summary>`
    
    

    """

    _prefix = 'ipv4-hsrp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Hsrp, self).__init__()
        self._top_entity = None

        self.yang_name = "hsrp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-hsrp-oper"

        self.bfd_sessions = Hsrp.BfdSessions()
        self.bfd_sessions.parent = self
        self._children_name_map["bfd_sessions"] = "bfd-sessions"
        self._children_yang_names.add("bfd-sessions")

        self.ipv4 = Hsrp.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"
        self._children_yang_names.add("ipv4")

        self.ipv6 = Hsrp.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"
        self._children_yang_names.add("ipv6")

        self.mgo_sessions = Hsrp.MgoSessions()
        self.mgo_sessions.parent = self
        self._children_name_map["mgo_sessions"] = "mgo-sessions"
        self._children_yang_names.add("mgo-sessions")

        self.summary = Hsrp.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")


    class Ipv4(Entity):
        """
        IPv4 HSRP information
        
        .. attribute:: groups
        
        	The HSRP standby group table
        	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups>`
        
        .. attribute:: interfaces
        
        	The HSRP interface information table
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Interfaces>`
        
        .. attribute:: tracked_interfaces
        
        	The HSRP tracked interfaces table
        	**type**\:   :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.TrackedInterfaces>`
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "hsrp"

            self.groups = Hsrp.Ipv4.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._children_yang_names.add("groups")

            self.interfaces = Hsrp.Ipv4.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.tracked_interfaces = Hsrp.Ipv4.TrackedInterfaces()
            self.tracked_interfaces.parent = self
            self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
            self._children_yang_names.add("tracked-interfaces")


        class Groups(Entity):
            """
            The HSRP standby group table
            
            .. attribute:: group
            
            	An HSRP standby group
            	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv4.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "ipv4"

                self.group = YList(self)

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
                            super(Hsrp.Ipv4.Groups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Hsrp.Ipv4.Groups, self).__setattr__(name, value)


            class Group(Entity):
                """
                An HSRP standby group
                
                .. attribute:: interface_name  <key>
                
                	The interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: group_number  <key>
                
                	The HSRP group number
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: active_ip_address
                
                	Active router's IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: active_ipv6_address
                
                	Active router's IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: active_mac_address
                
                	Active router's interface MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: active_priority
                
                	Priority of the Active router
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: active_timer_flag
                
                	Active timer running flag
                	**type**\:  bool
                
                .. attribute:: active_timer_msecs
                
                	Active timer running time msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: active_timer_secs
                
                	Active timer running time secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:   :py:class:`HsrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAf>`
                
                .. attribute:: authentication_string
                
                	Authentication string
                	**type**\:  str
                
                	**length:** 0..9
                
                .. attribute:: bfd_enabled
                
                	HSRP BFD fast failover
                	**type**\:  bool
                
                .. attribute:: bfd_interface
                
                	BFD Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: bfd_interval
                
                	BFD packet send interval
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_multiplier
                
                	BFD multiplier
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_peer_ip_address
                
                	BFD Peer IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_peer_ipv6_address
                
                	BFD Peer IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_session_state
                
                	BFD session state
                	**type**\:   :py:class:`HsrpBfdSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBfdSessionState>`
                
                .. attribute:: configured_mac_address
                
                	MAC address configured
                	**type**\:  bool
                
                .. attribute:: configured_priority
                
                	Configured priority
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: configured_timers
                
                	Non\-default timers are configured
                	**type**\:  bool
                
                .. attribute:: coup_received_time
                
                	Time last coup was received
                	**type**\:   :py:class:`CoupReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.CoupReceivedTime>`
                
                .. attribute:: coup_sent_time
                
                	Time last coup was sent
                	**type**\:   :py:class:`CoupSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.CoupSentTime>`
                
                .. attribute:: current_state_timer_secs
                
                	Time in current state secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: delay_timer_flag
                
                	Delay timer running flag
                	**type**\:  bool
                
                .. attribute:: delay_timer_msecs
                
                	Delay timer running time msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: delay_timer_secs
                
                	Delay timer running time secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: followed_session_name
                
                	Followed Session Name
                	**type**\:  str
                
                	**length:** 0..16
                
                .. attribute:: global_address
                
                	Global virtual IPv6 addresses
                	**type**\: list of    :py:class:`GlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.GlobalAddress>`
                
                .. attribute:: hello_time
                
                	Hellotime in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: hello_timer_flag
                
                	Hello timer running flag
                	**type**\:  bool
                
                .. attribute:: hello_timer_msecs
                
                	Hello timer running time msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: hello_timer_secs
                
                	Hello timer running time secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: hold_time
                
                	Holdtime in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: hsrp_group_number
                
                	HSRP Group number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hsrp_router_state
                
                	HSRP router state
                	**type**\:   :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_name_xr
                
                	Interface Name
                	**type**\:  str
                
                	**length:** 0..64
                
                .. attribute:: is_slave
                
                	Group is a slave group
                	**type**\:  bool
                
                .. attribute:: learned_hello_time
                
                	Learned hellotime in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: learned_hold_time
                
                	Learned holdtime in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: min_delay_time
                
                	Minimum delay time in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: preempt_delay
                
                	Preempt delay time in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: preempt_enabled
                
                	Preempt enabled
                	**type**\:  bool
                
                .. attribute:: preempt_timer_secs
                
                	Preempt time remaining in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: redirects_disabled
                
                	HSRP redirects disabled
                	**type**\:  bool
                
                .. attribute:: reload_delay_time
                
                	Reload delay time in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: resign_received_time
                
                	Time last resign was received
                	**type**\:   :py:class:`ResignReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.ResignReceivedTime>`
                
                .. attribute:: resign_sent_time
                
                	Time last resign was sent
                	**type**\:   :py:class:`ResignSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.ResignSentTime>`
                
                .. attribute:: router_priority
                
                	Priority of the router
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: secondary_address
                
                	Secondary virtual IP addresses
                	**type**\:  list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: session_name
                
                	Session Name
                	**type**\:  str
                
                	**length:** 0..16
                
                .. attribute:: slaves
                
                	Number of slaves following state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_ip_address
                
                	Standby router's IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: standby_ipv6_address
                
                	Standby router's IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: standby_mac_address
                
                	Standby router's interface MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: standby_timer_flag
                
                	Standby timer running flag
                	**type**\:  bool
                
                .. attribute:: standby_timer_msecs
                
                	Standby timer running time msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: standby_timer_secs
                
                	Standby timer running time secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: state_change_count
                
                	Number of state changes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_change_history
                
                	State change history
                	**type**\: list of    :py:class:`StateChangeHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.StateChangeHistory>`
                
                .. attribute:: statistics
                
                	HSRP Group statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.Statistics>`
                
                .. attribute:: tracked_interface_count
                
                	Number of tracked interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_up_count
                
                	Number of tracked interfaces up
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: use_bia_configured
                
                	Use burnt in MAC address configured
                	**type**\:  bool
                
                .. attribute:: use_configured_timers
                
                	Use configured timers
                	**type**\:  bool
                
                .. attribute:: use_configured_virtual_ip
                
                	Use configured virtual IP
                	**type**\:  bool
                
                .. attribute:: version
                
                	HSRP Protocol Version
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: virtual_ip_address
                
                	Configured Virtual IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtual_linklocal_ipv6_address
                
                	Virtual linklocal IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtual_mac_address
                
                	Virtual mac address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: virtual_mac_address_state
                
                	Virtual mac address state
                	**type**\:   :py:class:`HsrpVmacState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpVmacState>`
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv4.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.group_number = YLeaf(YType.int32, "group-number")

                    self.active_ip_address = YLeaf(YType.str, "active-ip-address")

                    self.active_ipv6_address = YLeaf(YType.str, "active-ipv6-address")

                    self.active_mac_address = YLeaf(YType.str, "active-mac-address")

                    self.active_priority = YLeaf(YType.uint8, "active-priority")

                    self.active_timer_flag = YLeaf(YType.boolean, "active-timer-flag")

                    self.active_timer_msecs = YLeaf(YType.uint32, "active-timer-msecs")

                    self.active_timer_secs = YLeaf(YType.uint32, "active-timer-secs")

                    self.address_family = YLeaf(YType.enumeration, "address-family")

                    self.authentication_string = YLeaf(YType.str, "authentication-string")

                    self.bfd_enabled = YLeaf(YType.boolean, "bfd-enabled")

                    self.bfd_interface = YLeaf(YType.str, "bfd-interface")

                    self.bfd_interval = YLeaf(YType.uint32, "bfd-interval")

                    self.bfd_multiplier = YLeaf(YType.uint32, "bfd-multiplier")

                    self.bfd_peer_ip_address = YLeaf(YType.str, "bfd-peer-ip-address")

                    self.bfd_peer_ipv6_address = YLeaf(YType.str, "bfd-peer-ipv6-address")

                    self.bfd_session_state = YLeaf(YType.enumeration, "bfd-session-state")

                    self.configured_mac_address = YLeaf(YType.boolean, "configured-mac-address")

                    self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                    self.configured_timers = YLeaf(YType.boolean, "configured-timers")

                    self.current_state_timer_secs = YLeaf(YType.uint32, "current-state-timer-secs")

                    self.delay_timer_flag = YLeaf(YType.boolean, "delay-timer-flag")

                    self.delay_timer_msecs = YLeaf(YType.uint32, "delay-timer-msecs")

                    self.delay_timer_secs = YLeaf(YType.uint32, "delay-timer-secs")

                    self.followed_session_name = YLeaf(YType.str, "followed-session-name")

                    self.hello_time = YLeaf(YType.uint32, "hello-time")

                    self.hello_timer_flag = YLeaf(YType.boolean, "hello-timer-flag")

                    self.hello_timer_msecs = YLeaf(YType.uint32, "hello-timer-msecs")

                    self.hello_timer_secs = YLeaf(YType.uint32, "hello-timer-secs")

                    self.hold_time = YLeaf(YType.uint32, "hold-time")

                    self.hsrp_group_number = YLeaf(YType.uint32, "hsrp-group-number")

                    self.hsrp_router_state = YLeaf(YType.enumeration, "hsrp-router-state")

                    self.interface = YLeaf(YType.str, "interface")

                    self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                    self.is_slave = YLeaf(YType.boolean, "is-slave")

                    self.learned_hello_time = YLeaf(YType.uint32, "learned-hello-time")

                    self.learned_hold_time = YLeaf(YType.uint32, "learned-hold-time")

                    self.min_delay_time = YLeaf(YType.uint32, "min-delay-time")

                    self.preempt_delay = YLeaf(YType.uint32, "preempt-delay")

                    self.preempt_enabled = YLeaf(YType.boolean, "preempt-enabled")

                    self.preempt_timer_secs = YLeaf(YType.uint32, "preempt-timer-secs")

                    self.redirects_disabled = YLeaf(YType.boolean, "redirects-disabled")

                    self.reload_delay_time = YLeaf(YType.uint32, "reload-delay-time")

                    self.router_priority = YLeaf(YType.uint8, "router-priority")

                    self.secondary_address = YLeafList(YType.str, "secondary-address")

                    self.session_name = YLeaf(YType.str, "session-name")

                    self.slaves = YLeaf(YType.uint32, "slaves")

                    self.standby_ip_address = YLeaf(YType.str, "standby-ip-address")

                    self.standby_ipv6_address = YLeaf(YType.str, "standby-ipv6-address")

                    self.standby_mac_address = YLeaf(YType.str, "standby-mac-address")

                    self.standby_timer_flag = YLeaf(YType.boolean, "standby-timer-flag")

                    self.standby_timer_msecs = YLeaf(YType.uint32, "standby-timer-msecs")

                    self.standby_timer_secs = YLeaf(YType.uint32, "standby-timer-secs")

                    self.state_change_count = YLeaf(YType.uint32, "state-change-count")

                    self.tracked_interface_count = YLeaf(YType.uint32, "tracked-interface-count")

                    self.tracked_interface_up_count = YLeaf(YType.uint32, "tracked-interface-up-count")

                    self.use_bia_configured = YLeaf(YType.boolean, "use-bia-configured")

                    self.use_configured_timers = YLeaf(YType.boolean, "use-configured-timers")

                    self.use_configured_virtual_ip = YLeaf(YType.boolean, "use-configured-virtual-ip")

                    self.version = YLeaf(YType.uint8, "version")

                    self.virtual_ip_address = YLeaf(YType.str, "virtual-ip-address")

                    self.virtual_linklocal_ipv6_address = YLeaf(YType.str, "virtual-linklocal-ipv6-address")

                    self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                    self.virtual_mac_address_state = YLeaf(YType.enumeration, "virtual-mac-address-state")

                    self.coup_received_time = Hsrp.Ipv4.Groups.Group.CoupReceivedTime()
                    self.coup_received_time.parent = self
                    self._children_name_map["coup_received_time"] = "coup-received-time"
                    self._children_yang_names.add("coup-received-time")

                    self.coup_sent_time = Hsrp.Ipv4.Groups.Group.CoupSentTime()
                    self.coup_sent_time.parent = self
                    self._children_name_map["coup_sent_time"] = "coup-sent-time"
                    self._children_yang_names.add("coup-sent-time")

                    self.resign_received_time = Hsrp.Ipv4.Groups.Group.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self._children_name_map["resign_received_time"] = "resign-received-time"
                    self._children_yang_names.add("resign-received-time")

                    self.resign_sent_time = Hsrp.Ipv4.Groups.Group.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self._children_name_map["resign_sent_time"] = "resign-sent-time"
                    self._children_yang_names.add("resign-sent-time")

                    self.statistics = Hsrp.Ipv4.Groups.Group.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")

                    self.global_address = YList(self)
                    self.state_change_history = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "group_number",
                                    "active_ip_address",
                                    "active_ipv6_address",
                                    "active_mac_address",
                                    "active_priority",
                                    "active_timer_flag",
                                    "active_timer_msecs",
                                    "active_timer_secs",
                                    "address_family",
                                    "authentication_string",
                                    "bfd_enabled",
                                    "bfd_interface",
                                    "bfd_interval",
                                    "bfd_multiplier",
                                    "bfd_peer_ip_address",
                                    "bfd_peer_ipv6_address",
                                    "bfd_session_state",
                                    "configured_mac_address",
                                    "configured_priority",
                                    "configured_timers",
                                    "current_state_timer_secs",
                                    "delay_timer_flag",
                                    "delay_timer_msecs",
                                    "delay_timer_secs",
                                    "followed_session_name",
                                    "hello_time",
                                    "hello_timer_flag",
                                    "hello_timer_msecs",
                                    "hello_timer_secs",
                                    "hold_time",
                                    "hsrp_group_number",
                                    "hsrp_router_state",
                                    "interface",
                                    "interface_name_xr",
                                    "is_slave",
                                    "learned_hello_time",
                                    "learned_hold_time",
                                    "min_delay_time",
                                    "preempt_delay",
                                    "preempt_enabled",
                                    "preempt_timer_secs",
                                    "redirects_disabled",
                                    "reload_delay_time",
                                    "router_priority",
                                    "secondary_address",
                                    "session_name",
                                    "slaves",
                                    "standby_ip_address",
                                    "standby_ipv6_address",
                                    "standby_mac_address",
                                    "standby_timer_flag",
                                    "standby_timer_msecs",
                                    "standby_timer_secs",
                                    "state_change_count",
                                    "tracked_interface_count",
                                    "tracked_interface_up_count",
                                    "use_bia_configured",
                                    "use_configured_timers",
                                    "use_configured_virtual_ip",
                                    "version",
                                    "virtual_ip_address",
                                    "virtual_linklocal_ipv6_address",
                                    "virtual_mac_address",
                                    "virtual_mac_address_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Hsrp.Ipv4.Groups.Group, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Hsrp.Ipv4.Groups.Group, self).__setattr__(name, value)


                class ResignSentTime(Entity):
                    """
                    Time last resign was sent
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.ResignSentTime, self).__init__()

                        self.yang_name = "resign-sent-time"
                        self.yang_parent_name = "group"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv4.Groups.Group.ResignSentTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv4.Groups.Group.ResignSentTime, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "resign-sent-time" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix


                class ResignReceivedTime(Entity):
                    """
                    Time last resign was received
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.ResignReceivedTime, self).__init__()

                        self.yang_name = "resign-received-time"
                        self.yang_parent_name = "group"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv4.Groups.Group.ResignReceivedTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv4.Groups.Group.ResignReceivedTime, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "resign-received-time" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix


                class CoupSentTime(Entity):
                    """
                    Time last coup was sent
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.CoupSentTime, self).__init__()

                        self.yang_name = "coup-sent-time"
                        self.yang_parent_name = "group"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv4.Groups.Group.CoupSentTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv4.Groups.Group.CoupSentTime, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "coup-sent-time" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix


                class CoupReceivedTime(Entity):
                    """
                    Time last coup was received
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.CoupReceivedTime, self).__init__()

                        self.yang_name = "coup-received-time"
                        self.yang_parent_name = "group"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv4.Groups.Group.CoupReceivedTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv4.Groups.Group.CoupReceivedTime, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "coup-received-time" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix


                class Statistics(Entity):
                    """
                    HSRP Group statistics
                    
                    .. attribute:: active_transitions
                    
                    	Number of transitions to Active State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: auth_fail_received
                    
                    	Number of Packets received that failed authentication
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coup_packets_received
                    
                    	Number of Coup Packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coup_packets_sent
                    
                    	Number of Coup Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hello_packets_received
                    
                    	Number of Hello Packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hello_packets_sent
                    
                    	Number of Hello Packets sent (NB\: Bundles only)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: init_transitions
                    
                    	Number of transitions to Init State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_timer_received
                    
                    	Number of packets received with invalid Hello Time value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: learn_transitions
                    
                    	Number of transitions to Learn State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: listen_transitions
                    
                    	Number of transitions to Listen State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mismatch_virtual_ip_address_received
                    
                    	Number of packets received with mismatching virtual IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resign_packets_received
                    
                    	Number of Resign Packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resign_packets_sent
                    
                    	Number of Resign Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: speak_transitions
                    
                    	Number of transitions to Speak State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: standby_transitions
                    
                    	Number of transitions to Standby State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "group"

                        self.active_transitions = YLeaf(YType.uint32, "active-transitions")

                        self.auth_fail_received = YLeaf(YType.uint32, "auth-fail-received")

                        self.coup_packets_received = YLeaf(YType.uint32, "coup-packets-received")

                        self.coup_packets_sent = YLeaf(YType.uint32, "coup-packets-sent")

                        self.hello_packets_received = YLeaf(YType.uint32, "hello-packets-received")

                        self.hello_packets_sent = YLeaf(YType.uint32, "hello-packets-sent")

                        self.init_transitions = YLeaf(YType.uint32, "init-transitions")

                        self.invalid_timer_received = YLeaf(YType.uint32, "invalid-timer-received")

                        self.learn_transitions = YLeaf(YType.uint32, "learn-transitions")

                        self.listen_transitions = YLeaf(YType.uint32, "listen-transitions")

                        self.mismatch_virtual_ip_address_received = YLeaf(YType.uint32, "mismatch-virtual-ip-address-received")

                        self.resign_packets_received = YLeaf(YType.uint32, "resign-packets-received")

                        self.resign_packets_sent = YLeaf(YType.uint32, "resign-packets-sent")

                        self.speak_transitions = YLeaf(YType.uint32, "speak-transitions")

                        self.standby_transitions = YLeaf(YType.uint32, "standby-transitions")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("active_transitions",
                                        "auth_fail_received",
                                        "coup_packets_received",
                                        "coup_packets_sent",
                                        "hello_packets_received",
                                        "hello_packets_sent",
                                        "init_transitions",
                                        "invalid_timer_received",
                                        "learn_transitions",
                                        "listen_transitions",
                                        "mismatch_virtual_ip_address_received",
                                        "resign_packets_received",
                                        "resign_packets_sent",
                                        "speak_transitions",
                                        "standby_transitions") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv4.Groups.Group.Statistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv4.Groups.Group.Statistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.active_transitions.is_set or
                            self.auth_fail_received.is_set or
                            self.coup_packets_received.is_set or
                            self.coup_packets_sent.is_set or
                            self.hello_packets_received.is_set or
                            self.hello_packets_sent.is_set or
                            self.init_transitions.is_set or
                            self.invalid_timer_received.is_set or
                            self.learn_transitions.is_set or
                            self.listen_transitions.is_set or
                            self.mismatch_virtual_ip_address_received.is_set or
                            self.resign_packets_received.is_set or
                            self.resign_packets_sent.is_set or
                            self.speak_transitions.is_set or
                            self.standby_transitions.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.active_transitions.yfilter != YFilter.not_set or
                            self.auth_fail_received.yfilter != YFilter.not_set or
                            self.coup_packets_received.yfilter != YFilter.not_set or
                            self.coup_packets_sent.yfilter != YFilter.not_set or
                            self.hello_packets_received.yfilter != YFilter.not_set or
                            self.hello_packets_sent.yfilter != YFilter.not_set or
                            self.init_transitions.yfilter != YFilter.not_set or
                            self.invalid_timer_received.yfilter != YFilter.not_set or
                            self.learn_transitions.yfilter != YFilter.not_set or
                            self.listen_transitions.yfilter != YFilter.not_set or
                            self.mismatch_virtual_ip_address_received.yfilter != YFilter.not_set or
                            self.resign_packets_received.yfilter != YFilter.not_set or
                            self.resign_packets_sent.yfilter != YFilter.not_set or
                            self.speak_transitions.yfilter != YFilter.not_set or
                            self.standby_transitions.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.active_transitions.is_set or self.active_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_transitions.get_name_leafdata())
                        if (self.auth_fail_received.is_set or self.auth_fail_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_fail_received.get_name_leafdata())
                        if (self.coup_packets_received.is_set or self.coup_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.coup_packets_received.get_name_leafdata())
                        if (self.coup_packets_sent.is_set or self.coup_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.coup_packets_sent.get_name_leafdata())
                        if (self.hello_packets_received.is_set or self.hello_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hello_packets_received.get_name_leafdata())
                        if (self.hello_packets_sent.is_set or self.hello_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hello_packets_sent.get_name_leafdata())
                        if (self.init_transitions.is_set or self.init_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.init_transitions.get_name_leafdata())
                        if (self.invalid_timer_received.is_set or self.invalid_timer_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_timer_received.get_name_leafdata())
                        if (self.learn_transitions.is_set or self.learn_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.learn_transitions.get_name_leafdata())
                        if (self.listen_transitions.is_set or self.listen_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.listen_transitions.get_name_leafdata())
                        if (self.mismatch_virtual_ip_address_received.is_set or self.mismatch_virtual_ip_address_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mismatch_virtual_ip_address_received.get_name_leafdata())
                        if (self.resign_packets_received.is_set or self.resign_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resign_packets_received.get_name_leafdata())
                        if (self.resign_packets_sent.is_set or self.resign_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resign_packets_sent.get_name_leafdata())
                        if (self.speak_transitions.is_set or self.speak_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.speak_transitions.get_name_leafdata())
                        if (self.standby_transitions.is_set or self.standby_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.standby_transitions.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active-transitions" or name == "auth-fail-received" or name == "coup-packets-received" or name == "coup-packets-sent" or name == "hello-packets-received" or name == "hello-packets-sent" or name == "init-transitions" or name == "invalid-timer-received" or name == "learn-transitions" or name == "listen-transitions" or name == "mismatch-virtual-ip-address-received" or name == "resign-packets-received" or name == "resign-packets-sent" or name == "speak-transitions" or name == "standby-transitions"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "active-transitions"):
                            self.active_transitions = value
                            self.active_transitions.value_namespace = name_space
                            self.active_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "auth-fail-received"):
                            self.auth_fail_received = value
                            self.auth_fail_received.value_namespace = name_space
                            self.auth_fail_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "coup-packets-received"):
                            self.coup_packets_received = value
                            self.coup_packets_received.value_namespace = name_space
                            self.coup_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "coup-packets-sent"):
                            self.coup_packets_sent = value
                            self.coup_packets_sent.value_namespace = name_space
                            self.coup_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "hello-packets-received"):
                            self.hello_packets_received = value
                            self.hello_packets_received.value_namespace = name_space
                            self.hello_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "hello-packets-sent"):
                            self.hello_packets_sent = value
                            self.hello_packets_sent.value_namespace = name_space
                            self.hello_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "init-transitions"):
                            self.init_transitions = value
                            self.init_transitions.value_namespace = name_space
                            self.init_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-timer-received"):
                            self.invalid_timer_received = value
                            self.invalid_timer_received.value_namespace = name_space
                            self.invalid_timer_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "learn-transitions"):
                            self.learn_transitions = value
                            self.learn_transitions.value_namespace = name_space
                            self.learn_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "listen-transitions"):
                            self.listen_transitions = value
                            self.listen_transitions.value_namespace = name_space
                            self.listen_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "mismatch-virtual-ip-address-received"):
                            self.mismatch_virtual_ip_address_received = value
                            self.mismatch_virtual_ip_address_received.value_namespace = name_space
                            self.mismatch_virtual_ip_address_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resign-packets-received"):
                            self.resign_packets_received = value
                            self.resign_packets_received.value_namespace = name_space
                            self.resign_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resign-packets-sent"):
                            self.resign_packets_sent = value
                            self.resign_packets_sent.value_namespace = name_space
                            self.resign_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "speak-transitions"):
                            self.speak_transitions = value
                            self.speak_transitions.value_namespace = name_space
                            self.speak_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "standby-transitions"):
                            self.standby_transitions = value
                            self.standby_transitions.value_namespace = name_space
                            self.standby_transitions.value_namespace_prefix = name_space_prefix


                class GlobalAddress(Entity):
                    """
                    Global virtual IPv6 addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.GlobalAddress, self).__init__()

                        self.yang_name = "global-address"
                        self.yang_parent_name = "group"

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipv6_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv4.Groups.Group.GlobalAddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv4.Groups.Group.GlobalAddress, self).__setattr__(name, value)

                    def has_data(self):
                        return self.ipv6_address.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipv6_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "global-address" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv6-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipv6-address"):
                            self.ipv6_address = value
                            self.ipv6_address.value_namespace = name_space
                            self.ipv6_address.value_namespace_prefix = name_space_prefix


                class StateChangeHistory(Entity):
                    """
                    State change history
                    
                    .. attribute:: new_state
                    
                    	New State
                    	**type**\:   :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:   :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:   :py:class:`HsrpStateChangeReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpStateChangeReason>`
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:   :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.StateChangeHistory, self).__init__()

                        self.yang_name = "state-change-history"
                        self.yang_parent_name = "group"

                        self.new_state = YLeaf(YType.enumeration, "new-state")

                        self.old_state = YLeaf(YType.enumeration, "old-state")

                        self.reason = YLeaf(YType.enumeration, "reason")

                        self.time = Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time()
                        self.time.parent = self
                        self._children_name_map["time"] = "time"
                        self._children_yang_names.add("time")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("new_state",
                                        "old_state",
                                        "reason") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv4.Groups.Group.StateChangeHistory, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv4.Groups.Group.StateChangeHistory, self).__setattr__(name, value)


                    class Time(Entity):
                        """
                        Time of state change
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time, self).__init__()

                            self.yang_name = "time"
                            self.yang_parent_name = "state-change-history"

                            self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                            self.seconds = YLeaf(YType.uint32, "seconds")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("nanoseconds",
                                            "seconds") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.nanoseconds.is_set or
                                self.seconds.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.nanoseconds.yfilter != YFilter.not_set or
                                self.seconds.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "time" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                            if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.seconds.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "nanoseconds" or name == "seconds"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "nanoseconds"):
                                self.nanoseconds = value
                                self.nanoseconds.value_namespace = name_space
                                self.nanoseconds.value_namespace_prefix = name_space_prefix
                            if(value_path == "seconds"):
                                self.seconds = value
                                self.seconds.value_namespace = name_space
                                self.seconds.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.new_state.is_set or
                            self.old_state.is_set or
                            self.reason.is_set or
                            (self.time is not None and self.time.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.new_state.yfilter != YFilter.not_set or
                            self.old_state.yfilter != YFilter.not_set or
                            self.reason.yfilter != YFilter.not_set or
                            (self.time is not None and self.time.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "state-change-history" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.new_state.is_set or self.new_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.new_state.get_name_leafdata())
                        if (self.old_state.is_set or self.old_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.old_state.get_name_leafdata())
                        if (self.reason.is_set or self.reason.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reason.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "time"):
                            if (self.time is None):
                                self.time = Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time()
                                self.time.parent = self
                                self._children_name_map["time"] = "time"
                            return self.time

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "time" or name == "new-state" or name == "old-state" or name == "reason"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "new-state"):
                            self.new_state = value
                            self.new_state.value_namespace = name_space
                            self.new_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "old-state"):
                            self.old_state = value
                            self.old_state.value_namespace = name_space
                            self.old_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "reason"):
                            self.reason = value
                            self.reason.value_namespace = name_space
                            self.reason.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.global_address:
                        if (c.has_data()):
                            return True
                    for c in self.state_change_history:
                        if (c.has_data()):
                            return True
                    for leaf in self.secondary_address.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.interface_name.is_set or
                        self.group_number.is_set or
                        self.active_ip_address.is_set or
                        self.active_ipv6_address.is_set or
                        self.active_mac_address.is_set or
                        self.active_priority.is_set or
                        self.active_timer_flag.is_set or
                        self.active_timer_msecs.is_set or
                        self.active_timer_secs.is_set or
                        self.address_family.is_set or
                        self.authentication_string.is_set or
                        self.bfd_enabled.is_set or
                        self.bfd_interface.is_set or
                        self.bfd_interval.is_set or
                        self.bfd_multiplier.is_set or
                        self.bfd_peer_ip_address.is_set or
                        self.bfd_peer_ipv6_address.is_set or
                        self.bfd_session_state.is_set or
                        self.configured_mac_address.is_set or
                        self.configured_priority.is_set or
                        self.configured_timers.is_set or
                        self.current_state_timer_secs.is_set or
                        self.delay_timer_flag.is_set or
                        self.delay_timer_msecs.is_set or
                        self.delay_timer_secs.is_set or
                        self.followed_session_name.is_set or
                        self.hello_time.is_set or
                        self.hello_timer_flag.is_set or
                        self.hello_timer_msecs.is_set or
                        self.hello_timer_secs.is_set or
                        self.hold_time.is_set or
                        self.hsrp_group_number.is_set or
                        self.hsrp_router_state.is_set or
                        self.interface.is_set or
                        self.interface_name_xr.is_set or
                        self.is_slave.is_set or
                        self.learned_hello_time.is_set or
                        self.learned_hold_time.is_set or
                        self.min_delay_time.is_set or
                        self.preempt_delay.is_set or
                        self.preempt_enabled.is_set or
                        self.preempt_timer_secs.is_set or
                        self.redirects_disabled.is_set or
                        self.reload_delay_time.is_set or
                        self.router_priority.is_set or
                        self.session_name.is_set or
                        self.slaves.is_set or
                        self.standby_ip_address.is_set or
                        self.standby_ipv6_address.is_set or
                        self.standby_mac_address.is_set or
                        self.standby_timer_flag.is_set or
                        self.standby_timer_msecs.is_set or
                        self.standby_timer_secs.is_set or
                        self.state_change_count.is_set or
                        self.tracked_interface_count.is_set or
                        self.tracked_interface_up_count.is_set or
                        self.use_bia_configured.is_set or
                        self.use_configured_timers.is_set or
                        self.use_configured_virtual_ip.is_set or
                        self.version.is_set or
                        self.virtual_ip_address.is_set or
                        self.virtual_linklocal_ipv6_address.is_set or
                        self.virtual_mac_address.is_set or
                        self.virtual_mac_address_state.is_set or
                        (self.coup_received_time is not None and self.coup_received_time.has_data()) or
                        (self.coup_sent_time is not None and self.coup_sent_time.has_data()) or
                        (self.resign_received_time is not None and self.resign_received_time.has_data()) or
                        (self.resign_sent_time is not None and self.resign_sent_time.has_data()) or
                        (self.statistics is not None and self.statistics.has_data()))

                def has_operation(self):
                    for c in self.global_address:
                        if (c.has_operation()):
                            return True
                    for c in self.state_change_history:
                        if (c.has_operation()):
                            return True
                    for leaf in self.secondary_address.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.group_number.yfilter != YFilter.not_set or
                        self.active_ip_address.yfilter != YFilter.not_set or
                        self.active_ipv6_address.yfilter != YFilter.not_set or
                        self.active_mac_address.yfilter != YFilter.not_set or
                        self.active_priority.yfilter != YFilter.not_set or
                        self.active_timer_flag.yfilter != YFilter.not_set or
                        self.active_timer_msecs.yfilter != YFilter.not_set or
                        self.active_timer_secs.yfilter != YFilter.not_set or
                        self.address_family.yfilter != YFilter.not_set or
                        self.authentication_string.yfilter != YFilter.not_set or
                        self.bfd_enabled.yfilter != YFilter.not_set or
                        self.bfd_interface.yfilter != YFilter.not_set or
                        self.bfd_interval.yfilter != YFilter.not_set or
                        self.bfd_multiplier.yfilter != YFilter.not_set or
                        self.bfd_peer_ip_address.yfilter != YFilter.not_set or
                        self.bfd_peer_ipv6_address.yfilter != YFilter.not_set or
                        self.bfd_session_state.yfilter != YFilter.not_set or
                        self.configured_mac_address.yfilter != YFilter.not_set or
                        self.configured_priority.yfilter != YFilter.not_set or
                        self.configured_timers.yfilter != YFilter.not_set or
                        self.current_state_timer_secs.yfilter != YFilter.not_set or
                        self.delay_timer_flag.yfilter != YFilter.not_set or
                        self.delay_timer_msecs.yfilter != YFilter.not_set or
                        self.delay_timer_secs.yfilter != YFilter.not_set or
                        self.followed_session_name.yfilter != YFilter.not_set or
                        self.hello_time.yfilter != YFilter.not_set or
                        self.hello_timer_flag.yfilter != YFilter.not_set or
                        self.hello_timer_msecs.yfilter != YFilter.not_set or
                        self.hello_timer_secs.yfilter != YFilter.not_set or
                        self.hold_time.yfilter != YFilter.not_set or
                        self.hsrp_group_number.yfilter != YFilter.not_set or
                        self.hsrp_router_state.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.interface_name_xr.yfilter != YFilter.not_set or
                        self.is_slave.yfilter != YFilter.not_set or
                        self.learned_hello_time.yfilter != YFilter.not_set or
                        self.learned_hold_time.yfilter != YFilter.not_set or
                        self.min_delay_time.yfilter != YFilter.not_set or
                        self.preempt_delay.yfilter != YFilter.not_set or
                        self.preempt_enabled.yfilter != YFilter.not_set or
                        self.preempt_timer_secs.yfilter != YFilter.not_set or
                        self.redirects_disabled.yfilter != YFilter.not_set or
                        self.reload_delay_time.yfilter != YFilter.not_set or
                        self.router_priority.yfilter != YFilter.not_set or
                        self.secondary_address.yfilter != YFilter.not_set or
                        self.session_name.yfilter != YFilter.not_set or
                        self.slaves.yfilter != YFilter.not_set or
                        self.standby_ip_address.yfilter != YFilter.not_set or
                        self.standby_ipv6_address.yfilter != YFilter.not_set or
                        self.standby_mac_address.yfilter != YFilter.not_set or
                        self.standby_timer_flag.yfilter != YFilter.not_set or
                        self.standby_timer_msecs.yfilter != YFilter.not_set or
                        self.standby_timer_secs.yfilter != YFilter.not_set or
                        self.state_change_count.yfilter != YFilter.not_set or
                        self.tracked_interface_count.yfilter != YFilter.not_set or
                        self.tracked_interface_up_count.yfilter != YFilter.not_set or
                        self.use_bia_configured.yfilter != YFilter.not_set or
                        self.use_configured_timers.yfilter != YFilter.not_set or
                        self.use_configured_virtual_ip.yfilter != YFilter.not_set or
                        self.version.yfilter != YFilter.not_set or
                        self.virtual_ip_address.yfilter != YFilter.not_set or
                        self.virtual_linklocal_ipv6_address.yfilter != YFilter.not_set or
                        self.virtual_mac_address.yfilter != YFilter.not_set or
                        self.virtual_mac_address_state.yfilter != YFilter.not_set or
                        (self.coup_received_time is not None and self.coup_received_time.has_operation()) or
                        (self.coup_sent_time is not None and self.coup_sent_time.has_operation()) or
                        (self.resign_received_time is not None and self.resign_received_time.has_operation()) or
                        (self.resign_sent_time is not None and self.resign_sent_time.has_operation()) or
                        (self.statistics is not None and self.statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "group" + "[interface-name='" + self.interface_name.get() + "']" + "[group-number='" + self.group_number.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.group_number.is_set or self.group_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_number.get_name_leafdata())
                    if (self.active_ip_address.is_set or self.active_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_ip_address.get_name_leafdata())
                    if (self.active_ipv6_address.is_set or self.active_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_ipv6_address.get_name_leafdata())
                    if (self.active_mac_address.is_set or self.active_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_mac_address.get_name_leafdata())
                    if (self.active_priority.is_set or self.active_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_priority.get_name_leafdata())
                    if (self.active_timer_flag.is_set or self.active_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_timer_flag.get_name_leafdata())
                    if (self.active_timer_msecs.is_set or self.active_timer_msecs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_timer_msecs.get_name_leafdata())
                    if (self.active_timer_secs.is_set or self.active_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_timer_secs.get_name_leafdata())
                    if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_family.get_name_leafdata())
                    if (self.authentication_string.is_set or self.authentication_string.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_string.get_name_leafdata())
                    if (self.bfd_enabled.is_set or self.bfd_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_enabled.get_name_leafdata())
                    if (self.bfd_interface.is_set or self.bfd_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_interface.get_name_leafdata())
                    if (self.bfd_interval.is_set or self.bfd_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_interval.get_name_leafdata())
                    if (self.bfd_multiplier.is_set or self.bfd_multiplier.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_multiplier.get_name_leafdata())
                    if (self.bfd_peer_ip_address.is_set or self.bfd_peer_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_peer_ip_address.get_name_leafdata())
                    if (self.bfd_peer_ipv6_address.is_set or self.bfd_peer_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_peer_ipv6_address.get_name_leafdata())
                    if (self.bfd_session_state.is_set or self.bfd_session_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_session_state.get_name_leafdata())
                    if (self.configured_mac_address.is_set or self.configured_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_mac_address.get_name_leafdata())
                    if (self.configured_priority.is_set or self.configured_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_priority.get_name_leafdata())
                    if (self.configured_timers.is_set or self.configured_timers.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_timers.get_name_leafdata())
                    if (self.current_state_timer_secs.is_set or self.current_state_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_state_timer_secs.get_name_leafdata())
                    if (self.delay_timer_flag.is_set or self.delay_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_flag.get_name_leafdata())
                    if (self.delay_timer_msecs.is_set or self.delay_timer_msecs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_msecs.get_name_leafdata())
                    if (self.delay_timer_secs.is_set or self.delay_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_secs.get_name_leafdata())
                    if (self.followed_session_name.is_set or self.followed_session_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.followed_session_name.get_name_leafdata())
                    if (self.hello_time.is_set or self.hello_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hello_time.get_name_leafdata())
                    if (self.hello_timer_flag.is_set or self.hello_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hello_timer_flag.get_name_leafdata())
                    if (self.hello_timer_msecs.is_set or self.hello_timer_msecs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hello_timer_msecs.get_name_leafdata())
                    if (self.hello_timer_secs.is_set or self.hello_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hello_timer_secs.get_name_leafdata())
                    if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hold_time.get_name_leafdata())
                    if (self.hsrp_group_number.is_set or self.hsrp_group_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hsrp_group_number.get_name_leafdata())
                    if (self.hsrp_router_state.is_set or self.hsrp_router_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hsrp_router_state.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                    if (self.is_slave.is_set or self.is_slave.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_slave.get_name_leafdata())
                    if (self.learned_hello_time.is_set or self.learned_hello_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.learned_hello_time.get_name_leafdata())
                    if (self.learned_hold_time.is_set or self.learned_hold_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.learned_hold_time.get_name_leafdata())
                    if (self.min_delay_time.is_set or self.min_delay_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.min_delay_time.get_name_leafdata())
                    if (self.preempt_delay.is_set or self.preempt_delay.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.preempt_delay.get_name_leafdata())
                    if (self.preempt_enabled.is_set or self.preempt_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.preempt_enabled.get_name_leafdata())
                    if (self.preempt_timer_secs.is_set or self.preempt_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.preempt_timer_secs.get_name_leafdata())
                    if (self.redirects_disabled.is_set or self.redirects_disabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redirects_disabled.get_name_leafdata())
                    if (self.reload_delay_time.is_set or self.reload_delay_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reload_delay_time.get_name_leafdata())
                    if (self.router_priority.is_set or self.router_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router_priority.get_name_leafdata())
                    if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_name.get_name_leafdata())
                    if (self.slaves.is_set or self.slaves.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.slaves.get_name_leafdata())
                    if (self.standby_ip_address.is_set or self.standby_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_ip_address.get_name_leafdata())
                    if (self.standby_ipv6_address.is_set or self.standby_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_ipv6_address.get_name_leafdata())
                    if (self.standby_mac_address.is_set or self.standby_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_mac_address.get_name_leafdata())
                    if (self.standby_timer_flag.is_set or self.standby_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_timer_flag.get_name_leafdata())
                    if (self.standby_timer_msecs.is_set or self.standby_timer_msecs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_timer_msecs.get_name_leafdata())
                    if (self.standby_timer_secs.is_set or self.standby_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_timer_secs.get_name_leafdata())
                    if (self.state_change_count.is_set or self.state_change_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state_change_count.get_name_leafdata())
                    if (self.tracked_interface_count.is_set or self.tracked_interface_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_count.get_name_leafdata())
                    if (self.tracked_interface_up_count.is_set or self.tracked_interface_up_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_up_count.get_name_leafdata())
                    if (self.use_bia_configured.is_set or self.use_bia_configured.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.use_bia_configured.get_name_leafdata())
                    if (self.use_configured_timers.is_set or self.use_configured_timers.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.use_configured_timers.get_name_leafdata())
                    if (self.use_configured_virtual_ip.is_set or self.use_configured_virtual_ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.use_configured_virtual_ip.get_name_leafdata())
                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version.get_name_leafdata())
                    if (self.virtual_ip_address.is_set or self.virtual_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_ip_address.get_name_leafdata())
                    if (self.virtual_linklocal_ipv6_address.is_set or self.virtual_linklocal_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_linklocal_ipv6_address.get_name_leafdata())
                    if (self.virtual_mac_address.is_set or self.virtual_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_mac_address.get_name_leafdata())
                    if (self.virtual_mac_address_state.is_set or self.virtual_mac_address_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_mac_address_state.get_name_leafdata())

                    leaf_name_data.extend(self.secondary_address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "coup-received-time"):
                        if (self.coup_received_time is None):
                            self.coup_received_time = Hsrp.Ipv4.Groups.Group.CoupReceivedTime()
                            self.coup_received_time.parent = self
                            self._children_name_map["coup_received_time"] = "coup-received-time"
                        return self.coup_received_time

                    if (child_yang_name == "coup-sent-time"):
                        if (self.coup_sent_time is None):
                            self.coup_sent_time = Hsrp.Ipv4.Groups.Group.CoupSentTime()
                            self.coup_sent_time.parent = self
                            self._children_name_map["coup_sent_time"] = "coup-sent-time"
                        return self.coup_sent_time

                    if (child_yang_name == "global-address"):
                        for c in self.global_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Hsrp.Ipv4.Groups.Group.GlobalAddress()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.global_address.append(c)
                        return c

                    if (child_yang_name == "resign-received-time"):
                        if (self.resign_received_time is None):
                            self.resign_received_time = Hsrp.Ipv4.Groups.Group.ResignReceivedTime()
                            self.resign_received_time.parent = self
                            self._children_name_map["resign_received_time"] = "resign-received-time"
                        return self.resign_received_time

                    if (child_yang_name == "resign-sent-time"):
                        if (self.resign_sent_time is None):
                            self.resign_sent_time = Hsrp.Ipv4.Groups.Group.ResignSentTime()
                            self.resign_sent_time.parent = self
                            self._children_name_map["resign_sent_time"] = "resign-sent-time"
                        return self.resign_sent_time

                    if (child_yang_name == "state-change-history"):
                        for c in self.state_change_history:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Hsrp.Ipv4.Groups.Group.StateChangeHistory()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.state_change_history.append(c)
                        return c

                    if (child_yang_name == "statistics"):
                        if (self.statistics is None):
                            self.statistics = Hsrp.Ipv4.Groups.Group.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                        return self.statistics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "coup-received-time" or name == "coup-sent-time" or name == "global-address" or name == "resign-received-time" or name == "resign-sent-time" or name == "state-change-history" or name == "statistics" or name == "interface-name" or name == "group-number" or name == "active-ip-address" or name == "active-ipv6-address" or name == "active-mac-address" or name == "active-priority" or name == "active-timer-flag" or name == "active-timer-msecs" or name == "active-timer-secs" or name == "address-family" or name == "authentication-string" or name == "bfd-enabled" or name == "bfd-interface" or name == "bfd-interval" or name == "bfd-multiplier" or name == "bfd-peer-ip-address" or name == "bfd-peer-ipv6-address" or name == "bfd-session-state" or name == "configured-mac-address" or name == "configured-priority" or name == "configured-timers" or name == "current-state-timer-secs" or name == "delay-timer-flag" or name == "delay-timer-msecs" or name == "delay-timer-secs" or name == "followed-session-name" or name == "hello-time" or name == "hello-timer-flag" or name == "hello-timer-msecs" or name == "hello-timer-secs" or name == "hold-time" or name == "hsrp-group-number" or name == "hsrp-router-state" or name == "interface" or name == "interface-name-xr" or name == "is-slave" or name == "learned-hello-time" or name == "learned-hold-time" or name == "min-delay-time" or name == "preempt-delay" or name == "preempt-enabled" or name == "preempt-timer-secs" or name == "redirects-disabled" or name == "reload-delay-time" or name == "router-priority" or name == "secondary-address" or name == "session-name" or name == "slaves" or name == "standby-ip-address" or name == "standby-ipv6-address" or name == "standby-mac-address" or name == "standby-timer-flag" or name == "standby-timer-msecs" or name == "standby-timer-secs" or name == "state-change-count" or name == "tracked-interface-count" or name == "tracked-interface-up-count" or name == "use-bia-configured" or name == "use-configured-timers" or name == "use-configured-virtual-ip" or name == "version" or name == "virtual-ip-address" or name == "virtual-linklocal-ipv6-address" or name == "virtual-mac-address" or name == "virtual-mac-address-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "group-number"):
                        self.group_number = value
                        self.group_number.value_namespace = name_space
                        self.group_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-ip-address"):
                        self.active_ip_address = value
                        self.active_ip_address.value_namespace = name_space
                        self.active_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-ipv6-address"):
                        self.active_ipv6_address = value
                        self.active_ipv6_address.value_namespace = name_space
                        self.active_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-mac-address"):
                        self.active_mac_address = value
                        self.active_mac_address.value_namespace = name_space
                        self.active_mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-priority"):
                        self.active_priority = value
                        self.active_priority.value_namespace = name_space
                        self.active_priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-timer-flag"):
                        self.active_timer_flag = value
                        self.active_timer_flag.value_namespace = name_space
                        self.active_timer_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-timer-msecs"):
                        self.active_timer_msecs = value
                        self.active_timer_msecs.value_namespace = name_space
                        self.active_timer_msecs.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-timer-secs"):
                        self.active_timer_secs = value
                        self.active_timer_secs.value_namespace = name_space
                        self.active_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "address-family"):
                        self.address_family = value
                        self.address_family.value_namespace = name_space
                        self.address_family.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-string"):
                        self.authentication_string = value
                        self.authentication_string.value_namespace = name_space
                        self.authentication_string.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-enabled"):
                        self.bfd_enabled = value
                        self.bfd_enabled.value_namespace = name_space
                        self.bfd_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-interface"):
                        self.bfd_interface = value
                        self.bfd_interface.value_namespace = name_space
                        self.bfd_interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-interval"):
                        self.bfd_interval = value
                        self.bfd_interval.value_namespace = name_space
                        self.bfd_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-multiplier"):
                        self.bfd_multiplier = value
                        self.bfd_multiplier.value_namespace = name_space
                        self.bfd_multiplier.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-peer-ip-address"):
                        self.bfd_peer_ip_address = value
                        self.bfd_peer_ip_address.value_namespace = name_space
                        self.bfd_peer_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-peer-ipv6-address"):
                        self.bfd_peer_ipv6_address = value
                        self.bfd_peer_ipv6_address.value_namespace = name_space
                        self.bfd_peer_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-session-state"):
                        self.bfd_session_state = value
                        self.bfd_session_state.value_namespace = name_space
                        self.bfd_session_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "configured-mac-address"):
                        self.configured_mac_address = value
                        self.configured_mac_address.value_namespace = name_space
                        self.configured_mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "configured-priority"):
                        self.configured_priority = value
                        self.configured_priority.value_namespace = name_space
                        self.configured_priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "configured-timers"):
                        self.configured_timers = value
                        self.configured_timers.value_namespace = name_space
                        self.configured_timers.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-state-timer-secs"):
                        self.current_state_timer_secs = value
                        self.current_state_timer_secs.value_namespace = name_space
                        self.current_state_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "delay-timer-flag"):
                        self.delay_timer_flag = value
                        self.delay_timer_flag.value_namespace = name_space
                        self.delay_timer_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "delay-timer-msecs"):
                        self.delay_timer_msecs = value
                        self.delay_timer_msecs.value_namespace = name_space
                        self.delay_timer_msecs.value_namespace_prefix = name_space_prefix
                    if(value_path == "delay-timer-secs"):
                        self.delay_timer_secs = value
                        self.delay_timer_secs.value_namespace = name_space
                        self.delay_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "followed-session-name"):
                        self.followed_session_name = value
                        self.followed_session_name.value_namespace = name_space
                        self.followed_session_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "hello-time"):
                        self.hello_time = value
                        self.hello_time.value_namespace = name_space
                        self.hello_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "hello-timer-flag"):
                        self.hello_timer_flag = value
                        self.hello_timer_flag.value_namespace = name_space
                        self.hello_timer_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "hello-timer-msecs"):
                        self.hello_timer_msecs = value
                        self.hello_timer_msecs.value_namespace = name_space
                        self.hello_timer_msecs.value_namespace_prefix = name_space_prefix
                    if(value_path == "hello-timer-secs"):
                        self.hello_timer_secs = value
                        self.hello_timer_secs.value_namespace = name_space
                        self.hello_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "hold-time"):
                        self.hold_time = value
                        self.hold_time.value_namespace = name_space
                        self.hold_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "hsrp-group-number"):
                        self.hsrp_group_number = value
                        self.hsrp_group_number.value_namespace = name_space
                        self.hsrp_group_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "hsrp-router-state"):
                        self.hsrp_router_state = value
                        self.hsrp_router_state.value_namespace = name_space
                        self.hsrp_router_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-name-xr"):
                        self.interface_name_xr = value
                        self.interface_name_xr.value_namespace = name_space
                        self.interface_name_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-slave"):
                        self.is_slave = value
                        self.is_slave.value_namespace = name_space
                        self.is_slave.value_namespace_prefix = name_space_prefix
                    if(value_path == "learned-hello-time"):
                        self.learned_hello_time = value
                        self.learned_hello_time.value_namespace = name_space
                        self.learned_hello_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "learned-hold-time"):
                        self.learned_hold_time = value
                        self.learned_hold_time.value_namespace = name_space
                        self.learned_hold_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "min-delay-time"):
                        self.min_delay_time = value
                        self.min_delay_time.value_namespace = name_space
                        self.min_delay_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "preempt-delay"):
                        self.preempt_delay = value
                        self.preempt_delay.value_namespace = name_space
                        self.preempt_delay.value_namespace_prefix = name_space_prefix
                    if(value_path == "preempt-enabled"):
                        self.preempt_enabled = value
                        self.preempt_enabled.value_namespace = name_space
                        self.preempt_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "preempt-timer-secs"):
                        self.preempt_timer_secs = value
                        self.preempt_timer_secs.value_namespace = name_space
                        self.preempt_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "redirects-disabled"):
                        self.redirects_disabled = value
                        self.redirects_disabled.value_namespace = name_space
                        self.redirects_disabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "reload-delay-time"):
                        self.reload_delay_time = value
                        self.reload_delay_time.value_namespace = name_space
                        self.reload_delay_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "router-priority"):
                        self.router_priority = value
                        self.router_priority.value_namespace = name_space
                        self.router_priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "secondary-address"):
                        self.secondary_address.append(value)
                    if(value_path == "session-name"):
                        self.session_name = value
                        self.session_name.value_namespace = name_space
                        self.session_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "slaves"):
                        self.slaves = value
                        self.slaves.value_namespace = name_space
                        self.slaves.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-ip-address"):
                        self.standby_ip_address = value
                        self.standby_ip_address.value_namespace = name_space
                        self.standby_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-ipv6-address"):
                        self.standby_ipv6_address = value
                        self.standby_ipv6_address.value_namespace = name_space
                        self.standby_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-mac-address"):
                        self.standby_mac_address = value
                        self.standby_mac_address.value_namespace = name_space
                        self.standby_mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-timer-flag"):
                        self.standby_timer_flag = value
                        self.standby_timer_flag.value_namespace = name_space
                        self.standby_timer_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-timer-msecs"):
                        self.standby_timer_msecs = value
                        self.standby_timer_msecs.value_namespace = name_space
                        self.standby_timer_msecs.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-timer-secs"):
                        self.standby_timer_secs = value
                        self.standby_timer_secs.value_namespace = name_space
                        self.standby_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "state-change-count"):
                        self.state_change_count = value
                        self.state_change_count.value_namespace = name_space
                        self.state_change_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-count"):
                        self.tracked_interface_count = value
                        self.tracked_interface_count.value_namespace = name_space
                        self.tracked_interface_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-up-count"):
                        self.tracked_interface_up_count = value
                        self.tracked_interface_up_count.value_namespace = name_space
                        self.tracked_interface_up_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "use-bia-configured"):
                        self.use_bia_configured = value
                        self.use_bia_configured.value_namespace = name_space
                        self.use_bia_configured.value_namespace_prefix = name_space_prefix
                    if(value_path == "use-configured-timers"):
                        self.use_configured_timers = value
                        self.use_configured_timers.value_namespace = name_space
                        self.use_configured_timers.value_namespace_prefix = name_space_prefix
                    if(value_path == "use-configured-virtual-ip"):
                        self.use_configured_virtual_ip = value
                        self.use_configured_virtual_ip.value_namespace = name_space
                        self.use_configured_virtual_ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "version"):
                        self.version = value
                        self.version.value_namespace = name_space
                        self.version.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-ip-address"):
                        self.virtual_ip_address = value
                        self.virtual_ip_address.value_namespace = name_space
                        self.virtual_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-linklocal-ipv6-address"):
                        self.virtual_linklocal_ipv6_address = value
                        self.virtual_linklocal_ipv6_address.value_namespace = name_space
                        self.virtual_linklocal_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-mac-address"):
                        self.virtual_mac_address = value
                        self.virtual_mac_address.value_namespace = name_space
                        self.virtual_mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-mac-address-state"):
                        self.virtual_mac_address_state = value
                        self.virtual_mac_address_state.value_namespace = name_space
                        self.virtual_mac_address_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "group"):
                    for c in self.group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Hsrp.Ipv4.Groups.Group()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class TrackedInterfaces(Entity):
            """
            The HSRP tracked interfaces table
            
            .. attribute:: tracked_interface
            
            	An HSRP tracked interface entry
            	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.TrackedInterfaces.TrackedInterface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv4.TrackedInterfaces, self).__init__()

                self.yang_name = "tracked-interfaces"
                self.yang_parent_name = "ipv4"

                self.tracked_interface = YList(self)

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
                            super(Hsrp.Ipv4.TrackedInterfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Hsrp.Ipv4.TrackedInterfaces, self).__setattr__(name, value)


            class TrackedInterface(Entity):
                """
                An HSRP tracked interface entry
                
                .. attribute:: interface_name  <key>
                
                	The interface name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: group_number  <key>
                
                	The HSRP group number
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tracked_interface_name  <key>
                
                	The interface name of the interface being tracked
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: hsrp_group_number
                
                	HSRP Group number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_up_flag
                
                	Interface up flag
                	**type**\:  bool
                
                .. attribute:: is_object
                
                	Tracked Object Flag
                	**type**\:  bool
                
                .. attribute:: priority_decrement
                
                	Priority weighting
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_name_xr
                
                	Tracked Interface Name
                	**type**\:  str
                
                	**length:** 0..64
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv4.TrackedInterfaces.TrackedInterface, self).__init__()

                    self.yang_name = "tracked-interface"
                    self.yang_parent_name = "tracked-interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.group_number = YLeaf(YType.int32, "group-number")

                    self.tracked_interface_name = YLeaf(YType.str, "tracked-interface-name")

                    self.hsrp_group_number = YLeaf(YType.uint32, "hsrp-group-number")

                    self.interface = YLeaf(YType.str, "interface")

                    self.interface_up_flag = YLeaf(YType.boolean, "interface-up-flag")

                    self.is_object = YLeaf(YType.boolean, "is-object")

                    self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")

                    self.tracked_interface_name_xr = YLeaf(YType.str, "tracked-interface-name-xr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "group_number",
                                    "tracked_interface_name",
                                    "hsrp_group_number",
                                    "interface",
                                    "interface_up_flag",
                                    "is_object",
                                    "priority_decrement",
                                    "tracked_interface_name_xr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Hsrp.Ipv4.TrackedInterfaces.TrackedInterface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Hsrp.Ipv4.TrackedInterfaces.TrackedInterface, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.group_number.is_set or
                        self.tracked_interface_name.is_set or
                        self.hsrp_group_number.is_set or
                        self.interface.is_set or
                        self.interface_up_flag.is_set or
                        self.is_object.is_set or
                        self.priority_decrement.is_set or
                        self.tracked_interface_name_xr.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.group_number.yfilter != YFilter.not_set or
                        self.tracked_interface_name.yfilter != YFilter.not_set or
                        self.hsrp_group_number.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.interface_up_flag.yfilter != YFilter.not_set or
                        self.is_object.yfilter != YFilter.not_set or
                        self.priority_decrement.yfilter != YFilter.not_set or
                        self.tracked_interface_name_xr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tracked-interface" + "[interface-name='" + self.interface_name.get() + "']" + "[group-number='" + self.group_number.get() + "']" + "[tracked-interface-name='" + self.tracked_interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/tracked-interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.group_number.is_set or self.group_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_number.get_name_leafdata())
                    if (self.tracked_interface_name.is_set or self.tracked_interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_name.get_name_leafdata())
                    if (self.hsrp_group_number.is_set or self.hsrp_group_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hsrp_group_number.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.interface_up_flag.is_set or self.interface_up_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_up_flag.get_name_leafdata())
                    if (self.is_object.is_set or self.is_object.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_object.get_name_leafdata())
                    if (self.priority_decrement.is_set or self.priority_decrement.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority_decrement.get_name_leafdata())
                    if (self.tracked_interface_name_xr.is_set or self.tracked_interface_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_name_xr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "group-number" or name == "tracked-interface-name" or name == "hsrp-group-number" or name == "interface" or name == "interface-up-flag" or name == "is-object" or name == "priority-decrement" or name == "tracked-interface-name-xr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "group-number"):
                        self.group_number = value
                        self.group_number.value_namespace = name_space
                        self.group_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-name"):
                        self.tracked_interface_name = value
                        self.tracked_interface_name.value_namespace = name_space
                        self.tracked_interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "hsrp-group-number"):
                        self.hsrp_group_number = value
                        self.hsrp_group_number.value_namespace = name_space
                        self.hsrp_group_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-up-flag"):
                        self.interface_up_flag = value
                        self.interface_up_flag.value_namespace = name_space
                        self.interface_up_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-object"):
                        self.is_object = value
                        self.is_object.value_namespace = name_space
                        self.is_object.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority-decrement"):
                        self.priority_decrement = value
                        self.priority_decrement.value_namespace = name_space
                        self.priority_decrement.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-name-xr"):
                        self.tracked_interface_name_xr = value
                        self.tracked_interface_name_xr.value_namespace = name_space
                        self.tracked_interface_name_xr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.tracked_interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.tracked_interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tracked-interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "tracked-interface"):
                    for c in self.tracked_interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Hsrp.Ipv4.TrackedInterfaces.TrackedInterface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.tracked_interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tracked-interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Interfaces(Entity):
            """
            The HSRP interface information table
            
            .. attribute:: interface
            
            	A HSRP interface entry
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv4.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "ipv4"

                self.interface = YList(self)

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
                            super(Hsrp.Ipv4.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Hsrp.Ipv4.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                A HSRP interface entry
                
                .. attribute:: interface_name  <key>
                
                	The interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: statistics
                
                	HSRP Interface Statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Interfaces.Interface.Statistics>`
                
                .. attribute:: use_bia_flag
                
                	Use burnt in mac address flag
                	**type**\:  bool
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv4.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface = YLeaf(YType.str, "interface")

                    self.use_bia_flag = YLeaf(YType.boolean, "use-bia-flag")

                    self.statistics = Hsrp.Ipv4.Interfaces.Interface.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "interface",
                                    "use_bia_flag") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Hsrp.Ipv4.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Hsrp.Ipv4.Interfaces.Interface, self).__setattr__(name, value)


                class Statistics(Entity):
                    """
                    HSRP Interface Statistics
                    
                    .. attribute:: advert_packets_received
                    
                    	Number of advertisement packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: advert_packets_sent
                    
                    	Number of advertisement packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: conflict_source_ip_address_received
                    
                    	Number of packets received from a conflicting Source IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inoperational_group_received
                    
                    	Number of packets received for an inoperational group
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_operation_code_received
                    
                    	Number of packets received with invalid operation code
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_version_received
                    
                    	Number of packets received with invalid version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: long_packets_received
                    
                    	Number of packets received that were too Long
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: short_packets_received
                    
                    	Number of packets received that were too short
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_group_received
                    
                    	Number of packets received for an unknown group id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Interfaces.Interface.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "interface"

                        self.advert_packets_received = YLeaf(YType.uint32, "advert-packets-received")

                        self.advert_packets_sent = YLeaf(YType.uint32, "advert-packets-sent")

                        self.conflict_source_ip_address_received = YLeaf(YType.uint32, "conflict-source-ip-address-received")

                        self.inoperational_group_received = YLeaf(YType.uint32, "inoperational-group-received")

                        self.invalid_operation_code_received = YLeaf(YType.uint32, "invalid-operation-code-received")

                        self.invalid_version_received = YLeaf(YType.uint32, "invalid-version-received")

                        self.long_packets_received = YLeaf(YType.uint32, "long-packets-received")

                        self.short_packets_received = YLeaf(YType.uint32, "short-packets-received")

                        self.unknown_group_received = YLeaf(YType.uint32, "unknown-group-received")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("advert_packets_received",
                                        "advert_packets_sent",
                                        "conflict_source_ip_address_received",
                                        "inoperational_group_received",
                                        "invalid_operation_code_received",
                                        "invalid_version_received",
                                        "long_packets_received",
                                        "short_packets_received",
                                        "unknown_group_received") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv4.Interfaces.Interface.Statistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv4.Interfaces.Interface.Statistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.advert_packets_received.is_set or
                            self.advert_packets_sent.is_set or
                            self.conflict_source_ip_address_received.is_set or
                            self.inoperational_group_received.is_set or
                            self.invalid_operation_code_received.is_set or
                            self.invalid_version_received.is_set or
                            self.long_packets_received.is_set or
                            self.short_packets_received.is_set or
                            self.unknown_group_received.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.advert_packets_received.yfilter != YFilter.not_set or
                            self.advert_packets_sent.yfilter != YFilter.not_set or
                            self.conflict_source_ip_address_received.yfilter != YFilter.not_set or
                            self.inoperational_group_received.yfilter != YFilter.not_set or
                            self.invalid_operation_code_received.yfilter != YFilter.not_set or
                            self.invalid_version_received.yfilter != YFilter.not_set or
                            self.long_packets_received.yfilter != YFilter.not_set or
                            self.short_packets_received.yfilter != YFilter.not_set or
                            self.unknown_group_received.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.advert_packets_received.is_set or self.advert_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.advert_packets_received.get_name_leafdata())
                        if (self.advert_packets_sent.is_set or self.advert_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.advert_packets_sent.get_name_leafdata())
                        if (self.conflict_source_ip_address_received.is_set or self.conflict_source_ip_address_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conflict_source_ip_address_received.get_name_leafdata())
                        if (self.inoperational_group_received.is_set or self.inoperational_group_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inoperational_group_received.get_name_leafdata())
                        if (self.invalid_operation_code_received.is_set or self.invalid_operation_code_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_operation_code_received.get_name_leafdata())
                        if (self.invalid_version_received.is_set or self.invalid_version_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_version_received.get_name_leafdata())
                        if (self.long_packets_received.is_set or self.long_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.long_packets_received.get_name_leafdata())
                        if (self.short_packets_received.is_set or self.short_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.short_packets_received.get_name_leafdata())
                        if (self.unknown_group_received.is_set or self.unknown_group_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_group_received.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "advert-packets-received" or name == "advert-packets-sent" or name == "conflict-source-ip-address-received" or name == "inoperational-group-received" or name == "invalid-operation-code-received" or name == "invalid-version-received" or name == "long-packets-received" or name == "short-packets-received" or name == "unknown-group-received"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "advert-packets-received"):
                            self.advert_packets_received = value
                            self.advert_packets_received.value_namespace = name_space
                            self.advert_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "advert-packets-sent"):
                            self.advert_packets_sent = value
                            self.advert_packets_sent.value_namespace = name_space
                            self.advert_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "conflict-source-ip-address-received"):
                            self.conflict_source_ip_address_received = value
                            self.conflict_source_ip_address_received.value_namespace = name_space
                            self.conflict_source_ip_address_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "inoperational-group-received"):
                            self.inoperational_group_received = value
                            self.inoperational_group_received.value_namespace = name_space
                            self.inoperational_group_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-operation-code-received"):
                            self.invalid_operation_code_received = value
                            self.invalid_operation_code_received.value_namespace = name_space
                            self.invalid_operation_code_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-version-received"):
                            self.invalid_version_received = value
                            self.invalid_version_received.value_namespace = name_space
                            self.invalid_version_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "long-packets-received"):
                            self.long_packets_received = value
                            self.long_packets_received.value_namespace = name_space
                            self.long_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "short-packets-received"):
                            self.short_packets_received = value
                            self.short_packets_received.value_namespace = name_space
                            self.short_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-group-received"):
                            self.unknown_group_received = value
                            self.unknown_group_received.value_namespace = name_space
                            self.unknown_group_received.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.interface.is_set or
                        self.use_bia_flag.is_set or
                        (self.statistics is not None and self.statistics.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.use_bia_flag.yfilter != YFilter.not_set or
                        (self.statistics is not None and self.statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.use_bia_flag.is_set or self.use_bia_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.use_bia_flag.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "statistics"):
                        if (self.statistics is None):
                            self.statistics = Hsrp.Ipv4.Interfaces.Interface.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                        return self.statistics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "statistics" or name == "interface-name" or name == "interface" or name == "use-bia-flag"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "use-bia-flag"):
                        self.use_bia_flag = value
                        self.use_bia_flag.value_namespace = name_space
                        self.use_bia_flag.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Hsrp.Ipv4.Interfaces.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.groups is not None and self.groups.has_data()) or
                (self.interfaces is not None and self.interfaces.has_data()) or
                (self.tracked_interfaces is not None and self.tracked_interfaces.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.groups is not None and self.groups.has_operation()) or
                (self.interfaces is not None and self.interfaces.has_operation()) or
                (self.tracked_interfaces is not None and self.tracked_interfaces.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv4" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "groups"):
                if (self.groups is None):
                    self.groups = Hsrp.Ipv4.Groups()
                    self.groups.parent = self
                    self._children_name_map["groups"] = "groups"
                return self.groups

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = Hsrp.Ipv4.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            if (child_yang_name == "tracked-interfaces"):
                if (self.tracked_interfaces is None):
                    self.tracked_interfaces = Hsrp.Ipv4.TrackedInterfaces()
                    self.tracked_interfaces.parent = self
                    self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
                return self.tracked_interfaces

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "groups" or name == "interfaces" or name == "tracked-interfaces"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class MgoSessions(Entity):
        """
        HSRP MGO session table
        
        .. attribute:: mgo_session
        
        	HSRP MGO session
        	**type**\: list of    :py:class:`MgoSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.MgoSessions.MgoSession>`
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.MgoSessions, self).__init__()

            self.yang_name = "mgo-sessions"
            self.yang_parent_name = "hsrp"

            self.mgo_session = YList(self)

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
                        super(Hsrp.MgoSessions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Hsrp.MgoSessions, self).__setattr__(name, value)


        class MgoSession(Entity):
            """
            HSRP MGO session
            
            .. attribute:: session_name  <key>
            
            	HSRP MGO session name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: primary_af_name
            
            	Address family of primary session
            	**type**\:   :py:class:`HsrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAf>`
            
            .. attribute:: primary_session_interface
            
            	Interface of primary session
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: primary_session_name
            
            	Session Name
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: primary_session_number
            
            	Group number of primary session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: primary_session_state
            
            	State of primary session
            	**type**\:   :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
            
            .. attribute:: slave
            
            	List of slaves following this primary session
            	**type**\: list of    :py:class:`Slave <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.MgoSessions.MgoSession.Slave>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.MgoSessions.MgoSession, self).__init__()

                self.yang_name = "mgo-session"
                self.yang_parent_name = "mgo-sessions"

                self.session_name = YLeaf(YType.str, "session-name")

                self.primary_af_name = YLeaf(YType.enumeration, "primary-af-name")

                self.primary_session_interface = YLeaf(YType.str, "primary-session-interface")

                self.primary_session_name = YLeaf(YType.str, "primary-session-name")

                self.primary_session_number = YLeaf(YType.uint32, "primary-session-number")

                self.primary_session_state = YLeaf(YType.enumeration, "primary-session-state")

                self.slave = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("session_name",
                                "primary_af_name",
                                "primary_session_interface",
                                "primary_session_name",
                                "primary_session_number",
                                "primary_session_state") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Hsrp.MgoSessions.MgoSession, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Hsrp.MgoSessions.MgoSession, self).__setattr__(name, value)


            class Slave(Entity):
                """
                List of slaves following this primary session
                
                .. attribute:: slave_group_interface
                
                	Interface of slave group
                	**type**\:  str
                
                	**length:** 0..64
                
                .. attribute:: slave_group_number
                
                	Group number of slave group
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.MgoSessions.MgoSession.Slave, self).__init__()

                    self.yang_name = "slave"
                    self.yang_parent_name = "mgo-session"

                    self.slave_group_interface = YLeaf(YType.str, "slave-group-interface")

                    self.slave_group_number = YLeaf(YType.uint32, "slave-group-number")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("slave_group_interface",
                                    "slave_group_number") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Hsrp.MgoSessions.MgoSession.Slave, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Hsrp.MgoSessions.MgoSession.Slave, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.slave_group_interface.is_set or
                        self.slave_group_number.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.slave_group_interface.yfilter != YFilter.not_set or
                        self.slave_group_number.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "slave" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.slave_group_interface.is_set or self.slave_group_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.slave_group_interface.get_name_leafdata())
                    if (self.slave_group_number.is_set or self.slave_group_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.slave_group_number.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "slave-group-interface" or name == "slave-group-number"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "slave-group-interface"):
                        self.slave_group_interface = value
                        self.slave_group_interface.value_namespace = name_space
                        self.slave_group_interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "slave-group-number"):
                        self.slave_group_number = value
                        self.slave_group_number.value_namespace = name_space
                        self.slave_group_number.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.slave:
                    if (c.has_data()):
                        return True
                return (
                    self.session_name.is_set or
                    self.primary_af_name.is_set or
                    self.primary_session_interface.is_set or
                    self.primary_session_name.is_set or
                    self.primary_session_number.is_set or
                    self.primary_session_state.is_set)

            def has_operation(self):
                for c in self.slave:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.session_name.yfilter != YFilter.not_set or
                    self.primary_af_name.yfilter != YFilter.not_set or
                    self.primary_session_interface.yfilter != YFilter.not_set or
                    self.primary_session_name.yfilter != YFilter.not_set or
                    self.primary_session_number.yfilter != YFilter.not_set or
                    self.primary_session_state.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mgo-session" + "[session-name='" + self.session_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/mgo-sessions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_name.get_name_leafdata())
                if (self.primary_af_name.is_set or self.primary_af_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.primary_af_name.get_name_leafdata())
                if (self.primary_session_interface.is_set or self.primary_session_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.primary_session_interface.get_name_leafdata())
                if (self.primary_session_name.is_set or self.primary_session_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.primary_session_name.get_name_leafdata())
                if (self.primary_session_number.is_set or self.primary_session_number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.primary_session_number.get_name_leafdata())
                if (self.primary_session_state.is_set or self.primary_session_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.primary_session_state.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "slave"):
                    for c in self.slave:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Hsrp.MgoSessions.MgoSession.Slave()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.slave.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "slave" or name == "session-name" or name == "primary-af-name" or name == "primary-session-interface" or name == "primary-session-name" or name == "primary-session-number" or name == "primary-session-state"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "session-name"):
                    self.session_name = value
                    self.session_name.value_namespace = name_space
                    self.session_name.value_namespace_prefix = name_space_prefix
                if(value_path == "primary-af-name"):
                    self.primary_af_name = value
                    self.primary_af_name.value_namespace = name_space
                    self.primary_af_name.value_namespace_prefix = name_space_prefix
                if(value_path == "primary-session-interface"):
                    self.primary_session_interface = value
                    self.primary_session_interface.value_namespace = name_space
                    self.primary_session_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "primary-session-name"):
                    self.primary_session_name = value
                    self.primary_session_name.value_namespace = name_space
                    self.primary_session_name.value_namespace_prefix = name_space_prefix
                if(value_path == "primary-session-number"):
                    self.primary_session_number = value
                    self.primary_session_number.value_namespace = name_space
                    self.primary_session_number.value_namespace_prefix = name_space_prefix
                if(value_path == "primary-session-state"):
                    self.primary_session_state = value
                    self.primary_session_state.value_namespace = name_space
                    self.primary_session_state.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mgo_session:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mgo_session:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mgo-sessions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mgo-session"):
                for c in self.mgo_session:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Hsrp.MgoSessions.MgoSession()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mgo_session.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mgo-session"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipv6(Entity):
        """
        IPv6 HSRP information
        
        .. attribute:: groups
        
        	The HSRP standby group table
        	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups>`
        
        .. attribute:: interfaces
        
        	The HSRP interface information table
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Interfaces>`
        
        .. attribute:: tracked_interfaces
        
        	The HSRP tracked interfaces table
        	**type**\:   :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.TrackedInterfaces>`
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "hsrp"

            self.groups = Hsrp.Ipv6.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._children_yang_names.add("groups")

            self.interfaces = Hsrp.Ipv6.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.tracked_interfaces = Hsrp.Ipv6.TrackedInterfaces()
            self.tracked_interfaces.parent = self
            self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
            self._children_yang_names.add("tracked-interfaces")


        class TrackedInterfaces(Entity):
            """
            The HSRP tracked interfaces table
            
            .. attribute:: tracked_interface
            
            	An HSRP tracked interface entry
            	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.TrackedInterfaces.TrackedInterface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv6.TrackedInterfaces, self).__init__()

                self.yang_name = "tracked-interfaces"
                self.yang_parent_name = "ipv6"

                self.tracked_interface = YList(self)

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
                            super(Hsrp.Ipv6.TrackedInterfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Hsrp.Ipv6.TrackedInterfaces, self).__setattr__(name, value)


            class TrackedInterface(Entity):
                """
                An HSRP tracked interface entry
                
                .. attribute:: interface_name  <key>
                
                	The interface name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: group_number  <key>
                
                	The HSRP group number
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tracked_interface_name  <key>
                
                	The interface name of the interface being tracked
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: hsrp_group_number
                
                	HSRP Group number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_up_flag
                
                	Interface up flag
                	**type**\:  bool
                
                .. attribute:: is_object
                
                	Tracked Object Flag
                	**type**\:  bool
                
                .. attribute:: priority_decrement
                
                	Priority weighting
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_name_xr
                
                	Tracked Interface Name
                	**type**\:  str
                
                	**length:** 0..64
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv6.TrackedInterfaces.TrackedInterface, self).__init__()

                    self.yang_name = "tracked-interface"
                    self.yang_parent_name = "tracked-interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.group_number = YLeaf(YType.int32, "group-number")

                    self.tracked_interface_name = YLeaf(YType.str, "tracked-interface-name")

                    self.hsrp_group_number = YLeaf(YType.uint32, "hsrp-group-number")

                    self.interface = YLeaf(YType.str, "interface")

                    self.interface_up_flag = YLeaf(YType.boolean, "interface-up-flag")

                    self.is_object = YLeaf(YType.boolean, "is-object")

                    self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")

                    self.tracked_interface_name_xr = YLeaf(YType.str, "tracked-interface-name-xr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "group_number",
                                    "tracked_interface_name",
                                    "hsrp_group_number",
                                    "interface",
                                    "interface_up_flag",
                                    "is_object",
                                    "priority_decrement",
                                    "tracked_interface_name_xr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Hsrp.Ipv6.TrackedInterfaces.TrackedInterface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Hsrp.Ipv6.TrackedInterfaces.TrackedInterface, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.group_number.is_set or
                        self.tracked_interface_name.is_set or
                        self.hsrp_group_number.is_set or
                        self.interface.is_set or
                        self.interface_up_flag.is_set or
                        self.is_object.is_set or
                        self.priority_decrement.is_set or
                        self.tracked_interface_name_xr.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.group_number.yfilter != YFilter.not_set or
                        self.tracked_interface_name.yfilter != YFilter.not_set or
                        self.hsrp_group_number.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.interface_up_flag.yfilter != YFilter.not_set or
                        self.is_object.yfilter != YFilter.not_set or
                        self.priority_decrement.yfilter != YFilter.not_set or
                        self.tracked_interface_name_xr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tracked-interface" + "[interface-name='" + self.interface_name.get() + "']" + "[group-number='" + self.group_number.get() + "']" + "[tracked-interface-name='" + self.tracked_interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/tracked-interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.group_number.is_set or self.group_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_number.get_name_leafdata())
                    if (self.tracked_interface_name.is_set or self.tracked_interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_name.get_name_leafdata())
                    if (self.hsrp_group_number.is_set or self.hsrp_group_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hsrp_group_number.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.interface_up_flag.is_set or self.interface_up_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_up_flag.get_name_leafdata())
                    if (self.is_object.is_set or self.is_object.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_object.get_name_leafdata())
                    if (self.priority_decrement.is_set or self.priority_decrement.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority_decrement.get_name_leafdata())
                    if (self.tracked_interface_name_xr.is_set or self.tracked_interface_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_name_xr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "group-number" or name == "tracked-interface-name" or name == "hsrp-group-number" or name == "interface" or name == "interface-up-flag" or name == "is-object" or name == "priority-decrement" or name == "tracked-interface-name-xr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "group-number"):
                        self.group_number = value
                        self.group_number.value_namespace = name_space
                        self.group_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-name"):
                        self.tracked_interface_name = value
                        self.tracked_interface_name.value_namespace = name_space
                        self.tracked_interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "hsrp-group-number"):
                        self.hsrp_group_number = value
                        self.hsrp_group_number.value_namespace = name_space
                        self.hsrp_group_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-up-flag"):
                        self.interface_up_flag = value
                        self.interface_up_flag.value_namespace = name_space
                        self.interface_up_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-object"):
                        self.is_object = value
                        self.is_object.value_namespace = name_space
                        self.is_object.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority-decrement"):
                        self.priority_decrement = value
                        self.priority_decrement.value_namespace = name_space
                        self.priority_decrement.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-name-xr"):
                        self.tracked_interface_name_xr = value
                        self.tracked_interface_name_xr.value_namespace = name_space
                        self.tracked_interface_name_xr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.tracked_interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.tracked_interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tracked-interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "tracked-interface"):
                    for c in self.tracked_interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Hsrp.Ipv6.TrackedInterfaces.TrackedInterface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.tracked_interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tracked-interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Groups(Entity):
            """
            The HSRP standby group table
            
            .. attribute:: group
            
            	An HSRP standby group
            	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv6.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "ipv6"

                self.group = YList(self)

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
                            super(Hsrp.Ipv6.Groups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Hsrp.Ipv6.Groups, self).__setattr__(name, value)


            class Group(Entity):
                """
                An HSRP standby group
                
                .. attribute:: interface_name  <key>
                
                	The interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: group_number  <key>
                
                	The HSRP group number
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: active_ip_address
                
                	Active router's IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: active_ipv6_address
                
                	Active router's IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: active_mac_address
                
                	Active router's interface MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: active_priority
                
                	Priority of the Active router
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: active_timer_flag
                
                	Active timer running flag
                	**type**\:  bool
                
                .. attribute:: active_timer_msecs
                
                	Active timer running time msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: active_timer_secs
                
                	Active timer running time secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:   :py:class:`HsrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAf>`
                
                .. attribute:: authentication_string
                
                	Authentication string
                	**type**\:  str
                
                	**length:** 0..9
                
                .. attribute:: bfd_enabled
                
                	HSRP BFD fast failover
                	**type**\:  bool
                
                .. attribute:: bfd_interface
                
                	BFD Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: bfd_interval
                
                	BFD packet send interval
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_multiplier
                
                	BFD multiplier
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_peer_ip_address
                
                	BFD Peer IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_peer_ipv6_address
                
                	BFD Peer IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_session_state
                
                	BFD session state
                	**type**\:   :py:class:`HsrpBfdSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBfdSessionState>`
                
                .. attribute:: configured_mac_address
                
                	MAC address configured
                	**type**\:  bool
                
                .. attribute:: configured_priority
                
                	Configured priority
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: configured_timers
                
                	Non\-default timers are configured
                	**type**\:  bool
                
                .. attribute:: coup_received_time
                
                	Time last coup was received
                	**type**\:   :py:class:`CoupReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.CoupReceivedTime>`
                
                .. attribute:: coup_sent_time
                
                	Time last coup was sent
                	**type**\:   :py:class:`CoupSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.CoupSentTime>`
                
                .. attribute:: current_state_timer_secs
                
                	Time in current state secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: delay_timer_flag
                
                	Delay timer running flag
                	**type**\:  bool
                
                .. attribute:: delay_timer_msecs
                
                	Delay timer running time msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: delay_timer_secs
                
                	Delay timer running time secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: followed_session_name
                
                	Followed Session Name
                	**type**\:  str
                
                	**length:** 0..16
                
                .. attribute:: global_address
                
                	Global virtual IPv6 addresses
                	**type**\: list of    :py:class:`GlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.GlobalAddress>`
                
                .. attribute:: hello_time
                
                	Hellotime in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: hello_timer_flag
                
                	Hello timer running flag
                	**type**\:  bool
                
                .. attribute:: hello_timer_msecs
                
                	Hello timer running time msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: hello_timer_secs
                
                	Hello timer running time secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: hold_time
                
                	Holdtime in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: hsrp_group_number
                
                	HSRP Group number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hsrp_router_state
                
                	HSRP router state
                	**type**\:   :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_name_xr
                
                	Interface Name
                	**type**\:  str
                
                	**length:** 0..64
                
                .. attribute:: is_slave
                
                	Group is a slave group
                	**type**\:  bool
                
                .. attribute:: learned_hello_time
                
                	Learned hellotime in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: learned_hold_time
                
                	Learned holdtime in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: min_delay_time
                
                	Minimum delay time in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: preempt_delay
                
                	Preempt delay time in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: preempt_enabled
                
                	Preempt enabled
                	**type**\:  bool
                
                .. attribute:: preempt_timer_secs
                
                	Preempt time remaining in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: redirects_disabled
                
                	HSRP redirects disabled
                	**type**\:  bool
                
                .. attribute:: reload_delay_time
                
                	Reload delay time in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: resign_received_time
                
                	Time last resign was received
                	**type**\:   :py:class:`ResignReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.ResignReceivedTime>`
                
                .. attribute:: resign_sent_time
                
                	Time last resign was sent
                	**type**\:   :py:class:`ResignSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.ResignSentTime>`
                
                .. attribute:: router_priority
                
                	Priority of the router
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: secondary_address
                
                	Secondary virtual IP addresses
                	**type**\:  list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: session_name
                
                	Session Name
                	**type**\:  str
                
                	**length:** 0..16
                
                .. attribute:: slaves
                
                	Number of slaves following state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_ip_address
                
                	Standby router's IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: standby_ipv6_address
                
                	Standby router's IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: standby_mac_address
                
                	Standby router's interface MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: standby_timer_flag
                
                	Standby timer running flag
                	**type**\:  bool
                
                .. attribute:: standby_timer_msecs
                
                	Standby timer running time msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: standby_timer_secs
                
                	Standby timer running time secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: state_change_count
                
                	Number of state changes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_change_history
                
                	State change history
                	**type**\: list of    :py:class:`StateChangeHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.StateChangeHistory>`
                
                .. attribute:: statistics
                
                	HSRP Group statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.Statistics>`
                
                .. attribute:: tracked_interface_count
                
                	Number of tracked interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_up_count
                
                	Number of tracked interfaces up
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: use_bia_configured
                
                	Use burnt in MAC address configured
                	**type**\:  bool
                
                .. attribute:: use_configured_timers
                
                	Use configured timers
                	**type**\:  bool
                
                .. attribute:: use_configured_virtual_ip
                
                	Use configured virtual IP
                	**type**\:  bool
                
                .. attribute:: version
                
                	HSRP Protocol Version
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: virtual_ip_address
                
                	Configured Virtual IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtual_linklocal_ipv6_address
                
                	Virtual linklocal IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtual_mac_address
                
                	Virtual mac address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: virtual_mac_address_state
                
                	Virtual mac address state
                	**type**\:   :py:class:`HsrpVmacState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpVmacState>`
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv6.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.group_number = YLeaf(YType.int32, "group-number")

                    self.active_ip_address = YLeaf(YType.str, "active-ip-address")

                    self.active_ipv6_address = YLeaf(YType.str, "active-ipv6-address")

                    self.active_mac_address = YLeaf(YType.str, "active-mac-address")

                    self.active_priority = YLeaf(YType.uint8, "active-priority")

                    self.active_timer_flag = YLeaf(YType.boolean, "active-timer-flag")

                    self.active_timer_msecs = YLeaf(YType.uint32, "active-timer-msecs")

                    self.active_timer_secs = YLeaf(YType.uint32, "active-timer-secs")

                    self.address_family = YLeaf(YType.enumeration, "address-family")

                    self.authentication_string = YLeaf(YType.str, "authentication-string")

                    self.bfd_enabled = YLeaf(YType.boolean, "bfd-enabled")

                    self.bfd_interface = YLeaf(YType.str, "bfd-interface")

                    self.bfd_interval = YLeaf(YType.uint32, "bfd-interval")

                    self.bfd_multiplier = YLeaf(YType.uint32, "bfd-multiplier")

                    self.bfd_peer_ip_address = YLeaf(YType.str, "bfd-peer-ip-address")

                    self.bfd_peer_ipv6_address = YLeaf(YType.str, "bfd-peer-ipv6-address")

                    self.bfd_session_state = YLeaf(YType.enumeration, "bfd-session-state")

                    self.configured_mac_address = YLeaf(YType.boolean, "configured-mac-address")

                    self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                    self.configured_timers = YLeaf(YType.boolean, "configured-timers")

                    self.current_state_timer_secs = YLeaf(YType.uint32, "current-state-timer-secs")

                    self.delay_timer_flag = YLeaf(YType.boolean, "delay-timer-flag")

                    self.delay_timer_msecs = YLeaf(YType.uint32, "delay-timer-msecs")

                    self.delay_timer_secs = YLeaf(YType.uint32, "delay-timer-secs")

                    self.followed_session_name = YLeaf(YType.str, "followed-session-name")

                    self.hello_time = YLeaf(YType.uint32, "hello-time")

                    self.hello_timer_flag = YLeaf(YType.boolean, "hello-timer-flag")

                    self.hello_timer_msecs = YLeaf(YType.uint32, "hello-timer-msecs")

                    self.hello_timer_secs = YLeaf(YType.uint32, "hello-timer-secs")

                    self.hold_time = YLeaf(YType.uint32, "hold-time")

                    self.hsrp_group_number = YLeaf(YType.uint32, "hsrp-group-number")

                    self.hsrp_router_state = YLeaf(YType.enumeration, "hsrp-router-state")

                    self.interface = YLeaf(YType.str, "interface")

                    self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                    self.is_slave = YLeaf(YType.boolean, "is-slave")

                    self.learned_hello_time = YLeaf(YType.uint32, "learned-hello-time")

                    self.learned_hold_time = YLeaf(YType.uint32, "learned-hold-time")

                    self.min_delay_time = YLeaf(YType.uint32, "min-delay-time")

                    self.preempt_delay = YLeaf(YType.uint32, "preempt-delay")

                    self.preempt_enabled = YLeaf(YType.boolean, "preempt-enabled")

                    self.preempt_timer_secs = YLeaf(YType.uint32, "preempt-timer-secs")

                    self.redirects_disabled = YLeaf(YType.boolean, "redirects-disabled")

                    self.reload_delay_time = YLeaf(YType.uint32, "reload-delay-time")

                    self.router_priority = YLeaf(YType.uint8, "router-priority")

                    self.secondary_address = YLeafList(YType.str, "secondary-address")

                    self.session_name = YLeaf(YType.str, "session-name")

                    self.slaves = YLeaf(YType.uint32, "slaves")

                    self.standby_ip_address = YLeaf(YType.str, "standby-ip-address")

                    self.standby_ipv6_address = YLeaf(YType.str, "standby-ipv6-address")

                    self.standby_mac_address = YLeaf(YType.str, "standby-mac-address")

                    self.standby_timer_flag = YLeaf(YType.boolean, "standby-timer-flag")

                    self.standby_timer_msecs = YLeaf(YType.uint32, "standby-timer-msecs")

                    self.standby_timer_secs = YLeaf(YType.uint32, "standby-timer-secs")

                    self.state_change_count = YLeaf(YType.uint32, "state-change-count")

                    self.tracked_interface_count = YLeaf(YType.uint32, "tracked-interface-count")

                    self.tracked_interface_up_count = YLeaf(YType.uint32, "tracked-interface-up-count")

                    self.use_bia_configured = YLeaf(YType.boolean, "use-bia-configured")

                    self.use_configured_timers = YLeaf(YType.boolean, "use-configured-timers")

                    self.use_configured_virtual_ip = YLeaf(YType.boolean, "use-configured-virtual-ip")

                    self.version = YLeaf(YType.uint8, "version")

                    self.virtual_ip_address = YLeaf(YType.str, "virtual-ip-address")

                    self.virtual_linklocal_ipv6_address = YLeaf(YType.str, "virtual-linklocal-ipv6-address")

                    self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                    self.virtual_mac_address_state = YLeaf(YType.enumeration, "virtual-mac-address-state")

                    self.coup_received_time = Hsrp.Ipv6.Groups.Group.CoupReceivedTime()
                    self.coup_received_time.parent = self
                    self._children_name_map["coup_received_time"] = "coup-received-time"
                    self._children_yang_names.add("coup-received-time")

                    self.coup_sent_time = Hsrp.Ipv6.Groups.Group.CoupSentTime()
                    self.coup_sent_time.parent = self
                    self._children_name_map["coup_sent_time"] = "coup-sent-time"
                    self._children_yang_names.add("coup-sent-time")

                    self.resign_received_time = Hsrp.Ipv6.Groups.Group.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self._children_name_map["resign_received_time"] = "resign-received-time"
                    self._children_yang_names.add("resign-received-time")

                    self.resign_sent_time = Hsrp.Ipv6.Groups.Group.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self._children_name_map["resign_sent_time"] = "resign-sent-time"
                    self._children_yang_names.add("resign-sent-time")

                    self.statistics = Hsrp.Ipv6.Groups.Group.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")

                    self.global_address = YList(self)
                    self.state_change_history = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "group_number",
                                    "active_ip_address",
                                    "active_ipv6_address",
                                    "active_mac_address",
                                    "active_priority",
                                    "active_timer_flag",
                                    "active_timer_msecs",
                                    "active_timer_secs",
                                    "address_family",
                                    "authentication_string",
                                    "bfd_enabled",
                                    "bfd_interface",
                                    "bfd_interval",
                                    "bfd_multiplier",
                                    "bfd_peer_ip_address",
                                    "bfd_peer_ipv6_address",
                                    "bfd_session_state",
                                    "configured_mac_address",
                                    "configured_priority",
                                    "configured_timers",
                                    "current_state_timer_secs",
                                    "delay_timer_flag",
                                    "delay_timer_msecs",
                                    "delay_timer_secs",
                                    "followed_session_name",
                                    "hello_time",
                                    "hello_timer_flag",
                                    "hello_timer_msecs",
                                    "hello_timer_secs",
                                    "hold_time",
                                    "hsrp_group_number",
                                    "hsrp_router_state",
                                    "interface",
                                    "interface_name_xr",
                                    "is_slave",
                                    "learned_hello_time",
                                    "learned_hold_time",
                                    "min_delay_time",
                                    "preempt_delay",
                                    "preempt_enabled",
                                    "preempt_timer_secs",
                                    "redirects_disabled",
                                    "reload_delay_time",
                                    "router_priority",
                                    "secondary_address",
                                    "session_name",
                                    "slaves",
                                    "standby_ip_address",
                                    "standby_ipv6_address",
                                    "standby_mac_address",
                                    "standby_timer_flag",
                                    "standby_timer_msecs",
                                    "standby_timer_secs",
                                    "state_change_count",
                                    "tracked_interface_count",
                                    "tracked_interface_up_count",
                                    "use_bia_configured",
                                    "use_configured_timers",
                                    "use_configured_virtual_ip",
                                    "version",
                                    "virtual_ip_address",
                                    "virtual_linklocal_ipv6_address",
                                    "virtual_mac_address",
                                    "virtual_mac_address_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Hsrp.Ipv6.Groups.Group, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Hsrp.Ipv6.Groups.Group, self).__setattr__(name, value)


                class ResignSentTime(Entity):
                    """
                    Time last resign was sent
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.ResignSentTime, self).__init__()

                        self.yang_name = "resign-sent-time"
                        self.yang_parent_name = "group"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv6.Groups.Group.ResignSentTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv6.Groups.Group.ResignSentTime, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "resign-sent-time" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix


                class ResignReceivedTime(Entity):
                    """
                    Time last resign was received
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.ResignReceivedTime, self).__init__()

                        self.yang_name = "resign-received-time"
                        self.yang_parent_name = "group"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv6.Groups.Group.ResignReceivedTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv6.Groups.Group.ResignReceivedTime, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "resign-received-time" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix


                class CoupSentTime(Entity):
                    """
                    Time last coup was sent
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.CoupSentTime, self).__init__()

                        self.yang_name = "coup-sent-time"
                        self.yang_parent_name = "group"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv6.Groups.Group.CoupSentTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv6.Groups.Group.CoupSentTime, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "coup-sent-time" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix


                class CoupReceivedTime(Entity):
                    """
                    Time last coup was received
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.CoupReceivedTime, self).__init__()

                        self.yang_name = "coup-received-time"
                        self.yang_parent_name = "group"

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nanoseconds",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv6.Groups.Group.CoupReceivedTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv6.Groups.Group.CoupReceivedTime, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nanoseconds.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nanoseconds.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "coup-received-time" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nanoseconds" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nanoseconds"):
                            self.nanoseconds = value
                            self.nanoseconds.value_namespace = name_space
                            self.nanoseconds.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix


                class Statistics(Entity):
                    """
                    HSRP Group statistics
                    
                    .. attribute:: active_transitions
                    
                    	Number of transitions to Active State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: auth_fail_received
                    
                    	Number of Packets received that failed authentication
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coup_packets_received
                    
                    	Number of Coup Packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coup_packets_sent
                    
                    	Number of Coup Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hello_packets_received
                    
                    	Number of Hello Packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hello_packets_sent
                    
                    	Number of Hello Packets sent (NB\: Bundles only)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: init_transitions
                    
                    	Number of transitions to Init State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_timer_received
                    
                    	Number of packets received with invalid Hello Time value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: learn_transitions
                    
                    	Number of transitions to Learn State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: listen_transitions
                    
                    	Number of transitions to Listen State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mismatch_virtual_ip_address_received
                    
                    	Number of packets received with mismatching virtual IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resign_packets_received
                    
                    	Number of Resign Packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resign_packets_sent
                    
                    	Number of Resign Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: speak_transitions
                    
                    	Number of transitions to Speak State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: standby_transitions
                    
                    	Number of transitions to Standby State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "group"

                        self.active_transitions = YLeaf(YType.uint32, "active-transitions")

                        self.auth_fail_received = YLeaf(YType.uint32, "auth-fail-received")

                        self.coup_packets_received = YLeaf(YType.uint32, "coup-packets-received")

                        self.coup_packets_sent = YLeaf(YType.uint32, "coup-packets-sent")

                        self.hello_packets_received = YLeaf(YType.uint32, "hello-packets-received")

                        self.hello_packets_sent = YLeaf(YType.uint32, "hello-packets-sent")

                        self.init_transitions = YLeaf(YType.uint32, "init-transitions")

                        self.invalid_timer_received = YLeaf(YType.uint32, "invalid-timer-received")

                        self.learn_transitions = YLeaf(YType.uint32, "learn-transitions")

                        self.listen_transitions = YLeaf(YType.uint32, "listen-transitions")

                        self.mismatch_virtual_ip_address_received = YLeaf(YType.uint32, "mismatch-virtual-ip-address-received")

                        self.resign_packets_received = YLeaf(YType.uint32, "resign-packets-received")

                        self.resign_packets_sent = YLeaf(YType.uint32, "resign-packets-sent")

                        self.speak_transitions = YLeaf(YType.uint32, "speak-transitions")

                        self.standby_transitions = YLeaf(YType.uint32, "standby-transitions")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("active_transitions",
                                        "auth_fail_received",
                                        "coup_packets_received",
                                        "coup_packets_sent",
                                        "hello_packets_received",
                                        "hello_packets_sent",
                                        "init_transitions",
                                        "invalid_timer_received",
                                        "learn_transitions",
                                        "listen_transitions",
                                        "mismatch_virtual_ip_address_received",
                                        "resign_packets_received",
                                        "resign_packets_sent",
                                        "speak_transitions",
                                        "standby_transitions") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv6.Groups.Group.Statistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv6.Groups.Group.Statistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.active_transitions.is_set or
                            self.auth_fail_received.is_set or
                            self.coup_packets_received.is_set or
                            self.coup_packets_sent.is_set or
                            self.hello_packets_received.is_set or
                            self.hello_packets_sent.is_set or
                            self.init_transitions.is_set or
                            self.invalid_timer_received.is_set or
                            self.learn_transitions.is_set or
                            self.listen_transitions.is_set or
                            self.mismatch_virtual_ip_address_received.is_set or
                            self.resign_packets_received.is_set or
                            self.resign_packets_sent.is_set or
                            self.speak_transitions.is_set or
                            self.standby_transitions.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.active_transitions.yfilter != YFilter.not_set or
                            self.auth_fail_received.yfilter != YFilter.not_set or
                            self.coup_packets_received.yfilter != YFilter.not_set or
                            self.coup_packets_sent.yfilter != YFilter.not_set or
                            self.hello_packets_received.yfilter != YFilter.not_set or
                            self.hello_packets_sent.yfilter != YFilter.not_set or
                            self.init_transitions.yfilter != YFilter.not_set or
                            self.invalid_timer_received.yfilter != YFilter.not_set or
                            self.learn_transitions.yfilter != YFilter.not_set or
                            self.listen_transitions.yfilter != YFilter.not_set or
                            self.mismatch_virtual_ip_address_received.yfilter != YFilter.not_set or
                            self.resign_packets_received.yfilter != YFilter.not_set or
                            self.resign_packets_sent.yfilter != YFilter.not_set or
                            self.speak_transitions.yfilter != YFilter.not_set or
                            self.standby_transitions.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.active_transitions.is_set or self.active_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_transitions.get_name_leafdata())
                        if (self.auth_fail_received.is_set or self.auth_fail_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auth_fail_received.get_name_leafdata())
                        if (self.coup_packets_received.is_set or self.coup_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.coup_packets_received.get_name_leafdata())
                        if (self.coup_packets_sent.is_set or self.coup_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.coup_packets_sent.get_name_leafdata())
                        if (self.hello_packets_received.is_set or self.hello_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hello_packets_received.get_name_leafdata())
                        if (self.hello_packets_sent.is_set or self.hello_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hello_packets_sent.get_name_leafdata())
                        if (self.init_transitions.is_set or self.init_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.init_transitions.get_name_leafdata())
                        if (self.invalid_timer_received.is_set or self.invalid_timer_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_timer_received.get_name_leafdata())
                        if (self.learn_transitions.is_set or self.learn_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.learn_transitions.get_name_leafdata())
                        if (self.listen_transitions.is_set or self.listen_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.listen_transitions.get_name_leafdata())
                        if (self.mismatch_virtual_ip_address_received.is_set or self.mismatch_virtual_ip_address_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mismatch_virtual_ip_address_received.get_name_leafdata())
                        if (self.resign_packets_received.is_set or self.resign_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resign_packets_received.get_name_leafdata())
                        if (self.resign_packets_sent.is_set or self.resign_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.resign_packets_sent.get_name_leafdata())
                        if (self.speak_transitions.is_set or self.speak_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.speak_transitions.get_name_leafdata())
                        if (self.standby_transitions.is_set or self.standby_transitions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.standby_transitions.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active-transitions" or name == "auth-fail-received" or name == "coup-packets-received" or name == "coup-packets-sent" or name == "hello-packets-received" or name == "hello-packets-sent" or name == "init-transitions" or name == "invalid-timer-received" or name == "learn-transitions" or name == "listen-transitions" or name == "mismatch-virtual-ip-address-received" or name == "resign-packets-received" or name == "resign-packets-sent" or name == "speak-transitions" or name == "standby-transitions"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "active-transitions"):
                            self.active_transitions = value
                            self.active_transitions.value_namespace = name_space
                            self.active_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "auth-fail-received"):
                            self.auth_fail_received = value
                            self.auth_fail_received.value_namespace = name_space
                            self.auth_fail_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "coup-packets-received"):
                            self.coup_packets_received = value
                            self.coup_packets_received.value_namespace = name_space
                            self.coup_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "coup-packets-sent"):
                            self.coup_packets_sent = value
                            self.coup_packets_sent.value_namespace = name_space
                            self.coup_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "hello-packets-received"):
                            self.hello_packets_received = value
                            self.hello_packets_received.value_namespace = name_space
                            self.hello_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "hello-packets-sent"):
                            self.hello_packets_sent = value
                            self.hello_packets_sent.value_namespace = name_space
                            self.hello_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "init-transitions"):
                            self.init_transitions = value
                            self.init_transitions.value_namespace = name_space
                            self.init_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-timer-received"):
                            self.invalid_timer_received = value
                            self.invalid_timer_received.value_namespace = name_space
                            self.invalid_timer_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "learn-transitions"):
                            self.learn_transitions = value
                            self.learn_transitions.value_namespace = name_space
                            self.learn_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "listen-transitions"):
                            self.listen_transitions = value
                            self.listen_transitions.value_namespace = name_space
                            self.listen_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "mismatch-virtual-ip-address-received"):
                            self.mismatch_virtual_ip_address_received = value
                            self.mismatch_virtual_ip_address_received.value_namespace = name_space
                            self.mismatch_virtual_ip_address_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resign-packets-received"):
                            self.resign_packets_received = value
                            self.resign_packets_received.value_namespace = name_space
                            self.resign_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "resign-packets-sent"):
                            self.resign_packets_sent = value
                            self.resign_packets_sent.value_namespace = name_space
                            self.resign_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "speak-transitions"):
                            self.speak_transitions = value
                            self.speak_transitions.value_namespace = name_space
                            self.speak_transitions.value_namespace_prefix = name_space_prefix
                        if(value_path == "standby-transitions"):
                            self.standby_transitions = value
                            self.standby_transitions.value_namespace = name_space
                            self.standby_transitions.value_namespace_prefix = name_space_prefix


                class GlobalAddress(Entity):
                    """
                    Global virtual IPv6 addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.GlobalAddress, self).__init__()

                        self.yang_name = "global-address"
                        self.yang_parent_name = "group"

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipv6_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv6.Groups.Group.GlobalAddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv6.Groups.Group.GlobalAddress, self).__setattr__(name, value)

                    def has_data(self):
                        return self.ipv6_address.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipv6_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "global-address" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv6-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipv6-address"):
                            self.ipv6_address = value
                            self.ipv6_address.value_namespace = name_space
                            self.ipv6_address.value_namespace_prefix = name_space_prefix


                class StateChangeHistory(Entity):
                    """
                    State change history
                    
                    .. attribute:: new_state
                    
                    	New State
                    	**type**\:   :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:   :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:   :py:class:`HsrpStateChangeReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpStateChangeReason>`
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:   :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.StateChangeHistory, self).__init__()

                        self.yang_name = "state-change-history"
                        self.yang_parent_name = "group"

                        self.new_state = YLeaf(YType.enumeration, "new-state")

                        self.old_state = YLeaf(YType.enumeration, "old-state")

                        self.reason = YLeaf(YType.enumeration, "reason")

                        self.time = Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time()
                        self.time.parent = self
                        self._children_name_map["time"] = "time"
                        self._children_yang_names.add("time")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("new_state",
                                        "old_state",
                                        "reason") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv6.Groups.Group.StateChangeHistory, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv6.Groups.Group.StateChangeHistory, self).__setattr__(name, value)


                    class Time(Entity):
                        """
                        Time of state change
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time, self).__init__()

                            self.yang_name = "time"
                            self.yang_parent_name = "state-change-history"

                            self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")

                            self.seconds = YLeaf(YType.uint32, "seconds")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("nanoseconds",
                                            "seconds") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.nanoseconds.is_set or
                                self.seconds.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.nanoseconds.yfilter != YFilter.not_set or
                                self.seconds.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "time" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.nanoseconds.is_set or self.nanoseconds.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nanoseconds.get_name_leafdata())
                            if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.seconds.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "nanoseconds" or name == "seconds"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "nanoseconds"):
                                self.nanoseconds = value
                                self.nanoseconds.value_namespace = name_space
                                self.nanoseconds.value_namespace_prefix = name_space_prefix
                            if(value_path == "seconds"):
                                self.seconds = value
                                self.seconds.value_namespace = name_space
                                self.seconds.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.new_state.is_set or
                            self.old_state.is_set or
                            self.reason.is_set or
                            (self.time is not None and self.time.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.new_state.yfilter != YFilter.not_set or
                            self.old_state.yfilter != YFilter.not_set or
                            self.reason.yfilter != YFilter.not_set or
                            (self.time is not None and self.time.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "state-change-history" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.new_state.is_set or self.new_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.new_state.get_name_leafdata())
                        if (self.old_state.is_set or self.old_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.old_state.get_name_leafdata())
                        if (self.reason.is_set or self.reason.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reason.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "time"):
                            if (self.time is None):
                                self.time = Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time()
                                self.time.parent = self
                                self._children_name_map["time"] = "time"
                            return self.time

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "time" or name == "new-state" or name == "old-state" or name == "reason"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "new-state"):
                            self.new_state = value
                            self.new_state.value_namespace = name_space
                            self.new_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "old-state"):
                            self.old_state = value
                            self.old_state.value_namespace = name_space
                            self.old_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "reason"):
                            self.reason = value
                            self.reason.value_namespace = name_space
                            self.reason.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.global_address:
                        if (c.has_data()):
                            return True
                    for c in self.state_change_history:
                        if (c.has_data()):
                            return True
                    for leaf in self.secondary_address.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.interface_name.is_set or
                        self.group_number.is_set or
                        self.active_ip_address.is_set or
                        self.active_ipv6_address.is_set or
                        self.active_mac_address.is_set or
                        self.active_priority.is_set or
                        self.active_timer_flag.is_set or
                        self.active_timer_msecs.is_set or
                        self.active_timer_secs.is_set or
                        self.address_family.is_set or
                        self.authentication_string.is_set or
                        self.bfd_enabled.is_set or
                        self.bfd_interface.is_set or
                        self.bfd_interval.is_set or
                        self.bfd_multiplier.is_set or
                        self.bfd_peer_ip_address.is_set or
                        self.bfd_peer_ipv6_address.is_set or
                        self.bfd_session_state.is_set or
                        self.configured_mac_address.is_set or
                        self.configured_priority.is_set or
                        self.configured_timers.is_set or
                        self.current_state_timer_secs.is_set or
                        self.delay_timer_flag.is_set or
                        self.delay_timer_msecs.is_set or
                        self.delay_timer_secs.is_set or
                        self.followed_session_name.is_set or
                        self.hello_time.is_set or
                        self.hello_timer_flag.is_set or
                        self.hello_timer_msecs.is_set or
                        self.hello_timer_secs.is_set or
                        self.hold_time.is_set or
                        self.hsrp_group_number.is_set or
                        self.hsrp_router_state.is_set or
                        self.interface.is_set or
                        self.interface_name_xr.is_set or
                        self.is_slave.is_set or
                        self.learned_hello_time.is_set or
                        self.learned_hold_time.is_set or
                        self.min_delay_time.is_set or
                        self.preempt_delay.is_set or
                        self.preempt_enabled.is_set or
                        self.preempt_timer_secs.is_set or
                        self.redirects_disabled.is_set or
                        self.reload_delay_time.is_set or
                        self.router_priority.is_set or
                        self.session_name.is_set or
                        self.slaves.is_set or
                        self.standby_ip_address.is_set or
                        self.standby_ipv6_address.is_set or
                        self.standby_mac_address.is_set or
                        self.standby_timer_flag.is_set or
                        self.standby_timer_msecs.is_set or
                        self.standby_timer_secs.is_set or
                        self.state_change_count.is_set or
                        self.tracked_interface_count.is_set or
                        self.tracked_interface_up_count.is_set or
                        self.use_bia_configured.is_set or
                        self.use_configured_timers.is_set or
                        self.use_configured_virtual_ip.is_set or
                        self.version.is_set or
                        self.virtual_ip_address.is_set or
                        self.virtual_linklocal_ipv6_address.is_set or
                        self.virtual_mac_address.is_set or
                        self.virtual_mac_address_state.is_set or
                        (self.coup_received_time is not None and self.coup_received_time.has_data()) or
                        (self.coup_sent_time is not None and self.coup_sent_time.has_data()) or
                        (self.resign_received_time is not None and self.resign_received_time.has_data()) or
                        (self.resign_sent_time is not None and self.resign_sent_time.has_data()) or
                        (self.statistics is not None and self.statistics.has_data()))

                def has_operation(self):
                    for c in self.global_address:
                        if (c.has_operation()):
                            return True
                    for c in self.state_change_history:
                        if (c.has_operation()):
                            return True
                    for leaf in self.secondary_address.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.group_number.yfilter != YFilter.not_set or
                        self.active_ip_address.yfilter != YFilter.not_set or
                        self.active_ipv6_address.yfilter != YFilter.not_set or
                        self.active_mac_address.yfilter != YFilter.not_set or
                        self.active_priority.yfilter != YFilter.not_set or
                        self.active_timer_flag.yfilter != YFilter.not_set or
                        self.active_timer_msecs.yfilter != YFilter.not_set or
                        self.active_timer_secs.yfilter != YFilter.not_set or
                        self.address_family.yfilter != YFilter.not_set or
                        self.authentication_string.yfilter != YFilter.not_set or
                        self.bfd_enabled.yfilter != YFilter.not_set or
                        self.bfd_interface.yfilter != YFilter.not_set or
                        self.bfd_interval.yfilter != YFilter.not_set or
                        self.bfd_multiplier.yfilter != YFilter.not_set or
                        self.bfd_peer_ip_address.yfilter != YFilter.not_set or
                        self.bfd_peer_ipv6_address.yfilter != YFilter.not_set or
                        self.bfd_session_state.yfilter != YFilter.not_set or
                        self.configured_mac_address.yfilter != YFilter.not_set or
                        self.configured_priority.yfilter != YFilter.not_set or
                        self.configured_timers.yfilter != YFilter.not_set or
                        self.current_state_timer_secs.yfilter != YFilter.not_set or
                        self.delay_timer_flag.yfilter != YFilter.not_set or
                        self.delay_timer_msecs.yfilter != YFilter.not_set or
                        self.delay_timer_secs.yfilter != YFilter.not_set or
                        self.followed_session_name.yfilter != YFilter.not_set or
                        self.hello_time.yfilter != YFilter.not_set or
                        self.hello_timer_flag.yfilter != YFilter.not_set or
                        self.hello_timer_msecs.yfilter != YFilter.not_set or
                        self.hello_timer_secs.yfilter != YFilter.not_set or
                        self.hold_time.yfilter != YFilter.not_set or
                        self.hsrp_group_number.yfilter != YFilter.not_set or
                        self.hsrp_router_state.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.interface_name_xr.yfilter != YFilter.not_set or
                        self.is_slave.yfilter != YFilter.not_set or
                        self.learned_hello_time.yfilter != YFilter.not_set or
                        self.learned_hold_time.yfilter != YFilter.not_set or
                        self.min_delay_time.yfilter != YFilter.not_set or
                        self.preempt_delay.yfilter != YFilter.not_set or
                        self.preempt_enabled.yfilter != YFilter.not_set or
                        self.preempt_timer_secs.yfilter != YFilter.not_set or
                        self.redirects_disabled.yfilter != YFilter.not_set or
                        self.reload_delay_time.yfilter != YFilter.not_set or
                        self.router_priority.yfilter != YFilter.not_set or
                        self.secondary_address.yfilter != YFilter.not_set or
                        self.session_name.yfilter != YFilter.not_set or
                        self.slaves.yfilter != YFilter.not_set or
                        self.standby_ip_address.yfilter != YFilter.not_set or
                        self.standby_ipv6_address.yfilter != YFilter.not_set or
                        self.standby_mac_address.yfilter != YFilter.not_set or
                        self.standby_timer_flag.yfilter != YFilter.not_set or
                        self.standby_timer_msecs.yfilter != YFilter.not_set or
                        self.standby_timer_secs.yfilter != YFilter.not_set or
                        self.state_change_count.yfilter != YFilter.not_set or
                        self.tracked_interface_count.yfilter != YFilter.not_set or
                        self.tracked_interface_up_count.yfilter != YFilter.not_set or
                        self.use_bia_configured.yfilter != YFilter.not_set or
                        self.use_configured_timers.yfilter != YFilter.not_set or
                        self.use_configured_virtual_ip.yfilter != YFilter.not_set or
                        self.version.yfilter != YFilter.not_set or
                        self.virtual_ip_address.yfilter != YFilter.not_set or
                        self.virtual_linklocal_ipv6_address.yfilter != YFilter.not_set or
                        self.virtual_mac_address.yfilter != YFilter.not_set or
                        self.virtual_mac_address_state.yfilter != YFilter.not_set or
                        (self.coup_received_time is not None and self.coup_received_time.has_operation()) or
                        (self.coup_sent_time is not None and self.coup_sent_time.has_operation()) or
                        (self.resign_received_time is not None and self.resign_received_time.has_operation()) or
                        (self.resign_sent_time is not None and self.resign_sent_time.has_operation()) or
                        (self.statistics is not None and self.statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "group" + "[interface-name='" + self.interface_name.get() + "']" + "[group-number='" + self.group_number.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.group_number.is_set or self.group_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_number.get_name_leafdata())
                    if (self.active_ip_address.is_set or self.active_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_ip_address.get_name_leafdata())
                    if (self.active_ipv6_address.is_set or self.active_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_ipv6_address.get_name_leafdata())
                    if (self.active_mac_address.is_set or self.active_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_mac_address.get_name_leafdata())
                    if (self.active_priority.is_set or self.active_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_priority.get_name_leafdata())
                    if (self.active_timer_flag.is_set or self.active_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_timer_flag.get_name_leafdata())
                    if (self.active_timer_msecs.is_set or self.active_timer_msecs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_timer_msecs.get_name_leafdata())
                    if (self.active_timer_secs.is_set or self.active_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_timer_secs.get_name_leafdata())
                    if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_family.get_name_leafdata())
                    if (self.authentication_string.is_set or self.authentication_string.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_string.get_name_leafdata())
                    if (self.bfd_enabled.is_set or self.bfd_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_enabled.get_name_leafdata())
                    if (self.bfd_interface.is_set or self.bfd_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_interface.get_name_leafdata())
                    if (self.bfd_interval.is_set or self.bfd_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_interval.get_name_leafdata())
                    if (self.bfd_multiplier.is_set or self.bfd_multiplier.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_multiplier.get_name_leafdata())
                    if (self.bfd_peer_ip_address.is_set or self.bfd_peer_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_peer_ip_address.get_name_leafdata())
                    if (self.bfd_peer_ipv6_address.is_set or self.bfd_peer_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_peer_ipv6_address.get_name_leafdata())
                    if (self.bfd_session_state.is_set or self.bfd_session_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_session_state.get_name_leafdata())
                    if (self.configured_mac_address.is_set or self.configured_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_mac_address.get_name_leafdata())
                    if (self.configured_priority.is_set or self.configured_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_priority.get_name_leafdata())
                    if (self.configured_timers.is_set or self.configured_timers.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_timers.get_name_leafdata())
                    if (self.current_state_timer_secs.is_set or self.current_state_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_state_timer_secs.get_name_leafdata())
                    if (self.delay_timer_flag.is_set or self.delay_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_flag.get_name_leafdata())
                    if (self.delay_timer_msecs.is_set or self.delay_timer_msecs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_msecs.get_name_leafdata())
                    if (self.delay_timer_secs.is_set or self.delay_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_secs.get_name_leafdata())
                    if (self.followed_session_name.is_set or self.followed_session_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.followed_session_name.get_name_leafdata())
                    if (self.hello_time.is_set or self.hello_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hello_time.get_name_leafdata())
                    if (self.hello_timer_flag.is_set or self.hello_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hello_timer_flag.get_name_leafdata())
                    if (self.hello_timer_msecs.is_set or self.hello_timer_msecs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hello_timer_msecs.get_name_leafdata())
                    if (self.hello_timer_secs.is_set or self.hello_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hello_timer_secs.get_name_leafdata())
                    if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hold_time.get_name_leafdata())
                    if (self.hsrp_group_number.is_set or self.hsrp_group_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hsrp_group_number.get_name_leafdata())
                    if (self.hsrp_router_state.is_set or self.hsrp_router_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hsrp_router_state.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                    if (self.is_slave.is_set or self.is_slave.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_slave.get_name_leafdata())
                    if (self.learned_hello_time.is_set or self.learned_hello_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.learned_hello_time.get_name_leafdata())
                    if (self.learned_hold_time.is_set or self.learned_hold_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.learned_hold_time.get_name_leafdata())
                    if (self.min_delay_time.is_set or self.min_delay_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.min_delay_time.get_name_leafdata())
                    if (self.preempt_delay.is_set or self.preempt_delay.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.preempt_delay.get_name_leafdata())
                    if (self.preempt_enabled.is_set or self.preempt_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.preempt_enabled.get_name_leafdata())
                    if (self.preempt_timer_secs.is_set or self.preempt_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.preempt_timer_secs.get_name_leafdata())
                    if (self.redirects_disabled.is_set or self.redirects_disabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redirects_disabled.get_name_leafdata())
                    if (self.reload_delay_time.is_set or self.reload_delay_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reload_delay_time.get_name_leafdata())
                    if (self.router_priority.is_set or self.router_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router_priority.get_name_leafdata())
                    if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_name.get_name_leafdata())
                    if (self.slaves.is_set or self.slaves.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.slaves.get_name_leafdata())
                    if (self.standby_ip_address.is_set or self.standby_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_ip_address.get_name_leafdata())
                    if (self.standby_ipv6_address.is_set or self.standby_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_ipv6_address.get_name_leafdata())
                    if (self.standby_mac_address.is_set or self.standby_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_mac_address.get_name_leafdata())
                    if (self.standby_timer_flag.is_set or self.standby_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_timer_flag.get_name_leafdata())
                    if (self.standby_timer_msecs.is_set or self.standby_timer_msecs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_timer_msecs.get_name_leafdata())
                    if (self.standby_timer_secs.is_set or self.standby_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_timer_secs.get_name_leafdata())
                    if (self.state_change_count.is_set or self.state_change_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state_change_count.get_name_leafdata())
                    if (self.tracked_interface_count.is_set or self.tracked_interface_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_count.get_name_leafdata())
                    if (self.tracked_interface_up_count.is_set or self.tracked_interface_up_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_up_count.get_name_leafdata())
                    if (self.use_bia_configured.is_set or self.use_bia_configured.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.use_bia_configured.get_name_leafdata())
                    if (self.use_configured_timers.is_set or self.use_configured_timers.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.use_configured_timers.get_name_leafdata())
                    if (self.use_configured_virtual_ip.is_set or self.use_configured_virtual_ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.use_configured_virtual_ip.get_name_leafdata())
                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version.get_name_leafdata())
                    if (self.virtual_ip_address.is_set or self.virtual_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_ip_address.get_name_leafdata())
                    if (self.virtual_linklocal_ipv6_address.is_set or self.virtual_linklocal_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_linklocal_ipv6_address.get_name_leafdata())
                    if (self.virtual_mac_address.is_set or self.virtual_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_mac_address.get_name_leafdata())
                    if (self.virtual_mac_address_state.is_set or self.virtual_mac_address_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_mac_address_state.get_name_leafdata())

                    leaf_name_data.extend(self.secondary_address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "coup-received-time"):
                        if (self.coup_received_time is None):
                            self.coup_received_time = Hsrp.Ipv6.Groups.Group.CoupReceivedTime()
                            self.coup_received_time.parent = self
                            self._children_name_map["coup_received_time"] = "coup-received-time"
                        return self.coup_received_time

                    if (child_yang_name == "coup-sent-time"):
                        if (self.coup_sent_time is None):
                            self.coup_sent_time = Hsrp.Ipv6.Groups.Group.CoupSentTime()
                            self.coup_sent_time.parent = self
                            self._children_name_map["coup_sent_time"] = "coup-sent-time"
                        return self.coup_sent_time

                    if (child_yang_name == "global-address"):
                        for c in self.global_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Hsrp.Ipv6.Groups.Group.GlobalAddress()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.global_address.append(c)
                        return c

                    if (child_yang_name == "resign-received-time"):
                        if (self.resign_received_time is None):
                            self.resign_received_time = Hsrp.Ipv6.Groups.Group.ResignReceivedTime()
                            self.resign_received_time.parent = self
                            self._children_name_map["resign_received_time"] = "resign-received-time"
                        return self.resign_received_time

                    if (child_yang_name == "resign-sent-time"):
                        if (self.resign_sent_time is None):
                            self.resign_sent_time = Hsrp.Ipv6.Groups.Group.ResignSentTime()
                            self.resign_sent_time.parent = self
                            self._children_name_map["resign_sent_time"] = "resign-sent-time"
                        return self.resign_sent_time

                    if (child_yang_name == "state-change-history"):
                        for c in self.state_change_history:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Hsrp.Ipv6.Groups.Group.StateChangeHistory()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.state_change_history.append(c)
                        return c

                    if (child_yang_name == "statistics"):
                        if (self.statistics is None):
                            self.statistics = Hsrp.Ipv6.Groups.Group.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                        return self.statistics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "coup-received-time" or name == "coup-sent-time" or name == "global-address" or name == "resign-received-time" or name == "resign-sent-time" or name == "state-change-history" or name == "statistics" or name == "interface-name" or name == "group-number" or name == "active-ip-address" or name == "active-ipv6-address" or name == "active-mac-address" or name == "active-priority" or name == "active-timer-flag" or name == "active-timer-msecs" or name == "active-timer-secs" or name == "address-family" or name == "authentication-string" or name == "bfd-enabled" or name == "bfd-interface" or name == "bfd-interval" or name == "bfd-multiplier" or name == "bfd-peer-ip-address" or name == "bfd-peer-ipv6-address" or name == "bfd-session-state" or name == "configured-mac-address" or name == "configured-priority" or name == "configured-timers" or name == "current-state-timer-secs" or name == "delay-timer-flag" or name == "delay-timer-msecs" or name == "delay-timer-secs" or name == "followed-session-name" or name == "hello-time" or name == "hello-timer-flag" or name == "hello-timer-msecs" or name == "hello-timer-secs" or name == "hold-time" or name == "hsrp-group-number" or name == "hsrp-router-state" or name == "interface" or name == "interface-name-xr" or name == "is-slave" or name == "learned-hello-time" or name == "learned-hold-time" or name == "min-delay-time" or name == "preempt-delay" or name == "preempt-enabled" or name == "preempt-timer-secs" or name == "redirects-disabled" or name == "reload-delay-time" or name == "router-priority" or name == "secondary-address" or name == "session-name" or name == "slaves" or name == "standby-ip-address" or name == "standby-ipv6-address" or name == "standby-mac-address" or name == "standby-timer-flag" or name == "standby-timer-msecs" or name == "standby-timer-secs" or name == "state-change-count" or name == "tracked-interface-count" or name == "tracked-interface-up-count" or name == "use-bia-configured" or name == "use-configured-timers" or name == "use-configured-virtual-ip" or name == "version" or name == "virtual-ip-address" or name == "virtual-linklocal-ipv6-address" or name == "virtual-mac-address" or name == "virtual-mac-address-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "group-number"):
                        self.group_number = value
                        self.group_number.value_namespace = name_space
                        self.group_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-ip-address"):
                        self.active_ip_address = value
                        self.active_ip_address.value_namespace = name_space
                        self.active_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-ipv6-address"):
                        self.active_ipv6_address = value
                        self.active_ipv6_address.value_namespace = name_space
                        self.active_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-mac-address"):
                        self.active_mac_address = value
                        self.active_mac_address.value_namespace = name_space
                        self.active_mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-priority"):
                        self.active_priority = value
                        self.active_priority.value_namespace = name_space
                        self.active_priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-timer-flag"):
                        self.active_timer_flag = value
                        self.active_timer_flag.value_namespace = name_space
                        self.active_timer_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-timer-msecs"):
                        self.active_timer_msecs = value
                        self.active_timer_msecs.value_namespace = name_space
                        self.active_timer_msecs.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-timer-secs"):
                        self.active_timer_secs = value
                        self.active_timer_secs.value_namespace = name_space
                        self.active_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "address-family"):
                        self.address_family = value
                        self.address_family.value_namespace = name_space
                        self.address_family.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-string"):
                        self.authentication_string = value
                        self.authentication_string.value_namespace = name_space
                        self.authentication_string.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-enabled"):
                        self.bfd_enabled = value
                        self.bfd_enabled.value_namespace = name_space
                        self.bfd_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-interface"):
                        self.bfd_interface = value
                        self.bfd_interface.value_namespace = name_space
                        self.bfd_interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-interval"):
                        self.bfd_interval = value
                        self.bfd_interval.value_namespace = name_space
                        self.bfd_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-multiplier"):
                        self.bfd_multiplier = value
                        self.bfd_multiplier.value_namespace = name_space
                        self.bfd_multiplier.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-peer-ip-address"):
                        self.bfd_peer_ip_address = value
                        self.bfd_peer_ip_address.value_namespace = name_space
                        self.bfd_peer_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-peer-ipv6-address"):
                        self.bfd_peer_ipv6_address = value
                        self.bfd_peer_ipv6_address.value_namespace = name_space
                        self.bfd_peer_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-session-state"):
                        self.bfd_session_state = value
                        self.bfd_session_state.value_namespace = name_space
                        self.bfd_session_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "configured-mac-address"):
                        self.configured_mac_address = value
                        self.configured_mac_address.value_namespace = name_space
                        self.configured_mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "configured-priority"):
                        self.configured_priority = value
                        self.configured_priority.value_namespace = name_space
                        self.configured_priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "configured-timers"):
                        self.configured_timers = value
                        self.configured_timers.value_namespace = name_space
                        self.configured_timers.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-state-timer-secs"):
                        self.current_state_timer_secs = value
                        self.current_state_timer_secs.value_namespace = name_space
                        self.current_state_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "delay-timer-flag"):
                        self.delay_timer_flag = value
                        self.delay_timer_flag.value_namespace = name_space
                        self.delay_timer_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "delay-timer-msecs"):
                        self.delay_timer_msecs = value
                        self.delay_timer_msecs.value_namespace = name_space
                        self.delay_timer_msecs.value_namespace_prefix = name_space_prefix
                    if(value_path == "delay-timer-secs"):
                        self.delay_timer_secs = value
                        self.delay_timer_secs.value_namespace = name_space
                        self.delay_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "followed-session-name"):
                        self.followed_session_name = value
                        self.followed_session_name.value_namespace = name_space
                        self.followed_session_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "hello-time"):
                        self.hello_time = value
                        self.hello_time.value_namespace = name_space
                        self.hello_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "hello-timer-flag"):
                        self.hello_timer_flag = value
                        self.hello_timer_flag.value_namespace = name_space
                        self.hello_timer_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "hello-timer-msecs"):
                        self.hello_timer_msecs = value
                        self.hello_timer_msecs.value_namespace = name_space
                        self.hello_timer_msecs.value_namespace_prefix = name_space_prefix
                    if(value_path == "hello-timer-secs"):
                        self.hello_timer_secs = value
                        self.hello_timer_secs.value_namespace = name_space
                        self.hello_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "hold-time"):
                        self.hold_time = value
                        self.hold_time.value_namespace = name_space
                        self.hold_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "hsrp-group-number"):
                        self.hsrp_group_number = value
                        self.hsrp_group_number.value_namespace = name_space
                        self.hsrp_group_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "hsrp-router-state"):
                        self.hsrp_router_state = value
                        self.hsrp_router_state.value_namespace = name_space
                        self.hsrp_router_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-name-xr"):
                        self.interface_name_xr = value
                        self.interface_name_xr.value_namespace = name_space
                        self.interface_name_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-slave"):
                        self.is_slave = value
                        self.is_slave.value_namespace = name_space
                        self.is_slave.value_namespace_prefix = name_space_prefix
                    if(value_path == "learned-hello-time"):
                        self.learned_hello_time = value
                        self.learned_hello_time.value_namespace = name_space
                        self.learned_hello_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "learned-hold-time"):
                        self.learned_hold_time = value
                        self.learned_hold_time.value_namespace = name_space
                        self.learned_hold_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "min-delay-time"):
                        self.min_delay_time = value
                        self.min_delay_time.value_namespace = name_space
                        self.min_delay_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "preempt-delay"):
                        self.preempt_delay = value
                        self.preempt_delay.value_namespace = name_space
                        self.preempt_delay.value_namespace_prefix = name_space_prefix
                    if(value_path == "preempt-enabled"):
                        self.preempt_enabled = value
                        self.preempt_enabled.value_namespace = name_space
                        self.preempt_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "preempt-timer-secs"):
                        self.preempt_timer_secs = value
                        self.preempt_timer_secs.value_namespace = name_space
                        self.preempt_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "redirects-disabled"):
                        self.redirects_disabled = value
                        self.redirects_disabled.value_namespace = name_space
                        self.redirects_disabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "reload-delay-time"):
                        self.reload_delay_time = value
                        self.reload_delay_time.value_namespace = name_space
                        self.reload_delay_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "router-priority"):
                        self.router_priority = value
                        self.router_priority.value_namespace = name_space
                        self.router_priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "secondary-address"):
                        self.secondary_address.append(value)
                    if(value_path == "session-name"):
                        self.session_name = value
                        self.session_name.value_namespace = name_space
                        self.session_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "slaves"):
                        self.slaves = value
                        self.slaves.value_namespace = name_space
                        self.slaves.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-ip-address"):
                        self.standby_ip_address = value
                        self.standby_ip_address.value_namespace = name_space
                        self.standby_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-ipv6-address"):
                        self.standby_ipv6_address = value
                        self.standby_ipv6_address.value_namespace = name_space
                        self.standby_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-mac-address"):
                        self.standby_mac_address = value
                        self.standby_mac_address.value_namespace = name_space
                        self.standby_mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-timer-flag"):
                        self.standby_timer_flag = value
                        self.standby_timer_flag.value_namespace = name_space
                        self.standby_timer_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-timer-msecs"):
                        self.standby_timer_msecs = value
                        self.standby_timer_msecs.value_namespace = name_space
                        self.standby_timer_msecs.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-timer-secs"):
                        self.standby_timer_secs = value
                        self.standby_timer_secs.value_namespace = name_space
                        self.standby_timer_secs.value_namespace_prefix = name_space_prefix
                    if(value_path == "state-change-count"):
                        self.state_change_count = value
                        self.state_change_count.value_namespace = name_space
                        self.state_change_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-count"):
                        self.tracked_interface_count = value
                        self.tracked_interface_count.value_namespace = name_space
                        self.tracked_interface_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-up-count"):
                        self.tracked_interface_up_count = value
                        self.tracked_interface_up_count.value_namespace = name_space
                        self.tracked_interface_up_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "use-bia-configured"):
                        self.use_bia_configured = value
                        self.use_bia_configured.value_namespace = name_space
                        self.use_bia_configured.value_namespace_prefix = name_space_prefix
                    if(value_path == "use-configured-timers"):
                        self.use_configured_timers = value
                        self.use_configured_timers.value_namespace = name_space
                        self.use_configured_timers.value_namespace_prefix = name_space_prefix
                    if(value_path == "use-configured-virtual-ip"):
                        self.use_configured_virtual_ip = value
                        self.use_configured_virtual_ip.value_namespace = name_space
                        self.use_configured_virtual_ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "version"):
                        self.version = value
                        self.version.value_namespace = name_space
                        self.version.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-ip-address"):
                        self.virtual_ip_address = value
                        self.virtual_ip_address.value_namespace = name_space
                        self.virtual_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-linklocal-ipv6-address"):
                        self.virtual_linklocal_ipv6_address = value
                        self.virtual_linklocal_ipv6_address.value_namespace = name_space
                        self.virtual_linklocal_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-mac-address"):
                        self.virtual_mac_address = value
                        self.virtual_mac_address.value_namespace = name_space
                        self.virtual_mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-mac-address-state"):
                        self.virtual_mac_address_state = value
                        self.virtual_mac_address_state.value_namespace = name_space
                        self.virtual_mac_address_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "group"):
                    for c in self.group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Hsrp.Ipv6.Groups.Group()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Interfaces(Entity):
            """
            The HSRP interface information table
            
            .. attribute:: interface
            
            	A HSRP interface entry
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv6.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "ipv6"

                self.interface = YList(self)

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
                            super(Hsrp.Ipv6.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Hsrp.Ipv6.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                A HSRP interface entry
                
                .. attribute:: interface_name  <key>
                
                	The interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: statistics
                
                	HSRP Interface Statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Interfaces.Interface.Statistics>`
                
                .. attribute:: use_bia_flag
                
                	Use burnt in mac address flag
                	**type**\:  bool
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv6.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface = YLeaf(YType.str, "interface")

                    self.use_bia_flag = YLeaf(YType.boolean, "use-bia-flag")

                    self.statistics = Hsrp.Ipv6.Interfaces.Interface.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "interface",
                                    "use_bia_flag") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Hsrp.Ipv6.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Hsrp.Ipv6.Interfaces.Interface, self).__setattr__(name, value)


                class Statistics(Entity):
                    """
                    HSRP Interface Statistics
                    
                    .. attribute:: advert_packets_received
                    
                    	Number of advertisement packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: advert_packets_sent
                    
                    	Number of advertisement packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: conflict_source_ip_address_received
                    
                    	Number of packets received from a conflicting Source IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inoperational_group_received
                    
                    	Number of packets received for an inoperational group
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_operation_code_received
                    
                    	Number of packets received with invalid operation code
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_version_received
                    
                    	Number of packets received with invalid version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: long_packets_received
                    
                    	Number of packets received that were too Long
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: short_packets_received
                    
                    	Number of packets received that were too short
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_group_received
                    
                    	Number of packets received for an unknown group id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Interfaces.Interface.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "interface"

                        self.advert_packets_received = YLeaf(YType.uint32, "advert-packets-received")

                        self.advert_packets_sent = YLeaf(YType.uint32, "advert-packets-sent")

                        self.conflict_source_ip_address_received = YLeaf(YType.uint32, "conflict-source-ip-address-received")

                        self.inoperational_group_received = YLeaf(YType.uint32, "inoperational-group-received")

                        self.invalid_operation_code_received = YLeaf(YType.uint32, "invalid-operation-code-received")

                        self.invalid_version_received = YLeaf(YType.uint32, "invalid-version-received")

                        self.long_packets_received = YLeaf(YType.uint32, "long-packets-received")

                        self.short_packets_received = YLeaf(YType.uint32, "short-packets-received")

                        self.unknown_group_received = YLeaf(YType.uint32, "unknown-group-received")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("advert_packets_received",
                                        "advert_packets_sent",
                                        "conflict_source_ip_address_received",
                                        "inoperational_group_received",
                                        "invalid_operation_code_received",
                                        "invalid_version_received",
                                        "long_packets_received",
                                        "short_packets_received",
                                        "unknown_group_received") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Hsrp.Ipv6.Interfaces.Interface.Statistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Ipv6.Interfaces.Interface.Statistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.advert_packets_received.is_set or
                            self.advert_packets_sent.is_set or
                            self.conflict_source_ip_address_received.is_set or
                            self.inoperational_group_received.is_set or
                            self.invalid_operation_code_received.is_set or
                            self.invalid_version_received.is_set or
                            self.long_packets_received.is_set or
                            self.short_packets_received.is_set or
                            self.unknown_group_received.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.advert_packets_received.yfilter != YFilter.not_set or
                            self.advert_packets_sent.yfilter != YFilter.not_set or
                            self.conflict_source_ip_address_received.yfilter != YFilter.not_set or
                            self.inoperational_group_received.yfilter != YFilter.not_set or
                            self.invalid_operation_code_received.yfilter != YFilter.not_set or
                            self.invalid_version_received.yfilter != YFilter.not_set or
                            self.long_packets_received.yfilter != YFilter.not_set or
                            self.short_packets_received.yfilter != YFilter.not_set or
                            self.unknown_group_received.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.advert_packets_received.is_set or self.advert_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.advert_packets_received.get_name_leafdata())
                        if (self.advert_packets_sent.is_set or self.advert_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.advert_packets_sent.get_name_leafdata())
                        if (self.conflict_source_ip_address_received.is_set or self.conflict_source_ip_address_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conflict_source_ip_address_received.get_name_leafdata())
                        if (self.inoperational_group_received.is_set or self.inoperational_group_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inoperational_group_received.get_name_leafdata())
                        if (self.invalid_operation_code_received.is_set or self.invalid_operation_code_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_operation_code_received.get_name_leafdata())
                        if (self.invalid_version_received.is_set or self.invalid_version_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_version_received.get_name_leafdata())
                        if (self.long_packets_received.is_set or self.long_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.long_packets_received.get_name_leafdata())
                        if (self.short_packets_received.is_set or self.short_packets_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.short_packets_received.get_name_leafdata())
                        if (self.unknown_group_received.is_set or self.unknown_group_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unknown_group_received.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "advert-packets-received" or name == "advert-packets-sent" or name == "conflict-source-ip-address-received" or name == "inoperational-group-received" or name == "invalid-operation-code-received" or name == "invalid-version-received" or name == "long-packets-received" or name == "short-packets-received" or name == "unknown-group-received"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "advert-packets-received"):
                            self.advert_packets_received = value
                            self.advert_packets_received.value_namespace = name_space
                            self.advert_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "advert-packets-sent"):
                            self.advert_packets_sent = value
                            self.advert_packets_sent.value_namespace = name_space
                            self.advert_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "conflict-source-ip-address-received"):
                            self.conflict_source_ip_address_received = value
                            self.conflict_source_ip_address_received.value_namespace = name_space
                            self.conflict_source_ip_address_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "inoperational-group-received"):
                            self.inoperational_group_received = value
                            self.inoperational_group_received.value_namespace = name_space
                            self.inoperational_group_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-operation-code-received"):
                            self.invalid_operation_code_received = value
                            self.invalid_operation_code_received.value_namespace = name_space
                            self.invalid_operation_code_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-version-received"):
                            self.invalid_version_received = value
                            self.invalid_version_received.value_namespace = name_space
                            self.invalid_version_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "long-packets-received"):
                            self.long_packets_received = value
                            self.long_packets_received.value_namespace = name_space
                            self.long_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "short-packets-received"):
                            self.short_packets_received = value
                            self.short_packets_received.value_namespace = name_space
                            self.short_packets_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "unknown-group-received"):
                            self.unknown_group_received = value
                            self.unknown_group_received.value_namespace = name_space
                            self.unknown_group_received.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.interface.is_set or
                        self.use_bia_flag.is_set or
                        (self.statistics is not None and self.statistics.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.use_bia_flag.yfilter != YFilter.not_set or
                        (self.statistics is not None and self.statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.use_bia_flag.is_set or self.use_bia_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.use_bia_flag.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "statistics"):
                        if (self.statistics is None):
                            self.statistics = Hsrp.Ipv6.Interfaces.Interface.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                        return self.statistics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "statistics" or name == "interface-name" or name == "interface" or name == "use-bia-flag"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "use-bia-flag"):
                        self.use_bia_flag = value
                        self.use_bia_flag.value_namespace = name_space
                        self.use_bia_flag.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Hsrp.Ipv6.Interfaces.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.groups is not None and self.groups.has_data()) or
                (self.interfaces is not None and self.interfaces.has_data()) or
                (self.tracked_interfaces is not None and self.tracked_interfaces.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.groups is not None and self.groups.has_operation()) or
                (self.interfaces is not None and self.interfaces.has_operation()) or
                (self.tracked_interfaces is not None and self.tracked_interfaces.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv6" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "groups"):
                if (self.groups is None):
                    self.groups = Hsrp.Ipv6.Groups()
                    self.groups.parent = self
                    self._children_name_map["groups"] = "groups"
                return self.groups

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = Hsrp.Ipv6.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            if (child_yang_name == "tracked-interfaces"):
                if (self.tracked_interfaces is None):
                    self.tracked_interfaces = Hsrp.Ipv6.TrackedInterfaces()
                    self.tracked_interfaces.parent = self
                    self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
                return self.tracked_interfaces

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "groups" or name == "interfaces" or name == "tracked-interfaces"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class BfdSessions(Entity):
        """
        The table of HSRP BFD Sessions
        
        .. attribute:: bfd_session
        
        	An HSRP BFD Session
        	**type**\: list of    :py:class:`BfdSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.BfdSessions.BfdSession>`
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.BfdSessions, self).__init__()

            self.yang_name = "bfd-sessions"
            self.yang_parent_name = "hsrp"

            self.bfd_session = YList(self)

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
                        super(Hsrp.BfdSessions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Hsrp.BfdSessions, self).__setattr__(name, value)


        class BfdSession(Entity):
            """
            An HSRP BFD Session
            
            .. attribute:: interface_name  <key>
            
            	The interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: ip_address  <key>
            
            	Destination IP Address of BFD Session
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: bfd_interface_name
            
            	BFD Interface Name
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: bfd_interval
            
            	BFD packet send interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bfd_multiplier
            
            	BFD multiplier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: bfd_session_state
            
            	BFD session state
            	**type**\:   :py:class:`HsrpBfdSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBfdSessionState>`
            
            .. attribute:: destination_address
            
            	BFD destination address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: destination_ipv6_address
            
            	BFD IPv6 destination address
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: group
            
            	HSRP Groups tracking the BFD session
            	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.BfdSessions.BfdSession.Group>`
            
            .. attribute:: session_address_family
            
            	Session Address family
            	**type**\:   :py:class:`HsrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAf>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.BfdSessions.BfdSession, self).__init__()

                self.yang_name = "bfd-session"
                self.yang_parent_name = "bfd-sessions"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.ip_address = YLeaf(YType.str, "ip-address")

                self.bfd_interface_name = YLeaf(YType.str, "bfd-interface-name")

                self.bfd_interval = YLeaf(YType.uint32, "bfd-interval")

                self.bfd_multiplier = YLeaf(YType.uint32, "bfd-multiplier")

                self.bfd_session_state = YLeaf(YType.enumeration, "bfd-session-state")

                self.destination_address = YLeaf(YType.str, "destination-address")

                self.destination_ipv6_address = YLeaf(YType.str, "destination-ipv6-address")

                self.session_address_family = YLeaf(YType.enumeration, "session-address-family")

                self.group = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name",
                                "ip_address",
                                "bfd_interface_name",
                                "bfd_interval",
                                "bfd_multiplier",
                                "bfd_session_state",
                                "destination_address",
                                "destination_ipv6_address",
                                "session_address_family") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Hsrp.BfdSessions.BfdSession, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Hsrp.BfdSessions.BfdSession, self).__setattr__(name, value)


            class Group(Entity):
                """
                HSRP Groups tracking the BFD session
                
                .. attribute:: hsrp_group_number
                
                	HSRP Group number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_name
                
                	Interface Name
                	**type**\:  str
                
                	**length:** 0..64
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.BfdSessions.BfdSession.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "bfd-session"

                    self.hsrp_group_number = YLeaf(YType.uint32, "hsrp-group-number")

                    self.interface_name = YLeaf(YType.str, "interface-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("hsrp_group_number",
                                    "interface_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Hsrp.BfdSessions.BfdSession.Group, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Hsrp.BfdSessions.BfdSession.Group, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.hsrp_group_number.is_set or
                        self.interface_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.hsrp_group_number.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "group" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.hsrp_group_number.is_set or self.hsrp_group_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hsrp_group_number.get_name_leafdata())
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hsrp-group-number" or name == "interface-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "hsrp-group-number"):
                        self.hsrp_group_number = value
                        self.hsrp_group_number.value_namespace = name_space
                        self.hsrp_group_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.group:
                    if (c.has_data()):
                        return True
                return (
                    self.interface_name.is_set or
                    self.ip_address.is_set or
                    self.bfd_interface_name.is_set or
                    self.bfd_interval.is_set or
                    self.bfd_multiplier.is_set or
                    self.bfd_session_state.is_set or
                    self.destination_address.is_set or
                    self.destination_ipv6_address.is_set or
                    self.session_address_family.is_set)

            def has_operation(self):
                for c in self.group:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.ip_address.yfilter != YFilter.not_set or
                    self.bfd_interface_name.yfilter != YFilter.not_set or
                    self.bfd_interval.yfilter != YFilter.not_set or
                    self.bfd_multiplier.yfilter != YFilter.not_set or
                    self.bfd_session_state.yfilter != YFilter.not_set or
                    self.destination_address.yfilter != YFilter.not_set or
                    self.destination_ipv6_address.yfilter != YFilter.not_set or
                    self.session_address_family.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bfd-session" + "[interface-name='" + self.interface_name.get() + "']" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/bfd-sessions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ip_address.get_name_leafdata())
                if (self.bfd_interface_name.is_set or self.bfd_interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bfd_interface_name.get_name_leafdata())
                if (self.bfd_interval.is_set or self.bfd_interval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bfd_interval.get_name_leafdata())
                if (self.bfd_multiplier.is_set or self.bfd_multiplier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bfd_multiplier.get_name_leafdata())
                if (self.bfd_session_state.is_set or self.bfd_session_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bfd_session_state.get_name_leafdata())
                if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.destination_address.get_name_leafdata())
                if (self.destination_ipv6_address.is_set or self.destination_ipv6_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.destination_ipv6_address.get_name_leafdata())
                if (self.session_address_family.is_set or self.session_address_family.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_address_family.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "group"):
                    for c in self.group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Hsrp.BfdSessions.BfdSession.Group()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "group" or name == "interface-name" or name == "ip-address" or name == "bfd-interface-name" or name == "bfd-interval" or name == "bfd-multiplier" or name == "bfd-session-state" or name == "destination-address" or name == "destination-ipv6-address" or name == "session-address-family"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "ip-address"):
                    self.ip_address = value
                    self.ip_address.value_namespace = name_space
                    self.ip_address.value_namespace_prefix = name_space_prefix
                if(value_path == "bfd-interface-name"):
                    self.bfd_interface_name = value
                    self.bfd_interface_name.value_namespace = name_space
                    self.bfd_interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "bfd-interval"):
                    self.bfd_interval = value
                    self.bfd_interval.value_namespace = name_space
                    self.bfd_interval.value_namespace_prefix = name_space_prefix
                if(value_path == "bfd-multiplier"):
                    self.bfd_multiplier = value
                    self.bfd_multiplier.value_namespace = name_space
                    self.bfd_multiplier.value_namespace_prefix = name_space_prefix
                if(value_path == "bfd-session-state"):
                    self.bfd_session_state = value
                    self.bfd_session_state.value_namespace = name_space
                    self.bfd_session_state.value_namespace_prefix = name_space_prefix
                if(value_path == "destination-address"):
                    self.destination_address = value
                    self.destination_address.value_namespace = name_space
                    self.destination_address.value_namespace_prefix = name_space_prefix
                if(value_path == "destination-ipv6-address"):
                    self.destination_ipv6_address = value
                    self.destination_ipv6_address.value_namespace = name_space
                    self.destination_ipv6_address.value_namespace_prefix = name_space_prefix
                if(value_path == "session-address-family"):
                    self.session_address_family = value
                    self.session_address_family.value_namespace = name_space
                    self.session_address_family.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.bfd_session:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.bfd_session:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bfd-sessions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bfd-session"):
                for c in self.bfd_session:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Hsrp.BfdSessions.BfdSession()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.bfd_session.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bfd-session"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Summary(Entity):
        """
        HSRP summary statistics
        
        .. attribute:: bfd_session_inactive
        
        	Number of HSRP BFD sessions in INACTIVE state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: bfd_sessions_down
        
        	Number of HSRP BFD sessions in DOWN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: bfd_sessions_up
        
        	Number of HSRP BFD sessions in UP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv4_state_down
        
        	Number of HSRP interfaces with IPv4 caps in DOWN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv4_state_up
        
        	Number of HSRP interfaces with IPv4 caps in UP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv6_state_down
        
        	Number of HSRP interfaces with IPv6 caps in DOWN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv6_state_up
        
        	Number of HSRP interfaces with IPv6 caps in UP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_active
        
        	Number of IPv4 sessions in ACTIVE state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_init
        
        	Number of IPv4 sessions in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_learn
        
        	Number of IPv4 sessions in LEARN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_listen
        
        	Number of IPv4 sessions in LISTEN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_speak
        
        	Number of IPv4 sessions in SPEAK state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_standby
        
        	Number of IPv4 sessions in STANDBY state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_active
        
        	Number of IPv4 slaves in ACTIVE state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_init
        
        	Number of IPv4 slaves in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_learn
        
        	Number of IPv4 slaves in LEARN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_listen
        
        	Number of IPv4 slaves in LISTEN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_speak
        
        	Number of IPv4 slaves in SPEAK state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_standby
        
        	Number of IPv4 slaves in STANDBY state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_active_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in ACTIVE state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_active_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in ACTIVE state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_init_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_init_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_learn_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in LEARN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_learn_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in LEARN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_listen_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in LISTEN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_listen_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in LISTEN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_speak_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in SPEAK state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_speak_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in SPEAK state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_standby_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in STANDBY state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_standby_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in STANDBY state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_active
        
        	Number of IPv6 sessions in ACTIVE state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_init
        
        	Number of IPv6 sessions in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_learn
        
        	Number of IPv6 sessions in LEARN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_listen
        
        	Number of IPv6 sessions in LISTEN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_speak
        
        	Number of IPv6 sessions in SPEAK state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_standby
        
        	Number of IPv6 sessions in STANDBY state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_active
        
        	Number of IPv6 slaves in ACTIVE state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_init
        
        	Number of IPv6 slaves in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_learn
        
        	Number of IPv6 slaves in LEARN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_listen
        
        	Number of IPv6 slaves in LISTEN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_speak
        
        	Number of IPv6 slaves in SPEAK state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_standby
        
        	Number of IPv6 slaves in STANDBY state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_active_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in ACTIVE state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_active_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in ACTIVE state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_init_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_init_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_learn_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in LEARN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_learn_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in LEARN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_listen_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in LISTEN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_listen_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in LISTEN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_speak_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in SPEAK state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_speak_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in SPEAK state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_standby_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in STANDBY state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_standby_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in STANDBY state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv4_state_down
        
        	Number of tracked interfaces with IPv4 caps in DOWN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv4_state_up
        
        	Number of tracked interfaces with IPv4 caps in UP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv6_state_down
        
        	Number of tracked interfaces with IPv6 caps in DOWN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv6_state_up
        
        	Number of tracked interfaces with IPv6 caps in UP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_objects_down
        
        	Number of tracked objects in DOWN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_objects_up
        
        	Number of tracked objects in UP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "hsrp"

            self.bfd_session_inactive = YLeaf(YType.uint32, "bfd-session-inactive")

            self.bfd_sessions_down = YLeaf(YType.uint32, "bfd-sessions-down")

            self.bfd_sessions_up = YLeaf(YType.uint32, "bfd-sessions-up")

            self.interfaces_ipv4_state_down = YLeaf(YType.uint32, "interfaces-ipv4-state-down")

            self.interfaces_ipv4_state_up = YLeaf(YType.uint32, "interfaces-ipv4-state-up")

            self.interfaces_ipv6_state_down = YLeaf(YType.uint32, "interfaces-ipv6-state-down")

            self.interfaces_ipv6_state_up = YLeaf(YType.uint32, "interfaces-ipv6-state-up")

            self.ipv4_sessions_active = YLeaf(YType.uint32, "ipv4-sessions-active")

            self.ipv4_sessions_init = YLeaf(YType.uint32, "ipv4-sessions-init")

            self.ipv4_sessions_learn = YLeaf(YType.uint32, "ipv4-sessions-learn")

            self.ipv4_sessions_listen = YLeaf(YType.uint32, "ipv4-sessions-listen")

            self.ipv4_sessions_speak = YLeaf(YType.uint32, "ipv4-sessions-speak")

            self.ipv4_sessions_standby = YLeaf(YType.uint32, "ipv4-sessions-standby")

            self.ipv4_slaves_active = YLeaf(YType.uint32, "ipv4-slaves-active")

            self.ipv4_slaves_init = YLeaf(YType.uint32, "ipv4-slaves-init")

            self.ipv4_slaves_learn = YLeaf(YType.uint32, "ipv4-slaves-learn")

            self.ipv4_slaves_listen = YLeaf(YType.uint32, "ipv4-slaves-listen")

            self.ipv4_slaves_speak = YLeaf(YType.uint32, "ipv4-slaves-speak")

            self.ipv4_slaves_standby = YLeaf(YType.uint32, "ipv4-slaves-standby")

            self.ipv4_virtual_ip_addresses_active_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-active-down")

            self.ipv4_virtual_ip_addresses_active_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-active-up")

            self.ipv4_virtual_ip_addresses_init_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-init-down")

            self.ipv4_virtual_ip_addresses_init_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-init-up")

            self.ipv4_virtual_ip_addresses_learn_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-learn-down")

            self.ipv4_virtual_ip_addresses_learn_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-learn-up")

            self.ipv4_virtual_ip_addresses_listen_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-listen-down")

            self.ipv4_virtual_ip_addresses_listen_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-listen-up")

            self.ipv4_virtual_ip_addresses_speak_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-speak-down")

            self.ipv4_virtual_ip_addresses_speak_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-speak-up")

            self.ipv4_virtual_ip_addresses_standby_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-standby-down")

            self.ipv4_virtual_ip_addresses_standby_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-standby-up")

            self.ipv6_sessions_active = YLeaf(YType.uint32, "ipv6-sessions-active")

            self.ipv6_sessions_init = YLeaf(YType.uint32, "ipv6-sessions-init")

            self.ipv6_sessions_learn = YLeaf(YType.uint32, "ipv6-sessions-learn")

            self.ipv6_sessions_listen = YLeaf(YType.uint32, "ipv6-sessions-listen")

            self.ipv6_sessions_speak = YLeaf(YType.uint32, "ipv6-sessions-speak")

            self.ipv6_sessions_standby = YLeaf(YType.uint32, "ipv6-sessions-standby")

            self.ipv6_slaves_active = YLeaf(YType.uint32, "ipv6-slaves-active")

            self.ipv6_slaves_init = YLeaf(YType.uint32, "ipv6-slaves-init")

            self.ipv6_slaves_learn = YLeaf(YType.uint32, "ipv6-slaves-learn")

            self.ipv6_slaves_listen = YLeaf(YType.uint32, "ipv6-slaves-listen")

            self.ipv6_slaves_speak = YLeaf(YType.uint32, "ipv6-slaves-speak")

            self.ipv6_slaves_standby = YLeaf(YType.uint32, "ipv6-slaves-standby")

            self.ipv6_virtual_ip_addresses_active_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-active-down")

            self.ipv6_virtual_ip_addresses_active_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-active-up")

            self.ipv6_virtual_ip_addresses_init_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-init-down")

            self.ipv6_virtual_ip_addresses_init_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-init-up")

            self.ipv6_virtual_ip_addresses_learn_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-learn-down")

            self.ipv6_virtual_ip_addresses_learn_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-learn-up")

            self.ipv6_virtual_ip_addresses_listen_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-listen-down")

            self.ipv6_virtual_ip_addresses_listen_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-listen-up")

            self.ipv6_virtual_ip_addresses_speak_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-speak-down")

            self.ipv6_virtual_ip_addresses_speak_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-speak-up")

            self.ipv6_virtual_ip_addresses_standby_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-standby-down")

            self.ipv6_virtual_ip_addresses_standby_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-standby-up")

            self.tracked_interfaces_ipv4_state_down = YLeaf(YType.uint32, "tracked-interfaces-ipv4-state-down")

            self.tracked_interfaces_ipv4_state_up = YLeaf(YType.uint32, "tracked-interfaces-ipv4-state-up")

            self.tracked_interfaces_ipv6_state_down = YLeaf(YType.uint32, "tracked-interfaces-ipv6-state-down")

            self.tracked_interfaces_ipv6_state_up = YLeaf(YType.uint32, "tracked-interfaces-ipv6-state-up")

            self.tracked_objects_down = YLeaf(YType.uint32, "tracked-objects-down")

            self.tracked_objects_up = YLeaf(YType.uint32, "tracked-objects-up")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("bfd_session_inactive",
                            "bfd_sessions_down",
                            "bfd_sessions_up",
                            "interfaces_ipv4_state_down",
                            "interfaces_ipv4_state_up",
                            "interfaces_ipv6_state_down",
                            "interfaces_ipv6_state_up",
                            "ipv4_sessions_active",
                            "ipv4_sessions_init",
                            "ipv4_sessions_learn",
                            "ipv4_sessions_listen",
                            "ipv4_sessions_speak",
                            "ipv4_sessions_standby",
                            "ipv4_slaves_active",
                            "ipv4_slaves_init",
                            "ipv4_slaves_learn",
                            "ipv4_slaves_listen",
                            "ipv4_slaves_speak",
                            "ipv4_slaves_standby",
                            "ipv4_virtual_ip_addresses_active_down",
                            "ipv4_virtual_ip_addresses_active_up",
                            "ipv4_virtual_ip_addresses_init_down",
                            "ipv4_virtual_ip_addresses_init_up",
                            "ipv4_virtual_ip_addresses_learn_down",
                            "ipv4_virtual_ip_addresses_learn_up",
                            "ipv4_virtual_ip_addresses_listen_down",
                            "ipv4_virtual_ip_addresses_listen_up",
                            "ipv4_virtual_ip_addresses_speak_down",
                            "ipv4_virtual_ip_addresses_speak_up",
                            "ipv4_virtual_ip_addresses_standby_down",
                            "ipv4_virtual_ip_addresses_standby_up",
                            "ipv6_sessions_active",
                            "ipv6_sessions_init",
                            "ipv6_sessions_learn",
                            "ipv6_sessions_listen",
                            "ipv6_sessions_speak",
                            "ipv6_sessions_standby",
                            "ipv6_slaves_active",
                            "ipv6_slaves_init",
                            "ipv6_slaves_learn",
                            "ipv6_slaves_listen",
                            "ipv6_slaves_speak",
                            "ipv6_slaves_standby",
                            "ipv6_virtual_ip_addresses_active_down",
                            "ipv6_virtual_ip_addresses_active_up",
                            "ipv6_virtual_ip_addresses_init_down",
                            "ipv6_virtual_ip_addresses_init_up",
                            "ipv6_virtual_ip_addresses_learn_down",
                            "ipv6_virtual_ip_addresses_learn_up",
                            "ipv6_virtual_ip_addresses_listen_down",
                            "ipv6_virtual_ip_addresses_listen_up",
                            "ipv6_virtual_ip_addresses_speak_down",
                            "ipv6_virtual_ip_addresses_speak_up",
                            "ipv6_virtual_ip_addresses_standby_down",
                            "ipv6_virtual_ip_addresses_standby_up",
                            "tracked_interfaces_ipv4_state_down",
                            "tracked_interfaces_ipv4_state_up",
                            "tracked_interfaces_ipv6_state_down",
                            "tracked_interfaces_ipv6_state_up",
                            "tracked_objects_down",
                            "tracked_objects_up") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Hsrp.Summary, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Hsrp.Summary, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.bfd_session_inactive.is_set or
                self.bfd_sessions_down.is_set or
                self.bfd_sessions_up.is_set or
                self.interfaces_ipv4_state_down.is_set or
                self.interfaces_ipv4_state_up.is_set or
                self.interfaces_ipv6_state_down.is_set or
                self.interfaces_ipv6_state_up.is_set or
                self.ipv4_sessions_active.is_set or
                self.ipv4_sessions_init.is_set or
                self.ipv4_sessions_learn.is_set or
                self.ipv4_sessions_listen.is_set or
                self.ipv4_sessions_speak.is_set or
                self.ipv4_sessions_standby.is_set or
                self.ipv4_slaves_active.is_set or
                self.ipv4_slaves_init.is_set or
                self.ipv4_slaves_learn.is_set or
                self.ipv4_slaves_listen.is_set or
                self.ipv4_slaves_speak.is_set or
                self.ipv4_slaves_standby.is_set or
                self.ipv4_virtual_ip_addresses_active_down.is_set or
                self.ipv4_virtual_ip_addresses_active_up.is_set or
                self.ipv4_virtual_ip_addresses_init_down.is_set or
                self.ipv4_virtual_ip_addresses_init_up.is_set or
                self.ipv4_virtual_ip_addresses_learn_down.is_set or
                self.ipv4_virtual_ip_addresses_learn_up.is_set or
                self.ipv4_virtual_ip_addresses_listen_down.is_set or
                self.ipv4_virtual_ip_addresses_listen_up.is_set or
                self.ipv4_virtual_ip_addresses_speak_down.is_set or
                self.ipv4_virtual_ip_addresses_speak_up.is_set or
                self.ipv4_virtual_ip_addresses_standby_down.is_set or
                self.ipv4_virtual_ip_addresses_standby_up.is_set or
                self.ipv6_sessions_active.is_set or
                self.ipv6_sessions_init.is_set or
                self.ipv6_sessions_learn.is_set or
                self.ipv6_sessions_listen.is_set or
                self.ipv6_sessions_speak.is_set or
                self.ipv6_sessions_standby.is_set or
                self.ipv6_slaves_active.is_set or
                self.ipv6_slaves_init.is_set or
                self.ipv6_slaves_learn.is_set or
                self.ipv6_slaves_listen.is_set or
                self.ipv6_slaves_speak.is_set or
                self.ipv6_slaves_standby.is_set or
                self.ipv6_virtual_ip_addresses_active_down.is_set or
                self.ipv6_virtual_ip_addresses_active_up.is_set or
                self.ipv6_virtual_ip_addresses_init_down.is_set or
                self.ipv6_virtual_ip_addresses_init_up.is_set or
                self.ipv6_virtual_ip_addresses_learn_down.is_set or
                self.ipv6_virtual_ip_addresses_learn_up.is_set or
                self.ipv6_virtual_ip_addresses_listen_down.is_set or
                self.ipv6_virtual_ip_addresses_listen_up.is_set or
                self.ipv6_virtual_ip_addresses_speak_down.is_set or
                self.ipv6_virtual_ip_addresses_speak_up.is_set or
                self.ipv6_virtual_ip_addresses_standby_down.is_set or
                self.ipv6_virtual_ip_addresses_standby_up.is_set or
                self.tracked_interfaces_ipv4_state_down.is_set or
                self.tracked_interfaces_ipv4_state_up.is_set or
                self.tracked_interfaces_ipv6_state_down.is_set or
                self.tracked_interfaces_ipv6_state_up.is_set or
                self.tracked_objects_down.is_set or
                self.tracked_objects_up.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.bfd_session_inactive.yfilter != YFilter.not_set or
                self.bfd_sessions_down.yfilter != YFilter.not_set or
                self.bfd_sessions_up.yfilter != YFilter.not_set or
                self.interfaces_ipv4_state_down.yfilter != YFilter.not_set or
                self.interfaces_ipv4_state_up.yfilter != YFilter.not_set or
                self.interfaces_ipv6_state_down.yfilter != YFilter.not_set or
                self.interfaces_ipv6_state_up.yfilter != YFilter.not_set or
                self.ipv4_sessions_active.yfilter != YFilter.not_set or
                self.ipv4_sessions_init.yfilter != YFilter.not_set or
                self.ipv4_sessions_learn.yfilter != YFilter.not_set or
                self.ipv4_sessions_listen.yfilter != YFilter.not_set or
                self.ipv4_sessions_speak.yfilter != YFilter.not_set or
                self.ipv4_sessions_standby.yfilter != YFilter.not_set or
                self.ipv4_slaves_active.yfilter != YFilter.not_set or
                self.ipv4_slaves_init.yfilter != YFilter.not_set or
                self.ipv4_slaves_learn.yfilter != YFilter.not_set or
                self.ipv4_slaves_listen.yfilter != YFilter.not_set or
                self.ipv4_slaves_speak.yfilter != YFilter.not_set or
                self.ipv4_slaves_standby.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_active_down.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_active_up.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_init_down.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_init_up.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_learn_down.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_learn_up.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_listen_down.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_listen_up.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_speak_down.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_speak_up.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_standby_down.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_standby_up.yfilter != YFilter.not_set or
                self.ipv6_sessions_active.yfilter != YFilter.not_set or
                self.ipv6_sessions_init.yfilter != YFilter.not_set or
                self.ipv6_sessions_learn.yfilter != YFilter.not_set or
                self.ipv6_sessions_listen.yfilter != YFilter.not_set or
                self.ipv6_sessions_speak.yfilter != YFilter.not_set or
                self.ipv6_sessions_standby.yfilter != YFilter.not_set or
                self.ipv6_slaves_active.yfilter != YFilter.not_set or
                self.ipv6_slaves_init.yfilter != YFilter.not_set or
                self.ipv6_slaves_learn.yfilter != YFilter.not_set or
                self.ipv6_slaves_listen.yfilter != YFilter.not_set or
                self.ipv6_slaves_speak.yfilter != YFilter.not_set or
                self.ipv6_slaves_standby.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_active_down.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_active_up.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_init_down.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_init_up.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_learn_down.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_learn_up.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_listen_down.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_listen_up.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_speak_down.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_speak_up.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_standby_down.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_standby_up.yfilter != YFilter.not_set or
                self.tracked_interfaces_ipv4_state_down.yfilter != YFilter.not_set or
                self.tracked_interfaces_ipv4_state_up.yfilter != YFilter.not_set or
                self.tracked_interfaces_ipv6_state_down.yfilter != YFilter.not_set or
                self.tracked_interfaces_ipv6_state_up.yfilter != YFilter.not_set or
                self.tracked_objects_down.yfilter != YFilter.not_set or
                self.tracked_objects_up.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "summary" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.bfd_session_inactive.is_set or self.bfd_session_inactive.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bfd_session_inactive.get_name_leafdata())
            if (self.bfd_sessions_down.is_set or self.bfd_sessions_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bfd_sessions_down.get_name_leafdata())
            if (self.bfd_sessions_up.is_set or self.bfd_sessions_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bfd_sessions_up.get_name_leafdata())
            if (self.interfaces_ipv4_state_down.is_set or self.interfaces_ipv4_state_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interfaces_ipv4_state_down.get_name_leafdata())
            if (self.interfaces_ipv4_state_up.is_set or self.interfaces_ipv4_state_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interfaces_ipv4_state_up.get_name_leafdata())
            if (self.interfaces_ipv6_state_down.is_set or self.interfaces_ipv6_state_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interfaces_ipv6_state_down.get_name_leafdata())
            if (self.interfaces_ipv6_state_up.is_set or self.interfaces_ipv6_state_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interfaces_ipv6_state_up.get_name_leafdata())
            if (self.ipv4_sessions_active.is_set or self.ipv4_sessions_active.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_sessions_active.get_name_leafdata())
            if (self.ipv4_sessions_init.is_set or self.ipv4_sessions_init.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_sessions_init.get_name_leafdata())
            if (self.ipv4_sessions_learn.is_set or self.ipv4_sessions_learn.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_sessions_learn.get_name_leafdata())
            if (self.ipv4_sessions_listen.is_set or self.ipv4_sessions_listen.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_sessions_listen.get_name_leafdata())
            if (self.ipv4_sessions_speak.is_set or self.ipv4_sessions_speak.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_sessions_speak.get_name_leafdata())
            if (self.ipv4_sessions_standby.is_set or self.ipv4_sessions_standby.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_sessions_standby.get_name_leafdata())
            if (self.ipv4_slaves_active.is_set or self.ipv4_slaves_active.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_slaves_active.get_name_leafdata())
            if (self.ipv4_slaves_init.is_set or self.ipv4_slaves_init.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_slaves_init.get_name_leafdata())
            if (self.ipv4_slaves_learn.is_set or self.ipv4_slaves_learn.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_slaves_learn.get_name_leafdata())
            if (self.ipv4_slaves_listen.is_set or self.ipv4_slaves_listen.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_slaves_listen.get_name_leafdata())
            if (self.ipv4_slaves_speak.is_set or self.ipv4_slaves_speak.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_slaves_speak.get_name_leafdata())
            if (self.ipv4_slaves_standby.is_set or self.ipv4_slaves_standby.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_slaves_standby.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_active_down.is_set or self.ipv4_virtual_ip_addresses_active_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_active_down.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_active_up.is_set or self.ipv4_virtual_ip_addresses_active_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_active_up.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_init_down.is_set or self.ipv4_virtual_ip_addresses_init_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_init_down.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_init_up.is_set or self.ipv4_virtual_ip_addresses_init_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_init_up.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_learn_down.is_set or self.ipv4_virtual_ip_addresses_learn_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_learn_down.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_learn_up.is_set or self.ipv4_virtual_ip_addresses_learn_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_learn_up.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_listen_down.is_set or self.ipv4_virtual_ip_addresses_listen_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_listen_down.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_listen_up.is_set or self.ipv4_virtual_ip_addresses_listen_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_listen_up.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_speak_down.is_set or self.ipv4_virtual_ip_addresses_speak_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_speak_down.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_speak_up.is_set or self.ipv4_virtual_ip_addresses_speak_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_speak_up.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_standby_down.is_set or self.ipv4_virtual_ip_addresses_standby_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_standby_down.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_standby_up.is_set or self.ipv4_virtual_ip_addresses_standby_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_standby_up.get_name_leafdata())
            if (self.ipv6_sessions_active.is_set or self.ipv6_sessions_active.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_sessions_active.get_name_leafdata())
            if (self.ipv6_sessions_init.is_set or self.ipv6_sessions_init.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_sessions_init.get_name_leafdata())
            if (self.ipv6_sessions_learn.is_set or self.ipv6_sessions_learn.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_sessions_learn.get_name_leafdata())
            if (self.ipv6_sessions_listen.is_set or self.ipv6_sessions_listen.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_sessions_listen.get_name_leafdata())
            if (self.ipv6_sessions_speak.is_set or self.ipv6_sessions_speak.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_sessions_speak.get_name_leafdata())
            if (self.ipv6_sessions_standby.is_set or self.ipv6_sessions_standby.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_sessions_standby.get_name_leafdata())
            if (self.ipv6_slaves_active.is_set or self.ipv6_slaves_active.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_slaves_active.get_name_leafdata())
            if (self.ipv6_slaves_init.is_set or self.ipv6_slaves_init.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_slaves_init.get_name_leafdata())
            if (self.ipv6_slaves_learn.is_set or self.ipv6_slaves_learn.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_slaves_learn.get_name_leafdata())
            if (self.ipv6_slaves_listen.is_set or self.ipv6_slaves_listen.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_slaves_listen.get_name_leafdata())
            if (self.ipv6_slaves_speak.is_set or self.ipv6_slaves_speak.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_slaves_speak.get_name_leafdata())
            if (self.ipv6_slaves_standby.is_set or self.ipv6_slaves_standby.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_slaves_standby.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_active_down.is_set or self.ipv6_virtual_ip_addresses_active_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_active_down.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_active_up.is_set or self.ipv6_virtual_ip_addresses_active_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_active_up.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_init_down.is_set or self.ipv6_virtual_ip_addresses_init_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_init_down.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_init_up.is_set or self.ipv6_virtual_ip_addresses_init_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_init_up.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_learn_down.is_set or self.ipv6_virtual_ip_addresses_learn_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_learn_down.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_learn_up.is_set or self.ipv6_virtual_ip_addresses_learn_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_learn_up.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_listen_down.is_set or self.ipv6_virtual_ip_addresses_listen_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_listen_down.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_listen_up.is_set or self.ipv6_virtual_ip_addresses_listen_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_listen_up.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_speak_down.is_set or self.ipv6_virtual_ip_addresses_speak_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_speak_down.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_speak_up.is_set or self.ipv6_virtual_ip_addresses_speak_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_speak_up.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_standby_down.is_set or self.ipv6_virtual_ip_addresses_standby_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_standby_down.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_standby_up.is_set or self.ipv6_virtual_ip_addresses_standby_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_standby_up.get_name_leafdata())
            if (self.tracked_interfaces_ipv4_state_down.is_set or self.tracked_interfaces_ipv4_state_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_interfaces_ipv4_state_down.get_name_leafdata())
            if (self.tracked_interfaces_ipv4_state_up.is_set or self.tracked_interfaces_ipv4_state_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_interfaces_ipv4_state_up.get_name_leafdata())
            if (self.tracked_interfaces_ipv6_state_down.is_set or self.tracked_interfaces_ipv6_state_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_interfaces_ipv6_state_down.get_name_leafdata())
            if (self.tracked_interfaces_ipv6_state_up.is_set or self.tracked_interfaces_ipv6_state_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_interfaces_ipv6_state_up.get_name_leafdata())
            if (self.tracked_objects_down.is_set or self.tracked_objects_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_objects_down.get_name_leafdata())
            if (self.tracked_objects_up.is_set or self.tracked_objects_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_objects_up.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bfd-session-inactive" or name == "bfd-sessions-down" or name == "bfd-sessions-up" or name == "interfaces-ipv4-state-down" or name == "interfaces-ipv4-state-up" or name == "interfaces-ipv6-state-down" or name == "interfaces-ipv6-state-up" or name == "ipv4-sessions-active" or name == "ipv4-sessions-init" or name == "ipv4-sessions-learn" or name == "ipv4-sessions-listen" or name == "ipv4-sessions-speak" or name == "ipv4-sessions-standby" or name == "ipv4-slaves-active" or name == "ipv4-slaves-init" or name == "ipv4-slaves-learn" or name == "ipv4-slaves-listen" or name == "ipv4-slaves-speak" or name == "ipv4-slaves-standby" or name == "ipv4-virtual-ip-addresses-active-down" or name == "ipv4-virtual-ip-addresses-active-up" or name == "ipv4-virtual-ip-addresses-init-down" or name == "ipv4-virtual-ip-addresses-init-up" or name == "ipv4-virtual-ip-addresses-learn-down" or name == "ipv4-virtual-ip-addresses-learn-up" or name == "ipv4-virtual-ip-addresses-listen-down" or name == "ipv4-virtual-ip-addresses-listen-up" or name == "ipv4-virtual-ip-addresses-speak-down" or name == "ipv4-virtual-ip-addresses-speak-up" or name == "ipv4-virtual-ip-addresses-standby-down" or name == "ipv4-virtual-ip-addresses-standby-up" or name == "ipv6-sessions-active" or name == "ipv6-sessions-init" or name == "ipv6-sessions-learn" or name == "ipv6-sessions-listen" or name == "ipv6-sessions-speak" or name == "ipv6-sessions-standby" or name == "ipv6-slaves-active" or name == "ipv6-slaves-init" or name == "ipv6-slaves-learn" or name == "ipv6-slaves-listen" or name == "ipv6-slaves-speak" or name == "ipv6-slaves-standby" or name == "ipv6-virtual-ip-addresses-active-down" or name == "ipv6-virtual-ip-addresses-active-up" or name == "ipv6-virtual-ip-addresses-init-down" or name == "ipv6-virtual-ip-addresses-init-up" or name == "ipv6-virtual-ip-addresses-learn-down" or name == "ipv6-virtual-ip-addresses-learn-up" or name == "ipv6-virtual-ip-addresses-listen-down" or name == "ipv6-virtual-ip-addresses-listen-up" or name == "ipv6-virtual-ip-addresses-speak-down" or name == "ipv6-virtual-ip-addresses-speak-up" or name == "ipv6-virtual-ip-addresses-standby-down" or name == "ipv6-virtual-ip-addresses-standby-up" or name == "tracked-interfaces-ipv4-state-down" or name == "tracked-interfaces-ipv4-state-up" or name == "tracked-interfaces-ipv6-state-down" or name == "tracked-interfaces-ipv6-state-up" or name == "tracked-objects-down" or name == "tracked-objects-up"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "bfd-session-inactive"):
                self.bfd_session_inactive = value
                self.bfd_session_inactive.value_namespace = name_space
                self.bfd_session_inactive.value_namespace_prefix = name_space_prefix
            if(value_path == "bfd-sessions-down"):
                self.bfd_sessions_down = value
                self.bfd_sessions_down.value_namespace = name_space
                self.bfd_sessions_down.value_namespace_prefix = name_space_prefix
            if(value_path == "bfd-sessions-up"):
                self.bfd_sessions_up = value
                self.bfd_sessions_up.value_namespace = name_space
                self.bfd_sessions_up.value_namespace_prefix = name_space_prefix
            if(value_path == "interfaces-ipv4-state-down"):
                self.interfaces_ipv4_state_down = value
                self.interfaces_ipv4_state_down.value_namespace = name_space
                self.interfaces_ipv4_state_down.value_namespace_prefix = name_space_prefix
            if(value_path == "interfaces-ipv4-state-up"):
                self.interfaces_ipv4_state_up = value
                self.interfaces_ipv4_state_up.value_namespace = name_space
                self.interfaces_ipv4_state_up.value_namespace_prefix = name_space_prefix
            if(value_path == "interfaces-ipv6-state-down"):
                self.interfaces_ipv6_state_down = value
                self.interfaces_ipv6_state_down.value_namespace = name_space
                self.interfaces_ipv6_state_down.value_namespace_prefix = name_space_prefix
            if(value_path == "interfaces-ipv6-state-up"):
                self.interfaces_ipv6_state_up = value
                self.interfaces_ipv6_state_up.value_namespace = name_space
                self.interfaces_ipv6_state_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-sessions-active"):
                self.ipv4_sessions_active = value
                self.ipv4_sessions_active.value_namespace = name_space
                self.ipv4_sessions_active.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-sessions-init"):
                self.ipv4_sessions_init = value
                self.ipv4_sessions_init.value_namespace = name_space
                self.ipv4_sessions_init.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-sessions-learn"):
                self.ipv4_sessions_learn = value
                self.ipv4_sessions_learn.value_namespace = name_space
                self.ipv4_sessions_learn.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-sessions-listen"):
                self.ipv4_sessions_listen = value
                self.ipv4_sessions_listen.value_namespace = name_space
                self.ipv4_sessions_listen.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-sessions-speak"):
                self.ipv4_sessions_speak = value
                self.ipv4_sessions_speak.value_namespace = name_space
                self.ipv4_sessions_speak.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-sessions-standby"):
                self.ipv4_sessions_standby = value
                self.ipv4_sessions_standby.value_namespace = name_space
                self.ipv4_sessions_standby.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-slaves-active"):
                self.ipv4_slaves_active = value
                self.ipv4_slaves_active.value_namespace = name_space
                self.ipv4_slaves_active.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-slaves-init"):
                self.ipv4_slaves_init = value
                self.ipv4_slaves_init.value_namespace = name_space
                self.ipv4_slaves_init.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-slaves-learn"):
                self.ipv4_slaves_learn = value
                self.ipv4_slaves_learn.value_namespace = name_space
                self.ipv4_slaves_learn.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-slaves-listen"):
                self.ipv4_slaves_listen = value
                self.ipv4_slaves_listen.value_namespace = name_space
                self.ipv4_slaves_listen.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-slaves-speak"):
                self.ipv4_slaves_speak = value
                self.ipv4_slaves_speak.value_namespace = name_space
                self.ipv4_slaves_speak.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-slaves-standby"):
                self.ipv4_slaves_standby = value
                self.ipv4_slaves_standby.value_namespace = name_space
                self.ipv4_slaves_standby.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-active-down"):
                self.ipv4_virtual_ip_addresses_active_down = value
                self.ipv4_virtual_ip_addresses_active_down.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_active_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-active-up"):
                self.ipv4_virtual_ip_addresses_active_up = value
                self.ipv4_virtual_ip_addresses_active_up.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_active_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-init-down"):
                self.ipv4_virtual_ip_addresses_init_down = value
                self.ipv4_virtual_ip_addresses_init_down.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_init_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-init-up"):
                self.ipv4_virtual_ip_addresses_init_up = value
                self.ipv4_virtual_ip_addresses_init_up.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_init_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-learn-down"):
                self.ipv4_virtual_ip_addresses_learn_down = value
                self.ipv4_virtual_ip_addresses_learn_down.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_learn_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-learn-up"):
                self.ipv4_virtual_ip_addresses_learn_up = value
                self.ipv4_virtual_ip_addresses_learn_up.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_learn_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-listen-down"):
                self.ipv4_virtual_ip_addresses_listen_down = value
                self.ipv4_virtual_ip_addresses_listen_down.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_listen_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-listen-up"):
                self.ipv4_virtual_ip_addresses_listen_up = value
                self.ipv4_virtual_ip_addresses_listen_up.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_listen_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-speak-down"):
                self.ipv4_virtual_ip_addresses_speak_down = value
                self.ipv4_virtual_ip_addresses_speak_down.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_speak_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-speak-up"):
                self.ipv4_virtual_ip_addresses_speak_up = value
                self.ipv4_virtual_ip_addresses_speak_up.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_speak_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-standby-down"):
                self.ipv4_virtual_ip_addresses_standby_down = value
                self.ipv4_virtual_ip_addresses_standby_down.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_standby_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-standby-up"):
                self.ipv4_virtual_ip_addresses_standby_up = value
                self.ipv4_virtual_ip_addresses_standby_up.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_standby_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-sessions-active"):
                self.ipv6_sessions_active = value
                self.ipv6_sessions_active.value_namespace = name_space
                self.ipv6_sessions_active.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-sessions-init"):
                self.ipv6_sessions_init = value
                self.ipv6_sessions_init.value_namespace = name_space
                self.ipv6_sessions_init.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-sessions-learn"):
                self.ipv6_sessions_learn = value
                self.ipv6_sessions_learn.value_namespace = name_space
                self.ipv6_sessions_learn.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-sessions-listen"):
                self.ipv6_sessions_listen = value
                self.ipv6_sessions_listen.value_namespace = name_space
                self.ipv6_sessions_listen.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-sessions-speak"):
                self.ipv6_sessions_speak = value
                self.ipv6_sessions_speak.value_namespace = name_space
                self.ipv6_sessions_speak.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-sessions-standby"):
                self.ipv6_sessions_standby = value
                self.ipv6_sessions_standby.value_namespace = name_space
                self.ipv6_sessions_standby.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-slaves-active"):
                self.ipv6_slaves_active = value
                self.ipv6_slaves_active.value_namespace = name_space
                self.ipv6_slaves_active.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-slaves-init"):
                self.ipv6_slaves_init = value
                self.ipv6_slaves_init.value_namespace = name_space
                self.ipv6_slaves_init.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-slaves-learn"):
                self.ipv6_slaves_learn = value
                self.ipv6_slaves_learn.value_namespace = name_space
                self.ipv6_slaves_learn.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-slaves-listen"):
                self.ipv6_slaves_listen = value
                self.ipv6_slaves_listen.value_namespace = name_space
                self.ipv6_slaves_listen.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-slaves-speak"):
                self.ipv6_slaves_speak = value
                self.ipv6_slaves_speak.value_namespace = name_space
                self.ipv6_slaves_speak.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-slaves-standby"):
                self.ipv6_slaves_standby = value
                self.ipv6_slaves_standby.value_namespace = name_space
                self.ipv6_slaves_standby.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-active-down"):
                self.ipv6_virtual_ip_addresses_active_down = value
                self.ipv6_virtual_ip_addresses_active_down.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_active_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-active-up"):
                self.ipv6_virtual_ip_addresses_active_up = value
                self.ipv6_virtual_ip_addresses_active_up.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_active_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-init-down"):
                self.ipv6_virtual_ip_addresses_init_down = value
                self.ipv6_virtual_ip_addresses_init_down.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_init_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-init-up"):
                self.ipv6_virtual_ip_addresses_init_up = value
                self.ipv6_virtual_ip_addresses_init_up.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_init_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-learn-down"):
                self.ipv6_virtual_ip_addresses_learn_down = value
                self.ipv6_virtual_ip_addresses_learn_down.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_learn_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-learn-up"):
                self.ipv6_virtual_ip_addresses_learn_up = value
                self.ipv6_virtual_ip_addresses_learn_up.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_learn_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-listen-down"):
                self.ipv6_virtual_ip_addresses_listen_down = value
                self.ipv6_virtual_ip_addresses_listen_down.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_listen_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-listen-up"):
                self.ipv6_virtual_ip_addresses_listen_up = value
                self.ipv6_virtual_ip_addresses_listen_up.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_listen_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-speak-down"):
                self.ipv6_virtual_ip_addresses_speak_down = value
                self.ipv6_virtual_ip_addresses_speak_down.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_speak_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-speak-up"):
                self.ipv6_virtual_ip_addresses_speak_up = value
                self.ipv6_virtual_ip_addresses_speak_up.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_speak_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-standby-down"):
                self.ipv6_virtual_ip_addresses_standby_down = value
                self.ipv6_virtual_ip_addresses_standby_down.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_standby_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-standby-up"):
                self.ipv6_virtual_ip_addresses_standby_up = value
                self.ipv6_virtual_ip_addresses_standby_up.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_standby_up.value_namespace_prefix = name_space_prefix
            if(value_path == "tracked-interfaces-ipv4-state-down"):
                self.tracked_interfaces_ipv4_state_down = value
                self.tracked_interfaces_ipv4_state_down.value_namespace = name_space
                self.tracked_interfaces_ipv4_state_down.value_namespace_prefix = name_space_prefix
            if(value_path == "tracked-interfaces-ipv4-state-up"):
                self.tracked_interfaces_ipv4_state_up = value
                self.tracked_interfaces_ipv4_state_up.value_namespace = name_space
                self.tracked_interfaces_ipv4_state_up.value_namespace_prefix = name_space_prefix
            if(value_path == "tracked-interfaces-ipv6-state-down"):
                self.tracked_interfaces_ipv6_state_down = value
                self.tracked_interfaces_ipv6_state_down.value_namespace = name_space
                self.tracked_interfaces_ipv6_state_down.value_namespace_prefix = name_space_prefix
            if(value_path == "tracked-interfaces-ipv6-state-up"):
                self.tracked_interfaces_ipv6_state_up = value
                self.tracked_interfaces_ipv6_state_up.value_namespace = name_space
                self.tracked_interfaces_ipv6_state_up.value_namespace_prefix = name_space_prefix
            if(value_path == "tracked-objects-down"):
                self.tracked_objects_down = value
                self.tracked_objects_down.value_namespace = name_space
                self.tracked_objects_down.value_namespace_prefix = name_space_prefix
            if(value_path == "tracked-objects-up"):
                self.tracked_objects_up = value
                self.tracked_objects_up.value_namespace = name_space
                self.tracked_objects_up.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.bfd_sessions is not None and self.bfd_sessions.has_data()) or
            (self.ipv4 is not None and self.ipv4.has_data()) or
            (self.ipv6 is not None and self.ipv6.has_data()) or
            (self.mgo_sessions is not None and self.mgo_sessions.has_data()) or
            (self.summary is not None and self.summary.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.bfd_sessions is not None and self.bfd_sessions.has_operation()) or
            (self.ipv4 is not None and self.ipv4.has_operation()) or
            (self.ipv6 is not None and self.ipv6.has_operation()) or
            (self.mgo_sessions is not None and self.mgo_sessions.has_operation()) or
            (self.summary is not None and self.summary.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp" + path_buffer

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

        if (child_yang_name == "bfd-sessions"):
            if (self.bfd_sessions is None):
                self.bfd_sessions = Hsrp.BfdSessions()
                self.bfd_sessions.parent = self
                self._children_name_map["bfd_sessions"] = "bfd-sessions"
            return self.bfd_sessions

        if (child_yang_name == "ipv4"):
            if (self.ipv4 is None):
                self.ipv4 = Hsrp.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
            return self.ipv4

        if (child_yang_name == "ipv6"):
            if (self.ipv6 is None):
                self.ipv6 = Hsrp.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
            return self.ipv6

        if (child_yang_name == "mgo-sessions"):
            if (self.mgo_sessions is None):
                self.mgo_sessions = Hsrp.MgoSessions()
                self.mgo_sessions.parent = self
                self._children_name_map["mgo_sessions"] = "mgo-sessions"
            return self.mgo_sessions

        if (child_yang_name == "summary"):
            if (self.summary is None):
                self.summary = Hsrp.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
            return self.summary

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "bfd-sessions" or name == "ipv4" or name == "ipv6" or name == "mgo-sessions" or name == "summary"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Hsrp()
        return self._top_entity

