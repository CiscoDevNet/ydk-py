""" Cisco_IOS_XR_ipv4_vrrp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-vrrp package operational data.

This module contains definitions
for the following management objects\:
  vrrp\: VRRP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class VrrpBAfEnum(Enum):
    """
    VrrpBAfEnum

    Vrrp b af

    .. data:: address_family_ipv4 = 0

    	IPv4 Address Family

    .. data:: address_family_ipv6 = 1

    	IPv6 Address Family

    .. data:: vrrp_baf_count = 2

    	Number of Adddress Families

    """

    address_family_ipv4 = 0

    address_family_ipv6 = 1

    vrrp_baf_count = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
        return meta._meta_table['VrrpBAfEnum']


class VrrpBagProtocolStateEnum(Enum):
    """
    VrrpBagProtocolStateEnum

    VRRP protocol state

    .. data:: state_initial = 1

    	Initial

    .. data:: state_backup = 2

    	Backup

    .. data:: state_master = 3

    	Master

    """

    state_initial = 1

    state_backup = 2

    state_master = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
        return meta._meta_table['VrrpBagProtocolStateEnum']


class VrrpBfdSessionStateEnum(Enum):
    """
    VrrpBfdSessionStateEnum

    Vrrp bfd session state

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
        return meta._meta_table['VrrpBfdSessionStateEnum']


class VrrpProtAuthEnum(Enum):
    """
    VrrpProtAuthEnum

    Vrrp prot auth

    .. data:: authentication_none = 0

    	Down

    .. data:: authentication_text = 1

    	Simple Text

    .. data:: authentication_ip = 2

    	IP header

    """

    authentication_none = 0

    authentication_text = 1

    authentication_ip = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
        return meta._meta_table['VrrpProtAuthEnum']


class VrrpStateChangeReasonEnum(Enum):
    """
    VrrpStateChangeReasonEnum

    Vrrp state change reason

    .. data:: state_change_bfd_down = 0

    	BFD session down

    .. data:: state_change_virtual_ip_configured = 1

    	Virtual IP configured

    .. data:: state_change_interface_ip = 2

    	Interface IP update

    .. data:: state_change_delay_timer = 3

    	Delay timer expired

    .. data:: state_change_startup = 4

    	Ready on startup

    .. data:: state_change_interface_up = 5

    	Interface Up update

    .. data:: state_change_interface_down = 6

    	Interface Down update

    .. data:: state_change_master_down_timer = 7

    	Master down timer expired

    .. data:: state_change_higher_priority_master = 8

    	Higher priority advert received

    .. data:: state_change_fhrp_admin = 9

    	FHRP Admin state change

    .. data:: state_change_mgo_parent = 10

    	Change of MGO parent session

    .. data:: state_change_chkpt_update = 11

    	Checkpoint update from Primary VRRP instance

    .. data:: state_change_issu_resync = 12

    	Resync following ISSU primary event

    """

    state_change_bfd_down = 0

    state_change_virtual_ip_configured = 1

    state_change_interface_ip = 2

    state_change_delay_timer = 3

    state_change_startup = 4

    state_change_interface_up = 5

    state_change_interface_down = 6

    state_change_master_down_timer = 7

    state_change_higher_priority_master = 8

    state_change_fhrp_admin = 9

    state_change_mgo_parent = 10

    state_change_chkpt_update = 11

    state_change_issu_resync = 12


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
        return meta._meta_table['VrrpStateChangeReasonEnum']


class VrrpVipStateEnum(Enum):
    """
    VrrpVipStateEnum

    Vrrp vip state

    .. data:: virtual_ip_state_down = 0

    	Down

    .. data:: virtual_ip_state_up = 1

    	Up

    """

    virtual_ip_state_down = 0

    virtual_ip_state_up = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
        return meta._meta_table['VrrpVipStateEnum']


