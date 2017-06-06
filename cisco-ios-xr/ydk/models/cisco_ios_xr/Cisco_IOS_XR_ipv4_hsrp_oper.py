""" Cisco_IOS_XR_ipv4_hsrp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-hsrp package operational data.

This module contains definitions
for the following management objects\:
  hsrp\: HSRP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class HsrpBAfEnum(Enum):
    """
    HsrpBAfEnum

    Hsrp b af

    .. data:: ipv4 = 0

    	IPv4 Address Family

    .. data:: ipv6 = 1

    	IPv6 Address Family

    .. data:: count = 2

    	The number of supported address families

    """

    ipv4 = 0

    ipv6 = 1

    count = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
        return meta._meta_table['HsrpBAfEnum']


class HsrpBfdSessionStateEnum(Enum):
    """
    HsrpBfdSessionStateEnum

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

    bfd_state_none = 0

    bfd_state_inactive = 1

    bfd_state_up = 2

    bfd_state_down = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
        return meta._meta_table['HsrpBfdSessionStateEnum']


class HsrpStateChangeReasonEnum(Enum):
    """
    HsrpStateChangeReasonEnum

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

    state_change_bfd_down = 0

    state_change_vip_learnt = 1

    state_change_interface_ip = 2

    state_change_delay_timer = 3

    state_change_startup = 4

    state_change_shutdown = 5

    state_change_interface_up = 6

    state_change_interface_down = 7

    state_change_active_timer = 8

    state_change_standby_timer = 9

    state_change_resign = 10

    state_change_coup = 11

    state_change_higher_priority_speak = 12

    state_change_higher_priority_standby = 13

    state_change_lower_priority_standby = 14

    state_change_higher_priority_active = 15

    state_change_lower_priority_active = 16

    state_change_virtual_ip_configured = 17

    state_change_virtual_ip_lost = 18

    state_change_recovered_from_checkpoint = 19

    state_change_mac_update = 20

    state_change_admin = 21

    state_change_parent = 22

    state_change_chkpt_update = 23

    state_change_issu_resync = 24

    state_change_max = 25


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
        return meta._meta_table['HsrpStateChangeReasonEnum']


class HsrpVmacStateEnum(Enum):
    """
    HsrpVmacStateEnum

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

    stored = 0

    reserved = 1

    active = 2

    reserving = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
        return meta._meta_table['HsrpVmacStateEnum']


