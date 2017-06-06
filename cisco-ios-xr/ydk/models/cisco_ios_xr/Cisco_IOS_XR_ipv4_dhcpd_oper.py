""" Cisco_IOS_XR_ipv4_dhcpd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-dhcpd package operational data.

This module contains definitions
for the following management objects\:
  dhcp\-client\: DHCP client operational data
  ipv4\-dhcpd\: ipv4 dhcpd

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BagDhcpdIntfSrgRoleEnum(Enum):
    """
    BagDhcpdIntfSrgRoleEnum

    Bag dhcpd intf srg role

    .. data:: none = 0

    	DHCPv4 Interface SRG role NONE

    .. data:: master = 1

    	DHCPv4 Interface SRG role Master

    .. data:: slave = 2

    	DHCPv4 Interface SRG role Slave

    """

    none = 0

    master = 1

    slave = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['BagDhcpdIntfSrgRoleEnum']


class BagDhcpdProxyStateEnum(Enum):
    """
    BagDhcpdProxyStateEnum

    Bag dhcpd proxy state

    .. data:: initializing = 0

    	Initializing

    .. data:: selecting = 1

    	Selecting

    .. data:: requesting = 2

    	Requesting

    .. data:: bound = 3

    	Bound

    .. data:: renewing = 4

    	Renewing

    .. data:: informing = 5

    	Informing

    .. data:: deleting = 6

    	Deleting

    .. data:: create_dpm = 7

    	Create dpm

    .. data:: offer_sent = 8

    	Offer sent

    .. data:: update_dpm = 9

    	Update dpm

    .. data:: route_install = 10

    	Route install

    .. data:: disc_dpm = 11

    	Disc dpm

    .. data:: renew_new_intf = 12

    	Renew new intf

    .. data:: other_intf_dpm = 13

    	Other intf dpm

    .. data:: request_dpm = 14

    	Request dpm

    .. data:: change_addr_dpm = 15

    	Change addr dpm

    .. data:: max = 16

    	Max

    """

    initializing = 0

    selecting = 1

    requesting = 2

    bound = 3

    renewing = 4

    informing = 5

    deleting = 6

    create_dpm = 7

    offer_sent = 8

    update_dpm = 9

    route_install = 10

    disc_dpm = 11

    renew_new_intf = 12

    other_intf_dpm = 13

    request_dpm = 14

    change_addr_dpm = 15

    max = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['BagDhcpdProxyStateEnum']


class BroadcastFlagEnum(Enum):
    """
    BroadcastFlagEnum

    Proxy profile broadcast flag

    .. data:: ignore = 0

    	Broadcast policy ignore

    .. data:: check = 1

    	Broadcast policy check

    .. data:: unicast_always = 2

    	Broadcast policy unicast always

    """

    ignore = 0

    check = 1

    unicast_always = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['BroadcastFlagEnum']


class DhcpIssuPhaseEnum(Enum):
    """
    DhcpIssuPhaseEnum

    Dhcp issu phase

    .. data:: phase_not_started = 0

    	An ISSU event has not started

    .. data:: phase_load = 1

    	ISSU Load Phase

    .. data:: phase_run = 2

    	ISSU Run Phase

    .. data:: phase_completed = 3

    	An ISSU event has completed successfully

    .. data:: phase_aborted = 4

    	An ISSU event has aborted

    """

    phase_not_started = 0

    phase_load = 1

    phase_run = 2

    phase_completed = 3

    phase_aborted = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['DhcpIssuPhaseEnum']


class DhcpIssuRoleEnum(Enum):
    """
    DhcpIssuRoleEnum

    Dhcp issu role

    .. data:: role_primary = 0

    	Primary role

    .. data:: role_secondary = 1

    	Secondary role

    """

    role_primary = 0

    role_secondary = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['DhcpIssuRoleEnum']


class DhcpIssuVersionEnum(Enum):
    """
    DhcpIssuVersionEnum

    Dhcp issu version

    .. data:: version1 = 0

    	Version 1

    .. data:: version2 = 1

    	Version 2

    """

    version1 = 0

    version2 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['DhcpIssuVersionEnum']


class DhcpcIpv4StateEnum(Enum):
    """
    DhcpcIpv4StateEnum

    Dhcp Client IPv4 State

    .. data:: init = 0

    	Init state

    .. data:: init_reboot = 1

    	Init Reboot state

    .. data:: rebooting = 2

    	Rebooting state

    .. data:: selecting = 3

    	Selecting state

    .. data:: requesting = 4

    	Requesting state

    .. data:: bound = 5

    	Bound state

    .. data:: renewing = 6

    	Renewing state

    .. data:: rebinding = 7

    	Rebinding state

    .. data:: invalid = 8

    	Invalid state

    """

    init = 0

    init_reboot = 1

    rebooting = 2

    selecting = 3

    requesting = 4

    bound = 5

    renewing = 6

    rebinding = 7

    invalid = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['DhcpcIpv4StateEnum']


class ProxyLeaseLimitEnum(Enum):
    """
    ProxyLeaseLimitEnum

    Proxy profile lease limit type

    .. data:: none = 0

    	Proxy lease limit type none

    .. data:: interface = 1

    	Proxy lease limit type interface

    .. data:: circuit_id = 2

    	Proxy lease limit type circuit ID

    .. data:: remote_id = 3

    	Proxy lease limit type remote ID

    .. data:: remote_id_circuit_id = 4

    	Proxy lease limit type remote ID + circuit ID

    """

    none = 0

    interface = 1

    circuit_id = 2

    remote_id = 3

    remote_id_circuit_id = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['ProxyLeaseLimitEnum']


class RelayInfoAuthenticateEnum(Enum):
    """
    RelayInfoAuthenticateEnum

    Profile relay authenticate

    .. data:: received = 0

    	Relay authenticate received

    .. data:: inserted = 1

    	Relay authenticate inserted

    """

    received = 0

    inserted = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['RelayInfoAuthenticateEnum']


class RelayInfoPolicyEnum(Enum):
    """
    RelayInfoPolicyEnum

    Proxy profile relay policy

    .. data:: replace = 0

    	Relay policy replace

    .. data:: keep = 1

    	Relay policy keep

    .. data:: drop = 2

    	Relay policy drop

    .. data:: encapsulate = 3

    	Relay policy encapsulate

    """

    replace = 0

    keep = 1

    drop = 2

    encapsulate = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['RelayInfoPolicyEnum']


class RelayInfoVpnModeEnum(Enum):
    """
    RelayInfoVpnModeEnum

    Relay Info Vpn Mode

    .. data:: rfc = 0

    	RFC Mode

    .. data:: cisco = 1

    	Cisco Mode

    """

    rfc = 0

    cisco = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['RelayInfoVpnModeEnum']



class DhcpClient(object):
    """
    DHCP client operational data
    
    .. attribute:: nodes
    
    	DHCP client list of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes>`
    
    

    """

    _prefix = 'ipv4-dhcpd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = DhcpClient.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        DHCP client list of nodes
        
        .. attribute:: node
        
        	DHCP client particular node name
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes.Node>`
        
        

        """

        _prefix = 'ipv4-dhcpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            DHCP client particular node name
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: client_stats
            
            	IPv4 DHCP client statistics table
            	**type**\:   :py:class:`ClientStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes.Node.ClientStats>`
            
            .. attribute:: clients
            
            	IPv4 DHCP client table
            	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes.Node.Clients>`
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.client_stats = DhcpClient.Nodes.Node.ClientStats()
                self.client_stats.parent = self
                self.clients = DhcpClient.Nodes.Node.Clients()
                self.clients.parent = self


            class ClientStats(object):
                """
                IPv4 DHCP client statistics table
                
                .. attribute:: client_stat
                
                	DHCP client binding statistics
                	**type**\: list of    :py:class:`ClientStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes.Node.ClientStats.ClientStat>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.client_stat = YList()
                    self.client_stat.parent = self
                    self.client_stat.name = 'client_stat'


                class ClientStat(object):
                    """
                    DHCP client binding statistics
                    
                    .. attribute:: client_ifhandle  <key>
                    
                    	Client Ifhandle
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: interface_name
                    
                    	Dhcp Client interface name
                    	**type**\:  str
                    
                    	**length:** 0..65
                    
                    .. attribute:: num_broadcast_failed
                    
                    	Number of broadcast packet send failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_broadcast_packet_sent_success
                    
                    	Number of broadcast packet sent successfully
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_create_event_received
                    
                    	Number of create client event received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_declines_failed
                    
                    	Number of decline send failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_declines_sent_successfully
                    
                    	Number of declines sent successfully
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_delete_event_received
                    
                    	Number of delete client event received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_discovers_failed
                    
                    	Number of discover send failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_discovers_sent_successfully
                    
                    	Number of discovers sent successfully
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_events_received
                    
                    	Number of events received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_init_timer_eventi
                    
                    	Number of init timer event
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_init_timer_start
                    
                    	Number of init timer starts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_init_timer_stop
                    
                    	Number of init timer stops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_invalid_acks
                    
                    	Number of invalid acks received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_invalid_events
                    
                    	Number of invalid events received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_invalid_nacks
                    
                    	Number of invalid nacks received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_invalid_offers
                    
                    	Number of invalid offers received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_invalid_packets
                    
                    	Number of invalid packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_lease_timer_event
                    
                    	Number of Lease timer event
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_lease_timer_start
                    
                    	Number of Lease timer starts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_lease_timer_stop
                    
                    	Number of Lease timer stops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_packet_event_received
                    
                    	Number of packet event received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_rebinds_failed
                    
                    	Number of rebind send failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_rebinds_sent_successfully
                    
                    	Number of rebinds sent successfully
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_reboot_event_received
                    
                    	Number of client rebooted event received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_reinit_event_received
                    
                    	Number of reinit client event received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_releases_failed
                    
                    	Number of release send failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_releases_sent_successfully
                    
                    	Number of releases sent successfully
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_renews_failed
                    
                    	Number of renew send failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_renews_sent_successfully
                    
                    	Number of renews sent successfully
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_request_after_reboot_failed
                    
                    	Number of requests sent after reboot failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_request_after_reboot_sent
                    
                    	Number of requests sent after reboot
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_requests_failed
                    
                    	Number of request send failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_requests_sent_successfully
                    
                    	Number of requests sent successfully
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t1_timer_event
                    
                    	Number of T1 timer event
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t1_timer_start
                    
                    	Number of T1 timer starts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t1_timer_stop
                    
                    	Number of T1 timer stops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t2_timer_event
                    
                    	Number of T2 timer event
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t2_timer_start
                    
                    	Number of T2 timer starts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t2_timer_stop
                    
                    	Number of T2 timer stops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_unicast_failed
                    
                    	Number of unicast packet send failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_unicast_packet_sent_successfully
                    
                    	Number of unicast packet sent successfully
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_valid_acks_received
                    
                    	Number of valid acks received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_valid_nacks_received
                    
                    	Number of valid nacks received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_valid_offers_received
                    
                    	Number of valid offers received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_xid_mismatch
                    
                    	Number of XID mismatch packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.client_ifhandle = None
                        self.interface_name = None
                        self.num_broadcast_failed = None
                        self.num_broadcast_packet_sent_success = None
                        self.num_create_event_received = None
                        self.num_declines_failed = None
                        self.num_declines_sent_successfully = None
                        self.num_delete_event_received = None
                        self.num_discovers_failed = None
                        self.num_discovers_sent_successfully = None
                        self.num_events_received = None
                        self.num_init_timer_eventi = None
                        self.num_init_timer_start = None
                        self.num_init_timer_stop = None
                        self.num_invalid_acks = None
                        self.num_invalid_events = None
                        self.num_invalid_nacks = None
                        self.num_invalid_offers = None
                        self.num_invalid_packets = None
                        self.num_lease_timer_event = None
                        self.num_lease_timer_start = None
                        self.num_lease_timer_stop = None
                        self.num_packet_event_received = None
                        self.num_rebinds_failed = None
                        self.num_rebinds_sent_successfully = None
                        self.num_reboot_event_received = None
                        self.num_reinit_event_received = None
                        self.num_releases_failed = None
                        self.num_releases_sent_successfully = None
                        self.num_renews_failed = None
                        self.num_renews_sent_successfully = None
                        self.num_request_after_reboot_failed = None
                        self.num_request_after_reboot_sent = None
                        self.num_requests_failed = None
                        self.num_requests_sent_successfully = None
                        self.num_t1_timer_event = None
                        self.num_t1_timer_start = None
                        self.num_t1_timer_stop = None
                        self.num_t2_timer_event = None
                        self.num_t2_timer_start = None
                        self.num_t2_timer_stop = None
                        self.num_unicast_failed = None
                        self.num_unicast_packet_sent_successfully = None
                        self.num_valid_acks_received = None
                        self.num_valid_nacks_received = None
                        self.num_valid_offers_received = None
                        self.num_xid_mismatch = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.client_ifhandle is None:
                            raise YPYModelError('Key property client_ifhandle is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:client-stat[Cisco-IOS-XR-ipv4-dhcpd-oper:client-ifhandle = ' + str(self.client_ifhandle) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.client_ifhandle is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.num_broadcast_failed is not None:
                            return True

                        if self.num_broadcast_packet_sent_success is not None:
                            return True

                        if self.num_create_event_received is not None:
                            return True

                        if self.num_declines_failed is not None:
                            return True

                        if self.num_declines_sent_successfully is not None:
                            return True

                        if self.num_delete_event_received is not None:
                            return True

                        if self.num_discovers_failed is not None:
                            return True

                        if self.num_discovers_sent_successfully is not None:
                            return True

                        if self.num_events_received is not None:
                            return True

                        if self.num_init_timer_eventi is not None:
                            return True

                        if self.num_init_timer_start is not None:
                            return True

                        if self.num_init_timer_stop is not None:
                            return True

                        if self.num_invalid_acks is not None:
                            return True

                        if self.num_invalid_events is not None:
                            return True

                        if self.num_invalid_nacks is not None:
                            return True

                        if self.num_invalid_offers is not None:
                            return True

                        if self.num_invalid_packets is not None:
                            return True

                        if self.num_lease_timer_event is not None:
                            return True

                        if self.num_lease_timer_start is not None:
                            return True

                        if self.num_lease_timer_stop is not None:
                            return True

                        if self.num_packet_event_received is not None:
                            return True

                        if self.num_rebinds_failed is not None:
                            return True

                        if self.num_rebinds_sent_successfully is not None:
                            return True

                        if self.num_reboot_event_received is not None:
                            return True

                        if self.num_reinit_event_received is not None:
                            return True

                        if self.num_releases_failed is not None:
                            return True

                        if self.num_releases_sent_successfully is not None:
                            return True

                        if self.num_renews_failed is not None:
                            return True

                        if self.num_renews_sent_successfully is not None:
                            return True

                        if self.num_request_after_reboot_failed is not None:
                            return True

                        if self.num_request_after_reboot_sent is not None:
                            return True

                        if self.num_requests_failed is not None:
                            return True

                        if self.num_requests_sent_successfully is not None:
                            return True

                        if self.num_t1_timer_event is not None:
                            return True

                        if self.num_t1_timer_start is not None:
                            return True

                        if self.num_t1_timer_stop is not None:
                            return True

                        if self.num_t2_timer_event is not None:
                            return True

                        if self.num_t2_timer_start is not None:
                            return True

                        if self.num_t2_timer_stop is not None:
                            return True

                        if self.num_unicast_failed is not None:
                            return True

                        if self.num_unicast_packet_sent_successfully is not None:
                            return True

                        if self.num_valid_acks_received is not None:
                            return True

                        if self.num_valid_nacks_received is not None:
                            return True

                        if self.num_valid_offers_received is not None:
                            return True

                        if self.num_xid_mismatch is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['DhcpClient.Nodes.Node.ClientStats.ClientStat']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:client-stats'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.client_stat is not None:
                        for child_ref in self.client_stat:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                    return meta._meta_table['DhcpClient.Nodes.Node.ClientStats']['meta_info']


            class Clients(object):
                """
                IPv4 DHCP client table
                
                .. attribute:: client
                
                	Single DHCP client binding
                	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes.Node.Clients.Client>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.client = YList()
                    self.client.parent = self
                    self.client.name = 'client'


                class Client(object):
                    """
                    Single DHCP client binding
                    
                    .. attribute:: client_ifhandle  <key>
                    
                    	Client Ifhandle
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: client_id
                    
                    	Dhcp Client ID
                    	**type**\:  str
                    
                    	**length:** 0..256
                    
                    .. attribute:: client_mac_address
                    
                    	Dhcp Client Interface MAC address
                    	**type**\:  str
                    
                    	**length:** 0..17
                    
                    .. attribute:: interface_name
                    
                    	Dhcp Client interface name
                    	**type**\:  str
                    
                    	**length:** 0..65
                    
                    .. attribute:: ipv4_address
                    
                    	Dhcp Client IP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_address_configured
                    
                    	Dhcp Client IPV4 address configured in interface
                    	**type**\:  bool
                    
                    .. attribute:: ipv4_client_state
                    
                    	Dhcp Client State
                    	**type**\:   :py:class:`DhcpcIpv4StateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpcIpv4StateEnum>`
                    
                    .. attribute:: ipv4_lease_time
                    
                    	Dhcp Client Lease time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_rebind_time
                    
                    	Dhcp Client Rebind time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_renew_time
                    
                    	Dhcp Client Renew time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_server_address
                    
                    	Dhcp Client selected server IP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_subnet_mask
                    
                    	Dhcp Client IP Address mask
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: next_hop_ipv4_address
                    
                    	Dhcp Client next hop IP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.client_ifhandle = None
                        self.client_id = None
                        self.client_mac_address = None
                        self.interface_name = None
                        self.ipv4_address = None
                        self.ipv4_address_configured = None
                        self.ipv4_client_state = None
                        self.ipv4_lease_time = None
                        self.ipv4_rebind_time = None
                        self.ipv4_renew_time = None
                        self.ipv4_server_address = None
                        self.ipv4_subnet_mask = None
                        self.next_hop_ipv4_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.client_ifhandle is None:
                            raise YPYModelError('Key property client_ifhandle is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:client[Cisco-IOS-XR-ipv4-dhcpd-oper:client-ifhandle = ' + str(self.client_ifhandle) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.client_ifhandle is not None:
                            return True

                        if self.client_id is not None:
                            return True

                        if self.client_mac_address is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.ipv4_address is not None:
                            return True

                        if self.ipv4_address_configured is not None:
                            return True

                        if self.ipv4_client_state is not None:
                            return True

                        if self.ipv4_lease_time is not None:
                            return True

                        if self.ipv4_rebind_time is not None:
                            return True

                        if self.ipv4_renew_time is not None:
                            return True

                        if self.ipv4_server_address is not None:
                            return True

                        if self.ipv4_subnet_mask is not None:
                            return True

                        if self.next_hop_ipv4_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['DhcpClient.Nodes.Node.Clients.Client']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:clients'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.client is not None:
                        for child_ref in self.client:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                    return meta._meta_table['DhcpClient.Nodes.Node.Clients']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ipv4-dhcpd-oper:dhcp-client/Cisco-IOS-XR-ipv4-dhcpd-oper:nodes/Cisco-IOS-XR-ipv4-dhcpd-oper:node[Cisco-IOS-XR-ipv4-dhcpd-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.client_stats is not None and self.client_stats._has_data():
                    return True

                if self.clients is not None and self.clients._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                return meta._meta_table['DhcpClient.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-dhcpd-oper:dhcp-client/Cisco-IOS-XR-ipv4-dhcpd-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
            return meta._meta_table['DhcpClient.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-dhcpd-oper:dhcp-client'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['DhcpClient']['meta_info']


class Ipv4Dhcpd(object):
    """
    ipv4 dhcpd
    
    .. attribute:: nodes
    
    	IPv4 DHCPD operational data for a particular location
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes>`
    
    .. attribute:: snoop
    
    	DHCP Snoop operational data
    	**type**\:   :py:class:`Snoop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop>`
    
    

    """

    _prefix = 'ipv4-dhcpd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Ipv4Dhcpd.Nodes()
        self.nodes.parent = self
        self.snoop = Ipv4Dhcpd.Snoop()
        self.snoop.parent = self


    class Snoop(object):
        """
        DHCP Snoop operational data
        
        .. attribute:: binding_statistics
        
        	DHCP snoop binding statistics
        	**type**\:   :py:class:`BindingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.BindingStatistics>`
        
        .. attribute:: bindings
        
        	DHCP Snoop Bindings
        	**type**\:   :py:class:`Bindings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Bindings>`
        
        .. attribute:: profiles
        
        	DHCP Snoop Profile
        	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Profiles>`
        
        .. attribute:: statistics
        
        	DHCP Snoop Statistics
        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Statistics>`
        
        .. attribute:: statistics_info
        
        	DHCP snoop statistics info
        	**type**\:   :py:class:`StatisticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.StatisticsInfo>`
        
        

        """

        _prefix = 'ipv4-dhcpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.binding_statistics = Ipv4Dhcpd.Snoop.BindingStatistics()
            self.binding_statistics.parent = self
            self.bindings = Ipv4Dhcpd.Snoop.Bindings()
            self.bindings.parent = self
            self.profiles = Ipv4Dhcpd.Snoop.Profiles()
            self.profiles.parent = self
            self.statistics = Ipv4Dhcpd.Snoop.Statistics()
            self.statistics.parent = self
            self.statistics_info = Ipv4Dhcpd.Snoop.StatisticsInfo()
            self.statistics_info.parent = self


        class Bindings(object):
            """
            DHCP Snoop Bindings
            
            .. attribute:: binding
            
            	DHCP Snoop binding
            	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Bindings.Binding>`
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.binding = YList()
                self.binding.parent = self
                self.binding.name = 'binding'


            class Binding(object):
                """
                DHCP Snoop binding
                
                .. attribute:: client_uid  <key>
                
                	Client opaque handle
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: snoop_binding_bridge_name
                
                	DHCP L2 bridge name
                	**type**\:  str
                
                	**length:** 0..74
                
                .. attribute:: snoop_binding_ch_addr
                
                	DHCP client MAC address
                	**type**\:  str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                .. attribute:: snoop_binding_ch_addr_len
                
                	DHCP client MAC address length
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: snoop_binding_client_id
                
                	DHCP client id
                	**type**\:  str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                .. attribute:: snoop_binding_client_id_len
                
                	DHCP client id len
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: snoop_binding_i_addr
                
                	DHCP iaddr
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: snoop_binding_lease
                
                	DHCP lease time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: snoop_binding_lease_start_time
                
                	DHCP lease start time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: snoop_binding_profile_name
                
                	DHCP profile name
                	**type**\:  str
                
                	**length:** 0..65
                
                .. attribute:: snoop_binding_state
                
                	DHCP sm state
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: snoop_bindng_interface_name
                
                	DHCP interface to client
                	**type**\:  str
                
                	**length:** 0..321
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.client_uid = None
                    self.snoop_binding_bridge_name = None
                    self.snoop_binding_ch_addr = None
                    self.snoop_binding_ch_addr_len = None
                    self.snoop_binding_client_id = None
                    self.snoop_binding_client_id_len = None
                    self.snoop_binding_i_addr = None
                    self.snoop_binding_lease = None
                    self.snoop_binding_lease_start_time = None
                    self.snoop_binding_profile_name = None
                    self.snoop_binding_state = None
                    self.snoop_bindng_interface_name = None

                @property
                def _common_path(self):
                    if self.client_uid is None:
                        raise YPYModelError('Key property client_uid is None')

                    return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-oper:snoop/Cisco-IOS-XR-ipv4-dhcpd-oper:bindings/Cisco-IOS-XR-ipv4-dhcpd-oper:binding[Cisco-IOS-XR-ipv4-dhcpd-oper:client-uid = ' + str(self.client_uid) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.client_uid is not None:
                        return True

                    if self.snoop_binding_bridge_name is not None:
                        return True

                    if self.snoop_binding_ch_addr is not None:
                        return True

                    if self.snoop_binding_ch_addr_len is not None:
                        return True

                    if self.snoop_binding_client_id is not None:
                        return True

                    if self.snoop_binding_client_id_len is not None:
                        return True

                    if self.snoop_binding_i_addr is not None:
                        return True

                    if self.snoop_binding_lease is not None:
                        return True

                    if self.snoop_binding_lease_start_time is not None:
                        return True

                    if self.snoop_binding_profile_name is not None:
                        return True

                    if self.snoop_binding_state is not None:
                        return True

                    if self.snoop_bindng_interface_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                    return meta._meta_table['Ipv4Dhcpd.Snoop.Bindings.Binding']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-oper:snoop/Cisco-IOS-XR-ipv4-dhcpd-oper:bindings'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.binding is not None:
                    for child_ref in self.binding:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                return meta._meta_table['Ipv4Dhcpd.Snoop.Bindings']['meta_info']


        class BindingStatistics(object):
            """
            DHCP snoop binding statistics
            
            .. attribute:: snoop_binding_timestamp
            
            	Snoop binding timestamp
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: snoop_binding_total
            
            	Total number of snoop bindings
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.snoop_binding_timestamp = None
                self.snoop_binding_total = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-oper:snoop/Cisco-IOS-XR-ipv4-dhcpd-oper:binding-statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.snoop_binding_timestamp is not None:
                    return True

                if self.snoop_binding_total is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                return meta._meta_table['Ipv4Dhcpd.Snoop.BindingStatistics']['meta_info']


        class StatisticsInfo(object):
            """
            DHCP snoop statistics info
            
            .. attribute:: snoop_stats_timestamp
            
            	Snoop Stats timestamp
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.snoop_stats_timestamp = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-oper:snoop/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.snoop_stats_timestamp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                return meta._meta_table['Ipv4Dhcpd.Snoop.StatisticsInfo']['meta_info']


        class Profiles(object):
            """
            DHCP Snoop Profile
            
            .. attribute:: profile
            
            	DHCP Snoop profile
            	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Profiles.Profile>`
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.profile = YList()
                self.profile.parent = self
                self.profile.name = 'profile'


            class Profile(object):
                """
                DHCP Snoop profile
                
                .. attribute:: profile_name  <key>
                
                	Profile name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: snoop_profile_name
                
                	Profile Name
                	**type**\:  str
                
                	**length:** 0..65
                
                .. attribute:: snoop_profile_relay_info_allow_untrusted
                
                	Allow untrusted relay info
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: snoop_profile_relay_info_option
                
                	Relay info option
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: snoop_profile_relay_info_policy
                
                	Relay info policy
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: snoop_profile_trusted
                
                	Trust
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: snoop_profile_uid
                
                	Profile unique ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.profile_name = None
                    self.snoop_profile_name = None
                    self.snoop_profile_relay_info_allow_untrusted = None
                    self.snoop_profile_relay_info_option = None
                    self.snoop_profile_relay_info_policy = None
                    self.snoop_profile_trusted = None
                    self.snoop_profile_uid = None

                @property
                def _common_path(self):
                    if self.profile_name is None:
                        raise YPYModelError('Key property profile_name is None')

                    return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-oper:snoop/Cisco-IOS-XR-ipv4-dhcpd-oper:profiles/Cisco-IOS-XR-ipv4-dhcpd-oper:profile[Cisco-IOS-XR-ipv4-dhcpd-oper:profile-name = ' + str(self.profile_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.profile_name is not None:
                        return True

                    if self.snoop_profile_name is not None:
                        return True

                    if self.snoop_profile_relay_info_allow_untrusted is not None:
                        return True

                    if self.snoop_profile_relay_info_option is not None:
                        return True

                    if self.snoop_profile_relay_info_policy is not None:
                        return True

                    if self.snoop_profile_trusted is not None:
                        return True

                    if self.snoop_profile_uid is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                    return meta._meta_table['Ipv4Dhcpd.Snoop.Profiles.Profile']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-oper:snoop/Cisco-IOS-XR-ipv4-dhcpd-oper:profiles'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.profile is not None:
                    for child_ref in self.profile:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                return meta._meta_table['Ipv4Dhcpd.Snoop.Profiles']['meta_info']


        class Statistics(object):
            """
            DHCP Snoop Statistics
            
            .. attribute:: statistic
            
            	DHCP Snoop bridge domain statistics
            	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Statistics.Statistic>`
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.statistic = YList()
                self.statistic.parent = self
                self.statistic.name = 'statistic'


            class Statistic(object):
                """
                DHCP Snoop bridge domain statistics
                
                .. attribute:: bridge_name  <key>
                
                	Bridge domain name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: snoop_statistic
                
                	Public snoop statistics
                	**type**\:  list of int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: snoop_statistics_bridge_name
                
                	DHCP L2 bridge name
                	**type**\:  str
                
                	**length:** 0..74
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bridge_name = None
                    self.snoop_statistic = YLeafList()
                    self.snoop_statistic.parent = self
                    self.snoop_statistic.name = 'snoop_statistic'
                    self.snoop_statistics_bridge_name = None

                @property
                def _common_path(self):
                    if self.bridge_name is None:
                        raise YPYModelError('Key property bridge_name is None')

                    return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-oper:snoop/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics/Cisco-IOS-XR-ipv4-dhcpd-oper:statistic[Cisco-IOS-XR-ipv4-dhcpd-oper:bridge-name = ' + str(self.bridge_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bridge_name is not None:
                        return True

                    if self.snoop_statistic is not None:
                        for child in self.snoop_statistic:
                            if child is not None:
                                return True

                    if self.snoop_statistics_bridge_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                    return meta._meta_table['Ipv4Dhcpd.Snoop.Statistics.Statistic']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-oper:snoop/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.statistic is not None:
                    for child_ref in self.statistic:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                return meta._meta_table['Ipv4Dhcpd.Snoop.Statistics']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-oper:snoop'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.binding_statistics is not None and self.binding_statistics._has_data():
                return True

            if self.bindings is not None and self.bindings._has_data():
                return True

            if self.profiles is not None and self.profiles._has_data():
                return True

            if self.statistics is not None and self.statistics._has_data():
                return True

            if self.statistics_info is not None and self.statistics_info._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
            return meta._meta_table['Ipv4Dhcpd.Snoop']['meta_info']


    class Nodes(object):
        """
        IPv4 DHCPD operational data for a particular
        location
        
        .. attribute:: node
        
        	Location. For eg., 0/1/CPU0
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node>`
        
        

        """

        _prefix = 'ipv4-dhcpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Location. For eg., 0/1/CPU0
            
            .. attribute:: nodeid  <key>
            
            	The node id to filter on. For eg., 0/1/CPU0
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: base
            
            	IPv4 DHCP base operational data
            	**type**\:   :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base>`
            
            .. attribute:: interfaces
            
            	IPv4 DHCP proxy/server Interface
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Interfaces>`
            
            .. attribute:: proxy
            
            	IPv4 DHCP proxy operational data
            	**type**\:   :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy>`
            
            .. attribute:: relay
            
            	IPv4 DHCPD Relay operational data
            	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay>`
            
            .. attribute:: server
            
            	IPv4 DHCP Server operational data
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server>`
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.nodeid = None
                self.base = Ipv4Dhcpd.Nodes.Node.Base()
                self.base.parent = self
                self.interfaces = Ipv4Dhcpd.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self.proxy = Ipv4Dhcpd.Nodes.Node.Proxy()
                self.proxy.parent = self
                self.relay = Ipv4Dhcpd.Nodes.Node.Relay()
                self.relay.parent = self
                self.server = Ipv4Dhcpd.Nodes.Node.Server()
                self.server.parent = self


            class Proxy(object):
                """
                IPv4 DHCP proxy operational data
                
                .. attribute:: binding
                
                	DHCP proxy bindings
                	**type**\:   :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Binding>`
                
                .. attribute:: profiles
                
                	IPv4 DHCP proxy profile
                	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles>`
                
                .. attribute:: statistics
                
                	DHCP proxy statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Statistics>`
                
                .. attribute:: statistics_info
                
                	DHCP proxy stats info
                	**type**\:   :py:class:`StatisticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo>`
                
                .. attribute:: vrfs
                
                	DHCP proxy list of VRF names
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.binding = Ipv4Dhcpd.Nodes.Node.Proxy.Binding()
                    self.binding.parent = self
                    self.profiles = Ipv4Dhcpd.Nodes.Node.Proxy.Profiles()
                    self.profiles.parent = self
                    self.statistics = Ipv4Dhcpd.Nodes.Node.Proxy.Statistics()
                    self.statistics.parent = self
                    self.statistics_info = Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo()
                    self.statistics_info.parent = self
                    self.vrfs = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs()
                    self.vrfs.parent = self


                class StatisticsInfo(object):
                    """
                    DHCP proxy stats info
                    
                    .. attribute:: proxy_stats_timestamp
                    
                    	Proxy Stats timestamp
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.proxy_stats_timestamp = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.proxy_stats_timestamp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo']['meta_info']


                class Vrfs(object):
                    """
                    DHCP proxy list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv4 DHCP proxy VRF name
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        IPv4 DHCP proxy VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv4 DHCP proxy statistics
                        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.statistics = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self


                        class Statistics(object):
                            """
                            IPv4 DHCP proxy statistics
                            
                            .. attribute:: ack
                            
                            	DHCP ack packets
                            	**type**\:   :py:class:`Ack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack>`
                            
                            .. attribute:: bootp_reply
                            
                            	DHCP BOOTP reply
                            	**type**\:   :py:class:`BootpReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply>`
                            
                            .. attribute:: bootp_request
                            
                            	DHCP BOOTP request
                            	**type**\:   :py:class:`BootpRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest>`
                            
                            .. attribute:: decline
                            
                            	DHCP decline packets
                            	**type**\:   :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: discover
                            
                            	DHCP discover packets
                            	**type**\:   :py:class:`Discover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover>`
                            
                            .. attribute:: inform
                            
                            	DHCP inform packets
                            	**type**\:   :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: lease_active
                            
                            	DHCP lease active
                            	**type**\:   :py:class:`LeaseActive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive>`
                            
                            .. attribute:: lease_not_assigned
                            
                            	DHCP lease not assigned
                            	**type**\:   :py:class:`LeaseNotAssigned <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned>`
                            
                            .. attribute:: lease_query
                            
                            	DHCP lease query packets
                            	**type**\:   :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_unknown
                            
                            	DHCP lease unknown
                            	**type**\:   :py:class:`LeaseUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown>`
                            
                            .. attribute:: nak
                            
                            	DHCP nak packets
                            	**type**\:   :py:class:`Nak <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak>`
                            
                            .. attribute:: offer
                            
                            	DHCP offer packets
                            	**type**\:   :py:class:`Offer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer>`
                            
                            .. attribute:: release
                            
                            	DHCP release packets
                            	**type**\:   :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: request
                            
                            	DHCP request packets
                            	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ack = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack()
                                self.ack.parent = self
                                self.bootp_reply = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply()
                                self.bootp_reply.parent = self
                                self.bootp_request = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest()
                                self.bootp_request.parent = self
                                self.decline = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self.discover = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover()
                                self.discover.parent = self
                                self.inform = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self.lease_active = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive()
                                self.lease_active.parent = self
                                self.lease_not_assigned = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned()
                                self.lease_not_assigned.parent = self
                                self.lease_query = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self.lease_unknown = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown()
                                self.lease_unknown.parent = self
                                self.nak = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak()
                                self.nak.parent = self
                                self.offer = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer()
                                self.offer.parent = self
                                self.release = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self.request = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self


                            class Discover(object):
                                """
                                DHCP discover packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:discover'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover']['meta_info']


                            class Offer(object):
                                """
                                DHCP offer packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:offer'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer']['meta_info']


                            class Request(object):
                                """
                                DHCP request packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:request'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request']['meta_info']


                            class Decline(object):
                                """
                                DHCP decline packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:decline'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline']['meta_info']


                            class Ack(object):
                                """
                                DHCP ack packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack']['meta_info']


                            class Nak(object):
                                """
                                DHCP nak packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:nak'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak']['meta_info']


                            class Release(object):
                                """
                                DHCP release packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:release'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release']['meta_info']


                            class Inform(object):
                                """
                                DHCP inform packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:inform'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform']['meta_info']


                            class LeaseQuery(object):
                                """
                                DHCP lease query packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-query'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info']


                            class LeaseNotAssigned(object):
                                """
                                DHCP lease not assigned
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-not-assigned'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned']['meta_info']


                            class LeaseUnknown(object):
                                """
                                DHCP lease unknown
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-unknown'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown']['meta_info']


                            class LeaseActive(object):
                                """
                                DHCP lease active
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-active'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive']['meta_info']


                            class BootpRequest(object):
                                """
                                DHCP BOOTP request
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:bootp-request'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest']['meta_info']


                            class BootpReply(object):
                                """
                                DHCP BOOTP reply
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:bootp-reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ack is not None and self.ack._has_data():
                                    return True

                                if self.bootp_reply is not None and self.bootp_reply._has_data():
                                    return True

                                if self.bootp_request is not None and self.bootp_request._has_data():
                                    return True

                                if self.decline is not None and self.decline._has_data():
                                    return True

                                if self.discover is not None and self.discover._has_data():
                                    return True

                                if self.inform is not None and self.inform._has_data():
                                    return True

                                if self.lease_active is not None and self.lease_active._has_data():
                                    return True

                                if self.lease_not_assigned is not None and self.lease_not_assigned._has_data():
                                    return True

                                if self.lease_query is not None and self.lease_query._has_data():
                                    return True

                                if self.lease_unknown is not None and self.lease_unknown._has_data():
                                    return True

                                if self.nak is not None and self.nak._has_data():
                                    return True

                                if self.offer is not None and self.offer._has_data():
                                    return True

                                if self.release is not None and self.release._has_data():
                                    return True

                                if self.request is not None and self.request._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:vrf[Cisco-IOS-XR-ipv4-dhcpd-oper:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.vrf_name is not None:
                                return True

                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:vrfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vrf is not None:
                            for child_ref in self.vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs']['meta_info']


                class Profiles(object):
                    """
                    IPv4 DHCP proxy profile
                    
                    .. attribute:: profile
                    
                    	IPv4 DHCP proxy profile
                    	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.profile = YList()
                        self.profile.parent = self
                        self.profile.name = 'profile'


                    class Profile(object):
                        """
                        IPv4 DHCP proxy profile
                        
                        .. attribute:: profile_name  <key>
                        
                        	Profile name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: gi_addr
                        
                        	Gateway addresses
                        	**type**\:  list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: interface_references
                        
                        	Interface references
                        	**type**\:   :py:class:`InterfaceReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences>`
                        
                        .. attribute:: is_move_allowed
                        
                        	Is true if dhcp subscriber is allowed to move
                        	**type**\:  bool
                        
                        .. attribute:: is_relay_allow_untrusted_enabled
                        
                        	Is true if relay untrusted is enabled
                        	**type**\:  bool
                        
                        .. attribute:: is_relay_check
                        
                        	Is true if relay check enabled
                        	**type**\:  bool
                        
                        .. attribute:: is_relay_option_enabled
                        
                        	Is true if relay option is enabled
                        	**type**\:  bool
                        
                        .. attribute:: is_relay_optionvpn_enabled
                        
                        	Is true if relay VPN enabled
                        	**type**\:  bool
                        
                        .. attribute:: profile_helper_address
                        
                        	Helper addresses
                        	**type**\:  list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: proxy_broadcast_flag_policy
                        
                        	Broadcast policy
                        	**type**\:   :py:class:`BroadcastFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.BroadcastFlagEnum>`
                        
                        .. attribute:: proxy_lease_limit_count
                        
                        	Lease limit count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: proxy_lease_limit_type
                        
                        	Lease limit type
                        	**type**\:   :py:class:`ProxyLeaseLimitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.ProxyLeaseLimitEnum>`
                        
                        .. attribute:: proxy_profile_client_lease_time
                        
                        	Client lease time in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: relay_authenticate
                        
                        	Relay authenticate
                        	**type**\:   :py:class:`RelayInfoAuthenticateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.RelayInfoAuthenticateEnum>`
                        
                        .. attribute:: relay_optionvpn_enabled_mode
                        
                        	Relay VPN RFC/Cisco mode
                        	**type**\:   :py:class:`RelayInfoVpnModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.RelayInfoVpnModeEnum>`
                        
                        .. attribute:: relay_policy
                        
                        	Relay policy
                        	**type**\:   :py:class:`RelayInfoPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.RelayInfoPolicyEnum>`
                        
                        .. attribute:: vrf_name
                        
                        	VRF names
                        	**type**\:  list of str
                        
                        	**length:** 0..33
                        
                        .. attribute:: vrf_references
                        
                        	VRF references
                        	**type**\:   :py:class:`VrfReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.profile_name = None
                            self.gi_addr = YLeafList()
                            self.gi_addr.parent = self
                            self.gi_addr.name = 'gi_addr'
                            self.interface_references = Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences()
                            self.interface_references.parent = self
                            self.is_move_allowed = None
                            self.is_relay_allow_untrusted_enabled = None
                            self.is_relay_check = None
                            self.is_relay_option_enabled = None
                            self.is_relay_optionvpn_enabled = None
                            self.profile_helper_address = YLeafList()
                            self.profile_helper_address.parent = self
                            self.profile_helper_address.name = 'profile_helper_address'
                            self.proxy_broadcast_flag_policy = None
                            self.proxy_lease_limit_count = None
                            self.proxy_lease_limit_type = None
                            self.proxy_profile_client_lease_time = None
                            self.relay_authenticate = None
                            self.relay_optionvpn_enabled_mode = None
                            self.relay_policy = None
                            self.vrf_name = YLeafList()
                            self.vrf_name.parent = self
                            self.vrf_name.name = 'vrf_name'
                            self.vrf_references = Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences()
                            self.vrf_references.parent = self


                        class VrfReferences(object):
                            """
                            VRF references
                            
                            .. attribute:: ipv4_dhcpd_proxy_vrf_reference
                            
                            	ipv4 dhcpd proxy vrf reference
                            	**type**\: list of    :py:class:`Ipv4DhcpdProxyVrfReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences.Ipv4DhcpdProxyVrfReference>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_dhcpd_proxy_vrf_reference = YList()
                                self.ipv4_dhcpd_proxy_vrf_reference.parent = self
                                self.ipv4_dhcpd_proxy_vrf_reference.name = 'ipv4_dhcpd_proxy_vrf_reference'


                            class Ipv4DhcpdProxyVrfReference(object):
                                """
                                ipv4 dhcpd proxy vrf reference
                                
                                .. attribute:: proxy_reference_vrf_name
                                
                                	VRF name
                                	**type**\:  str
                                
                                	**length:** 0..33
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.proxy_reference_vrf_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd-proxy-vrf-reference'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.proxy_reference_vrf_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences.Ipv4DhcpdProxyVrfReference']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:vrf-references'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_dhcpd_proxy_vrf_reference is not None:
                                    for child_ref in self.ipv4_dhcpd_proxy_vrf_reference:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences']['meta_info']


                        class InterfaceReferences(object):
                            """
                            Interface references
                            
                            .. attribute:: ipv4_dhcpd_proxy_interface_reference
                            
                            	ipv4 dhcpd proxy interface reference
                            	**type**\: list of    :py:class:`Ipv4DhcpdProxyInterfaceReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences.Ipv4DhcpdProxyInterfaceReference>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_dhcpd_proxy_interface_reference = YList()
                                self.ipv4_dhcpd_proxy_interface_reference.parent = self
                                self.ipv4_dhcpd_proxy_interface_reference.name = 'ipv4_dhcpd_proxy_interface_reference'


                            class Ipv4DhcpdProxyInterfaceReference(object):
                                """
                                ipv4 dhcpd proxy interface reference
                                
                                .. attribute:: proxy_reference_interface_name
                                
                                	Interface name
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.proxy_reference_interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd-proxy-interface-reference'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.proxy_reference_interface_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences.Ipv4DhcpdProxyInterfaceReference']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:interface-references'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_dhcpd_proxy_interface_reference is not None:
                                    for child_ref in self.ipv4_dhcpd_proxy_interface_reference:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.profile_name is None:
                                raise YPYModelError('Key property profile_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:profile[Cisco-IOS-XR-ipv4-dhcpd-oper:profile-name = ' + str(self.profile_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.profile_name is not None:
                                return True

                            if self.gi_addr is not None:
                                for child in self.gi_addr:
                                    if child is not None:
                                        return True

                            if self.interface_references is not None and self.interface_references._has_data():
                                return True

                            if self.is_move_allowed is not None:
                                return True

                            if self.is_relay_allow_untrusted_enabled is not None:
                                return True

                            if self.is_relay_check is not None:
                                return True

                            if self.is_relay_option_enabled is not None:
                                return True

                            if self.is_relay_optionvpn_enabled is not None:
                                return True

                            if self.profile_helper_address is not None:
                                for child in self.profile_helper_address:
                                    if child is not None:
                                        return True

                            if self.proxy_broadcast_flag_policy is not None:
                                return True

                            if self.proxy_lease_limit_count is not None:
                                return True

                            if self.proxy_lease_limit_type is not None:
                                return True

                            if self.proxy_profile_client_lease_time is not None:
                                return True

                            if self.relay_authenticate is not None:
                                return True

                            if self.relay_optionvpn_enabled_mode is not None:
                                return True

                            if self.relay_policy is not None:
                                return True

                            if self.vrf_name is not None:
                                for child in self.vrf_name:
                                    if child is not None:
                                        return True

                            if self.vrf_references is not None and self.vrf_references._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:profiles'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.profile is not None:
                            for child_ref in self.profile:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles']['meta_info']


                class Statistics(object):
                    """
                    DHCP proxy statistics
                    
                    .. attribute:: ipv4_dhcpd_proxy_stat
                    
                    	ipv4 dhcpd proxy stat
                    	**type**\: list of    :py:class:`Ipv4DhcpdProxyStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv4_dhcpd_proxy_stat = YList()
                        self.ipv4_dhcpd_proxy_stat.parent = self
                        self.ipv4_dhcpd_proxy_stat.name = 'ipv4_dhcpd_proxy_stat'


                    class Ipv4DhcpdProxyStat(object):
                        """
                        ipv4 dhcpd proxy stat
                        
                        .. attribute:: statistics
                        
                        	Proxy statistics
                        	**type**\:   :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCP L3 VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.statistics = Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_()
                            self.statistics.parent = self
                            self.vrf_name = None


                        class Statistics_(object):
                            """
                            Proxy statistics
                            
                            .. attribute:: dropped_packets
                            
                            	Dropped packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: received_packets
                            
                            	Received packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: transmitted_packets
                            
                            	Transmitted packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dropped_packets = None
                                self.received_packets = None
                                self.transmitted_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.dropped_packets is not None:
                                    return True

                                if self.received_packets is not None:
                                    return True

                                if self.transmitted_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd-proxy-stat'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv4_dhcpd_proxy_stat is not None:
                            for child_ref in self.ipv4_dhcpd_proxy_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Statistics']['meta_info']


                class Binding(object):
                    """
                    DHCP proxy bindings
                    
                    .. attribute:: clients
                    
                    	DHCP proxy client bindings
                    	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients>`
                    
                    .. attribute:: summary
                    
                    	DHCP proxy binding summary
                    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.clients = Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients()
                        self.clients.parent = self
                        self.summary = Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary()
                        self.summary.parent = self


                    class Clients(object):
                        """
                        DHCP proxy client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCP proxy binding
                        	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.client = YList()
                            self.client.parent = self
                            self.client.name = 'client'


                        class Client(object):
                            """
                            Single DHCP proxy binding
                            
                            .. attribute:: client_id  <key>
                            
                            	Client ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: access_vrf_name
                            
                            	DHCP access interface VRF name
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: client_gi_addr
                            
                            	DHCP client GIADDR
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: client_id_xr
                            
                            	DHCP client identifier
                            	**type**\:  str
                            
                            	**length:** 0..1275
                            
                            .. attribute:: event_history
                            
                            	event history
                            	**type**\:  list of int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	DHCP access interface to client
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: ip_address
                            
                            	DHCP IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: is_auth_received
                            
                            	Is true if authentication is on received option82
                            	**type**\:  bool
                            
                            .. attribute:: is_mbl_subscriber
                            
                            	Is true if DHCP subscriber is Mobile
                            	**type**\:  bool
                            
                            .. attribute:: is_nak_next_renew
                            
                            	Is true if DHCP next renew from client will be NAK'd
                            	**type**\:  bool
                            
                            .. attribute:: lease_time
                            
                            	Lease time in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: mac_address
                            
                            	DHCP client MAC address
                            	**type**\:  str
                            
                            .. attribute:: old_subscriber_label
                            
                            	DHCP old subscriber label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: param_request
                            
                            	DHCP parameter request option
                            	**type**\:  str
                            
                            	**length:** 0..513
                            
                            .. attribute:: param_response
                            
                            	DHCP saved options
                            	**type**\:  str
                            
                            	**length:** 0..2051
                            
                            .. attribute:: profile_name
                            
                            	DHCP profile name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            .. attribute:: proxy_binding_inner_tag
                            
                            	DHCP VLAN inner VLAN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_binding_outer_tag
                            
                            	DHCP VLAN outer VLAN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: remaining_lease_time
                            
                            	Remaining lease time in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: reply_server_ip_address
                            
                            	DHCP reply server IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: rx_circuit_id
                            
                            	DHCP received circuit ID
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: rx_remote_id
                            
                            	DHCP received Remote ID
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: rx_vsiso
                            
                            	DHCP received VSISO
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: server_ip_address
                            
                            	DHCP server IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: server_vrf_name
                            
                            	DHCP server VRF name
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: session_start_time
                            
                            	session start time
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: srg_state
                            
                            	DHCPV4 SRG state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state
                            
                            	DHCP client state
                            	**type**\:   :py:class:`BagDhcpdProxyStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.BagDhcpdProxyStateEnum>`
                            
                            .. attribute:: subscriber_interface_name
                            
                            	DHCP subscriber interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: subscriber_label
                            
                            	DHCP subscriber label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: to_server_gi_addr
                            
                            	DHCP to server GIADDR
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: tx_circuit_id
                            
                            	DHCP transmitted circuit ID
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: tx_remote_id
                            
                            	DHCP transmitted Remote ID
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: tx_vsiso
                            
                            	DHCP transmitted VSISO
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: vrf_name
                            
                            	DHCP client/subscriber VRF name
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.client_id = None
                                self.access_vrf_name = None
                                self.client_gi_addr = None
                                self.client_id_xr = None
                                self.event_history = YLeafList()
                                self.event_history.parent = self
                                self.event_history.name = 'event_history'
                                self.interface_name = None
                                self.ip_address = None
                                self.is_auth_received = None
                                self.is_mbl_subscriber = None
                                self.is_nak_next_renew = None
                                self.lease_time = None
                                self.mac_address = None
                                self.old_subscriber_label = None
                                self.param_request = None
                                self.param_response = None
                                self.profile_name = None
                                self.proxy_binding_inner_tag = None
                                self.proxy_binding_outer_tag = None
                                self.remaining_lease_time = None
                                self.reply_server_ip_address = None
                                self.rx_circuit_id = None
                                self.rx_remote_id = None
                                self.rx_vsiso = None
                                self.server_ip_address = None
                                self.server_vrf_name = None
                                self.session_start_time = None
                                self.srg_state = None
                                self.state = None
                                self.subscriber_interface_name = None
                                self.subscriber_label = None
                                self.to_server_gi_addr = None
                                self.tx_circuit_id = None
                                self.tx_remote_id = None
                                self.tx_vsiso = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.client_id is None:
                                    raise YPYModelError('Key property client_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:client[Cisco-IOS-XR-ipv4-dhcpd-oper:client-id = ' + str(self.client_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.client_id is not None:
                                    return True

                                if self.access_vrf_name is not None:
                                    return True

                                if self.client_gi_addr is not None:
                                    return True

                                if self.client_id_xr is not None:
                                    return True

                                if self.event_history is not None:
                                    for child in self.event_history:
                                        if child is not None:
                                            return True

                                if self.interface_name is not None:
                                    return True

                                if self.ip_address is not None:
                                    return True

                                if self.is_auth_received is not None:
                                    return True

                                if self.is_mbl_subscriber is not None:
                                    return True

                                if self.is_nak_next_renew is not None:
                                    return True

                                if self.lease_time is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.old_subscriber_label is not None:
                                    return True

                                if self.param_request is not None:
                                    return True

                                if self.param_response is not None:
                                    return True

                                if self.profile_name is not None:
                                    return True

                                if self.proxy_binding_inner_tag is not None:
                                    return True

                                if self.proxy_binding_outer_tag is not None:
                                    return True

                                if self.remaining_lease_time is not None:
                                    return True

                                if self.reply_server_ip_address is not None:
                                    return True

                                if self.rx_circuit_id is not None:
                                    return True

                                if self.rx_remote_id is not None:
                                    return True

                                if self.rx_vsiso is not None:
                                    return True

                                if self.server_ip_address is not None:
                                    return True

                                if self.server_vrf_name is not None:
                                    return True

                                if self.session_start_time is not None:
                                    return True

                                if self.srg_state is not None:
                                    return True

                                if self.state is not None:
                                    return True

                                if self.subscriber_interface_name is not None:
                                    return True

                                if self.subscriber_label is not None:
                                    return True

                                if self.to_server_gi_addr is not None:
                                    return True

                                if self.tx_circuit_id is not None:
                                    return True

                                if self.tx_remote_id is not None:
                                    return True

                                if self.tx_vsiso is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients.Client']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:clients'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.client is not None:
                                for child_ref in self.client:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients']['meta_info']


                    class Summary(object):
                        """
                        DHCP proxy binding summary
                        
                        .. attribute:: ack_waiting_for_dpm
                        
                        	Number of clients in Waiting for DPM with ACK
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bound_clients
                        
                        	Number of clients in bound state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: deleting_clients_d
                        
                        	Number of clients in deleting state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: disconnected_clients
                        
                        	Number of clients in disconnected state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: informing_clients
                        
                        	Number of clients in informing state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: initializing_clients
                        
                        	Number of clients in init state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: offer_sent_for_client
                        
                        	Number of clients in Offer sent state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reauthorizing_clients
                        
                        	Number of clients in reauth state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: renewing_clients
                        
                        	Number of clients in renewing state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: request_waiting_for_dpm
                        
                        	Number of clients in Waiting for DPM with Request
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: requesting_clients
                        
                        	Number of clients in requesting state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: restarting_clients
                        
                        	Number of clients in restarting state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: selecting_clients
                        
                        	Number of clients in selecting state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_daps_init
                        
                        	Number of clients in Init DAPS wait state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_addr_change
                        
                        	Number of clients in Waiting for DPM after addr change
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_disconnect
                        
                        	Number of clients in waiting for DPM disconnect state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_init
                        
                        	Number of clients in Init DPM wait state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ack_waiting_for_dpm = None
                            self.bound_clients = None
                            self.clients = None
                            self.deleting_clients_d = None
                            self.disconnected_clients = None
                            self.informing_clients = None
                            self.initializing_clients = None
                            self.offer_sent_for_client = None
                            self.reauthorizing_clients = None
                            self.renewing_clients = None
                            self.request_waiting_for_dpm = None
                            self.requesting_clients = None
                            self.restarting_clients = None
                            self.selecting_clients = None
                            self.waiting_for_daps_init = None
                            self.waiting_for_dpm_addr_change = None
                            self.waiting_for_dpm_disconnect = None
                            self.waiting_for_dpm_init = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ack_waiting_for_dpm is not None:
                                return True

                            if self.bound_clients is not None:
                                return True

                            if self.clients is not None:
                                return True

                            if self.deleting_clients_d is not None:
                                return True

                            if self.disconnected_clients is not None:
                                return True

                            if self.informing_clients is not None:
                                return True

                            if self.initializing_clients is not None:
                                return True

                            if self.offer_sent_for_client is not None:
                                return True

                            if self.reauthorizing_clients is not None:
                                return True

                            if self.renewing_clients is not None:
                                return True

                            if self.request_waiting_for_dpm is not None:
                                return True

                            if self.requesting_clients is not None:
                                return True

                            if self.restarting_clients is not None:
                                return True

                            if self.selecting_clients is not None:
                                return True

                            if self.waiting_for_daps_init is not None:
                                return True

                            if self.waiting_for_dpm_addr_change is not None:
                                return True

                            if self.waiting_for_dpm_disconnect is not None:
                                return True

                            if self.waiting_for_dpm_init is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:binding'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.clients is not None and self.clients._has_data():
                            return True

                        if self.summary is not None and self.summary._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Binding']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:proxy'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.binding is not None and self.binding._has_data():
                        return True

                    if self.profiles is not None and self.profiles._has_data():
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.statistics_info is not None and self.statistics_info._has_data():
                        return True

                    if self.vrfs is not None and self.vrfs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Proxy']['meta_info']


            class Interfaces(object):
                """
                IPv4 DHCP proxy/server Interface
                
                .. attribute:: interface
                
                	IPv4 DHCP proxy/server interface info
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    IPv4 DHCP proxy/server interface info
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: intf_ifhandle
                    
                    	Ifhandle of the interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: intf_is_ambiguous
                    
                    	Is interface ambiguous
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: intf_lease_limit_count
                    
                    	Lease limit count on interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: intf_lease_limit_type
                    
                    	Lease limit type on interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: intf_mode
                    
                    	Mode of interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: intf_profile_name
                    
                    	Name of profile attached to the interface
                    	**type**\:  str
                    
                    	**length:** 0..65
                    
                    .. attribute:: mac_throttle
                    
                    	Mac Throttle Status
                    	**type**\:  bool
                    
                    .. attribute:: srg_role
                    
                    	DHCPv6 Interface SRG role
                    	**type**\:   :py:class:`BagDhcpdIntfSrgRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.BagDhcpdIntfSrgRoleEnum>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\:  str
                    
                    	**length:** 0..33
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.intf_ifhandle = None
                        self.intf_is_ambiguous = None
                        self.intf_lease_limit_count = None
                        self.intf_lease_limit_type = None
                        self.intf_mode = None
                        self.intf_profile_name = None
                        self.mac_throttle = None
                        self.srg_role = None
                        self.vrf_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:interface[Cisco-IOS-XR-ipv4-dhcpd-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.intf_ifhandle is not None:
                            return True

                        if self.intf_is_ambiguous is not None:
                            return True

                        if self.intf_lease_limit_count is not None:
                            return True

                        if self.intf_lease_limit_type is not None:
                            return True

                        if self.intf_mode is not None:
                            return True

                        if self.intf_profile_name is not None:
                            return True

                        if self.mac_throttle is not None:
                            return True

                        if self.srg_role is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:interfaces'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Interfaces']['meta_info']


            class Base(object):
                """
                IPv4 DHCP base operational data
                
                .. attribute:: database
                
                	IPv4 DHCP database
                	**type**\:   :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Database>`
                
                .. attribute:: issu_status
                
                	IPv4 DHCP ISSU status
                	**type**\:   :py:class:`IssuStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.IssuStatus>`
                
                .. attribute:: profiles
                
                	IPv4 DHCP Base profile
                	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles>`
                
                .. attribute:: statistics
                
                	DHCP base statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Statistics>`
                
                .. attribute:: vrfs
                
                	DHCP base list of VRF names
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.database = Ipv4Dhcpd.Nodes.Node.Base.Database()
                    self.database.parent = self
                    self.issu_status = Ipv4Dhcpd.Nodes.Node.Base.IssuStatus()
                    self.issu_status.parent = self
                    self.profiles = Ipv4Dhcpd.Nodes.Node.Base.Profiles()
                    self.profiles.parent = self
                    self.statistics = Ipv4Dhcpd.Nodes.Node.Base.Statistics()
                    self.statistics.parent = self
                    self.vrfs = Ipv4Dhcpd.Nodes.Node.Base.Vrfs()
                    self.vrfs.parent = self


                class Statistics(object):
                    """
                    DHCP base statistics
                    
                    .. attribute:: ipv4_dhcpd_proxy_stat
                    
                    	ipv4 dhcpd proxy stat
                    	**type**\: list of    :py:class:`Ipv4DhcpdProxyStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv4_dhcpd_proxy_stat = YList()
                        self.ipv4_dhcpd_proxy_stat.parent = self
                        self.ipv4_dhcpd_proxy_stat.name = 'ipv4_dhcpd_proxy_stat'


                    class Ipv4DhcpdProxyStat(object):
                        """
                        ipv4 dhcpd proxy stat
                        
                        .. attribute:: statistics
                        
                        	Proxy statistics
                        	**type**\:   :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCP L3 VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.statistics = Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_()
                            self.statistics.parent = self
                            self.vrf_name = None


                        class Statistics_(object):
                            """
                            Proxy statistics
                            
                            .. attribute:: dropped_packets
                            
                            	Dropped packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: received_packets
                            
                            	Received packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: transmitted_packets
                            
                            	Transmitted packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dropped_packets = None
                                self.received_packets = None
                                self.transmitted_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.dropped_packets is not None:
                                    return True

                                if self.received_packets is not None:
                                    return True

                                if self.transmitted_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd-proxy-stat'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv4_dhcpd_proxy_stat is not None:
                            for child_ref in self.ipv4_dhcpd_proxy_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Statistics']['meta_info']


                class IssuStatus(object):
                    """
                    IPv4 DHCP ISSU status
                    
                    .. attribute:: big_bang_time
                    
                    	Timestamp for the Big Bang notification time in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: issu_ready_entries_replicate
                    
                    	Whether or not DHCP has received all replicated entries during the ISSU Load Phase
                    	**type**\:  bool
                    
                    .. attribute:: issu_ready_issu_mgr_connection
                    
                    	Whether or not DHCP is currently connected to ISSU Manager during the ISSU Load Phase
                    	**type**\:  bool
                    
                    .. attribute:: issu_ready_time
                    
                    	Timestamp for the ISSU ready declaration in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: issu_sync_complete_time
                    
                    	Timestamp for the ISSU sync complete in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: issu_sync_start_time
                    
                    	Timestamp for the ISSU sync start in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC, January 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: phase
                    
                    	The current ISSU phase of the DHCP process
                    	**type**\:   :py:class:`DhcpIssuPhaseEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpIssuPhaseEnum>`
                    
                    .. attribute:: primary_role_time
                    
                    	Timestamp for the change to Primary role notification time in nanoseconds since Epoch, i .e. since 00\:00\:00 UTC, January 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: role
                    
                    	The current role of the DHCP process
                    	**type**\:   :py:class:`DhcpIssuRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpIssuRoleEnum>`
                    
                    .. attribute:: version
                    
                    	The current version of the DHCP process in the context of an ISSU
                    	**type**\:   :py:class:`DhcpIssuVersionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpIssuVersionEnum>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.big_bang_time = None
                        self.issu_ready_entries_replicate = None
                        self.issu_ready_issu_mgr_connection = None
                        self.issu_ready_time = None
                        self.issu_sync_complete_time = None
                        self.issu_sync_start_time = None
                        self.phase = None
                        self.primary_role_time = None
                        self.role = None
                        self.version = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:issu-status'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.big_bang_time is not None:
                            return True

                        if self.issu_ready_entries_replicate is not None:
                            return True

                        if self.issu_ready_issu_mgr_connection is not None:
                            return True

                        if self.issu_ready_time is not None:
                            return True

                        if self.issu_sync_complete_time is not None:
                            return True

                        if self.issu_sync_start_time is not None:
                            return True

                        if self.phase is not None:
                            return True

                        if self.primary_role_time is not None:
                            return True

                        if self.role is not None:
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.IssuStatus']['meta_info']


                class Vrfs(object):
                    """
                    DHCP base list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv4 DHCP base VRF name
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        IPv4 DHCP base VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv4 DHCP base statistics
                        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.statistics = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self


                        class Statistics(object):
                            """
                            IPv4 DHCP base statistics
                            
                            .. attribute:: ack
                            
                            	DHCP ack packets
                            	**type**\:   :py:class:`Ack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack>`
                            
                            .. attribute:: bootp_reply
                            
                            	DHCP BOOTP reply
                            	**type**\:   :py:class:`BootpReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply>`
                            
                            .. attribute:: bootp_request
                            
                            	DHCP BOOTP request
                            	**type**\:   :py:class:`BootpRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest>`
                            
                            .. attribute:: decline
                            
                            	DHCP decline packets
                            	**type**\:   :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: discover
                            
                            	DHCP discover packets
                            	**type**\:   :py:class:`Discover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover>`
                            
                            .. attribute:: inform
                            
                            	DHCP inform packets
                            	**type**\:   :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: lease_active
                            
                            	DHCP lease active
                            	**type**\:   :py:class:`LeaseActive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive>`
                            
                            .. attribute:: lease_not_assigned
                            
                            	DHCP lease not assigned
                            	**type**\:   :py:class:`LeaseNotAssigned <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned>`
                            
                            .. attribute:: lease_query
                            
                            	DHCP lease query packets
                            	**type**\:   :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_unknown
                            
                            	DHCP lease unknown
                            	**type**\:   :py:class:`LeaseUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown>`
                            
                            .. attribute:: nak
                            
                            	DHCP nak packets
                            	**type**\:   :py:class:`Nak <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak>`
                            
                            .. attribute:: offer
                            
                            	DHCP offer packets
                            	**type**\:   :py:class:`Offer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer>`
                            
                            .. attribute:: release
                            
                            	DHCP release packets
                            	**type**\:   :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: request
                            
                            	DHCP request packets
                            	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ack = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack()
                                self.ack.parent = self
                                self.bootp_reply = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply()
                                self.bootp_reply.parent = self
                                self.bootp_request = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest()
                                self.bootp_request.parent = self
                                self.decline = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self.discover = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover()
                                self.discover.parent = self
                                self.inform = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self.lease_active = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive()
                                self.lease_active.parent = self
                                self.lease_not_assigned = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned()
                                self.lease_not_assigned.parent = self
                                self.lease_query = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self.lease_unknown = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown()
                                self.lease_unknown.parent = self
                                self.nak = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak()
                                self.nak.parent = self
                                self.offer = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer()
                                self.offer.parent = self
                                self.release = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self.request = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self


                            class Discover(object):
                                """
                                DHCP discover packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:discover'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover']['meta_info']


                            class Offer(object):
                                """
                                DHCP offer packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:offer'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer']['meta_info']


                            class Request(object):
                                """
                                DHCP request packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:request'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request']['meta_info']


                            class Decline(object):
                                """
                                DHCP decline packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:decline'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline']['meta_info']


                            class Ack(object):
                                """
                                DHCP ack packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack']['meta_info']


                            class Nak(object):
                                """
                                DHCP nak packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:nak'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak']['meta_info']


                            class Release(object):
                                """
                                DHCP release packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:release'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release']['meta_info']


                            class Inform(object):
                                """
                                DHCP inform packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:inform'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform']['meta_info']


                            class LeaseQuery(object):
                                """
                                DHCP lease query packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-query'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info']


                            class LeaseNotAssigned(object):
                                """
                                DHCP lease not assigned
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-not-assigned'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned']['meta_info']


                            class LeaseUnknown(object):
                                """
                                DHCP lease unknown
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-unknown'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown']['meta_info']


                            class LeaseActive(object):
                                """
                                DHCP lease active
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-active'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive']['meta_info']


                            class BootpRequest(object):
                                """
                                DHCP BOOTP request
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:bootp-request'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest']['meta_info']


                            class BootpReply(object):
                                """
                                DHCP BOOTP reply
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:bootp-reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ack is not None and self.ack._has_data():
                                    return True

                                if self.bootp_reply is not None and self.bootp_reply._has_data():
                                    return True

                                if self.bootp_request is not None and self.bootp_request._has_data():
                                    return True

                                if self.decline is not None and self.decline._has_data():
                                    return True

                                if self.discover is not None and self.discover._has_data():
                                    return True

                                if self.inform is not None and self.inform._has_data():
                                    return True

                                if self.lease_active is not None and self.lease_active._has_data():
                                    return True

                                if self.lease_not_assigned is not None and self.lease_not_assigned._has_data():
                                    return True

                                if self.lease_query is not None and self.lease_query._has_data():
                                    return True

                                if self.lease_unknown is not None and self.lease_unknown._has_data():
                                    return True

                                if self.nak is not None and self.nak._has_data():
                                    return True

                                if self.offer is not None and self.offer._has_data():
                                    return True

                                if self.release is not None and self.release._has_data():
                                    return True

                                if self.request is not None and self.request._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:vrf[Cisco-IOS-XR-ipv4-dhcpd-oper:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.vrf_name is not None:
                                return True

                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:vrfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vrf is not None:
                            for child_ref in self.vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs']['meta_info']


                class Profiles(object):
                    """
                    IPv4 DHCP Base profile
                    
                    .. attribute:: profile
                    
                    	IPv4 DHCP base profile
                    	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.profile = YList()
                        self.profile.parent = self
                        self.profile.name = 'profile'


                    class Profile(object):
                        """
                        IPv4 DHCP base profile
                        
                        .. attribute:: profile_name  <key>
                        
                        	Profile name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: base_default_profile_name
                        
                        	Base Default Profile name
                        	**type**\:  str
                        
                        	**length:** 0..65
                        
                        .. attribute:: child_profile_count
                        
                        	Child profile count
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: child_profile_info
                        
                        	child profile info
                        	**type**\:   :py:class:`ChildProfileInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo>`
                        
                        .. attribute:: default_profile_mode
                        
                        	Default Profile mode
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: interface_references
                        
                        	Interface references
                        	**type**\:   :py:class:`InterfaceReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences>`
                        
                        .. attribute:: intf_ref_count
                        
                        	Interface reference count
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_authenticate
                        
                        	Relay authenticate
                        	**type**\:   :py:class:`RelayInfoAuthenticateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.RelayInfoAuthenticateEnum>`
                        
                        .. attribute:: remote_id
                        
                        	DHCP configured Remote ID
                        	**type**\:  str
                        
                        	**length:** 0..768
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.profile_name = None
                            self.base_default_profile_name = None
                            self.child_profile_count = None
                            self.child_profile_info = Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo()
                            self.child_profile_info.parent = self
                            self.default_profile_mode = None
                            self.interface_references = Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences()
                            self.interface_references.parent = self
                            self.intf_ref_count = None
                            self.relay_authenticate = None
                            self.remote_id = None


                        class InterfaceReferences(object):
                            """
                            Interface references
                            
                            .. attribute:: ipv4_dhcpd_base_interface_reference
                            
                            	ipv4 dhcpd base interface reference
                            	**type**\: list of    :py:class:`Ipv4DhcpdBaseInterfaceReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences.Ipv4DhcpdBaseInterfaceReference>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_dhcpd_base_interface_reference = YList()
                                self.ipv4_dhcpd_base_interface_reference.parent = self
                                self.ipv4_dhcpd_base_interface_reference.name = 'ipv4_dhcpd_base_interface_reference'


                            class Ipv4DhcpdBaseInterfaceReference(object):
                                """
                                ipv4 dhcpd base interface reference
                                
                                .. attribute:: base_reference_interface_name
                                
                                	Interface name
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.base_reference_interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd-base-interface-reference'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.base_reference_interface_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences.Ipv4DhcpdBaseInterfaceReference']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:interface-references'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_dhcpd_base_interface_reference is not None:
                                    for child_ref in self.ipv4_dhcpd_base_interface_reference:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences']['meta_info']


                        class ChildProfileInfo(object):
                            """
                            child profile info
                            
                            .. attribute:: ipv4_dhcpd_base_child_profile_info
                            
                            	ipv4 dhcpd base child profile info
                            	**type**\: list of    :py:class:`Ipv4DhcpdBaseChildProfileInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo.Ipv4DhcpdBaseChildProfileInfo>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_dhcpd_base_child_profile_info = YList()
                                self.ipv4_dhcpd_base_child_profile_info.parent = self
                                self.ipv4_dhcpd_base_child_profile_info.name = 'ipv4_dhcpd_base_child_profile_info'


                            class Ipv4DhcpdBaseChildProfileInfo(object):
                                """
                                ipv4 dhcpd base child profile info
                                
                                .. attribute:: base_child_profile_name
                                
                                	Base Child Profile name
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                .. attribute:: matched_option_code
                                
                                	Matched option code
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: matched_option_len
                                
                                	Matched option len
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: mode
                                
                                	Profile mode
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: option_data
                                
                                	Matched option data
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.base_child_profile_name = None
                                    self.matched_option_code = None
                                    self.matched_option_len = None
                                    self.mode = None
                                    self.option_data = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd-base-child-profile-info'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.base_child_profile_name is not None:
                                        return True

                                    if self.matched_option_code is not None:
                                        return True

                                    if self.matched_option_len is not None:
                                        return True

                                    if self.mode is not None:
                                        return True

                                    if self.option_data is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo.Ipv4DhcpdBaseChildProfileInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:child-profile-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ipv4_dhcpd_base_child_profile_info is not None:
                                    for child_ref in self.ipv4_dhcpd_base_child_profile_info:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.profile_name is None:
                                raise YPYModelError('Key property profile_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:profile[Cisco-IOS-XR-ipv4-dhcpd-oper:profile-name = ' + str(self.profile_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.profile_name is not None:
                                return True

                            if self.base_default_profile_name is not None:
                                return True

                            if self.child_profile_count is not None:
                                return True

                            if self.child_profile_info is not None and self.child_profile_info._has_data():
                                return True

                            if self.default_profile_mode is not None:
                                return True

                            if self.interface_references is not None and self.interface_references._has_data():
                                return True

                            if self.intf_ref_count is not None:
                                return True

                            if self.relay_authenticate is not None:
                                return True

                            if self.remote_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:profiles'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.profile is not None:
                            for child_ref in self.profile:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles']['meta_info']


                class Database(object):
                    """
                    IPv4 DHCP database
                    
                    .. attribute:: configured
                    
                    	Database feature configured
                    	**type**\:  bool
                    
                    .. attribute:: failed_full_file_write_count
                    
                    	Failed full file write count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: failed_incremental_file_write_count
                    
                    	Failed incremental file write count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: full_file_record_count
                    
                    	Full file record count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: full_file_write_count
                    
                    	Full file write count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: full_file_write_interval
                    
                    	Full file write interval in minutes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    .. attribute:: incremental_file_record_count
                    
                    	Incremental file record count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incremental_file_write_count
                    
                    	Incremental file write count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incremental_file_write_interval
                    
                    	Incremental file write interval in minutes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    .. attribute:: last_full_file_write_error_timestamp
                    
                    	Last full file write error timestamp since epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_full_write_file_name
                    
                    	Last full write file name
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: last_full_write_time
                    
                    	Last full write time since epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_incremental_file_write_error_timestamp
                    
                    	Last incremental file write error timestamp since epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_incremental_write_file_name
                    
                    	Last incremental write file name
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: last_incremental_write_time
                    
                    	Last incremental write time since epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: version
                    
                    	Current file version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.configured = None
                        self.failed_full_file_write_count = None
                        self.failed_incremental_file_write_count = None
                        self.full_file_record_count = None
                        self.full_file_write_count = None
                        self.full_file_write_interval = None
                        self.incremental_file_record_count = None
                        self.incremental_file_write_count = None
                        self.incremental_file_write_interval = None
                        self.last_full_file_write_error_timestamp = None
                        self.last_full_write_file_name = None
                        self.last_full_write_time = None
                        self.last_incremental_file_write_error_timestamp = None
                        self.last_incremental_write_file_name = None
                        self.last_incremental_write_time = None
                        self.version = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:database'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.configured is not None:
                            return True

                        if self.failed_full_file_write_count is not None:
                            return True

                        if self.failed_incremental_file_write_count is not None:
                            return True

                        if self.full_file_record_count is not None:
                            return True

                        if self.full_file_write_count is not None:
                            return True

                        if self.full_file_write_interval is not None:
                            return True

                        if self.incremental_file_record_count is not None:
                            return True

                        if self.incremental_file_write_count is not None:
                            return True

                        if self.incremental_file_write_interval is not None:
                            return True

                        if self.last_full_file_write_error_timestamp is not None:
                            return True

                        if self.last_full_write_file_name is not None:
                            return True

                        if self.last_full_write_time is not None:
                            return True

                        if self.last_incremental_file_write_error_timestamp is not None:
                            return True

                        if self.last_incremental_write_file_name is not None:
                            return True

                        if self.last_incremental_write_time is not None:
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base.Database']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:base'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.database is not None and self.database._has_data():
                        return True

                    if self.issu_status is not None and self.issu_status._has_data():
                        return True

                    if self.profiles is not None and self.profiles._has_data():
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.vrfs is not None and self.vrfs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Base']['meta_info']


            class Server(object):
                """
                IPv4 DHCP Server operational data
                
                .. attribute:: binding
                
                	DHCP server bindings
                	**type**\:   :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Binding>`
                
                .. attribute:: profiles
                
                	IPv4 DHCP Server profile
                	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Profiles>`
                
                .. attribute:: statistics
                
                	DHCP Server statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Statistics>`
                
                .. attribute:: statistics_info
                
                	DHCP proxy stats info
                	**type**\:   :py:class:`StatisticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo>`
                
                .. attribute:: vrfs
                
                	DHCP Server list of VRF names
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.binding = Ipv4Dhcpd.Nodes.Node.Server.Binding()
                    self.binding.parent = self
                    self.profiles = Ipv4Dhcpd.Nodes.Node.Server.Profiles()
                    self.profiles.parent = self
                    self.statistics = Ipv4Dhcpd.Nodes.Node.Server.Statistics()
                    self.statistics.parent = self
                    self.statistics_info = Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo()
                    self.statistics_info.parent = self
                    self.vrfs = Ipv4Dhcpd.Nodes.Node.Server.Vrfs()
                    self.vrfs.parent = self


                class Profiles(object):
                    """
                    IPv4 DHCP Server profile
                    
                    .. attribute:: profile
                    
                    	IPv4 DHCP server profile
                    	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.profile = YList()
                        self.profile.parent = self
                        self.profile.name = 'profile'


                    class Profile(object):
                        """
                        IPv4 DHCP server profile
                        
                        .. attribute:: server_profile_name  <key>
                        
                        	Profile name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: bcast_policy
                        
                        	Bcast Policy
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: duplicate_ip_address_check
                        
                        	Duplicate IP Address Check
                        	**type**\:  bool
                        
                        .. attribute:: duplicate_mac_address_check
                        
                        	Duplicate MAC Address Check
                        	**type**\:  bool
                        
                        .. attribute:: giaddr_policy
                        
                        	Giaddr Policy
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_move_allowed
                        
                        	Is true if dhcp subscriber is allowed to move
                        	**type**\:  bool
                        
                        .. attribute:: lease_limit_count
                        
                        	Lease Limit Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lease_limit_type
                        
                        	Lease Limit Type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: requested_address_check
                        
                        	Requested Address Check
                        	**type**\:  bool
                        
                        .. attribute:: secure_arp
                        
                        	Secure ARP
                        	**type**\:  bool
                        
                        .. attribute:: server_bootfile_name
                        
                        	Server Bootfile name
                        	**type**\:  str
                        
                        	**length:** 0..256
                        
                        .. attribute:: server_domain_name
                        
                        	Server Domain name
                        	**type**\:  str
                        
                        	**length:** 0..256
                        
                        .. attribute:: server_id_check
                        
                        	Server ID Check
                        	**type**\:  bool
                        
                        .. attribute:: server_pool_name
                        
                        	Pool Name
                        	**type**\:  str
                        
                        	**length:** 0..65
                        
                        .. attribute:: server_profile_default_router
                        
                        	Server default addresses
                        	**type**\:  list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: server_profile_dns
                        
                        	Server DNS addresses
                        	**type**\:  list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: server_profile_lease
                        
                        	Lease
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: server_profile_name_xr
                        
                        	Profile Name
                        	**type**\:  str
                        
                        	**length:** 0..65
                        
                        .. attribute:: server_profile_netbios_name_svr_count
                        
                        	Server netbios svr count 
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: server_profile_netbios_node_type
                        
                        	Server netbios node type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: server_profile_netbious_name_server
                        
                        	Server netbios addresses
                        	**type**\:  list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: server_profile_server_dns_count
                        
                        	Server DNS Count
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: server_profile_time_server
                        
                        	Server Time addresses
                        	**type**\:  list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: server_profile_time_svr_count
                        
                        	Server time svr count 
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: server_profiledefault_router_count
                        
                        	Server default count 
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: server_profileiedge_check
                        
                        	Server iEdge Check
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: subnet_mask
                        
                        	Subnet Mask
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.server_profile_name = None
                            self.bcast_policy = None
                            self.duplicate_ip_address_check = None
                            self.duplicate_mac_address_check = None
                            self.giaddr_policy = None
                            self.is_move_allowed = None
                            self.lease_limit_count = None
                            self.lease_limit_type = None
                            self.requested_address_check = None
                            self.secure_arp = None
                            self.server_bootfile_name = None
                            self.server_domain_name = None
                            self.server_id_check = None
                            self.server_pool_name = None
                            self.server_profile_default_router = YLeafList()
                            self.server_profile_default_router.parent = self
                            self.server_profile_default_router.name = 'server_profile_default_router'
                            self.server_profile_dns = YLeafList()
                            self.server_profile_dns.parent = self
                            self.server_profile_dns.name = 'server_profile_dns'
                            self.server_profile_lease = None
                            self.server_profile_name_xr = None
                            self.server_profile_netbios_name_svr_count = None
                            self.server_profile_netbios_node_type = None
                            self.server_profile_netbious_name_server = YLeafList()
                            self.server_profile_netbious_name_server.parent = self
                            self.server_profile_netbious_name_server.name = 'server_profile_netbious_name_server'
                            self.server_profile_server_dns_count = None
                            self.server_profile_time_server = YLeafList()
                            self.server_profile_time_server.parent = self
                            self.server_profile_time_server.name = 'server_profile_time_server'
                            self.server_profile_time_svr_count = None
                            self.server_profiledefault_router_count = None
                            self.server_profileiedge_check = None
                            self.subnet_mask = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.server_profile_name is None:
                                raise YPYModelError('Key property server_profile_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:profile[Cisco-IOS-XR-ipv4-dhcpd-oper:server-profile-name = ' + str(self.server_profile_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.server_profile_name is not None:
                                return True

                            if self.bcast_policy is not None:
                                return True

                            if self.duplicate_ip_address_check is not None:
                                return True

                            if self.duplicate_mac_address_check is not None:
                                return True

                            if self.giaddr_policy is not None:
                                return True

                            if self.is_move_allowed is not None:
                                return True

                            if self.lease_limit_count is not None:
                                return True

                            if self.lease_limit_type is not None:
                                return True

                            if self.requested_address_check is not None:
                                return True

                            if self.secure_arp is not None:
                                return True

                            if self.server_bootfile_name is not None:
                                return True

                            if self.server_domain_name is not None:
                                return True

                            if self.server_id_check is not None:
                                return True

                            if self.server_pool_name is not None:
                                return True

                            if self.server_profile_default_router is not None:
                                for child in self.server_profile_default_router:
                                    if child is not None:
                                        return True

                            if self.server_profile_dns is not None:
                                for child in self.server_profile_dns:
                                    if child is not None:
                                        return True

                            if self.server_profile_lease is not None:
                                return True

                            if self.server_profile_name_xr is not None:
                                return True

                            if self.server_profile_netbios_name_svr_count is not None:
                                return True

                            if self.server_profile_netbios_node_type is not None:
                                return True

                            if self.server_profile_netbious_name_server is not None:
                                for child in self.server_profile_netbious_name_server:
                                    if child is not None:
                                        return True

                            if self.server_profile_server_dns_count is not None:
                                return True

                            if self.server_profile_time_server is not None:
                                for child in self.server_profile_time_server:
                                    if child is not None:
                                        return True

                            if self.server_profile_time_svr_count is not None:
                                return True

                            if self.server_profiledefault_router_count is not None:
                                return True

                            if self.server_profileiedge_check is not None:
                                return True

                            if self.subnet_mask is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Profiles.Profile']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:profiles'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.profile is not None:
                            for child_ref in self.profile:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Profiles']['meta_info']


                class Statistics(object):
                    """
                    DHCP Server statistics
                    
                    .. attribute:: ipv4_dhcpd_proxy_stat
                    
                    	ipv4 dhcpd proxy stat
                    	**type**\: list of    :py:class:`Ipv4DhcpdProxyStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv4_dhcpd_proxy_stat = YList()
                        self.ipv4_dhcpd_proxy_stat.parent = self
                        self.ipv4_dhcpd_proxy_stat.name = 'ipv4_dhcpd_proxy_stat'


                    class Ipv4DhcpdProxyStat(object):
                        """
                        ipv4 dhcpd proxy stat
                        
                        .. attribute:: statistics
                        
                        	Proxy statistics
                        	**type**\:   :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCP L3 VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.statistics = Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_()
                            self.statistics.parent = self
                            self.vrf_name = None


                        class Statistics_(object):
                            """
                            Proxy statistics
                            
                            .. attribute:: dropped_packets
                            
                            	Dropped packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: received_packets
                            
                            	Received packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: transmitted_packets
                            
                            	Transmitted packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dropped_packets = None
                                self.received_packets = None
                                self.transmitted_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.dropped_packets is not None:
                                    return True

                                if self.received_packets is not None:
                                    return True

                                if self.transmitted_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd-proxy-stat'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv4_dhcpd_proxy_stat is not None:
                            for child_ref in self.ipv4_dhcpd_proxy_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Statistics']['meta_info']


                class Binding(object):
                    """
                    DHCP server bindings
                    
                    .. attribute:: clients
                    
                    	DHCP server client bindings
                    	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients>`
                    
                    .. attribute:: summary
                    
                    	DHCP server binding summary
                    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.clients = Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients()
                        self.clients.parent = self
                        self.summary = Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary()
                        self.summary.parent = self


                    class Summary(object):
                        """
                        DHCP server binding summary
                        
                        .. attribute:: ack_waiting_for_dpm
                        
                        	Number of clients in Waiting for DPM with ACK
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bound_clients
                        
                        	Number of clients in bound state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: deleting_clients_d
                        
                        	Number of clients in deleting state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: disconnected_clients
                        
                        	Number of clients in disconnected state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: informing_clients
                        
                        	Number of clients in informing state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: initializing_clients
                        
                        	Number of clients in init state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: offer_sent_for_client
                        
                        	Number of clients in Offer sent state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reauthorizing_clients
                        
                        	Number of clients in reauth state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: renewing_clients
                        
                        	Number of clients in renewing state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: request_waiting_for_dpm
                        
                        	Number of clients in Waiting for DPM with Request
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: requesting_clients
                        
                        	Number of clients in requesting state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: restarting_clients
                        
                        	Number of clients in restarting state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: selecting_clients
                        
                        	Number of clients in selecting state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_daps_init
                        
                        	Number of clients in Init DAPS wait state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_addr_change
                        
                        	Number of clients in Waiting for DPM after addr change
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_disconnect
                        
                        	Number of clients in waiting for DPM disconnect state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_init
                        
                        	Number of clients in Init DPM wait state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ack_waiting_for_dpm = None
                            self.bound_clients = None
                            self.clients = None
                            self.deleting_clients_d = None
                            self.disconnected_clients = None
                            self.informing_clients = None
                            self.initializing_clients = None
                            self.offer_sent_for_client = None
                            self.reauthorizing_clients = None
                            self.renewing_clients = None
                            self.request_waiting_for_dpm = None
                            self.requesting_clients = None
                            self.restarting_clients = None
                            self.selecting_clients = None
                            self.waiting_for_daps_init = None
                            self.waiting_for_dpm_addr_change = None
                            self.waiting_for_dpm_disconnect = None
                            self.waiting_for_dpm_init = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ack_waiting_for_dpm is not None:
                                return True

                            if self.bound_clients is not None:
                                return True

                            if self.clients is not None:
                                return True

                            if self.deleting_clients_d is not None:
                                return True

                            if self.disconnected_clients is not None:
                                return True

                            if self.informing_clients is not None:
                                return True

                            if self.initializing_clients is not None:
                                return True

                            if self.offer_sent_for_client is not None:
                                return True

                            if self.reauthorizing_clients is not None:
                                return True

                            if self.renewing_clients is not None:
                                return True

                            if self.request_waiting_for_dpm is not None:
                                return True

                            if self.requesting_clients is not None:
                                return True

                            if self.restarting_clients is not None:
                                return True

                            if self.selecting_clients is not None:
                                return True

                            if self.waiting_for_daps_init is not None:
                                return True

                            if self.waiting_for_dpm_addr_change is not None:
                                return True

                            if self.waiting_for_dpm_disconnect is not None:
                                return True

                            if self.waiting_for_dpm_init is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary']['meta_info']


                    class Clients(object):
                        """
                        DHCP server client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCP Server binding
                        	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.client = YList()
                            self.client.parent = self
                            self.client.name = 'client'


                        class Client(object):
                            """
                            Single DHCP Server binding
                            
                            .. attribute:: client_id  <key>
                            
                            	Client ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: access_vrf_name
                            
                            	DHCP access interface VRF name
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: client_gi_addr
                            
                            	DHCP client GIADDR
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: client_id_xr
                            
                            	DHCP client identifier
                            	**type**\:  str
                            
                            	**length:** 0..1275
                            
                            .. attribute:: event_history
                            
                            	event history
                            	**type**\:  list of int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	DHCP access interface to client
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: ip_address
                            
                            	DHCP IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: is_auth_received
                            
                            	Is true if authentication is on received option82
                            	**type**\:  bool
                            
                            .. attribute:: is_mbl_subscriber
                            
                            	Is true if DHCP subscriber is Mobile
                            	**type**\:  bool
                            
                            .. attribute:: is_nak_next_renew
                            
                            	Is true if DHCP next renew from client will be NAK'd
                            	**type**\:  bool
                            
                            .. attribute:: lease_time
                            
                            	Lease time in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: mac_address
                            
                            	DHCP client MAC address
                            	**type**\:  str
                            
                            .. attribute:: old_subscriber_label
                            
                            	DHCP old subscriber label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: param_request
                            
                            	DHCP parameter request option
                            	**type**\:  str
                            
                            	**length:** 0..513
                            
                            .. attribute:: param_response
                            
                            	DHCP saved options
                            	**type**\:  str
                            
                            	**length:** 0..2051
                            
                            .. attribute:: profile_name
                            
                            	DHCP profile name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            .. attribute:: proxy_binding_inner_tag
                            
                            	DHCP VLAN inner VLAN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_binding_outer_tag
                            
                            	DHCP VLAN outer VLAN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: remaining_lease_time
                            
                            	Remaining lease time in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: reply_server_ip_address
                            
                            	DHCP reply server IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: rx_circuit_id
                            
                            	DHCP received circuit ID
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: rx_remote_id
                            
                            	DHCP received Remote ID
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: rx_vsiso
                            
                            	DHCP received VSISO
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: server_ip_address
                            
                            	DHCP server IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: server_vrf_name
                            
                            	DHCP server VRF name
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: session_start_time
                            
                            	session start time
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: srg_state
                            
                            	DHCPV4 SRG state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state
                            
                            	DHCP client state
                            	**type**\:   :py:class:`BagDhcpdProxyStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.BagDhcpdProxyStateEnum>`
                            
                            .. attribute:: subscriber_interface_name
                            
                            	DHCP subscriber interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: subscriber_label
                            
                            	DHCP subscriber label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: to_server_gi_addr
                            
                            	DHCP to server GIADDR
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: tx_circuit_id
                            
                            	DHCP transmitted circuit ID
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: tx_remote_id
                            
                            	DHCP transmitted Remote ID
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: tx_vsiso
                            
                            	DHCP transmitted VSISO
                            	**type**\:  str
                            
                            	**length:** 0..768
                            
                            .. attribute:: vrf_name
                            
                            	DHCP client/subscriber VRF name
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.client_id = None
                                self.access_vrf_name = None
                                self.client_gi_addr = None
                                self.client_id_xr = None
                                self.event_history = YLeafList()
                                self.event_history.parent = self
                                self.event_history.name = 'event_history'
                                self.interface_name = None
                                self.ip_address = None
                                self.is_auth_received = None
                                self.is_mbl_subscriber = None
                                self.is_nak_next_renew = None
                                self.lease_time = None
                                self.mac_address = None
                                self.old_subscriber_label = None
                                self.param_request = None
                                self.param_response = None
                                self.profile_name = None
                                self.proxy_binding_inner_tag = None
                                self.proxy_binding_outer_tag = None
                                self.remaining_lease_time = None
                                self.reply_server_ip_address = None
                                self.rx_circuit_id = None
                                self.rx_remote_id = None
                                self.rx_vsiso = None
                                self.server_ip_address = None
                                self.server_vrf_name = None
                                self.session_start_time = None
                                self.srg_state = None
                                self.state = None
                                self.subscriber_interface_name = None
                                self.subscriber_label = None
                                self.to_server_gi_addr = None
                                self.tx_circuit_id = None
                                self.tx_remote_id = None
                                self.tx_vsiso = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.client_id is None:
                                    raise YPYModelError('Key property client_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:client[Cisco-IOS-XR-ipv4-dhcpd-oper:client-id = ' + str(self.client_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.client_id is not None:
                                    return True

                                if self.access_vrf_name is not None:
                                    return True

                                if self.client_gi_addr is not None:
                                    return True

                                if self.client_id_xr is not None:
                                    return True

                                if self.event_history is not None:
                                    for child in self.event_history:
                                        if child is not None:
                                            return True

                                if self.interface_name is not None:
                                    return True

                                if self.ip_address is not None:
                                    return True

                                if self.is_auth_received is not None:
                                    return True

                                if self.is_mbl_subscriber is not None:
                                    return True

                                if self.is_nak_next_renew is not None:
                                    return True

                                if self.lease_time is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.old_subscriber_label is not None:
                                    return True

                                if self.param_request is not None:
                                    return True

                                if self.param_response is not None:
                                    return True

                                if self.profile_name is not None:
                                    return True

                                if self.proxy_binding_inner_tag is not None:
                                    return True

                                if self.proxy_binding_outer_tag is not None:
                                    return True

                                if self.remaining_lease_time is not None:
                                    return True

                                if self.reply_server_ip_address is not None:
                                    return True

                                if self.rx_circuit_id is not None:
                                    return True

                                if self.rx_remote_id is not None:
                                    return True

                                if self.rx_vsiso is not None:
                                    return True

                                if self.server_ip_address is not None:
                                    return True

                                if self.server_vrf_name is not None:
                                    return True

                                if self.session_start_time is not None:
                                    return True

                                if self.srg_state is not None:
                                    return True

                                if self.state is not None:
                                    return True

                                if self.subscriber_interface_name is not None:
                                    return True

                                if self.subscriber_label is not None:
                                    return True

                                if self.to_server_gi_addr is not None:
                                    return True

                                if self.tx_circuit_id is not None:
                                    return True

                                if self.tx_remote_id is not None:
                                    return True

                                if self.tx_vsiso is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients.Client']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:clients'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.client is not None:
                                for child_ref in self.client:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:binding'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.clients is not None and self.clients._has_data():
                            return True

                        if self.summary is not None and self.summary._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Binding']['meta_info']


                class StatisticsInfo(object):
                    """
                    DHCP proxy stats info
                    
                    .. attribute:: proxy_stats_timestamp
                    
                    	Proxy Stats timestamp
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.proxy_stats_timestamp = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.proxy_stats_timestamp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo']['meta_info']


                class Vrfs(object):
                    """
                    DHCP Server list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv4 DHCP server VRF name
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        IPv4 DHCP server VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv4 DHCP server statistics
                        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.statistics = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self


                        class Statistics(object):
                            """
                            IPv4 DHCP server statistics
                            
                            .. attribute:: ack
                            
                            	DHCP ack packets
                            	**type**\:   :py:class:`Ack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack>`
                            
                            .. attribute:: bootp_reply
                            
                            	DHCP BOOTP reply
                            	**type**\:   :py:class:`BootpReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply>`
                            
                            .. attribute:: bootp_request
                            
                            	DHCP BOOTP request
                            	**type**\:   :py:class:`BootpRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest>`
                            
                            .. attribute:: decline
                            
                            	DHCP decline packets
                            	**type**\:   :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: discover
                            
                            	DHCP discover packets
                            	**type**\:   :py:class:`Discover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover>`
                            
                            .. attribute:: inform
                            
                            	DHCP inform packets
                            	**type**\:   :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: lease_active
                            
                            	DHCP lease active
                            	**type**\:   :py:class:`LeaseActive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive>`
                            
                            .. attribute:: lease_not_assigned
                            
                            	DHCP lease not assigned
                            	**type**\:   :py:class:`LeaseNotAssigned <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned>`
                            
                            .. attribute:: lease_query
                            
                            	DHCP lease query packets
                            	**type**\:   :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_unknown
                            
                            	DHCP lease unknown
                            	**type**\:   :py:class:`LeaseUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown>`
                            
                            .. attribute:: nak
                            
                            	DHCP nak packets
                            	**type**\:   :py:class:`Nak <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak>`
                            
                            .. attribute:: offer
                            
                            	DHCP offer packets
                            	**type**\:   :py:class:`Offer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer>`
                            
                            .. attribute:: release
                            
                            	DHCP release packets
                            	**type**\:   :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: request
                            
                            	DHCP request packets
                            	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ack = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack()
                                self.ack.parent = self
                                self.bootp_reply = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply()
                                self.bootp_reply.parent = self
                                self.bootp_request = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest()
                                self.bootp_request.parent = self
                                self.decline = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self.discover = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover()
                                self.discover.parent = self
                                self.inform = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self.lease_active = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive()
                                self.lease_active.parent = self
                                self.lease_not_assigned = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned()
                                self.lease_not_assigned.parent = self
                                self.lease_query = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self.lease_unknown = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown()
                                self.lease_unknown.parent = self
                                self.nak = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak()
                                self.nak.parent = self
                                self.offer = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer()
                                self.offer.parent = self
                                self.release = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self.request = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self


                            class Discover(object):
                                """
                                DHCP discover packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:discover'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover']['meta_info']


                            class Offer(object):
                                """
                                DHCP offer packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:offer'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer']['meta_info']


                            class Request(object):
                                """
                                DHCP request packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:request'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request']['meta_info']


                            class Decline(object):
                                """
                                DHCP decline packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:decline'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline']['meta_info']


                            class Ack(object):
                                """
                                DHCP ack packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack']['meta_info']


                            class Nak(object):
                                """
                                DHCP nak packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:nak'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak']['meta_info']


                            class Release(object):
                                """
                                DHCP release packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:release'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release']['meta_info']


                            class Inform(object):
                                """
                                DHCP inform packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:inform'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform']['meta_info']


                            class LeaseQuery(object):
                                """
                                DHCP lease query packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-query'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info']


                            class LeaseNotAssigned(object):
                                """
                                DHCP lease not assigned
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-not-assigned'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned']['meta_info']


                            class LeaseUnknown(object):
                                """
                                DHCP lease unknown
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-unknown'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown']['meta_info']


                            class LeaseActive(object):
                                """
                                DHCP lease active
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-active'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive']['meta_info']


                            class BootpRequest(object):
                                """
                                DHCP BOOTP request
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:bootp-request'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest']['meta_info']


                            class BootpReply(object):
                                """
                                DHCP BOOTP reply
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:bootp-reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ack is not None and self.ack._has_data():
                                    return True

                                if self.bootp_reply is not None and self.bootp_reply._has_data():
                                    return True

                                if self.bootp_request is not None and self.bootp_request._has_data():
                                    return True

                                if self.decline is not None and self.decline._has_data():
                                    return True

                                if self.discover is not None and self.discover._has_data():
                                    return True

                                if self.inform is not None and self.inform._has_data():
                                    return True

                                if self.lease_active is not None and self.lease_active._has_data():
                                    return True

                                if self.lease_not_assigned is not None and self.lease_not_assigned._has_data():
                                    return True

                                if self.lease_query is not None and self.lease_query._has_data():
                                    return True

                                if self.lease_unknown is not None and self.lease_unknown._has_data():
                                    return True

                                if self.nak is not None and self.nak._has_data():
                                    return True

                                if self.offer is not None and self.offer._has_data():
                                    return True

                                if self.release is not None and self.release._has_data():
                                    return True

                                if self.request is not None and self.request._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:vrf[Cisco-IOS-XR-ipv4-dhcpd-oper:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.vrf_name is not None:
                                return True

                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:vrfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vrf is not None:
                            for child_ref in self.vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.binding is not None and self.binding._has_data():
                        return True

                    if self.profiles is not None and self.profiles._has_data():
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.statistics_info is not None and self.statistics_info._has_data():
                        return True

                    if self.vrfs is not None and self.vrfs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Server']['meta_info']


            class Relay(object):
                """
                IPv4 DHCPD Relay operational data
                
                .. attribute:: profiles
                
                	DHCP Relay Profiles
                	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Profiles>`
                
                .. attribute:: statistics
                
                	DHCP Relay VRF statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Statistics>`
                
                .. attribute:: statistics_info
                
                	DHCP relay statistics info
                	**type**\:   :py:class:`StatisticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo>`
                
                .. attribute:: vrfs
                
                	DHCP relay list of VRF names
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.profiles = Ipv4Dhcpd.Nodes.Node.Relay.Profiles()
                    self.profiles.parent = self
                    self.statistics = Ipv4Dhcpd.Nodes.Node.Relay.Statistics()
                    self.statistics.parent = self
                    self.statistics_info = Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo()
                    self.statistics_info.parent = self
                    self.vrfs = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs()
                    self.vrfs.parent = self


                class Profiles(object):
                    """
                    DHCP Relay Profiles
                    
                    .. attribute:: profile
                    
                    	DHCP Relay profile
                    	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.profile = YList()
                        self.profile.parent = self
                        self.profile.name = 'profile'


                    class Profile(object):
                        """
                        DHCP Relay profile
                        
                        .. attribute:: profile_name  <key>
                        
                        	Profile name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: relay_profile_broadcast_flag_policy
                        
                        	Broadcast policy
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_gi_addr
                        
                        	Gateway addresses
                        	**type**\:  list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: relay_profile_gi_addr_policy
                        
                        	GIADDR policy
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_helper_address
                        
                        	Helper addresses
                        	**type**\:  list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: relay_profile_helper_count
                        
                        	Helper address count
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_helper_vrf
                        
                        	Helper address vrfs
                        	**type**\:  list of str
                        
                        	**length:** 0..33
                        
                        .. attribute:: relay_profile_name
                        
                        	Profile Name
                        	**type**\:  str
                        
                        	**length:** 0..65
                        
                        .. attribute:: relay_profile_relay_info_allow_untrusted
                        
                        	Relay info untrusted
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_relay_info_check
                        
                        	Relay info check
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_relay_info_option
                        
                        	Relay info option
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_relay_info_optionvpn
                        
                        	Relay info option vpn
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_relay_info_optionvpn_mode
                        
                        	Relay info option vpn\-mode
                        	**type**\:   :py:class:`RelayInfoVpnModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.RelayInfoVpnModeEnum>`
                        
                        .. attribute:: relay_profile_relay_info_policy
                        
                        	Relay info policy
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_uid
                        
                        	Profile UID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.profile_name = None
                            self.relay_profile_broadcast_flag_policy = None
                            self.relay_profile_gi_addr = YLeafList()
                            self.relay_profile_gi_addr.parent = self
                            self.relay_profile_gi_addr.name = 'relay_profile_gi_addr'
                            self.relay_profile_gi_addr_policy = None
                            self.relay_profile_helper_address = YLeafList()
                            self.relay_profile_helper_address.parent = self
                            self.relay_profile_helper_address.name = 'relay_profile_helper_address'
                            self.relay_profile_helper_count = None
                            self.relay_profile_helper_vrf = YLeafList()
                            self.relay_profile_helper_vrf.parent = self
                            self.relay_profile_helper_vrf.name = 'relay_profile_helper_vrf'
                            self.relay_profile_name = None
                            self.relay_profile_relay_info_allow_untrusted = None
                            self.relay_profile_relay_info_check = None
                            self.relay_profile_relay_info_option = None
                            self.relay_profile_relay_info_optionvpn = None
                            self.relay_profile_relay_info_optionvpn_mode = None
                            self.relay_profile_relay_info_policy = None
                            self.relay_profile_uid = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.profile_name is None:
                                raise YPYModelError('Key property profile_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:profile[Cisco-IOS-XR-ipv4-dhcpd-oper:profile-name = ' + str(self.profile_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.profile_name is not None:
                                return True

                            if self.relay_profile_broadcast_flag_policy is not None:
                                return True

                            if self.relay_profile_gi_addr is not None:
                                for child in self.relay_profile_gi_addr:
                                    if child is not None:
                                        return True

                            if self.relay_profile_gi_addr_policy is not None:
                                return True

                            if self.relay_profile_helper_address is not None:
                                for child in self.relay_profile_helper_address:
                                    if child is not None:
                                        return True

                            if self.relay_profile_helper_count is not None:
                                return True

                            if self.relay_profile_helper_vrf is not None:
                                for child in self.relay_profile_helper_vrf:
                                    if child is not None:
                                        return True

                            if self.relay_profile_name is not None:
                                return True

                            if self.relay_profile_relay_info_allow_untrusted is not None:
                                return True

                            if self.relay_profile_relay_info_check is not None:
                                return True

                            if self.relay_profile_relay_info_option is not None:
                                return True

                            if self.relay_profile_relay_info_optionvpn is not None:
                                return True

                            if self.relay_profile_relay_info_optionvpn_mode is not None:
                                return True

                            if self.relay_profile_relay_info_policy is not None:
                                return True

                            if self.relay_profile_uid is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Profiles.Profile']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:profiles'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.profile is not None:
                            for child_ref in self.profile:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Profiles']['meta_info']


                class StatisticsInfo(object):
                    """
                    DHCP relay statistics info
                    
                    .. attribute:: relay_stats_timestamp
                    
                    	Relay Stats timestamp
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.relay_stats_timestamp = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.relay_stats_timestamp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo']['meta_info']


                class Statistics(object):
                    """
                    DHCP Relay VRF statistics
                    
                    .. attribute:: ipv4_dhcpd_relay_stat
                    
                    	ipv4 dhcpd relay stat
                    	**type**\: list of    :py:class:`Ipv4DhcpdRelayStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv4_dhcpd_relay_stat = YList()
                        self.ipv4_dhcpd_relay_stat.parent = self
                        self.ipv4_dhcpd_relay_stat.name = 'ipv4_dhcpd_relay_stat'


                    class Ipv4DhcpdRelayStat(object):
                        """
                        ipv4 dhcpd relay stat
                        
                        .. attribute:: relay_statistics_vrf_name
                        
                        	DHCP L3 VRF Name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        .. attribute:: statistics
                        
                        	Public relay statistics
                        	**type**\:   :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.relay_statistics_vrf_name = None
                            self.statistics = Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_()
                            self.statistics.parent = self


                        class Statistics_(object):
                            """
                            Public relay statistics
                            
                            .. attribute:: dropped_packets
                            
                            	Dropped packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: received_packets
                            
                            	Received packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: transmitted_packets
                            
                            	Transmitted packets
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dropped_packets = None
                                self.received_packets = None
                                self.transmitted_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.dropped_packets is not None:
                                    return True

                                if self.received_packets is not None:
                                    return True

                                if self.transmitted_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd-relay-stat'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.relay_statistics_vrf_name is not None:
                                return True

                            if self.statistics is not None and self.statistics._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv4_dhcpd_relay_stat is not None:
                            for child_ref in self.ipv4_dhcpd_relay_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Statistics']['meta_info']


                class Vrfs(object):
                    """
                    DHCP relay list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv4 DHCP relay VRF name
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        IPv4 DHCP relay VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: vrf_statistics
                        
                        	IPv4 DHCP relay statistics
                        	**type**\:   :py:class:`VrfStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.vrf_statistics = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics()
                            self.vrf_statistics.parent = self


                        class VrfStatistics(object):
                            """
                            IPv4 DHCP relay statistics
                            
                            .. attribute:: ack
                            
                            	DHCP ack packets
                            	**type**\:   :py:class:`Ack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack>`
                            
                            .. attribute:: bootp_reply
                            
                            	DHCP BOOTP reply
                            	**type**\:   :py:class:`BootpReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply>`
                            
                            .. attribute:: bootp_request
                            
                            	DHCP BOOTP request
                            	**type**\:   :py:class:`BootpRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest>`
                            
                            .. attribute:: decline
                            
                            	DHCP decline packets
                            	**type**\:   :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline>`
                            
                            .. attribute:: discover
                            
                            	DHCP discover packets
                            	**type**\:   :py:class:`Discover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover>`
                            
                            .. attribute:: inform
                            
                            	DHCP inform packets
                            	**type**\:   :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform>`
                            
                            .. attribute:: lease_active
                            
                            	DHCP lease active
                            	**type**\:   :py:class:`LeaseActive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive>`
                            
                            .. attribute:: lease_not_assigned
                            
                            	DHCP lease not assigned
                            	**type**\:   :py:class:`LeaseNotAssigned <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned>`
                            
                            .. attribute:: lease_query
                            
                            	DHCP lease query packets
                            	**type**\:   :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery>`
                            
                            .. attribute:: lease_unknown
                            
                            	DHCP lease unknown
                            	**type**\:   :py:class:`LeaseUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown>`
                            
                            .. attribute:: nak
                            
                            	DHCP nak packets
                            	**type**\:   :py:class:`Nak <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak>`
                            
                            .. attribute:: offer
                            
                            	DHCP offer packets
                            	**type**\:   :py:class:`Offer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer>`
                            
                            .. attribute:: release
                            
                            	DHCP release packets
                            	**type**\:   :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release>`
                            
                            .. attribute:: request
                            
                            	DHCP request packets
                            	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ack = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack()
                                self.ack.parent = self
                                self.bootp_reply = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply()
                                self.bootp_reply.parent = self
                                self.bootp_request = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest()
                                self.bootp_request.parent = self
                                self.decline = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline()
                                self.decline.parent = self
                                self.discover = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover()
                                self.discover.parent = self
                                self.inform = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform()
                                self.inform.parent = self
                                self.lease_active = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive()
                                self.lease_active.parent = self
                                self.lease_not_assigned = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned()
                                self.lease_not_assigned.parent = self
                                self.lease_query = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery()
                                self.lease_query.parent = self
                                self.lease_unknown = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown()
                                self.lease_unknown.parent = self
                                self.nak = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak()
                                self.nak.parent = self
                                self.offer = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer()
                                self.offer.parent = self
                                self.release = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release()
                                self.release.parent = self
                                self.request = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request()
                                self.request.parent = self


                            class Discover(object):
                                """
                                DHCP discover packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:discover'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover']['meta_info']


                            class Offer(object):
                                """
                                DHCP offer packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:offer'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer']['meta_info']


                            class Request(object):
                                """
                                DHCP request packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:request'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request']['meta_info']


                            class Decline(object):
                                """
                                DHCP decline packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:decline'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline']['meta_info']


                            class Ack(object):
                                """
                                DHCP ack packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:ack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack']['meta_info']


                            class Nak(object):
                                """
                                DHCP nak packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:nak'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak']['meta_info']


                            class Release(object):
                                """
                                DHCP release packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:release'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release']['meta_info']


                            class Inform(object):
                                """
                                DHCP inform packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:inform'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform']['meta_info']


                            class LeaseQuery(object):
                                """
                                DHCP lease query packets
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-query'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery']['meta_info']


                            class LeaseNotAssigned(object):
                                """
                                DHCP lease not assigned
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-not-assigned'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned']['meta_info']


                            class LeaseUnknown(object):
                                """
                                DHCP lease unknown
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-unknown'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown']['meta_info']


                            class LeaseActive(object):
                                """
                                DHCP lease active
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:lease-active'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive']['meta_info']


                            class BootpRequest(object):
                                """
                                DHCP BOOTP request
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:bootp-request'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest']['meta_info']


                            class BootpReply(object):
                                """
                                DHCP BOOTP reply
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dropped_packets = None
                                    self.received_packets = None
                                    self.transmitted_packets = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:bootp-reply'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dropped_packets is not None:
                                        return True

                                    if self.received_packets is not None:
                                        return True

                                    if self.transmitted_packets is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:vrf-statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ack is not None and self.ack._has_data():
                                    return True

                                if self.bootp_reply is not None and self.bootp_reply._has_data():
                                    return True

                                if self.bootp_request is not None and self.bootp_request._has_data():
                                    return True

                                if self.decline is not None and self.decline._has_data():
                                    return True

                                if self.discover is not None and self.discover._has_data():
                                    return True

                                if self.inform is not None and self.inform._has_data():
                                    return True

                                if self.lease_active is not None and self.lease_active._has_data():
                                    return True

                                if self.lease_not_assigned is not None and self.lease_not_assigned._has_data():
                                    return True

                                if self.lease_query is not None and self.lease_query._has_data():
                                    return True

                                if self.lease_unknown is not None and self.lease_unknown._has_data():
                                    return True

                                if self.nak is not None and self.nak._has_data():
                                    return True

                                if self.offer is not None and self.offer._has_data():
                                    return True

                                if self.release is not None and self.release._has_data():
                                    return True

                                if self.request is not None and self.request._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                                return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:vrf[Cisco-IOS-XR-ipv4-dhcpd-oper:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.vrf_name is not None:
                                return True

                            if self.vrf_statistics is not None and self.vrf_statistics._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                            return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:vrfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vrf is not None:
                            for child_ref in self.vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                        return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-dhcpd-oper:relay'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.profiles is not None and self.profiles._has_data():
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.statistics_info is not None and self.statistics_info._has_data():
                        return True

                    if self.vrfs is not None and self.vrfs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                    return meta._meta_table['Ipv4Dhcpd.Nodes.Node.Relay']['meta_info']

            @property
            def _common_path(self):
                if self.nodeid is None:
                    raise YPYModelError('Key property nodeid is None')

                return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-oper:nodes/Cisco-IOS-XR-ipv4-dhcpd-oper:node[Cisco-IOS-XR-ipv4-dhcpd-oper:nodeid = ' + str(self.nodeid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.nodeid is not None:
                    return True

                if self.base is not None and self.base._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.proxy is not None and self.proxy._has_data():
                    return True

                if self.relay is not None and self.relay._has_data():
                    return True

                if self.server is not None and self.server._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
                return meta._meta_table['Ipv4Dhcpd.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/Cisco-IOS-XR-ipv4-dhcpd-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
            return meta._meta_table['Ipv4Dhcpd.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        if self.snoop is not None and self.snoop._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_dhcpd_oper as meta
        return meta._meta_table['Ipv4Dhcpd']['meta_info']