class VrrpVmacStateEnum(Enum):
    """
    VrrpVmacStateEnum

    Vrrp vmac state

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
        return meta._meta_table['VrrpVmacStateEnum']



class Vrrp(object):
    """
    VRRP operational data
    
    .. attribute:: ipv4
    
    	IPv4 VRRP configuration
    	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4>`
    
    .. attribute:: ipv6
    
    	IPv6 VRRP configuration
    	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6>`
    
    .. attribute:: mgo_sessions
    
    	VRRP MGO Session information
    	**type**\:   :py:class:`MgoSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.MgoSessions>`
    
    .. attribute:: summary
    
    	VRRP summary statistics
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Summary>`
    
    

    """

    _prefix = 'ipv4-vrrp-oper'
    _revision = '2016-12-16'

    def __init__(self):
        self.ipv4 = Vrrp.Ipv4()
        self.ipv4.parent = self
        self.ipv6 = Vrrp.Ipv6()
        self.ipv6.parent = self
        self.mgo_sessions = Vrrp.MgoSessions()
        self.mgo_sessions.parent = self
        self.summary = Vrrp.Summary()
        self.summary.parent = self


    class Summary(object):
        """
        VRRP summary statistics
        
        .. attribute:: bfd_session_inactive
        
        	Number of VRRP IPv4 BFD sessions in INACTIVE state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: bfd_sessions_down
        
        	Number of VRRP IPv4 BFD sessions in DOWN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: bfd_sessions_up
        
        	Number of VRRP IPv4 BFD sessions in UP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv4_state_down
        
        	Number of VRRP interfaces with IPv4 caps in DOWN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv4_state_up
        
        	Number of VRRP interfaces with IPv4 caps in UP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv6_state_down
        
        	Number of VRRP interfaces with IPv6 caps in DOWN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv6_state_up
        
        	Number of VRRP interfaces with IPv6 caps in UP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_backup
        
        	Number of IPv4 sessions in BACKUP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_init
        
        	Number of IPv4 sessions in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_master
        
        	Number of IPv4 sessions in MASTER state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_master_owner
        
        	Number of IPv4 sessions in MASTER (owner) state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_backup
        
        	Number of IPv4 slaves in BACKUP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_init
        
        	Number of IPv4 slaves in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_master
        
        	Number of IPv4 slaves in MASTER state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_backup_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on virtual routers in BACKUP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_backup_up
        
        	Number of UP IPv4 Virtual IP Addresses on virtual routers in BACKUP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_init_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on virtual routers in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_init_up
        
        	Number of UP IPv4 Virtual IP Addresses on virtual routers in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_master_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on virtual routers in MASTER state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_master_owner_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on virtual routers in MASTER (owner) state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_master_owner_up
        
        	Number of UP IPv4 Virtual IP Addresses on virtual routers in MASTER (owner) state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_master_up
        
        	Number of UP IPv4 Virtual IP Addresses on virtual routers in MASTER state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_backup
        
        	Number of IPv6 sessions in BACKUP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_init
        
        	Number of IPv6 sessions in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_master
        
        	Number of IPv6 sessions in MASTER state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_master_owner
        
        	Number of IPv6 sessions in MASTER (owner) state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_backup
        
        	Number of IPv6 slaves in BACKUP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_init
        
        	Number of IPv6 slaves in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_master
        
        	Number of IPv6 slaves in MASTER state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_backup_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on virtual routers in BACKUP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_backup_up
        
        	Number of UP IPv6 Virtual IP Addresses on virtual routers in BACKUP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_init_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on virtual routers in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_init_up
        
        	Number of UP IPv6 Virtual IP Addresses on virtual routers in INIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_master_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on virtual routers in MASTER state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_master_owner_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on virtual routers in MASTER (owner) state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_master_owner_up
        
        	Number of UP IPv6 Virtual IP Addresses on virtual routers in MASTER (owner) state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_master_up
        
        	Number of UP IPv6 Virtual IP Addresses on virtual routers in MASTER state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6bfd_session_inactive
        
        	Number of VRRP IPv6 BFD sessions in INACTIVE state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6bfd_sessions_down
        
        	Number of VRRP IPv6 BFD sessions in DOWN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6bfd_sessions_up
        
        	Number of VRRP IPv6 BFD sessions in UP state
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
        
        .. attribute:: tracked_objects_state_down
        
        	Number of tracked objects in DOWN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_objects_state_up
        
        	Number of tracked objects in UP state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ipv4-vrrp-oper'
        _revision = '2016-12-16'

        def __init__(self):
            self.parent = None
            self.bfd_session_inactive = None
            self.bfd_sessions_down = None
            self.bfd_sessions_up = None
            self.interfaces_ipv4_state_down = None
            self.interfaces_ipv4_state_up = None
            self.interfaces_ipv6_state_down = None
            self.interfaces_ipv6_state_up = None
            self.ipv4_sessions_backup = None
            self.ipv4_sessions_init = None
            self.ipv4_sessions_master = None
            self.ipv4_sessions_master_owner = None
            self.ipv4_slaves_backup = None
            self.ipv4_slaves_init = None
            self.ipv4_slaves_master = None
            self.ipv4_virtual_ip_addresses_backup_down = None
            self.ipv4_virtual_ip_addresses_backup_up = None
            self.ipv4_virtual_ip_addresses_init_down = None
            self.ipv4_virtual_ip_addresses_init_up = None
            self.ipv4_virtual_ip_addresses_master_down = None
            self.ipv4_virtual_ip_addresses_master_owner_down = None
            self.ipv4_virtual_ip_addresses_master_owner_up = None
            self.ipv4_virtual_ip_addresses_master_up = None
            self.ipv6_sessions_backup = None
            self.ipv6_sessions_init = None
            self.ipv6_sessions_master = None
            self.ipv6_sessions_master_owner = None
            self.ipv6_slaves_backup = None
            self.ipv6_slaves_init = None
            self.ipv6_slaves_master = None
            self.ipv6_virtual_ip_addresses_backup_down = None
            self.ipv6_virtual_ip_addresses_backup_up = None
            self.ipv6_virtual_ip_addresses_init_down = None
            self.ipv6_virtual_ip_addresses_init_up = None
            self.ipv6_virtual_ip_addresses_master_down = None
            self.ipv6_virtual_ip_addresses_master_owner_down = None
            self.ipv6_virtual_ip_addresses_master_owner_up = None
            self.ipv6_virtual_ip_addresses_master_up = None
            self.ipv6bfd_session_inactive = None
            self.ipv6bfd_sessions_down = None
            self.ipv6bfd_sessions_up = None
            self.tracked_interfaces_ipv4_state_down = None
            self.tracked_interfaces_ipv4_state_up = None
            self.tracked_interfaces_ipv6_state_down = None
            self.tracked_interfaces_ipv6_state_up = None
            self.tracked_objects_state_down = None
            self.tracked_objects_state_up = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:summary'

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

            if self.ipv4_sessions_backup is not None:
                return True

            if self.ipv4_sessions_init is not None:
                return True

            if self.ipv4_sessions_master is not None:
                return True

            if self.ipv4_sessions_master_owner is not None:
                return True

            if self.ipv4_slaves_backup is not None:
                return True

            if self.ipv4_slaves_init is not None:
                return True

            if self.ipv4_slaves_master is not None:
                return True

            if self.ipv4_virtual_ip_addresses_backup_down is not None:
                return True

            if self.ipv4_virtual_ip_addresses_backup_up is not None:
                return True

            if self.ipv4_virtual_ip_addresses_init_down is not None:
                return True

            if self.ipv4_virtual_ip_addresses_init_up is not None:
                return True

            if self.ipv4_virtual_ip_addresses_master_down is not None:
                return True

            if self.ipv4_virtual_ip_addresses_master_owner_down is not None:
                return True

            if self.ipv4_virtual_ip_addresses_master_owner_up is not None:
                return True

            if self.ipv4_virtual_ip_addresses_master_up is not None:
                return True

            if self.ipv6_sessions_backup is not None:
                return True

            if self.ipv6_sessions_init is not None:
                return True

            if self.ipv6_sessions_master is not None:
                return True

            if self.ipv6_sessions_master_owner is not None:
                return True

            if self.ipv6_slaves_backup is not None:
                return True

            if self.ipv6_slaves_init is not None:
                return True

            if self.ipv6_slaves_master is not None:
                return True

            if self.ipv6_virtual_ip_addresses_backup_down is not None:
                return True

            if self.ipv6_virtual_ip_addresses_backup_up is not None:
                return True

            if self.ipv6_virtual_ip_addresses_init_down is not None:
                return True

            if self.ipv6_virtual_ip_addresses_init_up is not None:
                return True

            if self.ipv6_virtual_ip_addresses_master_down is not None:
                return True

            if self.ipv6_virtual_ip_addresses_master_owner_down is not None:
                return True

            if self.ipv6_virtual_ip_addresses_master_owner_up is not None:
                return True

            if self.ipv6_virtual_ip_addresses_master_up is not None:
                return True

            if self.ipv6bfd_session_inactive is not None:
                return True

            if self.ipv6bfd_sessions_down is not None:
                return True

            if self.ipv6bfd_sessions_up is not None:
                return True

            if self.tracked_interfaces_ipv4_state_down is not None:
                return True

            if self.tracked_interfaces_ipv4_state_up is not None:
                return True

            if self.tracked_interfaces_ipv6_state_down is not None:
                return True

            if self.tracked_interfaces_ipv6_state_up is not None:
                return True

            if self.tracked_objects_state_down is not None:
                return True

            if self.tracked_objects_state_up is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
            return meta._meta_table['Vrrp.Summary']['meta_info']


    class Ipv6(object):
        """
        IPv6 VRRP configuration
        
        .. attribute:: interfaces
        
        	The VRRP interface table
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.Interfaces>`
        
        .. attribute:: track_items
        
        	The VRRP tracked item table
        	**type**\:   :py:class:`TrackItems <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.TrackItems>`
        
        .. attribute:: virtual_routers
        
        	The VRRP virtual router table
        	**type**\:   :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters>`
        
        

        """

        _prefix = 'ipv4-vrrp-oper'
        _revision = '2016-12-16'

        def __init__(self):
            self.parent = None
            self.interfaces = Vrrp.Ipv6.Interfaces()
            self.interfaces.parent = self
            self.track_items = Vrrp.Ipv6.TrackItems()
            self.track_items.parent = self
            self.virtual_routers = Vrrp.Ipv6.VirtualRouters()
            self.virtual_routers.parent = self


        class TrackItems(object):
            """
            The VRRP tracked item table
            
            .. attribute:: track_item
            
            	A configured VRRP IP address entry
            	**type**\: list of    :py:class:`TrackItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.TrackItems.TrackItem>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                self.parent = None
                self.track_item = YList()
                self.track_item.parent = self
                self.track_item.name = 'track_item'


            class TrackItem(object):
                """
                A configured VRRP IP address entry
                
                .. attribute:: interface_name  <key>
                
                	The interface name to track
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: virtual_router_id  <key>
                
                	The VRRP virtual router id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tracked_interface_name  <key>
                
                	The name of the tracked interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: priority
                
                	Priority weight of item
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: state
                
                	State of the tracked item
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: tracked_item_index
                
                	Tracked item index
                	**type**\:  str
                
                	**length:** 0..32
                
                .. attribute:: tracked_item_type
                
                	Type of tracked item
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: virtual_router_id_xr
                
                	Virtual Router ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2016-12-16'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.virtual_router_id = None
                    self.tracked_interface_name = None
                    self.interface = None
                    self.priority = None
                    self.state = None
                    self.tracked_item_index = None
                    self.tracked_item_type = None
                    self.virtual_router_id_xr = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')
                    if self.virtual_router_id is None:
                        raise YPYModelError('Key property virtual_router_id is None')
                    if self.tracked_interface_name is None:
                        raise YPYModelError('Key property tracked_interface_name is None')

                    return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv6/Cisco-IOS-XR-ipv4-vrrp-oper:track-items/Cisco-IOS-XR-ipv4-vrrp-oper:track-item[Cisco-IOS-XR-ipv4-vrrp-oper:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv4-vrrp-oper:virtual-router-id = ' + str(self.virtual_router_id) + '][Cisco-IOS-XR-ipv4-vrrp-oper:tracked-interface-name = ' + str(self.tracked_interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.virtual_router_id is not None:
                        return True

                    if self.tracked_interface_name is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.priority is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.tracked_item_index is not None:
                        return True

                    if self.tracked_item_type is not None:
                        return True

                    if self.virtual_router_id_xr is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                    return meta._meta_table['Vrrp.Ipv6.TrackItems.TrackItem']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv6/Cisco-IOS-XR-ipv4-vrrp-oper:track-items'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.track_item is not None:
                    for child_ref in self.track_item:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                return meta._meta_table['Vrrp.Ipv6.TrackItems']['meta_info']


        class VirtualRouters(object):
            """
            The VRRP virtual router table
            
            .. attribute:: virtual_router
            
            	A VRRP virtual router
            	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                self.parent = None
                self.virtual_router = YList()
                self.virtual_router.parent = self
                self.virtual_router.name = 'virtual_router'


            class VirtualRouter(object):
                """
                A VRRP virtual router
                
                .. attribute:: interface_name  <key>
                
                	The name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: virtual_router_id  <key>
                
                	The VRRP virtual router id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:   :py:class:`VrrpBAfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBAfEnum>`
                
                .. attribute:: address_list_error_count
                
                	Address list errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: advert_interval_error_count
                
                	Advertise interval errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: adverts_received_count
                
                	No. of advertisements received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: adverts_sent_count
                
                	No. of advertisements sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: auth_type_mismatch_count
                
                	Authentication type mismatches
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_fail_count
                
                	Authentication failures
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_flag
                
                	Text authentication configured flag
                	**type**\:  bool
                
                .. attribute:: authentication_string
                
                	Authentication data
                	**type**\:  str
                
                .. attribute:: authentication_type
                
                	Authentication type
                	**type**\:   :py:class:`VrrpProtAuthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpProtAuthEnum>`
                
                .. attribute:: bfd_cfg_remote_ip
                
                	BFD configured remote IP
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_configured_remote_ipv6_address
                
                	BFD configured remote IPv6
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
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
                	**type**\:   :py:class:`VrrpBfdSessionStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBfdSessionStateEnum>`
                
                .. attribute:: configured_advertize_time
                
                	Configured advertize time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: configured_down_address_count
                
                	 Configured but Down VRRP address count
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: configured_priority
                
                	Configured priority
                	**type**\:  int
                
                	**range:** 0..255
                
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
                
                .. attribute:: force_timer_flag
                
                	Configured timers forced flag
                	**type**\:  bool
                
                .. attribute:: interface_ipv4_address
                
                	The Interface Primary IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: interface_ipv6_address
                
                	The Interface linklocal IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: interface_name_xr
                
                	IM Interface Name
                	**type**\:  str
                
                	**length:** 0..64
                
                .. attribute:: invalid_auth_type_count
                
                	Invalid authentication type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_packet_count
                
                	Invalid packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_address_owner_flag
                
                	IP address owner flag
                	**type**\:  bool
                
                .. attribute:: ipv4_configured_down_address
                
                	IPv4 Configured but Down VRRP addresses
                	**type**\:  list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_configured_down_address
                
                	IPv6 Configured but Down VRRP addresses
                	**type**\: list of    :py:class:`Ipv6ConfiguredDownAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress>`
                
                .. attribute:: ipv6_operational_address
                
                	IPv6 Operational VRRP addresses
                	**type**\: list of    :py:class:`Ipv6OperationalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress>`
                
                .. attribute:: is_accept_mode
                
                	Is accept mode
                	**type**\:  bool
                
                .. attribute:: is_slave
                
                	Group is a slave group
                	**type**\:  bool
                
                .. attribute:: master_count
                
                	No. of times become Master
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: master_ip_address
                
                	Master router real IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: master_ipv6_address
                
                	Master router real IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: master_priority
                
                	Master router priority
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: min_delay_time
                
                	Minimum delay time in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: oper_advertize_time
                
                	Operational advertize time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_address
                
                	Operational IPv4 VRRP addresses
                	**type**\:  list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: operational_address_count
                
                	Operational VRRP address count
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: operational_priority
                
                	Operational priority
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: pkt_length_errors_count
                
                	Packet length errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: preempt_delay_time
                
                	Preempt delay time
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: preempt_flag
                
                	Preempt configured flag
                	**type**\:  bool
                
                .. attribute:: primary_state
                
                	State of primary IP address
                	**type**\:   :py:class:`VrrpVipStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVipStateEnum>`
                
                .. attribute:: primary_virtual_ip
                
                	Configured IPv4 Primary address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: priority_decrement
                
                	Priority decrement
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority_zero_received_count
                
                	No. priority 0 received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority_zero_sent_count
                
                	No. priority 0 sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: reload_delay_time
                
                	Reload delay time in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: resign_received_time
                
                	Time last resign was received
                	**type**\:   :py:class:`ResignReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime>`
                
                .. attribute:: resign_sent_time
                
                	Time last resign was sent
                	**type**\:   :py:class:`ResignSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime>`
                
                .. attribute:: secondary_address_count
                
                	Configured VRRP secondary address count
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: session_name
                
                	Session Name
                	**type**\:  str
                
                	**length:** 0..16
                
                .. attribute:: slaves
                
                	Number of slaves following state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_change_count
                
                	Number of state changes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_change_history
                
                	State change history
                	**type**\: list of    :py:class:`StateChangeHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory>`
                
                .. attribute:: state_from_checkpoint
                
                	Whether state recovered from checkpoint
                	**type**\:  bool
                
                .. attribute:: time_in_current_state
                
                	Time in current state secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: time_stats_discontinuity
                
                	Time since a statistics discontinuity in ticks (10ns units)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: time_vrouter_up
                
                	Time vrouter is up in centiseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: centisecond
                
                .. attribute:: tracked_interface_count
                
                	Number of items tracked
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_up_count
                
                	Number of tracked items up
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_item_count
                
                	Number of tracked items
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_item_up_count
                
                	Number of tracked items in UP state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ttl_error_count
                
                	TTL errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: version
                
                	VRRP Protocol Version
                	**type**\:  int
                
                	**range:** 0..255
                
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
                	**type**\:   :py:class:`VrrpVmacStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVmacStateEnum>`
                
                .. attribute:: virtual_router_id_xr
                
                	Virtual Router ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrrp_state
                
                	VRRP state
                	**type**\:   :py:class:`VrrpBagProtocolStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolStateEnum>`
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2016-12-16'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.virtual_router_id = None
                    self.address_family = None
                    self.address_list_error_count = None
                    self.advert_interval_error_count = None
                    self.adverts_received_count = None
                    self.adverts_sent_count = None
                    self.auth_type_mismatch_count = None
                    self.authentication_fail_count = None
                    self.authentication_flag = None
                    self.authentication_string = None
                    self.authentication_type = None
                    self.bfd_cfg_remote_ip = None
                    self.bfd_configured_remote_ipv6_address = None
                    self.bfd_interval = None
                    self.bfd_multiplier = None
                    self.bfd_session_state = None
                    self.configured_advertize_time = None
                    self.configured_down_address_count = None
                    self.configured_priority = None
                    self.delay_timer_flag = None
                    self.delay_timer_msecs = None
                    self.delay_timer_secs = None
                    self.followed_session_name = None
                    self.force_timer_flag = None
                    self.interface_ipv4_address = None
                    self.interface_ipv6_address = None
                    self.interface_name_xr = None
                    self.invalid_auth_type_count = None
                    self.invalid_packet_count = None
                    self.ip_address_owner_flag = None
                    self.ipv4_configured_down_address = YLeafList()
                    self.ipv4_configured_down_address.parent = self
                    self.ipv4_configured_down_address.name = 'ipv4_configured_down_address'
                    self.ipv6_configured_down_address = YList()
                    self.ipv6_configured_down_address.parent = self
                    self.ipv6_configured_down_address.name = 'ipv6_configured_down_address'
                    self.ipv6_operational_address = YList()
                    self.ipv6_operational_address.parent = self
                    self.ipv6_operational_address.name = 'ipv6_operational_address'
                    self.is_accept_mode = None
                    self.is_slave = None
                    self.master_count = None
                    self.master_ip_address = None
                    self.master_ipv6_address = None
                    self.master_priority = None
                    self.min_delay_time = None
                    self.oper_advertize_time = None
                    self.operational_address = YLeafList()
                    self.operational_address.parent = self
                    self.operational_address.name = 'operational_address'
                    self.operational_address_count = None
                    self.operational_priority = None
                    self.pkt_length_errors_count = None
                    self.preempt_delay_time = None
                    self.preempt_flag = None
                    self.primary_state = None
                    self.primary_virtual_ip = None
                    self.priority_decrement = None
                    self.priority_zero_received_count = None
                    self.priority_zero_sent_count = None
                    self.reload_delay_time = None
                    self.resign_received_time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self.resign_sent_time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self.secondary_address_count = None
                    self.session_name = None
                    self.slaves = None
                    self.state_change_count = None
                    self.state_change_history = YList()
                    self.state_change_history.parent = self
                    self.state_change_history.name = 'state_change_history'
                    self.state_from_checkpoint = None
                    self.time_in_current_state = None
                    self.time_stats_discontinuity = None
                    self.time_vrouter_up = None
                    self.tracked_interface_count = None
                    self.tracked_interface_up_count = None
                    self.tracked_item_count = None
                    self.tracked_item_up_count = None
                    self.ttl_error_count = None
                    self.version = None
                    self.virtual_linklocal_ipv6_address = None
                    self.virtual_mac_address = None
                    self.virtual_mac_address_state = None
                    self.virtual_router_id_xr = None
                    self.vrrp_state = None


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

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:resign-sent-time'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                        return meta._meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime']['meta_info']


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

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:resign-received-time'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                        return meta._meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime']['meta_info']


                class Ipv6OperationalAddress(object):
                    """
                    IPv6 Operational VRRP addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:ipv6-operational-address'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv6_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                        return meta._meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress']['meta_info']


                class Ipv6ConfiguredDownAddress(object):
                    """
                    IPv6 Configured but Down VRRP addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:ipv6-configured-down-address'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv6_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                        return meta._meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress']['meta_info']


                class StateChangeHistory(object):
                    """
                    State change history
                    
                    .. attribute:: new_state
                    
                    	New State
                    	**type**\:   :py:class:`VrrpBagProtocolStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolStateEnum>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:   :py:class:`VrrpBagProtocolStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolStateEnum>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:   :py:class:`VrrpStateChangeReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpStateChangeReasonEnum>`
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:   :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.new_state = None
                        self.old_state = None
                        self.reason = None
                        self.time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time()
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

                        _prefix = 'ipv4-vrrp-oper'
                        _revision = '2016-12-16'

                        def __init__(self):
                            self.parent = None
                            self.nanoseconds = None
                            self.seconds = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:time'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                            return meta._meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:state-change-history'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                        return meta._meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')
                    if self.virtual_router_id is None:
                        raise YPYModelError('Key property virtual_router_id is None')

                    return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv6/Cisco-IOS-XR-ipv4-vrrp-oper:virtual-routers/Cisco-IOS-XR-ipv4-vrrp-oper:virtual-router[Cisco-IOS-XR-ipv4-vrrp-oper:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv4-vrrp-oper:virtual-router-id = ' + str(self.virtual_router_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.virtual_router_id is not None:
                        return True

                    if self.address_family is not None:
                        return True

                    if self.address_list_error_count is not None:
                        return True

                    if self.advert_interval_error_count is not None:
                        return True

                    if self.adverts_received_count is not None:
                        return True

                    if self.adverts_sent_count is not None:
                        return True

                    if self.auth_type_mismatch_count is not None:
                        return True

                    if self.authentication_fail_count is not None:
                        return True

                    if self.authentication_flag is not None:
                        return True

                    if self.authentication_string is not None:
                        return True

                    if self.authentication_type is not None:
                        return True

                    if self.bfd_cfg_remote_ip is not None:
                        return True

                    if self.bfd_configured_remote_ipv6_address is not None:
                        return True

                    if self.bfd_interval is not None:
                        return True

                    if self.bfd_multiplier is not None:
                        return True

                    if self.bfd_session_state is not None:
                        return True

                    if self.configured_advertize_time is not None:
                        return True

                    if self.configured_down_address_count is not None:
                        return True

                    if self.configured_priority is not None:
                        return True

                    if self.delay_timer_flag is not None:
                        return True

                    if self.delay_timer_msecs is not None:
                        return True

                    if self.delay_timer_secs is not None:
                        return True

                    if self.followed_session_name is not None:
                        return True

                    if self.force_timer_flag is not None:
                        return True

                    if self.interface_ipv4_address is not None:
                        return True

                    if self.interface_ipv6_address is not None:
                        return True

                    if self.interface_name_xr is not None:
                        return True

                    if self.invalid_auth_type_count is not None:
                        return True

                    if self.invalid_packet_count is not None:
                        return True

                    if self.ip_address_owner_flag is not None:
                        return True

                    if self.ipv4_configured_down_address is not None:
                        for child in self.ipv4_configured_down_address:
                            if child is not None:
                                return True

                    if self.ipv6_configured_down_address is not None:
                        for child_ref in self.ipv6_configured_down_address:
                            if child_ref._has_data():
                                return True

                    if self.ipv6_operational_address is not None:
                        for child_ref in self.ipv6_operational_address:
                            if child_ref._has_data():
                                return True

                    if self.is_accept_mode is not None:
                        return True

                    if self.is_slave is not None:
                        return True

                    if self.master_count is not None:
                        return True

                    if self.master_ip_address is not None:
                        return True

                    if self.master_ipv6_address is not None:
                        return True

                    if self.master_priority is not None:
                        return True

                    if self.min_delay_time is not None:
                        return True

                    if self.oper_advertize_time is not None:
                        return True

                    if self.operational_address is not None:
                        for child in self.operational_address:
                            if child is not None:
                                return True

                    if self.operational_address_count is not None:
                        return True

                    if self.operational_priority is not None:
                        return True

                    if self.pkt_length_errors_count is not None:
                        return True

                    if self.preempt_delay_time is not None:
                        return True

                    if self.preempt_flag is not None:
                        return True

                    if self.primary_state is not None:
                        return True

                    if self.primary_virtual_ip is not None:
                        return True

                    if self.priority_decrement is not None:
                        return True

                    if self.priority_zero_received_count is not None:
                        return True

                    if self.priority_zero_sent_count is not None:
                        return True

                    if self.reload_delay_time is not None:
                        return True

                    if self.resign_received_time is not None and self.resign_received_time._has_data():
                        return True

                    if self.resign_sent_time is not None and self.resign_sent_time._has_data():
                        return True

                    if self.secondary_address_count is not None:
                        return True

                    if self.session_name is not None:
                        return True

                    if self.slaves is not None:
                        return True

                    if self.state_change_count is not None:
                        return True

                    if self.state_change_history is not None:
                        for child_ref in self.state_change_history:
                            if child_ref._has_data():
                                return True

                    if self.state_from_checkpoint is not None:
                        return True

                    if self.time_in_current_state is not None:
                        return True

                    if self.time_stats_discontinuity is not None:
                        return True

                    if self.time_vrouter_up is not None:
                        return True

                    if self.tracked_interface_count is not None:
                        return True

                    if self.tracked_interface_up_count is not None:
                        return True

                    if self.tracked_item_count is not None:
                        return True

                    if self.tracked_item_up_count is not None:
                        return True

                    if self.ttl_error_count is not None:
                        return True

                    if self.version is not None:
                        return True

                    if self.virtual_linklocal_ipv6_address is not None:
                        return True

                    if self.virtual_mac_address is not None:
                        return True

                    if self.virtual_mac_address_state is not None:
                        return True

                    if self.virtual_router_id_xr is not None:
                        return True

                    if self.vrrp_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                    return meta._meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv6/Cisco-IOS-XR-ipv4-vrrp-oper:virtual-routers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.virtual_router is not None:
                    for child_ref in self.virtual_router:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                return meta._meta_table['Vrrp.Ipv6.VirtualRouters']['meta_info']


        class Interfaces(object):
            """
            The VRRP interface table
            
            .. attribute:: interface
            
            	A VRRP interface entry
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                A VRRP interface entry
                
                .. attribute:: interface_name  <key>
                
                	The name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: invalid_checksum_count
                
                	Invalid checksum
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_packet_length_count
                
                	Bad packet lengths
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_version_count
                
                	Unknown/unsupported version
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_vrid_count
                
                	Invalid vrID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2016-12-16'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.interface = None
                    self.invalid_checksum_count = None
                    self.invalid_packet_length_count = None
                    self.invalid_version_count = None
                    self.invalid_vrid_count = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv6/Cisco-IOS-XR-ipv4-vrrp-oper:interfaces/Cisco-IOS-XR-ipv4-vrrp-oper:interface[Cisco-IOS-XR-ipv4-vrrp-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.invalid_checksum_count is not None:
                        return True

                    if self.invalid_packet_length_count is not None:
                        return True

                    if self.invalid_version_count is not None:
                        return True

                    if self.invalid_vrid_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                    return meta._meta_table['Vrrp.Ipv6.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv6/Cisco-IOS-XR-ipv4-vrrp-oper:interfaces'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                return meta._meta_table['Vrrp.Ipv6.Interfaces']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv6'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.track_items is not None and self.track_items._has_data():
                return True

            if self.virtual_routers is not None and self.virtual_routers._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
            return meta._meta_table['Vrrp.Ipv6']['meta_info']


    class Ipv4(object):
        """
        IPv4 VRRP configuration
        
        .. attribute:: interfaces
        
        	The VRRP interface table
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.Interfaces>`
        
        .. attribute:: track_items
        
        	The VRRP tracked item table
        	**type**\:   :py:class:`TrackItems <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.TrackItems>`
        
        .. attribute:: virtual_routers
        
        	The VRRP virtual router table
        	**type**\:   :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters>`
        
        

        """

        _prefix = 'ipv4-vrrp-oper'
        _revision = '2016-12-16'

        def __init__(self):
            self.parent = None
            self.interfaces = Vrrp.Ipv4.Interfaces()
            self.interfaces.parent = self
            self.track_items = Vrrp.Ipv4.TrackItems()
            self.track_items.parent = self
            self.virtual_routers = Vrrp.Ipv4.VirtualRouters()
            self.virtual_routers.parent = self


        class Interfaces(object):
            """
            The VRRP interface table
            
            .. attribute:: interface
            
            	A VRRP interface entry
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                A VRRP interface entry
                
                .. attribute:: interface_name  <key>
                
                	The name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: invalid_checksum_count
                
                	Invalid checksum
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_packet_length_count
                
                	Bad packet lengths
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_version_count
                
                	Unknown/unsupported version
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_vrid_count
                
                	Invalid vrID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2016-12-16'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.interface = None
                    self.invalid_checksum_count = None
                    self.invalid_packet_length_count = None
                    self.invalid_version_count = None
                    self.invalid_vrid_count = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv4/Cisco-IOS-XR-ipv4-vrrp-oper:interfaces/Cisco-IOS-XR-ipv4-vrrp-oper:interface[Cisco-IOS-XR-ipv4-vrrp-oper:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.invalid_checksum_count is not None:
                        return True

                    if self.invalid_packet_length_count is not None:
                        return True

                    if self.invalid_version_count is not None:
                        return True

                    if self.invalid_vrid_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                    return meta._meta_table['Vrrp.Ipv4.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv4/Cisco-IOS-XR-ipv4-vrrp-oper:interfaces'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                return meta._meta_table['Vrrp.Ipv4.Interfaces']['meta_info']


        class TrackItems(object):
            """
            The VRRP tracked item table
            
            .. attribute:: track_item
            
            	A configured VRRP IP address entry
            	**type**\: list of    :py:class:`TrackItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.TrackItems.TrackItem>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                self.parent = None
                self.track_item = YList()
                self.track_item.parent = self
                self.track_item.name = 'track_item'


            class TrackItem(object):
                """
                A configured VRRP IP address entry
                
                .. attribute:: interface_name  <key>
                
                	The interface name to track
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: virtual_router_id  <key>
                
                	The VRRP virtual router id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tracked_interface_name  <key>
                
                	The name of the tracked interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: priority
                
                	Priority weight of item
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: state
                
                	State of the tracked item
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: tracked_item_index
                
                	Tracked item index
                	**type**\:  str
                
                	**length:** 0..32
                
                .. attribute:: tracked_item_type
                
                	Type of tracked item
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: virtual_router_id_xr
                
                	Virtual Router ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2016-12-16'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.virtual_router_id = None
                    self.tracked_interface_name = None
                    self.interface = None
                    self.priority = None
                    self.state = None
                    self.tracked_item_index = None
                    self.tracked_item_type = None
                    self.virtual_router_id_xr = None

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')
                    if self.virtual_router_id is None:
                        raise YPYModelError('Key property virtual_router_id is None')
                    if self.tracked_interface_name is None:
                        raise YPYModelError('Key property tracked_interface_name is None')

                    return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv4/Cisco-IOS-XR-ipv4-vrrp-oper:track-items/Cisco-IOS-XR-ipv4-vrrp-oper:track-item[Cisco-IOS-XR-ipv4-vrrp-oper:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv4-vrrp-oper:virtual-router-id = ' + str(self.virtual_router_id) + '][Cisco-IOS-XR-ipv4-vrrp-oper:tracked-interface-name = ' + str(self.tracked_interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.virtual_router_id is not None:
                        return True

                    if self.tracked_interface_name is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.priority is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.tracked_item_index is not None:
                        return True

                    if self.tracked_item_type is not None:
                        return True

                    if self.virtual_router_id_xr is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                    return meta._meta_table['Vrrp.Ipv4.TrackItems.TrackItem']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv4/Cisco-IOS-XR-ipv4-vrrp-oper:track-items'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.track_item is not None:
                    for child_ref in self.track_item:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                return meta._meta_table['Vrrp.Ipv4.TrackItems']['meta_info']


        class VirtualRouters(object):
            """
            The VRRP virtual router table
            
            .. attribute:: virtual_router
            
            	A VRRP virtual router
            	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                self.parent = None
                self.virtual_router = YList()
                self.virtual_router.parent = self
                self.virtual_router.name = 'virtual_router'


            class VirtualRouter(object):
                """
                A VRRP virtual router
                
                .. attribute:: interface_name  <key>
                
                	The name of the interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: virtual_router_id  <key>
                
                	The VRRP virtual router id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:   :py:class:`VrrpBAfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBAfEnum>`
                
                .. attribute:: address_list_error_count
                
                	Address list errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: advert_interval_error_count
                
                	Advertise interval errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: adverts_received_count
                
                	No. of advertisements received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: adverts_sent_count
                
                	No. of advertisements sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: auth_type_mismatch_count
                
                	Authentication type mismatches
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_fail_count
                
                	Authentication failures
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_flag
                
                	Text authentication configured flag
                	**type**\:  bool
                
                .. attribute:: authentication_string
                
                	Authentication data
                	**type**\:  str
                
                .. attribute:: authentication_type
                
                	Authentication type
                	**type**\:   :py:class:`VrrpProtAuthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpProtAuthEnum>`
                
                .. attribute:: bfd_cfg_remote_ip
                
                	BFD configured remote IP
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_configured_remote_ipv6_address
                
                	BFD configured remote IPv6
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
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
                	**type**\:   :py:class:`VrrpBfdSessionStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBfdSessionStateEnum>`
                
                .. attribute:: configured_advertize_time
                
                	Configured advertize time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: configured_down_address_count
                
                	 Configured but Down VRRP address count
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: configured_priority
                
                	Configured priority
                	**type**\:  int
                
                	**range:** 0..255
                
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
                
                .. attribute:: force_timer_flag
                
                	Configured timers forced flag
                	**type**\:  bool
                
                .. attribute:: interface_ipv4_address
                
                	The Interface Primary IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: interface_ipv6_address
                
                	The Interface linklocal IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: interface_name_xr
                
                	IM Interface Name
                	**type**\:  str
                
                	**length:** 0..64
                
                .. attribute:: invalid_auth_type_count
                
                	Invalid authentication type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_packet_count
                
                	Invalid packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_address_owner_flag
                
                	IP address owner flag
                	**type**\:  bool
                
                .. attribute:: ipv4_configured_down_address
                
                	IPv4 Configured but Down VRRP addresses
                	**type**\:  list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_configured_down_address
                
                	IPv6 Configured but Down VRRP addresses
                	**type**\: list of    :py:class:`Ipv6ConfiguredDownAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress>`
                
                .. attribute:: ipv6_operational_address
                
                	IPv6 Operational VRRP addresses
                	**type**\: list of    :py:class:`Ipv6OperationalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress>`
                
                .. attribute:: is_accept_mode
                
                	Is accept mode
                	**type**\:  bool
                
                .. attribute:: is_slave
                
                	Group is a slave group
                	**type**\:  bool
                
                .. attribute:: master_count
                
                	No. of times become Master
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: master_ip_address
                
                	Master router real IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: master_ipv6_address
                
                	Master router real IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: master_priority
                
                	Master router priority
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: min_delay_time
                
                	Minimum delay time in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: oper_advertize_time
                
                	Operational advertize time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_address
                
                	Operational IPv4 VRRP addresses
                	**type**\:  list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: operational_address_count
                
                	Operational VRRP address count
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: operational_priority
                
                	Operational priority
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: pkt_length_errors_count
                
                	Packet length errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: preempt_delay_time
                
                	Preempt delay time
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: preempt_flag
                
                	Preempt configured flag
                	**type**\:  bool
                
                .. attribute:: primary_state
                
                	State of primary IP address
                	**type**\:   :py:class:`VrrpVipStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVipStateEnum>`
                
                .. attribute:: primary_virtual_ip
                
                	Configured IPv4 Primary address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: priority_decrement
                
                	Priority decrement
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority_zero_received_count
                
                	No. priority 0 received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority_zero_sent_count
                
                	No. priority 0 sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: reload_delay_time
                
                	Reload delay time in msecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: resign_received_time
                
                	Time last resign was received
                	**type**\:   :py:class:`ResignReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime>`
                
                .. attribute:: resign_sent_time
                
                	Time last resign was sent
                	**type**\:   :py:class:`ResignSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime>`
                
                .. attribute:: secondary_address_count
                
                	Configured VRRP secondary address count
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: session_name
                
                	Session Name
                	**type**\:  str
                
                	**length:** 0..16
                
                .. attribute:: slaves
                
                	Number of slaves following state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_change_count
                
                	Number of state changes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_change_history
                
                	State change history
                	**type**\: list of    :py:class:`StateChangeHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory>`
                
                .. attribute:: state_from_checkpoint
                
                	Whether state recovered from checkpoint
                	**type**\:  bool
                
                .. attribute:: time_in_current_state
                
                	Time in current state secs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: time_stats_discontinuity
                
                	Time since a statistics discontinuity in ticks (10ns units)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: time_vrouter_up
                
                	Time vrouter is up in centiseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: centisecond
                
                .. attribute:: tracked_interface_count
                
                	Number of items tracked
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_up_count
                
                	Number of tracked items up
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_item_count
                
                	Number of tracked items
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_item_up_count
                
                	Number of tracked items in UP state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ttl_error_count
                
                	TTL errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: version
                
                	VRRP Protocol Version
                	**type**\:  int
                
                	**range:** 0..255
                
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
                	**type**\:   :py:class:`VrrpVmacStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVmacStateEnum>`
                
                .. attribute:: virtual_router_id_xr
                
                	Virtual Router ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrrp_state
                
                	VRRP state
                	**type**\:   :py:class:`VrrpBagProtocolStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolStateEnum>`
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2016-12-16'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.virtual_router_id = None
                    self.address_family = None
                    self.address_list_error_count = None
                    self.advert_interval_error_count = None
                    self.adverts_received_count = None
                    self.adverts_sent_count = None
                    self.auth_type_mismatch_count = None
                    self.authentication_fail_count = None
                    self.authentication_flag = None
                    self.authentication_string = None
                    self.authentication_type = None
                    self.bfd_cfg_remote_ip = None
                    self.bfd_configured_remote_ipv6_address = None
                    self.bfd_interval = None
                    self.bfd_multiplier = None
                    self.bfd_session_state = None
                    self.configured_advertize_time = None
                    self.configured_down_address_count = None
                    self.configured_priority = None
                    self.delay_timer_flag = None
                    self.delay_timer_msecs = None
                    self.delay_timer_secs = None
                    self.followed_session_name = None
                    self.force_timer_flag = None
                    self.interface_ipv4_address = None
                    self.interface_ipv6_address = None
                    self.interface_name_xr = None
                    self.invalid_auth_type_count = None
                    self.invalid_packet_count = None
                    self.ip_address_owner_flag = None
                    self.ipv4_configured_down_address = YLeafList()
                    self.ipv4_configured_down_address.parent = self
                    self.ipv4_configured_down_address.name = 'ipv4_configured_down_address'
                    self.ipv6_configured_down_address = YList()
                    self.ipv6_configured_down_address.parent = self
                    self.ipv6_configured_down_address.name = 'ipv6_configured_down_address'
                    self.ipv6_operational_address = YList()
                    self.ipv6_operational_address.parent = self
                    self.ipv6_operational_address.name = 'ipv6_operational_address'
                    self.is_accept_mode = None
                    self.is_slave = None
                    self.master_count = None
                    self.master_ip_address = None
                    self.master_ipv6_address = None
                    self.master_priority = None
                    self.min_delay_time = None
                    self.oper_advertize_time = None
                    self.operational_address = YLeafList()
                    self.operational_address.parent = self
                    self.operational_address.name = 'operational_address'
                    self.operational_address_count = None
                    self.operational_priority = None
                    self.pkt_length_errors_count = None
                    self.preempt_delay_time = None
                    self.preempt_flag = None
                    self.primary_state = None
                    self.primary_virtual_ip = None
                    self.priority_decrement = None
                    self.priority_zero_received_count = None
                    self.priority_zero_sent_count = None
                    self.reload_delay_time = None
                    self.resign_received_time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self.resign_sent_time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self.secondary_address_count = None
                    self.session_name = None
                    self.slaves = None
                    self.state_change_count = None
                    self.state_change_history = YList()
                    self.state_change_history.parent = self
                    self.state_change_history.name = 'state_change_history'
                    self.state_from_checkpoint = None
                    self.time_in_current_state = None
                    self.time_stats_discontinuity = None
                    self.time_vrouter_up = None
                    self.tracked_interface_count = None
                    self.tracked_interface_up_count = None
                    self.tracked_item_count = None
                    self.tracked_item_up_count = None
                    self.ttl_error_count = None
                    self.version = None
                    self.virtual_linklocal_ipv6_address = None
                    self.virtual_mac_address = None
                    self.virtual_mac_address_state = None
                    self.virtual_router_id_xr = None
                    self.vrrp_state = None


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

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:resign-sent-time'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                        return meta._meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime']['meta_info']


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

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:resign-received-time'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                        return meta._meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime']['meta_info']


                class Ipv6OperationalAddress(object):
                    """
                    IPv6 Operational VRRP addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:ipv6-operational-address'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv6_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                        return meta._meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress']['meta_info']


                class Ipv6ConfiguredDownAddress(object):
                    """
                    IPv6 Configured but Down VRRP addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:ipv6-configured-down-address'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv6_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                        return meta._meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress']['meta_info']


                class StateChangeHistory(object):
                    """
                    State change history
                    
                    .. attribute:: new_state
                    
                    	New State
                    	**type**\:   :py:class:`VrrpBagProtocolStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolStateEnum>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:   :py:class:`VrrpBagProtocolStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolStateEnum>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:   :py:class:`VrrpStateChangeReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpStateChangeReasonEnum>`
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:   :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        self.parent = None
                        self.new_state = None
                        self.old_state = None
                        self.reason = None
                        self.time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time()
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

                        _prefix = 'ipv4-vrrp-oper'
                        _revision = '2016-12-16'

                        def __init__(self):
                            self.parent = None
                            self.nanoseconds = None
                            self.seconds = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:time'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                            return meta._meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:state-change-history'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                        return meta._meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')
                    if self.virtual_router_id is None:
                        raise YPYModelError('Key property virtual_router_id is None')

                    return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv4/Cisco-IOS-XR-ipv4-vrrp-oper:virtual-routers/Cisco-IOS-XR-ipv4-vrrp-oper:virtual-router[Cisco-IOS-XR-ipv4-vrrp-oper:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv4-vrrp-oper:virtual-router-id = ' + str(self.virtual_router_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.virtual_router_id is not None:
                        return True

                    if self.address_family is not None:
                        return True

                    if self.address_list_error_count is not None:
                        return True

                    if self.advert_interval_error_count is not None:
                        return True

                    if self.adverts_received_count is not None:
                        return True

                    if self.adverts_sent_count is not None:
                        return True

                    if self.auth_type_mismatch_count is not None:
                        return True

                    if self.authentication_fail_count is not None:
                        return True

                    if self.authentication_flag is not None:
                        return True

                    if self.authentication_string is not None:
                        return True

                    if self.authentication_type is not None:
                        return True

                    if self.bfd_cfg_remote_ip is not None:
                        return True

                    if self.bfd_configured_remote_ipv6_address is not None:
                        return True

                    if self.bfd_interval is not None:
                        return True

                    if self.bfd_multiplier is not None:
                        return True

                    if self.bfd_session_state is not None:
                        return True

                    if self.configured_advertize_time is not None:
                        return True

                    if self.configured_down_address_count is not None:
                        return True

                    if self.configured_priority is not None:
                        return True

                    if self.delay_timer_flag is not None:
                        return True

                    if self.delay_timer_msecs is not None:
                        return True

                    if self.delay_timer_secs is not None:
                        return True

                    if self.followed_session_name is not None:
                        return True

                    if self.force_timer_flag is not None:
                        return True

                    if self.interface_ipv4_address is not None:
                        return True

                    if self.interface_ipv6_address is not None:
                        return True

                    if self.interface_name_xr is not None:
                        return True

                    if self.invalid_auth_type_count is not None:
                        return True

                    if self.invalid_packet_count is not None:
                        return True

                    if self.ip_address_owner_flag is not None:
                        return True

                    if self.ipv4_configured_down_address is not None:
                        for child in self.ipv4_configured_down_address:
                            if child is not None:
                                return True

                    if self.ipv6_configured_down_address is not None:
                        for child_ref in self.ipv6_configured_down_address:
                            if child_ref._has_data():
                                return True

                    if self.ipv6_operational_address is not None:
                        for child_ref in self.ipv6_operational_address:
                            if child_ref._has_data():
                                return True

                    if self.is_accept_mode is not None:
                        return True

                    if self.is_slave is not None:
                        return True

                    if self.master_count is not None:
                        return True

                    if self.master_ip_address is not None:
                        return True

                    if self.master_ipv6_address is not None:
                        return True

                    if self.master_priority is not None:
                        return True

                    if self.min_delay_time is not None:
                        return True

                    if self.oper_advertize_time is not None:
                        return True

                    if self.operational_address is not None:
                        for child in self.operational_address:
                            if child is not None:
                                return True

                    if self.operational_address_count is not None:
                        return True

                    if self.operational_priority is not None:
                        return True

                    if self.pkt_length_errors_count is not None:
                        return True

                    if self.preempt_delay_time is not None:
                        return True

                    if self.preempt_flag is not None:
                        return True

                    if self.primary_state is not None:
                        return True

                    if self.primary_virtual_ip is not None:
                        return True

                    if self.priority_decrement is not None:
                        return True

                    if self.priority_zero_received_count is not None:
                        return True

                    if self.priority_zero_sent_count is not None:
                        return True

                    if self.reload_delay_time is not None:
                        return True

                    if self.resign_received_time is not None and self.resign_received_time._has_data():
                        return True

                    if self.resign_sent_time is not None and self.resign_sent_time._has_data():
                        return True

                    if self.secondary_address_count is not None:
                        return True

                    if self.session_name is not None:
                        return True

                    if self.slaves is not None:
                        return True

                    if self.state_change_count is not None:
                        return True

                    if self.state_change_history is not None:
                        for child_ref in self.state_change_history:
                            if child_ref._has_data():
                                return True

                    if self.state_from_checkpoint is not None:
                        return True

                    if self.time_in_current_state is not None:
                        return True

                    if self.time_stats_discontinuity is not None:
                        return True

                    if self.time_vrouter_up is not None:
                        return True

                    if self.tracked_interface_count is not None:
                        return True

                    if self.tracked_interface_up_count is not None:
                        return True

                    if self.tracked_item_count is not None:
                        return True

                    if self.tracked_item_up_count is not None:
                        return True

                    if self.ttl_error_count is not None:
                        return True

                    if self.version is not None:
                        return True

                    if self.virtual_linklocal_ipv6_address is not None:
                        return True

                    if self.virtual_mac_address is not None:
                        return True

                    if self.virtual_mac_address_state is not None:
                        return True

                    if self.virtual_router_id_xr is not None:
                        return True

                    if self.vrrp_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                    return meta._meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv4/Cisco-IOS-XR-ipv4-vrrp-oper:virtual-routers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.virtual_router is not None:
                    for child_ref in self.virtual_router:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                return meta._meta_table['Vrrp.Ipv4.VirtualRouters']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:ipv4'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.track_items is not None and self.track_items._has_data():
                return True

            if self.virtual_routers is not None and self.virtual_routers._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
            return meta._meta_table['Vrrp.Ipv4']['meta_info']


    class MgoSessions(object):
        """
        VRRP MGO Session information
        
        .. attribute:: mgo_session
        
        	A VRRP MGO Session
        	**type**\: list of    :py:class:`MgoSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.MgoSessions.MgoSession>`
        
        

        """

        _prefix = 'ipv4-vrrp-oper'
        _revision = '2016-12-16'

        def __init__(self):
            self.parent = None
            self.mgo_session = YList()
            self.mgo_session.parent = self
            self.mgo_session.name = 'mgo_session'


        class MgoSession(object):
            """
            A VRRP MGO Session
            
            .. attribute:: session_name  <key>
            
            	The name of the session
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: primary_af_name
            
            	Address family of primary session
            	**type**\:   :py:class:`VrrpBAfEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBAfEnum>`
            
            .. attribute:: primary_session_interface
            
            	Interface of primary session
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: primary_session_name
            
            	Session Name
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: primary_session_number
            
            	VRID of primary session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: primary_session_state
            
            	State of primary session
            	**type**\:   :py:class:`VrrpBagProtocolStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolStateEnum>`
            
            .. attribute:: slave
            
            	List of slaves following this primary session
            	**type**\: list of    :py:class:`Slave <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.MgoSessions.MgoSession.Slave>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

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
                
                .. attribute:: slave_interface
                
                	Interface of slave
                	**type**\:  str
                
                	**length:** 0..64
                
                .. attribute:: slave_virtual_router_id
                
                	VRID of slave
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2016-12-16'

                def __init__(self):
                    self.parent = None
                    self.slave_interface = None
                    self.slave_virtual_router_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-vrrp-oper:slave'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.slave_interface is not None:
                        return True

                    if self.slave_virtual_router_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                    return meta._meta_table['Vrrp.MgoSessions.MgoSession.Slave']['meta_info']

            @property
            def _common_path(self):
                if self.session_name is None:
                    raise YPYModelError('Key property session_name is None')

                return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:mgo-sessions/Cisco-IOS-XR-ipv4-vrrp-oper:mgo-session[Cisco-IOS-XR-ipv4-vrrp-oper:session-name = ' + str(self.session_name) + ']'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
                return meta._meta_table['Vrrp.MgoSessions.MgoSession']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/Cisco-IOS-XR-ipv4-vrrp-oper:mgo-sessions'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
            return meta._meta_table['Vrrp.MgoSessions']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-vrrp-oper:vrrp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_vrrp_oper as meta
        return meta._meta_table['Vrrp']['meta_info']


