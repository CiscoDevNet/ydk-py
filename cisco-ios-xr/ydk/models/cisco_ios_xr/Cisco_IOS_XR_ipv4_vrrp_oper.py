""" Cisco_IOS_XR_ipv4_vrrp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-vrrp package operational data.

This module contains definitions
for the following management objects\:
  vrrp\: VRRP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class VrrpBAf(Enum):
    """
    VrrpBAf

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
    VrrpBagProtocolState

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
    VrrpBfdSessionState

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
    VrrpProtAuth

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
    VrrpStateChangeReason

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
    VrrpVipState

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
    VrrpVmacState

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
        super(Vrrp, self).__init__()
        self._top_entity = None

        self.yang_name = "vrrp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-vrrp-oper"

        self.ipv4 = Vrrp.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"
        self._children_yang_names.add("ipv4")

        self.ipv6 = Vrrp.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"
        self._children_yang_names.add("ipv6")

        self.mgo_sessions = Vrrp.MgoSessions()
        self.mgo_sessions.parent = self
        self._children_name_map["mgo_sessions"] = "mgo-sessions"
        self._children_yang_names.add("mgo-sessions")

        self.summary = Vrrp.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")


    class Summary(Entity):
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
            super(Vrrp.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "vrrp"

            self.bfd_session_inactive = YLeaf(YType.uint32, "bfd-session-inactive")

            self.bfd_sessions_down = YLeaf(YType.uint32, "bfd-sessions-down")

            self.bfd_sessions_up = YLeaf(YType.uint32, "bfd-sessions-up")

            self.interfaces_ipv4_state_down = YLeaf(YType.uint32, "interfaces-ipv4-state-down")

            self.interfaces_ipv4_state_up = YLeaf(YType.uint32, "interfaces-ipv4-state-up")

            self.interfaces_ipv6_state_down = YLeaf(YType.uint32, "interfaces-ipv6-state-down")

            self.interfaces_ipv6_state_up = YLeaf(YType.uint32, "interfaces-ipv6-state-up")

            self.ipv4_sessions_backup = YLeaf(YType.uint32, "ipv4-sessions-backup")

            self.ipv4_sessions_init = YLeaf(YType.uint32, "ipv4-sessions-init")

            self.ipv4_sessions_master = YLeaf(YType.uint32, "ipv4-sessions-master")

            self.ipv4_sessions_master_owner = YLeaf(YType.uint32, "ipv4-sessions-master-owner")

            self.ipv4_slaves_backup = YLeaf(YType.uint32, "ipv4-slaves-backup")

            self.ipv4_slaves_init = YLeaf(YType.uint32, "ipv4-slaves-init")

            self.ipv4_slaves_master = YLeaf(YType.uint32, "ipv4-slaves-master")

            self.ipv4_virtual_ip_addresses_backup_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-backup-down")

            self.ipv4_virtual_ip_addresses_backup_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-backup-up")

            self.ipv4_virtual_ip_addresses_init_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-init-down")

            self.ipv4_virtual_ip_addresses_init_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-init-up")

            self.ipv4_virtual_ip_addresses_master_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-master-down")

            self.ipv4_virtual_ip_addresses_master_owner_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-master-owner-down")

            self.ipv4_virtual_ip_addresses_master_owner_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-master-owner-up")

            self.ipv4_virtual_ip_addresses_master_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-master-up")

            self.ipv6_sessions_backup = YLeaf(YType.uint32, "ipv6-sessions-backup")

            self.ipv6_sessions_init = YLeaf(YType.uint32, "ipv6-sessions-init")

            self.ipv6_sessions_master = YLeaf(YType.uint32, "ipv6-sessions-master")

            self.ipv6_sessions_master_owner = YLeaf(YType.uint32, "ipv6-sessions-master-owner")

            self.ipv6_slaves_backup = YLeaf(YType.uint32, "ipv6-slaves-backup")

            self.ipv6_slaves_init = YLeaf(YType.uint32, "ipv6-slaves-init")

            self.ipv6_slaves_master = YLeaf(YType.uint32, "ipv6-slaves-master")

            self.ipv6_virtual_ip_addresses_backup_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-backup-down")

            self.ipv6_virtual_ip_addresses_backup_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-backup-up")

            self.ipv6_virtual_ip_addresses_init_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-init-down")

            self.ipv6_virtual_ip_addresses_init_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-init-up")

            self.ipv6_virtual_ip_addresses_master_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-master-down")

            self.ipv6_virtual_ip_addresses_master_owner_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-master-owner-down")

            self.ipv6_virtual_ip_addresses_master_owner_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-master-owner-up")

            self.ipv6_virtual_ip_addresses_master_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-master-up")

            self.ipv6bfd_session_inactive = YLeaf(YType.uint32, "ipv6bfd-session-inactive")

            self.ipv6bfd_sessions_down = YLeaf(YType.uint32, "ipv6bfd-sessions-down")

            self.ipv6bfd_sessions_up = YLeaf(YType.uint32, "ipv6bfd-sessions-up")

            self.tracked_interfaces_ipv4_state_down = YLeaf(YType.uint32, "tracked-interfaces-ipv4-state-down")

            self.tracked_interfaces_ipv4_state_up = YLeaf(YType.uint32, "tracked-interfaces-ipv4-state-up")

            self.tracked_interfaces_ipv6_state_down = YLeaf(YType.uint32, "tracked-interfaces-ipv6-state-down")

            self.tracked_interfaces_ipv6_state_up = YLeaf(YType.uint32, "tracked-interfaces-ipv6-state-up")

            self.tracked_objects_state_down = YLeaf(YType.uint32, "tracked-objects-state-down")

            self.tracked_objects_state_up = YLeaf(YType.uint32, "tracked-objects-state-up")

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
                            "ipv4_sessions_backup",
                            "ipv4_sessions_init",
                            "ipv4_sessions_master",
                            "ipv4_sessions_master_owner",
                            "ipv4_slaves_backup",
                            "ipv4_slaves_init",
                            "ipv4_slaves_master",
                            "ipv4_virtual_ip_addresses_backup_down",
                            "ipv4_virtual_ip_addresses_backup_up",
                            "ipv4_virtual_ip_addresses_init_down",
                            "ipv4_virtual_ip_addresses_init_up",
                            "ipv4_virtual_ip_addresses_master_down",
                            "ipv4_virtual_ip_addresses_master_owner_down",
                            "ipv4_virtual_ip_addresses_master_owner_up",
                            "ipv4_virtual_ip_addresses_master_up",
                            "ipv6_sessions_backup",
                            "ipv6_sessions_init",
                            "ipv6_sessions_master",
                            "ipv6_sessions_master_owner",
                            "ipv6_slaves_backup",
                            "ipv6_slaves_init",
                            "ipv6_slaves_master",
                            "ipv6_virtual_ip_addresses_backup_down",
                            "ipv6_virtual_ip_addresses_backup_up",
                            "ipv6_virtual_ip_addresses_init_down",
                            "ipv6_virtual_ip_addresses_init_up",
                            "ipv6_virtual_ip_addresses_master_down",
                            "ipv6_virtual_ip_addresses_master_owner_down",
                            "ipv6_virtual_ip_addresses_master_owner_up",
                            "ipv6_virtual_ip_addresses_master_up",
                            "ipv6bfd_session_inactive",
                            "ipv6bfd_sessions_down",
                            "ipv6bfd_sessions_up",
                            "tracked_interfaces_ipv4_state_down",
                            "tracked_interfaces_ipv4_state_up",
                            "tracked_interfaces_ipv6_state_down",
                            "tracked_interfaces_ipv6_state_up",
                            "tracked_objects_state_down",
                            "tracked_objects_state_up") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vrrp.Summary, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vrrp.Summary, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.bfd_session_inactive.is_set or
                self.bfd_sessions_down.is_set or
                self.bfd_sessions_up.is_set or
                self.interfaces_ipv4_state_down.is_set or
                self.interfaces_ipv4_state_up.is_set or
                self.interfaces_ipv6_state_down.is_set or
                self.interfaces_ipv6_state_up.is_set or
                self.ipv4_sessions_backup.is_set or
                self.ipv4_sessions_init.is_set or
                self.ipv4_sessions_master.is_set or
                self.ipv4_sessions_master_owner.is_set or
                self.ipv4_slaves_backup.is_set or
                self.ipv4_slaves_init.is_set or
                self.ipv4_slaves_master.is_set or
                self.ipv4_virtual_ip_addresses_backup_down.is_set or
                self.ipv4_virtual_ip_addresses_backup_up.is_set or
                self.ipv4_virtual_ip_addresses_init_down.is_set or
                self.ipv4_virtual_ip_addresses_init_up.is_set or
                self.ipv4_virtual_ip_addresses_master_down.is_set or
                self.ipv4_virtual_ip_addresses_master_owner_down.is_set or
                self.ipv4_virtual_ip_addresses_master_owner_up.is_set or
                self.ipv4_virtual_ip_addresses_master_up.is_set or
                self.ipv6_sessions_backup.is_set or
                self.ipv6_sessions_init.is_set or
                self.ipv6_sessions_master.is_set or
                self.ipv6_sessions_master_owner.is_set or
                self.ipv6_slaves_backup.is_set or
                self.ipv6_slaves_init.is_set or
                self.ipv6_slaves_master.is_set or
                self.ipv6_virtual_ip_addresses_backup_down.is_set or
                self.ipv6_virtual_ip_addresses_backup_up.is_set or
                self.ipv6_virtual_ip_addresses_init_down.is_set or
                self.ipv6_virtual_ip_addresses_init_up.is_set or
                self.ipv6_virtual_ip_addresses_master_down.is_set or
                self.ipv6_virtual_ip_addresses_master_owner_down.is_set or
                self.ipv6_virtual_ip_addresses_master_owner_up.is_set or
                self.ipv6_virtual_ip_addresses_master_up.is_set or
                self.ipv6bfd_session_inactive.is_set or
                self.ipv6bfd_sessions_down.is_set or
                self.ipv6bfd_sessions_up.is_set or
                self.tracked_interfaces_ipv4_state_down.is_set or
                self.tracked_interfaces_ipv4_state_up.is_set or
                self.tracked_interfaces_ipv6_state_down.is_set or
                self.tracked_interfaces_ipv6_state_up.is_set or
                self.tracked_objects_state_down.is_set or
                self.tracked_objects_state_up.is_set)

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
                self.ipv4_sessions_backup.yfilter != YFilter.not_set or
                self.ipv4_sessions_init.yfilter != YFilter.not_set or
                self.ipv4_sessions_master.yfilter != YFilter.not_set or
                self.ipv4_sessions_master_owner.yfilter != YFilter.not_set or
                self.ipv4_slaves_backup.yfilter != YFilter.not_set or
                self.ipv4_slaves_init.yfilter != YFilter.not_set or
                self.ipv4_slaves_master.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_backup_down.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_backup_up.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_init_down.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_init_up.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_master_down.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_master_owner_down.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_master_owner_up.yfilter != YFilter.not_set or
                self.ipv4_virtual_ip_addresses_master_up.yfilter != YFilter.not_set or
                self.ipv6_sessions_backup.yfilter != YFilter.not_set or
                self.ipv6_sessions_init.yfilter != YFilter.not_set or
                self.ipv6_sessions_master.yfilter != YFilter.not_set or
                self.ipv6_sessions_master_owner.yfilter != YFilter.not_set or
                self.ipv6_slaves_backup.yfilter != YFilter.not_set or
                self.ipv6_slaves_init.yfilter != YFilter.not_set or
                self.ipv6_slaves_master.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_backup_down.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_backup_up.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_init_down.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_init_up.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_master_down.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_master_owner_down.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_master_owner_up.yfilter != YFilter.not_set or
                self.ipv6_virtual_ip_addresses_master_up.yfilter != YFilter.not_set or
                self.ipv6bfd_session_inactive.yfilter != YFilter.not_set or
                self.ipv6bfd_sessions_down.yfilter != YFilter.not_set or
                self.ipv6bfd_sessions_up.yfilter != YFilter.not_set or
                self.tracked_interfaces_ipv4_state_down.yfilter != YFilter.not_set or
                self.tracked_interfaces_ipv4_state_up.yfilter != YFilter.not_set or
                self.tracked_interfaces_ipv6_state_down.yfilter != YFilter.not_set or
                self.tracked_interfaces_ipv6_state_up.yfilter != YFilter.not_set or
                self.tracked_objects_state_down.yfilter != YFilter.not_set or
                self.tracked_objects_state_up.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "summary" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/%s" % self.get_segment_path()
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
            if (self.ipv4_sessions_backup.is_set or self.ipv4_sessions_backup.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_sessions_backup.get_name_leafdata())
            if (self.ipv4_sessions_init.is_set or self.ipv4_sessions_init.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_sessions_init.get_name_leafdata())
            if (self.ipv4_sessions_master.is_set or self.ipv4_sessions_master.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_sessions_master.get_name_leafdata())
            if (self.ipv4_sessions_master_owner.is_set or self.ipv4_sessions_master_owner.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_sessions_master_owner.get_name_leafdata())
            if (self.ipv4_slaves_backup.is_set or self.ipv4_slaves_backup.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_slaves_backup.get_name_leafdata())
            if (self.ipv4_slaves_init.is_set or self.ipv4_slaves_init.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_slaves_init.get_name_leafdata())
            if (self.ipv4_slaves_master.is_set or self.ipv4_slaves_master.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_slaves_master.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_backup_down.is_set or self.ipv4_virtual_ip_addresses_backup_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_backup_down.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_backup_up.is_set or self.ipv4_virtual_ip_addresses_backup_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_backup_up.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_init_down.is_set or self.ipv4_virtual_ip_addresses_init_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_init_down.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_init_up.is_set or self.ipv4_virtual_ip_addresses_init_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_init_up.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_master_down.is_set or self.ipv4_virtual_ip_addresses_master_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_master_down.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_master_owner_down.is_set or self.ipv4_virtual_ip_addresses_master_owner_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_master_owner_down.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_master_owner_up.is_set or self.ipv4_virtual_ip_addresses_master_owner_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_master_owner_up.get_name_leafdata())
            if (self.ipv4_virtual_ip_addresses_master_up.is_set or self.ipv4_virtual_ip_addresses_master_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_virtual_ip_addresses_master_up.get_name_leafdata())
            if (self.ipv6_sessions_backup.is_set or self.ipv6_sessions_backup.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_sessions_backup.get_name_leafdata())
            if (self.ipv6_sessions_init.is_set or self.ipv6_sessions_init.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_sessions_init.get_name_leafdata())
            if (self.ipv6_sessions_master.is_set or self.ipv6_sessions_master.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_sessions_master.get_name_leafdata())
            if (self.ipv6_sessions_master_owner.is_set or self.ipv6_sessions_master_owner.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_sessions_master_owner.get_name_leafdata())
            if (self.ipv6_slaves_backup.is_set or self.ipv6_slaves_backup.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_slaves_backup.get_name_leafdata())
            if (self.ipv6_slaves_init.is_set or self.ipv6_slaves_init.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_slaves_init.get_name_leafdata())
            if (self.ipv6_slaves_master.is_set or self.ipv6_slaves_master.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_slaves_master.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_backup_down.is_set or self.ipv6_virtual_ip_addresses_backup_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_backup_down.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_backup_up.is_set or self.ipv6_virtual_ip_addresses_backup_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_backup_up.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_init_down.is_set or self.ipv6_virtual_ip_addresses_init_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_init_down.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_init_up.is_set or self.ipv6_virtual_ip_addresses_init_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_init_up.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_master_down.is_set or self.ipv6_virtual_ip_addresses_master_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_master_down.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_master_owner_down.is_set or self.ipv6_virtual_ip_addresses_master_owner_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_master_owner_down.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_master_owner_up.is_set or self.ipv6_virtual_ip_addresses_master_owner_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_master_owner_up.get_name_leafdata())
            if (self.ipv6_virtual_ip_addresses_master_up.is_set or self.ipv6_virtual_ip_addresses_master_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_virtual_ip_addresses_master_up.get_name_leafdata())
            if (self.ipv6bfd_session_inactive.is_set or self.ipv6bfd_session_inactive.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6bfd_session_inactive.get_name_leafdata())
            if (self.ipv6bfd_sessions_down.is_set or self.ipv6bfd_sessions_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6bfd_sessions_down.get_name_leafdata())
            if (self.ipv6bfd_sessions_up.is_set or self.ipv6bfd_sessions_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6bfd_sessions_up.get_name_leafdata())
            if (self.tracked_interfaces_ipv4_state_down.is_set or self.tracked_interfaces_ipv4_state_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_interfaces_ipv4_state_down.get_name_leafdata())
            if (self.tracked_interfaces_ipv4_state_up.is_set or self.tracked_interfaces_ipv4_state_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_interfaces_ipv4_state_up.get_name_leafdata())
            if (self.tracked_interfaces_ipv6_state_down.is_set or self.tracked_interfaces_ipv6_state_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_interfaces_ipv6_state_down.get_name_leafdata())
            if (self.tracked_interfaces_ipv6_state_up.is_set or self.tracked_interfaces_ipv6_state_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_interfaces_ipv6_state_up.get_name_leafdata())
            if (self.tracked_objects_state_down.is_set or self.tracked_objects_state_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_objects_state_down.get_name_leafdata())
            if (self.tracked_objects_state_up.is_set or self.tracked_objects_state_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tracked_objects_state_up.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bfd-session-inactive" or name == "bfd-sessions-down" or name == "bfd-sessions-up" or name == "interfaces-ipv4-state-down" or name == "interfaces-ipv4-state-up" or name == "interfaces-ipv6-state-down" or name == "interfaces-ipv6-state-up" or name == "ipv4-sessions-backup" or name == "ipv4-sessions-init" or name == "ipv4-sessions-master" or name == "ipv4-sessions-master-owner" or name == "ipv4-slaves-backup" or name == "ipv4-slaves-init" or name == "ipv4-slaves-master" or name == "ipv4-virtual-ip-addresses-backup-down" or name == "ipv4-virtual-ip-addresses-backup-up" or name == "ipv4-virtual-ip-addresses-init-down" or name == "ipv4-virtual-ip-addresses-init-up" or name == "ipv4-virtual-ip-addresses-master-down" or name == "ipv4-virtual-ip-addresses-master-owner-down" or name == "ipv4-virtual-ip-addresses-master-owner-up" or name == "ipv4-virtual-ip-addresses-master-up" or name == "ipv6-sessions-backup" or name == "ipv6-sessions-init" or name == "ipv6-sessions-master" or name == "ipv6-sessions-master-owner" or name == "ipv6-slaves-backup" or name == "ipv6-slaves-init" or name == "ipv6-slaves-master" or name == "ipv6-virtual-ip-addresses-backup-down" or name == "ipv6-virtual-ip-addresses-backup-up" or name == "ipv6-virtual-ip-addresses-init-down" or name == "ipv6-virtual-ip-addresses-init-up" or name == "ipv6-virtual-ip-addresses-master-down" or name == "ipv6-virtual-ip-addresses-master-owner-down" or name == "ipv6-virtual-ip-addresses-master-owner-up" or name == "ipv6-virtual-ip-addresses-master-up" or name == "ipv6bfd-session-inactive" or name == "ipv6bfd-sessions-down" or name == "ipv6bfd-sessions-up" or name == "tracked-interfaces-ipv4-state-down" or name == "tracked-interfaces-ipv4-state-up" or name == "tracked-interfaces-ipv6-state-down" or name == "tracked-interfaces-ipv6-state-up" or name == "tracked-objects-state-down" or name == "tracked-objects-state-up"):
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
            if(value_path == "ipv4-sessions-backup"):
                self.ipv4_sessions_backup = value
                self.ipv4_sessions_backup.value_namespace = name_space
                self.ipv4_sessions_backup.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-sessions-init"):
                self.ipv4_sessions_init = value
                self.ipv4_sessions_init.value_namespace = name_space
                self.ipv4_sessions_init.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-sessions-master"):
                self.ipv4_sessions_master = value
                self.ipv4_sessions_master.value_namespace = name_space
                self.ipv4_sessions_master.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-sessions-master-owner"):
                self.ipv4_sessions_master_owner = value
                self.ipv4_sessions_master_owner.value_namespace = name_space
                self.ipv4_sessions_master_owner.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-slaves-backup"):
                self.ipv4_slaves_backup = value
                self.ipv4_slaves_backup.value_namespace = name_space
                self.ipv4_slaves_backup.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-slaves-init"):
                self.ipv4_slaves_init = value
                self.ipv4_slaves_init.value_namespace = name_space
                self.ipv4_slaves_init.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-slaves-master"):
                self.ipv4_slaves_master = value
                self.ipv4_slaves_master.value_namespace = name_space
                self.ipv4_slaves_master.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-backup-down"):
                self.ipv4_virtual_ip_addresses_backup_down = value
                self.ipv4_virtual_ip_addresses_backup_down.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_backup_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-backup-up"):
                self.ipv4_virtual_ip_addresses_backup_up = value
                self.ipv4_virtual_ip_addresses_backup_up.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_backup_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-init-down"):
                self.ipv4_virtual_ip_addresses_init_down = value
                self.ipv4_virtual_ip_addresses_init_down.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_init_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-init-up"):
                self.ipv4_virtual_ip_addresses_init_up = value
                self.ipv4_virtual_ip_addresses_init_up.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_init_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-master-down"):
                self.ipv4_virtual_ip_addresses_master_down = value
                self.ipv4_virtual_ip_addresses_master_down.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_master_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-master-owner-down"):
                self.ipv4_virtual_ip_addresses_master_owner_down = value
                self.ipv4_virtual_ip_addresses_master_owner_down.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_master_owner_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-master-owner-up"):
                self.ipv4_virtual_ip_addresses_master_owner_up = value
                self.ipv4_virtual_ip_addresses_master_owner_up.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_master_owner_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-virtual-ip-addresses-master-up"):
                self.ipv4_virtual_ip_addresses_master_up = value
                self.ipv4_virtual_ip_addresses_master_up.value_namespace = name_space
                self.ipv4_virtual_ip_addresses_master_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-sessions-backup"):
                self.ipv6_sessions_backup = value
                self.ipv6_sessions_backup.value_namespace = name_space
                self.ipv6_sessions_backup.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-sessions-init"):
                self.ipv6_sessions_init = value
                self.ipv6_sessions_init.value_namespace = name_space
                self.ipv6_sessions_init.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-sessions-master"):
                self.ipv6_sessions_master = value
                self.ipv6_sessions_master.value_namespace = name_space
                self.ipv6_sessions_master.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-sessions-master-owner"):
                self.ipv6_sessions_master_owner = value
                self.ipv6_sessions_master_owner.value_namespace = name_space
                self.ipv6_sessions_master_owner.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-slaves-backup"):
                self.ipv6_slaves_backup = value
                self.ipv6_slaves_backup.value_namespace = name_space
                self.ipv6_slaves_backup.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-slaves-init"):
                self.ipv6_slaves_init = value
                self.ipv6_slaves_init.value_namespace = name_space
                self.ipv6_slaves_init.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-slaves-master"):
                self.ipv6_slaves_master = value
                self.ipv6_slaves_master.value_namespace = name_space
                self.ipv6_slaves_master.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-backup-down"):
                self.ipv6_virtual_ip_addresses_backup_down = value
                self.ipv6_virtual_ip_addresses_backup_down.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_backup_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-backup-up"):
                self.ipv6_virtual_ip_addresses_backup_up = value
                self.ipv6_virtual_ip_addresses_backup_up.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_backup_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-init-down"):
                self.ipv6_virtual_ip_addresses_init_down = value
                self.ipv6_virtual_ip_addresses_init_down.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_init_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-init-up"):
                self.ipv6_virtual_ip_addresses_init_up = value
                self.ipv6_virtual_ip_addresses_init_up.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_init_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-master-down"):
                self.ipv6_virtual_ip_addresses_master_down = value
                self.ipv6_virtual_ip_addresses_master_down.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_master_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-master-owner-down"):
                self.ipv6_virtual_ip_addresses_master_owner_down = value
                self.ipv6_virtual_ip_addresses_master_owner_down.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_master_owner_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-master-owner-up"):
                self.ipv6_virtual_ip_addresses_master_owner_up = value
                self.ipv6_virtual_ip_addresses_master_owner_up.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_master_owner_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-virtual-ip-addresses-master-up"):
                self.ipv6_virtual_ip_addresses_master_up = value
                self.ipv6_virtual_ip_addresses_master_up.value_namespace = name_space
                self.ipv6_virtual_ip_addresses_master_up.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6bfd-session-inactive"):
                self.ipv6bfd_session_inactive = value
                self.ipv6bfd_session_inactive.value_namespace = name_space
                self.ipv6bfd_session_inactive.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6bfd-sessions-down"):
                self.ipv6bfd_sessions_down = value
                self.ipv6bfd_sessions_down.value_namespace = name_space
                self.ipv6bfd_sessions_down.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6bfd-sessions-up"):
                self.ipv6bfd_sessions_up = value
                self.ipv6bfd_sessions_up.value_namespace = name_space
                self.ipv6bfd_sessions_up.value_namespace_prefix = name_space_prefix
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
            if(value_path == "tracked-objects-state-down"):
                self.tracked_objects_state_down = value
                self.tracked_objects_state_down.value_namespace = name_space
                self.tracked_objects_state_down.value_namespace_prefix = name_space_prefix
            if(value_path == "tracked-objects-state-up"):
                self.tracked_objects_state_up = value
                self.tracked_objects_state_up.value_namespace = name_space
                self.tracked_objects_state_up.value_namespace_prefix = name_space_prefix


    class Ipv6(Entity):
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
            super(Vrrp.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "vrrp"

            self.interfaces = Vrrp.Ipv6.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.track_items = Vrrp.Ipv6.TrackItems()
            self.track_items.parent = self
            self._children_name_map["track_items"] = "track-items"
            self._children_yang_names.add("track-items")

            self.virtual_routers = Vrrp.Ipv6.VirtualRouters()
            self.virtual_routers.parent = self
            self._children_name_map["virtual_routers"] = "virtual-routers"
            self._children_yang_names.add("virtual-routers")


        class TrackItems(Entity):
            """
            The VRRP tracked item table
            
            .. attribute:: track_item
            
            	A configured VRRP IP address entry
            	**type**\: list of    :py:class:`TrackItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.TrackItems.TrackItem>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                super(Vrrp.Ipv6.TrackItems, self).__init__()

                self.yang_name = "track-items"
                self.yang_parent_name = "ipv6"

                self.track_item = YList(self)

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
                            super(Vrrp.Ipv6.TrackItems, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vrrp.Ipv6.TrackItems, self).__setattr__(name, value)


            class TrackItem(Entity):
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
                    super(Vrrp.Ipv6.TrackItems.TrackItem, self).__init__()

                    self.yang_name = "track-item"
                    self.yang_parent_name = "track-items"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.virtual_router_id = YLeaf(YType.int32, "virtual-router-id")

                    self.tracked_interface_name = YLeaf(YType.str, "tracked-interface-name")

                    self.interface = YLeaf(YType.str, "interface")

                    self.priority = YLeaf(YType.uint8, "priority")

                    self.state = YLeaf(YType.uint8, "state")

                    self.tracked_item_index = YLeaf(YType.str, "tracked-item-index")

                    self.tracked_item_type = YLeaf(YType.uint16, "tracked-item-type")

                    self.virtual_router_id_xr = YLeaf(YType.uint32, "virtual-router-id-xr")

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
                                    "virtual_router_id",
                                    "tracked_interface_name",
                                    "interface",
                                    "priority",
                                    "state",
                                    "tracked_item_index",
                                    "tracked_item_type",
                                    "virtual_router_id_xr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrrp.Ipv6.TrackItems.TrackItem, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrrp.Ipv6.TrackItems.TrackItem, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.virtual_router_id.is_set or
                        self.tracked_interface_name.is_set or
                        self.interface.is_set or
                        self.priority.is_set or
                        self.state.is_set or
                        self.tracked_item_index.is_set or
                        self.tracked_item_type.is_set or
                        self.virtual_router_id_xr.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.virtual_router_id.yfilter != YFilter.not_set or
                        self.tracked_interface_name.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.priority.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.tracked_item_index.yfilter != YFilter.not_set or
                        self.tracked_item_type.yfilter != YFilter.not_set or
                        self.virtual_router_id_xr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "track-item" + "[interface-name='" + self.interface_name.get() + "']" + "[virtual-router-id='" + self.virtual_router_id.get() + "']" + "[tracked-interface-name='" + self.tracked_interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/track-items/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.virtual_router_id.is_set or self.virtual_router_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_router_id.get_name_leafdata())
                    if (self.tracked_interface_name.is_set or self.tracked_interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_name.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.tracked_item_index.is_set or self.tracked_item_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_item_index.get_name_leafdata())
                    if (self.tracked_item_type.is_set or self.tracked_item_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_item_type.get_name_leafdata())
                    if (self.virtual_router_id_xr.is_set or self.virtual_router_id_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_router_id_xr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "virtual-router-id" or name == "tracked-interface-name" or name == "interface" or name == "priority" or name == "state" or name == "tracked-item-index" or name == "tracked-item-type" or name == "virtual-router-id-xr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-router-id"):
                        self.virtual_router_id = value
                        self.virtual_router_id.value_namespace = name_space
                        self.virtual_router_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-name"):
                        self.tracked_interface_name = value
                        self.tracked_interface_name.value_namespace = name_space
                        self.tracked_interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority"):
                        self.priority = value
                        self.priority.value_namespace = name_space
                        self.priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-item-index"):
                        self.tracked_item_index = value
                        self.tracked_item_index.value_namespace = name_space
                        self.tracked_item_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-item-type"):
                        self.tracked_item_type = value
                        self.tracked_item_type.value_namespace = name_space
                        self.tracked_item_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-router-id-xr"):
                        self.virtual_router_id_xr = value
                        self.virtual_router_id_xr.value_namespace = name_space
                        self.virtual_router_id_xr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.track_item:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.track_item:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "track-items" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "track-item"):
                    for c in self.track_item:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Vrrp.Ipv6.TrackItems.TrackItem()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.track_item.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "track-item"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class VirtualRouters(Entity):
            """
            The VRRP virtual router table
            
            .. attribute:: virtual_router
            
            	A VRRP virtual router
            	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                super(Vrrp.Ipv6.VirtualRouters, self).__init__()

                self.yang_name = "virtual-routers"
                self.yang_parent_name = "ipv6"

                self.virtual_router = YList(self)

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
                            super(Vrrp.Ipv6.VirtualRouters, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vrrp.Ipv6.VirtualRouters, self).__setattr__(name, value)


            class VirtualRouter(Entity):
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
                	**type**\:   :py:class:`VrrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBAf>`
                
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
                	**type**\:   :py:class:`VrrpProtAuth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpProtAuth>`
                
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
                	**type**\:   :py:class:`VrrpBfdSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBfdSessionState>`
                
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
                	**type**\:   :py:class:`VrrpVipState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVipState>`
                
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
                	**type**\:   :py:class:`VrrpVmacState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVmacState>`
                
                .. attribute:: virtual_router_id_xr
                
                	Virtual Router ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrrp_state
                
                	VRRP state
                	**type**\:   :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2016-12-16'

                def __init__(self):
                    super(Vrrp.Ipv6.VirtualRouters.VirtualRouter, self).__init__()

                    self.yang_name = "virtual-router"
                    self.yang_parent_name = "virtual-routers"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.virtual_router_id = YLeaf(YType.int32, "virtual-router-id")

                    self.address_family = YLeaf(YType.enumeration, "address-family")

                    self.address_list_error_count = YLeaf(YType.uint32, "address-list-error-count")

                    self.advert_interval_error_count = YLeaf(YType.uint32, "advert-interval-error-count")

                    self.adverts_received_count = YLeaf(YType.uint32, "adverts-received-count")

                    self.adverts_sent_count = YLeaf(YType.uint32, "adverts-sent-count")

                    self.auth_type_mismatch_count = YLeaf(YType.uint32, "auth-type-mismatch-count")

                    self.authentication_fail_count = YLeaf(YType.uint32, "authentication-fail-count")

                    self.authentication_flag = YLeaf(YType.boolean, "authentication-flag")

                    self.authentication_string = YLeaf(YType.str, "authentication-string")

                    self.authentication_type = YLeaf(YType.enumeration, "authentication-type")

                    self.bfd_cfg_remote_ip = YLeaf(YType.str, "bfd-cfg-remote-ip")

                    self.bfd_configured_remote_ipv6_address = YLeaf(YType.str, "bfd-configured-remote-ipv6-address")

                    self.bfd_interval = YLeaf(YType.uint32, "bfd-interval")

                    self.bfd_multiplier = YLeaf(YType.uint32, "bfd-multiplier")

                    self.bfd_session_state = YLeaf(YType.enumeration, "bfd-session-state")

                    self.configured_advertize_time = YLeaf(YType.uint32, "configured-advertize-time")

                    self.configured_down_address_count = YLeaf(YType.uint8, "configured-down-address-count")

                    self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                    self.delay_timer_flag = YLeaf(YType.boolean, "delay-timer-flag")

                    self.delay_timer_msecs = YLeaf(YType.uint32, "delay-timer-msecs")

                    self.delay_timer_secs = YLeaf(YType.uint32, "delay-timer-secs")

                    self.followed_session_name = YLeaf(YType.str, "followed-session-name")

                    self.force_timer_flag = YLeaf(YType.boolean, "force-timer-flag")

                    self.interface_ipv4_address = YLeaf(YType.str, "interface-ipv4-address")

                    self.interface_ipv6_address = YLeaf(YType.str, "interface-ipv6-address")

                    self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                    self.invalid_auth_type_count = YLeaf(YType.uint32, "invalid-auth-type-count")

                    self.invalid_packet_count = YLeaf(YType.uint32, "invalid-packet-count")

                    self.ip_address_owner_flag = YLeaf(YType.boolean, "ip-address-owner-flag")

                    self.ipv4_configured_down_address = YLeafList(YType.str, "ipv4-configured-down-address")

                    self.is_accept_mode = YLeaf(YType.boolean, "is-accept-mode")

                    self.is_slave = YLeaf(YType.boolean, "is-slave")

                    self.master_count = YLeaf(YType.uint32, "master-count")

                    self.master_ip_address = YLeaf(YType.str, "master-ip-address")

                    self.master_ipv6_address = YLeaf(YType.str, "master-ipv6-address")

                    self.master_priority = YLeaf(YType.uint8, "master-priority")

                    self.min_delay_time = YLeaf(YType.uint32, "min-delay-time")

                    self.oper_advertize_time = YLeaf(YType.uint32, "oper-advertize-time")

                    self.operational_address = YLeafList(YType.str, "operational-address")

                    self.operational_address_count = YLeaf(YType.uint8, "operational-address-count")

                    self.operational_priority = YLeaf(YType.uint8, "operational-priority")

                    self.pkt_length_errors_count = YLeaf(YType.uint32, "pkt-length-errors-count")

                    self.preempt_delay_time = YLeaf(YType.uint16, "preempt-delay-time")

                    self.preempt_flag = YLeaf(YType.boolean, "preempt-flag")

                    self.primary_state = YLeaf(YType.enumeration, "primary-state")

                    self.primary_virtual_ip = YLeaf(YType.str, "primary-virtual-ip")

                    self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")

                    self.priority_zero_received_count = YLeaf(YType.uint32, "priority-zero-received-count")

                    self.priority_zero_sent_count = YLeaf(YType.uint32, "priority-zero-sent-count")

                    self.reload_delay_time = YLeaf(YType.uint32, "reload-delay-time")

                    self.secondary_address_count = YLeaf(YType.uint8, "secondary-address-count")

                    self.session_name = YLeaf(YType.str, "session-name")

                    self.slaves = YLeaf(YType.uint32, "slaves")

                    self.state_change_count = YLeaf(YType.uint32, "state-change-count")

                    self.state_from_checkpoint = YLeaf(YType.boolean, "state-from-checkpoint")

                    self.time_in_current_state = YLeaf(YType.uint32, "time-in-current-state")

                    self.time_stats_discontinuity = YLeaf(YType.uint32, "time-stats-discontinuity")

                    self.time_vrouter_up = YLeaf(YType.uint32, "time-vrouter-up")

                    self.tracked_interface_count = YLeaf(YType.uint32, "tracked-interface-count")

                    self.tracked_interface_up_count = YLeaf(YType.uint32, "tracked-interface-up-count")

                    self.tracked_item_count = YLeaf(YType.uint32, "tracked-item-count")

                    self.tracked_item_up_count = YLeaf(YType.uint32, "tracked-item-up-count")

                    self.ttl_error_count = YLeaf(YType.uint32, "ttl-error-count")

                    self.version = YLeaf(YType.uint8, "version")

                    self.virtual_linklocal_ipv6_address = YLeaf(YType.str, "virtual-linklocal-ipv6-address")

                    self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                    self.virtual_mac_address_state = YLeaf(YType.enumeration, "virtual-mac-address-state")

                    self.virtual_router_id_xr = YLeaf(YType.uint32, "virtual-router-id-xr")

                    self.vrrp_state = YLeaf(YType.enumeration, "vrrp-state")

                    self.resign_received_time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self._children_name_map["resign_received_time"] = "resign-received-time"
                    self._children_yang_names.add("resign-received-time")

                    self.resign_sent_time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self._children_name_map["resign_sent_time"] = "resign-sent-time"
                    self._children_yang_names.add("resign-sent-time")

                    self.ipv6_configured_down_address = YList(self)
                    self.ipv6_operational_address = YList(self)
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
                                    "virtual_router_id",
                                    "address_family",
                                    "address_list_error_count",
                                    "advert_interval_error_count",
                                    "adverts_received_count",
                                    "adverts_sent_count",
                                    "auth_type_mismatch_count",
                                    "authentication_fail_count",
                                    "authentication_flag",
                                    "authentication_string",
                                    "authentication_type",
                                    "bfd_cfg_remote_ip",
                                    "bfd_configured_remote_ipv6_address",
                                    "bfd_interval",
                                    "bfd_multiplier",
                                    "bfd_session_state",
                                    "configured_advertize_time",
                                    "configured_down_address_count",
                                    "configured_priority",
                                    "delay_timer_flag",
                                    "delay_timer_msecs",
                                    "delay_timer_secs",
                                    "followed_session_name",
                                    "force_timer_flag",
                                    "interface_ipv4_address",
                                    "interface_ipv6_address",
                                    "interface_name_xr",
                                    "invalid_auth_type_count",
                                    "invalid_packet_count",
                                    "ip_address_owner_flag",
                                    "ipv4_configured_down_address",
                                    "is_accept_mode",
                                    "is_slave",
                                    "master_count",
                                    "master_ip_address",
                                    "master_ipv6_address",
                                    "master_priority",
                                    "min_delay_time",
                                    "oper_advertize_time",
                                    "operational_address",
                                    "operational_address_count",
                                    "operational_priority",
                                    "pkt_length_errors_count",
                                    "preempt_delay_time",
                                    "preempt_flag",
                                    "primary_state",
                                    "primary_virtual_ip",
                                    "priority_decrement",
                                    "priority_zero_received_count",
                                    "priority_zero_sent_count",
                                    "reload_delay_time",
                                    "secondary_address_count",
                                    "session_name",
                                    "slaves",
                                    "state_change_count",
                                    "state_from_checkpoint",
                                    "time_in_current_state",
                                    "time_stats_discontinuity",
                                    "time_vrouter_up",
                                    "tracked_interface_count",
                                    "tracked_interface_up_count",
                                    "tracked_item_count",
                                    "tracked_item_up_count",
                                    "ttl_error_count",
                                    "version",
                                    "virtual_linklocal_ipv6_address",
                                    "virtual_mac_address",
                                    "virtual_mac_address_state",
                                    "virtual_router_id_xr",
                                    "vrrp_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrrp.Ipv6.VirtualRouters.VirtualRouter, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrrp.Ipv6.VirtualRouters.VirtualRouter, self).__setattr__(name, value)


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

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime, self).__init__()

                        self.yang_name = "resign-sent-time"
                        self.yang_parent_name = "virtual-router"

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
                                    super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime, self).__setattr__(name, value)

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

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime, self).__init__()

                        self.yang_name = "resign-received-time"
                        self.yang_parent_name = "virtual-router"

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
                                    super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime, self).__setattr__(name, value)

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


                class Ipv6OperationalAddress(Entity):
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
                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress, self).__init__()

                        self.yang_name = "ipv6-operational-address"
                        self.yang_parent_name = "virtual-router"

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
                                    super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress, self).__setattr__(name, value)

                    def has_data(self):
                        return self.ipv6_address.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipv6_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6-operational-address" + path_buffer

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


                class Ipv6ConfiguredDownAddress(Entity):
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
                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress, self).__init__()

                        self.yang_name = "ipv6-configured-down-address"
                        self.yang_parent_name = "virtual-router"

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
                                    super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress, self).__setattr__(name, value)

                    def has_data(self):
                        return self.ipv6_address.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipv6_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6-configured-down-address" + path_buffer

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
                    	**type**\:   :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:   :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:   :py:class:`VrrpStateChangeReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpStateChangeReason>`
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:   :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory, self).__init__()

                        self.yang_name = "state-change-history"
                        self.yang_parent_name = "virtual-router"

                        self.new_state = YLeaf(YType.enumeration, "new-state")

                        self.old_state = YLeaf(YType.enumeration, "old-state")

                        self.reason = YLeaf(YType.enumeration, "reason")

                        self.time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time()
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
                                    super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory, self).__setattr__(name, value)


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

                        _prefix = 'ipv4-vrrp-oper'
                        _revision = '2016-12-16'

                        def __init__(self):
                            super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time, self).__init__()

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
                                        super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time, self).__setattr__(name, value)

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
                                self.time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time()
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
                    for c in self.ipv6_configured_down_address:
                        if (c.has_data()):
                            return True
                    for c in self.ipv6_operational_address:
                        if (c.has_data()):
                            return True
                    for c in self.state_change_history:
                        if (c.has_data()):
                            return True
                    for leaf in self.ipv4_configured_down_address.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.operational_address.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.interface_name.is_set or
                        self.virtual_router_id.is_set or
                        self.address_family.is_set or
                        self.address_list_error_count.is_set or
                        self.advert_interval_error_count.is_set or
                        self.adverts_received_count.is_set or
                        self.adverts_sent_count.is_set or
                        self.auth_type_mismatch_count.is_set or
                        self.authentication_fail_count.is_set or
                        self.authentication_flag.is_set or
                        self.authentication_string.is_set or
                        self.authentication_type.is_set or
                        self.bfd_cfg_remote_ip.is_set or
                        self.bfd_configured_remote_ipv6_address.is_set or
                        self.bfd_interval.is_set or
                        self.bfd_multiplier.is_set or
                        self.bfd_session_state.is_set or
                        self.configured_advertize_time.is_set or
                        self.configured_down_address_count.is_set or
                        self.configured_priority.is_set or
                        self.delay_timer_flag.is_set or
                        self.delay_timer_msecs.is_set or
                        self.delay_timer_secs.is_set or
                        self.followed_session_name.is_set or
                        self.force_timer_flag.is_set or
                        self.interface_ipv4_address.is_set or
                        self.interface_ipv6_address.is_set or
                        self.interface_name_xr.is_set or
                        self.invalid_auth_type_count.is_set or
                        self.invalid_packet_count.is_set or
                        self.ip_address_owner_flag.is_set or
                        self.is_accept_mode.is_set or
                        self.is_slave.is_set or
                        self.master_count.is_set or
                        self.master_ip_address.is_set or
                        self.master_ipv6_address.is_set or
                        self.master_priority.is_set or
                        self.min_delay_time.is_set or
                        self.oper_advertize_time.is_set or
                        self.operational_address_count.is_set or
                        self.operational_priority.is_set or
                        self.pkt_length_errors_count.is_set or
                        self.preempt_delay_time.is_set or
                        self.preempt_flag.is_set or
                        self.primary_state.is_set or
                        self.primary_virtual_ip.is_set or
                        self.priority_decrement.is_set or
                        self.priority_zero_received_count.is_set or
                        self.priority_zero_sent_count.is_set or
                        self.reload_delay_time.is_set or
                        self.secondary_address_count.is_set or
                        self.session_name.is_set or
                        self.slaves.is_set or
                        self.state_change_count.is_set or
                        self.state_from_checkpoint.is_set or
                        self.time_in_current_state.is_set or
                        self.time_stats_discontinuity.is_set or
                        self.time_vrouter_up.is_set or
                        self.tracked_interface_count.is_set or
                        self.tracked_interface_up_count.is_set or
                        self.tracked_item_count.is_set or
                        self.tracked_item_up_count.is_set or
                        self.ttl_error_count.is_set or
                        self.version.is_set or
                        self.virtual_linklocal_ipv6_address.is_set or
                        self.virtual_mac_address.is_set or
                        self.virtual_mac_address_state.is_set or
                        self.virtual_router_id_xr.is_set or
                        self.vrrp_state.is_set or
                        (self.resign_received_time is not None and self.resign_received_time.has_data()) or
                        (self.resign_sent_time is not None and self.resign_sent_time.has_data()))

                def has_operation(self):
                    for c in self.ipv6_configured_down_address:
                        if (c.has_operation()):
                            return True
                    for c in self.ipv6_operational_address:
                        if (c.has_operation()):
                            return True
                    for c in self.state_change_history:
                        if (c.has_operation()):
                            return True
                    for leaf in self.ipv4_configured_down_address.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.operational_address.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.virtual_router_id.yfilter != YFilter.not_set or
                        self.address_family.yfilter != YFilter.not_set or
                        self.address_list_error_count.yfilter != YFilter.not_set or
                        self.advert_interval_error_count.yfilter != YFilter.not_set or
                        self.adverts_received_count.yfilter != YFilter.not_set or
                        self.adverts_sent_count.yfilter != YFilter.not_set or
                        self.auth_type_mismatch_count.yfilter != YFilter.not_set or
                        self.authentication_fail_count.yfilter != YFilter.not_set or
                        self.authentication_flag.yfilter != YFilter.not_set or
                        self.authentication_string.yfilter != YFilter.not_set or
                        self.authentication_type.yfilter != YFilter.not_set or
                        self.bfd_cfg_remote_ip.yfilter != YFilter.not_set or
                        self.bfd_configured_remote_ipv6_address.yfilter != YFilter.not_set or
                        self.bfd_interval.yfilter != YFilter.not_set or
                        self.bfd_multiplier.yfilter != YFilter.not_set or
                        self.bfd_session_state.yfilter != YFilter.not_set or
                        self.configured_advertize_time.yfilter != YFilter.not_set or
                        self.configured_down_address_count.yfilter != YFilter.not_set or
                        self.configured_priority.yfilter != YFilter.not_set or
                        self.delay_timer_flag.yfilter != YFilter.not_set or
                        self.delay_timer_msecs.yfilter != YFilter.not_set or
                        self.delay_timer_secs.yfilter != YFilter.not_set or
                        self.followed_session_name.yfilter != YFilter.not_set or
                        self.force_timer_flag.yfilter != YFilter.not_set or
                        self.interface_ipv4_address.yfilter != YFilter.not_set or
                        self.interface_ipv6_address.yfilter != YFilter.not_set or
                        self.interface_name_xr.yfilter != YFilter.not_set or
                        self.invalid_auth_type_count.yfilter != YFilter.not_set or
                        self.invalid_packet_count.yfilter != YFilter.not_set or
                        self.ip_address_owner_flag.yfilter != YFilter.not_set or
                        self.ipv4_configured_down_address.yfilter != YFilter.not_set or
                        self.is_accept_mode.yfilter != YFilter.not_set or
                        self.is_slave.yfilter != YFilter.not_set or
                        self.master_count.yfilter != YFilter.not_set or
                        self.master_ip_address.yfilter != YFilter.not_set or
                        self.master_ipv6_address.yfilter != YFilter.not_set or
                        self.master_priority.yfilter != YFilter.not_set or
                        self.min_delay_time.yfilter != YFilter.not_set or
                        self.oper_advertize_time.yfilter != YFilter.not_set or
                        self.operational_address.yfilter != YFilter.not_set or
                        self.operational_address_count.yfilter != YFilter.not_set or
                        self.operational_priority.yfilter != YFilter.not_set or
                        self.pkt_length_errors_count.yfilter != YFilter.not_set or
                        self.preempt_delay_time.yfilter != YFilter.not_set or
                        self.preempt_flag.yfilter != YFilter.not_set or
                        self.primary_state.yfilter != YFilter.not_set or
                        self.primary_virtual_ip.yfilter != YFilter.not_set or
                        self.priority_decrement.yfilter != YFilter.not_set or
                        self.priority_zero_received_count.yfilter != YFilter.not_set or
                        self.priority_zero_sent_count.yfilter != YFilter.not_set or
                        self.reload_delay_time.yfilter != YFilter.not_set or
                        self.secondary_address_count.yfilter != YFilter.not_set or
                        self.session_name.yfilter != YFilter.not_set or
                        self.slaves.yfilter != YFilter.not_set or
                        self.state_change_count.yfilter != YFilter.not_set or
                        self.state_from_checkpoint.yfilter != YFilter.not_set or
                        self.time_in_current_state.yfilter != YFilter.not_set or
                        self.time_stats_discontinuity.yfilter != YFilter.not_set or
                        self.time_vrouter_up.yfilter != YFilter.not_set or
                        self.tracked_interface_count.yfilter != YFilter.not_set or
                        self.tracked_interface_up_count.yfilter != YFilter.not_set or
                        self.tracked_item_count.yfilter != YFilter.not_set or
                        self.tracked_item_up_count.yfilter != YFilter.not_set or
                        self.ttl_error_count.yfilter != YFilter.not_set or
                        self.version.yfilter != YFilter.not_set or
                        self.virtual_linklocal_ipv6_address.yfilter != YFilter.not_set or
                        self.virtual_mac_address.yfilter != YFilter.not_set or
                        self.virtual_mac_address_state.yfilter != YFilter.not_set or
                        self.virtual_router_id_xr.yfilter != YFilter.not_set or
                        self.vrrp_state.yfilter != YFilter.not_set or
                        (self.resign_received_time is not None and self.resign_received_time.has_operation()) or
                        (self.resign_sent_time is not None and self.resign_sent_time.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "virtual-router" + "[interface-name='" + self.interface_name.get() + "']" + "[virtual-router-id='" + self.virtual_router_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/virtual-routers/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.virtual_router_id.is_set or self.virtual_router_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_router_id.get_name_leafdata())
                    if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_family.get_name_leafdata())
                    if (self.address_list_error_count.is_set or self.address_list_error_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_list_error_count.get_name_leafdata())
                    if (self.advert_interval_error_count.is_set or self.advert_interval_error_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.advert_interval_error_count.get_name_leafdata())
                    if (self.adverts_received_count.is_set or self.adverts_received_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.adverts_received_count.get_name_leafdata())
                    if (self.adverts_sent_count.is_set or self.adverts_sent_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.adverts_sent_count.get_name_leafdata())
                    if (self.auth_type_mismatch_count.is_set or self.auth_type_mismatch_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auth_type_mismatch_count.get_name_leafdata())
                    if (self.authentication_fail_count.is_set or self.authentication_fail_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_fail_count.get_name_leafdata())
                    if (self.authentication_flag.is_set or self.authentication_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_flag.get_name_leafdata())
                    if (self.authentication_string.is_set or self.authentication_string.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_string.get_name_leafdata())
                    if (self.authentication_type.is_set or self.authentication_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_type.get_name_leafdata())
                    if (self.bfd_cfg_remote_ip.is_set or self.bfd_cfg_remote_ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_cfg_remote_ip.get_name_leafdata())
                    if (self.bfd_configured_remote_ipv6_address.is_set or self.bfd_configured_remote_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_configured_remote_ipv6_address.get_name_leafdata())
                    if (self.bfd_interval.is_set or self.bfd_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_interval.get_name_leafdata())
                    if (self.bfd_multiplier.is_set or self.bfd_multiplier.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_multiplier.get_name_leafdata())
                    if (self.bfd_session_state.is_set or self.bfd_session_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_session_state.get_name_leafdata())
                    if (self.configured_advertize_time.is_set or self.configured_advertize_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_advertize_time.get_name_leafdata())
                    if (self.configured_down_address_count.is_set or self.configured_down_address_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_down_address_count.get_name_leafdata())
                    if (self.configured_priority.is_set or self.configured_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_priority.get_name_leafdata())
                    if (self.delay_timer_flag.is_set or self.delay_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_flag.get_name_leafdata())
                    if (self.delay_timer_msecs.is_set or self.delay_timer_msecs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_msecs.get_name_leafdata())
                    if (self.delay_timer_secs.is_set or self.delay_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_secs.get_name_leafdata())
                    if (self.followed_session_name.is_set or self.followed_session_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.followed_session_name.get_name_leafdata())
                    if (self.force_timer_flag.is_set or self.force_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.force_timer_flag.get_name_leafdata())
                    if (self.interface_ipv4_address.is_set or self.interface_ipv4_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_ipv4_address.get_name_leafdata())
                    if (self.interface_ipv6_address.is_set or self.interface_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_ipv6_address.get_name_leafdata())
                    if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                    if (self.invalid_auth_type_count.is_set or self.invalid_auth_type_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_auth_type_count.get_name_leafdata())
                    if (self.invalid_packet_count.is_set or self.invalid_packet_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_packet_count.get_name_leafdata())
                    if (self.ip_address_owner_flag.is_set or self.ip_address_owner_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_address_owner_flag.get_name_leafdata())
                    if (self.is_accept_mode.is_set or self.is_accept_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_accept_mode.get_name_leafdata())
                    if (self.is_slave.is_set or self.is_slave.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_slave.get_name_leafdata())
                    if (self.master_count.is_set or self.master_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.master_count.get_name_leafdata())
                    if (self.master_ip_address.is_set or self.master_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.master_ip_address.get_name_leafdata())
                    if (self.master_ipv6_address.is_set or self.master_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.master_ipv6_address.get_name_leafdata())
                    if (self.master_priority.is_set or self.master_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.master_priority.get_name_leafdata())
                    if (self.min_delay_time.is_set or self.min_delay_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.min_delay_time.get_name_leafdata())
                    if (self.oper_advertize_time.is_set or self.oper_advertize_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.oper_advertize_time.get_name_leafdata())
                    if (self.operational_address_count.is_set or self.operational_address_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operational_address_count.get_name_leafdata())
                    if (self.operational_priority.is_set or self.operational_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operational_priority.get_name_leafdata())
                    if (self.pkt_length_errors_count.is_set or self.pkt_length_errors_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pkt_length_errors_count.get_name_leafdata())
                    if (self.preempt_delay_time.is_set or self.preempt_delay_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.preempt_delay_time.get_name_leafdata())
                    if (self.preempt_flag.is_set or self.preempt_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.preempt_flag.get_name_leafdata())
                    if (self.primary_state.is_set or self.primary_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.primary_state.get_name_leafdata())
                    if (self.primary_virtual_ip.is_set or self.primary_virtual_ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.primary_virtual_ip.get_name_leafdata())
                    if (self.priority_decrement.is_set or self.priority_decrement.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority_decrement.get_name_leafdata())
                    if (self.priority_zero_received_count.is_set or self.priority_zero_received_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority_zero_received_count.get_name_leafdata())
                    if (self.priority_zero_sent_count.is_set or self.priority_zero_sent_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority_zero_sent_count.get_name_leafdata())
                    if (self.reload_delay_time.is_set or self.reload_delay_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reload_delay_time.get_name_leafdata())
                    if (self.secondary_address_count.is_set or self.secondary_address_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.secondary_address_count.get_name_leafdata())
                    if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_name.get_name_leafdata())
                    if (self.slaves.is_set or self.slaves.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.slaves.get_name_leafdata())
                    if (self.state_change_count.is_set or self.state_change_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state_change_count.get_name_leafdata())
                    if (self.state_from_checkpoint.is_set or self.state_from_checkpoint.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state_from_checkpoint.get_name_leafdata())
                    if (self.time_in_current_state.is_set or self.time_in_current_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time_in_current_state.get_name_leafdata())
                    if (self.time_stats_discontinuity.is_set or self.time_stats_discontinuity.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time_stats_discontinuity.get_name_leafdata())
                    if (self.time_vrouter_up.is_set or self.time_vrouter_up.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time_vrouter_up.get_name_leafdata())
                    if (self.tracked_interface_count.is_set or self.tracked_interface_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_count.get_name_leafdata())
                    if (self.tracked_interface_up_count.is_set or self.tracked_interface_up_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_up_count.get_name_leafdata())
                    if (self.tracked_item_count.is_set or self.tracked_item_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_item_count.get_name_leafdata())
                    if (self.tracked_item_up_count.is_set or self.tracked_item_up_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_item_up_count.get_name_leafdata())
                    if (self.ttl_error_count.is_set or self.ttl_error_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ttl_error_count.get_name_leafdata())
                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version.get_name_leafdata())
                    if (self.virtual_linklocal_ipv6_address.is_set or self.virtual_linklocal_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_linklocal_ipv6_address.get_name_leafdata())
                    if (self.virtual_mac_address.is_set or self.virtual_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_mac_address.get_name_leafdata())
                    if (self.virtual_mac_address_state.is_set or self.virtual_mac_address_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_mac_address_state.get_name_leafdata())
                    if (self.virtual_router_id_xr.is_set or self.virtual_router_id_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_router_id_xr.get_name_leafdata())
                    if (self.vrrp_state.is_set or self.vrrp_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrrp_state.get_name_leafdata())

                    leaf_name_data.extend(self.ipv4_configured_down_address.get_name_leafdata())

                    leaf_name_data.extend(self.operational_address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ipv6-configured-down-address"):
                        for c in self.ipv6_configured_down_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv6_configured_down_address.append(c)
                        return c

                    if (child_yang_name == "ipv6-operational-address"):
                        for c in self.ipv6_operational_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv6_operational_address.append(c)
                        return c

                    if (child_yang_name == "resign-received-time"):
                        if (self.resign_received_time is None):
                            self.resign_received_time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime()
                            self.resign_received_time.parent = self
                            self._children_name_map["resign_received_time"] = "resign-received-time"
                        return self.resign_received_time

                    if (child_yang_name == "resign-sent-time"):
                        if (self.resign_sent_time is None):
                            self.resign_sent_time = Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime()
                            self.resign_sent_time.parent = self
                            self._children_name_map["resign_sent_time"] = "resign-sent-time"
                        return self.resign_sent_time

                    if (child_yang_name == "state-change-history"):
                        for c in self.state_change_history:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.state_change_history.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv6-configured-down-address" or name == "ipv6-operational-address" or name == "resign-received-time" or name == "resign-sent-time" or name == "state-change-history" or name == "interface-name" or name == "virtual-router-id" or name == "address-family" or name == "address-list-error-count" or name == "advert-interval-error-count" or name == "adverts-received-count" or name == "adverts-sent-count" or name == "auth-type-mismatch-count" or name == "authentication-fail-count" or name == "authentication-flag" or name == "authentication-string" or name == "authentication-type" or name == "bfd-cfg-remote-ip" or name == "bfd-configured-remote-ipv6-address" or name == "bfd-interval" or name == "bfd-multiplier" or name == "bfd-session-state" or name == "configured-advertize-time" or name == "configured-down-address-count" or name == "configured-priority" or name == "delay-timer-flag" or name == "delay-timer-msecs" or name == "delay-timer-secs" or name == "followed-session-name" or name == "force-timer-flag" or name == "interface-ipv4-address" or name == "interface-ipv6-address" or name == "interface-name-xr" or name == "invalid-auth-type-count" or name == "invalid-packet-count" or name == "ip-address-owner-flag" or name == "ipv4-configured-down-address" or name == "is-accept-mode" or name == "is-slave" or name == "master-count" or name == "master-ip-address" or name == "master-ipv6-address" or name == "master-priority" or name == "min-delay-time" or name == "oper-advertize-time" or name == "operational-address" or name == "operational-address-count" or name == "operational-priority" or name == "pkt-length-errors-count" or name == "preempt-delay-time" or name == "preempt-flag" or name == "primary-state" or name == "primary-virtual-ip" or name == "priority-decrement" or name == "priority-zero-received-count" or name == "priority-zero-sent-count" or name == "reload-delay-time" or name == "secondary-address-count" or name == "session-name" or name == "slaves" or name == "state-change-count" or name == "state-from-checkpoint" or name == "time-in-current-state" or name == "time-stats-discontinuity" or name == "time-vrouter-up" or name == "tracked-interface-count" or name == "tracked-interface-up-count" or name == "tracked-item-count" or name == "tracked-item-up-count" or name == "ttl-error-count" or name == "version" or name == "virtual-linklocal-ipv6-address" or name == "virtual-mac-address" or name == "virtual-mac-address-state" or name == "virtual-router-id-xr" or name == "vrrp-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-router-id"):
                        self.virtual_router_id = value
                        self.virtual_router_id.value_namespace = name_space
                        self.virtual_router_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "address-family"):
                        self.address_family = value
                        self.address_family.value_namespace = name_space
                        self.address_family.value_namespace_prefix = name_space_prefix
                    if(value_path == "address-list-error-count"):
                        self.address_list_error_count = value
                        self.address_list_error_count.value_namespace = name_space
                        self.address_list_error_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "advert-interval-error-count"):
                        self.advert_interval_error_count = value
                        self.advert_interval_error_count.value_namespace = name_space
                        self.advert_interval_error_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "adverts-received-count"):
                        self.adverts_received_count = value
                        self.adverts_received_count.value_namespace = name_space
                        self.adverts_received_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "adverts-sent-count"):
                        self.adverts_sent_count = value
                        self.adverts_sent_count.value_namespace = name_space
                        self.adverts_sent_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "auth-type-mismatch-count"):
                        self.auth_type_mismatch_count = value
                        self.auth_type_mismatch_count.value_namespace = name_space
                        self.auth_type_mismatch_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-fail-count"):
                        self.authentication_fail_count = value
                        self.authentication_fail_count.value_namespace = name_space
                        self.authentication_fail_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-flag"):
                        self.authentication_flag = value
                        self.authentication_flag.value_namespace = name_space
                        self.authentication_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-string"):
                        self.authentication_string = value
                        self.authentication_string.value_namespace = name_space
                        self.authentication_string.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-type"):
                        self.authentication_type = value
                        self.authentication_type.value_namespace = name_space
                        self.authentication_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-cfg-remote-ip"):
                        self.bfd_cfg_remote_ip = value
                        self.bfd_cfg_remote_ip.value_namespace = name_space
                        self.bfd_cfg_remote_ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-configured-remote-ipv6-address"):
                        self.bfd_configured_remote_ipv6_address = value
                        self.bfd_configured_remote_ipv6_address.value_namespace = name_space
                        self.bfd_configured_remote_ipv6_address.value_namespace_prefix = name_space_prefix
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
                    if(value_path == "configured-advertize-time"):
                        self.configured_advertize_time = value
                        self.configured_advertize_time.value_namespace = name_space
                        self.configured_advertize_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "configured-down-address-count"):
                        self.configured_down_address_count = value
                        self.configured_down_address_count.value_namespace = name_space
                        self.configured_down_address_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "configured-priority"):
                        self.configured_priority = value
                        self.configured_priority.value_namespace = name_space
                        self.configured_priority.value_namespace_prefix = name_space_prefix
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
                    if(value_path == "force-timer-flag"):
                        self.force_timer_flag = value
                        self.force_timer_flag.value_namespace = name_space
                        self.force_timer_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-ipv4-address"):
                        self.interface_ipv4_address = value
                        self.interface_ipv4_address.value_namespace = name_space
                        self.interface_ipv4_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-ipv6-address"):
                        self.interface_ipv6_address = value
                        self.interface_ipv6_address.value_namespace = name_space
                        self.interface_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-name-xr"):
                        self.interface_name_xr = value
                        self.interface_name_xr.value_namespace = name_space
                        self.interface_name_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-auth-type-count"):
                        self.invalid_auth_type_count = value
                        self.invalid_auth_type_count.value_namespace = name_space
                        self.invalid_auth_type_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-packet-count"):
                        self.invalid_packet_count = value
                        self.invalid_packet_count.value_namespace = name_space
                        self.invalid_packet_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-address-owner-flag"):
                        self.ip_address_owner_flag = value
                        self.ip_address_owner_flag.value_namespace = name_space
                        self.ip_address_owner_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv4-configured-down-address"):
                        self.ipv4_configured_down_address.append(value)
                    if(value_path == "is-accept-mode"):
                        self.is_accept_mode = value
                        self.is_accept_mode.value_namespace = name_space
                        self.is_accept_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-slave"):
                        self.is_slave = value
                        self.is_slave.value_namespace = name_space
                        self.is_slave.value_namespace_prefix = name_space_prefix
                    if(value_path == "master-count"):
                        self.master_count = value
                        self.master_count.value_namespace = name_space
                        self.master_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "master-ip-address"):
                        self.master_ip_address = value
                        self.master_ip_address.value_namespace = name_space
                        self.master_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "master-ipv6-address"):
                        self.master_ipv6_address = value
                        self.master_ipv6_address.value_namespace = name_space
                        self.master_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "master-priority"):
                        self.master_priority = value
                        self.master_priority.value_namespace = name_space
                        self.master_priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "min-delay-time"):
                        self.min_delay_time = value
                        self.min_delay_time.value_namespace = name_space
                        self.min_delay_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "oper-advertize-time"):
                        self.oper_advertize_time = value
                        self.oper_advertize_time.value_namespace = name_space
                        self.oper_advertize_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "operational-address"):
                        self.operational_address.append(value)
                    if(value_path == "operational-address-count"):
                        self.operational_address_count = value
                        self.operational_address_count.value_namespace = name_space
                        self.operational_address_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "operational-priority"):
                        self.operational_priority = value
                        self.operational_priority.value_namespace = name_space
                        self.operational_priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "pkt-length-errors-count"):
                        self.pkt_length_errors_count = value
                        self.pkt_length_errors_count.value_namespace = name_space
                        self.pkt_length_errors_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "preempt-delay-time"):
                        self.preempt_delay_time = value
                        self.preempt_delay_time.value_namespace = name_space
                        self.preempt_delay_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "preempt-flag"):
                        self.preempt_flag = value
                        self.preempt_flag.value_namespace = name_space
                        self.preempt_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "primary-state"):
                        self.primary_state = value
                        self.primary_state.value_namespace = name_space
                        self.primary_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "primary-virtual-ip"):
                        self.primary_virtual_ip = value
                        self.primary_virtual_ip.value_namespace = name_space
                        self.primary_virtual_ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority-decrement"):
                        self.priority_decrement = value
                        self.priority_decrement.value_namespace = name_space
                        self.priority_decrement.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority-zero-received-count"):
                        self.priority_zero_received_count = value
                        self.priority_zero_received_count.value_namespace = name_space
                        self.priority_zero_received_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority-zero-sent-count"):
                        self.priority_zero_sent_count = value
                        self.priority_zero_sent_count.value_namespace = name_space
                        self.priority_zero_sent_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "reload-delay-time"):
                        self.reload_delay_time = value
                        self.reload_delay_time.value_namespace = name_space
                        self.reload_delay_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "secondary-address-count"):
                        self.secondary_address_count = value
                        self.secondary_address_count.value_namespace = name_space
                        self.secondary_address_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "session-name"):
                        self.session_name = value
                        self.session_name.value_namespace = name_space
                        self.session_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "slaves"):
                        self.slaves = value
                        self.slaves.value_namespace = name_space
                        self.slaves.value_namespace_prefix = name_space_prefix
                    if(value_path == "state-change-count"):
                        self.state_change_count = value
                        self.state_change_count.value_namespace = name_space
                        self.state_change_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "state-from-checkpoint"):
                        self.state_from_checkpoint = value
                        self.state_from_checkpoint.value_namespace = name_space
                        self.state_from_checkpoint.value_namespace_prefix = name_space_prefix
                    if(value_path == "time-in-current-state"):
                        self.time_in_current_state = value
                        self.time_in_current_state.value_namespace = name_space
                        self.time_in_current_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "time-stats-discontinuity"):
                        self.time_stats_discontinuity = value
                        self.time_stats_discontinuity.value_namespace = name_space
                        self.time_stats_discontinuity.value_namespace_prefix = name_space_prefix
                    if(value_path == "time-vrouter-up"):
                        self.time_vrouter_up = value
                        self.time_vrouter_up.value_namespace = name_space
                        self.time_vrouter_up.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-count"):
                        self.tracked_interface_count = value
                        self.tracked_interface_count.value_namespace = name_space
                        self.tracked_interface_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-up-count"):
                        self.tracked_interface_up_count = value
                        self.tracked_interface_up_count.value_namespace = name_space
                        self.tracked_interface_up_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-item-count"):
                        self.tracked_item_count = value
                        self.tracked_item_count.value_namespace = name_space
                        self.tracked_item_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-item-up-count"):
                        self.tracked_item_up_count = value
                        self.tracked_item_up_count.value_namespace = name_space
                        self.tracked_item_up_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "ttl-error-count"):
                        self.ttl_error_count = value
                        self.ttl_error_count.value_namespace = name_space
                        self.ttl_error_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "version"):
                        self.version = value
                        self.version.value_namespace = name_space
                        self.version.value_namespace_prefix = name_space_prefix
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
                    if(value_path == "virtual-router-id-xr"):
                        self.virtual_router_id_xr = value
                        self.virtual_router_id_xr.value_namespace = name_space
                        self.virtual_router_id_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrrp-state"):
                        self.vrrp_state = value
                        self.vrrp_state.value_namespace = name_space
                        self.vrrp_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.virtual_router:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.virtual_router:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "virtual-routers" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "virtual-router"):
                    for c in self.virtual_router:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Vrrp.Ipv6.VirtualRouters.VirtualRouter()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.virtual_router.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "virtual-router"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Interfaces(Entity):
            """
            The VRRP interface table
            
            .. attribute:: interface
            
            	A VRRP interface entry
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv6.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                super(Vrrp.Ipv6.Interfaces, self).__init__()

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
                            super(Vrrp.Ipv6.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vrrp.Ipv6.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
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
                    super(Vrrp.Ipv6.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface = YLeaf(YType.str, "interface")

                    self.invalid_checksum_count = YLeaf(YType.uint32, "invalid-checksum-count")

                    self.invalid_packet_length_count = YLeaf(YType.uint32, "invalid-packet-length-count")

                    self.invalid_version_count = YLeaf(YType.uint32, "invalid-version-count")

                    self.invalid_vrid_count = YLeaf(YType.uint32, "invalid-vrid-count")

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
                                    "invalid_checksum_count",
                                    "invalid_packet_length_count",
                                    "invalid_version_count",
                                    "invalid_vrid_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrrp.Ipv6.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrrp.Ipv6.Interfaces.Interface, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.interface.is_set or
                        self.invalid_checksum_count.is_set or
                        self.invalid_packet_length_count.is_set or
                        self.invalid_version_count.is_set or
                        self.invalid_vrid_count.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.invalid_checksum_count.yfilter != YFilter.not_set or
                        self.invalid_packet_length_count.yfilter != YFilter.not_set or
                        self.invalid_version_count.yfilter != YFilter.not_set or
                        self.invalid_vrid_count.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.invalid_checksum_count.is_set or self.invalid_checksum_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_checksum_count.get_name_leafdata())
                    if (self.invalid_packet_length_count.is_set or self.invalid_packet_length_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_packet_length_count.get_name_leafdata())
                    if (self.invalid_version_count.is_set or self.invalid_version_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_version_count.get_name_leafdata())
                    if (self.invalid_vrid_count.is_set or self.invalid_vrid_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_vrid_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "interface" or name == "invalid-checksum-count" or name == "invalid-packet-length-count" or name == "invalid-version-count" or name == "invalid-vrid-count"):
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
                    if(value_path == "invalid-checksum-count"):
                        self.invalid_checksum_count = value
                        self.invalid_checksum_count.value_namespace = name_space
                        self.invalid_checksum_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-packet-length-count"):
                        self.invalid_packet_length_count = value
                        self.invalid_packet_length_count.value_namespace = name_space
                        self.invalid_packet_length_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-version-count"):
                        self.invalid_version_count = value
                        self.invalid_version_count.value_namespace = name_space
                        self.invalid_version_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-vrid-count"):
                        self.invalid_vrid_count = value
                        self.invalid_vrid_count.value_namespace = name_space
                        self.invalid_vrid_count.value_namespace_prefix = name_space_prefix

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
                    path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv6/%s" % self.get_segment_path()
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
                    c = Vrrp.Ipv6.Interfaces.Interface()
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
                (self.interfaces is not None and self.interfaces.has_data()) or
                (self.track_items is not None and self.track_items.has_data()) or
                (self.virtual_routers is not None and self.virtual_routers.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.interfaces is not None and self.interfaces.has_operation()) or
                (self.track_items is not None and self.track_items.has_operation()) or
                (self.virtual_routers is not None and self.virtual_routers.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv6" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = Vrrp.Ipv6.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            if (child_yang_name == "track-items"):
                if (self.track_items is None):
                    self.track_items = Vrrp.Ipv6.TrackItems()
                    self.track_items.parent = self
                    self._children_name_map["track_items"] = "track-items"
                return self.track_items

            if (child_yang_name == "virtual-routers"):
                if (self.virtual_routers is None):
                    self.virtual_routers = Vrrp.Ipv6.VirtualRouters()
                    self.virtual_routers.parent = self
                    self._children_name_map["virtual_routers"] = "virtual-routers"
                return self.virtual_routers

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interfaces" or name == "track-items" or name == "virtual-routers"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipv4(Entity):
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
            super(Vrrp.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "vrrp"

            self.interfaces = Vrrp.Ipv4.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.track_items = Vrrp.Ipv4.TrackItems()
            self.track_items.parent = self
            self._children_name_map["track_items"] = "track-items"
            self._children_yang_names.add("track-items")

            self.virtual_routers = Vrrp.Ipv4.VirtualRouters()
            self.virtual_routers.parent = self
            self._children_name_map["virtual_routers"] = "virtual-routers"
            self._children_yang_names.add("virtual-routers")


        class Interfaces(Entity):
            """
            The VRRP interface table
            
            .. attribute:: interface
            
            	A VRRP interface entry
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                super(Vrrp.Ipv4.Interfaces, self).__init__()

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
                            super(Vrrp.Ipv4.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vrrp.Ipv4.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
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
                    super(Vrrp.Ipv4.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface = YLeaf(YType.str, "interface")

                    self.invalid_checksum_count = YLeaf(YType.uint32, "invalid-checksum-count")

                    self.invalid_packet_length_count = YLeaf(YType.uint32, "invalid-packet-length-count")

                    self.invalid_version_count = YLeaf(YType.uint32, "invalid-version-count")

                    self.invalid_vrid_count = YLeaf(YType.uint32, "invalid-vrid-count")

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
                                    "invalid_checksum_count",
                                    "invalid_packet_length_count",
                                    "invalid_version_count",
                                    "invalid_vrid_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrrp.Ipv4.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrrp.Ipv4.Interfaces.Interface, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.interface.is_set or
                        self.invalid_checksum_count.is_set or
                        self.invalid_packet_length_count.is_set or
                        self.invalid_version_count.is_set or
                        self.invalid_vrid_count.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.invalid_checksum_count.yfilter != YFilter.not_set or
                        self.invalid_packet_length_count.yfilter != YFilter.not_set or
                        self.invalid_version_count.yfilter != YFilter.not_set or
                        self.invalid_vrid_count.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.invalid_checksum_count.is_set or self.invalid_checksum_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_checksum_count.get_name_leafdata())
                    if (self.invalid_packet_length_count.is_set or self.invalid_packet_length_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_packet_length_count.get_name_leafdata())
                    if (self.invalid_version_count.is_set or self.invalid_version_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_version_count.get_name_leafdata())
                    if (self.invalid_vrid_count.is_set or self.invalid_vrid_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_vrid_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "interface" or name == "invalid-checksum-count" or name == "invalid-packet-length-count" or name == "invalid-version-count" or name == "invalid-vrid-count"):
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
                    if(value_path == "invalid-checksum-count"):
                        self.invalid_checksum_count = value
                        self.invalid_checksum_count.value_namespace = name_space
                        self.invalid_checksum_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-packet-length-count"):
                        self.invalid_packet_length_count = value
                        self.invalid_packet_length_count.value_namespace = name_space
                        self.invalid_packet_length_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-version-count"):
                        self.invalid_version_count = value
                        self.invalid_version_count.value_namespace = name_space
                        self.invalid_version_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-vrid-count"):
                        self.invalid_vrid_count = value
                        self.invalid_vrid_count.value_namespace = name_space
                        self.invalid_vrid_count.value_namespace_prefix = name_space_prefix

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
                    path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/%s" % self.get_segment_path()
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
                    c = Vrrp.Ipv4.Interfaces.Interface()
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


        class TrackItems(Entity):
            """
            The VRRP tracked item table
            
            .. attribute:: track_item
            
            	A configured VRRP IP address entry
            	**type**\: list of    :py:class:`TrackItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.TrackItems.TrackItem>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                super(Vrrp.Ipv4.TrackItems, self).__init__()

                self.yang_name = "track-items"
                self.yang_parent_name = "ipv4"

                self.track_item = YList(self)

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
                            super(Vrrp.Ipv4.TrackItems, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vrrp.Ipv4.TrackItems, self).__setattr__(name, value)


            class TrackItem(Entity):
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
                    super(Vrrp.Ipv4.TrackItems.TrackItem, self).__init__()

                    self.yang_name = "track-item"
                    self.yang_parent_name = "track-items"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.virtual_router_id = YLeaf(YType.int32, "virtual-router-id")

                    self.tracked_interface_name = YLeaf(YType.str, "tracked-interface-name")

                    self.interface = YLeaf(YType.str, "interface")

                    self.priority = YLeaf(YType.uint8, "priority")

                    self.state = YLeaf(YType.uint8, "state")

                    self.tracked_item_index = YLeaf(YType.str, "tracked-item-index")

                    self.tracked_item_type = YLeaf(YType.uint16, "tracked-item-type")

                    self.virtual_router_id_xr = YLeaf(YType.uint32, "virtual-router-id-xr")

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
                                    "virtual_router_id",
                                    "tracked_interface_name",
                                    "interface",
                                    "priority",
                                    "state",
                                    "tracked_item_index",
                                    "tracked_item_type",
                                    "virtual_router_id_xr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrrp.Ipv4.TrackItems.TrackItem, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrrp.Ipv4.TrackItems.TrackItem, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.virtual_router_id.is_set or
                        self.tracked_interface_name.is_set or
                        self.interface.is_set or
                        self.priority.is_set or
                        self.state.is_set or
                        self.tracked_item_index.is_set or
                        self.tracked_item_type.is_set or
                        self.virtual_router_id_xr.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.virtual_router_id.yfilter != YFilter.not_set or
                        self.tracked_interface_name.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.priority.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.tracked_item_index.yfilter != YFilter.not_set or
                        self.tracked_item_type.yfilter != YFilter.not_set or
                        self.virtual_router_id_xr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "track-item" + "[interface-name='" + self.interface_name.get() + "']" + "[virtual-router-id='" + self.virtual_router_id.get() + "']" + "[tracked-interface-name='" + self.tracked_interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/track-items/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.virtual_router_id.is_set or self.virtual_router_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_router_id.get_name_leafdata())
                    if (self.tracked_interface_name.is_set or self.tracked_interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_name.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.tracked_item_index.is_set or self.tracked_item_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_item_index.get_name_leafdata())
                    if (self.tracked_item_type.is_set or self.tracked_item_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_item_type.get_name_leafdata())
                    if (self.virtual_router_id_xr.is_set or self.virtual_router_id_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_router_id_xr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "virtual-router-id" or name == "tracked-interface-name" or name == "interface" or name == "priority" or name == "state" or name == "tracked-item-index" or name == "tracked-item-type" or name == "virtual-router-id-xr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-router-id"):
                        self.virtual_router_id = value
                        self.virtual_router_id.value_namespace = name_space
                        self.virtual_router_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-name"):
                        self.tracked_interface_name = value
                        self.tracked_interface_name.value_namespace = name_space
                        self.tracked_interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority"):
                        self.priority = value
                        self.priority.value_namespace = name_space
                        self.priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-item-index"):
                        self.tracked_item_index = value
                        self.tracked_item_index.value_namespace = name_space
                        self.tracked_item_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-item-type"):
                        self.tracked_item_type = value
                        self.tracked_item_type.value_namespace = name_space
                        self.tracked_item_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-router-id-xr"):
                        self.virtual_router_id_xr = value
                        self.virtual_router_id_xr.value_namespace = name_space
                        self.virtual_router_id_xr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.track_item:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.track_item:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "track-items" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "track-item"):
                    for c in self.track_item:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Vrrp.Ipv4.TrackItems.TrackItem()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.track_item.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "track-item"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class VirtualRouters(Entity):
            """
            The VRRP virtual router table
            
            .. attribute:: virtual_router
            
            	A VRRP virtual router
            	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                super(Vrrp.Ipv4.VirtualRouters, self).__init__()

                self.yang_name = "virtual-routers"
                self.yang_parent_name = "ipv4"

                self.virtual_router = YList(self)

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
                            super(Vrrp.Ipv4.VirtualRouters, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vrrp.Ipv4.VirtualRouters, self).__setattr__(name, value)


            class VirtualRouter(Entity):
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
                	**type**\:   :py:class:`VrrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBAf>`
                
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
                	**type**\:   :py:class:`VrrpProtAuth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpProtAuth>`
                
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
                	**type**\:   :py:class:`VrrpBfdSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBfdSessionState>`
                
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
                	**type**\:   :py:class:`VrrpVipState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVipState>`
                
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
                	**type**\:   :py:class:`VrrpVmacState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpVmacState>`
                
                .. attribute:: virtual_router_id_xr
                
                	Virtual Router ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrrp_state
                
                	VRRP state
                	**type**\:   :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                
                

                """

                _prefix = 'ipv4-vrrp-oper'
                _revision = '2016-12-16'

                def __init__(self):
                    super(Vrrp.Ipv4.VirtualRouters.VirtualRouter, self).__init__()

                    self.yang_name = "virtual-router"
                    self.yang_parent_name = "virtual-routers"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.virtual_router_id = YLeaf(YType.int32, "virtual-router-id")

                    self.address_family = YLeaf(YType.enumeration, "address-family")

                    self.address_list_error_count = YLeaf(YType.uint32, "address-list-error-count")

                    self.advert_interval_error_count = YLeaf(YType.uint32, "advert-interval-error-count")

                    self.adverts_received_count = YLeaf(YType.uint32, "adverts-received-count")

                    self.adverts_sent_count = YLeaf(YType.uint32, "adverts-sent-count")

                    self.auth_type_mismatch_count = YLeaf(YType.uint32, "auth-type-mismatch-count")

                    self.authentication_fail_count = YLeaf(YType.uint32, "authentication-fail-count")

                    self.authentication_flag = YLeaf(YType.boolean, "authentication-flag")

                    self.authentication_string = YLeaf(YType.str, "authentication-string")

                    self.authentication_type = YLeaf(YType.enumeration, "authentication-type")

                    self.bfd_cfg_remote_ip = YLeaf(YType.str, "bfd-cfg-remote-ip")

                    self.bfd_configured_remote_ipv6_address = YLeaf(YType.str, "bfd-configured-remote-ipv6-address")

                    self.bfd_interval = YLeaf(YType.uint32, "bfd-interval")

                    self.bfd_multiplier = YLeaf(YType.uint32, "bfd-multiplier")

                    self.bfd_session_state = YLeaf(YType.enumeration, "bfd-session-state")

                    self.configured_advertize_time = YLeaf(YType.uint32, "configured-advertize-time")

                    self.configured_down_address_count = YLeaf(YType.uint8, "configured-down-address-count")

                    self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                    self.delay_timer_flag = YLeaf(YType.boolean, "delay-timer-flag")

                    self.delay_timer_msecs = YLeaf(YType.uint32, "delay-timer-msecs")

                    self.delay_timer_secs = YLeaf(YType.uint32, "delay-timer-secs")

                    self.followed_session_name = YLeaf(YType.str, "followed-session-name")

                    self.force_timer_flag = YLeaf(YType.boolean, "force-timer-flag")

                    self.interface_ipv4_address = YLeaf(YType.str, "interface-ipv4-address")

                    self.interface_ipv6_address = YLeaf(YType.str, "interface-ipv6-address")

                    self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                    self.invalid_auth_type_count = YLeaf(YType.uint32, "invalid-auth-type-count")

                    self.invalid_packet_count = YLeaf(YType.uint32, "invalid-packet-count")

                    self.ip_address_owner_flag = YLeaf(YType.boolean, "ip-address-owner-flag")

                    self.ipv4_configured_down_address = YLeafList(YType.str, "ipv4-configured-down-address")

                    self.is_accept_mode = YLeaf(YType.boolean, "is-accept-mode")

                    self.is_slave = YLeaf(YType.boolean, "is-slave")

                    self.master_count = YLeaf(YType.uint32, "master-count")

                    self.master_ip_address = YLeaf(YType.str, "master-ip-address")

                    self.master_ipv6_address = YLeaf(YType.str, "master-ipv6-address")

                    self.master_priority = YLeaf(YType.uint8, "master-priority")

                    self.min_delay_time = YLeaf(YType.uint32, "min-delay-time")

                    self.oper_advertize_time = YLeaf(YType.uint32, "oper-advertize-time")

                    self.operational_address = YLeafList(YType.str, "operational-address")

                    self.operational_address_count = YLeaf(YType.uint8, "operational-address-count")

                    self.operational_priority = YLeaf(YType.uint8, "operational-priority")

                    self.pkt_length_errors_count = YLeaf(YType.uint32, "pkt-length-errors-count")

                    self.preempt_delay_time = YLeaf(YType.uint16, "preempt-delay-time")

                    self.preempt_flag = YLeaf(YType.boolean, "preempt-flag")

                    self.primary_state = YLeaf(YType.enumeration, "primary-state")

                    self.primary_virtual_ip = YLeaf(YType.str, "primary-virtual-ip")

                    self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")

                    self.priority_zero_received_count = YLeaf(YType.uint32, "priority-zero-received-count")

                    self.priority_zero_sent_count = YLeaf(YType.uint32, "priority-zero-sent-count")

                    self.reload_delay_time = YLeaf(YType.uint32, "reload-delay-time")

                    self.secondary_address_count = YLeaf(YType.uint8, "secondary-address-count")

                    self.session_name = YLeaf(YType.str, "session-name")

                    self.slaves = YLeaf(YType.uint32, "slaves")

                    self.state_change_count = YLeaf(YType.uint32, "state-change-count")

                    self.state_from_checkpoint = YLeaf(YType.boolean, "state-from-checkpoint")

                    self.time_in_current_state = YLeaf(YType.uint32, "time-in-current-state")

                    self.time_stats_discontinuity = YLeaf(YType.uint32, "time-stats-discontinuity")

                    self.time_vrouter_up = YLeaf(YType.uint32, "time-vrouter-up")

                    self.tracked_interface_count = YLeaf(YType.uint32, "tracked-interface-count")

                    self.tracked_interface_up_count = YLeaf(YType.uint32, "tracked-interface-up-count")

                    self.tracked_item_count = YLeaf(YType.uint32, "tracked-item-count")

                    self.tracked_item_up_count = YLeaf(YType.uint32, "tracked-item-up-count")

                    self.ttl_error_count = YLeaf(YType.uint32, "ttl-error-count")

                    self.version = YLeaf(YType.uint8, "version")

                    self.virtual_linklocal_ipv6_address = YLeaf(YType.str, "virtual-linklocal-ipv6-address")

                    self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                    self.virtual_mac_address_state = YLeaf(YType.enumeration, "virtual-mac-address-state")

                    self.virtual_router_id_xr = YLeaf(YType.uint32, "virtual-router-id-xr")

                    self.vrrp_state = YLeaf(YType.enumeration, "vrrp-state")

                    self.resign_received_time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self._children_name_map["resign_received_time"] = "resign-received-time"
                    self._children_yang_names.add("resign-received-time")

                    self.resign_sent_time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self._children_name_map["resign_sent_time"] = "resign-sent-time"
                    self._children_yang_names.add("resign-sent-time")

                    self.ipv6_configured_down_address = YList(self)
                    self.ipv6_operational_address = YList(self)
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
                                    "virtual_router_id",
                                    "address_family",
                                    "address_list_error_count",
                                    "advert_interval_error_count",
                                    "adverts_received_count",
                                    "adverts_sent_count",
                                    "auth_type_mismatch_count",
                                    "authentication_fail_count",
                                    "authentication_flag",
                                    "authentication_string",
                                    "authentication_type",
                                    "bfd_cfg_remote_ip",
                                    "bfd_configured_remote_ipv6_address",
                                    "bfd_interval",
                                    "bfd_multiplier",
                                    "bfd_session_state",
                                    "configured_advertize_time",
                                    "configured_down_address_count",
                                    "configured_priority",
                                    "delay_timer_flag",
                                    "delay_timer_msecs",
                                    "delay_timer_secs",
                                    "followed_session_name",
                                    "force_timer_flag",
                                    "interface_ipv4_address",
                                    "interface_ipv6_address",
                                    "interface_name_xr",
                                    "invalid_auth_type_count",
                                    "invalid_packet_count",
                                    "ip_address_owner_flag",
                                    "ipv4_configured_down_address",
                                    "is_accept_mode",
                                    "is_slave",
                                    "master_count",
                                    "master_ip_address",
                                    "master_ipv6_address",
                                    "master_priority",
                                    "min_delay_time",
                                    "oper_advertize_time",
                                    "operational_address",
                                    "operational_address_count",
                                    "operational_priority",
                                    "pkt_length_errors_count",
                                    "preempt_delay_time",
                                    "preempt_flag",
                                    "primary_state",
                                    "primary_virtual_ip",
                                    "priority_decrement",
                                    "priority_zero_received_count",
                                    "priority_zero_sent_count",
                                    "reload_delay_time",
                                    "secondary_address_count",
                                    "session_name",
                                    "slaves",
                                    "state_change_count",
                                    "state_from_checkpoint",
                                    "time_in_current_state",
                                    "time_stats_discontinuity",
                                    "time_vrouter_up",
                                    "tracked_interface_count",
                                    "tracked_interface_up_count",
                                    "tracked_item_count",
                                    "tracked_item_up_count",
                                    "ttl_error_count",
                                    "version",
                                    "virtual_linklocal_ipv6_address",
                                    "virtual_mac_address",
                                    "virtual_mac_address_state",
                                    "virtual_router_id_xr",
                                    "vrrp_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrrp.Ipv4.VirtualRouters.VirtualRouter, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrrp.Ipv4.VirtualRouters.VirtualRouter, self).__setattr__(name, value)


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

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime, self).__init__()

                        self.yang_name = "resign-sent-time"
                        self.yang_parent_name = "virtual-router"

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
                                    super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime, self).__setattr__(name, value)

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

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime, self).__init__()

                        self.yang_name = "resign-received-time"
                        self.yang_parent_name = "virtual-router"

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
                                    super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime, self).__setattr__(name, value)

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


                class Ipv6OperationalAddress(Entity):
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
                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress, self).__init__()

                        self.yang_name = "ipv6-operational-address"
                        self.yang_parent_name = "virtual-router"

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
                                    super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress, self).__setattr__(name, value)

                    def has_data(self):
                        return self.ipv6_address.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipv6_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6-operational-address" + path_buffer

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


                class Ipv6ConfiguredDownAddress(Entity):
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
                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress, self).__init__()

                        self.yang_name = "ipv6-configured-down-address"
                        self.yang_parent_name = "virtual-router"

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
                                    super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress, self).__setattr__(name, value)

                    def has_data(self):
                        return self.ipv6_address.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipv6_address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6-configured-down-address" + path_buffer

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
                    	**type**\:   :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:   :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:   :py:class:`VrrpStateChangeReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpStateChangeReason>`
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:   :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-oper'
                    _revision = '2016-12-16'

                    def __init__(self):
                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory, self).__init__()

                        self.yang_name = "state-change-history"
                        self.yang_parent_name = "virtual-router"

                        self.new_state = YLeaf(YType.enumeration, "new-state")

                        self.old_state = YLeaf(YType.enumeration, "old-state")

                        self.reason = YLeaf(YType.enumeration, "reason")

                        self.time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time()
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
                                    super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory, self).__setattr__(name, value)


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

                        _prefix = 'ipv4-vrrp-oper'
                        _revision = '2016-12-16'

                        def __init__(self):
                            super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time, self).__init__()

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
                                        super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time, self).__setattr__(name, value)

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
                                self.time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time()
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
                    for c in self.ipv6_configured_down_address:
                        if (c.has_data()):
                            return True
                    for c in self.ipv6_operational_address:
                        if (c.has_data()):
                            return True
                    for c in self.state_change_history:
                        if (c.has_data()):
                            return True
                    for leaf in self.ipv4_configured_down_address.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.operational_address.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.interface_name.is_set or
                        self.virtual_router_id.is_set or
                        self.address_family.is_set or
                        self.address_list_error_count.is_set or
                        self.advert_interval_error_count.is_set or
                        self.adverts_received_count.is_set or
                        self.adverts_sent_count.is_set or
                        self.auth_type_mismatch_count.is_set or
                        self.authentication_fail_count.is_set or
                        self.authentication_flag.is_set or
                        self.authentication_string.is_set or
                        self.authentication_type.is_set or
                        self.bfd_cfg_remote_ip.is_set or
                        self.bfd_configured_remote_ipv6_address.is_set or
                        self.bfd_interval.is_set or
                        self.bfd_multiplier.is_set or
                        self.bfd_session_state.is_set or
                        self.configured_advertize_time.is_set or
                        self.configured_down_address_count.is_set or
                        self.configured_priority.is_set or
                        self.delay_timer_flag.is_set or
                        self.delay_timer_msecs.is_set or
                        self.delay_timer_secs.is_set or
                        self.followed_session_name.is_set or
                        self.force_timer_flag.is_set or
                        self.interface_ipv4_address.is_set or
                        self.interface_ipv6_address.is_set or
                        self.interface_name_xr.is_set or
                        self.invalid_auth_type_count.is_set or
                        self.invalid_packet_count.is_set or
                        self.ip_address_owner_flag.is_set or
                        self.is_accept_mode.is_set or
                        self.is_slave.is_set or
                        self.master_count.is_set or
                        self.master_ip_address.is_set or
                        self.master_ipv6_address.is_set or
                        self.master_priority.is_set or
                        self.min_delay_time.is_set or
                        self.oper_advertize_time.is_set or
                        self.operational_address_count.is_set or
                        self.operational_priority.is_set or
                        self.pkt_length_errors_count.is_set or
                        self.preempt_delay_time.is_set or
                        self.preempt_flag.is_set or
                        self.primary_state.is_set or
                        self.primary_virtual_ip.is_set or
                        self.priority_decrement.is_set or
                        self.priority_zero_received_count.is_set or
                        self.priority_zero_sent_count.is_set or
                        self.reload_delay_time.is_set or
                        self.secondary_address_count.is_set or
                        self.session_name.is_set or
                        self.slaves.is_set or
                        self.state_change_count.is_set or
                        self.state_from_checkpoint.is_set or
                        self.time_in_current_state.is_set or
                        self.time_stats_discontinuity.is_set or
                        self.time_vrouter_up.is_set or
                        self.tracked_interface_count.is_set or
                        self.tracked_interface_up_count.is_set or
                        self.tracked_item_count.is_set or
                        self.tracked_item_up_count.is_set or
                        self.ttl_error_count.is_set or
                        self.version.is_set or
                        self.virtual_linklocal_ipv6_address.is_set or
                        self.virtual_mac_address.is_set or
                        self.virtual_mac_address_state.is_set or
                        self.virtual_router_id_xr.is_set or
                        self.vrrp_state.is_set or
                        (self.resign_received_time is not None and self.resign_received_time.has_data()) or
                        (self.resign_sent_time is not None and self.resign_sent_time.has_data()))

                def has_operation(self):
                    for c in self.ipv6_configured_down_address:
                        if (c.has_operation()):
                            return True
                    for c in self.ipv6_operational_address:
                        if (c.has_operation()):
                            return True
                    for c in self.state_change_history:
                        if (c.has_operation()):
                            return True
                    for leaf in self.ipv4_configured_down_address.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.operational_address.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.virtual_router_id.yfilter != YFilter.not_set or
                        self.address_family.yfilter != YFilter.not_set or
                        self.address_list_error_count.yfilter != YFilter.not_set or
                        self.advert_interval_error_count.yfilter != YFilter.not_set or
                        self.adverts_received_count.yfilter != YFilter.not_set or
                        self.adverts_sent_count.yfilter != YFilter.not_set or
                        self.auth_type_mismatch_count.yfilter != YFilter.not_set or
                        self.authentication_fail_count.yfilter != YFilter.not_set or
                        self.authentication_flag.yfilter != YFilter.not_set or
                        self.authentication_string.yfilter != YFilter.not_set or
                        self.authentication_type.yfilter != YFilter.not_set or
                        self.bfd_cfg_remote_ip.yfilter != YFilter.not_set or
                        self.bfd_configured_remote_ipv6_address.yfilter != YFilter.not_set or
                        self.bfd_interval.yfilter != YFilter.not_set or
                        self.bfd_multiplier.yfilter != YFilter.not_set or
                        self.bfd_session_state.yfilter != YFilter.not_set or
                        self.configured_advertize_time.yfilter != YFilter.not_set or
                        self.configured_down_address_count.yfilter != YFilter.not_set or
                        self.configured_priority.yfilter != YFilter.not_set or
                        self.delay_timer_flag.yfilter != YFilter.not_set or
                        self.delay_timer_msecs.yfilter != YFilter.not_set or
                        self.delay_timer_secs.yfilter != YFilter.not_set or
                        self.followed_session_name.yfilter != YFilter.not_set or
                        self.force_timer_flag.yfilter != YFilter.not_set or
                        self.interface_ipv4_address.yfilter != YFilter.not_set or
                        self.interface_ipv6_address.yfilter != YFilter.not_set or
                        self.interface_name_xr.yfilter != YFilter.not_set or
                        self.invalid_auth_type_count.yfilter != YFilter.not_set or
                        self.invalid_packet_count.yfilter != YFilter.not_set or
                        self.ip_address_owner_flag.yfilter != YFilter.not_set or
                        self.ipv4_configured_down_address.yfilter != YFilter.not_set or
                        self.is_accept_mode.yfilter != YFilter.not_set or
                        self.is_slave.yfilter != YFilter.not_set or
                        self.master_count.yfilter != YFilter.not_set or
                        self.master_ip_address.yfilter != YFilter.not_set or
                        self.master_ipv6_address.yfilter != YFilter.not_set or
                        self.master_priority.yfilter != YFilter.not_set or
                        self.min_delay_time.yfilter != YFilter.not_set or
                        self.oper_advertize_time.yfilter != YFilter.not_set or
                        self.operational_address.yfilter != YFilter.not_set or
                        self.operational_address_count.yfilter != YFilter.not_set or
                        self.operational_priority.yfilter != YFilter.not_set or
                        self.pkt_length_errors_count.yfilter != YFilter.not_set or
                        self.preempt_delay_time.yfilter != YFilter.not_set or
                        self.preempt_flag.yfilter != YFilter.not_set or
                        self.primary_state.yfilter != YFilter.not_set or
                        self.primary_virtual_ip.yfilter != YFilter.not_set or
                        self.priority_decrement.yfilter != YFilter.not_set or
                        self.priority_zero_received_count.yfilter != YFilter.not_set or
                        self.priority_zero_sent_count.yfilter != YFilter.not_set or
                        self.reload_delay_time.yfilter != YFilter.not_set or
                        self.secondary_address_count.yfilter != YFilter.not_set or
                        self.session_name.yfilter != YFilter.not_set or
                        self.slaves.yfilter != YFilter.not_set or
                        self.state_change_count.yfilter != YFilter.not_set or
                        self.state_from_checkpoint.yfilter != YFilter.not_set or
                        self.time_in_current_state.yfilter != YFilter.not_set or
                        self.time_stats_discontinuity.yfilter != YFilter.not_set or
                        self.time_vrouter_up.yfilter != YFilter.not_set or
                        self.tracked_interface_count.yfilter != YFilter.not_set or
                        self.tracked_interface_up_count.yfilter != YFilter.not_set or
                        self.tracked_item_count.yfilter != YFilter.not_set or
                        self.tracked_item_up_count.yfilter != YFilter.not_set or
                        self.ttl_error_count.yfilter != YFilter.not_set or
                        self.version.yfilter != YFilter.not_set or
                        self.virtual_linklocal_ipv6_address.yfilter != YFilter.not_set or
                        self.virtual_mac_address.yfilter != YFilter.not_set or
                        self.virtual_mac_address_state.yfilter != YFilter.not_set or
                        self.virtual_router_id_xr.yfilter != YFilter.not_set or
                        self.vrrp_state.yfilter != YFilter.not_set or
                        (self.resign_received_time is not None and self.resign_received_time.has_operation()) or
                        (self.resign_sent_time is not None and self.resign_sent_time.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "virtual-router" + "[interface-name='" + self.interface_name.get() + "']" + "[virtual-router-id='" + self.virtual_router_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/virtual-routers/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.virtual_router_id.is_set or self.virtual_router_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_router_id.get_name_leafdata())
                    if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_family.get_name_leafdata())
                    if (self.address_list_error_count.is_set or self.address_list_error_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_list_error_count.get_name_leafdata())
                    if (self.advert_interval_error_count.is_set or self.advert_interval_error_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.advert_interval_error_count.get_name_leafdata())
                    if (self.adverts_received_count.is_set or self.adverts_received_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.adverts_received_count.get_name_leafdata())
                    if (self.adverts_sent_count.is_set or self.adverts_sent_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.adverts_sent_count.get_name_leafdata())
                    if (self.auth_type_mismatch_count.is_set or self.auth_type_mismatch_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auth_type_mismatch_count.get_name_leafdata())
                    if (self.authentication_fail_count.is_set or self.authentication_fail_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_fail_count.get_name_leafdata())
                    if (self.authentication_flag.is_set or self.authentication_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_flag.get_name_leafdata())
                    if (self.authentication_string.is_set or self.authentication_string.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_string.get_name_leafdata())
                    if (self.authentication_type.is_set or self.authentication_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_type.get_name_leafdata())
                    if (self.bfd_cfg_remote_ip.is_set or self.bfd_cfg_remote_ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_cfg_remote_ip.get_name_leafdata())
                    if (self.bfd_configured_remote_ipv6_address.is_set or self.bfd_configured_remote_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_configured_remote_ipv6_address.get_name_leafdata())
                    if (self.bfd_interval.is_set or self.bfd_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_interval.get_name_leafdata())
                    if (self.bfd_multiplier.is_set or self.bfd_multiplier.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_multiplier.get_name_leafdata())
                    if (self.bfd_session_state.is_set or self.bfd_session_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bfd_session_state.get_name_leafdata())
                    if (self.configured_advertize_time.is_set or self.configured_advertize_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_advertize_time.get_name_leafdata())
                    if (self.configured_down_address_count.is_set or self.configured_down_address_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_down_address_count.get_name_leafdata())
                    if (self.configured_priority.is_set or self.configured_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_priority.get_name_leafdata())
                    if (self.delay_timer_flag.is_set or self.delay_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_flag.get_name_leafdata())
                    if (self.delay_timer_msecs.is_set or self.delay_timer_msecs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_msecs.get_name_leafdata())
                    if (self.delay_timer_secs.is_set or self.delay_timer_secs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delay_timer_secs.get_name_leafdata())
                    if (self.followed_session_name.is_set or self.followed_session_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.followed_session_name.get_name_leafdata())
                    if (self.force_timer_flag.is_set or self.force_timer_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.force_timer_flag.get_name_leafdata())
                    if (self.interface_ipv4_address.is_set or self.interface_ipv4_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_ipv4_address.get_name_leafdata())
                    if (self.interface_ipv6_address.is_set or self.interface_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_ipv6_address.get_name_leafdata())
                    if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                    if (self.invalid_auth_type_count.is_set or self.invalid_auth_type_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_auth_type_count.get_name_leafdata())
                    if (self.invalid_packet_count.is_set or self.invalid_packet_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_packet_count.get_name_leafdata())
                    if (self.ip_address_owner_flag.is_set or self.ip_address_owner_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_address_owner_flag.get_name_leafdata())
                    if (self.is_accept_mode.is_set or self.is_accept_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_accept_mode.get_name_leafdata())
                    if (self.is_slave.is_set or self.is_slave.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_slave.get_name_leafdata())
                    if (self.master_count.is_set or self.master_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.master_count.get_name_leafdata())
                    if (self.master_ip_address.is_set or self.master_ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.master_ip_address.get_name_leafdata())
                    if (self.master_ipv6_address.is_set or self.master_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.master_ipv6_address.get_name_leafdata())
                    if (self.master_priority.is_set or self.master_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.master_priority.get_name_leafdata())
                    if (self.min_delay_time.is_set or self.min_delay_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.min_delay_time.get_name_leafdata())
                    if (self.oper_advertize_time.is_set or self.oper_advertize_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.oper_advertize_time.get_name_leafdata())
                    if (self.operational_address_count.is_set or self.operational_address_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operational_address_count.get_name_leafdata())
                    if (self.operational_priority.is_set or self.operational_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operational_priority.get_name_leafdata())
                    if (self.pkt_length_errors_count.is_set or self.pkt_length_errors_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pkt_length_errors_count.get_name_leafdata())
                    if (self.preempt_delay_time.is_set or self.preempt_delay_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.preempt_delay_time.get_name_leafdata())
                    if (self.preempt_flag.is_set or self.preempt_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.preempt_flag.get_name_leafdata())
                    if (self.primary_state.is_set or self.primary_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.primary_state.get_name_leafdata())
                    if (self.primary_virtual_ip.is_set or self.primary_virtual_ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.primary_virtual_ip.get_name_leafdata())
                    if (self.priority_decrement.is_set or self.priority_decrement.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority_decrement.get_name_leafdata())
                    if (self.priority_zero_received_count.is_set or self.priority_zero_received_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority_zero_received_count.get_name_leafdata())
                    if (self.priority_zero_sent_count.is_set or self.priority_zero_sent_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority_zero_sent_count.get_name_leafdata())
                    if (self.reload_delay_time.is_set or self.reload_delay_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reload_delay_time.get_name_leafdata())
                    if (self.secondary_address_count.is_set or self.secondary_address_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.secondary_address_count.get_name_leafdata())
                    if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_name.get_name_leafdata())
                    if (self.slaves.is_set or self.slaves.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.slaves.get_name_leafdata())
                    if (self.state_change_count.is_set or self.state_change_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state_change_count.get_name_leafdata())
                    if (self.state_from_checkpoint.is_set or self.state_from_checkpoint.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state_from_checkpoint.get_name_leafdata())
                    if (self.time_in_current_state.is_set or self.time_in_current_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time_in_current_state.get_name_leafdata())
                    if (self.time_stats_discontinuity.is_set or self.time_stats_discontinuity.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time_stats_discontinuity.get_name_leafdata())
                    if (self.time_vrouter_up.is_set or self.time_vrouter_up.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time_vrouter_up.get_name_leafdata())
                    if (self.tracked_interface_count.is_set or self.tracked_interface_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_count.get_name_leafdata())
                    if (self.tracked_interface_up_count.is_set or self.tracked_interface_up_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_interface_up_count.get_name_leafdata())
                    if (self.tracked_item_count.is_set or self.tracked_item_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_item_count.get_name_leafdata())
                    if (self.tracked_item_up_count.is_set or self.tracked_item_up_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracked_item_up_count.get_name_leafdata())
                    if (self.ttl_error_count.is_set or self.ttl_error_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ttl_error_count.get_name_leafdata())
                    if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.version.get_name_leafdata())
                    if (self.virtual_linklocal_ipv6_address.is_set or self.virtual_linklocal_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_linklocal_ipv6_address.get_name_leafdata())
                    if (self.virtual_mac_address.is_set or self.virtual_mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_mac_address.get_name_leafdata())
                    if (self.virtual_mac_address_state.is_set or self.virtual_mac_address_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_mac_address_state.get_name_leafdata())
                    if (self.virtual_router_id_xr.is_set or self.virtual_router_id_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.virtual_router_id_xr.get_name_leafdata())
                    if (self.vrrp_state.is_set or self.vrrp_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrrp_state.get_name_leafdata())

                    leaf_name_data.extend(self.ipv4_configured_down_address.get_name_leafdata())

                    leaf_name_data.extend(self.operational_address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ipv6-configured-down-address"):
                        for c in self.ipv6_configured_down_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv6_configured_down_address.append(c)
                        return c

                    if (child_yang_name == "ipv6-operational-address"):
                        for c in self.ipv6_operational_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv6_operational_address.append(c)
                        return c

                    if (child_yang_name == "resign-received-time"):
                        if (self.resign_received_time is None):
                            self.resign_received_time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime()
                            self.resign_received_time.parent = self
                            self._children_name_map["resign_received_time"] = "resign-received-time"
                        return self.resign_received_time

                    if (child_yang_name == "resign-sent-time"):
                        if (self.resign_sent_time is None):
                            self.resign_sent_time = Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime()
                            self.resign_sent_time.parent = self
                            self._children_name_map["resign_sent_time"] = "resign-sent-time"
                        return self.resign_sent_time

                    if (child_yang_name == "state-change-history"):
                        for c in self.state_change_history:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.state_change_history.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv6-configured-down-address" or name == "ipv6-operational-address" or name == "resign-received-time" or name == "resign-sent-time" or name == "state-change-history" or name == "interface-name" or name == "virtual-router-id" or name == "address-family" or name == "address-list-error-count" or name == "advert-interval-error-count" or name == "adverts-received-count" or name == "adverts-sent-count" or name == "auth-type-mismatch-count" or name == "authentication-fail-count" or name == "authentication-flag" or name == "authentication-string" or name == "authentication-type" or name == "bfd-cfg-remote-ip" or name == "bfd-configured-remote-ipv6-address" or name == "bfd-interval" or name == "bfd-multiplier" or name == "bfd-session-state" or name == "configured-advertize-time" or name == "configured-down-address-count" or name == "configured-priority" or name == "delay-timer-flag" or name == "delay-timer-msecs" or name == "delay-timer-secs" or name == "followed-session-name" or name == "force-timer-flag" or name == "interface-ipv4-address" or name == "interface-ipv6-address" or name == "interface-name-xr" or name == "invalid-auth-type-count" or name == "invalid-packet-count" or name == "ip-address-owner-flag" or name == "ipv4-configured-down-address" or name == "is-accept-mode" or name == "is-slave" or name == "master-count" or name == "master-ip-address" or name == "master-ipv6-address" or name == "master-priority" or name == "min-delay-time" or name == "oper-advertize-time" or name == "operational-address" or name == "operational-address-count" or name == "operational-priority" or name == "pkt-length-errors-count" or name == "preempt-delay-time" or name == "preempt-flag" or name == "primary-state" or name == "primary-virtual-ip" or name == "priority-decrement" or name == "priority-zero-received-count" or name == "priority-zero-sent-count" or name == "reload-delay-time" or name == "secondary-address-count" or name == "session-name" or name == "slaves" or name == "state-change-count" or name == "state-from-checkpoint" or name == "time-in-current-state" or name == "time-stats-discontinuity" or name == "time-vrouter-up" or name == "tracked-interface-count" or name == "tracked-interface-up-count" or name == "tracked-item-count" or name == "tracked-item-up-count" or name == "ttl-error-count" or name == "version" or name == "virtual-linklocal-ipv6-address" or name == "virtual-mac-address" or name == "virtual-mac-address-state" or name == "virtual-router-id-xr" or name == "vrrp-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "virtual-router-id"):
                        self.virtual_router_id = value
                        self.virtual_router_id.value_namespace = name_space
                        self.virtual_router_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "address-family"):
                        self.address_family = value
                        self.address_family.value_namespace = name_space
                        self.address_family.value_namespace_prefix = name_space_prefix
                    if(value_path == "address-list-error-count"):
                        self.address_list_error_count = value
                        self.address_list_error_count.value_namespace = name_space
                        self.address_list_error_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "advert-interval-error-count"):
                        self.advert_interval_error_count = value
                        self.advert_interval_error_count.value_namespace = name_space
                        self.advert_interval_error_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "adverts-received-count"):
                        self.adverts_received_count = value
                        self.adverts_received_count.value_namespace = name_space
                        self.adverts_received_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "adverts-sent-count"):
                        self.adverts_sent_count = value
                        self.adverts_sent_count.value_namespace = name_space
                        self.adverts_sent_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "auth-type-mismatch-count"):
                        self.auth_type_mismatch_count = value
                        self.auth_type_mismatch_count.value_namespace = name_space
                        self.auth_type_mismatch_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-fail-count"):
                        self.authentication_fail_count = value
                        self.authentication_fail_count.value_namespace = name_space
                        self.authentication_fail_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-flag"):
                        self.authentication_flag = value
                        self.authentication_flag.value_namespace = name_space
                        self.authentication_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-string"):
                        self.authentication_string = value
                        self.authentication_string.value_namespace = name_space
                        self.authentication_string.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-type"):
                        self.authentication_type = value
                        self.authentication_type.value_namespace = name_space
                        self.authentication_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-cfg-remote-ip"):
                        self.bfd_cfg_remote_ip = value
                        self.bfd_cfg_remote_ip.value_namespace = name_space
                        self.bfd_cfg_remote_ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "bfd-configured-remote-ipv6-address"):
                        self.bfd_configured_remote_ipv6_address = value
                        self.bfd_configured_remote_ipv6_address.value_namespace = name_space
                        self.bfd_configured_remote_ipv6_address.value_namespace_prefix = name_space_prefix
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
                    if(value_path == "configured-advertize-time"):
                        self.configured_advertize_time = value
                        self.configured_advertize_time.value_namespace = name_space
                        self.configured_advertize_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "configured-down-address-count"):
                        self.configured_down_address_count = value
                        self.configured_down_address_count.value_namespace = name_space
                        self.configured_down_address_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "configured-priority"):
                        self.configured_priority = value
                        self.configured_priority.value_namespace = name_space
                        self.configured_priority.value_namespace_prefix = name_space_prefix
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
                    if(value_path == "force-timer-flag"):
                        self.force_timer_flag = value
                        self.force_timer_flag.value_namespace = name_space
                        self.force_timer_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-ipv4-address"):
                        self.interface_ipv4_address = value
                        self.interface_ipv4_address.value_namespace = name_space
                        self.interface_ipv4_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-ipv6-address"):
                        self.interface_ipv6_address = value
                        self.interface_ipv6_address.value_namespace = name_space
                        self.interface_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-name-xr"):
                        self.interface_name_xr = value
                        self.interface_name_xr.value_namespace = name_space
                        self.interface_name_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-auth-type-count"):
                        self.invalid_auth_type_count = value
                        self.invalid_auth_type_count.value_namespace = name_space
                        self.invalid_auth_type_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-packet-count"):
                        self.invalid_packet_count = value
                        self.invalid_packet_count.value_namespace = name_space
                        self.invalid_packet_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-address-owner-flag"):
                        self.ip_address_owner_flag = value
                        self.ip_address_owner_flag.value_namespace = name_space
                        self.ip_address_owner_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv4-configured-down-address"):
                        self.ipv4_configured_down_address.append(value)
                    if(value_path == "is-accept-mode"):
                        self.is_accept_mode = value
                        self.is_accept_mode.value_namespace = name_space
                        self.is_accept_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-slave"):
                        self.is_slave = value
                        self.is_slave.value_namespace = name_space
                        self.is_slave.value_namespace_prefix = name_space_prefix
                    if(value_path == "master-count"):
                        self.master_count = value
                        self.master_count.value_namespace = name_space
                        self.master_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "master-ip-address"):
                        self.master_ip_address = value
                        self.master_ip_address.value_namespace = name_space
                        self.master_ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "master-ipv6-address"):
                        self.master_ipv6_address = value
                        self.master_ipv6_address.value_namespace = name_space
                        self.master_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "master-priority"):
                        self.master_priority = value
                        self.master_priority.value_namespace = name_space
                        self.master_priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "min-delay-time"):
                        self.min_delay_time = value
                        self.min_delay_time.value_namespace = name_space
                        self.min_delay_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "oper-advertize-time"):
                        self.oper_advertize_time = value
                        self.oper_advertize_time.value_namespace = name_space
                        self.oper_advertize_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "operational-address"):
                        self.operational_address.append(value)
                    if(value_path == "operational-address-count"):
                        self.operational_address_count = value
                        self.operational_address_count.value_namespace = name_space
                        self.operational_address_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "operational-priority"):
                        self.operational_priority = value
                        self.operational_priority.value_namespace = name_space
                        self.operational_priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "pkt-length-errors-count"):
                        self.pkt_length_errors_count = value
                        self.pkt_length_errors_count.value_namespace = name_space
                        self.pkt_length_errors_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "preempt-delay-time"):
                        self.preempt_delay_time = value
                        self.preempt_delay_time.value_namespace = name_space
                        self.preempt_delay_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "preempt-flag"):
                        self.preempt_flag = value
                        self.preempt_flag.value_namespace = name_space
                        self.preempt_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "primary-state"):
                        self.primary_state = value
                        self.primary_state.value_namespace = name_space
                        self.primary_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "primary-virtual-ip"):
                        self.primary_virtual_ip = value
                        self.primary_virtual_ip.value_namespace = name_space
                        self.primary_virtual_ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority-decrement"):
                        self.priority_decrement = value
                        self.priority_decrement.value_namespace = name_space
                        self.priority_decrement.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority-zero-received-count"):
                        self.priority_zero_received_count = value
                        self.priority_zero_received_count.value_namespace = name_space
                        self.priority_zero_received_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority-zero-sent-count"):
                        self.priority_zero_sent_count = value
                        self.priority_zero_sent_count.value_namespace = name_space
                        self.priority_zero_sent_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "reload-delay-time"):
                        self.reload_delay_time = value
                        self.reload_delay_time.value_namespace = name_space
                        self.reload_delay_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "secondary-address-count"):
                        self.secondary_address_count = value
                        self.secondary_address_count.value_namespace = name_space
                        self.secondary_address_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "session-name"):
                        self.session_name = value
                        self.session_name.value_namespace = name_space
                        self.session_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "slaves"):
                        self.slaves = value
                        self.slaves.value_namespace = name_space
                        self.slaves.value_namespace_prefix = name_space_prefix
                    if(value_path == "state-change-count"):
                        self.state_change_count = value
                        self.state_change_count.value_namespace = name_space
                        self.state_change_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "state-from-checkpoint"):
                        self.state_from_checkpoint = value
                        self.state_from_checkpoint.value_namespace = name_space
                        self.state_from_checkpoint.value_namespace_prefix = name_space_prefix
                    if(value_path == "time-in-current-state"):
                        self.time_in_current_state = value
                        self.time_in_current_state.value_namespace = name_space
                        self.time_in_current_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "time-stats-discontinuity"):
                        self.time_stats_discontinuity = value
                        self.time_stats_discontinuity.value_namespace = name_space
                        self.time_stats_discontinuity.value_namespace_prefix = name_space_prefix
                    if(value_path == "time-vrouter-up"):
                        self.time_vrouter_up = value
                        self.time_vrouter_up.value_namespace = name_space
                        self.time_vrouter_up.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-count"):
                        self.tracked_interface_count = value
                        self.tracked_interface_count.value_namespace = name_space
                        self.tracked_interface_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-interface-up-count"):
                        self.tracked_interface_up_count = value
                        self.tracked_interface_up_count.value_namespace = name_space
                        self.tracked_interface_up_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-item-count"):
                        self.tracked_item_count = value
                        self.tracked_item_count.value_namespace = name_space
                        self.tracked_item_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracked-item-up-count"):
                        self.tracked_item_up_count = value
                        self.tracked_item_up_count.value_namespace = name_space
                        self.tracked_item_up_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "ttl-error-count"):
                        self.ttl_error_count = value
                        self.ttl_error_count.value_namespace = name_space
                        self.ttl_error_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "version"):
                        self.version = value
                        self.version.value_namespace = name_space
                        self.version.value_namespace_prefix = name_space_prefix
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
                    if(value_path == "virtual-router-id-xr"):
                        self.virtual_router_id_xr = value
                        self.virtual_router_id_xr.value_namespace = name_space
                        self.virtual_router_id_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrrp-state"):
                        self.vrrp_state = value
                        self.vrrp_state.value_namespace = name_space
                        self.vrrp_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.virtual_router:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.virtual_router:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "virtual-routers" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/ipv4/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "virtual-router"):
                    for c in self.virtual_router:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Vrrp.Ipv4.VirtualRouters.VirtualRouter()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.virtual_router.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "virtual-router"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.interfaces is not None and self.interfaces.has_data()) or
                (self.track_items is not None and self.track_items.has_data()) or
                (self.virtual_routers is not None and self.virtual_routers.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.interfaces is not None and self.interfaces.has_operation()) or
                (self.track_items is not None and self.track_items.has_operation()) or
                (self.virtual_routers is not None and self.virtual_routers.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv4" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = Vrrp.Ipv4.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            if (child_yang_name == "track-items"):
                if (self.track_items is None):
                    self.track_items = Vrrp.Ipv4.TrackItems()
                    self.track_items.parent = self
                    self._children_name_map["track_items"] = "track-items"
                return self.track_items

            if (child_yang_name == "virtual-routers"):
                if (self.virtual_routers is None):
                    self.virtual_routers = Vrrp.Ipv4.VirtualRouters()
                    self.virtual_routers.parent = self
                    self._children_name_map["virtual_routers"] = "virtual-routers"
                return self.virtual_routers

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interfaces" or name == "track-items" or name == "virtual-routers"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class MgoSessions(Entity):
        """
        VRRP MGO Session information
        
        .. attribute:: mgo_session
        
        	A VRRP MGO Session
        	**type**\: list of    :py:class:`MgoSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.MgoSessions.MgoSession>`
        
        

        """

        _prefix = 'ipv4-vrrp-oper'
        _revision = '2016-12-16'

        def __init__(self):
            super(Vrrp.MgoSessions, self).__init__()

            self.yang_name = "mgo-sessions"
            self.yang_parent_name = "vrrp"

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
                        super(Vrrp.MgoSessions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vrrp.MgoSessions, self).__setattr__(name, value)


        class MgoSession(Entity):
            """
            A VRRP MGO Session
            
            .. attribute:: session_name  <key>
            
            	The name of the session
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: primary_af_name
            
            	Address family of primary session
            	**type**\:   :py:class:`VrrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBAf>`
            
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
            	**type**\:   :py:class:`VrrpBagProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.VrrpBagProtocolState>`
            
            .. attribute:: slave
            
            	List of slaves following this primary session
            	**type**\: list of    :py:class:`Slave <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper.Vrrp.MgoSessions.MgoSession.Slave>`
            
            

            """

            _prefix = 'ipv4-vrrp-oper'
            _revision = '2016-12-16'

            def __init__(self):
                super(Vrrp.MgoSessions.MgoSession, self).__init__()

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
                            super(Vrrp.MgoSessions.MgoSession, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vrrp.MgoSessions.MgoSession, self).__setattr__(name, value)


            class Slave(Entity):
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
                    super(Vrrp.MgoSessions.MgoSession.Slave, self).__init__()

                    self.yang_name = "slave"
                    self.yang_parent_name = "mgo-session"

                    self.slave_interface = YLeaf(YType.str, "slave-interface")

                    self.slave_virtual_router_id = YLeaf(YType.uint32, "slave-virtual-router-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("slave_interface",
                                    "slave_virtual_router_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrrp.MgoSessions.MgoSession.Slave, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrrp.MgoSessions.MgoSession.Slave, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.slave_interface.is_set or
                        self.slave_virtual_router_id.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.slave_interface.yfilter != YFilter.not_set or
                        self.slave_virtual_router_id.yfilter != YFilter.not_set)

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
                    if (self.slave_interface.is_set or self.slave_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.slave_interface.get_name_leafdata())
                    if (self.slave_virtual_router_id.is_set or self.slave_virtual_router_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.slave_virtual_router_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "slave-interface" or name == "slave-virtual-router-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "slave-interface"):
                        self.slave_interface = value
                        self.slave_interface.value_namespace = name_space
                        self.slave_interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "slave-virtual-router-id"):
                        self.slave_virtual_router_id = value
                        self.slave_virtual_router_id.value_namespace = name_space
                        self.slave_virtual_router_id.value_namespace_prefix = name_space_prefix

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
                    path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/mgo-sessions/%s" % self.get_segment_path()
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
                    c = Vrrp.MgoSessions.MgoSession.Slave()
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
                path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp/%s" % self.get_segment_path()
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
                c = Vrrp.MgoSessions.MgoSession()
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

    def has_data(self):
        return (
            (self.ipv4 is not None and self.ipv4.has_data()) or
            (self.ipv6 is not None and self.ipv6.has_data()) or
            (self.mgo_sessions is not None and self.mgo_sessions.has_data()) or
            (self.summary is not None and self.summary.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ipv4 is not None and self.ipv4.has_operation()) or
            (self.ipv6 is not None and self.ipv6.has_operation()) or
            (self.mgo_sessions is not None and self.mgo_sessions.has_operation()) or
            (self.summary is not None and self.summary.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-vrrp-oper:vrrp" + path_buffer

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

        if (child_yang_name == "ipv4"):
            if (self.ipv4 is None):
                self.ipv4 = Vrrp.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
            return self.ipv4

        if (child_yang_name == "ipv6"):
            if (self.ipv6 is None):
                self.ipv6 = Vrrp.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
            return self.ipv6

        if (child_yang_name == "mgo-sessions"):
            if (self.mgo_sessions is None):
                self.mgo_sessions = Vrrp.MgoSessions()
                self.mgo_sessions.parent = self
                self._children_name_map["mgo_sessions"] = "mgo-sessions"
            return self.mgo_sessions

        if (child_yang_name == "summary"):
            if (self.summary is None):
                self.summary = Vrrp.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
            return self.summary

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ipv4" or name == "ipv6" or name == "mgo-sessions" or name == "summary"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Vrrp()
        return self._top_entity

