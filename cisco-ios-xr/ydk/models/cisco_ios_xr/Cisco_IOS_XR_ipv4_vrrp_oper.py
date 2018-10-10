""" Cisco_IOS_XR_ipv4_vrrp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-vrrp package operational data.

This module contains definitions
for the following management objects\:
  vrrp\: VRRP operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class VrrpBAf(Enum):
    """
    VrrpBAf (Enum Class)

    Vrrp b af

    .. data:: address_family_ipv4 = 0

    	IPv4 Address Family

    .. data:: address_family_ipv6 = 1

    	IPv6 Address Family

    .. data:: vrrp_baf_count = 2

    	Number of Adddress Families

    """

    address_family_ipv4 = Enum.YLeaf(0, "address-family-ipv4")

    address_family_ipv6 = Enum.YLeaf(1, "address-family-ipv6")

    vrrp_baf_count = Enum.YLeaf(2, "vrrp-baf-count")


class VrrpBagProtocolState(Enum):
    """
    VrrpBagProtocolState (Enum Class)

    VRRP protocol state

    .. data:: state_initial = 1

    	Initial

    .. data:: state_backup = 2

    	Backup

    .. data:: state_master = 3

    	Master

    """

    state_initial = Enum.YLeaf(1, "state-initial")

    state_backup = Enum.YLeaf(2, "state-backup")

    state_master = Enum.YLeaf(3, "state-master")


class VrrpBfdSessionState(Enum):
    """
    VrrpBfdSessionState (Enum Class)

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

    bfd_state_none = Enum.YLeaf(0, "bfd-state-none")

    bfd_state_inactive = Enum.YLeaf(1, "bfd-state-inactive")

    bfd_state_up = Enum.YLeaf(2, "bfd-state-up")

    bfd_state_down = Enum.YLeaf(3, "bfd-state-down")


class VrrpProtAuth(Enum):
    """
    VrrpProtAuth (Enum Class)

    Vrrp prot auth

    .. data:: authentication_none = 0

    	Down

    .. data:: authentication_text = 1

    	Simple Text

    .. data:: authentication_ip = 2

    	IP header

    """

    authentication_none = Enum.YLeaf(0, "authentication-none")

    authentication_text = Enum.YLeaf(1, "authentication-text")

    authentication_ip = Enum.YLeaf(2, "authentication-ip")


class VrrpStateChangeReason(Enum):
    """
    VrrpStateChangeReason (Enum Class)

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

    state_change_bfd_down = Enum.YLeaf(0, "state-change-bfd-down")

    state_change_virtual_ip_configured = Enum.YLeaf(1, "state-change-virtual-ip-configured")

    state_change_interface_ip = Enum.YLeaf(2, "state-change-interface-ip")

    state_change_delay_timer = Enum.YLeaf(3, "state-change-delay-timer")

    state_change_startup = Enum.YLeaf(4, "state-change-startup")

    state_change_interface_up = Enum.YLeaf(5, "state-change-interface-up")

    state_change_interface_down = Enum.YLeaf(6, "state-change-interface-down")

    state_change_master_down_timer = Enum.YLeaf(7, "state-change-master-down-timer")

    state_change_higher_priority_master = Enum.YLeaf(8, "state-change-higher-priority-master")

    state_change_fhrp_admin = Enum.YLeaf(9, "state-change-fhrp-admin")

    state_change_mgo_parent = Enum.YLeaf(10, "state-change-mgo-parent")

    state_change_chkpt_update = Enum.YLeaf(11, "state-change-chkpt-update")

    state_change_issu_resync = Enum.YLeaf(12, "state-change-issu-resync")


class VrrpVipState(Enum):
    """
    VrrpVipState (Enum Class)

    Vrrp vip state

    .. data:: virtual_ip_state_down = 0

    	Down

    .. data:: virtual_ip_state_up = 1

    	Up

    """

    virtual_ip_state_down = Enum.YLeaf(0, "virtual-ip-state-down")

    virtual_ip_state_up = Enum.YLeaf(1, "virtual-ip-state-up")


class VrrpVmacState(Enum):
    """
    VrrpVmacState (Enum Class)

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

    stored = Enum.YLeaf(0, "stored")

    reserved = Enum.YLeaf(1, "reserved")

    active = Enum.YLeaf(2, "active")

    reserving = Enum.YLeaf(3, "reserving")



