""" Cisco_IOS_XR_ipv4_dhcpd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-dhcpd package operational data.

This module contains definitions
for the following management objects\:
  dhcp\-client\: DHCP client operational data
  ipv4\-dhcpd\: ipv4 dhcpd

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BagDhcpdIntfSrgRole(Enum):
    """
    BagDhcpdIntfSrgRole (Enum Class)

    Bag dhcpd intf srg role

    .. data:: none = 0

    	DHCPv4 Interface SRG role NONE

    .. data:: master = 1

    	DHCPv4 Interface SRG role Master

    .. data:: slave = 2

    	DHCPv4 Interface SRG role Slave

    """

    none = Enum.YLeaf(0, "none")

    master = Enum.YLeaf(1, "master")

    slave = Enum.YLeaf(2, "slave")


class BagDhcpdProxyState(Enum):
    """
    BagDhcpdProxyState (Enum Class)

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

    initializing = Enum.YLeaf(0, "initializing")

    selecting = Enum.YLeaf(1, "selecting")

    requesting = Enum.YLeaf(2, "requesting")

    bound = Enum.YLeaf(3, "bound")

    renewing = Enum.YLeaf(4, "renewing")

    informing = Enum.YLeaf(5, "informing")

    deleting = Enum.YLeaf(6, "deleting")

    create_dpm = Enum.YLeaf(7, "create-dpm")

    offer_sent = Enum.YLeaf(8, "offer-sent")

    update_dpm = Enum.YLeaf(9, "update-dpm")

    route_install = Enum.YLeaf(10, "route-install")

    disc_dpm = Enum.YLeaf(11, "disc-dpm")

    renew_new_intf = Enum.YLeaf(12, "renew-new-intf")

    other_intf_dpm = Enum.YLeaf(13, "other-intf-dpm")

    request_dpm = Enum.YLeaf(14, "request-dpm")

    change_addr_dpm = Enum.YLeaf(15, "change-addr-dpm")

    max = Enum.YLeaf(16, "max")


class BroadcastFlag(Enum):
    """
    BroadcastFlag (Enum Class)

    Proxy profile broadcast flag

    .. data:: ignore = 0

    	Broadcast policy ignore

    .. data:: check = 1

    	Broadcast policy check

    .. data:: unicast_always = 2

    	Broadcast policy unicast always

    """

    ignore = Enum.YLeaf(0, "ignore")

    check = Enum.YLeaf(1, "check")

    unicast_always = Enum.YLeaf(2, "unicast-always")


class DhcpIssuPhase(Enum):
    """
    DhcpIssuPhase (Enum Class)

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

    phase_not_started = Enum.YLeaf(0, "phase-not-started")

    phase_load = Enum.YLeaf(1, "phase-load")

    phase_run = Enum.YLeaf(2, "phase-run")

    phase_completed = Enum.YLeaf(3, "phase-completed")

    phase_aborted = Enum.YLeaf(4, "phase-aborted")


class DhcpIssuRole(Enum):
    """
    DhcpIssuRole (Enum Class)

    Dhcp issu role

    .. data:: role_primary = 0

    	Primary role

    .. data:: role_secondary = 1

    	Secondary role

    """

    role_primary = Enum.YLeaf(0, "role-primary")

    role_secondary = Enum.YLeaf(1, "role-secondary")


class DhcpIssuVersion(Enum):
    """
    DhcpIssuVersion (Enum Class)

    Dhcp issu version

    .. data:: version1 = 0

    	Version 1

    .. data:: version2 = 1

    	Version 2

    """

    version1 = Enum.YLeaf(0, "version1")

    version2 = Enum.YLeaf(1, "version2")


class DhcpcIpv4State(Enum):
    """
    DhcpcIpv4State (Enum Class)

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

    init = Enum.YLeaf(0, "init")

    init_reboot = Enum.YLeaf(1, "init-reboot")

    rebooting = Enum.YLeaf(2, "rebooting")

    selecting = Enum.YLeaf(3, "selecting")

    requesting = Enum.YLeaf(4, "requesting")

    bound = Enum.YLeaf(5, "bound")

    renewing = Enum.YLeaf(6, "renewing")

    rebinding = Enum.YLeaf(7, "rebinding")

    invalid = Enum.YLeaf(8, "invalid")


class ProxyLeaseLimit(Enum):
    """
    ProxyLeaseLimit (Enum Class)

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

    none = Enum.YLeaf(0, "none")

    interface = Enum.YLeaf(1, "interface")

    circuit_id = Enum.YLeaf(2, "circuit-id")

    remote_id = Enum.YLeaf(3, "remote-id")

    remote_id_circuit_id = Enum.YLeaf(4, "remote-id-circuit-id")


class RelayInfoAuthenticate(Enum):
    """
    RelayInfoAuthenticate (Enum Class)

    Profile relay authenticate

    .. data:: received = 0

    	Relay authenticate received

    .. data:: inserted = 1

    	Relay authenticate inserted

    """

    received = Enum.YLeaf(0, "received")

    inserted = Enum.YLeaf(1, "inserted")


class RelayInfoPolicy(Enum):
    """
    RelayInfoPolicy (Enum Class)

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

    replace = Enum.YLeaf(0, "replace")

    keep = Enum.YLeaf(1, "keep")

    drop = Enum.YLeaf(2, "drop")

    encapsulate = Enum.YLeaf(3, "encapsulate")


class RelayInfoVpnMode(Enum):
    """
    RelayInfoVpnMode (Enum Class)

    Relay Info Vpn Mode

    .. data:: rfc = 0

    	RFC Mode

    .. data:: cisco = 1

    	Cisco Mode

    """

    rfc = Enum.YLeaf(0, "rfc")

    cisco = Enum.YLeaf(1, "cisco")