class StandbyGrpStateEnum(Enum):
    """
    StandbyGrpStateEnum

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

    state_initial = 1

    state_learn = 2

    state_listen = 3

    state_speak = 4

    state_standby = 5

    state_active = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
        return meta._meta_table['StandbyGrpStateEnum']



class Hsrp(object):
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
        self.bfd_sessions = Hsrp.BfdSessions()
        self.bfd_sessions.parent = self
        self.ipv4 = Hsrp.Ipv4()
        self.ipv4.parent = self
        self.ipv6 = Hsrp.Ipv6()
        self.ipv6.parent = self
        self.mgo_sessions = Hsrp.MgoSessions()
        self.mgo_sessions.parent = self
        self.summary = Hsrp.Summary()
        self.summary.parent = self


    class Ipv4(object):
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
            self.parent = None
            self.groups = Hsrp.Ipv4.Groups()
            self.groups.parent = self
            self.interfaces = Hsrp.Ipv4.Interfaces()
            self.interfaces.parent = self
            self.tracked_interfaces = Hsrp.Ipv4.TrackedInterfaces()
            self.tracked_interfaces.parent = self


        class Groups(object):
            """
            The HSRP standby group table
            
            .. attribute:: group
            
            	An HSRP standby group
            	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.group = YList()
                self.group.parent = self
                self.group.name = 'group'


            class Group(object):
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
                	**type**\:   :py:class:`HsrpBAfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAfEnum>`
                
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
                	**type**\:   :py:class:`HsrpBfdSessionStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBfdSessionStateEnum>`
                
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
                	**type**\:   :py:class:`StandbyGrpStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpStateEnum>`
                
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
                	**type**\:   :py:class:`HsrpVmacStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpVmacStateEnum>`
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.group_number = None
                    self.active_ip_address = None
                    self.active_ipv6_address = None
                    self.active_mac_address = None
                    self.active_priority = None
                    self.active_timer_flag = None
                    self.active_timer_msecs = None
                    self.active_timer_secs = None
                    self.address_family = None
                    self.authentication_string = None
                    self.bfd_enabled = None
                    self.bfd_interface = None
                    self.bfd_interval = None
                    self.bfd_multiplier = None
                    self.bfd_peer_ip_address = None
                    self.bfd_peer_ipv6_address = None
                    self.bfd_session_state = None
                    self.configured_mac_address = None
                    self.configured_priority = None
                    self.configured_timers = None
                    self.coup_received_time = Hsrp.Ipv4.Groups.Group.CoupReceivedTime()
                    self.coup_received_time.parent = self
                    self.coup_sent_time = Hsrp.Ipv4.Groups.Group.CoupSentTime()
                    self.coup_sent_time.parent = self
                    self.current_state_timer_secs = None
                    self.delay_timer_flag = None
                    self.delay_timer_msecs = None
                    self.delay_timer_secs = None
                    self.followed_session_name = None
                    self.global_address = YList()
                    self.global_address.parent = self
                    self.global_address.name = 'global_address'
                    self.hello_time = None
                    self.hello_timer_flag = None
                    self.hello_timer_msecs = None
                    self.hello_timer_secs = None
                    self.hold_time = None
                    self.hsrp_group_number = None
                    self.hsrp_router_state = None
                    self.interface = None
                    self.interface_name_xr = None
                    self.is_slave = None
                    self.learned_hello_time = None
                    self.learned_hold_time = None
                    self.min_delay_time = None
                    self.preempt_delay = None
                    self.preempt_enabled = None
                    self.preempt_timer_secs = None
                    self.redirects_disabled = None
                    self.reload_delay_time = None
                    self.resign_received_time = Hsrp.Ipv4.Groups.Group.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self.resign_sent_time = Hsrp.Ipv4.Groups.Group.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self.router_priority = None
                    self.secondary_address = YLeafList()
                    self.secondary_address.parent = self
                    self.secondary_address.name = 'secondary_address'
                    self.session_name = None
                    self.slaves = None
                    self.standby_ip_address = None
                    self.standby_ipv6_address = None
                    self.standby_mac_address = None
                    self.standby_timer_flag = None
                    self.standby_timer_msecs = None
                    self.standby_timer_secs = None
                    self.state_change_count = None
                    self.state_change_history = YList()
                    self.state_change_history.parent = self
                    self.state_change_history.name = 'state_change_history'
                    self.statistics = Hsrp.Ipv4.Groups.Group.Statistics()
                    self.statistics.parent = self
                    self.tracked_interface_count = None
                    self.tracked_interface_up_count = None
                    self.use_bia_configured = None
                    self.use_configured_timers = None
                    self.use_configured_virtual_ip = None
                    self.version = None
                    self.virtual_ip_address = None
                    self.virtual_linklocal_ipv6_address = None
                    self.virtual_mac_address = None
                    self.virtual_mac_address_state = None


                class ResignSentTime(object):
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
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:resign-sent-time'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv4.Groups.Group.ResignSentTime']['meta_info']


                class ResignReceivedTime(object):
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
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:resign-received-time'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv4.Groups.Group.ResignReceivedTime']['meta_info']


                class CoupSentTime(object):
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
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:coup-sent-time'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv4.Groups.Group.CoupSentTime']['meta_info']


                class CoupReceivedTime(object):
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
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:coup-received-time'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv4.Groups.Group.CoupReceivedTime']['meta_info']


                class Statistics(object):
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
                        self.parent = None
                        self.active_transitions = None
                        self.auth_fail_received = None
                        self.coup_packets_received = None
                        self.coup_packets_sent = None
                        self.hello_packets_received = None
                        self.hello_packets_sent = None
                        self.init_transitions = None
                        self.invalid_timer_received = None
                        self.learn_transitions = None
                        self.listen_transitions = None
                        self.mismatch_virtual_ip_address_received = None
                        self.resign_packets_received = None
                        self.resign_packets_sent = None
                        self.speak_transitions = None
                        self.standby_transitions = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active_transitions is not None:
                            return True

                        if self.auth_fail_received is not None:
                            return True

                        if self.coup_packets_received is not None:
                            return True

                        if self.coup_packets_sent is not None:
                            return True

                        if self.hello_packets_received is not None:
                            return True

                        if self.hello_packets_sent is not None:
                            return True

                        if self.init_transitions is not None:
                            return True

                        if self.invalid_timer_received is not None:
                            return True

                        if self.learn_transitions is not None:
                            return True

                        if self.listen_transitions is not None:
                            return True

                        if self.mismatch_virtual_ip_address_received is not None:
                            return True

                        if self.resign_packets_received is not None:
                            return True

                        if self.resign_packets_sent is not None:
                            return True

                        if self.speak_transitions is not None:
                            return True

                        if self.standby_transitions is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv4.Groups.Group.Statistics']['meta_info']


                class GlobalAddress(object):
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
                        self.parent = None
                        self.ipv6_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:global-address'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv6_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv4.Groups.Group.GlobalAddress']['meta_info']


                class StateChangeHistory(object):
                    """
                    State change history
                    
                    .. attribute:: new_state
                    
                    	New State
                    	**type**\:   :py:class:`StandbyGrpStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpStateEnum>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:   :py:class:`StandbyGrpStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpStateEnum>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:   :py:class:`HsrpStateChangeReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpStateChangeReasonEnum>`
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:   :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.new_state = None
                        self.old_state = None
                        self.reason = None
                        self.time = Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time()
                        self.time.parent = self


                    class Time(object):
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
                            self.parent = None
                            self.nanoseconds = None
                            self.seconds = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:time'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.nanoseconds is not None:
                                return True

                            if self.seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                            return meta._meta_table['Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:state-change-history'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.new_state is not None:
                            return True

                        if self.old_state is not None:
                            return True

                        if self.reason is not None:
                            return True

                        if self.time is not None and self.time._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv4.Groups.Group.StateChangeHistory']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')
                    if self.group_number is None:
                        raise YPYModelError('Key property group_number is None')

                    return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv4/Cisco-IOS-XR-ipv4-hsrp-oper:groups/Cisco-IOS-XR-ipv4-hsrp-oper:group[Cisco-IOS-XR-ipv4-hsrp-oper:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv4-hsrp-oper:group-number = ' + str(self.group_number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.group_number is not None:
                        return True

                    if self.active_ip_address is not None:
                        return True

                    if self.active_ipv6_address is not None:
                        return True

                    if self.active_mac_address is not None:
                        return True

                    if self.active_priority is not None:
                        return True

                    if self.active_timer_flag is not None:
                        return True

                    if self.active_timer_msecs is not None:
                        return True

                    if self.active_timer_secs is not None:
                        return True

                    if self.address_family is not None:
                        return True

                    if self.authentication_string is not None:
                        return True

                    if self.bfd_enabled is not None:
                        return True

                    if self.bfd_interface is not None:
                        return True

                    if self.bfd_interval is not None:
                        return True

                    if self.bfd_multiplier is not None:
                        return True

                    if self.bfd_peer_ip_address is not None:
                        return True

                    if self.bfd_peer_ipv6_address is not None:
                        return True

                    if self.bfd_session_state is not None:
                        return True

                    if self.configured_mac_address is not None:
                        return True

                    if self.configured_priority is not None:
                        return True

                    if self.configured_timers is not None:
                        return True

                    if self.coup_received_time is not None and self.coup_received_time._has_data():
                        return True

                    if self.coup_sent_time is not None and self.coup_sent_time._has_data():
                        return True

                    if self.current_state_timer_secs is not None:
                        return True

                    if self.delay_timer_flag is not None:
                        return True

                    if self.delay_timer_msecs is not None:
                        return True

                    if self.delay_timer_secs is not None:
                        return True

                    if self.followed_session_name is not None:
                        return True

                    if self.global_address is not None:
                        for child_ref in self.global_address:
                            if child_ref._has_data():
                                return True

                    if self.hello_time is not None:
                        return True

                    if self.hello_timer_flag is not None:
                        return True

                    if self.hello_timer_msecs is not None:
                        return True

                    if self.hello_timer_secs is not None:
                        return True

                    if self.hold_time is not None:
                        return True

                    if self.hsrp_group_number is not None:
                        return True

                    if self.hsrp_router_state is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.interface_name_xr is not None:
                        return True

                    if self.is_slave is not None:
                        return True

                    if self.learned_hello_time is not None:
                        return True

                    if self.learned_hold_time is not None:
                        return True

                    if self.min_delay_time is not None:
                        return True

                    if self.preempt_delay is not None:
                        return True

                    if self.preempt_enabled is not None:
                        return True

                    if self.preempt_timer_secs is not None:
                        return True

                    if self.redirects_disabled is not None:
                        return True

                    if self.reload_delay_time is not None:
                        return True

                    if self.resign_received_time is not None and self.resign_received_time._has_data():
                        return True

                    if self.resign_sent_time is not None and self.resign_sent_time._has_data():
                        return True

                    if self.router_priority is not None:
                        return True

                    if self.secondary_address is not None:
                        for child in self.secondary_address:
                            if child is not None:
                                return True

                    if self.session_name is not None:
                        return True

                    if self.slaves is not None:
                        return True

                    if self.standby_ip_address is not None:
                        return True

                    if self.standby_ipv6_address is not None:
                        return True

                    if self.standby_mac_address is not None:
                        return True

                    if self.standby_timer_flag is not None:
                        return True

                    if self.standby_timer_msecs is not None:
                        return True

                    if self.standby_timer_secs is not None:
                        return True

                    if self.state_change_count is not None:
                        return True

                    if self.state_change_history is not None:
                        for child_ref in self.state_change_history:
                            if child_ref._has_data():
                                return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.tracked_interface_count is not None:
                        return True

                    if self.tracked_interface_up_count is not None:
                        return True

                    if self.use_bia_configured is not None:
                        return True

                    if self.use_configured_timers is not None:
                        return True

                    if self.use_configured_virtual_ip is not None:
                        return True

                    if self.version is not None:
                        return True

                    if self.virtual_ip_address is not None:
                        return True

                    if self.virtual_linklocal_ipv6_address is not None:
                        return True

                    if self.virtual_mac_address is not None:
                        return True

                    if self.virtual_mac_address_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                    return meta._meta_table['Hsrp.Ipv4.Groups.Group']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv4/Cisco-IOS-XR-ipv4-hsrp-oper:groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.group is not None:
                    for child_ref in self.group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                return meta._meta_table['Hsrp.Ipv4.Groups']['meta_info']


        class TrackedInterfaces(object):
            """
            The HSRP tracked interfaces table
            
            .. attribute:: tracked_interface
            
            	An HSRP tracked interface entry
            	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.TrackedInterfaces.TrackedInterface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.tracked_interface = YList()
                self.tracked_interface.parent = self
                self.tracked_interface.name = 'tracked_interface'


            class TrackedInterface(object):
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
                    self.parent = None
                    self.interface_name = None
                    self.group_number = None
                    self.tracked_interface_name = None
                    self.hsrp_group_number = None
                    self.interface = None
                    self.interface_up_flag = None
                    self.is_object = None
                    self.priority_decrement = None
                    self.tracked_interface_name_xr = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')
                    if self.group_number is None:
                        raise YPYModelError('Key property group_number is None')
                    if self.tracked_interface_name is None:
                        raise YPYModelError('Key property tracked_interface_name is None')

                    return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv4/Cisco-IOS-XR-ipv4-hsrp-oper:tracked-interfaces/Cisco-IOS-XR-ipv4-hsrp-oper:tracked-interface[Cisco-IOS-XR-ipv4-hsrp-oper:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv4-hsrp-oper:group-number = ' + str(self.group_number) + '][Cisco-IOS-XR-ipv4-hsrp-oper:tracked-interface-name = ' + str(self.tracked_interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.group_number is not None:
                        return True

                    if self.tracked_interface_name is not None:
                        return True

                    if self.hsrp_group_number is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.interface_up_flag is not None:
                        return True

                    if self.is_object is not None:
                        return True

                    if self.priority_decrement is not None:
                        return True

                    if self.tracked_interface_name_xr is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                    return meta._meta_table['Hsrp.Ipv4.TrackedInterfaces.TrackedInterface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv4/Cisco-IOS-XR-ipv4-hsrp-oper:tracked-interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.tracked_interface is not None:
                    for child_ref in self.tracked_interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                return meta._meta_table['Hsrp.Ipv4.TrackedInterfaces']['meta_info']


        class Interfaces(object):
            """
            The HSRP interface information table
            
            .. attribute:: interface
            
            	A HSRP interface entry
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
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
                    self.parent = None
                    self.interface_name = None
                    self.interface = None
                    self.statistics = Hsrp.Ipv4.Interfaces.Interface.Statistics()
                    self.statistics.parent = self
                    self.use_bia_flag = None


                class Statistics(object):
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
                        self.parent = None
                        self.advert_packets_received = None
                        self.advert_packets_sent = None
                        self.conflict_source_ip_address_received = None
                        self.inoperational_group_received = None
                        self.invalid_operation_code_received = None
                        self.invalid_version_received = None
                        self.long_packets_received = None
                        self.short_packets_received = None
                        self.unknown_group_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.advert_packets_received is not None:
                            return True

                        if self.advert_packets_sent is not None:
                            return True

                        if self.conflict_source_ip_address_received is not None:
                            return True

                        if self.inoperational_group_received is not None:
                            return True

                        if self.invalid_operation_code_received is not None:
                            return True

                        if self.invalid_version_received is not None:
                            return True

                        if self.long_packets_received is not None:
                            return True

                        if self.short_packets_received is not None:
                            return True

                        if self.unknown_group_received is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv4.Interfaces.Interface.Statistics']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv4/Cisco-IOS-XR-ipv4-hsrp-oper:interfaces/Cisco-IOS-XR-ipv4-hsrp-oper:interface[Cisco-IOS-XR-ipv4-hsrp-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.use_bia_flag is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                    return meta._meta_table['Hsrp.Ipv4.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv4/Cisco-IOS-XR-ipv4-hsrp-oper:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                return meta._meta_table['Hsrp.Ipv4.Interfaces']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv4'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.groups is not None and self.groups._has_data():
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.tracked_interfaces is not None and self.tracked_interfaces._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
            return meta._meta_table['Hsrp.Ipv4']['meta_info']


    class MgoSessions(object):
        """
        HSRP MGO session table
        
        .. attribute:: mgo_session
        
        	HSRP MGO session
        	**type**\: list of    :py:class:`MgoSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.MgoSessions.MgoSession>`
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.mgo_session = YList()
            self.mgo_session.parent = self
            self.mgo_session.name = 'mgo_session'


        class MgoSession(object):
            """
            HSRP MGO session
            
            .. attribute:: session_name  <key>
            
            	HSRP MGO session name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: primary_af_name
            
            	Address family of primary session
            	**type**\:   :py:class:`HsrpBAfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAfEnum>`
            
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
            	**type**\:   :py:class:`StandbyGrpStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpStateEnum>`
            
            .. attribute:: slave
            
            	List of slaves following this primary session
            	**type**\: list of    :py:class:`Slave <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.MgoSessions.MgoSession.Slave>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.session_name = None
                self.primary_af_name = None
                self.primary_session_interface = None
                self.primary_session_name = None
                self.primary_session_number = None
                self.primary_session_state = None
                self.slave = YList()
                self.slave.parent = self
                self.slave.name = 'slave'


            class Slave(object):
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
                    self.parent = None
                    self.slave_group_interface = None
                    self.slave_group_number = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:slave'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.slave_group_interface is not None:
                        return True

                    if self.slave_group_number is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                    return meta._meta_table['Hsrp.MgoSessions.MgoSession.Slave']['meta_info']

            @property
            def _common_path(self):
                if self.session_name is None:
                    raise YPYModelError('Key property session_name is None')

                return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:mgo-sessions/Cisco-IOS-XR-ipv4-hsrp-oper:mgo-session[Cisco-IOS-XR-ipv4-hsrp-oper:session-name = ' + str(self.session_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.session_name is not None:
                    return True

                if self.primary_af_name is not None:
                    return True

                if self.primary_session_interface is not None:
                    return True

                if self.primary_session_name is not None:
                    return True

                if self.primary_session_number is not None:
                    return True

                if self.primary_session_state is not None:
                    return True

                if self.slave is not None:
                    for child_ref in self.slave:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                return meta._meta_table['Hsrp.MgoSessions.MgoSession']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:mgo-sessions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.mgo_session is not None:
                for child_ref in self.mgo_session:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
            return meta._meta_table['Hsrp.MgoSessions']['meta_info']


    class Ipv6(object):
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
            self.parent = None
            self.groups = Hsrp.Ipv6.Groups()
            self.groups.parent = self
            self.interfaces = Hsrp.Ipv6.Interfaces()
            self.interfaces.parent = self
            self.tracked_interfaces = Hsrp.Ipv6.TrackedInterfaces()
            self.tracked_interfaces.parent = self


        class TrackedInterfaces(object):
            """
            The HSRP tracked interfaces table
            
            .. attribute:: tracked_interface
            
            	An HSRP tracked interface entry
            	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.TrackedInterfaces.TrackedInterface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.tracked_interface = YList()
                self.tracked_interface.parent = self
                self.tracked_interface.name = 'tracked_interface'


            class TrackedInterface(object):
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
                    self.parent = None
                    self.interface_name = None
                    self.group_number = None
                    self.tracked_interface_name = None
                    self.hsrp_group_number = None
                    self.interface = None
                    self.interface_up_flag = None
                    self.is_object = None
                    self.priority_decrement = None
                    self.tracked_interface_name_xr = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')
                    if self.group_number is None:
                        raise YPYModelError('Key property group_number is None')
                    if self.tracked_interface_name is None:
                        raise YPYModelError('Key property tracked_interface_name is None')

                    return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv6/Cisco-IOS-XR-ipv4-hsrp-oper:tracked-interfaces/Cisco-IOS-XR-ipv4-hsrp-oper:tracked-interface[Cisco-IOS-XR-ipv4-hsrp-oper:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv4-hsrp-oper:group-number = ' + str(self.group_number) + '][Cisco-IOS-XR-ipv4-hsrp-oper:tracked-interface-name = ' + str(self.tracked_interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.group_number is not None:
                        return True

                    if self.tracked_interface_name is not None:
                        return True

                    if self.hsrp_group_number is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.interface_up_flag is not None:
                        return True

                    if self.is_object is not None:
                        return True

                    if self.priority_decrement is not None:
                        return True

                    if self.tracked_interface_name_xr is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                    return meta._meta_table['Hsrp.Ipv6.TrackedInterfaces.TrackedInterface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv6/Cisco-IOS-XR-ipv4-hsrp-oper:tracked-interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.tracked_interface is not None:
                    for child_ref in self.tracked_interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                return meta._meta_table['Hsrp.Ipv6.TrackedInterfaces']['meta_info']


        class Groups(object):
            """
            The HSRP standby group table
            
            .. attribute:: group
            
            	An HSRP standby group
            	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.group = YList()
                self.group.parent = self
                self.group.name = 'group'


            class Group(object):
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
                	**type**\:   :py:class:`HsrpBAfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAfEnum>`
                
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
                	**type**\:   :py:class:`HsrpBfdSessionStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBfdSessionStateEnum>`
                
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
                	**type**\:   :py:class:`StandbyGrpStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpStateEnum>`
                
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
                	**type**\:   :py:class:`HsrpVmacStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpVmacStateEnum>`
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.group_number = None
                    self.active_ip_address = None
                    self.active_ipv6_address = None
                    self.active_mac_address = None
                    self.active_priority = None
                    self.active_timer_flag = None
                    self.active_timer_msecs = None
                    self.active_timer_secs = None
                    self.address_family = None
                    self.authentication_string = None
                    self.bfd_enabled = None
                    self.bfd_interface = None
                    self.bfd_interval = None
                    self.bfd_multiplier = None
                    self.bfd_peer_ip_address = None
                    self.bfd_peer_ipv6_address = None
                    self.bfd_session_state = None
                    self.configured_mac_address = None
                    self.configured_priority = None
                    self.configured_timers = None
                    self.coup_received_time = Hsrp.Ipv6.Groups.Group.CoupReceivedTime()
                    self.coup_received_time.parent = self
                    self.coup_sent_time = Hsrp.Ipv6.Groups.Group.CoupSentTime()
                    self.coup_sent_time.parent = self
                    self.current_state_timer_secs = None
                    self.delay_timer_flag = None
                    self.delay_timer_msecs = None
                    self.delay_timer_secs = None
                    self.followed_session_name = None
                    self.global_address = YList()
                    self.global_address.parent = self
                    self.global_address.name = 'global_address'
                    self.hello_time = None
                    self.hello_timer_flag = None
                    self.hello_timer_msecs = None
                    self.hello_timer_secs = None
                    self.hold_time = None
                    self.hsrp_group_number = None
                    self.hsrp_router_state = None
                    self.interface = None
                    self.interface_name_xr = None
                    self.is_slave = None
                    self.learned_hello_time = None
                    self.learned_hold_time = None
                    self.min_delay_time = None
                    self.preempt_delay = None
                    self.preempt_enabled = None
                    self.preempt_timer_secs = None
                    self.redirects_disabled = None
                    self.reload_delay_time = None
                    self.resign_received_time = Hsrp.Ipv6.Groups.Group.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self.resign_sent_time = Hsrp.Ipv6.Groups.Group.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self.router_priority = None
                    self.secondary_address = YLeafList()
                    self.secondary_address.parent = self
                    self.secondary_address.name = 'secondary_address'
                    self.session_name = None
                    self.slaves = None
                    self.standby_ip_address = None
                    self.standby_ipv6_address = None
                    self.standby_mac_address = None
                    self.standby_timer_flag = None
                    self.standby_timer_msecs = None
                    self.standby_timer_secs = None
                    self.state_change_count = None
                    self.state_change_history = YList()
                    self.state_change_history.parent = self
                    self.state_change_history.name = 'state_change_history'
                    self.statistics = Hsrp.Ipv6.Groups.Group.Statistics()
                    self.statistics.parent = self
                    self.tracked_interface_count = None
                    self.tracked_interface_up_count = None
                    self.use_bia_configured = None
                    self.use_configured_timers = None
                    self.use_configured_virtual_ip = None
                    self.version = None
                    self.virtual_ip_address = None
                    self.virtual_linklocal_ipv6_address = None
                    self.virtual_mac_address = None
                    self.virtual_mac_address_state = None


                class ResignSentTime(object):
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
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:resign-sent-time'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv6.Groups.Group.ResignSentTime']['meta_info']


                class ResignReceivedTime(object):
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
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:resign-received-time'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv6.Groups.Group.ResignReceivedTime']['meta_info']


                class CoupSentTime(object):
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
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:coup-sent-time'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv6.Groups.Group.CoupSentTime']['meta_info']


                class CoupReceivedTime(object):
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
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:coup-received-time'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv6.Groups.Group.CoupReceivedTime']['meta_info']


                class Statistics(object):
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
                        self.parent = None
                        self.active_transitions = None
                        self.auth_fail_received = None
                        self.coup_packets_received = None
                        self.coup_packets_sent = None
                        self.hello_packets_received = None
                        self.hello_packets_sent = None
                        self.init_transitions = None
                        self.invalid_timer_received = None
                        self.learn_transitions = None
                        self.listen_transitions = None
                        self.mismatch_virtual_ip_address_received = None
                        self.resign_packets_received = None
                        self.resign_packets_sent = None
                        self.speak_transitions = None
                        self.standby_transitions = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active_transitions is not None:
                            return True

                        if self.auth_fail_received is not None:
                            return True

                        if self.coup_packets_received is not None:
                            return True

                        if self.coup_packets_sent is not None:
                            return True

                        if self.hello_packets_received is not None:
                            return True

                        if self.hello_packets_sent is not None:
                            return True

                        if self.init_transitions is not None:
                            return True

                        if self.invalid_timer_received is not None:
                            return True

                        if self.learn_transitions is not None:
                            return True

                        if self.listen_transitions is not None:
                            return True

                        if self.mismatch_virtual_ip_address_received is not None:
                            return True

                        if self.resign_packets_received is not None:
                            return True

                        if self.resign_packets_sent is not None:
                            return True

                        if self.speak_transitions is not None:
                            return True

                        if self.standby_transitions is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv6.Groups.Group.Statistics']['meta_info']


                class GlobalAddress(object):
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
                        self.parent = None
                        self.ipv6_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:global-address'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv6_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv6.Groups.Group.GlobalAddress']['meta_info']


                class StateChangeHistory(object):
                    """
                    State change history
                    
                    .. attribute:: new_state
                    
                    	New State
                    	**type**\:   :py:class:`StandbyGrpStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpStateEnum>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:   :py:class:`StandbyGrpStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpStateEnum>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:   :py:class:`HsrpStateChangeReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpStateChangeReasonEnum>`
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:   :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.new_state = None
                        self.old_state = None
                        self.reason = None
                        self.time = Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time()
                        self.time.parent = self


                    class Time(object):
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
                            self.parent = None
                            self.nanoseconds = None
                            self.seconds = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:time'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.nanoseconds is not None:
                                return True

                            if self.seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                            return meta._meta_table['Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:state-change-history'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.new_state is not None:
                            return True

                        if self.old_state is not None:
                            return True

                        if self.reason is not None:
                            return True

                        if self.time is not None and self.time._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv6.Groups.Group.StateChangeHistory']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')
                    if self.group_number is None:
                        raise YPYModelError('Key property group_number is None')

                    return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv6/Cisco-IOS-XR-ipv4-hsrp-oper:groups/Cisco-IOS-XR-ipv4-hsrp-oper:group[Cisco-IOS-XR-ipv4-hsrp-oper:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv4-hsrp-oper:group-number = ' + str(self.group_number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.group_number is not None:
                        return True

                    if self.active_ip_address is not None:
                        return True

                    if self.active_ipv6_address is not None:
                        return True

                    if self.active_mac_address is not None:
                        return True

                    if self.active_priority is not None:
                        return True

                    if self.active_timer_flag is not None:
                        return True

                    if self.active_timer_msecs is not None:
                        return True

                    if self.active_timer_secs is not None:
                        return True

                    if self.address_family is not None:
                        return True

                    if self.authentication_string is not None:
                        return True

                    if self.bfd_enabled is not None:
                        return True

                    if self.bfd_interface is not None:
                        return True

                    if self.bfd_interval is not None:
                        return True

                    if self.bfd_multiplier is not None:
                        return True

                    if self.bfd_peer_ip_address is not None:
                        return True

                    if self.bfd_peer_ipv6_address is not None:
                        return True

                    if self.bfd_session_state is not None:
                        return True

                    if self.configured_mac_address is not None:
                        return True

                    if self.configured_priority is not None:
                        return True

                    if self.configured_timers is not None:
                        return True

                    if self.coup_received_time is not None and self.coup_received_time._has_data():
                        return True

                    if self.coup_sent_time is not None and self.coup_sent_time._has_data():
                        return True

                    if self.current_state_timer_secs is not None:
                        return True

                    if self.delay_timer_flag is not None:
                        return True

                    if self.delay_timer_msecs is not None:
                        return True

                    if self.delay_timer_secs is not None:
                        return True

                    if self.followed_session_name is not None:
                        return True

                    if self.global_address is not None:
                        for child_ref in self.global_address:
                            if child_ref._has_data():
                                return True

                    if self.hello_time is not None:
                        return True

                    if self.hello_timer_flag is not None:
                        return True

                    if self.hello_timer_msecs is not None:
                        return True

                    if self.hello_timer_secs is not None:
                        return True

                    if self.hold_time is not None:
                        return True

                    if self.hsrp_group_number is not None:
                        return True

                    if self.hsrp_router_state is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.interface_name_xr is not None:
                        return True

                    if self.is_slave is not None:
                        return True

                    if self.learned_hello_time is not None:
                        return True

                    if self.learned_hold_time is not None:
                        return True

                    if self.min_delay_time is not None:
                        return True

                    if self.preempt_delay is not None:
                        return True

                    if self.preempt_enabled is not None:
                        return True

                    if self.preempt_timer_secs is not None:
                        return True

                    if self.redirects_disabled is not None:
                        return True

                    if self.reload_delay_time is not None:
                        return True

                    if self.resign_received_time is not None and self.resign_received_time._has_data():
                        return True

                    if self.resign_sent_time is not None and self.resign_sent_time._has_data():
                        return True

                    if self.router_priority is not None:
                        return True

                    if self.secondary_address is not None:
                        for child in self.secondary_address:
                            if child is not None:
                                return True

                    if self.session_name is not None:
                        return True

                    if self.slaves is not None:
                        return True

                    if self.standby_ip_address is not None:
                        return True

                    if self.standby_ipv6_address is not None:
                        return True

                    if self.standby_mac_address is not None:
                        return True

                    if self.standby_timer_flag is not None:
                        return True

                    if self.standby_timer_msecs is not None:
                        return True

                    if self.standby_timer_secs is not None:
                        return True

                    if self.state_change_count is not None:
                        return True

                    if self.state_change_history is not None:
                        for child_ref in self.state_change_history:
                            if child_ref._has_data():
                                return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.tracked_interface_count is not None:
                        return True

                    if self.tracked_interface_up_count is not None:
                        return True

                    if self.use_bia_configured is not None:
                        return True

                    if self.use_configured_timers is not None:
                        return True

                    if self.use_configured_virtual_ip is not None:
                        return True

                    if self.version is not None:
                        return True

                    if self.virtual_ip_address is not None:
                        return True

                    if self.virtual_linklocal_ipv6_address is not None:
                        return True

                    if self.virtual_mac_address is not None:
                        return True

                    if self.virtual_mac_address_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                    return meta._meta_table['Hsrp.Ipv6.Groups.Group']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv6/Cisco-IOS-XR-ipv4-hsrp-oper:groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.group is not None:
                    for child_ref in self.group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                return meta._meta_table['Hsrp.Ipv6.Groups']['meta_info']


        class Interfaces(object):
            """
            The HSRP interface information table
            
            .. attribute:: interface
            
            	A HSRP interface entry
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
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
                    self.parent = None
                    self.interface_name = None
                    self.interface = None
                    self.statistics = Hsrp.Ipv6.Interfaces.Interface.Statistics()
                    self.statistics.parent = self
                    self.use_bia_flag = None


                class Statistics(object):
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
                        self.parent = None
                        self.advert_packets_received = None
                        self.advert_packets_sent = None
                        self.conflict_source_ip_address_received = None
                        self.inoperational_group_received = None
                        self.invalid_operation_code_received = None
                        self.invalid_version_received = None
                        self.long_packets_received = None
                        self.short_packets_received = None
                        self.unknown_group_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.advert_packets_received is not None:
                            return True

                        if self.advert_packets_sent is not None:
                            return True

                        if self.conflict_source_ip_address_received is not None:
                            return True

                        if self.inoperational_group_received is not None:
                            return True

                        if self.invalid_operation_code_received is not None:
                            return True

                        if self.invalid_version_received is not None:
                            return True

                        if self.long_packets_received is not None:
                            return True

                        if self.short_packets_received is not None:
                            return True

                        if self.unknown_group_received is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                        return meta._meta_table['Hsrp.Ipv6.Interfaces.Interface.Statistics']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv6/Cisco-IOS-XR-ipv4-hsrp-oper:interfaces/Cisco-IOS-XR-ipv4-hsrp-oper:interface[Cisco-IOS-XR-ipv4-hsrp-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.use_bia_flag is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                    return meta._meta_table['Hsrp.Ipv6.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv6/Cisco-IOS-XR-ipv4-hsrp-oper:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                return meta._meta_table['Hsrp.Ipv6.Interfaces']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:ipv6'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.groups is not None and self.groups._has_data():
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.tracked_interfaces is not None and self.tracked_interfaces._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
            return meta._meta_table['Hsrp.Ipv6']['meta_info']


    class BfdSessions(object):
        """
        The table of HSRP BFD Sessions
        
        .. attribute:: bfd_session
        
        	An HSRP BFD Session
        	**type**\: list of    :py:class:`BfdSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.BfdSessions.BfdSession>`
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.bfd_session = YList()
            self.bfd_session.parent = self
            self.bfd_session.name = 'bfd_session'


        class BfdSession(object):
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
            	**type**\:   :py:class:`HsrpBfdSessionStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBfdSessionStateEnum>`
            
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
            	**type**\:   :py:class:`HsrpBAfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAfEnum>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.ip_address = None
                self.bfd_interface_name = None
                self.bfd_interval = None
                self.bfd_multiplier = None
                self.bfd_session_state = None
                self.destination_address = None
                self.destination_ipv6_address = None
                self.group = YList()
                self.group.parent = self
                self.group.name = 'group'
                self.session_address_family = None


            class Group(object):
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
                    self.parent = None
                    self.hsrp_group_number = None
                    self.interface_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-hsrp-oper:group'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.hsrp_group_number is not None:
                        return True

                    if self.interface_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                    return meta._meta_table['Hsrp.BfdSessions.BfdSession.Group']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')
                if self.ip_address is None:
                    raise YPYModelError('Key property ip_address is None')

                return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:bfd-sessions/Cisco-IOS-XR-ipv4-hsrp-oper:bfd-session[Cisco-IOS-XR-ipv4-hsrp-oper:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv4-hsrp-oper:ip-address = ' + str(self.ip_address) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.ip_address is not None:
                    return True

                if self.bfd_interface_name is not None:
                    return True

                if self.bfd_interval is not None:
                    return True

                if self.bfd_multiplier is not None:
                    return True

                if self.bfd_session_state is not None:
                    return True

                if self.destination_address is not None:
                    return True

                if self.destination_ipv6_address is not None:
                    return True

                if self.group is not None:
                    for child_ref in self.group:
                        if child_ref._has_data():
                            return True

                if self.session_address_family is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
                return meta._meta_table['Hsrp.BfdSessions.BfdSession']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:bfd-sessions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bfd_session is not None:
                for child_ref in self.bfd_session:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
            return meta._meta_table['Hsrp.BfdSessions']['meta_info']


    class Summary(object):
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
            self.parent = None
            self.bfd_session_inactive = None
            self.bfd_sessions_down = None
            self.bfd_sessions_up = None
            self.interfaces_ipv4_state_down = None
            self.interfaces_ipv4_state_up = None
            self.interfaces_ipv6_state_down = None
            self.interfaces_ipv6_state_up = None
            self.ipv4_sessions_active = None
            self.ipv4_sessions_init = None
            self.ipv4_sessions_learn = None
            self.ipv4_sessions_listen = None
            self.ipv4_sessions_speak = None
            self.ipv4_sessions_standby = None
            self.ipv4_slaves_active = None
            self.ipv4_slaves_init = None
            self.ipv4_slaves_learn = None
            self.ipv4_slaves_listen = None
            self.ipv4_slaves_speak = None
            self.ipv4_slaves_standby = None
            self.ipv4_virtual_ip_addresses_active_down = None
            self.ipv4_virtual_ip_addresses_active_up = None
            self.ipv4_virtual_ip_addresses_init_down = None
            self.ipv4_virtual_ip_addresses_init_up = None
            self.ipv4_virtual_ip_addresses_learn_down = None
            self.ipv4_virtual_ip_addresses_learn_up = None
            self.ipv4_virtual_ip_addresses_listen_down = None
            self.ipv4_virtual_ip_addresses_listen_up = None
            self.ipv4_virtual_ip_addresses_speak_down = None
            self.ipv4_virtual_ip_addresses_speak_up = None
            self.ipv4_virtual_ip_addresses_standby_down = None
            self.ipv4_virtual_ip_addresses_standby_up = None
            self.ipv6_sessions_active = None
            self.ipv6_sessions_init = None
            self.ipv6_sessions_learn = None
            self.ipv6_sessions_listen = None
            self.ipv6_sessions_speak = None
            self.ipv6_sessions_standby = None
            self.ipv6_slaves_active = None
            self.ipv6_slaves_init = None
            self.ipv6_slaves_learn = None
            self.ipv6_slaves_listen = None
            self.ipv6_slaves_speak = None
            self.ipv6_slaves_standby = None
            self.ipv6_virtual_ip_addresses_active_down = None
            self.ipv6_virtual_ip_addresses_active_up = None
            self.ipv6_virtual_ip_addresses_init_down = None
            self.ipv6_virtual_ip_addresses_init_up = None
            self.ipv6_virtual_ip_addresses_learn_down = None
            self.ipv6_virtual_ip_addresses_learn_up = None
            self.ipv6_virtual_ip_addresses_listen_down = None
            self.ipv6_virtual_ip_addresses_listen_up = None
            self.ipv6_virtual_ip_addresses_speak_down = None
            self.ipv6_virtual_ip_addresses_speak_up = None
            self.ipv6_virtual_ip_addresses_standby_down = None
            self.ipv6_virtual_ip_addresses_standby_up = None
            self.tracked_interfaces_ipv4_state_down = None
            self.tracked_interfaces_ipv4_state_up = None
            self.tracked_interfaces_ipv6_state_down = None
            self.tracked_interfaces_ipv6_state_up = None
            self.tracked_objects_down = None
            self.tracked_objects_up = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/Cisco-IOS-XR-ipv4-hsrp-oper:summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bfd_session_inactive is not None:
                return True

            if self.bfd_sessions_down is not None:
                return True

            if self.bfd_sessions_up is not None:
                return True

            if self.interfaces_ipv4_state_down is not None:
                return True

            if self.interfaces_ipv4_state_up is not None:
                return True

            if self.interfaces_ipv6_state_down is not None:
                return True

            if self.interfaces_ipv6_state_up is not None:
                return True

            if self.ipv4_sessions_active is not None:
                return True

            if self.ipv4_sessions_init is not None:
                return True

            if self.ipv4_sessions_learn is not None:
                return True

            if self.ipv4_sessions_listen is not None:
                return True

            if self.ipv4_sessions_speak is not None:
                return True

            if self.ipv4_sessions_standby is not None:
                return True

            if self.ipv4_slaves_active is not None:
                return True

            if self.ipv4_slaves_init is not None:
                return True

            if self.ipv4_slaves_learn is not None:
                return True

            if self.ipv4_slaves_listen is not None:
                return True

            if self.ipv4_slaves_speak is not None:
                return True

            if self.ipv4_slaves_standby is not None:
                return True

            if self.ipv4_virtual_ip_addresses_active_down is not None:
                return True

            if self.ipv4_virtual_ip_addresses_active_up is not None:
                return True

            if self.ipv4_virtual_ip_addresses_init_down is not None:
                return True

            if self.ipv4_virtual_ip_addresses_init_up is not None:
                return True

            if self.ipv4_virtual_ip_addresses_learn_down is not None:
                return True

            if self.ipv4_virtual_ip_addresses_learn_up is not None:
                return True

            if self.ipv4_virtual_ip_addresses_listen_down is not None:
                return True

            if self.ipv4_virtual_ip_addresses_listen_up is not None:
                return True

            if self.ipv4_virtual_ip_addresses_speak_down is not None:
                return True

            if self.ipv4_virtual_ip_addresses_speak_up is not None:
                return True

            if self.ipv4_virtual_ip_addresses_standby_down is not None:
                return True

            if self.ipv4_virtual_ip_addresses_standby_up is not None:
                return True

            if self.ipv6_sessions_active is not None:
                return True

            if self.ipv6_sessions_init is not None:
                return True

            if self.ipv6_sessions_learn is not None:
                return True

            if self.ipv6_sessions_listen is not None:
                return True

            if self.ipv6_sessions_speak is not None:
                return True

            if self.ipv6_sessions_standby is not None:
                return True

            if self.ipv6_slaves_active is not None:
                return True

            if self.ipv6_slaves_init is not None:
                return True

            if self.ipv6_slaves_learn is not None:
                return True

            if self.ipv6_slaves_listen is not None:
                return True

            if self.ipv6_slaves_speak is not None:
                return True

            if self.ipv6_slaves_standby is not None:
                return True

            if self.ipv6_virtual_ip_addresses_active_down is not None:
                return True

            if self.ipv6_virtual_ip_addresses_active_up is not None:
                return True

            if self.ipv6_virtual_ip_addresses_init_down is not None:
                return True

            if self.ipv6_virtual_ip_addresses_init_up is not None:
                return True

            if self.ipv6_virtual_ip_addresses_learn_down is not None:
                return True

            if self.ipv6_virtual_ip_addresses_learn_up is not None:
                return True

            if self.ipv6_virtual_ip_addresses_listen_down is not None:
                return True

            if self.ipv6_virtual_ip_addresses_listen_up is not None:
                return True

            if self.ipv6_virtual_ip_addresses_speak_down is not None:
                return True

            if self.ipv6_virtual_ip_addresses_speak_up is not None:
                return True

            if self.ipv6_virtual_ip_addresses_standby_down is not None:
                return True

            if self.ipv6_virtual_ip_addresses_standby_up is not None:
                return True

            if self.tracked_interfaces_ipv4_state_down is not None:
                return True

            if self.tracked_interfaces_ipv4_state_up is not None:
                return True

            if self.tracked_interfaces_ipv6_state_down is not None:
                return True

            if self.tracked_interfaces_ipv6_state_up is not None:
                return True

            if self.tracked_objects_down is not None:
                return True

            if self.tracked_objects_up is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
            return meta._meta_table['Hsrp.Summary']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-hsrp-oper:hsrp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.bfd_sessions is not None and self.bfd_sessions._has_data():
            return True

        if self.ipv4 is not None and self.ipv4._has_data():
            return True

        if self.ipv6 is not None and self.ipv6._has_data():
            return True

        if self.mgo_sessions is not None and self.mgo_sessions._has_data():
            return True

        if self.summary is not None and self.summary._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_hsrp_oper as meta
        return meta._meta_table['Hsrp']['meta_info']