class Vrrp(Entity):
    """
    VRRP operational data
    
    .. attribute:: summary
    
    	VRRP summary statistics
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Summary>`
    
    .. attribute:: ipv6
    
    	IPv6 VRRP configuration
    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6>`
    
    .. attribute:: ipv4
    
    	IPv4 VRRP configuration
    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4>`
    
    .. attribute:: mgo_sessions
    
    	VRRP MGO Session information
    	**type**\:  :py:class:`MgoSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.MgoSessions>`
    
    

    """

    _prefix = 'ipv4-vrrp-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(Vrrp, self).__init__()
        self._top_entity = None

        self.yang_name = "vrrp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-vrrp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("summary", ("summary", Vrrp.Summary)), ("ipv6", ("ipv6", Vrrp.Ipv6)), ("ipv4", ("ipv4", Vrrp.Ipv4)), ("mgo-sessions", ("mgo_sessions", Vrrp.MgoSessions))])
        self._leafs = OrderedDict()

        self.summary = Vrrp.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"

        self.ipv6 = Vrrp.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"

        self.ipv4 = Vrrp.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"

        self.mgo_sessions = Vrrp.MgoSessions()
        self.mgo_sessions.parent = self
        self._children_name_map["mgo_sessions"] = "mgo-sessions"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Vrrp, [], name, value)


    class Summary(Entity):
        """
        VRRP summary statistics
        
        .. attribute:: ipv4_sessions_master_owner
        
        	Number of IPv4 sessions in MASTER (owner) state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_master
        
        	Number of IPv4 sessions in MASTER state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_backup
        
        	Number of IPv4 sessions in BACKUP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_init
        
        	Number of IPv4 sessions in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_master
        
        	Number of IPv4 slaves in MASTER state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_backup
        
        	Number of IPv4 slaves in BACKUP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_init
        
        	Number of IPv4 slaves in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_master_owner_up
        
        	Number of UP IPv4 Virtual IP Addresses on virtual routers in MASTER (owner) state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_master_owner_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on virtual routers in MASTER (owner) state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_master_up
        
        	Number of UP IPv4 Virtual IP Addresses on virtual routers in MASTER state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_master_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on virtual routers in MASTER state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_backup_up
        
        	Number of UP IPv4 Virtual IP Addresses on virtual routers in BACKUP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_backup_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on virtual routers in BACKUP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_init_up
        
        	Number of UP IPv4 Virtual IP Addresses on virtual routers in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_init_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on virtual routers in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_master_owner
        
        	Number of IPv6 sessions in MASTER (owner) state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_master
        
        	Number of IPv6 sessions in MASTER state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_backup
        
        	Number of IPv6 sessions in BACKUP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_init
        
        	Number of IPv6 sessions in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_master
        
        	Number of IPv6 slaves in MASTER state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_backup
        
        	Number of IPv6 slaves in BACKUP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_init
        
        	Number of IPv6 slaves in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_master_owner_up
        
        	Number of UP IPv6 Virtual IP Addresses on virtual routers in MASTER (owner) state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_master_owner_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on virtual routers in MASTER (owner) state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_master_up
        
        	Number of UP IPv6 Virtual IP Addresses on virtual routers in MASTER state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_master_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on virtual routers in MASTER state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_backup_up
        
        	Number of UP IPv6 Virtual IP Addresses on virtual routers in BACKUP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_backup_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on virtual routers in BACKUP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_init_up
        
        	Number of UP IPv6 Virtual IP Addresses on virtual routers in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_init_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on virtual routers in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv4_state_up
        
        	Number of VRRP interfaces with IPv4 caps in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv4_state_down
        
        	Number of VRRP interfaces with IPv4 caps in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv4_state_up
        
        	Number of tracked interfaces with IPv4 caps in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv4_state_down
        
        	Number of tracked interfaces with IPv4 caps in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv6_state_up
        
        	Number of VRRP interfaces with IPv6 caps in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv6_state_down
        
        	Number of VRRP interfaces with IPv6 caps in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv6_state_up
        
        	Number of tracked interfaces with IPv6 caps in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv6_state_down
        
        	Number of tracked interfaces with IPv6 caps in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_objects_state_up
        
        	Number of tracked objects in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_objects_state_down
        
        	Number of tracked objects in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: bfd_sessions_up
        
        	Number of VRRP IPv4 BFD sessions in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: bfd_sessions_down
        
        	Number of VRRP IPv4 BFD sessions in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: bfd_session_inactive
        
        	Number of VRRP IPv4 BFD sessions in INACTIVE state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6bfd_sessions_up
        
        	Number of VRRP IPv6 BFD sessions in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6bfd_sessions_down
        
        	Number of VRRP IPv6 BFD sessions in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6bfd_session_inactive
        
        	Number of VRRP IPv6 BFD sessions in INACTIVE state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ipv4-vrrp-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vrrp.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "vrrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ipv4_sessions_master_owner', (YLeaf(YType.uint32, 'ipv4-sessions-master-owner'), ['int'])),
                ('ipv4_sessions_master', (YLeaf(YType.uint32, 'ipv4-sessions-master'), ['int'])),
                ('ipv4_sessions_backup', (YLeaf(YType.uint32, 'ipv4-sessions-backup'), ['int'])),
                ('ipv4_sessions_init', (YLeaf(YType.uint32, 'ipv4-sessions-init'), ['int'])),
                ('ipv4_slaves_master', (YLeaf(YType.uint32, 'ipv4-slaves-master'), ['int'])),
                ('ipv4_slaves_backup', (YLeaf(YType.uint32, 'ipv4-slaves-backup'), ['int'])),
                ('ipv4_slaves_init', (YLeaf(YType.uint32, 'ipv4-slaves-init'), ['int'])),
                ('ipv4_virtual_ip_addresses_master_owner_up', (YLeaf(YType.uint32, 'ipv4-virtual-ip-addresses-master-owner-up'), ['int'])),
                ('ipv4_virtual_ip_addresses_master_owner_down', (YLeaf(YType.uint32, 'ipv4-virtual-ip-addresses-master-owner-down'), ['int'])),
                ('ipv4_virtual_ip_addresses_master_up', (YLeaf(YType.uint32, 'ipv4-virtual-ip-addresses-master-up'), ['int'])),
                ('ipv4_virtual_ip_addresses_master_down', (YLeaf(YType.uint32, 'ipv4-virtual-ip-addresses-master-down'), ['int'])),
                ('ipv4_virtual_ip_addresses_backup_up', (YLeaf(YType.uint32, 'ipv4-virtual-ip-addresses-backup-up'), ['int'])),
                ('ipv4_virtual_ip_addresses_backup_down', (YLeaf(YType.uint32, 'ipv4-virtual-ip-addresses-backup-down'), ['int'])),
                ('ipv4_virtual_ip_addresses_init_up', (YLeaf(YType.uint32, 'ipv4-virtual-ip-addresses-init-up'), ['int'])),
                ('ipv4_virtual_ip_addresses_init_down', (YLeaf(YType.uint32, 'ipv4-virtual-ip-addresses-init-down'), ['int'])),
                ('ipv6_sessions_master_owner', (YLeaf(YType.uint32, 'ipv6-sessions-master-owner'), ['int'])),
                ('ipv6_sessions_master', (YLeaf(YType.uint32, 'ipv6-sessions-master'), ['int'])),
                ('ipv6_sessions_backup', (YLeaf(YType.uint32, 'ipv6-sessions-backup'), ['int'])),
                ('ipv6_sessions_init', (YLeaf(YType.uint32, 'ipv6-sessions-init'), ['int'])),
                ('ipv6_slaves_master', (YLeaf(YType.uint32, 'ipv6-slaves-master'), ['int'])),
                ('ipv6_slaves_backup', (YLeaf(YType.uint32, 'ipv6-slaves-backup'), ['int'])),
                ('ipv6_slaves_init', (YLeaf(YType.uint32, 'ipv6-slaves-init'), ['int'])),
                ('ipv6_virtual_ip_addresses_master_owner_up', (YLeaf(YType.uint32, 'ipv6-virtual-ip-addresses-master-owner-up'), ['int'])),
                ('ipv6_virtual_ip_addresses_master_owner_down', (YLeaf(YType.uint32, 'ipv6-virtual-ip-addresses-master-owner-down'), ['int'])),
                ('ipv6_virtual_ip_addresses_master_up', (YLeaf(YType.uint32, 'ipv6-virtual-ip-addresses-master-up'), ['int'])),
                ('ipv6_virtual_ip_addresses_master_down', (YLeaf(YType.uint32, 'ipv6-virtual-ip-addresses-master-down'), ['int'])),
                ('ipv6_virtual_ip_addresses_backup_up', (YLeaf(YType.uint32, 'ipv6-virtual-ip-addresses-backup-up'), ['int'])),
                ('ipv6_virtual_ip_addresses_backup_down', (YLeaf(YType.uint32, 'ipv6-virtual-ip-addresses-backup-down'), ['int'])),
                ('ipv6_virtual_ip_addresses_init_up', (YLeaf(YType.uint32, 'ipv6-virtual-ip-addresses-init-up'), ['int'])),
                ('ipv6_virtual_ip_addresses_init_down', (YLeaf(YType.uint32, 'ipv6-virtual-ip-addresses-init-down'), ['int'])),
                ('interfaces_ipv4_state_up', (YLeaf(YType.uint32, 'interfaces-ipv4-state-up'), ['int'])),
                ('interfaces_ipv4_state_down', (YLeaf(YType.uint32, 'interfaces-ipv4-state-down'), ['int'])),
                ('tracked_interfaces_ipv4_state_up', (YLeaf(YType.uint32, 'tracked-interfaces-ipv4-state-up'), ['int'])),
                ('tracked_interfaces_ipv4_state_down', (YLeaf(YType.uint32, 'tracked-interfaces-ipv4-state-down'), ['int'])),
                ('interfaces_ipv6_state_up', (YLeaf(YType.uint32, 'interfaces-ipv6-state-up'), ['int'])),
                ('interfaces_ipv6_state_down', (YLeaf(YType.uint32, 'interfaces-ipv6-state-down'), ['int'])),
                ('tracked_interfaces_ipv6_state_up', (YLeaf(YType.uint32, 'tracked-interfaces-ipv6-state-up'), ['int'])),
                ('tracked_interfaces_ipv6_state_down', (YLeaf(YType.uint32, 'tracked-interfaces-ipv6-state-down'), ['int'])),
                ('tracked_objects_state_up', (YLeaf(YType.uint32, 'tracked-objects-state-up'), ['int'])),
                ('tracked_objects_state_down', (YLeaf(YType.uint32, 'tracked-objects-state-down'), ['int'])),
                ('bfd_sessions_up', (YLeaf(YType.uint32, 'bfd-sessions-up'), ['int'])),
                ('bfd_sessions_down', (YLeaf(YType.uint32, 'bfd-sessions-down'), ['int'])),
                ('bfd_session_inactive', (YLeaf(YType.uint32, 'bfd-session-inactive'), ['int'])),
                ('ipv6bfd_sessions_up', (YLeaf(YType.uint32, 'ipv6bfd-sessions-up'), ['int'])),
                ('ipv6bfd_sessions_down', (YLeaf(YType.uint32, 'ipv6bfd-sessions-down'), ['int'])),
                ('ipv6bfd_session_inactive', (YLeaf(YType.uint32, 'ipv6bfd-session-inactive'), ['int'])),
            ])
            self.ipv4_sessions_master_owner = None
            self.ipv4_sessions_master = None
            self.ipv4_sessions_backup = None
            self.ipv4_sessions_init = None
            self.ipv4_slaves_master = None
            self.ipv4_slaves_backup = None
            self.ipv4_slaves_init = None
            self.ipv4_virtual_ip_addresses_master_owner_up = None
            self.ipv4_virtual_ip_addresses_master_owner_down = None
            self.ipv4_virtual_ip_addresses_master_up = None
            self.ipv4_virtual_ip_addresses_master_down = None
            self.ipv4_virtual_ip_addresses_backup_up = None
            self.ipv4_virtual_ip_addresses_backup_down = None
            self.ipv4_virtual_ip_addresses_init_up = None
            self.ipv4_virtual_ip_addresses_init_down = None
            self.ipv6_sessions_master_owner = None
            self.ipv6_sessions_master = None
            self.ipv6_sessions_backup = None
            self.ipv6_sessions_init = None
            self.ipv6_slaves_master = None
            self.ipv6_slaves_backup = None
            self.ipv6_slaves_init = None
            self.ipv6_virtual_ip_addresses_master_owner_up = None
            self.ipv6_virtual_ip_addresses_master_owner_down = None
            self.ipv6_virtual_ip_addresses_master_up = None
            self.ipv6_virtual_ip_addresses_master_down = None
            self.ipv6_virtual_ip_addresses_backup_up = None
            self.ipv6_virtual_ip_addresses_backup_down = None
            self.ipv6_virtual_ip_addresses_init_up = None
            self.ipv6_virtual_ip_addresses_init_down = None
            self.interfaces_ipv4_state_up = None
            self.interfaces_ipv4_state_down = None
            self.tracked_interfaces_ipv4_state_up = None
            self.tracked_interfaces_ipv4_state_down = None
            self.interfaces_ipv6_state_up = None
            self.interfaces_ipv6_state_down = None
            self.tracked_interfaces_ipv6_state_up = None
            self.tracked_interfaces_ipv6_state_down = None
            self.tracked_objects_state_up = None
            self.tracked_objects_state_down = None
            self.bfd_sessions_up = None
            self.bfd_sessions_down = None
            self.bfd_session_inactive = None
            self.ipv6bfd_sessions_up = None
            self.ipv6bfd_sessions_down = None
            self.ipv6bfd_session_inactive = None
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vrrp.Summary, [u'ipv4_sessions_master_owner', u'ipv4_sessions_master', u'ipv4_sessions_backup', u'ipv4_sessions_init', u'ipv4_slaves_master', u'ipv4_slaves_backup', u'ipv4_slaves_init', u'ipv4_virtual_ip_addresses_master_owner_up', u'ipv4_virtual_ip_addresses_master_owner_down', u'ipv4_virtual_ip_addresses_master_up', u'ipv4_virtual_ip_addresses_master_down', u'ipv4_virtual_ip_addresses_backup_up', u'ipv4_virtual_ip_addresses_backup_down', u'ipv4_virtual_ip_addresses_init_up', u'ipv4_virtual_ip_addresses_init_down', u'ipv6_sessions_master_owner', u'ipv6_sessions_master', u'ipv6_sessions_backup', u'ipv6_sessions_init', u'ipv6_slaves_master', u'ipv6_slaves_backup', u'ipv6_slaves_init', u'ipv6_virtual_ip_addresses_master_owner_up', u'ipv6_virtual_ip_addresses_master_owner_down', u'ipv6_virtual_ip_addresses_master_up', u'ipv6_virtual_ip_addresses_master_down', u'ipv6_virtual_ip_addresses_backup_up', u'ipv6_virtual_ip_addresses_backup_down', u'ipv6_virtual_ip_addresses_init_up', u'ipv6_virtual_ip_addresses_init_down', u'interfaces_ipv4_state_up', u'interfaces_ipv4_state_down', u'tracked_interfaces_ipv4_state_up', u'tracked_interfaces_ipv4_state_down', u'interfaces_ipv6_state_up', u'interfaces_ipv6_state_down', u'tracked_interfaces_ipv6_state_up', u'tracked_interfaces_ipv6_state_down', u'tracked_objects_state_up', u'tracked_objects_state_down', u'bfd_sessions_up', u'bfd_sessions_down', u'bfd_session_inactive', u'ipv6bfd_sessions_up', u'ipv6bfd_sessions_down', u'ipv6bfd_session_inactive'], name, value)


    class Ipv6(Entity):
        """
        IPv6 VRRP configuration
        
        .. attribute:: track_items
        
        	The VRRP tracked item table
        	**type**\:  :py:class:`TrackItems <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.TrackItems>`
        
        .. attribute:: virtual_routers
        
        	The VRRP virtual router table
        	**type**\:  :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters>`
        
        .. attribute:: interfaces
        
        	The VRRP interface table
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.Interfaces>`
        
        

        """

        _prefix = 'ipv4-vrrp-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vrrp.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "vrrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("track-items", ("track_items", Vrrp.Ipv6.TrackItems)), ("virtual-routers", ("virtual_routers", Vrrp.Ipv6.VirtualRouters)), ("interfaces", ("interfaces", Vrrp.Ipv6.Interfaces))])
            self._leafs = OrderedDict()

            self.track_items = Vrrp.Ipv6.TrackItems()
            self.track_items.parent = self
            self._children_name_map["track_items"] = "track-items"

            self.virtual_routers = Vrrp.Ipv6.VirtualRouters()
            self.virtual_routers.parent = self
            self._children_name_map["virtual_routers"] = "virtual-routers"

            self.interfaces = Vrrp.Ipv6.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._segment_path = lambda: "ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vrrp.Ipv6, [], name, value)


        class TrackItems(Entity):
            """
            The VRRP tracked item table
            
            .. attribute:: track_item
            
            	A configured VRRP IP address entry
            	**type**\: list of  		 :py:class:`TrackItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.TrackItems.TrackItem>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vrrp.Ipv6.TrackItems, self).__init__()

                self.yang_name = "track-items"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("track-item", ("track_item", Vrrp.Ipv6.TrackItems.TrackItem))])
                self._leafs = OrderedDict()

                self.track_item = YList(self)
                self._segment_path = lambda: "track-items"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrrp.Ipv6.TrackItems, [], name, value)


            class TrackItem(Entity):
                """
                A configured VRRP IP address entry
                
                .. attribute:: interface_name  (key)
                
                	The interface name to track
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: virtual_router_id  (key)
                
                	The VRRP virtual router id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_name  (key)
                
                	The name of the tracked interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: virtual_router_id_xr
                
                	Virtual Router ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_item_type
                
                	Type of tracked item
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: tracked_item_index
                
                	Tracked item index
                	**type**\: str
                
                	**length:** 0..32
                
                .. attribute:: state
                
                	State of the tracked item
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: priority
                
                	Priority weight of item
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vrrp.Ipv6.TrackItems.TrackItem, self).__init__()

                    self.yang_name = "track-item"
                    self.yang_parent_name = "track-items"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name','virtual_router_id','tracked_interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('virtual_router_id', (YLeaf(YType.uint32, 'virtual-router-id'), ['int'])),
                        ('tracked_interface_name', (YLeaf(YType.str, 'tracked-interface-name'), ['str'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('virtual_router_id_xr', (YLeaf(YType.uint32, 'virtual-router-id-xr'), ['int'])),
                        ('tracked_item_type', (YLeaf(YType.uint16, 'tracked-item-type'), ['int'])),
                        ('tracked_item_index', (YLeaf(YType.str, 'tracked-item-index'), ['str'])),
                        ('state', (YLeaf(YType.uint8, 'state'), ['int'])),
                        ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                    ])
                    self.interface_name = None
                    self.virtual_router_id = None
                    self.tracked_interface_name = None
                    self.interface = None
                    self.virtual_router_id_xr = None
                    self.tracked_item_type = None
                    self.tracked_item_index = None
                    self.state = None
                    self.priority = None
                    self._segment_path = lambda: "track-item" + "[interface-name='" + str(self.interface_name) + "']" + "[virtual-router-id='" + str(self.virtual_router_id) + "']" + "[tracked-interface-name='" + str(self.tracked_interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/track-items/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Ipv6.TrackItems.TrackItem, ['interface_name', 'virtual_router_id', 'tracked_interface_name', u'interface', u'virtual_router_id_xr', u'tracked_item_type', u'tracked_item_index', u'state', u'priority'], name, value)


        class VirtualRouters(Entity):
            """
            The VRRP virtual router table
            
            .. attribute:: virtual_router
            
            	A VRRP virtual router
            	**type**\: list of  		 :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vrrp.Ipv6.VirtualRouters, self).__init__()

                self.yang_name = "virtual-routers"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("virtual-router", ("virtual_router", Vrrp.Ipv6.VirtualRouters.VirtualRouter))])
                self._leafs = OrderedDict()

                self.virtual_router = YList(self)
                self._segment_path = lambda: "virtual-routers"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrrp.Ipv6.VirtualRouters, [], name, value)


            class VirtualRouter(Entity):
                """
                A VRRP virtual router
                
                .. attribute:: interface_name  (key)
                
                	The name of the interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: virtual_router_id  (key)
                
                	The VRRP virtual router id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: resign_sent_time
                
                	Time last resign was sent
                	**type**\:  :py:class:`ResignSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime>`
                
                .. attribute:: resign_received_time
                
                	Time last resign was received
                	**type**\:  :py:class:`ResignReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime>`
                
                .. attribute:: interface_name_xr
                
                	IM Interface Name
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: virtual_router_id_xr
                
                	Virtual Router ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: version
                
                	VRRP Protocol Version
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:  :py:class:`VrrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBAf>`
                
                .. attribute:: session_name
                
                	Session Name
                	**type**\: str
                
                	**length:** 0..16
                
                .. attribute:: slaves
                
                	Number of slaves following state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_slave
                
                	Group is a slave group
                	**type**\: bool
                
                .. attribute:: followed_session_name
                
                	Followed Session Name
                	**type**\: str
                
                	**length:** 0..16
                
                .. attribute:: secondary_address_count
                
                	Configured VRRP secondary address count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: operational_address_count
                
                	Operational VRRP address count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: primary_virtual_ip
                
                	Configured IPv4 Primary address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: configured_down_address_count
                
                	 Configured but Down VRRP address count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: virtual_linklocal_ipv6_address
                
                	Virtual linklocal IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: primary_state
                
                	State of primary IP address
                	**type**\:  :py:class:`VrrpVipState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVipState>`
                
                .. attribute:: master_ip_address
                
                	Master router real IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: master_ipv6_address
                
                	Master router real IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: master_priority
                
                	Master router priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: vrrp_state
                
                	VRRP state
                	**type**\:  :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                
                .. attribute:: authentication_type
                
                	Authentication type
                	**type**\:  :py:class:`VrrpProtAuth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpProtAuth>`
                
                .. attribute:: authentication_string
                
                	Authentication data
                	**type**\: str
                
                .. attribute:: configured_advertize_time
                
                	Configured advertize time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: oper_advertize_time
                
                	Operational advertize time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: min_delay_time
                
                	Minimum delay time in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: reload_delay_time
                
                	Reload delay time in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: delay_timer_flag
                
                	Delay timer running flag
                	**type**\: bool
                
                .. attribute:: delay_timer_secs
                
                	Delay timer running time secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: delay_timer_msecs
                
                	Delay timer running time msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: authentication_flag
                
                	Text authentication configured flag
                	**type**\: bool
                
                .. attribute:: force_timer_flag
                
                	Configured timers forced flag
                	**type**\: bool
                
                .. attribute:: preempt_flag
                
                	Preempt configured flag
                	**type**\: bool
                
                .. attribute:: ip_address_owner_flag
                
                	IP address owner flag
                	**type**\: bool
                
                .. attribute:: is_accept_mode
                
                	Is accept mode
                	**type**\: bool
                
                .. attribute:: preempt_delay_time
                
                	Preempt delay time
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: configured_priority
                
                	Configured priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: operational_priority
                
                	Operational priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: priority_decrement
                
                	Priority decrement
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_count
                
                	Number of items tracked
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_up_count
                
                	Number of tracked items up
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_item_count
                
                	Number of tracked items
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_item_up_count
                
                	Number of tracked items in UP state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: time_in_current_state
                
                	Time in current state secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: state_change_count
                
                	Number of state changes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: time_vrouter_up
                
                	Time vrouter is up in centiseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: centisecond
                
                .. attribute:: master_count
                
                	No. of times become Master
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: adverts_received_count
                
                	No. of advertisements received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: advert_interval_error_count
                
                	Advertise interval errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: adverts_sent_count
                
                	No. of advertisements sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_fail_count
                
                	Authentication failures
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ttl_error_count
                
                	TTL errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority_zero_received_count
                
                	No. priority 0 received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority_zero_sent_count
                
                	No. priority 0 sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_packet_count
                
                	Invalid packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: address_list_error_count
                
                	Address list errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_auth_type_count
                
                	Invalid authentication type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: auth_type_mismatch_count
                
                	Authentication type mismatches
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_length_errors_count
                
                	Packet length errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: time_stats_discontinuity
                
                	Time since a statistics discontinuity in ticks (10ns units)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_session_state
                
                	BFD session state
                	**type**\:  :py:class:`VrrpBfdSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBfdSessionState>`
                
                .. attribute:: bfd_interval
                
                	BFD packet send interval
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_multiplier
                
                	BFD multiplier
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_cfg_remote_ip
                
                	BFD configured remote IP
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_configured_remote_ipv6_address
                
                	BFD configured remote IPv6
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: state_from_checkpoint
                
                	Whether state recovered from checkpoint
                	**type**\: bool
                
                .. attribute:: interface_ipv4_address
                
                	The Interface Primary IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: interface_ipv6_address
                
                	The Interface linklocal IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtual_mac_address
                
                	Virtual mac address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: virtual_mac_address_state
                
                	Virtual mac address state
                	**type**\:  :py:class:`VrrpVmacState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVmacState>`
                
                .. attribute:: operational_address
                
                	Operational IPv4 VRRP addresses
                	**type**\: list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4_configured_down_address
                
                	IPv4 Configured but Down VRRP addresses
                	**type**\: list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_operational_address
                
                	IPv6 Operational VRRP addresses
                	**type**\: list of  		 :py:class:`Ipv6OperationalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress>`
                
                .. attribute:: ipv6_configured_down_address
                
                	IPv6 Configured but Down VRRP addresses
                	**type**\: list of  		 :py:class:`Ipv6ConfiguredDownAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress>`
                
                .. attribute:: track_item_info
                
                	Track Item Info
                	**type**\: list of  		 :py:class:`TrackItemInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.TrackItemInfo>`
                
                .. attribute:: state_change_history
                
                	State change history
                	**type**\: list of  		 :py:class:`StateChangeHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory>`
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vrrp.Ipv6.VirtualRouters.VirtualRouter, self).__init__()

                    self.yang_name = "virtual-router"
                    self.yang_parent_name = "virtual-routers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name','virtual_router_id']
                    self._child_classes = OrderedDict([("resign-sent-time", ("resign_sent_time", Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime)), ("resign-received-time", ("resign_received_time", Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime)), ("ipv6-operational-address", ("ipv6_operational_address", Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress)), ("ipv6-configured-down-address", ("ipv6_configured_down_address", Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress)), ("track-item-info", ("track_item_info", Vrrp.Ipv6.VirtualRouters.VirtualRouter.TrackItemInfo)), ("state-change-history", ("state_change_history", Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory))])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('virtual_router_id', (YLeaf(YType.uint32, 'virtual-router-id'), ['int'])),
                        ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                        ('virtual_router_id_xr', (YLeaf(YType.uint32, 'virtual-router-id-xr'), ['int'])),
                        ('version', (YLeaf(YType.uint8, 'version'), ['int'])),
                        ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBAf', '')])),
                        ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                        ('slaves', (YLeaf(YType.uint32, 'slaves'), ['int'])),
                        ('is_slave', (YLeaf(YType.boolean, 'is-slave'), ['bool'])),
                        ('followed_session_name', (YLeaf(YType.str, 'followed-session-name'), ['str'])),
                        ('secondary_address_count', (YLeaf(YType.uint8, 'secondary-address-count'), ['int'])),
                        ('operational_address_count', (YLeaf(YType.uint8, 'operational-address-count'), ['int'])),
                        ('primary_virtual_ip', (YLeaf(YType.str, 'primary-virtual-ip'), ['str'])),
                        ('configured_down_address_count', (YLeaf(YType.uint8, 'configured-down-address-count'), ['int'])),
                        ('virtual_linklocal_ipv6_address', (YLeaf(YType.str, 'virtual-linklocal-ipv6-address'), ['str'])),
                        ('primary_state', (YLeaf(YType.enumeration, 'primary-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpVipState', '')])),
                        ('master_ip_address', (YLeaf(YType.str, 'master-ip-address'), ['str'])),
                        ('master_ipv6_address', (YLeaf(YType.str, 'master-ipv6-address'), ['str'])),
                        ('master_priority', (YLeaf(YType.uint8, 'master-priority'), ['int'])),
                        ('vrrp_state', (YLeaf(YType.enumeration, 'vrrp-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolState', '')])),
                        ('authentication_type', (YLeaf(YType.enumeration, 'authentication-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpProtAuth', '')])),
                        ('authentication_string', (YLeaf(YType.str, 'authentication-string'), ['str'])),
                        ('configured_advertize_time', (YLeaf(YType.uint32, 'configured-advertize-time'), ['int'])),
                        ('oper_advertize_time', (YLeaf(YType.uint32, 'oper-advertize-time'), ['int'])),
                        ('min_delay_time', (YLeaf(YType.uint32, 'min-delay-time'), ['int'])),
                        ('reload_delay_time', (YLeaf(YType.uint32, 'reload-delay-time'), ['int'])),
                        ('delay_timer_flag', (YLeaf(YType.boolean, 'delay-timer-flag'), ['bool'])),
                        ('delay_timer_secs', (YLeaf(YType.uint32, 'delay-timer-secs'), ['int'])),
                        ('delay_timer_msecs', (YLeaf(YType.uint32, 'delay-timer-msecs'), ['int'])),
                        ('authentication_flag', (YLeaf(YType.boolean, 'authentication-flag'), ['bool'])),
                        ('force_timer_flag', (YLeaf(YType.boolean, 'force-timer-flag'), ['bool'])),
                        ('preempt_flag', (YLeaf(YType.boolean, 'preempt-flag'), ['bool'])),
                        ('ip_address_owner_flag', (YLeaf(YType.boolean, 'ip-address-owner-flag'), ['bool'])),
                        ('is_accept_mode', (YLeaf(YType.boolean, 'is-accept-mode'), ['bool'])),
                        ('preempt_delay_time', (YLeaf(YType.uint16, 'preempt-delay-time'), ['int'])),
                        ('configured_priority', (YLeaf(YType.uint8, 'configured-priority'), ['int'])),
                        ('operational_priority', (YLeaf(YType.uint8, 'operational-priority'), ['int'])),
                        ('priority_decrement', (YLeaf(YType.uint32, 'priority-decrement'), ['int'])),
                        ('tracked_interface_count', (YLeaf(YType.uint32, 'tracked-interface-count'), ['int'])),
                        ('tracked_interface_up_count', (YLeaf(YType.uint32, 'tracked-interface-up-count'), ['int'])),
                        ('tracked_item_count', (YLeaf(YType.uint32, 'tracked-item-count'), ['int'])),
                        ('tracked_item_up_count', (YLeaf(YType.uint32, 'tracked-item-up-count'), ['int'])),
                        ('time_in_current_state', (YLeaf(YType.uint32, 'time-in-current-state'), ['int'])),
                        ('state_change_count', (YLeaf(YType.uint32, 'state-change-count'), ['int'])),
                        ('time_vrouter_up', (YLeaf(YType.uint32, 'time-vrouter-up'), ['int'])),
                        ('master_count', (YLeaf(YType.uint32, 'master-count'), ['int'])),
                        ('adverts_received_count', (YLeaf(YType.uint32, 'adverts-received-count'), ['int'])),
                        ('advert_interval_error_count', (YLeaf(YType.uint32, 'advert-interval-error-count'), ['int'])),
                        ('adverts_sent_count', (YLeaf(YType.uint32, 'adverts-sent-count'), ['int'])),
                        ('authentication_fail_count', (YLeaf(YType.uint32, 'authentication-fail-count'), ['int'])),
                        ('ttl_error_count', (YLeaf(YType.uint32, 'ttl-error-count'), ['int'])),
                        ('priority_zero_received_count', (YLeaf(YType.uint32, 'priority-zero-received-count'), ['int'])),
                        ('priority_zero_sent_count', (YLeaf(YType.uint32, 'priority-zero-sent-count'), ['int'])),
                        ('invalid_packet_count', (YLeaf(YType.uint32, 'invalid-packet-count'), ['int'])),
                        ('address_list_error_count', (YLeaf(YType.uint32, 'address-list-error-count'), ['int'])),
                        ('invalid_auth_type_count', (YLeaf(YType.uint32, 'invalid-auth-type-count'), ['int'])),
                        ('auth_type_mismatch_count', (YLeaf(YType.uint32, 'auth-type-mismatch-count'), ['int'])),
                        ('pkt_length_errors_count', (YLeaf(YType.uint32, 'pkt-length-errors-count'), ['int'])),
                        ('time_stats_discontinuity', (YLeaf(YType.uint32, 'time-stats-discontinuity'), ['int'])),
                        ('bfd_session_state', (YLeaf(YType.enumeration, 'bfd-session-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBfdSessionState', '')])),
                        ('bfd_interval', (YLeaf(YType.uint32, 'bfd-interval'), ['int'])),
                        ('bfd_multiplier', (YLeaf(YType.uint32, 'bfd-multiplier'), ['int'])),
                        ('bfd_cfg_remote_ip', (YLeaf(YType.str, 'bfd-cfg-remote-ip'), ['str'])),
                        ('bfd_configured_remote_ipv6_address', (YLeaf(YType.str, 'bfd-configured-remote-ipv6-address'), ['str'])),
                        ('state_from_checkpoint', (YLeaf(YType.boolean, 'state-from-checkpoint'), ['bool'])),
                        ('interface_ipv4_address', (YLeaf(YType.str, 'interface-ipv4-address'), ['str'])),
                        ('interface_ipv6_address', (YLeaf(YType.str, 'interface-ipv6-address'), ['str'])),
                        ('virtual_mac_address', (YLeaf(YType.str, 'virtual-mac-address'), ['str'])),
                        ('virtual_mac_address_state', (YLeaf(YType.enumeration, 'virtual-mac-address-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpVmacState', '')])),
                        ('operational_address', (YLeafList(YType.str, 'operational-address'), ['str'])),
                        ('ipv4_configured_down_address', (YLeafList(YType.str, 'ipv4-configured-down-address'), ['str'])),
                    ])
                    self.interface_name = None
                    self.virtual_router_id = None
                    self.interface_name_xr = None
                    self.virtual_router_id_xr = None
                    self.version = None
                    self.address_family = None
                    self.session_name = None
                    self.slaves = None
                    self.is_slave = None
                    self.followed_session_name = None
                    self.secondary_address_count = None
                    self.operational_address_count = None
                    self.primary_virtual_ip = None
                    self.configured_down_address_count = None
                    self.virtual_linklocal_ipv6_address = None
                    self.primary_state = None
                    self.master_ip_address = None
                    self.master_ipv6_address = None
                    self.master_priority = None
                    self.vrrp_state = None
                    self.authentication_type = None
                    self.authentication_string = None
                    self.configured_advertize_time = None
                    self.oper_advertize_time = None
                    self.min_delay_time = None
                    self.reload_delay_time = None
                    self.delay_timer_flag = None
                    self.delay_timer_secs = None
                    self.delay_timer_msecs = None
                    self.authentication_flag = None
                    self.force_timer_flag = None
                    self.preempt_flag = None
                    self.ip_address_owner_flag = None
                    self.is_accept_mode = None
                    self.preempt_delay_time = None
                    self.configured_priority = None
                    self.operational_priority = None
                    self.priority_decrement = None
                    self.tracked_interface_count = None
                    self.tracked_interface_up_count = None
                    self.tracked_item_count = None
                    self.tracked_item_up_count = None
                    self.time_in_current_state = None
                    self.state_change_count = None
                    self.time_vrouter_up = None
                    self.master_count = None
                    self.adverts_received_count = None
                    self.advert_interval_error_count = None
                    self.adverts_sent_count = None
                    self.authentication_fail_count = None
                    self.ttl_error_count = None
                    self.priority_zero_received_count = None
                    self.priority_zero_sent_count = None
                    self.invalid_packet_count = None
                    self.address_list_error_count = None
                    self.invalid_auth_type_count = None
                    self.auth_type_mismatch_count = None
                    self.pkt_length_errors_count = None
                    self.time_stats_discontinuity = None
                    self.bfd_session_state = None
                    self.bfd_interval = None
                    self.bfd_multiplier = None
                    self.bfd_cfg_remote_ip = None
                    self.bfd_configured_remote_ipv6_address = None
                    self.state_from_checkpoint = None
                    self.interface_ipv4_address = None
                    self.interface_ipv6_address = None
                    self.virtual_mac_address = None
                    self.virtual_mac_address_state = None
                    self.operational_address = []
                    self.ipv4_configured_down_address = []

                    self.resign_sent_time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self._children_name_map["resign_sent_time"] = "resign-sent-time"

                    self.resign_received_time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self._children_name_map["resign_received_time"] = "resign-received-time"

                    self.ipv6_operational_address = YList(self)
                    self.ipv6_configured_down_address = YList(self)
                    self.track_item_info = YList(self)
                    self.state_change_history = YList(self)
                    self._segment_path = lambda: "virtual-router" + "[interface-name='" + str(self.interface_name) + "']" + "[virtual-router-id='" + str(self.virtual_router_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/virtual-routers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Ipv6.VirtualRouters.VirtualRouter, ['interface_name', 'virtual_router_id', u'interface_name_xr', u'virtual_router_id_xr', u'version', u'address_family', u'session_name', u'slaves', u'is_slave', u'followed_session_name', u'secondary_address_count', u'operational_address_count', u'primary_virtual_ip', u'configured_down_address_count', u'virtual_linklocal_ipv6_address', u'primary_state', u'master_ip_address', u'master_ipv6_address', u'master_priority', u'vrrp_state', u'authentication_type', u'authentication_string', u'configured_advertize_time', u'oper_advertize_time', u'min_delay_time', u'reload_delay_time', u'delay_timer_flag', u'delay_timer_secs', u'delay_timer_msecs', u'authentication_flag', u'force_timer_flag', u'preempt_flag', u'ip_address_owner_flag', u'is_accept_mode', u'preempt_delay_time', u'configured_priority', u'operational_priority', u'priority_decrement', u'tracked_interface_count', u'tracked_interface_up_count', u'tracked_item_count', u'tracked_item_up_count', u'time_in_current_state', u'state_change_count', u'time_vrouter_up', u'master_count', u'adverts_received_count', u'advert_interval_error_count', u'adverts_sent_count', u'authentication_fail_count', u'ttl_error_count', u'priority_zero_received_count', u'priority_zero_sent_count', u'invalid_packet_count', u'address_list_error_count', u'invalid_auth_type_count', u'auth_type_mismatch_count', u'pkt_length_errors_count', u'time_stats_discontinuity', u'bfd_session_state', u'bfd_interval', u'bfd_multiplier', u'bfd_cfg_remote_ip', u'bfd_configured_remote_ipv6_address', u'state_from_checkpoint', u'interface_ipv4_address', u'interface_ipv6_address', u'virtual_mac_address', u'virtual_mac_address_state', u'operational_address', u'ipv4_configured_down_address'], name, value)


                class ResignSentTime(Entity):
                    """
                    Time last resign was sent
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime, self).__init__()

                        self.yang_name = "resign-sent-time"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                            ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                        ])
                        self.seconds = None
                        self.nanoseconds = None
                        self._segment_path = lambda: "resign-sent-time"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime, [u'seconds', u'nanoseconds'], name, value)


                class ResignReceivedTime(Entity):
                    """
                    Time last resign was received
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime, self).__init__()

                        self.yang_name = "resign-received-time"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                            ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                        ])
                        self.seconds = None
                        self.nanoseconds = None
                        self._segment_path = lambda: "resign-received-time"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime, [u'seconds', u'nanoseconds'], name, value)


                class Ipv6OperationalAddress(Entity):
                    """
                    IPv6 Operational VRRP addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress, self).__init__()

                        self.yang_name = "ipv6-operational-address"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                        ])
                        self.ipv6_address = None
                        self._segment_path = lambda: "ipv6-operational-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress, [u'ipv6_address'], name, value)


                class Ipv6ConfiguredDownAddress(Entity):
                    """
                    IPv6 Configured but Down VRRP addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress, self).__init__()

                        self.yang_name = "ipv6-configured-down-address"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                        ])
                        self.ipv6_address = None
                        self._segment_path = lambda: "ipv6-configured-down-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress, [u'ipv6_address'], name, value)


                class TrackItemInfo(Entity):
                    """
                    Track Item Info
                    
                    .. attribute:: interface
                    
                    	IM Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: virtual_router_id_xr
                    
                    	Virtual Router ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tracked_item_type
                    
                    	Type of tracked item
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: tracked_item_index
                    
                    	Tracked item index
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: state
                    
                    	State of the tracked item
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: priority
                    
                    	Priority weight of item
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.TrackItemInfo, self).__init__()

                        self.yang_name = "track-item-info"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('virtual_router_id_xr', (YLeaf(YType.uint32, 'virtual-router-id-xr'), ['int'])),
                            ('tracked_item_type', (YLeaf(YType.uint16, 'tracked-item-type'), ['int'])),
                            ('tracked_item_index', (YLeaf(YType.str, 'tracked-item-index'), ['str'])),
                            ('state', (YLeaf(YType.uint8, 'state'), ['int'])),
                            ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                        ])
                        self.interface = None
                        self.virtual_router_id_xr = None
                        self.tracked_item_type = None
                        self.tracked_item_index = None
                        self.state = None
                        self.priority = None
                        self._segment_path = lambda: "track-item-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv6.VirtualRouters.VirtualRouter.TrackItemInfo, [u'interface', u'virtual_router_id_xr', u'tracked_item_type', u'tracked_item_index', u'state', u'priority'], name, value)


                class StateChangeHistory(Entity):
                    """
                    State change history
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:  :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:  :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                    
                    .. attribute:: new_state
                    
                    	New State
                    	**type**\:  :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:  :py:class:`VrrpStateChangeReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpStateChangeReason>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory, self).__init__()

                        self.yang_name = "state-change-history"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("time", ("time", Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time))])
                        self._leafs = OrderedDict([
                            ('old_state', (YLeaf(YType.enumeration, 'old-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolState', '')])),
                            ('new_state', (YLeaf(YType.enumeration, 'new-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolState', '')])),
                            ('reason', (YLeaf(YType.enumeration, 'reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpStateChangeReason', '')])),
                        ])
                        self.old_state = None
                        self.new_state = None
                        self.reason = None

                        self.time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time()
                        self.time.parent = self
                        self._children_name_map["time"] = "time"
                        self._segment_path = lambda: "state-change-history"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory, [u'old_state', u'new_state', u'reason'], name, value)


                    class Time(Entity):
                        """
                        Time of state change
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time, self).__init__()

                            self.yang_name = "time"
                            self.yang_parent_name = "state-change-history"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                            ])
                            self.seconds = None
                            self.nanoseconds = None
                            self._segment_path = lambda: "time"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time, [u'seconds', u'nanoseconds'], name, value)


        class Interfaces(Entity):
            """
            The VRRP interface table
            
            .. attribute:: interface
            
            	A VRRP interface entry
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vrrp.Ipv6.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", Vrrp.Ipv6.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrrp.Ipv6.Interfaces, [], name, value)


            class Interface(Entity):
                """
                A VRRP interface entry
                
                .. attribute:: interface_name  (key)
                
                	The name of the interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: invalid_checksum_count
                
                	Invalid checksum
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_version_count
                
                	Unknown/unsupported version
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_vrid_count
                
                	Invalid vrID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_packet_length_count
                
                	Bad packet lengths
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vrrp.Ipv6.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('invalid_checksum_count', (YLeaf(YType.uint32, 'invalid-checksum-count'), ['int'])),
                        ('invalid_version_count', (YLeaf(YType.uint32, 'invalid-version-count'), ['int'])),
                        ('invalid_vrid_count', (YLeaf(YType.uint32, 'invalid-vrid-count'), ['int'])),
                        ('invalid_packet_length_count', (YLeaf(YType.uint32, 'invalid-packet-length-count'), ['int'])),
                    ])
                    self.interface_name = None
                    self.interface = None
                    self.invalid_checksum_count = None
                    self.invalid_version_count = None
                    self.invalid_vrid_count = None
                    self.invalid_packet_length_count = None
                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Ipv6.Interfaces.Interface, ['interface_name', u'interface', u'invalid_checksum_count', u'invalid_version_count', u'invalid_vrid_count', u'invalid_packet_length_count'], name, value)


    class Ipv4(Entity):
        """
        IPv4 VRRP configuration
        
        .. attribute:: interfaces
        
        	The VRRP interface table
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.Interfaces>`
        
        .. attribute:: track_items
        
        	The VRRP tracked item table
        	**type**\:  :py:class:`TrackItems <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.TrackItems>`
        
        .. attribute:: virtual_routers
        
        	The VRRP virtual router table
        	**type**\:  :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters>`
        
        

        """

        _prefix = 'ipv4-vrrp-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vrrp.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "vrrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interfaces", ("interfaces", Vrrp.Ipv4.Interfaces)), ("track-items", ("track_items", Vrrp.Ipv4.TrackItems)), ("virtual-routers", ("virtual_routers", Vrrp.Ipv4.VirtualRouters))])
            self._leafs = OrderedDict()

            self.interfaces = Vrrp.Ipv4.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"

            self.track_items = Vrrp.Ipv4.TrackItems()
            self.track_items.parent = self
            self._children_name_map["track_items"] = "track-items"

            self.virtual_routers = Vrrp.Ipv4.VirtualRouters()
            self.virtual_routers.parent = self
            self._children_name_map["virtual_routers"] = "virtual-routers"
            self._segment_path = lambda: "ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vrrp.Ipv4, [], name, value)


        class Interfaces(Entity):
            """
            The VRRP interface table
            
            .. attribute:: interface
            
            	A VRRP interface entry
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vrrp.Ipv4.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", Vrrp.Ipv4.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrrp.Ipv4.Interfaces, [], name, value)


            class Interface(Entity):
                """
                A VRRP interface entry
                
                .. attribute:: interface_name  (key)
                
                	The name of the interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: invalid_checksum_count
                
                	Invalid checksum
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_version_count
                
                	Unknown/unsupported version
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_vrid_count
                
                	Invalid vrID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_packet_length_count
                
                	Bad packet lengths
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vrrp.Ipv4.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('invalid_checksum_count', (YLeaf(YType.uint32, 'invalid-checksum-count'), ['int'])),
                        ('invalid_version_count', (YLeaf(YType.uint32, 'invalid-version-count'), ['int'])),
                        ('invalid_vrid_count', (YLeaf(YType.uint32, 'invalid-vrid-count'), ['int'])),
                        ('invalid_packet_length_count', (YLeaf(YType.uint32, 'invalid-packet-length-count'), ['int'])),
                    ])
                    self.interface_name = None
                    self.interface = None
                    self.invalid_checksum_count = None
                    self.invalid_version_count = None
                    self.invalid_vrid_count = None
                    self.invalid_packet_length_count = None
                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Ipv4.Interfaces.Interface, ['interface_name', u'interface', u'invalid_checksum_count', u'invalid_version_count', u'invalid_vrid_count', u'invalid_packet_length_count'], name, value)


        class TrackItems(Entity):
            """
            The VRRP tracked item table
            
            .. attribute:: track_item
            
            	A configured VRRP IP address entry
            	**type**\: list of  		 :py:class:`TrackItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.TrackItems.TrackItem>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vrrp.Ipv4.TrackItems, self).__init__()

                self.yang_name = "track-items"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("track-item", ("track_item", Vrrp.Ipv4.TrackItems.TrackItem))])
                self._leafs = OrderedDict()

                self.track_item = YList(self)
                self._segment_path = lambda: "track-items"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrrp.Ipv4.TrackItems, [], name, value)


            class TrackItem(Entity):
                """
                A configured VRRP IP address entry
                
                .. attribute:: interface_name  (key)
                
                	The interface name to track
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: virtual_router_id  (key)
                
                	The VRRP virtual router id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_name  (key)
                
                	The name of the tracked interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: virtual_router_id_xr
                
                	Virtual Router ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_item_type
                
                	Type of tracked item
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: tracked_item_index
                
                	Tracked item index
                	**type**\: str
                
                	**length:** 0..32
                
                .. attribute:: state
                
                	State of the tracked item
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: priority
                
                	Priority weight of item
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vrrp.Ipv4.TrackItems.TrackItem, self).__init__()

                    self.yang_name = "track-item"
                    self.yang_parent_name = "track-items"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name','virtual_router_id','tracked_interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('virtual_router_id', (YLeaf(YType.uint32, 'virtual-router-id'), ['int'])),
                        ('tracked_interface_name', (YLeaf(YType.str, 'tracked-interface-name'), ['str'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('virtual_router_id_xr', (YLeaf(YType.uint32, 'virtual-router-id-xr'), ['int'])),
                        ('tracked_item_type', (YLeaf(YType.uint16, 'tracked-item-type'), ['int'])),
                        ('tracked_item_index', (YLeaf(YType.str, 'tracked-item-index'), ['str'])),
                        ('state', (YLeaf(YType.uint8, 'state'), ['int'])),
                        ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                    ])
                    self.interface_name = None
                    self.virtual_router_id = None
                    self.tracked_interface_name = None
                    self.interface = None
                    self.virtual_router_id_xr = None
                    self.tracked_item_type = None
                    self.tracked_item_index = None
                    self.state = None
                    self.priority = None
                    self._segment_path = lambda: "track-item" + "[interface-name='" + str(self.interface_name) + "']" + "[virtual-router-id='" + str(self.virtual_router_id) + "']" + "[tracked-interface-name='" + str(self.tracked_interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/track-items/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Ipv4.TrackItems.TrackItem, ['interface_name', 'virtual_router_id', 'tracked_interface_name', u'interface', u'virtual_router_id_xr', u'tracked_item_type', u'tracked_item_index', u'state', u'priority'], name, value)


        class VirtualRouters(Entity):
            """
            The VRRP virtual router table
            
            .. attribute:: virtual_router
            
            	A VRRP virtual router
            	**type**\: list of  		 :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vrrp.Ipv4.VirtualRouters, self).__init__()

                self.yang_name = "virtual-routers"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("virtual-router", ("virtual_router", Vrrp.Ipv4.VirtualRouters.VirtualRouter))])
                self._leafs = OrderedDict()

                self.virtual_router = YList(self)
                self._segment_path = lambda: "virtual-routers"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrrp.Ipv4.VirtualRouters, [], name, value)


            class VirtualRouter(Entity):
                """
                A VRRP virtual router
                
                .. attribute:: interface_name  (key)
                
                	The name of the interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: virtual_router_id  (key)
                
                	The VRRP virtual router id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: resign_sent_time
                
                	Time last resign was sent
                	**type**\:  :py:class:`ResignSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime>`
                
                .. attribute:: resign_received_time
                
                	Time last resign was received
                	**type**\:  :py:class:`ResignReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime>`
                
                .. attribute:: interface_name_xr
                
                	IM Interface Name
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: virtual_router_id_xr
                
                	Virtual Router ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: version
                
                	VRRP Protocol Version
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:  :py:class:`VrrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBAf>`
                
                .. attribute:: session_name
                
                	Session Name
                	**type**\: str
                
                	**length:** 0..16
                
                .. attribute:: slaves
                
                	Number of slaves following state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_slave
                
                	Group is a slave group
                	**type**\: bool
                
                .. attribute:: followed_session_name
                
                	Followed Session Name
                	**type**\: str
                
                	**length:** 0..16
                
                .. attribute:: secondary_address_count
                
                	Configured VRRP secondary address count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: operational_address_count
                
                	Operational VRRP address count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: primary_virtual_ip
                
                	Configured IPv4 Primary address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: configured_down_address_count
                
                	 Configured but Down VRRP address count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: virtual_linklocal_ipv6_address
                
                	Virtual linklocal IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: primary_state
                
                	State of primary IP address
                	**type**\:  :py:class:`VrrpVipState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVipState>`
                
                .. attribute:: master_ip_address
                
                	Master router real IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: master_ipv6_address
                
                	Master router real IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: master_priority
                
                	Master router priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: vrrp_state
                
                	VRRP state
                	**type**\:  :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                
                .. attribute:: authentication_type
                
                	Authentication type
                	**type**\:  :py:class:`VrrpProtAuth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpProtAuth>`
                
                .. attribute:: authentication_string
                
                	Authentication data
                	**type**\: str
                
                .. attribute:: configured_advertize_time
                
                	Configured advertize time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: oper_advertize_time
                
                	Operational advertize time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: min_delay_time
                
                	Minimum delay time in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: reload_delay_time
                
                	Reload delay time in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: delay_timer_flag
                
                	Delay timer running flag
                	**type**\: bool
                
                .. attribute:: delay_timer_secs
                
                	Delay timer running time secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: delay_timer_msecs
                
                	Delay timer running time msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: authentication_flag
                
                	Text authentication configured flag
                	**type**\: bool
                
                .. attribute:: force_timer_flag
                
                	Configured timers forced flag
                	**type**\: bool
                
                .. attribute:: preempt_flag
                
                	Preempt configured flag
                	**type**\: bool
                
                .. attribute:: ip_address_owner_flag
                
                	IP address owner flag
                	**type**\: bool
                
                .. attribute:: is_accept_mode
                
                	Is accept mode
                	**type**\: bool
                
                .. attribute:: preempt_delay_time
                
                	Preempt delay time
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: configured_priority
                
                	Configured priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: operational_priority
                
                	Operational priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: priority_decrement
                
                	Priority decrement
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_count
                
                	Number of items tracked
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_up_count
                
                	Number of tracked items up
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_item_count
                
                	Number of tracked items
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_item_up_count
                
                	Number of tracked items in UP state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: time_in_current_state
                
                	Time in current state secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: state_change_count
                
                	Number of state changes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: time_vrouter_up
                
                	Time vrouter is up in centiseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: centisecond
                
                .. attribute:: master_count
                
                	No. of times become Master
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: adverts_received_count
                
                	No. of advertisements received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: advert_interval_error_count
                
                	Advertise interval errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: adverts_sent_count
                
                	No. of advertisements sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_fail_count
                
                	Authentication failures
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ttl_error_count
                
                	TTL errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority_zero_received_count
                
                	No. priority 0 received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority_zero_sent_count
                
                	No. priority 0 sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_packet_count
                
                	Invalid packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: address_list_error_count
                
                	Address list errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_auth_type_count
                
                	Invalid authentication type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: auth_type_mismatch_count
                
                	Authentication type mismatches
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_length_errors_count
                
                	Packet length errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: time_stats_discontinuity
                
                	Time since a statistics discontinuity in ticks (10ns units)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_session_state
                
                	BFD session state
                	**type**\:  :py:class:`VrrpBfdSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBfdSessionState>`
                
                .. attribute:: bfd_interval
                
                	BFD packet send interval
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_multiplier
                
                	BFD multiplier
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_cfg_remote_ip
                
                	BFD configured remote IP
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_configured_remote_ipv6_address
                
                	BFD configured remote IPv6
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: state_from_checkpoint
                
                	Whether state recovered from checkpoint
                	**type**\: bool
                
                .. attribute:: interface_ipv4_address
                
                	The Interface Primary IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: interface_ipv6_address
                
                	The Interface linklocal IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtual_mac_address
                
                	Virtual mac address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: virtual_mac_address_state
                
                	Virtual mac address state
                	**type**\:  :py:class:`VrrpVmacState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVmacState>`
                
                .. attribute:: operational_address
                
                	Operational IPv4 VRRP addresses
                	**type**\: list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4_configured_down_address
                
                	IPv4 Configured but Down VRRP addresses
                	**type**\: list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_operational_address
                
                	IPv6 Operational VRRP addresses
                	**type**\: list of  		 :py:class:`Ipv6OperationalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress>`
                
                .. attribute:: ipv6_configured_down_address
                
                	IPv6 Configured but Down VRRP addresses
                	**type**\: list of  		 :py:class:`Ipv6ConfiguredDownAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress>`
                
                .. attribute:: track_item_info
                
                	Track Item Info
                	**type**\: list of  		 :py:class:`TrackItemInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.TrackItemInfo>`
                
                .. attribute:: state_change_history
                
                	State change history
                	**type**\: list of  		 :py:class:`StateChangeHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory>`
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vrrp.Ipv4.VirtualRouters.VirtualRouter, self).__init__()

                    self.yang_name = "virtual-router"
                    self.yang_parent_name = "virtual-routers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name','virtual_router_id']
                    self._child_classes = OrderedDict([("resign-sent-time", ("resign_sent_time", Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime)), ("resign-received-time", ("resign_received_time", Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime)), ("ipv6-operational-address", ("ipv6_operational_address", Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress)), ("ipv6-configured-down-address", ("ipv6_configured_down_address", Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress)), ("track-item-info", ("track_item_info", Vrrp.Ipv4.VirtualRouters.VirtualRouter.TrackItemInfo)), ("state-change-history", ("state_change_history", Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory))])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('virtual_router_id', (YLeaf(YType.uint32, 'virtual-router-id'), ['int'])),
                        ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                        ('virtual_router_id_xr', (YLeaf(YType.uint32, 'virtual-router-id-xr'), ['int'])),
                        ('version', (YLeaf(YType.uint8, 'version'), ['int'])),
                        ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBAf', '')])),
                        ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                        ('slaves', (YLeaf(YType.uint32, 'slaves'), ['int'])),
                        ('is_slave', (YLeaf(YType.boolean, 'is-slave'), ['bool'])),
                        ('followed_session_name', (YLeaf(YType.str, 'followed-session-name'), ['str'])),
                        ('secondary_address_count', (YLeaf(YType.uint8, 'secondary-address-count'), ['int'])),
                        ('operational_address_count', (YLeaf(YType.uint8, 'operational-address-count'), ['int'])),
                        ('primary_virtual_ip', (YLeaf(YType.str, 'primary-virtual-ip'), ['str'])),
                        ('configured_down_address_count', (YLeaf(YType.uint8, 'configured-down-address-count'), ['int'])),
                        ('virtual_linklocal_ipv6_address', (YLeaf(YType.str, 'virtual-linklocal-ipv6-address'), ['str'])),
                        ('primary_state', (YLeaf(YType.enumeration, 'primary-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpVipState', '')])),
                        ('master_ip_address', (YLeaf(YType.str, 'master-ip-address'), ['str'])),
                        ('master_ipv6_address', (YLeaf(YType.str, 'master-ipv6-address'), ['str'])),
                        ('master_priority', (YLeaf(YType.uint8, 'master-priority'), ['int'])),
                        ('vrrp_state', (YLeaf(YType.enumeration, 'vrrp-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolState', '')])),
                        ('authentication_type', (YLeaf(YType.enumeration, 'authentication-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpProtAuth', '')])),
                        ('authentication_string', (YLeaf(YType.str, 'authentication-string'), ['str'])),
                        ('configured_advertize_time', (YLeaf(YType.uint32, 'configured-advertize-time'), ['int'])),
                        ('oper_advertize_time', (YLeaf(YType.uint32, 'oper-advertize-time'), ['int'])),
                        ('min_delay_time', (YLeaf(YType.uint32, 'min-delay-time'), ['int'])),
                        ('reload_delay_time', (YLeaf(YType.uint32, 'reload-delay-time'), ['int'])),
                        ('delay_timer_flag', (YLeaf(YType.boolean, 'delay-timer-flag'), ['bool'])),
                        ('delay_timer_secs', (YLeaf(YType.uint32, 'delay-timer-secs'), ['int'])),
                        ('delay_timer_msecs', (YLeaf(YType.uint32, 'delay-timer-msecs'), ['int'])),
                        ('authentication_flag', (YLeaf(YType.boolean, 'authentication-flag'), ['bool'])),
                        ('force_timer_flag', (YLeaf(YType.boolean, 'force-timer-flag'), ['bool'])),
                        ('preempt_flag', (YLeaf(YType.boolean, 'preempt-flag'), ['bool'])),
                        ('ip_address_owner_flag', (YLeaf(YType.boolean, 'ip-address-owner-flag'), ['bool'])),
                        ('is_accept_mode', (YLeaf(YType.boolean, 'is-accept-mode'), ['bool'])),
                        ('preempt_delay_time', (YLeaf(YType.uint16, 'preempt-delay-time'), ['int'])),
                        ('configured_priority', (YLeaf(YType.uint8, 'configured-priority'), ['int'])),
                        ('operational_priority', (YLeaf(YType.uint8, 'operational-priority'), ['int'])),
                        ('priority_decrement', (YLeaf(YType.uint32, 'priority-decrement'), ['int'])),
                        ('tracked_interface_count', (YLeaf(YType.uint32, 'tracked-interface-count'), ['int'])),
                        ('tracked_interface_up_count', (YLeaf(YType.uint32, 'tracked-interface-up-count'), ['int'])),
                        ('tracked_item_count', (YLeaf(YType.uint32, 'tracked-item-count'), ['int'])),
                        ('tracked_item_up_count', (YLeaf(YType.uint32, 'tracked-item-up-count'), ['int'])),
                        ('time_in_current_state', (YLeaf(YType.uint32, 'time-in-current-state'), ['int'])),
                        ('state_change_count', (YLeaf(YType.uint32, 'state-change-count'), ['int'])),
                        ('time_vrouter_up', (YLeaf(YType.uint32, 'time-vrouter-up'), ['int'])),
                        ('master_count', (YLeaf(YType.uint32, 'master-count'), ['int'])),
                        ('adverts_received_count', (YLeaf(YType.uint32, 'adverts-received-count'), ['int'])),
                        ('advert_interval_error_count', (YLeaf(YType.uint32, 'advert-interval-error-count'), ['int'])),
                        ('adverts_sent_count', (YLeaf(YType.uint32, 'adverts-sent-count'), ['int'])),
                        ('authentication_fail_count', (YLeaf(YType.uint32, 'authentication-fail-count'), ['int'])),
                        ('ttl_error_count', (YLeaf(YType.uint32, 'ttl-error-count'), ['int'])),
                        ('priority_zero_received_count', (YLeaf(YType.uint32, 'priority-zero-received-count'), ['int'])),
                        ('priority_zero_sent_count', (YLeaf(YType.uint32, 'priority-zero-sent-count'), ['int'])),
                        ('invalid_packet_count', (YLeaf(YType.uint32, 'invalid-packet-count'), ['int'])),
                        ('address_list_error_count', (YLeaf(YType.uint32, 'address-list-error-count'), ['int'])),
                        ('invalid_auth_type_count', (YLeaf(YType.uint32, 'invalid-auth-type-count'), ['int'])),
                        ('auth_type_mismatch_count', (YLeaf(YType.uint32, 'auth-type-mismatch-count'), ['int'])),
                        ('pkt_length_errors_count', (YLeaf(YType.uint32, 'pkt-length-errors-count'), ['int'])),
                        ('time_stats_discontinuity', (YLeaf(YType.uint32, 'time-stats-discontinuity'), ['int'])),
                        ('bfd_session_state', (YLeaf(YType.enumeration, 'bfd-session-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBfdSessionState', '')])),
                        ('bfd_interval', (YLeaf(YType.uint32, 'bfd-interval'), ['int'])),
                        ('bfd_multiplier', (YLeaf(YType.uint32, 'bfd-multiplier'), ['int'])),
                        ('bfd_cfg_remote_ip', (YLeaf(YType.str, 'bfd-cfg-remote-ip'), ['str'])),
                        ('bfd_configured_remote_ipv6_address', (YLeaf(YType.str, 'bfd-configured-remote-ipv6-address'), ['str'])),
                        ('state_from_checkpoint', (YLeaf(YType.boolean, 'state-from-checkpoint'), ['bool'])),
                        ('interface_ipv4_address', (YLeaf(YType.str, 'interface-ipv4-address'), ['str'])),
                        ('interface_ipv6_address', (YLeaf(YType.str, 'interface-ipv6-address'), ['str'])),
                        ('virtual_mac_address', (YLeaf(YType.str, 'virtual-mac-address'), ['str'])),
                        ('virtual_mac_address_state', (YLeaf(YType.enumeration, 'virtual-mac-address-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpVmacState', '')])),
                        ('operational_address', (YLeafList(YType.str, 'operational-address'), ['str'])),
                        ('ipv4_configured_down_address', (YLeafList(YType.str, 'ipv4-configured-down-address'), ['str'])),
                    ])
                    self.interface_name = None
                    self.virtual_router_id = None
                    self.interface_name_xr = None
                    self.virtual_router_id_xr = None
                    self.version = None
                    self.address_family = None
                    self.session_name = None
                    self.slaves = None
                    self.is_slave = None
                    self.followed_session_name = None
                    self.secondary_address_count = None
                    self.operational_address_count = None
                    self.primary_virtual_ip = None
                    self.configured_down_address_count = None
                    self.virtual_linklocal_ipv6_address = None
                    self.primary_state = None
                    self.master_ip_address = None
                    self.master_ipv6_address = None
                    self.master_priority = None
                    self.vrrp_state = None
                    self.authentication_type = None
                    self.authentication_string = None
                    self.configured_advertize_time = None
                    self.oper_advertize_time = None
                    self.min_delay_time = None
                    self.reload_delay_time = None
                    self.delay_timer_flag = None
                    self.delay_timer_secs = None
                    self.delay_timer_msecs = None
                    self.authentication_flag = None
                    self.force_timer_flag = None
                    self.preempt_flag = None
                    self.ip_address_owner_flag = None
                    self.is_accept_mode = None
                    self.preempt_delay_time = None
                    self.configured_priority = None
                    self.operational_priority = None
                    self.priority_decrement = None
                    self.tracked_interface_count = None
                    self.tracked_interface_up_count = None
                    self.tracked_item_count = None
                    self.tracked_item_up_count = None
                    self.time_in_current_state = None
                    self.state_change_count = None
                    self.time_vrouter_up = None
                    self.master_count = None
                    self.adverts_received_count = None
                    self.advert_interval_error_count = None
                    self.adverts_sent_count = None
                    self.authentication_fail_count = None
                    self.ttl_error_count = None
                    self.priority_zero_received_count = None
                    self.priority_zero_sent_count = None
                    self.invalid_packet_count = None
                    self.address_list_error_count = None
                    self.invalid_auth_type_count = None
                    self.auth_type_mismatch_count = None
                    self.pkt_length_errors_count = None
                    self.time_stats_discontinuity = None
                    self.bfd_session_state = None
                    self.bfd_interval = None
                    self.bfd_multiplier = None
                    self.bfd_cfg_remote_ip = None
                    self.bfd_configured_remote_ipv6_address = None
                    self.state_from_checkpoint = None
                    self.interface_ipv4_address = None
                    self.interface_ipv6_address = None
                    self.virtual_mac_address = None
                    self.virtual_mac_address_state = None
                    self.operational_address = []
                    self.ipv4_configured_down_address = []

                    self.resign_sent_time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self._children_name_map["resign_sent_time"] = "resign-sent-time"

                    self.resign_received_time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self._children_name_map["resign_received_time"] = "resign-received-time"

                    self.ipv6_operational_address = YList(self)
                    self.ipv6_configured_down_address = YList(self)
                    self.track_item_info = YList(self)
                    self.state_change_history = YList(self)
                    self._segment_path = lambda: "virtual-router" + "[interface-name='" + str(self.interface_name) + "']" + "[virtual-router-id='" + str(self.virtual_router_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/virtual-routers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Ipv4.VirtualRouters.VirtualRouter, ['interface_name', 'virtual_router_id', u'interface_name_xr', u'virtual_router_id_xr', u'version', u'address_family', u'session_name', u'slaves', u'is_slave', u'followed_session_name', u'secondary_address_count', u'operational_address_count', u'primary_virtual_ip', u'configured_down_address_count', u'virtual_linklocal_ipv6_address', u'primary_state', u'master_ip_address', u'master_ipv6_address', u'master_priority', u'vrrp_state', u'authentication_type', u'authentication_string', u'configured_advertize_time', u'oper_advertize_time', u'min_delay_time', u'reload_delay_time', u'delay_timer_flag', u'delay_timer_secs', u'delay_timer_msecs', u'authentication_flag', u'force_timer_flag', u'preempt_flag', u'ip_address_owner_flag', u'is_accept_mode', u'preempt_delay_time', u'configured_priority', u'operational_priority', u'priority_decrement', u'tracked_interface_count', u'tracked_interface_up_count', u'tracked_item_count', u'tracked_item_up_count', u'time_in_current_state', u'state_change_count', u'time_vrouter_up', u'master_count', u'adverts_received_count', u'advert_interval_error_count', u'adverts_sent_count', u'authentication_fail_count', u'ttl_error_count', u'priority_zero_received_count', u'priority_zero_sent_count', u'invalid_packet_count', u'address_list_error_count', u'invalid_auth_type_count', u'auth_type_mismatch_count', u'pkt_length_errors_count', u'time_stats_discontinuity', u'bfd_session_state', u'bfd_interval', u'bfd_multiplier', u'bfd_cfg_remote_ip', u'bfd_configured_remote_ipv6_address', u'state_from_checkpoint', u'interface_ipv4_address', u'interface_ipv6_address', u'virtual_mac_address', u'virtual_mac_address_state', u'operational_address', u'ipv4_configured_down_address'], name, value)


                class ResignSentTime(Entity):
                    """
                    Time last resign was sent
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime, self).__init__()

                        self.yang_name = "resign-sent-time"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                            ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                        ])
                        self.seconds = None
                        self.nanoseconds = None
                        self._segment_path = lambda: "resign-sent-time"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime, [u'seconds', u'nanoseconds'], name, value)


                class ResignReceivedTime(Entity):
                    """
                    Time last resign was received
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime, self).__init__()

                        self.yang_name = "resign-received-time"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                            ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                        ])
                        self.seconds = None
                        self.nanoseconds = None
                        self._segment_path = lambda: "resign-received-time"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime, [u'seconds', u'nanoseconds'], name, value)


                class Ipv6OperationalAddress(Entity):
                    """
                    IPv6 Operational VRRP addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress, self).__init__()

                        self.yang_name = "ipv6-operational-address"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                        ])
                        self.ipv6_address = None
                        self._segment_path = lambda: "ipv6-operational-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress, [u'ipv6_address'], name, value)


                class Ipv6ConfiguredDownAddress(Entity):
                    """
                    IPv6 Configured but Down VRRP addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress, self).__init__()

                        self.yang_name = "ipv6-configured-down-address"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                        ])
                        self.ipv6_address = None
                        self._segment_path = lambda: "ipv6-configured-down-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress, [u'ipv6_address'], name, value)


                class TrackItemInfo(Entity):
                    """
                    Track Item Info
                    
                    .. attribute:: interface
                    
                    	IM Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: virtual_router_id_xr
                    
                    	Virtual Router ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tracked_item_type
                    
                    	Type of tracked item
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: tracked_item_index
                    
                    	Tracked item index
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: state
                    
                    	State of the tracked item
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: priority
                    
                    	Priority weight of item
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.TrackItemInfo, self).__init__()

                        self.yang_name = "track-item-info"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('virtual_router_id_xr', (YLeaf(YType.uint32, 'virtual-router-id-xr'), ['int'])),
                            ('tracked_item_type', (YLeaf(YType.uint16, 'tracked-item-type'), ['int'])),
                            ('tracked_item_index', (YLeaf(YType.str, 'tracked-item-index'), ['str'])),
                            ('state', (YLeaf(YType.uint8, 'state'), ['int'])),
                            ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                        ])
                        self.interface = None
                        self.virtual_router_id_xr = None
                        self.tracked_item_type = None
                        self.tracked_item_index = None
                        self.state = None
                        self.priority = None
                        self._segment_path = lambda: "track-item-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv4.VirtualRouters.VirtualRouter.TrackItemInfo, [u'interface', u'virtual_router_id_xr', u'tracked_item_type', u'tracked_item_index', u'state', u'priority'], name, value)


                class StateChangeHistory(Entity):
                    """
                    State change history
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:  :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:  :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                    
                    .. attribute:: new_state
                    
                    	New State
                    	**type**\:  :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:  :py:class:`VrrpStateChangeReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpStateChangeReason>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory, self).__init__()

                        self.yang_name = "state-change-history"
                        self.yang_parent_name = "virtual-router"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("time", ("time", Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time))])
                        self._leafs = OrderedDict([
                            ('old_state', (YLeaf(YType.enumeration, 'old-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolState', '')])),
                            ('new_state', (YLeaf(YType.enumeration, 'new-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolState', '')])),
                            ('reason', (YLeaf(YType.enumeration, 'reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpStateChangeReason', '')])),
                        ])
                        self.old_state = None
                        self.new_state = None
                        self.reason = None

                        self.time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time()
                        self.time.parent = self
                        self._children_name_map["time"] = "time"
                        self._segment_path = lambda: "state-change-history"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory, [u'old_state', u'new_state', u'reason'], name, value)


                    class Time(Entity):
                        """
                        Time of state change
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time, self).__init__()

                            self.yang_name = "time"
                            self.yang_parent_name = "state-change-history"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                            ])
                            self.seconds = None
                            self.nanoseconds = None
                            self._segment_path = lambda: "time"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time, [u'seconds', u'nanoseconds'], name, value)


    class MgoSessions(Entity):
        """
        VRRP MGO Session information
        
        .. attribute:: mgo_session
        
        	A VRRP MGO Session
        	**type**\: list of  		 :py:class:`MgoSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.MgoSessions.MgoSession>`
        
        

        """

        _prefix = 'ipv4-vrrp-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vrrp.MgoSessions, self).__init__()

            self.yang_name = "mgo-sessions"
            self.yang_parent_name = "vrrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mgo-session", ("mgo_session", Vrrp.MgoSessions.MgoSession))])
            self._leafs = OrderedDict()

            self.mgo_session = YList(self)
            self._segment_path = lambda: "mgo-sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vrrp.MgoSessions, [], name, value)


        class MgoSession(Entity):
            """
            A VRRP MGO Session
            
            .. attribute:: session_name  (key)
            
            	The name of the session
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: primary_session_name
            
            	Session Name
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: primary_session_interface
            
            	Interface of primary session
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: primary_af_name
            
            	Address family of primary session
            	**type**\:  :py:class:`VrrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBAf>`
            
            .. attribute:: primary_session_number
            
            	VRID of primary session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: primary_session_state
            
            	State of primary session
            	**type**\:  :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
            
            .. attribute:: slave
            
            	List of slaves following this primary session
            	**type**\: list of  		 :py:class:`Slave <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.MgoSessions.MgoSession.Slave>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vrrp.MgoSessions.MgoSession, self).__init__()

                self.yang_name = "mgo-session"
                self.yang_parent_name = "mgo-sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['session_name']
                self._child_classes = OrderedDict([("slave", ("slave", Vrrp.MgoSessions.MgoSession.Slave))])
                self._leafs = OrderedDict([
                    ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                    ('primary_session_name', (YLeaf(YType.str, 'primary-session-name'), ['str'])),
                    ('primary_session_interface', (YLeaf(YType.str, 'primary-session-interface'), ['str'])),
                    ('primary_af_name', (YLeaf(YType.enumeration, 'primary-af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBAf', '')])),
                    ('primary_session_number', (YLeaf(YType.uint32, 'primary-session-number'), ['int'])),
                    ('primary_session_state', (YLeaf(YType.enumeration, 'primary-session-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolState', '')])),
                ])
                self.session_name = None
                self.primary_session_name = None
                self.primary_session_interface = None
                self.primary_af_name = None
                self.primary_session_number = None
                self.primary_session_state = None

                self.slave = YList(self)
                self._segment_path = lambda: "mgo-session" + "[session-name='" + str(self.session_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/mgo-sessions/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrrp.MgoSessions.MgoSession, ['session_name', u'primary_session_name', u'primary_session_interface', u'primary_af_name', u'primary_session_number', u'primary_session_state'], name, value)


            class Slave(Entity):
                """
                List of slaves following this primary session
                
                .. attribute:: slave_interface
                
                	Interface of slave
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: slave_virtual_router_id
                
                	VRID of slave
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vrrp.MgoSessions.MgoSession.Slave, self).__init__()

                    self.yang_name = "slave"
                    self.yang_parent_name = "mgo-session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('slave_interface', (YLeaf(YType.str, 'slave-interface'), ['str'])),
                        ('slave_virtual_router_id', (YLeaf(YType.uint32, 'slave-virtual-router-id'), ['int'])),
                    ])
                    self.slave_interface = None
                    self.slave_virtual_router_id = None
                    self._segment_path = lambda: "slave"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.MgoSessions.MgoSession.Slave, [u'slave_interface', u'slave_virtual_router_id'], name, value)

    def clone_ptr(self):
        self._top_entity = Vrrp()
        return self._top_entity