class DhcpClient(Entity):
    """
    DHCP client operational data
    
    .. attribute:: nodes
    
    	DHCP client list of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes>`
    
    

    """

    _prefix = 'ipv4-dhcpd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(DhcpClient, self).__init__()
        self._top_entity = None

        self.yang_name = "dhcp-client"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-dhcpd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", DhcpClient.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = DhcpClient.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:dhcp-client"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DhcpClient, [], name, value)


    class Nodes(Entity):
        """
        DHCP client list of nodes
        
        .. attribute:: node
        
        	DHCP client particular node name
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes.Node>`
        
        

        """

        _prefix = 'ipv4-dhcpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(DhcpClient.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "dhcp-client"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", DhcpClient.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:dhcp-client/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DhcpClient.Nodes, [], name, value)


        class Node(Entity):
            """
            DHCP client particular node name
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: client_stats
            
            	IPv4 DHCP client statistics table
            	**type**\:  :py:class:`ClientStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes.Node.ClientStats>`
            
            .. attribute:: clients
            
            	IPv4 DHCP client table
            	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes.Node.Clients>`
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(DhcpClient.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("client-stats", ("client_stats", DhcpClient.Nodes.Node.ClientStats)), ("clients", ("clients", DhcpClient.Nodes.Node.Clients))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.client_stats = DhcpClient.Nodes.Node.ClientStats()
                self.client_stats.parent = self
                self._children_name_map["client_stats"] = "client-stats"

                self.clients = DhcpClient.Nodes.Node.Clients()
                self.clients.parent = self
                self._children_name_map["clients"] = "clients"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:dhcp-client/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DhcpClient.Nodes.Node, ['node_name'], name, value)


            class ClientStats(Entity):
                """
                IPv4 DHCP client statistics table
                
                .. attribute:: client_stat
                
                	DHCP client binding statistics
                	**type**\: list of  		 :py:class:`ClientStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes.Node.ClientStats.ClientStat>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DhcpClient.Nodes.Node.ClientStats, self).__init__()

                    self.yang_name = "client-stats"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("client-stat", ("client_stat", DhcpClient.Nodes.Node.ClientStats.ClientStat))])
                    self._leafs = OrderedDict()

                    self.client_stat = YList(self)
                    self._segment_path = lambda: "client-stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DhcpClient.Nodes.Node.ClientStats, [], name, value)


                class ClientStat(Entity):
                    """
                    DHCP client binding statistics
                    
                    .. attribute:: client_ifhandle  (key)
                    
                    	Client Ifhandle
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: interface_name
                    
                    	Dhcp Client interface name
                    	**type**\: str
                    
                    	**length:** 0..65
                    
                    .. attribute:: num_events_received
                    
                    	Number of events received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_create_event_received
                    
                    	Number of create client event received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_delete_event_received
                    
                    	Number of delete client event received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_reboot_event_received
                    
                    	Number of client rebooted event received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_reinit_event_received
                    
                    	Number of reinit client event received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_packet_event_received
                    
                    	Number of packet event received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_init_timer_eventi
                    
                    	Number of init timer event
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t1_timer_event
                    
                    	Number of T1 timer event
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t2_timer_event
                    
                    	Number of T2 timer event
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_lease_timer_event
                    
                    	Number of Lease timer event
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_vbind_timer_event
                    
                    	Number of vbind timer event
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_discovers_sent_successfully
                    
                    	Number of discovers sent successfully
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_requests_sent_successfully
                    
                    	Number of requests sent successfully
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_releases_sent_successfully
                    
                    	Number of releases sent successfully
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_renews_sent_successfully
                    
                    	Number of renews sent successfully
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_rebinds_sent_successfully
                    
                    	Number of rebinds sent successfully
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_declines_sent_successfully
                    
                    	Number of declines sent successfully
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_request_after_reboot_sent
                    
                    	Number of requests sent after reboot
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_valid_offers_received
                    
                    	Number of valid offers received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_valid_acks_received
                    
                    	Number of valid acks received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_valid_nacks_received
                    
                    	Number of valid nacks received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_unicast_packet_sent_successfully
                    
                    	Number of unicast packet sent successfully
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_broadcast_packet_sent_success
                    
                    	Number of broadcast packet sent successfully
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_init_timer_start
                    
                    	Number of init timer starts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_init_timer_stop
                    
                    	Number of init timer stops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t1_timer_start
                    
                    	Number of T1 timer starts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t1_timer_stop
                    
                    	Number of T1 timer stops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t2_timer_start
                    
                    	Number of T2 timer starts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_t2_timer_stop
                    
                    	Number of T2 timer stops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_lease_timer_start
                    
                    	Number of Lease timer starts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_lease_timer_stop
                    
                    	Number of Lease timer stops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_vbind_timer_start
                    
                    	Number of vbind timer starts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_vbind_timer_stop
                    
                    	Number of vbind timer stops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_invalid_events
                    
                    	Number of invalid events received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_discovers_failed
                    
                    	Number of discover send failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_requests_failed
                    
                    	Number of request send failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_releases_failed
                    
                    	Number of release send failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_renews_failed
                    
                    	Number of renew send failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_rebinds_failed
                    
                    	Number of rebind send failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_declines_failed
                    
                    	Number of decline send failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_request_after_reboot_failed
                    
                    	Number of requests sent after reboot failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_invalid_offers
                    
                    	Number of invalid offers received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_invalid_acks
                    
                    	Number of invalid acks received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_invalid_nacks
                    
                    	Number of invalid nacks received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_invalid_packets
                    
                    	Number of invalid packets dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_unicast_failed
                    
                    	Number of unicast packet send failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_broadcast_failed
                    
                    	Number of broadcast packet send failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_xid_mismatch
                    
                    	Number of XID mismatch packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_vbind_failed
                    
                    	Number of socket vbind failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DhcpClient.Nodes.Node.ClientStats.ClientStat, self).__init__()

                        self.yang_name = "client-stat"
                        self.yang_parent_name = "client-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['client_ifhandle']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('client_ifhandle', (YLeaf(YType.str, 'client-ifhandle'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('num_events_received', (YLeaf(YType.uint32, 'num-events-received'), ['int'])),
                            ('num_create_event_received', (YLeaf(YType.uint32, 'num-create-event-received'), ['int'])),
                            ('num_delete_event_received', (YLeaf(YType.uint32, 'num-delete-event-received'), ['int'])),
                            ('num_reboot_event_received', (YLeaf(YType.uint32, 'num-reboot-event-received'), ['int'])),
                            ('num_reinit_event_received', (YLeaf(YType.uint32, 'num-reinit-event-received'), ['int'])),
                            ('num_packet_event_received', (YLeaf(YType.uint32, 'num-packet-event-received'), ['int'])),
                            ('num_init_timer_eventi', (YLeaf(YType.uint32, 'num-init-timer-eventi'), ['int'])),
                            ('num_t1_timer_event', (YLeaf(YType.uint32, 'num-t1-timer-event'), ['int'])),
                            ('num_t2_timer_event', (YLeaf(YType.uint32, 'num-t2-timer-event'), ['int'])),
                            ('num_lease_timer_event', (YLeaf(YType.uint32, 'num-lease-timer-event'), ['int'])),
                            ('num_vbind_timer_event', (YLeaf(YType.uint32, 'num-vbind-timer-event'), ['int'])),
                            ('num_discovers_sent_successfully', (YLeaf(YType.uint32, 'num-discovers-sent-successfully'), ['int'])),
                            ('num_requests_sent_successfully', (YLeaf(YType.uint32, 'num-requests-sent-successfully'), ['int'])),
                            ('num_releases_sent_successfully', (YLeaf(YType.uint32, 'num-releases-sent-successfully'), ['int'])),
                            ('num_renews_sent_successfully', (YLeaf(YType.uint32, 'num-renews-sent-successfully'), ['int'])),
                            ('num_rebinds_sent_successfully', (YLeaf(YType.uint32, 'num-rebinds-sent-successfully'), ['int'])),
                            ('num_declines_sent_successfully', (YLeaf(YType.uint32, 'num-declines-sent-successfully'), ['int'])),
                            ('num_request_after_reboot_sent', (YLeaf(YType.uint32, 'num-request-after-reboot-sent'), ['int'])),
                            ('num_valid_offers_received', (YLeaf(YType.uint32, 'num-valid-offers-received'), ['int'])),
                            ('num_valid_acks_received', (YLeaf(YType.uint32, 'num-valid-acks-received'), ['int'])),
                            ('num_valid_nacks_received', (YLeaf(YType.uint32, 'num-valid-nacks-received'), ['int'])),
                            ('num_unicast_packet_sent_successfully', (YLeaf(YType.uint32, 'num-unicast-packet-sent-successfully'), ['int'])),
                            ('num_broadcast_packet_sent_success', (YLeaf(YType.uint32, 'num-broadcast-packet-sent-success'), ['int'])),
                            ('num_init_timer_start', (YLeaf(YType.uint32, 'num-init-timer-start'), ['int'])),
                            ('num_init_timer_stop', (YLeaf(YType.uint32, 'num-init-timer-stop'), ['int'])),
                            ('num_t1_timer_start', (YLeaf(YType.uint32, 'num-t1-timer-start'), ['int'])),
                            ('num_t1_timer_stop', (YLeaf(YType.uint32, 'num-t1-timer-stop'), ['int'])),
                            ('num_t2_timer_start', (YLeaf(YType.uint32, 'num-t2-timer-start'), ['int'])),
                            ('num_t2_timer_stop', (YLeaf(YType.uint32, 'num-t2-timer-stop'), ['int'])),
                            ('num_lease_timer_start', (YLeaf(YType.uint32, 'num-lease-timer-start'), ['int'])),
                            ('num_lease_timer_stop', (YLeaf(YType.uint32, 'num-lease-timer-stop'), ['int'])),
                            ('num_vbind_timer_start', (YLeaf(YType.uint32, 'num-vbind-timer-start'), ['int'])),
                            ('num_vbind_timer_stop', (YLeaf(YType.uint32, 'num-vbind-timer-stop'), ['int'])),
                            ('num_invalid_events', (YLeaf(YType.uint32, 'num-invalid-events'), ['int'])),
                            ('num_discovers_failed', (YLeaf(YType.uint32, 'num-discovers-failed'), ['int'])),
                            ('num_requests_failed', (YLeaf(YType.uint32, 'num-requests-failed'), ['int'])),
                            ('num_releases_failed', (YLeaf(YType.uint32, 'num-releases-failed'), ['int'])),
                            ('num_renews_failed', (YLeaf(YType.uint32, 'num-renews-failed'), ['int'])),
                            ('num_rebinds_failed', (YLeaf(YType.uint32, 'num-rebinds-failed'), ['int'])),
                            ('num_declines_failed', (YLeaf(YType.uint32, 'num-declines-failed'), ['int'])),
                            ('num_request_after_reboot_failed', (YLeaf(YType.uint32, 'num-request-after-reboot-failed'), ['int'])),
                            ('num_invalid_offers', (YLeaf(YType.uint32, 'num-invalid-offers'), ['int'])),
                            ('num_invalid_acks', (YLeaf(YType.uint32, 'num-invalid-acks'), ['int'])),
                            ('num_invalid_nacks', (YLeaf(YType.uint32, 'num-invalid-nacks'), ['int'])),
                            ('num_invalid_packets', (YLeaf(YType.uint32, 'num-invalid-packets'), ['int'])),
                            ('num_unicast_failed', (YLeaf(YType.uint32, 'num-unicast-failed'), ['int'])),
                            ('num_broadcast_failed', (YLeaf(YType.uint32, 'num-broadcast-failed'), ['int'])),
                            ('num_xid_mismatch', (YLeaf(YType.uint32, 'num-xid-mismatch'), ['int'])),
                            ('num_vbind_failed', (YLeaf(YType.uint32, 'num-vbind-failed'), ['int'])),
                        ])
                        self.client_ifhandle = None
                        self.interface_name = None
                        self.num_events_received = None
                        self.num_create_event_received = None
                        self.num_delete_event_received = None
                        self.num_reboot_event_received = None
                        self.num_reinit_event_received = None
                        self.num_packet_event_received = None
                        self.num_init_timer_eventi = None
                        self.num_t1_timer_event = None
                        self.num_t2_timer_event = None
                        self.num_lease_timer_event = None
                        self.num_vbind_timer_event = None
                        self.num_discovers_sent_successfully = None
                        self.num_requests_sent_successfully = None
                        self.num_releases_sent_successfully = None
                        self.num_renews_sent_successfully = None
                        self.num_rebinds_sent_successfully = None
                        self.num_declines_sent_successfully = None
                        self.num_request_after_reboot_sent = None
                        self.num_valid_offers_received = None
                        self.num_valid_acks_received = None
                        self.num_valid_nacks_received = None
                        self.num_unicast_packet_sent_successfully = None
                        self.num_broadcast_packet_sent_success = None
                        self.num_init_timer_start = None
                        self.num_init_timer_stop = None
                        self.num_t1_timer_start = None
                        self.num_t1_timer_stop = None
                        self.num_t2_timer_start = None
                        self.num_t2_timer_stop = None
                        self.num_lease_timer_start = None
                        self.num_lease_timer_stop = None
                        self.num_vbind_timer_start = None
                        self.num_vbind_timer_stop = None
                        self.num_invalid_events = None
                        self.num_discovers_failed = None
                        self.num_requests_failed = None
                        self.num_releases_failed = None
                        self.num_renews_failed = None
                        self.num_rebinds_failed = None
                        self.num_declines_failed = None
                        self.num_request_after_reboot_failed = None
                        self.num_invalid_offers = None
                        self.num_invalid_acks = None
                        self.num_invalid_nacks = None
                        self.num_invalid_packets = None
                        self.num_unicast_failed = None
                        self.num_broadcast_failed = None
                        self.num_xid_mismatch = None
                        self.num_vbind_failed = None
                        self._segment_path = lambda: "client-stat" + "[client-ifhandle='" + str(self.client_ifhandle) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DhcpClient.Nodes.Node.ClientStats.ClientStat, ['client_ifhandle', u'interface_name', u'num_events_received', u'num_create_event_received', u'num_delete_event_received', u'num_reboot_event_received', u'num_reinit_event_received', u'num_packet_event_received', u'num_init_timer_eventi', u'num_t1_timer_event', u'num_t2_timer_event', u'num_lease_timer_event', u'num_vbind_timer_event', u'num_discovers_sent_successfully', u'num_requests_sent_successfully', u'num_releases_sent_successfully', u'num_renews_sent_successfully', u'num_rebinds_sent_successfully', u'num_declines_sent_successfully', u'num_request_after_reboot_sent', u'num_valid_offers_received', u'num_valid_acks_received', u'num_valid_nacks_received', u'num_unicast_packet_sent_successfully', u'num_broadcast_packet_sent_success', u'num_init_timer_start', u'num_init_timer_stop', u'num_t1_timer_start', u'num_t1_timer_stop', u'num_t2_timer_start', u'num_t2_timer_stop', u'num_lease_timer_start', u'num_lease_timer_stop', u'num_vbind_timer_start', u'num_vbind_timer_stop', u'num_invalid_events', u'num_discovers_failed', u'num_requests_failed', u'num_releases_failed', u'num_renews_failed', u'num_rebinds_failed', u'num_declines_failed', u'num_request_after_reboot_failed', u'num_invalid_offers', u'num_invalid_acks', u'num_invalid_nacks', u'num_invalid_packets', u'num_unicast_failed', u'num_broadcast_failed', u'num_xid_mismatch', u'num_vbind_failed'], name, value)


            class Clients(Entity):
                """
                IPv4 DHCP client table
                
                .. attribute:: client
                
                	Single DHCP client binding
                	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpClient.Nodes.Node.Clients.Client>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(DhcpClient.Nodes.Node.Clients, self).__init__()

                    self.yang_name = "clients"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("client", ("client", DhcpClient.Nodes.Node.Clients.Client))])
                    self._leafs = OrderedDict()

                    self.client = YList(self)
                    self._segment_path = lambda: "clients"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DhcpClient.Nodes.Node.Clients, [], name, value)


                class Client(Entity):
                    """
                    Single DHCP client binding
                    
                    .. attribute:: client_ifhandle  (key)
                    
                    	Client Ifhandle
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: interface_name
                    
                    	Dhcp Client interface name
                    	**type**\: str
                    
                    	**length:** 0..65
                    
                    .. attribute:: client_mac_address
                    
                    	Dhcp Client Interface MAC address
                    	**type**\: str
                    
                    	**length:** 0..17
                    
                    .. attribute:: client_id
                    
                    	Dhcp Client ID
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    .. attribute:: ipv4_client_state
                    
                    	Dhcp Client State
                    	**type**\:  :py:class:`DhcpcIpv4State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpcIpv4State>`
                    
                    .. attribute:: ipv4_address
                    
                    	Dhcp Client IP Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_subnet_mask
                    
                    	Dhcp Client IP Address mask
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_server_address
                    
                    	Dhcp Client selected server IP Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: next_hop_ipv4_address
                    
                    	Dhcp Client next hop IP Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_lease_time
                    
                    	Dhcp Client Lease time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_renew_time
                    
                    	Dhcp Client Renew time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_rebind_time
                    
                    	Dhcp Client Rebind time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_address_configured
                    
                    	Dhcp Client IPV4 address configured in interface
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(DhcpClient.Nodes.Node.Clients.Client, self).__init__()

                        self.yang_name = "client"
                        self.yang_parent_name = "clients"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['client_ifhandle']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('client_ifhandle', (YLeaf(YType.str, 'client-ifhandle'), ['str'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('client_mac_address', (YLeaf(YType.str, 'client-mac-address'), ['str'])),
                            ('client_id', (YLeaf(YType.str, 'client-id'), ['str'])),
                            ('ipv4_client_state', (YLeaf(YType.enumeration, 'ipv4-client-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpcIpv4State', '')])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                            ('ipv4_subnet_mask', (YLeaf(YType.str, 'ipv4-subnet-mask'), ['str'])),
                            ('ipv4_server_address', (YLeaf(YType.str, 'ipv4-server-address'), ['str'])),
                            ('next_hop_ipv4_address', (YLeaf(YType.str, 'next-hop-ipv4-address'), ['str'])),
                            ('ipv4_lease_time', (YLeaf(YType.uint32, 'ipv4-lease-time'), ['int'])),
                            ('ipv4_renew_time', (YLeaf(YType.uint32, 'ipv4-renew-time'), ['int'])),
                            ('ipv4_rebind_time', (YLeaf(YType.uint32, 'ipv4-rebind-time'), ['int'])),
                            ('ipv4_address_configured', (YLeaf(YType.boolean, 'ipv4-address-configured'), ['bool'])),
                        ])
                        self.client_ifhandle = None
                        self.interface_name = None
                        self.client_mac_address = None
                        self.client_id = None
                        self.ipv4_client_state = None
                        self.ipv4_address = None
                        self.ipv4_subnet_mask = None
                        self.ipv4_server_address = None
                        self.next_hop_ipv4_address = None
                        self.ipv4_lease_time = None
                        self.ipv4_renew_time = None
                        self.ipv4_rebind_time = None
                        self.ipv4_address_configured = None
                        self._segment_path = lambda: "client" + "[client-ifhandle='" + str(self.client_ifhandle) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DhcpClient.Nodes.Node.Clients.Client, ['client_ifhandle', u'interface_name', u'client_mac_address', u'client_id', u'ipv4_client_state', u'ipv4_address', u'ipv4_subnet_mask', u'ipv4_server_address', u'next_hop_ipv4_address', u'ipv4_lease_time', u'ipv4_renew_time', u'ipv4_rebind_time', u'ipv4_address_configured'], name, value)

    def clone_ptr(self):
        self._top_entity = DhcpClient()
        return self._top_entity

class Ipv4Dhcpd(Entity):
    """
    ipv4 dhcpd
    
    .. attribute:: snoop
    
    	DHCP Snoop operational data
    	**type**\:  :py:class:`Snoop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop>`
    
    .. attribute:: nodes
    
    	IPv4 DHCPD operational data for a particular location
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes>`
    
    

    """

    _prefix = 'ipv4-dhcpd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipv4Dhcpd, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-dhcpd"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-dhcpd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("snoop", ("snoop", Ipv4Dhcpd.Snoop)), ("nodes", ("nodes", Ipv4Dhcpd.Nodes))])
        self._leafs = OrderedDict()

        self.snoop = Ipv4Dhcpd.Snoop()
        self.snoop.parent = self
        self._children_name_map["snoop"] = "snoop"

        self.nodes = Ipv4Dhcpd.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv4Dhcpd, [], name, value)


    class Snoop(Entity):
        """
        DHCP Snoop operational data
        
        .. attribute:: bindings
        
        	DHCP Snoop Bindings
        	**type**\:  :py:class:`Bindings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Bindings>`
        
        .. attribute:: binding_statistics
        
        	DHCP snoop binding statistics
        	**type**\:  :py:class:`BindingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.BindingStatistics>`
        
        .. attribute:: statistics_info
        
        	DHCP snoop statistics info
        	**type**\:  :py:class:`StatisticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.StatisticsInfo>`
        
        .. attribute:: profiles
        
        	DHCP Snoop Profile
        	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Profiles>`
        
        .. attribute:: statistics
        
        	DHCP Snoop Statistics
        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Statistics>`
        
        

        """

        _prefix = 'ipv4-dhcpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv4Dhcpd.Snoop, self).__init__()

            self.yang_name = "snoop"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("bindings", ("bindings", Ipv4Dhcpd.Snoop.Bindings)), ("binding-statistics", ("binding_statistics", Ipv4Dhcpd.Snoop.BindingStatistics)), ("statistics-info", ("statistics_info", Ipv4Dhcpd.Snoop.StatisticsInfo)), ("profiles", ("profiles", Ipv4Dhcpd.Snoop.Profiles)), ("statistics", ("statistics", Ipv4Dhcpd.Snoop.Statistics))])
            self._leafs = OrderedDict()

            self.bindings = Ipv4Dhcpd.Snoop.Bindings()
            self.bindings.parent = self
            self._children_name_map["bindings"] = "bindings"

            self.binding_statistics = Ipv4Dhcpd.Snoop.BindingStatistics()
            self.binding_statistics.parent = self
            self._children_name_map["binding_statistics"] = "binding-statistics"

            self.statistics_info = Ipv4Dhcpd.Snoop.StatisticsInfo()
            self.statistics_info.parent = self
            self._children_name_map["statistics_info"] = "statistics-info"

            self.profiles = Ipv4Dhcpd.Snoop.Profiles()
            self.profiles.parent = self
            self._children_name_map["profiles"] = "profiles"

            self.statistics = Ipv4Dhcpd.Snoop.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._segment_path = lambda: "snoop"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.Snoop, [], name, value)


        class Bindings(Entity):
            """
            DHCP Snoop Bindings
            
            .. attribute:: binding
            
            	DHCP Snoop binding
            	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Bindings.Binding>`
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4Dhcpd.Snoop.Bindings, self).__init__()

                self.yang_name = "bindings"
                self.yang_parent_name = "snoop"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("binding", ("binding", Ipv4Dhcpd.Snoop.Bindings.Binding))])
                self._leafs = OrderedDict()

                self.binding = YList(self)
                self._segment_path = lambda: "bindings"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/snoop/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Snoop.Bindings, [], name, value)


            class Binding(Entity):
                """
                DHCP Snoop binding
                
                .. attribute:: client_uid  (key)
                
                	Client opaque handle
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: snoop_binding_ch_addr
                
                	DHCP client MAC address
                	**type**\: str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                .. attribute:: snoop_binding_ch_addr_len
                
                	DHCP client MAC address length
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: snoop_binding_i_addr
                
                	DHCP iaddr
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: snoop_binding_client_id
                
                	DHCP client id
                	**type**\: str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                .. attribute:: snoop_binding_client_id_len
                
                	DHCP client id len
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: snoop_binding_state
                
                	DHCP sm state
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: snoop_binding_lease
                
                	DHCP lease time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: snoop_binding_lease_start_time
                
                	DHCP lease start time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: snoop_binding_profile_name
                
                	DHCP profile name
                	**type**\: str
                
                	**length:** 0..65
                
                .. attribute:: snoop_bindng_interface_name
                
                	DHCP interface to client
                	**type**\: str
                
                	**length:** 0..321
                
                .. attribute:: snoop_binding_bridge_name
                
                	DHCP L2 bridge name
                	**type**\: str
                
                	**length:** 0..74
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Snoop.Bindings.Binding, self).__init__()

                    self.yang_name = "binding"
                    self.yang_parent_name = "bindings"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['client_uid']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('client_uid', (YLeaf(YType.str, 'client-uid'), ['str'])),
                        ('snoop_binding_ch_addr', (YLeaf(YType.str, 'snoop-binding-ch-addr'), ['str'])),
                        ('snoop_binding_ch_addr_len', (YLeaf(YType.uint8, 'snoop-binding-ch-addr-len'), ['int'])),
                        ('snoop_binding_i_addr', (YLeaf(YType.str, 'snoop-binding-i-addr'), ['str'])),
                        ('snoop_binding_client_id', (YLeaf(YType.str, 'snoop-binding-client-id'), ['str'])),
                        ('snoop_binding_client_id_len', (YLeaf(YType.uint8, 'snoop-binding-client-id-len'), ['int'])),
                        ('snoop_binding_state', (YLeaf(YType.uint8, 'snoop-binding-state'), ['int'])),
                        ('snoop_binding_lease', (YLeaf(YType.uint32, 'snoop-binding-lease'), ['int'])),
                        ('snoop_binding_lease_start_time', (YLeaf(YType.uint32, 'snoop-binding-lease-start-time'), ['int'])),
                        ('snoop_binding_profile_name', (YLeaf(YType.str, 'snoop-binding-profile-name'), ['str'])),
                        ('snoop_bindng_interface_name', (YLeaf(YType.str, 'snoop-bindng-interface-name'), ['str'])),
                        ('snoop_binding_bridge_name', (YLeaf(YType.str, 'snoop-binding-bridge-name'), ['str'])),
                    ])
                    self.client_uid = None
                    self.snoop_binding_ch_addr = None
                    self.snoop_binding_ch_addr_len = None
                    self.snoop_binding_i_addr = None
                    self.snoop_binding_client_id = None
                    self.snoop_binding_client_id_len = None
                    self.snoop_binding_state = None
                    self.snoop_binding_lease = None
                    self.snoop_binding_lease_start_time = None
                    self.snoop_binding_profile_name = None
                    self.snoop_bindng_interface_name = None
                    self.snoop_binding_bridge_name = None
                    self._segment_path = lambda: "binding" + "[client-uid='" + str(self.client_uid) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/snoop/bindings/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Snoop.Bindings.Binding, ['client_uid', u'snoop_binding_ch_addr', u'snoop_binding_ch_addr_len', u'snoop_binding_i_addr', u'snoop_binding_client_id', u'snoop_binding_client_id_len', u'snoop_binding_state', u'snoop_binding_lease', u'snoop_binding_lease_start_time', u'snoop_binding_profile_name', u'snoop_bindng_interface_name', u'snoop_binding_bridge_name'], name, value)


        class BindingStatistics(Entity):
            """
            DHCP snoop binding statistics
            
            .. attribute:: snoop_binding_total
            
            	Total number of snoop bindings
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: snoop_binding_timestamp
            
            	Snoop binding timestamp
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4Dhcpd.Snoop.BindingStatistics, self).__init__()

                self.yang_name = "binding-statistics"
                self.yang_parent_name = "snoop"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('snoop_binding_total', (YLeaf(YType.uint32, 'snoop-binding-total'), ['int'])),
                    ('snoop_binding_timestamp', (YLeaf(YType.uint32, 'snoop-binding-timestamp'), ['int'])),
                ])
                self.snoop_binding_total = None
                self.snoop_binding_timestamp = None
                self._segment_path = lambda: "binding-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/snoop/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Snoop.BindingStatistics, [u'snoop_binding_total', u'snoop_binding_timestamp'], name, value)


        class StatisticsInfo(Entity):
            """
            DHCP snoop statistics info
            
            .. attribute:: snoop_stats_timestamp
            
            	Snoop Stats timestamp
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4Dhcpd.Snoop.StatisticsInfo, self).__init__()

                self.yang_name = "statistics-info"
                self.yang_parent_name = "snoop"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('snoop_stats_timestamp', (YLeaf(YType.uint32, 'snoop-stats-timestamp'), ['int'])),
                ])
                self.snoop_stats_timestamp = None
                self._segment_path = lambda: "statistics-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/snoop/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Snoop.StatisticsInfo, [u'snoop_stats_timestamp'], name, value)


        class Profiles(Entity):
            """
            DHCP Snoop Profile
            
            .. attribute:: profile
            
            	DHCP Snoop profile
            	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Profiles.Profile>`
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4Dhcpd.Snoop.Profiles, self).__init__()

                self.yang_name = "profiles"
                self.yang_parent_name = "snoop"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("profile", ("profile", Ipv4Dhcpd.Snoop.Profiles.Profile))])
                self._leafs = OrderedDict()

                self.profile = YList(self)
                self._segment_path = lambda: "profiles"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/snoop/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Snoop.Profiles, [], name, value)


            class Profile(Entity):
                """
                DHCP Snoop profile
                
                .. attribute:: profile_name  (key)
                
                	Profile name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: snoop_profile_name
                
                	Profile Name
                	**type**\: str
                
                	**length:** 0..65
                
                .. attribute:: snoop_profile_uid
                
                	Profile unique ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: snoop_profile_relay_info_option
                
                	Relay info option
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: snoop_profile_relay_info_allow_untrusted
                
                	Allow untrusted relay info
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: snoop_profile_relay_info_policy
                
                	Relay info policy
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: snoop_profile_trusted
                
                	Trust
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Snoop.Profiles.Profile, self).__init__()

                    self.yang_name = "profile"
                    self.yang_parent_name = "profiles"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['profile_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                        ('snoop_profile_name', (YLeaf(YType.str, 'snoop-profile-name'), ['str'])),
                        ('snoop_profile_uid', (YLeaf(YType.uint32, 'snoop-profile-uid'), ['int'])),
                        ('snoop_profile_relay_info_option', (YLeaf(YType.uint8, 'snoop-profile-relay-info-option'), ['int'])),
                        ('snoop_profile_relay_info_allow_untrusted', (YLeaf(YType.uint8, 'snoop-profile-relay-info-allow-untrusted'), ['int'])),
                        ('snoop_profile_relay_info_policy', (YLeaf(YType.uint8, 'snoop-profile-relay-info-policy'), ['int'])),
                        ('snoop_profile_trusted', (YLeaf(YType.uint8, 'snoop-profile-trusted'), ['int'])),
                    ])
                    self.profile_name = None
                    self.snoop_profile_name = None
                    self.snoop_profile_uid = None
                    self.snoop_profile_relay_info_option = None
                    self.snoop_profile_relay_info_allow_untrusted = None
                    self.snoop_profile_relay_info_policy = None
                    self.snoop_profile_trusted = None
                    self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/snoop/profiles/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Snoop.Profiles.Profile, ['profile_name', u'snoop_profile_name', u'snoop_profile_uid', u'snoop_profile_relay_info_option', u'snoop_profile_relay_info_allow_untrusted', u'snoop_profile_relay_info_policy', u'snoop_profile_trusted'], name, value)


        class Statistics(Entity):
            """
            DHCP Snoop Statistics
            
            .. attribute:: statistic
            
            	DHCP Snoop bridge domain statistics
            	**type**\: list of  		 :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Snoop.Statistics.Statistic>`
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4Dhcpd.Snoop.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "snoop"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("statistic", ("statistic", Ipv4Dhcpd.Snoop.Statistics.Statistic))])
                self._leafs = OrderedDict()

                self.statistic = YList(self)
                self._segment_path = lambda: "statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/snoop/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Snoop.Statistics, [], name, value)


            class Statistic(Entity):
                """
                DHCP Snoop bridge domain statistics
                
                .. attribute:: bridge_name  (key)
                
                	Bridge domain name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: snoop_statistics_bridge_name
                
                	DHCP L2 bridge name
                	**type**\: str
                
                	**length:** 0..74
                
                .. attribute:: snoop_statistic
                
                	Public snoop statistics
                	**type**\: list of int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Snoop.Statistics.Statistic, self).__init__()

                    self.yang_name = "statistic"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['bridge_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('bridge_name', (YLeaf(YType.str, 'bridge-name'), ['str'])),
                        ('snoop_statistics_bridge_name', (YLeaf(YType.str, 'snoop-statistics-bridge-name'), ['str'])),
                        ('snoop_statistic', (YLeafList(YType.uint64, 'snoop-statistic'), ['int'])),
                    ])
                    self.bridge_name = None
                    self.snoop_statistics_bridge_name = None
                    self.snoop_statistic = []
                    self._segment_path = lambda: "statistic" + "[bridge-name='" + str(self.bridge_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/snoop/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Snoop.Statistics.Statistic, ['bridge_name', u'snoop_statistics_bridge_name', u'snoop_statistic'], name, value)


    class Nodes(Entity):
        """
        IPv4 DHCPD operational data for a particular
        location
        
        .. attribute:: node
        
        	Location. For eg., 0/1/CPU0
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node>`
        
        

        """

        _prefix = 'ipv4-dhcpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv4Dhcpd.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Ipv4Dhcpd.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.Nodes, [], name, value)


        class Node(Entity):
            """
            Location. For eg., 0/1/CPU0
            
            .. attribute:: nodeid  (key)
            
            	The node id to filter on. For eg., 0/1/CPU0
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: proxy
            
            	IPv4 DHCP proxy operational data
            	**type**\:  :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy>`
            
            .. attribute:: interfaces
            
            	IPv4 DHCP proxy/server Interface
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Interfaces>`
            
            .. attribute:: base
            
            	IPv4 DHCP base operational data
            	**type**\:  :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base>`
            
            .. attribute:: server
            
            	IPv4 DHCP Server operational data
            	**type**\:  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server>`
            
            .. attribute:: relay
            
            	IPv4 DHCPD Relay operational data
            	**type**\:  :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay>`
            
            

            """

            _prefix = 'ipv4-dhcpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4Dhcpd.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nodeid']
                self._child_classes = OrderedDict([("proxy", ("proxy", Ipv4Dhcpd.Nodes.Node.Proxy)), ("interfaces", ("interfaces", Ipv4Dhcpd.Nodes.Node.Interfaces)), ("base", ("base", Ipv4Dhcpd.Nodes.Node.Base)), ("server", ("server", Ipv4Dhcpd.Nodes.Node.Server)), ("relay", ("relay", Ipv4Dhcpd.Nodes.Node.Relay))])
                self._leafs = OrderedDict([
                    ('nodeid', (YLeaf(YType.str, 'nodeid'), ['str'])),
                ])
                self.nodeid = None

                self.proxy = Ipv4Dhcpd.Nodes.Node.Proxy()
                self.proxy.parent = self
                self._children_name_map["proxy"] = "proxy"

                self.interfaces = Ipv4Dhcpd.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.base = Ipv4Dhcpd.Nodes.Node.Base()
                self.base.parent = self
                self._children_name_map["base"] = "base"

                self.server = Ipv4Dhcpd.Nodes.Node.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"

                self.relay = Ipv4Dhcpd.Nodes.Node.Relay()
                self.relay.parent = self
                self._children_name_map["relay"] = "relay"
                self._segment_path = lambda: "node" + "[nodeid='" + str(self.nodeid) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-oper:ipv4-dhcpd/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Nodes.Node, ['nodeid'], name, value)


            class Proxy(Entity):
                """
                IPv4 DHCP proxy operational data
                
                .. attribute:: statistics_info
                
                	DHCP proxy stats info
                	**type**\:  :py:class:`StatisticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo>`
                
                .. attribute:: vrfs
                
                	DHCP proxy list of VRF names
                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs>`
                
                .. attribute:: profiles
                
                	IPv4 DHCP proxy profile
                	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles>`
                
                .. attribute:: statistics
                
                	DHCP proxy statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Statistics>`
                
                .. attribute:: binding
                
                	DHCP proxy bindings
                	**type**\:  :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Binding>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Nodes.Node.Proxy, self).__init__()

                    self.yang_name = "proxy"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statistics-info", ("statistics_info", Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo)), ("vrfs", ("vrfs", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs)), ("profiles", ("profiles", Ipv4Dhcpd.Nodes.Node.Proxy.Profiles)), ("statistics", ("statistics", Ipv4Dhcpd.Nodes.Node.Proxy.Statistics)), ("binding", ("binding", Ipv4Dhcpd.Nodes.Node.Proxy.Binding))])
                    self._leafs = OrderedDict()

                    self.statistics_info = Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo()
                    self.statistics_info.parent = self
                    self._children_name_map["statistics_info"] = "statistics-info"

                    self.vrfs = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"

                    self.profiles = Ipv4Dhcpd.Nodes.Node.Proxy.Profiles()
                    self.profiles.parent = self
                    self._children_name_map["profiles"] = "profiles"

                    self.statistics = Ipv4Dhcpd.Nodes.Node.Proxy.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"

                    self.binding = Ipv4Dhcpd.Nodes.Node.Proxy.Binding()
                    self.binding.parent = self
                    self._children_name_map["binding"] = "binding"
                    self._segment_path = lambda: "proxy"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy, [], name, value)


                class StatisticsInfo(Entity):
                    """
                    DHCP proxy stats info
                    
                    .. attribute:: proxy_stats_timestamp
                    
                    	Proxy Stats timestamp
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo, self).__init__()

                        self.yang_name = "statistics-info"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('proxy_stats_timestamp', (YLeaf(YType.uint32, 'proxy-stats-timestamp'), ['int'])),
                        ])
                        self.proxy_stats_timestamp = None
                        self._segment_path = lambda: "statistics-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo, [u'proxy_stats_timestamp'], name, value)


                class Vrfs(Entity):
                    """
                    DHCP proxy list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv4 DHCP proxy VRF name
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vrf", ("vrf", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf))])
                        self._leafs = OrderedDict()

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs, [], name, value)


                    class Vrf(Entity):
                        """
                        IPv4 DHCP proxy VRF name
                        
                        .. attribute:: vrf_name  (key)
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv4 DHCP proxy statistics
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_classes = OrderedDict([("statistics", ("statistics", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics))])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None

                            self.statistics = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf, ['vrf_name'], name, value)


                        class Statistics(Entity):
                            """
                            IPv4 DHCP proxy statistics
                            
                            .. attribute:: discover
                            
                            	DHCP discover packets
                            	**type**\:  :py:class:`Discover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover>`
                            
                            .. attribute:: offer
                            
                            	DHCP offer packets
                            	**type**\:  :py:class:`Offer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer>`
                            
                            .. attribute:: request
                            
                            	DHCP request packets
                            	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: decline
                            
                            	DHCP decline packets
                            	**type**\:  :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: ack
                            
                            	DHCP ack packets
                            	**type**\:  :py:class:`Ack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack>`
                            
                            .. attribute:: nak
                            
                            	DHCP nak packets
                            	**type**\:  :py:class:`Nak <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak>`
                            
                            .. attribute:: release
                            
                            	DHCP release packets
                            	**type**\:  :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: inform
                            
                            	DHCP inform packets
                            	**type**\:  :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: lease_query
                            
                            	DHCP lease query packets
                            	**type**\:  :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_not_assigned
                            
                            	DHCP lease not assigned
                            	**type**\:  :py:class:`LeaseNotAssigned <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned>`
                            
                            .. attribute:: lease_unknown
                            
                            	DHCP lease unknown
                            	**type**\:  :py:class:`LeaseUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown>`
                            
                            .. attribute:: lease_active
                            
                            	DHCP lease active
                            	**type**\:  :py:class:`LeaseActive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive>`
                            
                            .. attribute:: bootp_request
                            
                            	DHCP BOOTP request
                            	**type**\:  :py:class:`BootpRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest>`
                            
                            .. attribute:: bootp_reply
                            
                            	DHCP BOOTP reply
                            	**type**\:  :py:class:`BootpReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("discover", ("discover", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover)), ("offer", ("offer", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer)), ("request", ("request", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request)), ("decline", ("decline", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline)), ("ack", ("ack", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack)), ("nak", ("nak", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak)), ("release", ("release", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release)), ("inform", ("inform", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform)), ("lease-query", ("lease_query", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery)), ("lease-not-assigned", ("lease_not_assigned", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned)), ("lease-unknown", ("lease_unknown", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown)), ("lease-active", ("lease_active", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive)), ("bootp-request", ("bootp_request", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest)), ("bootp-reply", ("bootp_reply", Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply))])
                                self._leafs = OrderedDict()

                                self.discover = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover()
                                self.discover.parent = self
                                self._children_name_map["discover"] = "discover"

                                self.offer = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer()
                                self.offer.parent = self
                                self._children_name_map["offer"] = "offer"

                                self.request = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self._children_name_map["request"] = "request"

                                self.decline = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self._children_name_map["decline"] = "decline"

                                self.ack = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack()
                                self.ack.parent = self
                                self._children_name_map["ack"] = "ack"

                                self.nak = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak()
                                self.nak.parent = self
                                self._children_name_map["nak"] = "nak"

                                self.release = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self._children_name_map["release"] = "release"

                                self.inform = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self._children_name_map["inform"] = "inform"

                                self.lease_query = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self._children_name_map["lease_query"] = "lease-query"

                                self.lease_not_assigned = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned()
                                self.lease_not_assigned.parent = self
                                self._children_name_map["lease_not_assigned"] = "lease-not-assigned"

                                self.lease_unknown = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown()
                                self.lease_unknown.parent = self
                                self._children_name_map["lease_unknown"] = "lease-unknown"

                                self.lease_active = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive()
                                self.lease_active.parent = self
                                self._children_name_map["lease_active"] = "lease-active"

                                self.bootp_request = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest()
                                self.bootp_request.parent = self
                                self._children_name_map["bootp_request"] = "bootp-request"

                                self.bootp_reply = Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply()
                                self.bootp_reply.parent = self
                                self._children_name_map["bootp_reply"] = "bootp-reply"
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics, [], name, value)


                            class Discover(Entity):
                                """
                                DHCP discover packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover, self).__init__()

                                    self.yang_name = "discover"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "discover"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Offer(Entity):
                                """
                                DHCP offer packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer, self).__init__()

                                    self.yang_name = "offer"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "offer"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Request(Entity):
                                """
                                DHCP request packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request, self).__init__()

                                    self.yang_name = "request"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "request"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Decline(Entity):
                                """
                                DHCP decline packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline, self).__init__()

                                    self.yang_name = "decline"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "decline"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Ack(Entity):
                                """
                                DHCP ack packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack, self).__init__()

                                    self.yang_name = "ack"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "ack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Nak(Entity):
                                """
                                DHCP nak packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak, self).__init__()

                                    self.yang_name = "nak"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "nak"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Release(Entity):
                                """
                                DHCP release packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release, self).__init__()

                                    self.yang_name = "release"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "release"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Inform(Entity):
                                """
                                DHCP inform packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform, self).__init__()

                                    self.yang_name = "inform"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "inform"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseQuery(Entity):
                                """
                                DHCP lease query packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery, self).__init__()

                                    self.yang_name = "lease-query"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseNotAssigned(Entity):
                                """
                                DHCP lease not assigned
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned, self).__init__()

                                    self.yang_name = "lease-not-assigned"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-not-assigned"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseUnknown(Entity):
                                """
                                DHCP lease unknown
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown, self).__init__()

                                    self.yang_name = "lease-unknown"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-unknown"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseActive(Entity):
                                """
                                DHCP lease active
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive, self).__init__()

                                    self.yang_name = "lease-active"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-active"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class BootpRequest(Entity):
                                """
                                DHCP BOOTP request
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest, self).__init__()

                                    self.yang_name = "bootp-request"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "bootp-request"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class BootpReply(Entity):
                                """
                                DHCP BOOTP reply
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply, self).__init__()

                                    self.yang_name = "bootp-reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "bootp-reply"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                class Profiles(Entity):
                    """
                    IPv4 DHCP proxy profile
                    
                    .. attribute:: profile
                    
                    	IPv4 DHCP proxy profile
                    	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles, self).__init__()

                        self.yang_name = "profiles"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("profile", ("profile", Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile))])
                        self._leafs = OrderedDict()

                        self.profile = YList(self)
                        self._segment_path = lambda: "profiles"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles, [], name, value)


                    class Profile(Entity):
                        """
                        IPv4 DHCP proxy profile
                        
                        .. attribute:: profile_name  (key)
                        
                        	Profile name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: vrf_references
                        
                        	VRF references
                        	**type**\:  :py:class:`VrfReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences>`
                        
                        .. attribute:: interface_references
                        
                        	Interface references
                        	**type**\:  :py:class:`InterfaceReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences>`
                        
                        .. attribute:: is_relay_option_enabled
                        
                        	Is true if relay option is enabled
                        	**type**\: bool
                        
                        .. attribute:: relay_policy
                        
                        	Relay policy
                        	**type**\:  :py:class:`RelayInfoPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.RelayInfoPolicy>`
                        
                        .. attribute:: relay_authenticate
                        
                        	Relay authenticate
                        	**type**\:  :py:class:`RelayInfoAuthenticate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.RelayInfoAuthenticate>`
                        
                        .. attribute:: is_relay_allow_untrusted_enabled
                        
                        	Is true if relay untrusted is enabled
                        	**type**\: bool
                        
                        .. attribute:: is_relay_optionvpn_enabled
                        
                        	Is true if relay VPN enabled
                        	**type**\: bool
                        
                        .. attribute:: relay_optionvpn_enabled_mode
                        
                        	Relay VPN RFC/Cisco mode
                        	**type**\:  :py:class:`RelayInfoVpnMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.RelayInfoVpnMode>`
                        
                        .. attribute:: is_relay_check
                        
                        	Is true if relay check enabled
                        	**type**\: bool
                        
                        .. attribute:: is_move_allowed
                        
                        	Is true if dhcp subscriber is allowed to move
                        	**type**\: bool
                        
                        .. attribute:: proxy_broadcast_flag_policy
                        
                        	Broadcast policy
                        	**type**\:  :py:class:`BroadcastFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.BroadcastFlag>`
                        
                        .. attribute:: proxy_profile_client_lease_time
                        
                        	Client lease time in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: proxy_lease_limit_type
                        
                        	Lease limit type
                        	**type**\:  :py:class:`ProxyLeaseLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.ProxyLeaseLimit>`
                        
                        .. attribute:: proxy_lease_limit_count
                        
                        	Lease limit count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: profile_helper_address
                        
                        	Helper addresses
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF names
                        	**type**\: list of str
                        
                        	**length:** 0..33
                        
                        .. attribute:: gi_addr
                        
                        	Gateway addresses
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile, self).__init__()

                            self.yang_name = "profile"
                            self.yang_parent_name = "profiles"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['profile_name']
                            self._child_classes = OrderedDict([("vrf-references", ("vrf_references", Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences)), ("interface-references", ("interface_references", Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences))])
                            self._leafs = OrderedDict([
                                ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                ('is_relay_option_enabled', (YLeaf(YType.boolean, 'is-relay-option-enabled'), ['bool'])),
                                ('relay_policy', (YLeaf(YType.enumeration, 'relay-policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'RelayInfoPolicy', '')])),
                                ('relay_authenticate', (YLeaf(YType.enumeration, 'relay-authenticate'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'RelayInfoAuthenticate', '')])),
                                ('is_relay_allow_untrusted_enabled', (YLeaf(YType.boolean, 'is-relay-allow-untrusted-enabled'), ['bool'])),
                                ('is_relay_optionvpn_enabled', (YLeaf(YType.boolean, 'is-relay-optionvpn-enabled'), ['bool'])),
                                ('relay_optionvpn_enabled_mode', (YLeaf(YType.enumeration, 'relay-optionvpn-enabled-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'RelayInfoVpnMode', '')])),
                                ('is_relay_check', (YLeaf(YType.boolean, 'is-relay-check'), ['bool'])),
                                ('is_move_allowed', (YLeaf(YType.boolean, 'is-move-allowed'), ['bool'])),
                                ('proxy_broadcast_flag_policy', (YLeaf(YType.enumeration, 'proxy-broadcast-flag-policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'BroadcastFlag', '')])),
                                ('proxy_profile_client_lease_time', (YLeaf(YType.uint32, 'proxy-profile-client-lease-time'), ['int'])),
                                ('proxy_lease_limit_type', (YLeaf(YType.enumeration, 'proxy-lease-limit-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'ProxyLeaseLimit', '')])),
                                ('proxy_lease_limit_count', (YLeaf(YType.uint32, 'proxy-lease-limit-count'), ['int'])),
                                ('profile_helper_address', (YLeafList(YType.str, 'profile-helper-address'), ['str'])),
                                ('vrf_name', (YLeafList(YType.str, 'vrf-name'), ['str'])),
                                ('gi_addr', (YLeafList(YType.str, 'gi-addr'), ['str'])),
                            ])
                            self.profile_name = None
                            self.is_relay_option_enabled = None
                            self.relay_policy = None
                            self.relay_authenticate = None
                            self.is_relay_allow_untrusted_enabled = None
                            self.is_relay_optionvpn_enabled = None
                            self.relay_optionvpn_enabled_mode = None
                            self.is_relay_check = None
                            self.is_move_allowed = None
                            self.proxy_broadcast_flag_policy = None
                            self.proxy_profile_client_lease_time = None
                            self.proxy_lease_limit_type = None
                            self.proxy_lease_limit_count = None
                            self.profile_helper_address = []
                            self.vrf_name = []
                            self.gi_addr = []

                            self.vrf_references = Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences()
                            self.vrf_references.parent = self
                            self._children_name_map["vrf_references"] = "vrf-references"

                            self.interface_references = Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences()
                            self.interface_references.parent = self
                            self._children_name_map["interface_references"] = "interface-references"
                            self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile, ['profile_name', u'is_relay_option_enabled', u'relay_policy', u'relay_authenticate', u'is_relay_allow_untrusted_enabled', u'is_relay_optionvpn_enabled', u'relay_optionvpn_enabled_mode', u'is_relay_check', u'is_move_allowed', u'proxy_broadcast_flag_policy', u'proxy_profile_client_lease_time', u'proxy_lease_limit_type', u'proxy_lease_limit_count', u'profile_helper_address', u'vrf_name', u'gi_addr'], name, value)


                        class VrfReferences(Entity):
                            """
                            VRF references
                            
                            .. attribute:: ipv4_dhcpd_proxy_vrf_reference
                            
                            	ipv4 dhcpd proxy vrf reference
                            	**type**\: list of  		 :py:class:`Ipv4DhcpdProxyVrfReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences.Ipv4DhcpdProxyVrfReference>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences, self).__init__()

                                self.yang_name = "vrf-references"
                                self.yang_parent_name = "profile"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ipv4-dhcpd-proxy-vrf-reference", ("ipv4_dhcpd_proxy_vrf_reference", Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences.Ipv4DhcpdProxyVrfReference))])
                                self._leafs = OrderedDict()

                                self.ipv4_dhcpd_proxy_vrf_reference = YList(self)
                                self._segment_path = lambda: "vrf-references"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences, [], name, value)


                            class Ipv4DhcpdProxyVrfReference(Entity):
                                """
                                ipv4 dhcpd proxy vrf reference
                                
                                .. attribute:: proxy_reference_vrf_name
                                
                                	VRF name
                                	**type**\: str
                                
                                	**length:** 0..33
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences.Ipv4DhcpdProxyVrfReference, self).__init__()

                                    self.yang_name = "ipv4-dhcpd-proxy-vrf-reference"
                                    self.yang_parent_name = "vrf-references"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('proxy_reference_vrf_name', (YLeaf(YType.str, 'proxy-reference-vrf-name'), ['str'])),
                                    ])
                                    self.proxy_reference_vrf_name = None
                                    self._segment_path = lambda: "ipv4-dhcpd-proxy-vrf-reference"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences.Ipv4DhcpdProxyVrfReference, [u'proxy_reference_vrf_name'], name, value)


                        class InterfaceReferences(Entity):
                            """
                            Interface references
                            
                            .. attribute:: ipv4_dhcpd_proxy_interface_reference
                            
                            	ipv4 dhcpd proxy interface reference
                            	**type**\: list of  		 :py:class:`Ipv4DhcpdProxyInterfaceReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences.Ipv4DhcpdProxyInterfaceReference>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences, self).__init__()

                                self.yang_name = "interface-references"
                                self.yang_parent_name = "profile"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ipv4-dhcpd-proxy-interface-reference", ("ipv4_dhcpd_proxy_interface_reference", Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences.Ipv4DhcpdProxyInterfaceReference))])
                                self._leafs = OrderedDict()

                                self.ipv4_dhcpd_proxy_interface_reference = YList(self)
                                self._segment_path = lambda: "interface-references"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences, [], name, value)


                            class Ipv4DhcpdProxyInterfaceReference(Entity):
                                """
                                ipv4 dhcpd proxy interface reference
                                
                                .. attribute:: proxy_reference_interface_name
                                
                                	Interface name
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences.Ipv4DhcpdProxyInterfaceReference, self).__init__()

                                    self.yang_name = "ipv4-dhcpd-proxy-interface-reference"
                                    self.yang_parent_name = "interface-references"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('proxy_reference_interface_name', (YLeaf(YType.str, 'proxy-reference-interface-name'), ['str'])),
                                    ])
                                    self.proxy_reference_interface_name = None
                                    self._segment_path = lambda: "ipv4-dhcpd-proxy-interface-reference"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences.Ipv4DhcpdProxyInterfaceReference, [u'proxy_reference_interface_name'], name, value)


                class Statistics(Entity):
                    """
                    DHCP proxy statistics
                    
                    .. attribute:: ipv4_dhcpd_proxy_stat
                    
                    	ipv4 dhcpd proxy stat
                    	**type**\: list of  		 :py:class:`Ipv4DhcpdProxyStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Proxy.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv4-dhcpd-proxy-stat", ("ipv4_dhcpd_proxy_stat", Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat))])
                        self._leafs = OrderedDict()

                        self.ipv4_dhcpd_proxy_stat = YList(self)
                        self._segment_path = lambda: "statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Statistics, [], name, value)


                    class Ipv4DhcpdProxyStat(Entity):
                        """
                        ipv4 dhcpd proxy stat
                        
                        .. attribute:: statistics
                        
                        	Proxy statistics
                        	**type**\:  :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCP L3 VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat, self).__init__()

                            self.yang_name = "ipv4-dhcpd-proxy-stat"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("statistics", ("statistics", Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_))])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None

                            self.statistics = Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._segment_path = lambda: "ipv4-dhcpd-proxy-stat"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat, [u'vrf_name'], name, value)


                        class Statistics_(Entity):
                            """
                            Proxy statistics
                            
                            .. attribute:: received_packets
                            
                            	Received packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: transmitted_packets
                            
                            	Transmitted packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dropped_packets
                            
                            	Dropped packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "ipv4-dhcpd-proxy-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                    ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                    ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                ])
                                self.received_packets = None
                                self.transmitted_packets = None
                                self.dropped_packets = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                class Binding(Entity):
                    """
                    DHCP proxy bindings
                    
                    .. attribute:: clients
                    
                    	DHCP proxy client bindings
                    	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients>`
                    
                    .. attribute:: summary
                    
                    	DHCP proxy binding summary
                    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Proxy.Binding, self).__init__()

                        self.yang_name = "binding"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("clients", ("clients", Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients)), ("summary", ("summary", Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary))])
                        self._leafs = OrderedDict()

                        self.clients = Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients()
                        self.clients.parent = self
                        self._children_name_map["clients"] = "clients"

                        self.summary = Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                        self._segment_path = lambda: "binding"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Binding, [], name, value)


                    class Clients(Entity):
                        """
                        DHCP proxy client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCP proxy binding
                        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients, self).__init__()

                            self.yang_name = "clients"
                            self.yang_parent_name = "binding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("client", ("client", Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients.Client))])
                            self._leafs = OrderedDict()

                            self.client = YList(self)
                            self._segment_path = lambda: "clients"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients, [], name, value)


                        class Client(Entity):
                            """
                            Single DHCP proxy binding
                            
                            .. attribute:: client_id  (key)
                            
                            	Client ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: client_id_xr
                            
                            	DHCP client identifier
                            	**type**\: str
                            
                            	**length:** 0..1275
                            
                            .. attribute:: mac_address
                            
                            	DHCP client MAC address
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	DHCP client/subscriber VRF name
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: server_vrf_name
                            
                            	DHCP server VRF name
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: ip_address
                            
                            	DHCP IP address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: client_gi_addr
                            
                            	DHCP client GIADDR
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: to_server_gi_addr
                            
                            	DHCP to server GIADDR
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: server_ip_address
                            
                            	DHCP server IP address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: reply_server_ip_address
                            
                            	DHCP reply server IP address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: lease_time
                            
                            	Lease time in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: remaining_lease_time
                            
                            	Remaining lease time in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: state
                            
                            	DHCP client state
                            	**type**\:  :py:class:`BagDhcpdProxyState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.BagDhcpdProxyState>`
                            
                            .. attribute:: interface_name
                            
                            	DHCP access interface to client
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: access_vrf_name
                            
                            	DHCP access interface VRF name
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: proxy_binding_outer_tag
                            
                            	DHCP VLAN outer VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_binding_inner_tag
                            
                            	DHCP VLAN inner VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: profile_name
                            
                            	DHCP profile name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            .. attribute:: is_nak_next_renew
                            
                            	Is true if DHCP next renew from client will be NAK'd
                            	**type**\: bool
                            
                            .. attribute:: subscriber_label
                            
                            	DHCP subscriber label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: old_subscriber_label
                            
                            	DHCP old subscriber label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: subscriber_interface_name
                            
                            	DHCP subscriber interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: rx_circuit_id
                            
                            	DHCP received circuit ID
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: tx_circuit_id
                            
                            	DHCP transmitted circuit ID
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: rx_remote_id
                            
                            	DHCP received Remote ID
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: tx_remote_id
                            
                            	DHCP transmitted Remote ID
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: rx_vsiso
                            
                            	DHCP received VSISO
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: tx_vsiso
                            
                            	DHCP transmitted VSISO
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: is_auth_received
                            
                            	Is true if authentication is on received option82
                            	**type**\: bool
                            
                            .. attribute:: is_mbl_subscriber
                            
                            	Is true if DHCP subscriber is Mobile
                            	**type**\: bool
                            
                            .. attribute:: param_request
                            
                            	DHCP parameter request option
                            	**type**\: str
                            
                            	**length:** 0..513
                            
                            .. attribute:: param_response
                            
                            	DHCP saved options
                            	**type**\: str
                            
                            	**length:** 0..2051
                            
                            .. attribute:: session_start_time
                            
                            	session start time
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: srg_state
                            
                            	DHCPV4 SRG state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: event_history
                            
                            	event history
                            	**type**\: list of int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients.Client, self).__init__()

                                self.yang_name = "client"
                                self.yang_parent_name = "clients"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['client_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('client_id', (YLeaf(YType.str, 'client-id'), ['str'])),
                                    ('client_id_xr', (YLeaf(YType.str, 'client-id-xr'), ['str'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ('server_vrf_name', (YLeaf(YType.str, 'server-vrf-name'), ['str'])),
                                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                    ('client_gi_addr', (YLeaf(YType.str, 'client-gi-addr'), ['str'])),
                                    ('to_server_gi_addr', (YLeaf(YType.str, 'to-server-gi-addr'), ['str'])),
                                    ('server_ip_address', (YLeaf(YType.str, 'server-ip-address'), ['str'])),
                                    ('reply_server_ip_address', (YLeaf(YType.str, 'reply-server-ip-address'), ['str'])),
                                    ('lease_time', (YLeaf(YType.uint32, 'lease-time'), ['int'])),
                                    ('remaining_lease_time', (YLeaf(YType.uint32, 'remaining-lease-time'), ['int'])),
                                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'BagDhcpdProxyState', '')])),
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('access_vrf_name', (YLeaf(YType.str, 'access-vrf-name'), ['str'])),
                                    ('proxy_binding_outer_tag', (YLeaf(YType.uint32, 'proxy-binding-outer-tag'), ['int'])),
                                    ('proxy_binding_inner_tag', (YLeaf(YType.uint32, 'proxy-binding-inner-tag'), ['int'])),
                                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                    ('is_nak_next_renew', (YLeaf(YType.boolean, 'is-nak-next-renew'), ['bool'])),
                                    ('subscriber_label', (YLeaf(YType.uint32, 'subscriber-label'), ['int'])),
                                    ('old_subscriber_label', (YLeaf(YType.uint32, 'old-subscriber-label'), ['int'])),
                                    ('subscriber_interface_name', (YLeaf(YType.str, 'subscriber-interface-name'), ['str'])),
                                    ('rx_circuit_id', (YLeaf(YType.str, 'rx-circuit-id'), ['str'])),
                                    ('tx_circuit_id', (YLeaf(YType.str, 'tx-circuit-id'), ['str'])),
                                    ('rx_remote_id', (YLeaf(YType.str, 'rx-remote-id'), ['str'])),
                                    ('tx_remote_id', (YLeaf(YType.str, 'tx-remote-id'), ['str'])),
                                    ('rx_vsiso', (YLeaf(YType.str, 'rx-vsiso'), ['str'])),
                                    ('tx_vsiso', (YLeaf(YType.str, 'tx-vsiso'), ['str'])),
                                    ('is_auth_received', (YLeaf(YType.boolean, 'is-auth-received'), ['bool'])),
                                    ('is_mbl_subscriber', (YLeaf(YType.boolean, 'is-mbl-subscriber'), ['bool'])),
                                    ('param_request', (YLeaf(YType.str, 'param-request'), ['str'])),
                                    ('param_response', (YLeaf(YType.str, 'param-response'), ['str'])),
                                    ('session_start_time', (YLeaf(YType.uint64, 'session-start-time'), ['int'])),
                                    ('srg_state', (YLeaf(YType.uint32, 'srg-state'), ['int'])),
                                    ('event_history', (YLeafList(YType.uint32, 'event-history'), ['int'])),
                                ])
                                self.client_id = None
                                self.client_id_xr = None
                                self.mac_address = None
                                self.vrf_name = None
                                self.server_vrf_name = None
                                self.ip_address = None
                                self.client_gi_addr = None
                                self.to_server_gi_addr = None
                                self.server_ip_address = None
                                self.reply_server_ip_address = None
                                self.lease_time = None
                                self.remaining_lease_time = None
                                self.state = None
                                self.interface_name = None
                                self.access_vrf_name = None
                                self.proxy_binding_outer_tag = None
                                self.proxy_binding_inner_tag = None
                                self.profile_name = None
                                self.is_nak_next_renew = None
                                self.subscriber_label = None
                                self.old_subscriber_label = None
                                self.subscriber_interface_name = None
                                self.rx_circuit_id = None
                                self.tx_circuit_id = None
                                self.rx_remote_id = None
                                self.tx_remote_id = None
                                self.rx_vsiso = None
                                self.tx_vsiso = None
                                self.is_auth_received = None
                                self.is_mbl_subscriber = None
                                self.param_request = None
                                self.param_response = None
                                self.session_start_time = None
                                self.srg_state = None
                                self.event_history = []
                                self._segment_path = lambda: "client" + "[client-id='" + str(self.client_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients.Client, ['client_id', u'client_id_xr', u'mac_address', u'vrf_name', u'server_vrf_name', u'ip_address', u'client_gi_addr', u'to_server_gi_addr', u'server_ip_address', u'reply_server_ip_address', u'lease_time', u'remaining_lease_time', u'state', u'interface_name', u'access_vrf_name', u'proxy_binding_outer_tag', u'proxy_binding_inner_tag', u'profile_name', u'is_nak_next_renew', u'subscriber_label', u'old_subscriber_label', u'subscriber_interface_name', u'rx_circuit_id', u'tx_circuit_id', u'rx_remote_id', u'tx_remote_id', u'rx_vsiso', u'tx_vsiso', u'is_auth_received', u'is_mbl_subscriber', u'param_request', u'param_response', u'session_start_time', u'srg_state', u'event_history'], name, value)


                    class Summary(Entity):
                        """
                        DHCP proxy binding summary
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: initializing_clients
                        
                        	Number of clients in init state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_init
                        
                        	Number of clients in Init DPM wait state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_request
                        
                        	Number of clients in Request DPM wait state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_daps_init
                        
                        	Number of clients in Init DAPS wait state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: selecting_clients
                        
                        	Number of clients in selecting state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: offer_sent_for_client
                        
                        	Number of clients in Offer sent state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: requesting_clients
                        
                        	Number of clients in requesting state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: request_waiting_for_dpm
                        
                        	Number of clients in Waiting for DPM with Request
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ack_waiting_for_dpm
                        
                        	Number of clients in Waiting for DPM with ACK
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bound_clients
                        
                        	Number of clients in bound state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: renewing_clients
                        
                        	Number of clients in renewing state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: informing_clients
                        
                        	Number of clients in informing state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reauthorizing_clients
                        
                        	Number of clients in reauth state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_disconnect
                        
                        	Number of clients in waiting for DPM disconnect state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_addr_change
                        
                        	Number of clients in Waiting for DPM after addr change
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: deleting_clients_d
                        
                        	Number of clients in deleting state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: disconnected_clients
                        
                        	Number of clients in disconnected state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: restarting_clients
                        
                        	Number of clients in restarting state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "binding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('clients', (YLeaf(YType.uint32, 'clients'), ['int'])),
                                ('initializing_clients', (YLeaf(YType.uint32, 'initializing-clients'), ['int'])),
                                ('waiting_for_dpm_init', (YLeaf(YType.uint32, 'waiting-for-dpm-init'), ['int'])),
                                ('waiting_for_dpm_request', (YLeaf(YType.uint32, 'waiting-for-dpm-request'), ['int'])),
                                ('waiting_for_daps_init', (YLeaf(YType.uint32, 'waiting-for-daps-init'), ['int'])),
                                ('selecting_clients', (YLeaf(YType.uint32, 'selecting-clients'), ['int'])),
                                ('offer_sent_for_client', (YLeaf(YType.uint32, 'offer-sent-for-client'), ['int'])),
                                ('requesting_clients', (YLeaf(YType.uint32, 'requesting-clients'), ['int'])),
                                ('request_waiting_for_dpm', (YLeaf(YType.uint32, 'request-waiting-for-dpm'), ['int'])),
                                ('ack_waiting_for_dpm', (YLeaf(YType.uint32, 'ack-waiting-for-dpm'), ['int'])),
                                ('bound_clients', (YLeaf(YType.uint32, 'bound-clients'), ['int'])),
                                ('renewing_clients', (YLeaf(YType.uint32, 'renewing-clients'), ['int'])),
                                ('informing_clients', (YLeaf(YType.uint32, 'informing-clients'), ['int'])),
                                ('reauthorizing_clients', (YLeaf(YType.uint32, 'reauthorizing-clients'), ['int'])),
                                ('waiting_for_dpm_disconnect', (YLeaf(YType.uint32, 'waiting-for-dpm-disconnect'), ['int'])),
                                ('waiting_for_dpm_addr_change', (YLeaf(YType.uint32, 'waiting-for-dpm-addr-change'), ['int'])),
                                ('deleting_clients_d', (YLeaf(YType.uint32, 'deleting-clients-d'), ['int'])),
                                ('disconnected_clients', (YLeaf(YType.uint32, 'disconnected-clients'), ['int'])),
                                ('restarting_clients', (YLeaf(YType.uint32, 'restarting-clients'), ['int'])),
                            ])
                            self.clients = None
                            self.initializing_clients = None
                            self.waiting_for_dpm_init = None
                            self.waiting_for_dpm_request = None
                            self.waiting_for_daps_init = None
                            self.selecting_clients = None
                            self.offer_sent_for_client = None
                            self.requesting_clients = None
                            self.request_waiting_for_dpm = None
                            self.ack_waiting_for_dpm = None
                            self.bound_clients = None
                            self.renewing_clients = None
                            self.informing_clients = None
                            self.reauthorizing_clients = None
                            self.waiting_for_dpm_disconnect = None
                            self.waiting_for_dpm_addr_change = None
                            self.deleting_clients_d = None
                            self.disconnected_clients = None
                            self.restarting_clients = None
                            self._segment_path = lambda: "summary"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary, [u'clients', u'initializing_clients', u'waiting_for_dpm_init', u'waiting_for_dpm_request', u'waiting_for_daps_init', u'selecting_clients', u'offer_sent_for_client', u'requesting_clients', u'request_waiting_for_dpm', u'ack_waiting_for_dpm', u'bound_clients', u'renewing_clients', u'informing_clients', u'reauthorizing_clients', u'waiting_for_dpm_disconnect', u'waiting_for_dpm_addr_change', u'deleting_clients_d', u'disconnected_clients', u'restarting_clients'], name, value)


            class Interfaces(Entity):
                """
                IPv4 DHCP proxy/server Interface
                
                .. attribute:: interface
                
                	IPv4 DHCP proxy/server interface info
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Ipv4Dhcpd.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    IPv4 DHCP proxy/server interface info
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: intf_ifhandle
                    
                    	Ifhandle of the interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\: str
                    
                    	**length:** 0..33
                    
                    .. attribute:: intf_mode
                    
                    	Mode of interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: intf_is_ambiguous
                    
                    	Is interface ambiguous
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: intf_profile_name
                    
                    	Name of profile attached to the interface
                    	**type**\: str
                    
                    	**length:** 0..65
                    
                    .. attribute:: intf_lease_limit_type
                    
                    	Lease limit type on interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: intf_lease_limit_count
                    
                    	Lease limit count on interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srg_role
                    
                    	DHCPv6 Interface SRG role
                    	**type**\:  :py:class:`BagDhcpdIntfSrgRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.BagDhcpdIntfSrgRole>`
                    
                    .. attribute:: mac_throttle
                    
                    	Mac Throttle Status
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('intf_ifhandle', (YLeaf(YType.uint32, 'intf-ifhandle'), ['int'])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('intf_mode', (YLeaf(YType.uint32, 'intf-mode'), ['int'])),
                            ('intf_is_ambiguous', (YLeaf(YType.uint32, 'intf-is-ambiguous'), ['int'])),
                            ('intf_profile_name', (YLeaf(YType.str, 'intf-profile-name'), ['str'])),
                            ('intf_lease_limit_type', (YLeaf(YType.uint32, 'intf-lease-limit-type'), ['int'])),
                            ('intf_lease_limit_count', (YLeaf(YType.uint32, 'intf-lease-limit-count'), ['int'])),
                            ('srg_role', (YLeaf(YType.enumeration, 'srg-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'BagDhcpdIntfSrgRole', '')])),
                            ('mac_throttle', (YLeaf(YType.boolean, 'mac-throttle'), ['bool'])),
                        ])
                        self.interface_name = None
                        self.intf_ifhandle = None
                        self.vrf_name = None
                        self.intf_mode = None
                        self.intf_is_ambiguous = None
                        self.intf_profile_name = None
                        self.intf_lease_limit_type = None
                        self.intf_lease_limit_count = None
                        self.srg_role = None
                        self.mac_throttle = None
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Interfaces.Interface, ['interface_name', u'intf_ifhandle', u'vrf_name', u'intf_mode', u'intf_is_ambiguous', u'intf_profile_name', u'intf_lease_limit_type', u'intf_lease_limit_count', u'srg_role', u'mac_throttle'], name, value)


            class Base(Entity):
                """
                IPv4 DHCP base operational data
                
                .. attribute:: statistics
                
                	DHCP base statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Statistics>`
                
                .. attribute:: issu_status
                
                	IPv4 DHCP ISSU status
                	**type**\:  :py:class:`IssuStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.IssuStatus>`
                
                .. attribute:: vrfs
                
                	DHCP base list of VRF names
                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs>`
                
                .. attribute:: profiles
                
                	IPv4 DHCP Base profile
                	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles>`
                
                .. attribute:: database
                
                	IPv4 DHCP database
                	**type**\:  :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Database>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Nodes.Node.Base, self).__init__()

                    self.yang_name = "base"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statistics", ("statistics", Ipv4Dhcpd.Nodes.Node.Base.Statistics)), ("issu-status", ("issu_status", Ipv4Dhcpd.Nodes.Node.Base.IssuStatus)), ("vrfs", ("vrfs", Ipv4Dhcpd.Nodes.Node.Base.Vrfs)), ("profiles", ("profiles", Ipv4Dhcpd.Nodes.Node.Base.Profiles)), ("database", ("database", Ipv4Dhcpd.Nodes.Node.Base.Database))])
                    self._leafs = OrderedDict()

                    self.statistics = Ipv4Dhcpd.Nodes.Node.Base.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"

                    self.issu_status = Ipv4Dhcpd.Nodes.Node.Base.IssuStatus()
                    self.issu_status.parent = self
                    self._children_name_map["issu_status"] = "issu-status"

                    self.vrfs = Ipv4Dhcpd.Nodes.Node.Base.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"

                    self.profiles = Ipv4Dhcpd.Nodes.Node.Base.Profiles()
                    self.profiles.parent = self
                    self._children_name_map["profiles"] = "profiles"

                    self.database = Ipv4Dhcpd.Nodes.Node.Base.Database()
                    self.database.parent = self
                    self._children_name_map["database"] = "database"
                    self._segment_path = lambda: "base"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base, [], name, value)


                class Statistics(Entity):
                    """
                    DHCP base statistics
                    
                    .. attribute:: ipv4_dhcpd_proxy_stat
                    
                    	ipv4 dhcpd proxy stat
                    	**type**\: list of  		 :py:class:`Ipv4DhcpdProxyStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Base.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv4-dhcpd-proxy-stat", ("ipv4_dhcpd_proxy_stat", Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat))])
                        self._leafs = OrderedDict()

                        self.ipv4_dhcpd_proxy_stat = YList(self)
                        self._segment_path = lambda: "statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Statistics, [], name, value)


                    class Ipv4DhcpdProxyStat(Entity):
                        """
                        ipv4 dhcpd proxy stat
                        
                        .. attribute:: statistics
                        
                        	Proxy statistics
                        	**type**\:  :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCP L3 VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat, self).__init__()

                            self.yang_name = "ipv4-dhcpd-proxy-stat"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("statistics", ("statistics", Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_))])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None

                            self.statistics = Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._segment_path = lambda: "ipv4-dhcpd-proxy-stat"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat, [u'vrf_name'], name, value)


                        class Statistics_(Entity):
                            """
                            Proxy statistics
                            
                            .. attribute:: received_packets
                            
                            	Received packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: transmitted_packets
                            
                            	Transmitted packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dropped_packets
                            
                            	Dropped packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "ipv4-dhcpd-proxy-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                    ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                    ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                ])
                                self.received_packets = None
                                self.transmitted_packets = None
                                self.dropped_packets = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                class IssuStatus(Entity):
                    """
                    IPv4 DHCP ISSU status
                    
                    .. attribute:: issu_sync_complete_time
                    
                    	Timestamp for the ISSU sync complete in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: issu_sync_start_time
                    
                    	Timestamp for the ISSU sync start in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC, January 1, 1970
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: issu_ready_time
                    
                    	Timestamp for the ISSU ready declaration in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: big_bang_time
                    
                    	Timestamp for the Big Bang notification time in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: primary_role_time
                    
                    	Timestamp for the change to Primary role notification time in nanoseconds since Epoch, i .e. since 00\:00\:00 UTC, January 1, 1970
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: role
                    
                    	The current role of the DHCP process
                    	**type**\:  :py:class:`DhcpIssuRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpIssuRole>`
                    
                    .. attribute:: phase
                    
                    	The current ISSU phase of the DHCP process
                    	**type**\:  :py:class:`DhcpIssuPhase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpIssuPhase>`
                    
                    .. attribute:: version
                    
                    	The current version of the DHCP process in the context of an ISSU
                    	**type**\:  :py:class:`DhcpIssuVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.DhcpIssuVersion>`
                    
                    .. attribute:: issu_ready_issu_mgr_connection
                    
                    	Whether or not DHCP is currently connected to ISSU Manager during the ISSU Load Phase
                    	**type**\: bool
                    
                    .. attribute:: issu_ready_entries_replicate
                    
                    	Whether or not DHCP has received all replicated entries during the ISSU Load Phase
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Base.IssuStatus, self).__init__()

                        self.yang_name = "issu-status"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('issu_sync_complete_time', (YLeaf(YType.uint64, 'issu-sync-complete-time'), ['int'])),
                            ('issu_sync_start_time', (YLeaf(YType.uint64, 'issu-sync-start-time'), ['int'])),
                            ('issu_ready_time', (YLeaf(YType.uint64, 'issu-ready-time'), ['int'])),
                            ('big_bang_time', (YLeaf(YType.uint64, 'big-bang-time'), ['int'])),
                            ('primary_role_time', (YLeaf(YType.uint64, 'primary-role-time'), ['int'])),
                            ('role', (YLeaf(YType.enumeration, 'role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpIssuRole', '')])),
                            ('phase', (YLeaf(YType.enumeration, 'phase'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpIssuPhase', '')])),
                            ('version', (YLeaf(YType.enumeration, 'version'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpIssuVersion', '')])),
                            ('issu_ready_issu_mgr_connection', (YLeaf(YType.boolean, 'issu-ready-issu-mgr-connection'), ['bool'])),
                            ('issu_ready_entries_replicate', (YLeaf(YType.boolean, 'issu-ready-entries-replicate'), ['bool'])),
                        ])
                        self.issu_sync_complete_time = None
                        self.issu_sync_start_time = None
                        self.issu_ready_time = None
                        self.big_bang_time = None
                        self.primary_role_time = None
                        self.role = None
                        self.phase = None
                        self.version = None
                        self.issu_ready_issu_mgr_connection = None
                        self.issu_ready_entries_replicate = None
                        self._segment_path = lambda: "issu-status"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.IssuStatus, [u'issu_sync_complete_time', u'issu_sync_start_time', u'issu_ready_time', u'big_bang_time', u'primary_role_time', u'role', u'phase', u'version', u'issu_ready_issu_mgr_connection', u'issu_ready_entries_replicate'], name, value)


                class Vrfs(Entity):
                    """
                    DHCP base list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv4 DHCP base VRF name
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vrf", ("vrf", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf))])
                        self._leafs = OrderedDict()

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs, [], name, value)


                    class Vrf(Entity):
                        """
                        IPv4 DHCP base VRF name
                        
                        .. attribute:: vrf_name  (key)
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv4 DHCP base statistics
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_classes = OrderedDict([("statistics", ("statistics", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics))])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None

                            self.statistics = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf, ['vrf_name'], name, value)


                        class Statistics(Entity):
                            """
                            IPv4 DHCP base statistics
                            
                            .. attribute:: discover
                            
                            	DHCP discover packets
                            	**type**\:  :py:class:`Discover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover>`
                            
                            .. attribute:: offer
                            
                            	DHCP offer packets
                            	**type**\:  :py:class:`Offer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer>`
                            
                            .. attribute:: request
                            
                            	DHCP request packets
                            	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: decline
                            
                            	DHCP decline packets
                            	**type**\:  :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: ack
                            
                            	DHCP ack packets
                            	**type**\:  :py:class:`Ack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack>`
                            
                            .. attribute:: nak
                            
                            	DHCP nak packets
                            	**type**\:  :py:class:`Nak <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak>`
                            
                            .. attribute:: release
                            
                            	DHCP release packets
                            	**type**\:  :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: inform
                            
                            	DHCP inform packets
                            	**type**\:  :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: lease_query
                            
                            	DHCP lease query packets
                            	**type**\:  :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_not_assigned
                            
                            	DHCP lease not assigned
                            	**type**\:  :py:class:`LeaseNotAssigned <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned>`
                            
                            .. attribute:: lease_unknown
                            
                            	DHCP lease unknown
                            	**type**\:  :py:class:`LeaseUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown>`
                            
                            .. attribute:: lease_active
                            
                            	DHCP lease active
                            	**type**\:  :py:class:`LeaseActive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive>`
                            
                            .. attribute:: bootp_request
                            
                            	DHCP BOOTP request
                            	**type**\:  :py:class:`BootpRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest>`
                            
                            .. attribute:: bootp_reply
                            
                            	DHCP BOOTP reply
                            	**type**\:  :py:class:`BootpReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("discover", ("discover", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover)), ("offer", ("offer", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer)), ("request", ("request", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request)), ("decline", ("decline", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline)), ("ack", ("ack", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack)), ("nak", ("nak", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak)), ("release", ("release", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release)), ("inform", ("inform", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform)), ("lease-query", ("lease_query", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery)), ("lease-not-assigned", ("lease_not_assigned", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned)), ("lease-unknown", ("lease_unknown", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown)), ("lease-active", ("lease_active", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive)), ("bootp-request", ("bootp_request", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest)), ("bootp-reply", ("bootp_reply", Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply))])
                                self._leafs = OrderedDict()

                                self.discover = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover()
                                self.discover.parent = self
                                self._children_name_map["discover"] = "discover"

                                self.offer = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer()
                                self.offer.parent = self
                                self._children_name_map["offer"] = "offer"

                                self.request = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self._children_name_map["request"] = "request"

                                self.decline = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self._children_name_map["decline"] = "decline"

                                self.ack = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack()
                                self.ack.parent = self
                                self._children_name_map["ack"] = "ack"

                                self.nak = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak()
                                self.nak.parent = self
                                self._children_name_map["nak"] = "nak"

                                self.release = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self._children_name_map["release"] = "release"

                                self.inform = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self._children_name_map["inform"] = "inform"

                                self.lease_query = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self._children_name_map["lease_query"] = "lease-query"

                                self.lease_not_assigned = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned()
                                self.lease_not_assigned.parent = self
                                self._children_name_map["lease_not_assigned"] = "lease-not-assigned"

                                self.lease_unknown = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown()
                                self.lease_unknown.parent = self
                                self._children_name_map["lease_unknown"] = "lease-unknown"

                                self.lease_active = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive()
                                self.lease_active.parent = self
                                self._children_name_map["lease_active"] = "lease-active"

                                self.bootp_request = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest()
                                self.bootp_request.parent = self
                                self._children_name_map["bootp_request"] = "bootp-request"

                                self.bootp_reply = Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply()
                                self.bootp_reply.parent = self
                                self._children_name_map["bootp_reply"] = "bootp-reply"
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics, [], name, value)


                            class Discover(Entity):
                                """
                                DHCP discover packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover, self).__init__()

                                    self.yang_name = "discover"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "discover"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Offer(Entity):
                                """
                                DHCP offer packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer, self).__init__()

                                    self.yang_name = "offer"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "offer"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Request(Entity):
                                """
                                DHCP request packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request, self).__init__()

                                    self.yang_name = "request"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "request"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Decline(Entity):
                                """
                                DHCP decline packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline, self).__init__()

                                    self.yang_name = "decline"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "decline"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Ack(Entity):
                                """
                                DHCP ack packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack, self).__init__()

                                    self.yang_name = "ack"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "ack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Nak(Entity):
                                """
                                DHCP nak packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak, self).__init__()

                                    self.yang_name = "nak"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "nak"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Release(Entity):
                                """
                                DHCP release packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release, self).__init__()

                                    self.yang_name = "release"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "release"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Inform(Entity):
                                """
                                DHCP inform packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform, self).__init__()

                                    self.yang_name = "inform"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "inform"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseQuery(Entity):
                                """
                                DHCP lease query packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery, self).__init__()

                                    self.yang_name = "lease-query"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseNotAssigned(Entity):
                                """
                                DHCP lease not assigned
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned, self).__init__()

                                    self.yang_name = "lease-not-assigned"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-not-assigned"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseUnknown(Entity):
                                """
                                DHCP lease unknown
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown, self).__init__()

                                    self.yang_name = "lease-unknown"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-unknown"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseActive(Entity):
                                """
                                DHCP lease active
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive, self).__init__()

                                    self.yang_name = "lease-active"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-active"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class BootpRequest(Entity):
                                """
                                DHCP BOOTP request
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest, self).__init__()

                                    self.yang_name = "bootp-request"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "bootp-request"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class BootpReply(Entity):
                                """
                                DHCP BOOTP reply
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply, self).__init__()

                                    self.yang_name = "bootp-reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "bootp-reply"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                class Profiles(Entity):
                    """
                    IPv4 DHCP Base profile
                    
                    .. attribute:: profile
                    
                    	IPv4 DHCP base profile
                    	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Base.Profiles, self).__init__()

                        self.yang_name = "profiles"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("profile", ("profile", Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile))])
                        self._leafs = OrderedDict()

                        self.profile = YList(self)
                        self._segment_path = lambda: "profiles"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Profiles, [], name, value)


                    class Profile(Entity):
                        """
                        IPv4 DHCP base profile
                        
                        .. attribute:: profile_name  (key)
                        
                        	Profile name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: interface_references
                        
                        	Interface references
                        	**type**\:  :py:class:`InterfaceReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences>`
                        
                        .. attribute:: child_profile_info
                        
                        	child profile info
                        	**type**\:  :py:class:`ChildProfileInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo>`
                        
                        .. attribute:: base_default_profile_name
                        
                        	Base Default Profile name
                        	**type**\: str
                        
                        	**length:** 0..65
                        
                        .. attribute:: default_profile_mode
                        
                        	Default Profile mode
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_authenticate
                        
                        	Relay authenticate
                        	**type**\:  :py:class:`RelayInfoAuthenticate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.RelayInfoAuthenticate>`
                        
                        .. attribute:: remote_id
                        
                        	DHCP configured Remote ID
                        	**type**\: str
                        
                        	**length:** 0..768
                        
                        .. attribute:: child_profile_count
                        
                        	Child profile count
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: intf_ref_count
                        
                        	Interface reference count
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile, self).__init__()

                            self.yang_name = "profile"
                            self.yang_parent_name = "profiles"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['profile_name']
                            self._child_classes = OrderedDict([("interface-references", ("interface_references", Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences)), ("child-profile-info", ("child_profile_info", Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo))])
                            self._leafs = OrderedDict([
                                ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                ('base_default_profile_name', (YLeaf(YType.str, 'base-default-profile-name'), ['str'])),
                                ('default_profile_mode', (YLeaf(YType.uint8, 'default-profile-mode'), ['int'])),
                                ('relay_authenticate', (YLeaf(YType.enumeration, 'relay-authenticate'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'RelayInfoAuthenticate', '')])),
                                ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                ('child_profile_count', (YLeaf(YType.uint8, 'child-profile-count'), ['int'])),
                                ('intf_ref_count', (YLeaf(YType.uint8, 'intf-ref-count'), ['int'])),
                            ])
                            self.profile_name = None
                            self.base_default_profile_name = None
                            self.default_profile_mode = None
                            self.relay_authenticate = None
                            self.remote_id = None
                            self.child_profile_count = None
                            self.intf_ref_count = None

                            self.interface_references = Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences()
                            self.interface_references.parent = self
                            self._children_name_map["interface_references"] = "interface-references"

                            self.child_profile_info = Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo()
                            self.child_profile_info.parent = self
                            self._children_name_map["child_profile_info"] = "child-profile-info"
                            self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile, ['profile_name', u'base_default_profile_name', u'default_profile_mode', u'relay_authenticate', u'remote_id', u'child_profile_count', u'intf_ref_count'], name, value)


                        class InterfaceReferences(Entity):
                            """
                            Interface references
                            
                            .. attribute:: ipv4_dhcpd_base_interface_reference
                            
                            	ipv4 dhcpd base interface reference
                            	**type**\: list of  		 :py:class:`Ipv4DhcpdBaseInterfaceReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences.Ipv4DhcpdBaseInterfaceReference>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences, self).__init__()

                                self.yang_name = "interface-references"
                                self.yang_parent_name = "profile"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ipv4-dhcpd-base-interface-reference", ("ipv4_dhcpd_base_interface_reference", Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences.Ipv4DhcpdBaseInterfaceReference))])
                                self._leafs = OrderedDict()

                                self.ipv4_dhcpd_base_interface_reference = YList(self)
                                self._segment_path = lambda: "interface-references"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences, [], name, value)


                            class Ipv4DhcpdBaseInterfaceReference(Entity):
                                """
                                ipv4 dhcpd base interface reference
                                
                                .. attribute:: base_reference_interface_name
                                
                                	Interface name
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences.Ipv4DhcpdBaseInterfaceReference, self).__init__()

                                    self.yang_name = "ipv4-dhcpd-base-interface-reference"
                                    self.yang_parent_name = "interface-references"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('base_reference_interface_name', (YLeaf(YType.str, 'base-reference-interface-name'), ['str'])),
                                    ])
                                    self.base_reference_interface_name = None
                                    self._segment_path = lambda: "ipv4-dhcpd-base-interface-reference"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences.Ipv4DhcpdBaseInterfaceReference, [u'base_reference_interface_name'], name, value)


                        class ChildProfileInfo(Entity):
                            """
                            child profile info
                            
                            .. attribute:: ipv4_dhcpd_base_child_profile_info
                            
                            	ipv4 dhcpd base child profile info
                            	**type**\: list of  		 :py:class:`Ipv4DhcpdBaseChildProfileInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo.Ipv4DhcpdBaseChildProfileInfo>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo, self).__init__()

                                self.yang_name = "child-profile-info"
                                self.yang_parent_name = "profile"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ipv4-dhcpd-base-child-profile-info", ("ipv4_dhcpd_base_child_profile_info", Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo.Ipv4DhcpdBaseChildProfileInfo))])
                                self._leafs = OrderedDict()

                                self.ipv4_dhcpd_base_child_profile_info = YList(self)
                                self._segment_path = lambda: "child-profile-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo, [], name, value)


                            class Ipv4DhcpdBaseChildProfileInfo(Entity):
                                """
                                ipv4 dhcpd base child profile info
                                
                                .. attribute:: base_child_profile_name
                                
                                	Base Child Profile name
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                .. attribute:: mode
                                
                                	Profile mode
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: matched_option_code
                                
                                	Matched option code
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: matched_option_len
                                
                                	Matched option len
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: option_data
                                
                                	Matched option data
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo.Ipv4DhcpdBaseChildProfileInfo, self).__init__()

                                    self.yang_name = "ipv4-dhcpd-base-child-profile-info"
                                    self.yang_parent_name = "child-profile-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('base_child_profile_name', (YLeaf(YType.str, 'base-child-profile-name'), ['str'])),
                                        ('mode', (YLeaf(YType.uint8, 'mode'), ['int'])),
                                        ('matched_option_code', (YLeaf(YType.uint8, 'matched-option-code'), ['int'])),
                                        ('matched_option_len', (YLeaf(YType.uint8, 'matched-option-len'), ['int'])),
                                        ('option_data', (YLeaf(YType.str, 'option-data'), ['str'])),
                                    ])
                                    self.base_child_profile_name = None
                                    self.mode = None
                                    self.matched_option_code = None
                                    self.matched_option_len = None
                                    self.option_data = None
                                    self._segment_path = lambda: "ipv4-dhcpd-base-child-profile-info"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo.Ipv4DhcpdBaseChildProfileInfo, [u'base_child_profile_name', u'mode', u'matched_option_code', u'matched_option_len', u'option_data'], name, value)


                class Database(Entity):
                    """
                    IPv4 DHCP database
                    
                    .. attribute:: configured
                    
                    	Database feature configured
                    	**type**\: bool
                    
                    .. attribute:: version
                    
                    	Current file version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: full_file_write_interval
                    
                    	Full file write interval in minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    .. attribute:: last_full_write_file_name
                    
                    	Last full write file name
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: last_full_write_time
                    
                    	Last full write time since epoch
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: full_file_write_count
                    
                    	Full file write count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: failed_full_file_write_count
                    
                    	Failed full file write count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: full_file_record_count
                    
                    	Full file record count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_full_file_write_error_timestamp
                    
                    	Last full file write error timestamp since epoch
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incremental_file_write_interval
                    
                    	Incremental file write interval in minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    .. attribute:: last_incremental_write_file_name
                    
                    	Last incremental write file name
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: last_incremental_write_time
                    
                    	Last incremental write time since epoch
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incremental_file_write_count
                    
                    	Incremental file write count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: failed_incremental_file_write_count
                    
                    	Failed incremental file write count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: incremental_file_record_count
                    
                    	Incremental file record count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_incremental_file_write_error_timestamp
                    
                    	Last incremental file write error timestamp since epoch
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Base.Database, self).__init__()

                        self.yang_name = "database"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('configured', (YLeaf(YType.boolean, 'configured'), ['bool'])),
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                            ('full_file_write_interval', (YLeaf(YType.uint32, 'full-file-write-interval'), ['int'])),
                            ('last_full_write_file_name', (YLeaf(YType.str, 'last-full-write-file-name'), ['str'])),
                            ('last_full_write_time', (YLeaf(YType.uint32, 'last-full-write-time'), ['int'])),
                            ('full_file_write_count', (YLeaf(YType.uint32, 'full-file-write-count'), ['int'])),
                            ('failed_full_file_write_count', (YLeaf(YType.uint32, 'failed-full-file-write-count'), ['int'])),
                            ('full_file_record_count', (YLeaf(YType.uint32, 'full-file-record-count'), ['int'])),
                            ('last_full_file_write_error_timestamp', (YLeaf(YType.uint32, 'last-full-file-write-error-timestamp'), ['int'])),
                            ('incremental_file_write_interval', (YLeaf(YType.uint32, 'incremental-file-write-interval'), ['int'])),
                            ('last_incremental_write_file_name', (YLeaf(YType.str, 'last-incremental-write-file-name'), ['str'])),
                            ('last_incremental_write_time', (YLeaf(YType.uint32, 'last-incremental-write-time'), ['int'])),
                            ('incremental_file_write_count', (YLeaf(YType.uint32, 'incremental-file-write-count'), ['int'])),
                            ('failed_incremental_file_write_count', (YLeaf(YType.uint32, 'failed-incremental-file-write-count'), ['int'])),
                            ('incremental_file_record_count', (YLeaf(YType.uint32, 'incremental-file-record-count'), ['int'])),
                            ('last_incremental_file_write_error_timestamp', (YLeaf(YType.uint32, 'last-incremental-file-write-error-timestamp'), ['int'])),
                        ])
                        self.configured = None
                        self.version = None
                        self.full_file_write_interval = None
                        self.last_full_write_file_name = None
                        self.last_full_write_time = None
                        self.full_file_write_count = None
                        self.failed_full_file_write_count = None
                        self.full_file_record_count = None
                        self.last_full_file_write_error_timestamp = None
                        self.incremental_file_write_interval = None
                        self.last_incremental_write_file_name = None
                        self.last_incremental_write_time = None
                        self.incremental_file_write_count = None
                        self.failed_incremental_file_write_count = None
                        self.incremental_file_record_count = None
                        self.last_incremental_file_write_error_timestamp = None
                        self._segment_path = lambda: "database"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Base.Database, [u'configured', u'version', u'full_file_write_interval', u'last_full_write_file_name', u'last_full_write_time', u'full_file_write_count', u'failed_full_file_write_count', u'full_file_record_count', u'last_full_file_write_error_timestamp', u'incremental_file_write_interval', u'last_incremental_write_file_name', u'last_incremental_write_time', u'incremental_file_write_count', u'failed_incremental_file_write_count', u'incremental_file_record_count', u'last_incremental_file_write_error_timestamp'], name, value)


            class Server(Entity):
                """
                IPv4 DHCP Server operational data
                
                .. attribute:: profiles
                
                	IPv4 DHCP Server profile
                	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Profiles>`
                
                .. attribute:: statistics
                
                	DHCP Server statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Statistics>`
                
                .. attribute:: binding
                
                	DHCP server bindings
                	**type**\:  :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Binding>`
                
                .. attribute:: statistics_info
                
                	DHCP proxy stats info
                	**type**\:  :py:class:`StatisticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo>`
                
                .. attribute:: vrfs
                
                	DHCP Server list of VRF names
                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Nodes.Node.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("profiles", ("profiles", Ipv4Dhcpd.Nodes.Node.Server.Profiles)), ("statistics", ("statistics", Ipv4Dhcpd.Nodes.Node.Server.Statistics)), ("binding", ("binding", Ipv4Dhcpd.Nodes.Node.Server.Binding)), ("statistics-info", ("statistics_info", Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo)), ("vrfs", ("vrfs", Ipv4Dhcpd.Nodes.Node.Server.Vrfs))])
                    self._leafs = OrderedDict()

                    self.profiles = Ipv4Dhcpd.Nodes.Node.Server.Profiles()
                    self.profiles.parent = self
                    self._children_name_map["profiles"] = "profiles"

                    self.statistics = Ipv4Dhcpd.Nodes.Node.Server.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"

                    self.binding = Ipv4Dhcpd.Nodes.Node.Server.Binding()
                    self.binding.parent = self
                    self._children_name_map["binding"] = "binding"

                    self.statistics_info = Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo()
                    self.statistics_info.parent = self
                    self._children_name_map["statistics_info"] = "statistics-info"

                    self.vrfs = Ipv4Dhcpd.Nodes.Node.Server.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                    self._segment_path = lambda: "server"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server, [], name, value)


                class Profiles(Entity):
                    """
                    IPv4 DHCP Server profile
                    
                    .. attribute:: profile
                    
                    	IPv4 DHCP server profile
                    	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Server.Profiles, self).__init__()

                        self.yang_name = "profiles"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("profile", ("profile", Ipv4Dhcpd.Nodes.Node.Server.Profiles.Profile))])
                        self._leafs = OrderedDict()

                        self.profile = YList(self)
                        self._segment_path = lambda: "profiles"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Profiles, [], name, value)


                    class Profile(Entity):
                        """
                        IPv4 DHCP server profile
                        
                        .. attribute:: server_profile_name  (key)
                        
                        	Profile name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: server_profile_name_xr
                        
                        	Profile Name
                        	**type**\: str
                        
                        	**length:** 0..65
                        
                        .. attribute:: secure_arp
                        
                        	Secure ARP
                        	**type**\: bool
                        
                        .. attribute:: requested_address_check
                        
                        	Requested Address Check
                        	**type**\: bool
                        
                        .. attribute:: server_id_check
                        
                        	Server ID Check
                        	**type**\: bool
                        
                        .. attribute:: duplicate_mac_address_check
                        
                        	Duplicate MAC Address Check
                        	**type**\: bool
                        
                        .. attribute:: duplicate_ip_address_check
                        
                        	Duplicate IP Address Check
                        	**type**\: bool
                        
                        .. attribute:: is_move_allowed
                        
                        	Is true if dhcp subscriber is allowed to move
                        	**type**\: bool
                        
                        .. attribute:: bcast_policy
                        
                        	Bcast Policy
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: giaddr_policy
                        
                        	Giaddr Policy
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: subnet_mask
                        
                        	Subnet Mask
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: server_pool_name
                        
                        	Pool Name
                        	**type**\: str
                        
                        	**length:** 0..65
                        
                        .. attribute:: server_profile_lease
                        
                        	Lease
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: server_profile_netbios_node_type
                        
                        	Server netbios node type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: server_bootfile_name
                        
                        	Server Bootfile name
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        .. attribute:: server_domain_name
                        
                        	Server Domain name
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        .. attribute:: server_profileiedge_check
                        
                        	Server iEdge Check
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: server_profile_server_dns_count
                        
                        	Server DNS Count
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: server_profiledefault_router_count
                        
                        	Server default count 
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: server_profile_netbios_name_svr_count
                        
                        	Server netbios svr count 
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: server_profile_time_svr_count
                        
                        	Server time svr count 
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: lease_limit_type
                        
                        	Lease Limit Type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: lease_limit_count
                        
                        	Lease Limit Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: server_profile_dns
                        
                        	Server DNS addresses
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: server_profile_default_router
                        
                        	Server default addresses
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: server_profile_netbious_name_server
                        
                        	Server netbios addresses
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: server_profile_time_server
                        
                        	Server Time addresses
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Server.Profiles.Profile, self).__init__()

                            self.yang_name = "profile"
                            self.yang_parent_name = "profiles"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['server_profile_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('server_profile_name', (YLeaf(YType.str, 'server-profile-name'), ['str'])),
                                ('server_profile_name_xr', (YLeaf(YType.str, 'server-profile-name-xr'), ['str'])),
                                ('secure_arp', (YLeaf(YType.boolean, 'secure-arp'), ['bool'])),
                                ('requested_address_check', (YLeaf(YType.boolean, 'requested-address-check'), ['bool'])),
                                ('server_id_check', (YLeaf(YType.boolean, 'server-id-check'), ['bool'])),
                                ('duplicate_mac_address_check', (YLeaf(YType.boolean, 'duplicate-mac-address-check'), ['bool'])),
                                ('duplicate_ip_address_check', (YLeaf(YType.boolean, 'duplicate-ip-address-check'), ['bool'])),
                                ('is_move_allowed', (YLeaf(YType.boolean, 'is-move-allowed'), ['bool'])),
                                ('bcast_policy', (YLeaf(YType.uint8, 'bcast-policy'), ['int'])),
                                ('giaddr_policy', (YLeaf(YType.uint8, 'giaddr-policy'), ['int'])),
                                ('subnet_mask', (YLeaf(YType.str, 'subnet-mask'), ['str'])),
                                ('server_pool_name', (YLeaf(YType.str, 'server-pool-name'), ['str'])),
                                ('server_profile_lease', (YLeaf(YType.uint32, 'server-profile-lease'), ['int'])),
                                ('server_profile_netbios_node_type', (YLeaf(YType.uint8, 'server-profile-netbios-node-type'), ['int'])),
                                ('server_bootfile_name', (YLeaf(YType.str, 'server-bootfile-name'), ['str'])),
                                ('server_domain_name', (YLeaf(YType.str, 'server-domain-name'), ['str'])),
                                ('server_profileiedge_check', (YLeaf(YType.uint8, 'server-profileiedge-check'), ['int'])),
                                ('server_profile_server_dns_count', (YLeaf(YType.uint8, 'server-profile-server-dns-count'), ['int'])),
                                ('server_profiledefault_router_count', (YLeaf(YType.uint8, 'server-profiledefault-router-count'), ['int'])),
                                ('server_profile_netbios_name_svr_count', (YLeaf(YType.uint8, 'server-profile-netbios-name-svr-count'), ['int'])),
                                ('server_profile_time_svr_count', (YLeaf(YType.uint8, 'server-profile-time-svr-count'), ['int'])),
                                ('lease_limit_type', (YLeaf(YType.uint8, 'lease-limit-type'), ['int'])),
                                ('lease_limit_count', (YLeaf(YType.uint32, 'lease-limit-count'), ['int'])),
                                ('server_profile_dns', (YLeafList(YType.str, 'server-profile-dns'), ['str'])),
                                ('server_profile_default_router', (YLeafList(YType.str, 'server-profile-default-router'), ['str'])),
                                ('server_profile_netbious_name_server', (YLeafList(YType.str, 'server-profile-netbious-name-server'), ['str'])),
                                ('server_profile_time_server', (YLeafList(YType.str, 'server-profile-time-server'), ['str'])),
                            ])
                            self.server_profile_name = None
                            self.server_profile_name_xr = None
                            self.secure_arp = None
                            self.requested_address_check = None
                            self.server_id_check = None
                            self.duplicate_mac_address_check = None
                            self.duplicate_ip_address_check = None
                            self.is_move_allowed = None
                            self.bcast_policy = None
                            self.giaddr_policy = None
                            self.subnet_mask = None
                            self.server_pool_name = None
                            self.server_profile_lease = None
                            self.server_profile_netbios_node_type = None
                            self.server_bootfile_name = None
                            self.server_domain_name = None
                            self.server_profileiedge_check = None
                            self.server_profile_server_dns_count = None
                            self.server_profiledefault_router_count = None
                            self.server_profile_netbios_name_svr_count = None
                            self.server_profile_time_svr_count = None
                            self.lease_limit_type = None
                            self.lease_limit_count = None
                            self.server_profile_dns = []
                            self.server_profile_default_router = []
                            self.server_profile_netbious_name_server = []
                            self.server_profile_time_server = []
                            self._segment_path = lambda: "profile" + "[server-profile-name='" + str(self.server_profile_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Profiles.Profile, ['server_profile_name', u'server_profile_name_xr', u'secure_arp', u'requested_address_check', u'server_id_check', u'duplicate_mac_address_check', u'duplicate_ip_address_check', u'is_move_allowed', u'bcast_policy', u'giaddr_policy', u'subnet_mask', u'server_pool_name', u'server_profile_lease', u'server_profile_netbios_node_type', u'server_bootfile_name', u'server_domain_name', u'server_profileiedge_check', u'server_profile_server_dns_count', u'server_profiledefault_router_count', u'server_profile_netbios_name_svr_count', u'server_profile_time_svr_count', u'lease_limit_type', u'lease_limit_count', u'server_profile_dns', u'server_profile_default_router', u'server_profile_netbious_name_server', u'server_profile_time_server'], name, value)


                class Statistics(Entity):
                    """
                    DHCP Server statistics
                    
                    .. attribute:: ipv4_dhcpd_proxy_stat
                    
                    	ipv4 dhcpd proxy stat
                    	**type**\: list of  		 :py:class:`Ipv4DhcpdProxyStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Server.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv4-dhcpd-proxy-stat", ("ipv4_dhcpd_proxy_stat", Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat))])
                        self._leafs = OrderedDict()

                        self.ipv4_dhcpd_proxy_stat = YList(self)
                        self._segment_path = lambda: "statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Statistics, [], name, value)


                    class Ipv4DhcpdProxyStat(Entity):
                        """
                        ipv4 dhcpd proxy stat
                        
                        .. attribute:: statistics
                        
                        	Proxy statistics
                        	**type**\:  :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCP L3 VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat, self).__init__()

                            self.yang_name = "ipv4-dhcpd-proxy-stat"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("statistics", ("statistics", Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_))])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None

                            self.statistics = Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._segment_path = lambda: "ipv4-dhcpd-proxy-stat"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat, [u'vrf_name'], name, value)


                        class Statistics_(Entity):
                            """
                            Proxy statistics
                            
                            .. attribute:: received_packets
                            
                            	Received packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: transmitted_packets
                            
                            	Transmitted packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dropped_packets
                            
                            	Dropped packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "ipv4-dhcpd-proxy-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                    ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                    ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                ])
                                self.received_packets = None
                                self.transmitted_packets = None
                                self.dropped_packets = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                class Binding(Entity):
                    """
                    DHCP server bindings
                    
                    .. attribute:: summary
                    
                    	DHCP server binding summary
                    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary>`
                    
                    .. attribute:: clients
                    
                    	DHCP server client bindings
                    	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Server.Binding, self).__init__()

                        self.yang_name = "binding"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("summary", ("summary", Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary)), ("clients", ("clients", Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients))])
                        self._leafs = OrderedDict()

                        self.summary = Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"

                        self.clients = Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients()
                        self.clients.parent = self
                        self._children_name_map["clients"] = "clients"
                        self._segment_path = lambda: "binding"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Binding, [], name, value)


                    class Summary(Entity):
                        """
                        DHCP server binding summary
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: initializing_clients
                        
                        	Number of clients in init state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_init
                        
                        	Number of clients in Init DPM wait state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_request
                        
                        	Number of clients in Request DPM wait state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_daps_init
                        
                        	Number of clients in Init DAPS wait state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: selecting_clients
                        
                        	Number of clients in selecting state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: offer_sent_for_client
                        
                        	Number of clients in Offer sent state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: requesting_clients
                        
                        	Number of clients in requesting state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: request_waiting_for_dpm
                        
                        	Number of clients in Waiting for DPM with Request
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ack_waiting_for_dpm
                        
                        	Number of clients in Waiting for DPM with ACK
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bound_clients
                        
                        	Number of clients in bound state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: renewing_clients
                        
                        	Number of clients in renewing state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: informing_clients
                        
                        	Number of clients in informing state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reauthorizing_clients
                        
                        	Number of clients in reauth state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_disconnect
                        
                        	Number of clients in waiting for DPM disconnect state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: waiting_for_dpm_addr_change
                        
                        	Number of clients in Waiting for DPM after addr change
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: deleting_clients_d
                        
                        	Number of clients in deleting state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: disconnected_clients
                        
                        	Number of clients in disconnected state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: restarting_clients
                        
                        	Number of clients in restarting state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "binding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('clients', (YLeaf(YType.uint32, 'clients'), ['int'])),
                                ('initializing_clients', (YLeaf(YType.uint32, 'initializing-clients'), ['int'])),
                                ('waiting_for_dpm_init', (YLeaf(YType.uint32, 'waiting-for-dpm-init'), ['int'])),
                                ('waiting_for_dpm_request', (YLeaf(YType.uint32, 'waiting-for-dpm-request'), ['int'])),
                                ('waiting_for_daps_init', (YLeaf(YType.uint32, 'waiting-for-daps-init'), ['int'])),
                                ('selecting_clients', (YLeaf(YType.uint32, 'selecting-clients'), ['int'])),
                                ('offer_sent_for_client', (YLeaf(YType.uint32, 'offer-sent-for-client'), ['int'])),
                                ('requesting_clients', (YLeaf(YType.uint32, 'requesting-clients'), ['int'])),
                                ('request_waiting_for_dpm', (YLeaf(YType.uint32, 'request-waiting-for-dpm'), ['int'])),
                                ('ack_waiting_for_dpm', (YLeaf(YType.uint32, 'ack-waiting-for-dpm'), ['int'])),
                                ('bound_clients', (YLeaf(YType.uint32, 'bound-clients'), ['int'])),
                                ('renewing_clients', (YLeaf(YType.uint32, 'renewing-clients'), ['int'])),
                                ('informing_clients', (YLeaf(YType.uint32, 'informing-clients'), ['int'])),
                                ('reauthorizing_clients', (YLeaf(YType.uint32, 'reauthorizing-clients'), ['int'])),
                                ('waiting_for_dpm_disconnect', (YLeaf(YType.uint32, 'waiting-for-dpm-disconnect'), ['int'])),
                                ('waiting_for_dpm_addr_change', (YLeaf(YType.uint32, 'waiting-for-dpm-addr-change'), ['int'])),
                                ('deleting_clients_d', (YLeaf(YType.uint32, 'deleting-clients-d'), ['int'])),
                                ('disconnected_clients', (YLeaf(YType.uint32, 'disconnected-clients'), ['int'])),
                                ('restarting_clients', (YLeaf(YType.uint32, 'restarting-clients'), ['int'])),
                            ])
                            self.clients = None
                            self.initializing_clients = None
                            self.waiting_for_dpm_init = None
                            self.waiting_for_dpm_request = None
                            self.waiting_for_daps_init = None
                            self.selecting_clients = None
                            self.offer_sent_for_client = None
                            self.requesting_clients = None
                            self.request_waiting_for_dpm = None
                            self.ack_waiting_for_dpm = None
                            self.bound_clients = None
                            self.renewing_clients = None
                            self.informing_clients = None
                            self.reauthorizing_clients = None
                            self.waiting_for_dpm_disconnect = None
                            self.waiting_for_dpm_addr_change = None
                            self.deleting_clients_d = None
                            self.disconnected_clients = None
                            self.restarting_clients = None
                            self._segment_path = lambda: "summary"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary, [u'clients', u'initializing_clients', u'waiting_for_dpm_init', u'waiting_for_dpm_request', u'waiting_for_daps_init', u'selecting_clients', u'offer_sent_for_client', u'requesting_clients', u'request_waiting_for_dpm', u'ack_waiting_for_dpm', u'bound_clients', u'renewing_clients', u'informing_clients', u'reauthorizing_clients', u'waiting_for_dpm_disconnect', u'waiting_for_dpm_addr_change', u'deleting_clients_d', u'disconnected_clients', u'restarting_clients'], name, value)


                    class Clients(Entity):
                        """
                        DHCP server client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCP Server binding
                        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients, self).__init__()

                            self.yang_name = "clients"
                            self.yang_parent_name = "binding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("client", ("client", Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients.Client))])
                            self._leafs = OrderedDict()

                            self.client = YList(self)
                            self._segment_path = lambda: "clients"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients, [], name, value)


                        class Client(Entity):
                            """
                            Single DHCP Server binding
                            
                            .. attribute:: client_id  (key)
                            
                            	Client ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: client_id_xr
                            
                            	DHCP client identifier
                            	**type**\: str
                            
                            	**length:** 0..1275
                            
                            .. attribute:: mac_address
                            
                            	DHCP client MAC address
                            	**type**\: str
                            
                            .. attribute:: vrf_name
                            
                            	DHCP client/subscriber VRF name
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: server_vrf_name
                            
                            	DHCP server VRF name
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: ip_address
                            
                            	DHCP IP address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: client_gi_addr
                            
                            	DHCP client GIADDR
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: to_server_gi_addr
                            
                            	DHCP to server GIADDR
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: server_ip_address
                            
                            	DHCP server IP address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: reply_server_ip_address
                            
                            	DHCP reply server IP address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: lease_time
                            
                            	Lease time in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: remaining_lease_time
                            
                            	Remaining lease time in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: state
                            
                            	DHCP client state
                            	**type**\:  :py:class:`BagDhcpdProxyState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.BagDhcpdProxyState>`
                            
                            .. attribute:: interface_name
                            
                            	DHCP access interface to client
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: access_vrf_name
                            
                            	DHCP access interface VRF name
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: proxy_binding_outer_tag
                            
                            	DHCP VLAN outer VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_binding_inner_tag
                            
                            	DHCP VLAN inner VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: profile_name
                            
                            	DHCP profile name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            .. attribute:: is_nak_next_renew
                            
                            	Is true if DHCP next renew from client will be NAK'd
                            	**type**\: bool
                            
                            .. attribute:: subscriber_label
                            
                            	DHCP subscriber label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: old_subscriber_label
                            
                            	DHCP old subscriber label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: subscriber_interface_name
                            
                            	DHCP subscriber interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: rx_circuit_id
                            
                            	DHCP received circuit ID
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: tx_circuit_id
                            
                            	DHCP transmitted circuit ID
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: rx_remote_id
                            
                            	DHCP received Remote ID
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: tx_remote_id
                            
                            	DHCP transmitted Remote ID
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: rx_vsiso
                            
                            	DHCP received VSISO
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: tx_vsiso
                            
                            	DHCP transmitted VSISO
                            	**type**\: str
                            
                            	**length:** 0..768
                            
                            .. attribute:: is_auth_received
                            
                            	Is true if authentication is on received option82
                            	**type**\: bool
                            
                            .. attribute:: is_mbl_subscriber
                            
                            	Is true if DHCP subscriber is Mobile
                            	**type**\: bool
                            
                            .. attribute:: param_request
                            
                            	DHCP parameter request option
                            	**type**\: str
                            
                            	**length:** 0..513
                            
                            .. attribute:: param_response
                            
                            	DHCP saved options
                            	**type**\: str
                            
                            	**length:** 0..2051
                            
                            .. attribute:: session_start_time
                            
                            	session start time
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: srg_state
                            
                            	DHCPV4 SRG state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: event_history
                            
                            	event history
                            	**type**\: list of int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients.Client, self).__init__()

                                self.yang_name = "client"
                                self.yang_parent_name = "clients"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['client_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('client_id', (YLeaf(YType.str, 'client-id'), ['str'])),
                                    ('client_id_xr', (YLeaf(YType.str, 'client-id-xr'), ['str'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ('server_vrf_name', (YLeaf(YType.str, 'server-vrf-name'), ['str'])),
                                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                    ('client_gi_addr', (YLeaf(YType.str, 'client-gi-addr'), ['str'])),
                                    ('to_server_gi_addr', (YLeaf(YType.str, 'to-server-gi-addr'), ['str'])),
                                    ('server_ip_address', (YLeaf(YType.str, 'server-ip-address'), ['str'])),
                                    ('reply_server_ip_address', (YLeaf(YType.str, 'reply-server-ip-address'), ['str'])),
                                    ('lease_time', (YLeaf(YType.uint32, 'lease-time'), ['int'])),
                                    ('remaining_lease_time', (YLeaf(YType.uint32, 'remaining-lease-time'), ['int'])),
                                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'BagDhcpdProxyState', '')])),
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('access_vrf_name', (YLeaf(YType.str, 'access-vrf-name'), ['str'])),
                                    ('proxy_binding_outer_tag', (YLeaf(YType.uint32, 'proxy-binding-outer-tag'), ['int'])),
                                    ('proxy_binding_inner_tag', (YLeaf(YType.uint32, 'proxy-binding-inner-tag'), ['int'])),
                                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                    ('is_nak_next_renew', (YLeaf(YType.boolean, 'is-nak-next-renew'), ['bool'])),
                                    ('subscriber_label', (YLeaf(YType.uint32, 'subscriber-label'), ['int'])),
                                    ('old_subscriber_label', (YLeaf(YType.uint32, 'old-subscriber-label'), ['int'])),
                                    ('subscriber_interface_name', (YLeaf(YType.str, 'subscriber-interface-name'), ['str'])),
                                    ('rx_circuit_id', (YLeaf(YType.str, 'rx-circuit-id'), ['str'])),
                                    ('tx_circuit_id', (YLeaf(YType.str, 'tx-circuit-id'), ['str'])),
                                    ('rx_remote_id', (YLeaf(YType.str, 'rx-remote-id'), ['str'])),
                                    ('tx_remote_id', (YLeaf(YType.str, 'tx-remote-id'), ['str'])),
                                    ('rx_vsiso', (YLeaf(YType.str, 'rx-vsiso'), ['str'])),
                                    ('tx_vsiso', (YLeaf(YType.str, 'tx-vsiso'), ['str'])),
                                    ('is_auth_received', (YLeaf(YType.boolean, 'is-auth-received'), ['bool'])),
                                    ('is_mbl_subscriber', (YLeaf(YType.boolean, 'is-mbl-subscriber'), ['bool'])),
                                    ('param_request', (YLeaf(YType.str, 'param-request'), ['str'])),
                                    ('param_response', (YLeaf(YType.str, 'param-response'), ['str'])),
                                    ('session_start_time', (YLeaf(YType.uint64, 'session-start-time'), ['int'])),
                                    ('srg_state', (YLeaf(YType.uint32, 'srg-state'), ['int'])),
                                    ('event_history', (YLeafList(YType.uint32, 'event-history'), ['int'])),
                                ])
                                self.client_id = None
                                self.client_id_xr = None
                                self.mac_address = None
                                self.vrf_name = None
                                self.server_vrf_name = None
                                self.ip_address = None
                                self.client_gi_addr = None
                                self.to_server_gi_addr = None
                                self.server_ip_address = None
                                self.reply_server_ip_address = None
                                self.lease_time = None
                                self.remaining_lease_time = None
                                self.state = None
                                self.interface_name = None
                                self.access_vrf_name = None
                                self.proxy_binding_outer_tag = None
                                self.proxy_binding_inner_tag = None
                                self.profile_name = None
                                self.is_nak_next_renew = None
                                self.subscriber_label = None
                                self.old_subscriber_label = None
                                self.subscriber_interface_name = None
                                self.rx_circuit_id = None
                                self.tx_circuit_id = None
                                self.rx_remote_id = None
                                self.tx_remote_id = None
                                self.rx_vsiso = None
                                self.tx_vsiso = None
                                self.is_auth_received = None
                                self.is_mbl_subscriber = None
                                self.param_request = None
                                self.param_response = None
                                self.session_start_time = None
                                self.srg_state = None
                                self.event_history = []
                                self._segment_path = lambda: "client" + "[client-id='" + str(self.client_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients.Client, ['client_id', u'client_id_xr', u'mac_address', u'vrf_name', u'server_vrf_name', u'ip_address', u'client_gi_addr', u'to_server_gi_addr', u'server_ip_address', u'reply_server_ip_address', u'lease_time', u'remaining_lease_time', u'state', u'interface_name', u'access_vrf_name', u'proxy_binding_outer_tag', u'proxy_binding_inner_tag', u'profile_name', u'is_nak_next_renew', u'subscriber_label', u'old_subscriber_label', u'subscriber_interface_name', u'rx_circuit_id', u'tx_circuit_id', u'rx_remote_id', u'tx_remote_id', u'rx_vsiso', u'tx_vsiso', u'is_auth_received', u'is_mbl_subscriber', u'param_request', u'param_response', u'session_start_time', u'srg_state', u'event_history'], name, value)


                class StatisticsInfo(Entity):
                    """
                    DHCP proxy stats info
                    
                    .. attribute:: proxy_stats_timestamp
                    
                    	Proxy Stats timestamp
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo, self).__init__()

                        self.yang_name = "statistics-info"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('proxy_stats_timestamp', (YLeaf(YType.uint32, 'proxy-stats-timestamp'), ['int'])),
                        ])
                        self.proxy_stats_timestamp = None
                        self._segment_path = lambda: "statistics-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo, [u'proxy_stats_timestamp'], name, value)


                class Vrfs(Entity):
                    """
                    DHCP Server list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv4 DHCP server VRF name
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vrf", ("vrf", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf))])
                        self._leafs = OrderedDict()

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs, [], name, value)


                    class Vrf(Entity):
                        """
                        IPv4 DHCP server VRF name
                        
                        .. attribute:: vrf_name  (key)
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv4 DHCP server statistics
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_classes = OrderedDict([("statistics", ("statistics", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics))])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None

                            self.statistics = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf, ['vrf_name'], name, value)


                        class Statistics(Entity):
                            """
                            IPv4 DHCP server statistics
                            
                            .. attribute:: discover
                            
                            	DHCP discover packets
                            	**type**\:  :py:class:`Discover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover>`
                            
                            .. attribute:: offer
                            
                            	DHCP offer packets
                            	**type**\:  :py:class:`Offer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer>`
                            
                            .. attribute:: request
                            
                            	DHCP request packets
                            	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: decline
                            
                            	DHCP decline packets
                            	**type**\:  :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: ack
                            
                            	DHCP ack packets
                            	**type**\:  :py:class:`Ack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack>`
                            
                            .. attribute:: nak
                            
                            	DHCP nak packets
                            	**type**\:  :py:class:`Nak <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak>`
                            
                            .. attribute:: release
                            
                            	DHCP release packets
                            	**type**\:  :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: inform
                            
                            	DHCP inform packets
                            	**type**\:  :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: lease_query
                            
                            	DHCP lease query packets
                            	**type**\:  :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_not_assigned
                            
                            	DHCP lease not assigned
                            	**type**\:  :py:class:`LeaseNotAssigned <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned>`
                            
                            .. attribute:: lease_unknown
                            
                            	DHCP lease unknown
                            	**type**\:  :py:class:`LeaseUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown>`
                            
                            .. attribute:: lease_active
                            
                            	DHCP lease active
                            	**type**\:  :py:class:`LeaseActive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive>`
                            
                            .. attribute:: bootp_request
                            
                            	DHCP BOOTP request
                            	**type**\:  :py:class:`BootpRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest>`
                            
                            .. attribute:: bootp_reply
                            
                            	DHCP BOOTP reply
                            	**type**\:  :py:class:`BootpReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("discover", ("discover", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover)), ("offer", ("offer", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer)), ("request", ("request", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request)), ("decline", ("decline", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline)), ("ack", ("ack", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack)), ("nak", ("nak", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak)), ("release", ("release", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release)), ("inform", ("inform", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform)), ("lease-query", ("lease_query", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery)), ("lease-not-assigned", ("lease_not_assigned", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned)), ("lease-unknown", ("lease_unknown", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown)), ("lease-active", ("lease_active", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive)), ("bootp-request", ("bootp_request", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest)), ("bootp-reply", ("bootp_reply", Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply))])
                                self._leafs = OrderedDict()

                                self.discover = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover()
                                self.discover.parent = self
                                self._children_name_map["discover"] = "discover"

                                self.offer = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer()
                                self.offer.parent = self
                                self._children_name_map["offer"] = "offer"

                                self.request = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self._children_name_map["request"] = "request"

                                self.decline = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self._children_name_map["decline"] = "decline"

                                self.ack = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack()
                                self.ack.parent = self
                                self._children_name_map["ack"] = "ack"

                                self.nak = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak()
                                self.nak.parent = self
                                self._children_name_map["nak"] = "nak"

                                self.release = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self._children_name_map["release"] = "release"

                                self.inform = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self._children_name_map["inform"] = "inform"

                                self.lease_query = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self._children_name_map["lease_query"] = "lease-query"

                                self.lease_not_assigned = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned()
                                self.lease_not_assigned.parent = self
                                self._children_name_map["lease_not_assigned"] = "lease-not-assigned"

                                self.lease_unknown = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown()
                                self.lease_unknown.parent = self
                                self._children_name_map["lease_unknown"] = "lease-unknown"

                                self.lease_active = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive()
                                self.lease_active.parent = self
                                self._children_name_map["lease_active"] = "lease-active"

                                self.bootp_request = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest()
                                self.bootp_request.parent = self
                                self._children_name_map["bootp_request"] = "bootp-request"

                                self.bootp_reply = Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply()
                                self.bootp_reply.parent = self
                                self._children_name_map["bootp_reply"] = "bootp-reply"
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics, [], name, value)


                            class Discover(Entity):
                                """
                                DHCP discover packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover, self).__init__()

                                    self.yang_name = "discover"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "discover"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Offer(Entity):
                                """
                                DHCP offer packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer, self).__init__()

                                    self.yang_name = "offer"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "offer"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Request(Entity):
                                """
                                DHCP request packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request, self).__init__()

                                    self.yang_name = "request"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "request"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Decline(Entity):
                                """
                                DHCP decline packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline, self).__init__()

                                    self.yang_name = "decline"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "decline"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Ack(Entity):
                                """
                                DHCP ack packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack, self).__init__()

                                    self.yang_name = "ack"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "ack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Nak(Entity):
                                """
                                DHCP nak packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak, self).__init__()

                                    self.yang_name = "nak"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "nak"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Release(Entity):
                                """
                                DHCP release packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release, self).__init__()

                                    self.yang_name = "release"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "release"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Inform(Entity):
                                """
                                DHCP inform packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform, self).__init__()

                                    self.yang_name = "inform"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "inform"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseQuery(Entity):
                                """
                                DHCP lease query packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery, self).__init__()

                                    self.yang_name = "lease-query"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseNotAssigned(Entity):
                                """
                                DHCP lease not assigned
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned, self).__init__()

                                    self.yang_name = "lease-not-assigned"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-not-assigned"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseUnknown(Entity):
                                """
                                DHCP lease unknown
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown, self).__init__()

                                    self.yang_name = "lease-unknown"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-unknown"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseActive(Entity):
                                """
                                DHCP lease active
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive, self).__init__()

                                    self.yang_name = "lease-active"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-active"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class BootpRequest(Entity):
                                """
                                DHCP BOOTP request
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest, self).__init__()

                                    self.yang_name = "bootp-request"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "bootp-request"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class BootpReply(Entity):
                                """
                                DHCP BOOTP reply
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply, self).__init__()

                                    self.yang_name = "bootp-reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "bootp-reply"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


            class Relay(Entity):
                """
                IPv4 DHCPD Relay operational data
                
                .. attribute:: profiles
                
                	DHCP Relay Profiles
                	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Profiles>`
                
                .. attribute:: statistics_info
                
                	DHCP relay statistics info
                	**type**\:  :py:class:`StatisticsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo>`
                
                .. attribute:: statistics
                
                	DHCP Relay VRF statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Statistics>`
                
                .. attribute:: vrfs
                
                	DHCP relay list of VRF names
                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs>`
                
                

                """

                _prefix = 'ipv4-dhcpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Nodes.Node.Relay, self).__init__()

                    self.yang_name = "relay"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("profiles", ("profiles", Ipv4Dhcpd.Nodes.Node.Relay.Profiles)), ("statistics-info", ("statistics_info", Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo)), ("statistics", ("statistics", Ipv4Dhcpd.Nodes.Node.Relay.Statistics)), ("vrfs", ("vrfs", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs))])
                    self._leafs = OrderedDict()

                    self.profiles = Ipv4Dhcpd.Nodes.Node.Relay.Profiles()
                    self.profiles.parent = self
                    self._children_name_map["profiles"] = "profiles"

                    self.statistics_info = Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo()
                    self.statistics_info.parent = self
                    self._children_name_map["statistics_info"] = "statistics-info"

                    self.statistics = Ipv4Dhcpd.Nodes.Node.Relay.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"

                    self.vrfs = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                    self._segment_path = lambda: "relay"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay, [], name, value)


                class Profiles(Entity):
                    """
                    DHCP Relay Profiles
                    
                    .. attribute:: profile
                    
                    	DHCP Relay profile
                    	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Relay.Profiles, self).__init__()

                        self.yang_name = "profiles"
                        self.yang_parent_name = "relay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("profile", ("profile", Ipv4Dhcpd.Nodes.Node.Relay.Profiles.Profile))])
                        self._leafs = OrderedDict()

                        self.profile = YList(self)
                        self._segment_path = lambda: "profiles"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Profiles, [], name, value)


                    class Profile(Entity):
                        """
                        DHCP Relay profile
                        
                        .. attribute:: profile_name  (key)
                        
                        	Profile name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: relay_profile_name
                        
                        	Profile Name
                        	**type**\: str
                        
                        	**length:** 0..65
                        
                        .. attribute:: relay_profile_uid
                        
                        	Profile UID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: relay_profile_helper_count
                        
                        	Helper address count
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_relay_info_option
                        
                        	Relay info option
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_relay_info_policy
                        
                        	Relay info policy
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_relay_info_allow_untrusted
                        
                        	Relay info untrusted
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_relay_info_optionvpn
                        
                        	Relay info option vpn
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_relay_info_optionvpn_mode
                        
                        	Relay info option vpn\-mode
                        	**type**\:  :py:class:`RelayInfoVpnMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.RelayInfoVpnMode>`
                        
                        .. attribute:: relay_profile_relay_info_check
                        
                        	Relay info check
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_gi_addr_policy
                        
                        	GIADDR policy
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_broadcast_flag_policy
                        
                        	Broadcast policy
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_mac_mismatch_action
                        
                        	Mac Mismatch Action
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_profile_helper_address
                        
                        	Helper addresses
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: relay_profile_helper_vrf
                        
                        	Helper address vrfs
                        	**type**\: list of str
                        
                        	**length:** 0..33
                        
                        .. attribute:: relay_profile_gi_addr
                        
                        	Gateway addresses
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Relay.Profiles.Profile, self).__init__()

                            self.yang_name = "profile"
                            self.yang_parent_name = "profiles"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['profile_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                ('relay_profile_name', (YLeaf(YType.str, 'relay-profile-name'), ['str'])),
                                ('relay_profile_uid', (YLeaf(YType.uint32, 'relay-profile-uid'), ['int'])),
                                ('relay_profile_helper_count', (YLeaf(YType.uint8, 'relay-profile-helper-count'), ['int'])),
                                ('relay_profile_relay_info_option', (YLeaf(YType.uint8, 'relay-profile-relay-info-option'), ['int'])),
                                ('relay_profile_relay_info_policy', (YLeaf(YType.uint8, 'relay-profile-relay-info-policy'), ['int'])),
                                ('relay_profile_relay_info_allow_untrusted', (YLeaf(YType.uint8, 'relay-profile-relay-info-allow-untrusted'), ['int'])),
                                ('relay_profile_relay_info_optionvpn', (YLeaf(YType.uint8, 'relay-profile-relay-info-optionvpn'), ['int'])),
                                ('relay_profile_relay_info_optionvpn_mode', (YLeaf(YType.enumeration, 'relay-profile-relay-info-optionvpn-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'RelayInfoVpnMode', '')])),
                                ('relay_profile_relay_info_check', (YLeaf(YType.uint8, 'relay-profile-relay-info-check'), ['int'])),
                                ('relay_profile_gi_addr_policy', (YLeaf(YType.uint8, 'relay-profile-gi-addr-policy'), ['int'])),
                                ('relay_profile_broadcast_flag_policy', (YLeaf(YType.uint8, 'relay-profile-broadcast-flag-policy'), ['int'])),
                                ('relay_profile_mac_mismatch_action', (YLeaf(YType.uint8, 'relay-profile-mac-mismatch-action'), ['int'])),
                                ('relay_profile_helper_address', (YLeafList(YType.str, 'relay-profile-helper-address'), ['str'])),
                                ('relay_profile_helper_vrf', (YLeafList(YType.str, 'relay-profile-helper-vrf'), ['str'])),
                                ('relay_profile_gi_addr', (YLeafList(YType.str, 'relay-profile-gi-addr'), ['str'])),
                            ])
                            self.profile_name = None
                            self.relay_profile_name = None
                            self.relay_profile_uid = None
                            self.relay_profile_helper_count = None
                            self.relay_profile_relay_info_option = None
                            self.relay_profile_relay_info_policy = None
                            self.relay_profile_relay_info_allow_untrusted = None
                            self.relay_profile_relay_info_optionvpn = None
                            self.relay_profile_relay_info_optionvpn_mode = None
                            self.relay_profile_relay_info_check = None
                            self.relay_profile_gi_addr_policy = None
                            self.relay_profile_broadcast_flag_policy = None
                            self.relay_profile_mac_mismatch_action = None
                            self.relay_profile_helper_address = []
                            self.relay_profile_helper_vrf = []
                            self.relay_profile_gi_addr = []
                            self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Profiles.Profile, ['profile_name', u'relay_profile_name', u'relay_profile_uid', u'relay_profile_helper_count', u'relay_profile_relay_info_option', u'relay_profile_relay_info_policy', u'relay_profile_relay_info_allow_untrusted', u'relay_profile_relay_info_optionvpn', u'relay_profile_relay_info_optionvpn_mode', u'relay_profile_relay_info_check', u'relay_profile_gi_addr_policy', u'relay_profile_broadcast_flag_policy', u'relay_profile_mac_mismatch_action', u'relay_profile_helper_address', u'relay_profile_helper_vrf', u'relay_profile_gi_addr'], name, value)


                class StatisticsInfo(Entity):
                    """
                    DHCP relay statistics info
                    
                    .. attribute:: relay_stats_timestamp
                    
                    	Relay Stats timestamp
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo, self).__init__()

                        self.yang_name = "statistics-info"
                        self.yang_parent_name = "relay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('relay_stats_timestamp', (YLeaf(YType.uint32, 'relay-stats-timestamp'), ['int'])),
                        ])
                        self.relay_stats_timestamp = None
                        self._segment_path = lambda: "statistics-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo, [u'relay_stats_timestamp'], name, value)


                class Statistics(Entity):
                    """
                    DHCP Relay VRF statistics
                    
                    .. attribute:: ipv4_dhcpd_relay_stat
                    
                    	ipv4 dhcpd relay stat
                    	**type**\: list of  		 :py:class:`Ipv4DhcpdRelayStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Relay.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "relay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv4-dhcpd-relay-stat", ("ipv4_dhcpd_relay_stat", Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat))])
                        self._leafs = OrderedDict()

                        self.ipv4_dhcpd_relay_stat = YList(self)
                        self._segment_path = lambda: "statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Statistics, [], name, value)


                    class Ipv4DhcpdRelayStat(Entity):
                        """
                        ipv4 dhcpd relay stat
                        
                        .. attribute:: statistics
                        
                        	Public relay statistics
                        	**type**\:  :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_>`
                        
                        .. attribute:: relay_statistics_vrf_name
                        
                        	DHCP L3 VRF Name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat, self).__init__()

                            self.yang_name = "ipv4-dhcpd-relay-stat"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("statistics", ("statistics", Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_))])
                            self._leafs = OrderedDict([
                                ('relay_statistics_vrf_name', (YLeaf(YType.str, 'relay-statistics-vrf-name'), ['str'])),
                            ])
                            self.relay_statistics_vrf_name = None

                            self.statistics = Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._segment_path = lambda: "ipv4-dhcpd-relay-stat"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat, [u'relay_statistics_vrf_name'], name, value)


                        class Statistics_(Entity):
                            """
                            Public relay statistics
                            
                            .. attribute:: received_packets
                            
                            	Received packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: transmitted_packets
                            
                            	Transmitted packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dropped_packets
                            
                            	Dropped packets
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "ipv4-dhcpd-relay-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                    ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                    ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                ])
                                self.received_packets = None
                                self.transmitted_packets = None
                                self.dropped_packets = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                class Vrfs(Entity):
                    """
                    DHCP relay list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv4 DHCP relay VRF name
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "relay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vrf", ("vrf", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf))])
                        self._leafs = OrderedDict()

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs, [], name, value)


                    class Vrf(Entity):
                        """
                        IPv4 DHCP relay VRF name
                        
                        .. attribute:: vrf_name  (key)
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: vrf_statistics
                        
                        	IPv4 DHCP relay statistics
                        	**type**\:  :py:class:`VrfStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_classes = OrderedDict([("vrf-statistics", ("vrf_statistics", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics))])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None

                            self.vrf_statistics = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics()
                            self.vrf_statistics.parent = self
                            self._children_name_map["vrf_statistics"] = "vrf-statistics"
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf, ['vrf_name'], name, value)


                        class VrfStatistics(Entity):
                            """
                            IPv4 DHCP relay statistics
                            
                            .. attribute:: discover
                            
                            	DHCP discover packets
                            	**type**\:  :py:class:`Discover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover>`
                            
                            .. attribute:: offer
                            
                            	DHCP offer packets
                            	**type**\:  :py:class:`Offer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer>`
                            
                            .. attribute:: request
                            
                            	DHCP request packets
                            	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request>`
                            
                            .. attribute:: decline
                            
                            	DHCP decline packets
                            	**type**\:  :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline>`
                            
                            .. attribute:: ack
                            
                            	DHCP ack packets
                            	**type**\:  :py:class:`Ack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack>`
                            
                            .. attribute:: nak
                            
                            	DHCP nak packets
                            	**type**\:  :py:class:`Nak <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak>`
                            
                            .. attribute:: release
                            
                            	DHCP release packets
                            	**type**\:  :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release>`
                            
                            .. attribute:: inform
                            
                            	DHCP inform packets
                            	**type**\:  :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform>`
                            
                            .. attribute:: lease_query
                            
                            	DHCP lease query packets
                            	**type**\:  :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery>`
                            
                            .. attribute:: lease_not_assigned
                            
                            	DHCP lease not assigned
                            	**type**\:  :py:class:`LeaseNotAssigned <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned>`
                            
                            .. attribute:: lease_unknown
                            
                            	DHCP lease unknown
                            	**type**\:  :py:class:`LeaseUnknown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown>`
                            
                            .. attribute:: lease_active
                            
                            	DHCP lease active
                            	**type**\:  :py:class:`LeaseActive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive>`
                            
                            .. attribute:: bootp_request
                            
                            	DHCP BOOTP request
                            	**type**\:  :py:class:`BootpRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest>`
                            
                            .. attribute:: bootp_reply
                            
                            	DHCP BOOTP reply
                            	**type**\:  :py:class:`BootpReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper.Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics, self).__init__()

                                self.yang_name = "vrf-statistics"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("discover", ("discover", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover)), ("offer", ("offer", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer)), ("request", ("request", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request)), ("decline", ("decline", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline)), ("ack", ("ack", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack)), ("nak", ("nak", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak)), ("release", ("release", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release)), ("inform", ("inform", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform)), ("lease-query", ("lease_query", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery)), ("lease-not-assigned", ("lease_not_assigned", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned)), ("lease-unknown", ("lease_unknown", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown)), ("lease-active", ("lease_active", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive)), ("bootp-request", ("bootp_request", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest)), ("bootp-reply", ("bootp_reply", Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply))])
                                self._leafs = OrderedDict()

                                self.discover = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover()
                                self.discover.parent = self
                                self._children_name_map["discover"] = "discover"

                                self.offer = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer()
                                self.offer.parent = self
                                self._children_name_map["offer"] = "offer"

                                self.request = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request()
                                self.request.parent = self
                                self._children_name_map["request"] = "request"

                                self.decline = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline()
                                self.decline.parent = self
                                self._children_name_map["decline"] = "decline"

                                self.ack = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack()
                                self.ack.parent = self
                                self._children_name_map["ack"] = "ack"

                                self.nak = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak()
                                self.nak.parent = self
                                self._children_name_map["nak"] = "nak"

                                self.release = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release()
                                self.release.parent = self
                                self._children_name_map["release"] = "release"

                                self.inform = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform()
                                self.inform.parent = self
                                self._children_name_map["inform"] = "inform"

                                self.lease_query = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery()
                                self.lease_query.parent = self
                                self._children_name_map["lease_query"] = "lease-query"

                                self.lease_not_assigned = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned()
                                self.lease_not_assigned.parent = self
                                self._children_name_map["lease_not_assigned"] = "lease-not-assigned"

                                self.lease_unknown = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown()
                                self.lease_unknown.parent = self
                                self._children_name_map["lease_unknown"] = "lease-unknown"

                                self.lease_active = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive()
                                self.lease_active.parent = self
                                self._children_name_map["lease_active"] = "lease-active"

                                self.bootp_request = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest()
                                self.bootp_request.parent = self
                                self._children_name_map["bootp_request"] = "bootp-request"

                                self.bootp_reply = Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply()
                                self.bootp_reply.parent = self
                                self._children_name_map["bootp_reply"] = "bootp-reply"
                                self._segment_path = lambda: "vrf-statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics, [], name, value)


                            class Discover(Entity):
                                """
                                DHCP discover packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover, self).__init__()

                                    self.yang_name = "discover"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "discover"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Offer(Entity):
                                """
                                DHCP offer packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer, self).__init__()

                                    self.yang_name = "offer"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "offer"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Request(Entity):
                                """
                                DHCP request packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request, self).__init__()

                                    self.yang_name = "request"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "request"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Decline(Entity):
                                """
                                DHCP decline packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline, self).__init__()

                                    self.yang_name = "decline"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "decline"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Ack(Entity):
                                """
                                DHCP ack packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack, self).__init__()

                                    self.yang_name = "ack"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "ack"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Nak(Entity):
                                """
                                DHCP nak packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak, self).__init__()

                                    self.yang_name = "nak"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "nak"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Release(Entity):
                                """
                                DHCP release packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release, self).__init__()

                                    self.yang_name = "release"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "release"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class Inform(Entity):
                                """
                                DHCP inform packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform, self).__init__()

                                    self.yang_name = "inform"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "inform"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseQuery(Entity):
                                """
                                DHCP lease query packets
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery, self).__init__()

                                    self.yang_name = "lease-query"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseNotAssigned(Entity):
                                """
                                DHCP lease not assigned
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned, self).__init__()

                                    self.yang_name = "lease-not-assigned"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-not-assigned"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseUnknown(Entity):
                                """
                                DHCP lease unknown
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown, self).__init__()

                                    self.yang_name = "lease-unknown"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-unknown"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class LeaseActive(Entity):
                                """
                                DHCP lease active
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive, self).__init__()

                                    self.yang_name = "lease-active"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-active"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class BootpRequest(Entity):
                                """
                                DHCP BOOTP request
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest, self).__init__()

                                    self.yang_name = "bootp-request"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "bootp-request"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)


                            class BootpReply(Entity):
                                """
                                DHCP BOOTP reply
                                
                                .. attribute:: received_packets
                                
                                	Received packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmitted_packets
                                
                                	Transmitted packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	Dropped packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply, self).__init__()

                                    self.yang_name = "bootp-reply"
                                    self.yang_parent_name = "vrf-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                        ('transmitted_packets', (YLeaf(YType.uint64, 'transmitted-packets'), ['int'])),
                                        ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "bootp-reply"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply, [u'received_packets', u'transmitted_packets', u'dropped_packets'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv4Dhcpd()
        return self._top_entity

