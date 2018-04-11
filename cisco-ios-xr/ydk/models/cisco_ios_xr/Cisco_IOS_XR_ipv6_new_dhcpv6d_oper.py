""" Cisco_IOS_XR_ipv6_new_dhcpv6d_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-new\-dhcpv6d package operational data.

This module contains definitions
for the following management objects\:
  dhcpv6\: IPV6 DHCPD operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BagDhcpv6DFsmState(Enum):
    """
    BagDhcpv6DFsmState (Enum Class)

    Bag dhcpv6d fsm state

    .. data:: server_initializing = 0

    	Server initializing state for client binding

    .. data:: server_waiting_dpm = 1

    	Server waiting on DPM to validate subscriber

    .. data:: server_waiting_daps = 2

    	Server waiting on DAPS to assign/free

    	addr/prefix

    .. data:: server_waiting_client = 3

    	Server waiting for a request from the client

    .. data:: server_waiting_subscriber = 4

    	Server waiting for iedge response for the

    	session

    .. data:: server_waiting_rib = 5

    	Server waiting for RIB response for route add

    .. data:: server_bound_client = 6

    	Server bound state to the client

    .. data:: proxy_initializing = 10

    	Proxy initializing state for client binding

    .. data:: proxy_waiting_dpm = 11

    	Proxy waiting on DPM to validate subscriber

    .. data:: proxy_waiting_daps = 12

    	Proxy waiting on DAPS to assign/free prefix(ND)

    .. data:: proxy_waiting_client_server = 13

    	Proxy waiting for a msg from the client/srv

    .. data:: proxy_waiting_subscriber = 14

    	Proxy waiting on iedge to sub session resp

    .. data:: proxy_waiting_rib = 15

    	Proxy waiting on RIB response

    .. data:: proxy_bound_client = 16

    	Proxy bound state to the client

    """

    server_initializing = Enum.YLeaf(0, "server-initializing")

    server_waiting_dpm = Enum.YLeaf(1, "server-waiting-dpm")

    server_waiting_daps = Enum.YLeaf(2, "server-waiting-daps")

    server_waiting_client = Enum.YLeaf(3, "server-waiting-client")

    server_waiting_subscriber = Enum.YLeaf(4, "server-waiting-subscriber")

    server_waiting_rib = Enum.YLeaf(5, "server-waiting-rib")

    server_bound_client = Enum.YLeaf(6, "server-bound-client")

    proxy_initializing = Enum.YLeaf(10, "proxy-initializing")

    proxy_waiting_dpm = Enum.YLeaf(11, "proxy-waiting-dpm")

    proxy_waiting_daps = Enum.YLeaf(12, "proxy-waiting-daps")

    proxy_waiting_client_server = Enum.YLeaf(13, "proxy-waiting-client-server")

    proxy_waiting_subscriber = Enum.YLeaf(14, "proxy-waiting-subscriber")

    proxy_waiting_rib = Enum.YLeaf(15, "proxy-waiting-rib")

    proxy_bound_client = Enum.YLeaf(16, "proxy-bound-client")


class BagDhcpv6DIaId(Enum):
    """
    BagDhcpv6DIaId (Enum Class)

    Bag dhcpv6d ia id

    .. data:: iana = 0

    	Non-temporary Addresses assigned 

    .. data:: iapd = 1

    	Prefix delegeated to client      

    .. data:: iata = 2

    	Temporary Addresses - not supported 

    """

    iana = Enum.YLeaf(0, "iana")

    iapd = Enum.YLeaf(1, "iapd")

    iata = Enum.YLeaf(2, "iata")


class BagDhcpv6DIntfSergRole(Enum):
    """
    BagDhcpv6DIntfSergRole (Enum Class)

    Bag dhcpv6d intf serg role

    .. data:: none = 0

    	DHCPv6 Interface SERG role NONE

    .. data:: master = 1

    	DHCPv6 Interface SERG role Master

    .. data:: slave = 2

    	DHCPv6 Interface SERG role Slave

    """

    none = Enum.YLeaf(0, "none")

    master = Enum.YLeaf(1, "master")

    slave = Enum.YLeaf(2, "slave")


class BagDhcpv6DIntfSrgRole(Enum):
    """
    BagDhcpv6DIntfSrgRole (Enum Class)

    Bag dhcpv6d intf srg role

    .. data:: none = 0

    	DHCPv6 Interface SRG role NONE

    .. data:: master = 1

    	DHCPv6 Interface SRG role Master

    .. data:: slave = 2

    	DHCPv6 Interface SRG role Slave

    """

    none = Enum.YLeaf(0, "none")

    master = Enum.YLeaf(1, "master")

    slave = Enum.YLeaf(2, "slave")


class BagDhcpv6DSubMode(Enum):
    """
    BagDhcpv6DSubMode (Enum Class)

    Bag dhcpv6d sub mode

    .. data:: base = 0

    	DHCPv6 Base mode

    .. data:: server = 1

    	DHCPv6 Server mode

    .. data:: proxy = 2

    	DHCPv6 Proxy mode

    """

    base = Enum.YLeaf(0, "base")

    server = Enum.YLeaf(1, "server")

    proxy = Enum.YLeaf(2, "proxy")


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


class Dhcpv6IssuRole(Enum):
    """
    Dhcpv6IssuRole (Enum Class)

    Dhcpv6 issu role

    .. data:: role_primary = 0

    	Primary role

    .. data:: role_secondary = 1

    	Secondary role

    """

    role_primary = Enum.YLeaf(0, "role-primary")

    role_secondary = Enum.YLeaf(1, "role-secondary")


class Dhcpv6IssuVersion(Enum):
    """
    Dhcpv6IssuVersion (Enum Class)

    Dhcpv6 issu version

    .. data:: version1 = 0

    	Version 1

    .. data:: version2 = 1

    	Version 2

    """

    version1 = Enum.YLeaf(0, "version1")

    version2 = Enum.YLeaf(1, "version2")


class LeaseLimit(Enum):
    """
    LeaseLimit (Enum Class)

    Profile lease limit type

    .. data:: none = 0

    	Lease limit type none

    .. data:: interface = 1

    	Lease limit type interface

    .. data:: circuit_id = 2

    	Lease limit type circuit ID

    .. data:: remote_id = 3

    	Lease limit type remote ID

    """

    none = Enum.YLeaf(0, "none")

    interface = Enum.YLeaf(1, "interface")

    circuit_id = Enum.YLeaf(2, "circuit-id")

    remote_id = Enum.YLeaf(3, "remote-id")



class Dhcpv6(Entity):
    """
    IPV6 DHCPD operational data
    
    .. attribute:: issu_status
    
    	DHCP IssuStatus
    	**type**\:  :py:class:`IssuStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.IssuStatus>`
    
    .. attribute:: nodes
    
    	IPv6 DHCP list of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes>`
    
    

    """

    _prefix = 'ipv6-new-dhcpv6d-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Dhcpv6, self).__init__()
        self._top_entity = None

        self.yang_name = "dhcpv6"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-new-dhcpv6d-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("issu-status", ("issu_status", Dhcpv6.IssuStatus)), ("nodes", ("nodes", Dhcpv6.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.issu_status = Dhcpv6.IssuStatus()
        self.issu_status.parent = self
        self._children_name_map["issu_status"] = "issu-status"
        self._children_yang_names.add("issu-status")

        self.nodes = Dhcpv6.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6"


    class IssuStatus(Entity):
        """
        DHCP IssuStatus
        
        .. attribute:: process_start_time
        
        	Timestamp for the process start time in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: nanosecond
        
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
        
        .. attribute:: issu_ready_issu_mgr_connection
        
        	Whether or not DHCP is currently connected to ISSU Manager during the ISSU Load Phase
        	**type**\: bool
        
        .. attribute:: role
        
        	The current role of the DHCP process
        	**type**\:  :py:class:`Dhcpv6IssuRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6IssuRole>`
        
        .. attribute:: phase
        
        	The current ISSU phase of the DHCP process
        	**type**\:  :py:class:`DhcpIssuPhase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.DhcpIssuPhase>`
        
        .. attribute:: version
        
        	The current version of the DHCP process in the context of an ISSU
        	**type**\:  :py:class:`Dhcpv6IssuVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6IssuVersion>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dhcpv6.IssuStatus, self).__init__()

            self.yang_name = "issu-status"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('process_start_time', YLeaf(YType.uint64, 'process-start-time')),
                ('issu_sync_complete_time', YLeaf(YType.uint64, 'issu-sync-complete-time')),
                ('issu_sync_start_time', YLeaf(YType.uint64, 'issu-sync-start-time')),
                ('issu_ready_time', YLeaf(YType.uint64, 'issu-ready-time')),
                ('big_bang_time', YLeaf(YType.uint64, 'big-bang-time')),
                ('primary_role_time', YLeaf(YType.uint64, 'primary-role-time')),
                ('issu_ready_issu_mgr_connection', YLeaf(YType.boolean, 'issu-ready-issu-mgr-connection')),
                ('role', YLeaf(YType.enumeration, 'role')),
                ('phase', YLeaf(YType.enumeration, 'phase')),
                ('version', YLeaf(YType.enumeration, 'version')),
            ])
            self.process_start_time = None
            self.issu_sync_complete_time = None
            self.issu_sync_start_time = None
            self.issu_ready_time = None
            self.big_bang_time = None
            self.primary_role_time = None
            self.issu_ready_issu_mgr_connection = None
            self.role = None
            self.phase = None
            self.version = None
            self._segment_path = lambda: "issu-status"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.IssuStatus, ['process_start_time', 'issu_sync_complete_time', 'issu_sync_start_time', 'issu_ready_time', 'big_bang_time', 'primary_role_time', 'issu_ready_issu_mgr_connection', 'role', 'phase', 'version'], name, value)


    class Nodes(Entity):
        """
        IPv6 DHCP list of nodes
        
        .. attribute:: node
        
        	IPv6 DHCP particular node name
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dhcpv6.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", Dhcpv6.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.Nodes, [], name, value)


        class Node(Entity):
            """
            IPv6 DHCP particular node name
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: proxy
            
            	IPv6 DHCP proxy operational data
            	**type**\:  :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy>`
            
            .. attribute:: base
            
            	IPv6 DHCP Base
            	**type**\:  :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Base>`
            
            .. attribute:: server
            
            	IPv6 DHCP server operational data
            	**type**\:  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server>`
            
            .. attribute:: relay
            
            	IPv6 DHCP relay operational data
            	**type**\:  :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay>`
            
            

            """

            _prefix = 'ipv6-new-dhcpv6d-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dhcpv6.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("proxy", ("proxy", Dhcpv6.Nodes.Node.Proxy)), ("base", ("base", Dhcpv6.Nodes.Node.Base)), ("server", ("server", Dhcpv6.Nodes.Node.Server)), ("relay", ("relay", Dhcpv6.Nodes.Node.Relay))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.proxy = Dhcpv6.Nodes.Node.Proxy()
                self.proxy.parent = self
                self._children_name_map["proxy"] = "proxy"
                self._children_yang_names.add("proxy")

                self.base = Dhcpv6.Nodes.Node.Base()
                self.base.parent = self
                self._children_name_map["base"] = "base"
                self._children_yang_names.add("base")

                self.server = Dhcpv6.Nodes.Node.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")

                self.relay = Dhcpv6.Nodes.Node.Relay()
                self.relay.parent = self
                self._children_name_map["relay"] = "relay"
                self._children_yang_names.add("relay")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dhcpv6.Nodes.Node, ['node_name'], name, value)


            class Proxy(Entity):
                """
                IPv6 DHCP proxy operational data
                
                .. attribute:: vrfs
                
                	DHCPV6 proxy list of VRF names
                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs>`
                
                .. attribute:: profiles
                
                	IPv6 DHCP proxy profile
                	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles>`
                
                .. attribute:: interfaces
                
                	DHCPV6 proxy interface
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Interfaces>`
                
                .. attribute:: statistics
                
                	DHCPv6 proxy statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Statistics>`
                
                .. attribute:: binding
                
                	DHCPV6 proxy bindings
                	**type**\:  :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding>`
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dhcpv6.Nodes.Node.Proxy, self).__init__()

                    self.yang_name = "proxy"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("vrfs", ("vrfs", Dhcpv6.Nodes.Node.Proxy.Vrfs)), ("profiles", ("profiles", Dhcpv6.Nodes.Node.Proxy.Profiles)), ("interfaces", ("interfaces", Dhcpv6.Nodes.Node.Proxy.Interfaces)), ("statistics", ("statistics", Dhcpv6.Nodes.Node.Proxy.Statistics)), ("binding", ("binding", Dhcpv6.Nodes.Node.Proxy.Binding))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.vrfs = Dhcpv6.Nodes.Node.Proxy.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                    self._children_yang_names.add("vrfs")

                    self.profiles = Dhcpv6.Nodes.Node.Proxy.Profiles()
                    self.profiles.parent = self
                    self._children_name_map["profiles"] = "profiles"
                    self._children_yang_names.add("profiles")

                    self.interfaces = Dhcpv6.Nodes.Node.Proxy.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")

                    self.statistics = Dhcpv6.Nodes.Node.Proxy.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")

                    self.binding = Dhcpv6.Nodes.Node.Proxy.Binding()
                    self.binding.parent = self
                    self._children_name_map["binding"] = "binding"
                    self._children_yang_names.add("binding")
                    self._segment_path = lambda: "proxy"


                class Vrfs(Entity):
                    """
                    DHCPV6 proxy list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP proxy VRF name
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Proxy.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("vrf", ("vrf", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf))])
                        self._leafs = OrderedDict()

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs, [], name, value)


                    class Vrf(Entity):
                        """
                        IPv6 DHCP proxy VRF name
                        
                        .. attribute:: vrf_name  (key)
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv6 DHCP proxy statistics
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_container_classes = OrderedDict([("statistics", ("statistics", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ])
                            self.vrf_name = None

                            self.statistics = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._children_yang_names.add("statistics")
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf, ['vrf_name'], name, value)


                        class Statistics(Entity):
                            """
                            IPv6 DHCP proxy statistics
                            
                            .. attribute:: solicit
                            
                            	DHCPV6 solicit packets
                            	**type**\:  :py:class:`Solicit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit>`
                            
                            .. attribute:: advertise
                            
                            	DHCPV6 advertise packets
                            	**type**\:  :py:class:`Advertise <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise>`
                            
                            .. attribute:: request
                            
                            	DHCPV6 request packets
                            	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: reply
                            
                            	DHCPV6 reply packets
                            	**type**\:  :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply>`
                            
                            .. attribute:: confirm
                            
                            	DHCPV6 confirm packets
                            	**type**\:  :py:class:`Confirm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm>`
                            
                            .. attribute:: decline
                            
                            	DHCPV6 decline packets
                            	**type**\:  :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: renew
                            
                            	DHCPV6 renew packets
                            	**type**\:  :py:class:`Renew <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew>`
                            
                            .. attribute:: rebind
                            
                            	DHCPV6 rebind packets
                            	**type**\:  :py:class:`Rebind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind>`
                            
                            .. attribute:: release
                            
                            	DHCPV6 release packets
                            	**type**\:  :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: reconfig
                            
                            	DHCPV6 reconfig packets
                            	**type**\:  :py:class:`Reconfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig>`
                            
                            .. attribute:: inform
                            
                            	DHCPV6 inform packets
                            	**type**\:  :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: relay_forward
                            
                            	DHCPV6 relay forward packets
                            	**type**\:  :py:class:`RelayForward <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward>`
                            
                            .. attribute:: relay_reply
                            
                            	DHCPV6 relay reply packets
                            	**type**\:  :py:class:`RelayReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply>`
                            
                            .. attribute:: lease_query
                            
                            	DHCPV6 lease query packets
                            	**type**\:  :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_query_reply
                            
                            	DHCPV6 lease query reply packets
                            	**type**\:  :py:class:`LeaseQueryReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply>`
                            
                            .. attribute:: lease_query_done
                            
                            	DHCPV6 lease query done packets
                            	**type**\:  :py:class:`LeaseQueryDone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone>`
                            
                            .. attribute:: lease_query_data
                            
                            	DHCPV6 lease query data packets
                            	**type**\:  :py:class:`LeaseQueryData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("solicit", ("solicit", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit)), ("advertise", ("advertise", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise)), ("request", ("request", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request)), ("reply", ("reply", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply)), ("confirm", ("confirm", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm)), ("decline", ("decline", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline)), ("renew", ("renew", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew)), ("rebind", ("rebind", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind)), ("release", ("release", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release)), ("reconfig", ("reconfig", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig)), ("inform", ("inform", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform)), ("relay-forward", ("relay_forward", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward)), ("relay-reply", ("relay_reply", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply)), ("lease-query", ("lease_query", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery)), ("lease-query-reply", ("lease_query_reply", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply)), ("lease-query-done", ("lease_query_done", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone)), ("lease-query-data", ("lease_query_data", Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.solicit = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit()
                                self.solicit.parent = self
                                self._children_name_map["solicit"] = "solicit"
                                self._children_yang_names.add("solicit")

                                self.advertise = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise()
                                self.advertise.parent = self
                                self._children_name_map["advertise"] = "advertise"
                                self._children_yang_names.add("advertise")

                                self.request = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self._children_name_map["request"] = "request"
                                self._children_yang_names.add("request")

                                self.reply = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply()
                                self.reply.parent = self
                                self._children_name_map["reply"] = "reply"
                                self._children_yang_names.add("reply")

                                self.confirm = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm()
                                self.confirm.parent = self
                                self._children_name_map["confirm"] = "confirm"
                                self._children_yang_names.add("confirm")

                                self.decline = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self._children_name_map["decline"] = "decline"
                                self._children_yang_names.add("decline")

                                self.renew = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew()
                                self.renew.parent = self
                                self._children_name_map["renew"] = "renew"
                                self._children_yang_names.add("renew")

                                self.rebind = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind()
                                self.rebind.parent = self
                                self._children_name_map["rebind"] = "rebind"
                                self._children_yang_names.add("rebind")

                                self.release = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self._children_name_map["release"] = "release"
                                self._children_yang_names.add("release")

                                self.reconfig = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig()
                                self.reconfig.parent = self
                                self._children_name_map["reconfig"] = "reconfig"
                                self._children_yang_names.add("reconfig")

                                self.inform = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self._children_name_map["inform"] = "inform"
                                self._children_yang_names.add("inform")

                                self.relay_forward = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward()
                                self.relay_forward.parent = self
                                self._children_name_map["relay_forward"] = "relay-forward"
                                self._children_yang_names.add("relay-forward")

                                self.relay_reply = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply()
                                self.relay_reply.parent = self
                                self._children_name_map["relay_reply"] = "relay-reply"
                                self._children_yang_names.add("relay-reply")

                                self.lease_query = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self._children_name_map["lease_query"] = "lease-query"
                                self._children_yang_names.add("lease-query")

                                self.lease_query_reply = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply()
                                self.lease_query_reply.parent = self
                                self._children_name_map["lease_query_reply"] = "lease-query-reply"
                                self._children_yang_names.add("lease-query-reply")

                                self.lease_query_done = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone()
                                self.lease_query_done.parent = self
                                self._children_name_map["lease_query_done"] = "lease-query-done"
                                self._children_yang_names.add("lease-query-done")

                                self.lease_query_data = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData()
                                self.lease_query_data.parent = self
                                self._children_name_map["lease_query_data"] = "lease-query-data"
                                self._children_yang_names.add("lease-query-data")
                                self._segment_path = lambda: "statistics"


                            class Solicit(Entity):
                                """
                                DHCPV6 solicit packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit, self).__init__()

                                    self.yang_name = "solicit"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "solicit"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Advertise(Entity):
                                """
                                DHCPV6 advertise packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise, self).__init__()

                                    self.yang_name = "advertise"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "advertise"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Request(Entity):
                                """
                                DHCPV6 request packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request, self).__init__()

                                    self.yang_name = "request"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "request"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Reply(Entity):
                                """
                                DHCPV6 reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply, self).__init__()

                                    self.yang_name = "reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "reply"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Confirm(Entity):
                                """
                                DHCPV6 confirm packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm, self).__init__()

                                    self.yang_name = "confirm"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "confirm"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Decline(Entity):
                                """
                                DHCPV6 decline packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline, self).__init__()

                                    self.yang_name = "decline"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "decline"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Renew(Entity):
                                """
                                DHCPV6 renew packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew, self).__init__()

                                    self.yang_name = "renew"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "renew"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Rebind(Entity):
                                """
                                DHCPV6 rebind packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind, self).__init__()

                                    self.yang_name = "rebind"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "rebind"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Release(Entity):
                                """
                                DHCPV6 release packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release, self).__init__()

                                    self.yang_name = "release"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "release"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Reconfig(Entity):
                                """
                                DHCPV6 reconfig packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig, self).__init__()

                                    self.yang_name = "reconfig"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "reconfig"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Inform(Entity):
                                """
                                DHCPV6 inform packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform, self).__init__()

                                    self.yang_name = "inform"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "inform"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class RelayForward(Entity):
                                """
                                DHCPV6 relay forward packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward, self).__init__()

                                    self.yang_name = "relay-forward"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "relay-forward"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class RelayReply(Entity):
                                """
                                DHCPV6 relay reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply, self).__init__()

                                    self.yang_name = "relay-reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "relay-reply"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQuery(Entity):
                                """
                                DHCPV6 lease query packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery, self).__init__()

                                    self.yang_name = "lease-query"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQueryReply(Entity):
                                """
                                DHCPV6 lease query reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply, self).__init__()

                                    self.yang_name = "lease-query-reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query-reply"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQueryDone(Entity):
                                """
                                DHCPV6 lease query done packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone, self).__init__()

                                    self.yang_name = "lease-query-done"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query-done"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQueryData(Entity):
                                """
                                DHCPV6 lease query data packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData, self).__init__()

                                    self.yang_name = "lease-query-data"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query-data"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                class Profiles(Entity):
                    """
                    IPv6 DHCP proxy profile
                    
                    .. attribute:: profile
                    
                    	IPv6 DHCP proxy profile
                    	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Proxy.Profiles, self).__init__()

                        self.yang_name = "profiles"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("profile", ("profile", Dhcpv6.Nodes.Node.Proxy.Profiles.Profile))])
                        self._leafs = OrderedDict()

                        self.profile = YList(self)
                        self._segment_path = lambda: "profiles"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Profiles, [], name, value)


                    class Profile(Entity):
                        """
                        IPv6 DHCP proxy profile
                        
                        .. attribute:: profile_name  (key)
                        
                        	Profile name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: throttle_infos
                        
                        	DHCPV6 throttle table
                        	**type**\:  :py:class:`ThrottleInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos>`
                        
                        .. attribute:: info
                        
                        	IPv6 DHCP proxy profile Info
                        	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile, self).__init__()

                            self.yang_name = "profile"
                            self.yang_parent_name = "profiles"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['profile_name']
                            self._child_container_classes = OrderedDict([("throttle-infos", ("throttle_infos", Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos)), ("info", ("info", Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('profile_name', YLeaf(YType.str, 'profile-name')),
                            ])
                            self.profile_name = None

                            self.throttle_infos = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos()
                            self.throttle_infos.parent = self
                            self._children_name_map["throttle_infos"] = "throttle-infos"
                            self._children_yang_names.add("throttle-infos")

                            self.info = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info()
                            self.info.parent = self
                            self._children_name_map["info"] = "info"
                            self._children_yang_names.add("info")
                            self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile, ['profile_name'], name, value)


                        class ThrottleInfos(Entity):
                            """
                            DHCPV6 throttle table
                            
                            .. attribute:: throttle_info
                            
                            	IPv6 DHCP proxy profile Throttle Info
                            	**type**\: list of  		 :py:class:`ThrottleInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos, self).__init__()

                                self.yang_name = "throttle-infos"
                                self.yang_parent_name = "profile"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("throttle-info", ("throttle_info", Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo))])
                                self._leafs = OrderedDict()

                                self.throttle_info = YList(self)
                                self._segment_path = lambda: "throttle-infos"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos, [], name, value)


                            class ThrottleInfo(Entity):
                                """
                                IPv6 DHCP proxy profile Throttle Info
                                
                                .. attribute:: mac_address  (key)
                                
                                	MAC address
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: binding_chaddr
                                
                                	Client MAC address
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: ifname
                                
                                	DHCP access interface
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                .. attribute:: state
                                
                                	State of entry
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_left
                                
                                	Time Left in secs
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo, self).__init__()

                                    self.yang_name = "throttle-info"
                                    self.yang_parent_name = "throttle-infos"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mac_address']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mac_address', YLeaf(YType.str, 'mac-address')),
                                        ('binding_chaddr', YLeaf(YType.str, 'binding-chaddr')),
                                        ('ifname', YLeaf(YType.str, 'ifname')),
                                        ('state', YLeaf(YType.uint32, 'state')),
                                        ('time_left', YLeaf(YType.uint32, 'time-left')),
                                    ])
                                    self.mac_address = None
                                    self.binding_chaddr = None
                                    self.ifname = None
                                    self.state = None
                                    self.time_left = None
                                    self._segment_path = lambda: "throttle-info" + "[mac-address='" + str(self.mac_address) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo, ['mac_address', 'binding_chaddr', 'ifname', 'state', 'time_left'], name, value)


                        class Info(Entity):
                            """
                            IPv6 DHCP proxy profile Info
                            
                            .. attribute:: interface_id_references
                            
                            	Interface id references
                            	**type**\:  :py:class:`InterfaceIdReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences>`
                            
                            .. attribute:: vrf_references
                            
                            	VRF references
                            	**type**\:  :py:class:`VrfReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences>`
                            
                            .. attribute:: interface_references
                            
                            	Interface references
                            	**type**\:  :py:class:`InterfaceReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences>`
                            
                            .. attribute:: profile_name
                            
                            	Proxy profile name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            .. attribute:: remote_id
                            
                            	Remote id
                            	**type**\: str
                            
                            	**length:** 0..257
                            
                            .. attribute:: profile_link_address
                            
                            	Link address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: proxy_profile_linkaddress_from_ra_enable
                            
                            	LinkAddress From RA mesage
                            	**type**\: bool
                            
                            .. attribute:: profile_helper_address
                            
                            	Helper addresses
                            	**type**\: list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF names
                            	**type**\: list of str
                            
                            	**length:** 0..33
                            
                            .. attribute:: interface_name
                            
                            	Interface names
                            	**type**\: list of str
                            
                            	**length:** 0..65
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info, self).__init__()

                                self.yang_name = "info"
                                self.yang_parent_name = "profile"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("interface-id-references", ("interface_id_references", Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences)), ("vrf-references", ("vrf_references", Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences)), ("interface-references", ("interface_references", Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', YLeaf(YType.str, 'profile-name')),
                                    ('remote_id', YLeaf(YType.str, 'remote-id')),
                                    ('profile_link_address', YLeaf(YType.str, 'profile-link-address')),
                                    ('proxy_profile_linkaddress_from_ra_enable', YLeaf(YType.boolean, 'proxy-profile-linkaddress-from-ra-enable')),
                                    ('profile_helper_address', YLeafList(YType.str, 'profile-helper-address')),
                                    ('vrf_name', YLeafList(YType.str, 'vrf-name')),
                                    ('interface_name', YLeafList(YType.str, 'interface-name')),
                                ])
                                self.profile_name = None
                                self.remote_id = None
                                self.profile_link_address = None
                                self.proxy_profile_linkaddress_from_ra_enable = None
                                self.profile_helper_address = []
                                self.vrf_name = []
                                self.interface_name = []

                                self.interface_id_references = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences()
                                self.interface_id_references.parent = self
                                self._children_name_map["interface_id_references"] = "interface-id-references"
                                self._children_yang_names.add("interface-id-references")

                                self.vrf_references = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences()
                                self.vrf_references.parent = self
                                self._children_name_map["vrf_references"] = "vrf-references"
                                self._children_yang_names.add("vrf-references")

                                self.interface_references = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences()
                                self.interface_references.parent = self
                                self._children_name_map["interface_references"] = "interface-references"
                                self._children_yang_names.add("interface-references")
                                self._segment_path = lambda: "info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info, ['profile_name', 'remote_id', 'profile_link_address', 'proxy_profile_linkaddress_from_ra_enable', 'profile_helper_address', 'vrf_name', 'interface_name'], name, value)


                            class InterfaceIdReferences(Entity):
                                """
                                Interface id references
                                
                                .. attribute:: ipv6_dhcpv6d_proxy_iid_reference
                                
                                	ipv6 dhcpv6d proxy iid reference
                                	**type**\: list of  		 :py:class:`Ipv6Dhcpv6DProxyIidReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences, self).__init__()

                                    self.yang_name = "interface-id-references"
                                    self.yang_parent_name = "info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("ipv6-dhcpv6d-proxy-iid-reference", ("ipv6_dhcpv6d_proxy_iid_reference", Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference))])
                                    self._leafs = OrderedDict()

                                    self.ipv6_dhcpv6d_proxy_iid_reference = YList(self)
                                    self._segment_path = lambda: "interface-id-references"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences, [], name, value)


                                class Ipv6Dhcpv6DProxyIidReference(Entity):
                                    """
                                    ipv6 dhcpv6d proxy iid reference
                                    
                                    .. attribute:: proxy_iid_interface_name
                                    
                                    	Interface name for interface id
                                    	**type**\: str
                                    
                                    	**length:** 0..65
                                    
                                    .. attribute:: proxy_interface_id
                                    
                                    	Interface id
                                    	**type**\: str
                                    
                                    	**length:** 0..257
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference, self).__init__()

                                        self.yang_name = "ipv6-dhcpv6d-proxy-iid-reference"
                                        self.yang_parent_name = "interface-id-references"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('proxy_iid_interface_name', YLeaf(YType.str, 'proxy-iid-interface-name')),
                                            ('proxy_interface_id', YLeaf(YType.str, 'proxy-interface-id')),
                                        ])
                                        self.proxy_iid_interface_name = None
                                        self.proxy_interface_id = None
                                        self._segment_path = lambda: "ipv6-dhcpv6d-proxy-iid-reference"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference, ['proxy_iid_interface_name', 'proxy_interface_id'], name, value)


                            class VrfReferences(Entity):
                                """
                                VRF references
                                
                                .. attribute:: ipv6_dhcpv6d_proxy_vrf_reference
                                
                                	ipv6 dhcpv6d proxy vrf reference
                                	**type**\: list of  		 :py:class:`Ipv6Dhcpv6DProxyVrfReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences, self).__init__()

                                    self.yang_name = "vrf-references"
                                    self.yang_parent_name = "info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("ipv6-dhcpv6d-proxy-vrf-reference", ("ipv6_dhcpv6d_proxy_vrf_reference", Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference))])
                                    self._leafs = OrderedDict()

                                    self.ipv6_dhcpv6d_proxy_vrf_reference = YList(self)
                                    self._segment_path = lambda: "vrf-references"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences, [], name, value)


                                class Ipv6Dhcpv6DProxyVrfReference(Entity):
                                    """
                                    ipv6 dhcpv6d proxy vrf reference
                                    
                                    .. attribute:: proxy_reference_vrf_name
                                    
                                    	VRF name
                                    	**type**\: str
                                    
                                    	**length:** 0..33
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference, self).__init__()

                                        self.yang_name = "ipv6-dhcpv6d-proxy-vrf-reference"
                                        self.yang_parent_name = "vrf-references"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('proxy_reference_vrf_name', YLeaf(YType.str, 'proxy-reference-vrf-name')),
                                        ])
                                        self.proxy_reference_vrf_name = None
                                        self._segment_path = lambda: "ipv6-dhcpv6d-proxy-vrf-reference"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference, ['proxy_reference_vrf_name'], name, value)


                            class InterfaceReferences(Entity):
                                """
                                Interface references
                                
                                .. attribute:: ipv6_dhcpv6d_proxy_interface_reference
                                
                                	ipv6 dhcpv6d proxy interface reference
                                	**type**\: list of  		 :py:class:`Ipv6Dhcpv6DProxyInterfaceReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences, self).__init__()

                                    self.yang_name = "interface-references"
                                    self.yang_parent_name = "info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("ipv6-dhcpv6d-proxy-interface-reference", ("ipv6_dhcpv6d_proxy_interface_reference", Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference))])
                                    self._leafs = OrderedDict()

                                    self.ipv6_dhcpv6d_proxy_interface_reference = YList(self)
                                    self._segment_path = lambda: "interface-references"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences, [], name, value)


                                class Ipv6Dhcpv6DProxyInterfaceReference(Entity):
                                    """
                                    ipv6 dhcpv6d proxy interface reference
                                    
                                    .. attribute:: proxy_reference_interface_name
                                    
                                    	Interface name
                                    	**type**\: str
                                    
                                    	**length:** 0..65
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference, self).__init__()

                                        self.yang_name = "ipv6-dhcpv6d-proxy-interface-reference"
                                        self.yang_parent_name = "interface-references"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('proxy_reference_interface_name', YLeaf(YType.str, 'proxy-reference-interface-name')),
                                        ])
                                        self.proxy_reference_interface_name = None
                                        self._segment_path = lambda: "ipv6-dhcpv6d-proxy-interface-reference"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference, ['proxy_reference_interface_name'], name, value)


                class Interfaces(Entity):
                    """
                    DHCPV6 proxy interface
                    
                    .. attribute:: interface
                    
                    	IPv6 DHCP proxy interface
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Proxy.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("interface", ("interface", Dhcpv6.Nodes.Node.Proxy.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        IPv6 DHCP proxy interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: proxy_vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        .. attribute:: proxy_interface_mode
                        
                        	Mode of interface
                        	**type**\:  :py:class:`BagDhcpv6DSubMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DSubMode>`
                        
                        .. attribute:: is_proxy_interface_ambiguous
                        
                        	Is interface ambiguous
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: proxy_interface_profile_name
                        
                        	Name of profile attached to the interface
                        	**type**\: str
                        
                        	**length:** 0..65
                        
                        .. attribute:: proxy_interface_lease_limit_type
                        
                        	Lease limit type on interface
                        	**type**\:  :py:class:`LeaseLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.LeaseLimit>`
                        
                        .. attribute:: proxy_interface_lease_limits
                        
                        	Lease limit count on interface
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srg_role
                        
                        	DHCPv6 Interface SRG role
                        	**type**\:  :py:class:`BagDhcpv6DIntfSrgRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIntfSrgRole>`
                        
                        .. attribute:: serg_role
                        
                        	DHCPv6 Interface SERG role
                        	**type**\:  :py:class:`BagDhcpv6DIntfSergRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIntfSergRole>`
                        
                        .. attribute:: mac_throttle
                        
                        	Mac Throttle Status
                        	**type**\: bool
                        
                        .. attribute:: srg_vrf_name
                        
                        	SRG VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        .. attribute:: srgp2p
                        
                        	SRG P2P Status
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Proxy.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('proxy_vrf_name', YLeaf(YType.str, 'proxy-vrf-name')),
                                ('proxy_interface_mode', YLeaf(YType.enumeration, 'proxy-interface-mode')),
                                ('is_proxy_interface_ambiguous', YLeaf(YType.uint32, 'is-proxy-interface-ambiguous')),
                                ('proxy_interface_profile_name', YLeaf(YType.str, 'proxy-interface-profile-name')),
                                ('proxy_interface_lease_limit_type', YLeaf(YType.enumeration, 'proxy-interface-lease-limit-type')),
                                ('proxy_interface_lease_limits', YLeaf(YType.uint32, 'proxy-interface-lease-limits')),
                                ('srg_role', YLeaf(YType.enumeration, 'srg-role')),
                                ('serg_role', YLeaf(YType.enumeration, 'serg-role')),
                                ('mac_throttle', YLeaf(YType.boolean, 'mac-throttle')),
                                ('srg_vrf_name', YLeaf(YType.str, 'srg-vrf-name')),
                                ('srgp2p', YLeaf(YType.boolean, 'srgp2p')),
                            ])
                            self.interface_name = None
                            self.proxy_vrf_name = None
                            self.proxy_interface_mode = None
                            self.is_proxy_interface_ambiguous = None
                            self.proxy_interface_profile_name = None
                            self.proxy_interface_lease_limit_type = None
                            self.proxy_interface_lease_limits = None
                            self.srg_role = None
                            self.serg_role = None
                            self.mac_throttle = None
                            self.srg_vrf_name = None
                            self.srgp2p = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Interfaces.Interface, ['interface_name', 'proxy_vrf_name', 'proxy_interface_mode', 'is_proxy_interface_ambiguous', 'proxy_interface_profile_name', 'proxy_interface_lease_limit_type', 'proxy_interface_lease_limits', 'srg_role', 'serg_role', 'mac_throttle', 'srg_vrf_name', 'srgp2p'], name, value)


                class Statistics(Entity):
                    """
                    DHCPv6 proxy statistics
                    
                    .. attribute:: ipv6_dhcpv6d_proxy_stat
                    
                    	ipv6 dhcpv6d proxy stat
                    	**type**\: list of  		 :py:class:`Ipv6Dhcpv6DProxyStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Proxy.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("ipv6-dhcpv6d-proxy-stat", ("ipv6_dhcpv6d_proxy_stat", Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat))])
                        self._leafs = OrderedDict()

                        self.ipv6_dhcpv6d_proxy_stat = YList(self)
                        self._segment_path = lambda: "statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Statistics, [], name, value)


                    class Ipv6Dhcpv6DProxyStat(Entity):
                        """
                        ipv6 dhcpv6d proxy stat
                        
                        .. attribute:: statistics
                        
                        	Proxy statistics
                        	**type**\:  :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCPv6 L3 VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat, self).__init__()

                            self.yang_name = "ipv6-dhcpv6d-proxy-stat"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("statistics", ("statistics", Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ])
                            self.vrf_name = None

                            self.statistics = Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._children_yang_names.add("statistics")
                            self._segment_path = lambda: "ipv6-dhcpv6d-proxy-stat"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat, ['vrf_name'], name, value)


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

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "ipv6-dhcpv6d-proxy-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                    ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                    ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                ])
                                self.received_packets = None
                                self.transmitted_packets = None
                                self.dropped_packets = None
                                self._segment_path = lambda: "statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                class Binding(Entity):
                    """
                    DHCPV6 proxy bindings
                    
                    .. attribute:: clients
                    
                    	DHCPV6 proxy client bindings
                    	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients>`
                    
                    .. attribute:: summary
                    
                    	DHCPV6 proxy binding summary
                    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Summary>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Proxy.Binding, self).__init__()

                        self.yang_name = "binding"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("clients", ("clients", Dhcpv6.Nodes.Node.Proxy.Binding.Clients)), ("summary", ("summary", Dhcpv6.Nodes.Node.Proxy.Binding.Summary))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.clients = Dhcpv6.Nodes.Node.Proxy.Binding.Clients()
                        self.clients.parent = self
                        self._children_name_map["clients"] = "clients"
                        self._children_yang_names.add("clients")

                        self.summary = Dhcpv6.Nodes.Node.Proxy.Binding.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                        self._children_yang_names.add("summary")
                        self._segment_path = lambda: "binding"


                    class Clients(Entity):
                        """
                        DHCPV6 proxy client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCPV6 proxy binding
                        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Proxy.Binding.Clients, self).__init__()

                            self.yang_name = "clients"
                            self.yang_parent_name = "binding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("client", ("client", Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client))])
                            self._leafs = OrderedDict()

                            self.client = YList(self)
                            self._segment_path = lambda: "clients"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Binding.Clients, [], name, value)


                        class Client(Entity):
                            """
                            Single DHCPV6 proxy binding
                            
                            .. attribute:: client_id  (key)
                            
                            	Client ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: ia_id_pd
                            
                            	List of DHCPv6 IA\_ID/PDs
                            	**type**\:  :py:class:`IaIdPd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd>`
                            
                            .. attribute:: duid
                            
                            	Client DUID
                            	**type**\: str
                            
                            .. attribute:: client_flag
                            
                            	DHCPV6 client flag
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: subscriber_label
                            
                            	DHCPV6 subscriber label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_name
                            
                            	DHCPVV6 client/subscriber VRF name
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: mac_address
                            
                            	Client MAC address
                            	**type**\: str
                            
                            .. attribute:: ia_id_p_ds
                            
                            	Number of ia\_id/pd
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	DHCPV6 access interface to client
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: access_vrf_name
                            
                            	DHCPV6 access VRF name to client
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: proxy_binding_tags
                            
                            	DHCPV6 VLAN tag count
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: proxy_binding_outer_tag
                            
                            	DHCPV6 VLAN Outer VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_binding_inner_tag
                            
                            	DHCPV6 VLAN Inner VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: class_name
                            
                            	DHCPV6 class name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: pool_name
                            
                            	DHCPV6 pool name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: rx_remote_id
                            
                            	DHCPV6 received Remote ID
                            	**type**\: str
                            
                            	**length:** 0..771
                            
                            .. attribute:: tx_remote_id
                            
                            	DHCPV6 transmitted Remote ID
                            	**type**\: str
                            
                            	**length:** 0..771
                            
                            .. attribute:: rx_interface_id
                            
                            	DHCPV6 received Interface ID
                            	**type**\: str
                            
                            	**length:** 0..771
                            
                            .. attribute:: tx_interface_id
                            
                            	DHCPV6 transmitted Interface ID
                            	**type**\: str
                            
                            	**length:** 0..771
                            
                            .. attribute:: server_ipv6_address
                            
                            	DHCPV6 server IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: profile_name
                            
                            	DHCPV6 profile name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            .. attribute:: framed_ipv6_prefix
                            
                            	DHCPV6 framed ipv6 addess used by ND
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: framed_prefix_length
                            
                            	DHCPV6 framed ipv6 prefix length used by ND
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: is_nak_next_renew
                            
                            	Is true if DHCP next renew from client will be NAK'd
                            	**type**\: bool
                            
                            .. attribute:: srg_state
                            
                            	DHCPV6 SRG state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srg_intf_role
                            
                            	DHCPV6 SRG Intf Role
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srgp2p
                            
                            	SRG P2P Status
                            	**type**\: bool
                            
                            .. attribute:: srg_vrf_name
                            
                            	DHCPV6 SRG VRF NAME
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: serg_state
                            
                            	DHCPV6 SERG state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: serg_intf_role
                            
                            	DHCPV6 SERG Intf Role
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client, self).__init__()

                                self.yang_name = "client"
                                self.yang_parent_name = "clients"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['client_id']
                                self._child_container_classes = OrderedDict([("ia-id-pd", ("ia_id_pd", Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('client_id', YLeaf(YType.str, 'client-id')),
                                    ('duid', YLeaf(YType.str, 'duid')),
                                    ('client_flag', YLeaf(YType.uint32, 'client-flag')),
                                    ('subscriber_label', YLeaf(YType.uint32, 'subscriber-label')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('mac_address', YLeaf(YType.str, 'mac-address')),
                                    ('ia_id_p_ds', YLeaf(YType.uint32, 'ia-id-p-ds')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('access_vrf_name', YLeaf(YType.str, 'access-vrf-name')),
                                    ('proxy_binding_tags', YLeaf(YType.uint8, 'proxy-binding-tags')),
                                    ('proxy_binding_outer_tag', YLeaf(YType.uint32, 'proxy-binding-outer-tag')),
                                    ('proxy_binding_inner_tag', YLeaf(YType.uint32, 'proxy-binding-inner-tag')),
                                    ('class_name', YLeaf(YType.str, 'class-name')),
                                    ('pool_name', YLeaf(YType.str, 'pool-name')),
                                    ('rx_remote_id', YLeaf(YType.str, 'rx-remote-id')),
                                    ('tx_remote_id', YLeaf(YType.str, 'tx-remote-id')),
                                    ('rx_interface_id', YLeaf(YType.str, 'rx-interface-id')),
                                    ('tx_interface_id', YLeaf(YType.str, 'tx-interface-id')),
                                    ('server_ipv6_address', YLeaf(YType.str, 'server-ipv6-address')),
                                    ('profile_name', YLeaf(YType.str, 'profile-name')),
                                    ('framed_ipv6_prefix', YLeaf(YType.str, 'framed-ipv6-prefix')),
                                    ('framed_prefix_length', YLeaf(YType.uint8, 'framed-prefix-length')),
                                    ('is_nak_next_renew', YLeaf(YType.boolean, 'is-nak-next-renew')),
                                    ('srg_state', YLeaf(YType.uint32, 'srg-state')),
                                    ('srg_intf_role', YLeaf(YType.uint32, 'srg-intf-role')),
                                    ('srgp2p', YLeaf(YType.boolean, 'srgp2p')),
                                    ('srg_vrf_name', YLeaf(YType.str, 'srg-vrf-name')),
                                    ('serg_state', YLeaf(YType.uint32, 'serg-state')),
                                    ('serg_intf_role', YLeaf(YType.uint32, 'serg-intf-role')),
                                ])
                                self.client_id = None
                                self.duid = None
                                self.client_flag = None
                                self.subscriber_label = None
                                self.vrf_name = None
                                self.mac_address = None
                                self.ia_id_p_ds = None
                                self.interface_name = None
                                self.access_vrf_name = None
                                self.proxy_binding_tags = None
                                self.proxy_binding_outer_tag = None
                                self.proxy_binding_inner_tag = None
                                self.class_name = None
                                self.pool_name = None
                                self.rx_remote_id = None
                                self.tx_remote_id = None
                                self.rx_interface_id = None
                                self.tx_interface_id = None
                                self.server_ipv6_address = None
                                self.profile_name = None
                                self.framed_ipv6_prefix = None
                                self.framed_prefix_length = None
                                self.is_nak_next_renew = None
                                self.srg_state = None
                                self.srg_intf_role = None
                                self.srgp2p = None
                                self.srg_vrf_name = None
                                self.serg_state = None
                                self.serg_intf_role = None

                                self.ia_id_pd = Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd()
                                self.ia_id_pd.parent = self
                                self._children_name_map["ia_id_pd"] = "ia-id-pd"
                                self._children_yang_names.add("ia-id-pd")
                                self._segment_path = lambda: "client" + "[client-id='" + str(self.client_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client, ['client_id', 'duid', 'client_flag', 'subscriber_label', 'vrf_name', 'mac_address', 'ia_id_p_ds', 'interface_name', 'access_vrf_name', 'proxy_binding_tags', 'proxy_binding_outer_tag', 'proxy_binding_inner_tag', 'class_name', 'pool_name', 'rx_remote_id', 'tx_remote_id', 'rx_interface_id', 'tx_interface_id', 'server_ipv6_address', 'profile_name', 'framed_ipv6_prefix', 'framed_prefix_length', 'is_nak_next_renew', 'srg_state', 'srg_intf_role', 'srgp2p', 'srg_vrf_name', 'serg_state', 'serg_intf_role'], name, value)


                            class IaIdPd(Entity):
                                """
                                List of DHCPv6 IA\_ID/PDs
                                
                                .. attribute:: bag_dhcpv6d_ia_id_pd_info
                                
                                	bag dhcpv6d ia id pd info
                                	**type**\: list of  		 :py:class:`BagDhcpv6DIaIdPdInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd, self).__init__()

                                    self.yang_name = "ia-id-pd"
                                    self.yang_parent_name = "client"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("bag-dhcpv6d-ia-id-pd-info", ("bag_dhcpv6d_ia_id_pd_info", Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo))])
                                    self._leafs = OrderedDict()

                                    self.bag_dhcpv6d_ia_id_pd_info = YList(self)
                                    self._segment_path = lambda: "ia-id-pd"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd, [], name, value)


                                class BagDhcpv6DIaIdPdInfo(Entity):
                                    """
                                    bag dhcpv6d ia id pd info
                                    
                                    .. attribute:: addresses
                                    
                                    	List of addresses in this IA
                                    	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses>`
                                    
                                    .. attribute:: ia_type
                                    
                                    	IA type
                                    	**type**\:  :py:class:`BagDhcpv6DIaId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIaId>`
                                    
                                    .. attribute:: ia_id
                                    
                                    	IA\_ID of this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: flags
                                    
                                    	FSM Flag for this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_address
                                    
                                    	Total address in this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\:  :py:class:`BagDhcpv6DFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DFsmState>`
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo, self).__init__()

                                        self.yang_name = "bag-dhcpv6d-ia-id-pd-info"
                                        self.yang_parent_name = "ia-id-pd"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("addresses", ("addresses", Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ia_type', YLeaf(YType.enumeration, 'ia-type')),
                                            ('ia_id', YLeaf(YType.uint32, 'ia-id')),
                                            ('flags', YLeaf(YType.uint32, 'flags')),
                                            ('total_address', YLeaf(YType.uint16, 'total-address')),
                                            ('state', YLeaf(YType.enumeration, 'state')),
                                        ])
                                        self.ia_type = None
                                        self.ia_id = None
                                        self.flags = None
                                        self.total_address = None
                                        self.state = None

                                        self.addresses = Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses()
                                        self.addresses.parent = self
                                        self._children_name_map["addresses"] = "addresses"
                                        self._children_yang_names.add("addresses")
                                        self._segment_path = lambda: "bag-dhcpv6d-ia-id-pd-info"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo, ['ia_type', 'ia_id', 'flags', 'total_address', 'state'], name, value)


                                    class Addresses(Entity):
                                        """
                                        List of addresses in this IA
                                        
                                        .. attribute:: bag_dhcpv6d_addr_attrb
                                        
                                        	bag dhcpv6d addr attrb
                                        	**type**\: list of  		 :py:class:`BagDhcpv6DAddrAttrb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb>`
                                        
                                        

                                        """

                                        _prefix = 'ipv6-new-dhcpv6d-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses, self).__init__()

                                            self.yang_name = "addresses"
                                            self.yang_parent_name = "bag-dhcpv6d-ia-id-pd-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("bag-dhcpv6d-addr-attrb", ("bag_dhcpv6d_addr_attrb", Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb))])
                                            self._leafs = OrderedDict()

                                            self.bag_dhcpv6d_addr_attrb = YList(self)
                                            self._segment_path = lambda: "addresses"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses, [], name, value)


                                        class BagDhcpv6DAddrAttrb(Entity):
                                            """
                                            bag dhcpv6d addr attrb
                                            
                                            .. attribute:: prefix
                                            
                                            	IPv6 prefix
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: prefix_length
                                            
                                            	Prefix length
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
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
                                            
                                            

                                            """

                                            _prefix = 'ipv6-new-dhcpv6d-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb, self).__init__()

                                                self.yang_name = "bag-dhcpv6d-addr-attrb"
                                                self.yang_parent_name = "addresses"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('prefix', YLeaf(YType.str, 'prefix')),
                                                    ('prefix_length', YLeaf(YType.uint8, 'prefix-length')),
                                                    ('lease_time', YLeaf(YType.uint32, 'lease-time')),
                                                    ('remaining_lease_time', YLeaf(YType.uint32, 'remaining-lease-time')),
                                                ])
                                                self.prefix = None
                                                self.prefix_length = None
                                                self.lease_time = None
                                                self.remaining_lease_time = None
                                                self._segment_path = lambda: "bag-dhcpv6d-addr-attrb"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb, ['prefix', 'prefix_length', 'lease_time', 'remaining_lease_time'], name, value)


                    class Summary(Entity):
                        """
                        DHCPV6 proxy binding summary
                        
                        .. attribute:: iana
                        
                        	IANA proxy binding summary
                        	**type**\:  :py:class:`Iana <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana>`
                        
                        .. attribute:: iapd
                        
                        	IAPD proxy binding summary
                        	**type**\:  :py:class:`Iapd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd>`
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Proxy.Binding.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "binding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("iana", ("iana", Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana)), ("iapd", ("iapd", Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('clients', YLeaf(YType.uint32, 'clients')),
                            ])
                            self.clients = None

                            self.iana = Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana()
                            self.iana.parent = self
                            self._children_name_map["iana"] = "iana"
                            self._children_yang_names.add("iana")

                            self.iapd = Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd()
                            self.iapd.parent = self
                            self._children_name_map["iapd"] = "iapd"
                            self._children_yang_names.add("iapd")
                            self._segment_path = lambda: "summary"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Binding.Summary, ['clients'], name, value)


                        class Iana(Entity):
                            """
                            IANA proxy binding summary
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free prefix(ND)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: msg_waiting_clients
                            
                            	Number of clients waiting for a message from the client/server
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting on iedge to subscriber session
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting on RIB response
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana, self).__init__()

                                self.yang_name = "iana"
                                self.yang_parent_name = "summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('initializing_clients', YLeaf(YType.uint32, 'initializing-clients')),
                                    ('dpm_waiting_clients', YLeaf(YType.uint32, 'dpm-waiting-clients')),
                                    ('daps_waiting_clients', YLeaf(YType.uint32, 'daps-waiting-clients')),
                                    ('msg_waiting_clients', YLeaf(YType.uint32, 'msg-waiting-clients')),
                                    ('iedge_waiting_clients', YLeaf(YType.uint32, 'iedge-waiting-clients')),
                                    ('rib_waiting_clients', YLeaf(YType.uint32, 'rib-waiting-clients')),
                                    ('bound_clients', YLeaf(YType.uint32, 'bound-clients')),
                                ])
                                self.initializing_clients = None
                                self.dpm_waiting_clients = None
                                self.daps_waiting_clients = None
                                self.msg_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.rib_waiting_clients = None
                                self.bound_clients = None
                                self._segment_path = lambda: "iana"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana, ['initializing_clients', 'dpm_waiting_clients', 'daps_waiting_clients', 'msg_waiting_clients', 'iedge_waiting_clients', 'rib_waiting_clients', 'bound_clients'], name, value)


                        class Iapd(Entity):
                            """
                            IAPD proxy binding summary
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free prefix(ND)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: msg_waiting_clients
                            
                            	Number of clients waiting for a message from the client/server
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting on iedge to subscriber session
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting on RIB response
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd, self).__init__()

                                self.yang_name = "iapd"
                                self.yang_parent_name = "summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('initializing_clients', YLeaf(YType.uint32, 'initializing-clients')),
                                    ('dpm_waiting_clients', YLeaf(YType.uint32, 'dpm-waiting-clients')),
                                    ('daps_waiting_clients', YLeaf(YType.uint32, 'daps-waiting-clients')),
                                    ('msg_waiting_clients', YLeaf(YType.uint32, 'msg-waiting-clients')),
                                    ('iedge_waiting_clients', YLeaf(YType.uint32, 'iedge-waiting-clients')),
                                    ('rib_waiting_clients', YLeaf(YType.uint32, 'rib-waiting-clients')),
                                    ('bound_clients', YLeaf(YType.uint32, 'bound-clients')),
                                ])
                                self.initializing_clients = None
                                self.dpm_waiting_clients = None
                                self.daps_waiting_clients = None
                                self.msg_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.rib_waiting_clients = None
                                self.bound_clients = None
                                self._segment_path = lambda: "iapd"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd, ['initializing_clients', 'dpm_waiting_clients', 'daps_waiting_clients', 'msg_waiting_clients', 'iedge_waiting_clients', 'rib_waiting_clients', 'bound_clients'], name, value)


            class Base(Entity):
                """
                IPv6 DHCP Base
                
                .. attribute:: database
                
                	DHCP database
                	**type**\:  :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Base.Database>`
                
                .. attribute:: addr_bindings
                
                	IPv6 DHCP Base Binding
                	**type**\:  :py:class:`AddrBindings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Base.AddrBindings>`
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dhcpv6.Nodes.Node.Base, self).__init__()

                    self.yang_name = "base"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("database", ("database", Dhcpv6.Nodes.Node.Base.Database)), ("addr-bindings", ("addr_bindings", Dhcpv6.Nodes.Node.Base.AddrBindings))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.database = Dhcpv6.Nodes.Node.Base.Database()
                    self.database.parent = self
                    self._children_name_map["database"] = "database"
                    self._children_yang_names.add("database")

                    self.addr_bindings = Dhcpv6.Nodes.Node.Base.AddrBindings()
                    self.addr_bindings.parent = self
                    self._children_name_map["addr_bindings"] = "addr-bindings"
                    self._children_yang_names.add("addr-bindings")
                    self._segment_path = lambda: "base"


                class Database(Entity):
                    """
                    DHCP database
                    
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

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Base.Database, self).__init__()

                        self.yang_name = "database"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('configured', YLeaf(YType.boolean, 'configured')),
                            ('version', YLeaf(YType.uint32, 'version')),
                            ('full_file_write_interval', YLeaf(YType.uint32, 'full-file-write-interval')),
                            ('last_full_write_file_name', YLeaf(YType.str, 'last-full-write-file-name')),
                            ('last_full_write_time', YLeaf(YType.uint32, 'last-full-write-time')),
                            ('full_file_write_count', YLeaf(YType.uint32, 'full-file-write-count')),
                            ('failed_full_file_write_count', YLeaf(YType.uint32, 'failed-full-file-write-count')),
                            ('full_file_record_count', YLeaf(YType.uint32, 'full-file-record-count')),
                            ('last_full_file_write_error_timestamp', YLeaf(YType.uint32, 'last-full-file-write-error-timestamp')),
                            ('incremental_file_write_interval', YLeaf(YType.uint32, 'incremental-file-write-interval')),
                            ('last_incremental_write_file_name', YLeaf(YType.str, 'last-incremental-write-file-name')),
                            ('last_incremental_write_time', YLeaf(YType.uint32, 'last-incremental-write-time')),
                            ('incremental_file_write_count', YLeaf(YType.uint32, 'incremental-file-write-count')),
                            ('failed_incremental_file_write_count', YLeaf(YType.uint32, 'failed-incremental-file-write-count')),
                            ('incremental_file_record_count', YLeaf(YType.uint32, 'incremental-file-record-count')),
                            ('last_incremental_file_write_error_timestamp', YLeaf(YType.uint32, 'last-incremental-file-write-error-timestamp')),
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

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Base.Database, ['configured', 'version', 'full_file_write_interval', 'last_full_write_file_name', 'last_full_write_time', 'full_file_write_count', 'failed_full_file_write_count', 'full_file_record_count', 'last_full_file_write_error_timestamp', 'incremental_file_write_interval', 'last_incremental_write_file_name', 'last_incremental_write_time', 'incremental_file_write_count', 'failed_incremental_file_write_count', 'incremental_file_record_count', 'last_incremental_file_write_error_timestamp'], name, value)


                class AddrBindings(Entity):
                    """
                    IPv6 DHCP Base Binding
                    
                    .. attribute:: addr_binding
                    
                    	DHCPv6 base stats debug
                    	**type**\: list of  		 :py:class:`AddrBinding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Base.AddrBindings.AddrBinding>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Base.AddrBindings, self).__init__()

                        self.yang_name = "addr-bindings"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("addr-binding", ("addr_binding", Dhcpv6.Nodes.Node.Base.AddrBindings.AddrBinding))])
                        self._leafs = OrderedDict()

                        self.addr_binding = YList(self)
                        self._segment_path = lambda: "addr-bindings"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Base.AddrBindings, [], name, value)


                    class AddrBinding(Entity):
                        """
                        DHCPv6 base stats debug
                        
                        .. attribute:: addr_string  (key)
                        
                        	Address String
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: mac_address
                        
                        	DHCPV6 client MAC address
                        	**type**\: str
                        
                        .. attribute:: vrf_name
                        
                        	DHCPV6 client/subscriber VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        .. attribute:: server_vrf_name
                        
                        	DHCPV6 server VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        .. attribute:: ipv6_address
                        
                        	DHCPV6 IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: server_ipv6_address
                        
                        	DHCPV6 server IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: reply_server_ipv6_address
                        
                        	DHCPV6 reply server IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
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
                        
                        	DHCPV6 client state
                        	**type**\:  :py:class:`BagDhcpv6DFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DFsmState>`
                        
                        .. attribute:: interface_name
                        
                        	DHCPV6 access interface to client
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: access_vrf_name
                        
                        	DHCPV6 access interface VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        .. attribute:: base_binding_tags
                        
                        	DHCPV6 VLAN tag count
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: base_binding_outer_tag
                        
                        	DHCPV6 VLAN Outer VLAN
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: base_binding_inner_tag
                        
                        	DHCPV6 VLAN Inner VLAN
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: profile_name
                        
                        	DHCPV6 profile name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: is_nak_next_renew
                        
                        	Is true if DHCPV6 next renew from client will be NAK'd
                        	**type**\: bool
                        
                        .. attribute:: subscriber_label
                        
                        	DHCPV6 subscriber label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: old_subscriber_label
                        
                        	DHCPV6 old subscriber label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_client_duid
                        
                        	DHCPV6 received client DUID
                        	**type**\: str
                        
                        	**length:** 0..771
                        
                        .. attribute:: tx_client_uid
                        
                        	DHCPV6 transmitted client DUID
                        	**type**\: str
                        
                        	**length:** 0..771
                        
                        .. attribute:: rx_remote_id
                        
                        	DHCPV6 received Remote ID
                        	**type**\: str
                        
                        	**length:** 0..771
                        
                        .. attribute:: tx_remote_id
                        
                        	DHCPV6 transmitted Remote ID
                        	**type**\: str
                        
                        	**length:** 0..771
                        
                        .. attribute:: rx_interface_id
                        
                        	DHCPV6 received Interface ID
                        	**type**\: str
                        
                        	**length:** 0..771
                        
                        .. attribute:: tx_interface_id
                        
                        	DHCPV6 transmitted Interface ID
                        	**type**\: str
                        
                        	**length:** 0..771
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Base.AddrBindings.AddrBinding, self).__init__()

                            self.yang_name = "addr-binding"
                            self.yang_parent_name = "addr-bindings"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['addr_string']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('addr_string', YLeaf(YType.str, 'addr-string')),
                                ('mac_address', YLeaf(YType.str, 'mac-address')),
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                ('server_vrf_name', YLeaf(YType.str, 'server-vrf-name')),
                                ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                                ('server_ipv6_address', YLeaf(YType.str, 'server-ipv6-address')),
                                ('reply_server_ipv6_address', YLeaf(YType.str, 'reply-server-ipv6-address')),
                                ('lease_time', YLeaf(YType.uint32, 'lease-time')),
                                ('remaining_lease_time', YLeaf(YType.uint32, 'remaining-lease-time')),
                                ('state', YLeaf(YType.enumeration, 'state')),
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('access_vrf_name', YLeaf(YType.str, 'access-vrf-name')),
                                ('base_binding_tags', YLeaf(YType.uint8, 'base-binding-tags')),
                                ('base_binding_outer_tag', YLeaf(YType.uint32, 'base-binding-outer-tag')),
                                ('base_binding_inner_tag', YLeaf(YType.uint32, 'base-binding-inner-tag')),
                                ('profile_name', YLeaf(YType.str, 'profile-name')),
                                ('is_nak_next_renew', YLeaf(YType.boolean, 'is-nak-next-renew')),
                                ('subscriber_label', YLeaf(YType.uint32, 'subscriber-label')),
                                ('old_subscriber_label', YLeaf(YType.uint32, 'old-subscriber-label')),
                                ('rx_client_duid', YLeaf(YType.str, 'rx-client-duid')),
                                ('tx_client_uid', YLeaf(YType.str, 'tx-client-uid')),
                                ('rx_remote_id', YLeaf(YType.str, 'rx-remote-id')),
                                ('tx_remote_id', YLeaf(YType.str, 'tx-remote-id')),
                                ('rx_interface_id', YLeaf(YType.str, 'rx-interface-id')),
                                ('tx_interface_id', YLeaf(YType.str, 'tx-interface-id')),
                            ])
                            self.addr_string = None
                            self.mac_address = None
                            self.vrf_name = None
                            self.server_vrf_name = None
                            self.ipv6_address = None
                            self.server_ipv6_address = None
                            self.reply_server_ipv6_address = None
                            self.lease_time = None
                            self.remaining_lease_time = None
                            self.state = None
                            self.interface_name = None
                            self.access_vrf_name = None
                            self.base_binding_tags = None
                            self.base_binding_outer_tag = None
                            self.base_binding_inner_tag = None
                            self.profile_name = None
                            self.is_nak_next_renew = None
                            self.subscriber_label = None
                            self.old_subscriber_label = None
                            self.rx_client_duid = None
                            self.tx_client_uid = None
                            self.rx_remote_id = None
                            self.tx_remote_id = None
                            self.rx_interface_id = None
                            self.tx_interface_id = None
                            self._segment_path = lambda: "addr-binding" + "[addr-string='" + str(self.addr_string) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Base.AddrBindings.AddrBinding, ['addr_string', 'mac_address', 'vrf_name', 'server_vrf_name', 'ipv6_address', 'server_ipv6_address', 'reply_server_ipv6_address', 'lease_time', 'remaining_lease_time', 'state', 'interface_name', 'access_vrf_name', 'base_binding_tags', 'base_binding_outer_tag', 'base_binding_inner_tag', 'profile_name', 'is_nak_next_renew', 'subscriber_label', 'old_subscriber_label', 'rx_client_duid', 'tx_client_uid', 'rx_remote_id', 'tx_remote_id', 'rx_interface_id', 'tx_interface_id'], name, value)


            class Server(Entity):
                """
                IPv6 DHCP server operational data
                
                .. attribute:: binding
                
                	DHCPV6 server bindings
                	**type**\:  :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding>`
                
                .. attribute:: vrfs
                
                	DHCPV6 server list of VRF names
                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs>`
                
                .. attribute:: profiles
                
                	IPv6 DHCP server profile
                	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles>`
                
                .. attribute:: interfaces
                
                	DHCPV6 server interface
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Interfaces>`
                
                .. attribute:: statistics
                
                	DHCPv6 server statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Statistics>`
                
                .. attribute:: binding_options
                
                	DHCPv6 server binding with options
                	**type**\:  :py:class:`BindingOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.BindingOptions>`
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dhcpv6.Nodes.Node.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("binding", ("binding", Dhcpv6.Nodes.Node.Server.Binding)), ("vrfs", ("vrfs", Dhcpv6.Nodes.Node.Server.Vrfs)), ("profiles", ("profiles", Dhcpv6.Nodes.Node.Server.Profiles)), ("interfaces", ("interfaces", Dhcpv6.Nodes.Node.Server.Interfaces)), ("statistics", ("statistics", Dhcpv6.Nodes.Node.Server.Statistics)), ("binding-options", ("binding_options", Dhcpv6.Nodes.Node.Server.BindingOptions))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.binding = Dhcpv6.Nodes.Node.Server.Binding()
                    self.binding.parent = self
                    self._children_name_map["binding"] = "binding"
                    self._children_yang_names.add("binding")

                    self.vrfs = Dhcpv6.Nodes.Node.Server.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                    self._children_yang_names.add("vrfs")

                    self.profiles = Dhcpv6.Nodes.Node.Server.Profiles()
                    self.profiles.parent = self
                    self._children_name_map["profiles"] = "profiles"
                    self._children_yang_names.add("profiles")

                    self.interfaces = Dhcpv6.Nodes.Node.Server.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")

                    self.statistics = Dhcpv6.Nodes.Node.Server.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")

                    self.binding_options = Dhcpv6.Nodes.Node.Server.BindingOptions()
                    self.binding_options.parent = self
                    self._children_name_map["binding_options"] = "binding-options"
                    self._children_yang_names.add("binding-options")
                    self._segment_path = lambda: "server"


                class Binding(Entity):
                    """
                    DHCPV6 server bindings
                    
                    .. attribute:: summary
                    
                    	DHCPV6 server binding summary
                    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Summary>`
                    
                    .. attribute:: clients
                    
                    	DHCPV6 server client bindings
                    	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Server.Binding, self).__init__()

                        self.yang_name = "binding"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("summary", ("summary", Dhcpv6.Nodes.Node.Server.Binding.Summary)), ("clients", ("clients", Dhcpv6.Nodes.Node.Server.Binding.Clients))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.summary = Dhcpv6.Nodes.Node.Server.Binding.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                        self._children_yang_names.add("summary")

                        self.clients = Dhcpv6.Nodes.Node.Server.Binding.Clients()
                        self.clients.parent = self
                        self._children_name_map["clients"] = "clients"
                        self._children_yang_names.add("clients")
                        self._segment_path = lambda: "binding"


                    class Summary(Entity):
                        """
                        DHCPV6 server binding summary
                        
                        .. attribute:: iana
                        
                        	IANA server binding summary
                        	**type**\:  :py:class:`Iana <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana>`
                        
                        .. attribute:: iapd
                        
                        	IAPD server binding summary
                        	**type**\:  :py:class:`Iapd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd>`
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Server.Binding.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "binding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("iana", ("iana", Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana)), ("iapd", ("iapd", Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('clients', YLeaf(YType.uint32, 'clients')),
                            ])
                            self.clients = None

                            self.iana = Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana()
                            self.iana.parent = self
                            self._children_name_map["iana"] = "iana"
                            self._children_yang_names.add("iana")

                            self.iapd = Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd()
                            self.iapd.parent = self
                            self._children_name_map["iapd"] = "iapd"
                            self._children_yang_names.add("iapd")
                            self._segment_path = lambda: "summary"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Server.Binding.Summary, ['clients'], name, value)


                        class Iana(Entity):
                            """
                            IANA server binding summary
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free addr/prefix
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_waiting_clients
                            
                            	Number of clients waiting for a request from the client
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting for iedge for the session
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting for RIB response
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana, self).__init__()

                                self.yang_name = "iana"
                                self.yang_parent_name = "summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('initializing_clients', YLeaf(YType.uint32, 'initializing-clients')),
                                    ('dpm_waiting_clients', YLeaf(YType.uint32, 'dpm-waiting-clients')),
                                    ('daps_waiting_clients', YLeaf(YType.uint32, 'daps-waiting-clients')),
                                    ('request_waiting_clients', YLeaf(YType.uint32, 'request-waiting-clients')),
                                    ('iedge_waiting_clients', YLeaf(YType.uint32, 'iedge-waiting-clients')),
                                    ('rib_waiting_clients', YLeaf(YType.uint32, 'rib-waiting-clients')),
                                    ('bound_clients', YLeaf(YType.uint32, 'bound-clients')),
                                ])
                                self.initializing_clients = None
                                self.dpm_waiting_clients = None
                                self.daps_waiting_clients = None
                                self.request_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.rib_waiting_clients = None
                                self.bound_clients = None
                                self._segment_path = lambda: "iana"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana, ['initializing_clients', 'dpm_waiting_clients', 'daps_waiting_clients', 'request_waiting_clients', 'iedge_waiting_clients', 'rib_waiting_clients', 'bound_clients'], name, value)


                        class Iapd(Entity):
                            """
                            IAPD server binding summary
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free addr/prefix
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_waiting_clients
                            
                            	Number of clients waiting for a request from the client
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting for iedge for the session
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting for RIB response
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd, self).__init__()

                                self.yang_name = "iapd"
                                self.yang_parent_name = "summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('initializing_clients', YLeaf(YType.uint32, 'initializing-clients')),
                                    ('dpm_waiting_clients', YLeaf(YType.uint32, 'dpm-waiting-clients')),
                                    ('daps_waiting_clients', YLeaf(YType.uint32, 'daps-waiting-clients')),
                                    ('request_waiting_clients', YLeaf(YType.uint32, 'request-waiting-clients')),
                                    ('iedge_waiting_clients', YLeaf(YType.uint32, 'iedge-waiting-clients')),
                                    ('rib_waiting_clients', YLeaf(YType.uint32, 'rib-waiting-clients')),
                                    ('bound_clients', YLeaf(YType.uint32, 'bound-clients')),
                                ])
                                self.initializing_clients = None
                                self.dpm_waiting_clients = None
                                self.daps_waiting_clients = None
                                self.request_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.rib_waiting_clients = None
                                self.bound_clients = None
                                self._segment_path = lambda: "iapd"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd, ['initializing_clients', 'dpm_waiting_clients', 'daps_waiting_clients', 'request_waiting_clients', 'iedge_waiting_clients', 'rib_waiting_clients', 'bound_clients'], name, value)


                    class Clients(Entity):
                        """
                        DHCPV6 server client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCPV6 server binding
                        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Server.Binding.Clients, self).__init__()

                            self.yang_name = "clients"
                            self.yang_parent_name = "binding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("client", ("client", Dhcpv6.Nodes.Node.Server.Binding.Clients.Client))])
                            self._leafs = OrderedDict()

                            self.client = YList(self)
                            self._segment_path = lambda: "clients"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Server.Binding.Clients, [], name, value)


                        class Client(Entity):
                            """
                            Single DHCPV6 server binding
                            
                            .. attribute:: client_id  (key)
                            
                            	Client ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: ia_id_pd
                            
                            	List of DHCPv6 IA\_ID/PDs
                            	**type**\:  :py:class:`IaIdPd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd>`
                            
                            .. attribute:: duid
                            
                            	Client DUID
                            	**type**\: str
                            
                            .. attribute:: client_id_xr
                            
                            	Client unique identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: client_flag
                            
                            	DHCPV6 client flag
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: subscriber_label
                            
                            	DHCPV6 subscriber label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_name
                            
                            	DHCPVV6 client/subscriber VRF name
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: mac_address
                            
                            	Client MAC address
                            	**type**\: str
                            
                            .. attribute:: ia_id_p_ds
                            
                            	Number of ia\_id/pd
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: link_local_address
                            
                            	DHCPV6 IPv6 client link local address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: interface_name
                            
                            	DHCPV6 access interface to client
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: access_vrf_name
                            
                            	DHCPV6 access VRF name to client
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: server_binding_tags
                            
                            	DHCPV6 VLAN tag count
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: server_binding_outer_tag
                            
                            	DHCPV6 VLAN Outer VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: server_binding_inner_tag
                            
                            	DHCPV6 VLAN Inner VLAN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pool_name
                            
                            	DHCPV6 pool name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: profile_name
                            
                            	DHCPV6 profile name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: framed_ipv6_prefix
                            
                            	DHCPV6 framed ipv6 addess used by ND
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: framed_prefix_length
                            
                            	DHCPV6 framed ipv6 prefix length used by ND
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: class_name
                            
                            	DHCPV6 class name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: rx_remote_id
                            
                            	DHCPV6 received Remote ID
                            	**type**\: str
                            
                            	**length:** 0..771
                            
                            .. attribute:: rx_interface_id
                            
                            	DHCPV6 received Interface ID
                            	**type**\: str
                            
                            	**length:** 0..771
                            
                            .. attribute:: prefix_pool_name
                            
                            	DHCPV6 server prefix pool name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: address_pool_name
                            
                            	DHCPV6 server address pool name
                            	**type**\: str
                            
                            	**length:** 0..64
                            
                            .. attribute:: dns_server_count
                            
                            	DNS server count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_nak_next_renew
                            
                            	Is true if DHCPv6 next renew from client will be NAK'd
                            	**type**\: bool
                            
                            .. attribute:: srg_state
                            
                            	DHCPV6 SRG state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srg_intf_role
                            
                            	DHCPV6 SRG Intf Role
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srgp2p
                            
                            	SRG P2P Status
                            	**type**\: bool
                            
                            .. attribute:: srg_vrf_name
                            
                            	DHCPV6 SRG VRF NAME
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: sesrg_state
                            
                            	DHCPV6 SERG state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: serg_intf_role
                            
                            	DHCPV6 SERG Intf Role
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Server.Binding.Clients.Client, self).__init__()

                                self.yang_name = "client"
                                self.yang_parent_name = "clients"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['client_id']
                                self._child_container_classes = OrderedDict([("ia-id-pd", ("ia_id_pd", Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('client_id', YLeaf(YType.str, 'client-id')),
                                    ('duid', YLeaf(YType.str, 'duid')),
                                    ('client_id_xr', YLeaf(YType.uint32, 'client-id-xr')),
                                    ('client_flag', YLeaf(YType.uint32, 'client-flag')),
                                    ('subscriber_label', YLeaf(YType.uint32, 'subscriber-label')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('mac_address', YLeaf(YType.str, 'mac-address')),
                                    ('ia_id_p_ds', YLeaf(YType.uint32, 'ia-id-p-ds')),
                                    ('link_local_address', YLeaf(YType.str, 'link-local-address')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('access_vrf_name', YLeaf(YType.str, 'access-vrf-name')),
                                    ('server_binding_tags', YLeaf(YType.uint8, 'server-binding-tags')),
                                    ('server_binding_outer_tag', YLeaf(YType.uint32, 'server-binding-outer-tag')),
                                    ('server_binding_inner_tag', YLeaf(YType.uint32, 'server-binding-inner-tag')),
                                    ('pool_name', YLeaf(YType.str, 'pool-name')),
                                    ('profile_name', YLeaf(YType.str, 'profile-name')),
                                    ('framed_ipv6_prefix', YLeaf(YType.str, 'framed-ipv6-prefix')),
                                    ('framed_prefix_length', YLeaf(YType.uint8, 'framed-prefix-length')),
                                    ('class_name', YLeaf(YType.str, 'class-name')),
                                    ('rx_remote_id', YLeaf(YType.str, 'rx-remote-id')),
                                    ('rx_interface_id', YLeaf(YType.str, 'rx-interface-id')),
                                    ('prefix_pool_name', YLeaf(YType.str, 'prefix-pool-name')),
                                    ('address_pool_name', YLeaf(YType.str, 'address-pool-name')),
                                    ('dns_server_count', YLeaf(YType.uint32, 'dns-server-count')),
                                    ('is_nak_next_renew', YLeaf(YType.boolean, 'is-nak-next-renew')),
                                    ('srg_state', YLeaf(YType.uint32, 'srg-state')),
                                    ('srg_intf_role', YLeaf(YType.uint32, 'srg-intf-role')),
                                    ('srgp2p', YLeaf(YType.boolean, 'srgp2p')),
                                    ('srg_vrf_name', YLeaf(YType.str, 'srg-vrf-name')),
                                    ('sesrg_state', YLeaf(YType.uint32, 'sesrg-state')),
                                    ('serg_intf_role', YLeaf(YType.uint32, 'serg-intf-role')),
                                ])
                                self.client_id = None
                                self.duid = None
                                self.client_id_xr = None
                                self.client_flag = None
                                self.subscriber_label = None
                                self.vrf_name = None
                                self.mac_address = None
                                self.ia_id_p_ds = None
                                self.link_local_address = None
                                self.interface_name = None
                                self.access_vrf_name = None
                                self.server_binding_tags = None
                                self.server_binding_outer_tag = None
                                self.server_binding_inner_tag = None
                                self.pool_name = None
                                self.profile_name = None
                                self.framed_ipv6_prefix = None
                                self.framed_prefix_length = None
                                self.class_name = None
                                self.rx_remote_id = None
                                self.rx_interface_id = None
                                self.prefix_pool_name = None
                                self.address_pool_name = None
                                self.dns_server_count = None
                                self.is_nak_next_renew = None
                                self.srg_state = None
                                self.srg_intf_role = None
                                self.srgp2p = None
                                self.srg_vrf_name = None
                                self.sesrg_state = None
                                self.serg_intf_role = None

                                self.ia_id_pd = Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd()
                                self.ia_id_pd.parent = self
                                self._children_name_map["ia_id_pd"] = "ia-id-pd"
                                self._children_yang_names.add("ia-id-pd")
                                self._segment_path = lambda: "client" + "[client-id='" + str(self.client_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Server.Binding.Clients.Client, ['client_id', 'duid', 'client_id_xr', 'client_flag', 'subscriber_label', 'vrf_name', 'mac_address', 'ia_id_p_ds', 'link_local_address', 'interface_name', 'access_vrf_name', 'server_binding_tags', 'server_binding_outer_tag', 'server_binding_inner_tag', 'pool_name', 'profile_name', 'framed_ipv6_prefix', 'framed_prefix_length', 'class_name', 'rx_remote_id', 'rx_interface_id', 'prefix_pool_name', 'address_pool_name', 'dns_server_count', 'is_nak_next_renew', 'srg_state', 'srg_intf_role', 'srgp2p', 'srg_vrf_name', 'sesrg_state', 'serg_intf_role'], name, value)


                            class IaIdPd(Entity):
                                """
                                List of DHCPv6 IA\_ID/PDs
                                
                                .. attribute:: bag_dhcpv6d_ia_id_pd_info
                                
                                	bag dhcpv6d ia id pd info
                                	**type**\: list of  		 :py:class:`BagDhcpv6DIaIdPdInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd, self).__init__()

                                    self.yang_name = "ia-id-pd"
                                    self.yang_parent_name = "client"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("bag-dhcpv6d-ia-id-pd-info", ("bag_dhcpv6d_ia_id_pd_info", Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo))])
                                    self._leafs = OrderedDict()

                                    self.bag_dhcpv6d_ia_id_pd_info = YList(self)
                                    self._segment_path = lambda: "ia-id-pd"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd, [], name, value)


                                class BagDhcpv6DIaIdPdInfo(Entity):
                                    """
                                    bag dhcpv6d ia id pd info
                                    
                                    .. attribute:: addresses
                                    
                                    	List of addresses in this IA
                                    	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses>`
                                    
                                    .. attribute:: ia_type
                                    
                                    	IA type
                                    	**type**\:  :py:class:`BagDhcpv6DIaId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIaId>`
                                    
                                    .. attribute:: ia_id
                                    
                                    	IA\_ID of this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: flags
                                    
                                    	FSM Flag for this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_address
                                    
                                    	Total address in this IA
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\:  :py:class:`BagDhcpv6DFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DFsmState>`
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo, self).__init__()

                                        self.yang_name = "bag-dhcpv6d-ia-id-pd-info"
                                        self.yang_parent_name = "ia-id-pd"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("addresses", ("addresses", Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ia_type', YLeaf(YType.enumeration, 'ia-type')),
                                            ('ia_id', YLeaf(YType.uint32, 'ia-id')),
                                            ('flags', YLeaf(YType.uint32, 'flags')),
                                            ('total_address', YLeaf(YType.uint16, 'total-address')),
                                            ('state', YLeaf(YType.enumeration, 'state')),
                                        ])
                                        self.ia_type = None
                                        self.ia_id = None
                                        self.flags = None
                                        self.total_address = None
                                        self.state = None

                                        self.addresses = Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses()
                                        self.addresses.parent = self
                                        self._children_name_map["addresses"] = "addresses"
                                        self._children_yang_names.add("addresses")
                                        self._segment_path = lambda: "bag-dhcpv6d-ia-id-pd-info"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo, ['ia_type', 'ia_id', 'flags', 'total_address', 'state'], name, value)


                                    class Addresses(Entity):
                                        """
                                        List of addresses in this IA
                                        
                                        .. attribute:: bag_dhcpv6d_addr_attrb
                                        
                                        	bag dhcpv6d addr attrb
                                        	**type**\: list of  		 :py:class:`BagDhcpv6DAddrAttrb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb>`
                                        
                                        

                                        """

                                        _prefix = 'ipv6-new-dhcpv6d-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses, self).__init__()

                                            self.yang_name = "addresses"
                                            self.yang_parent_name = "bag-dhcpv6d-ia-id-pd-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("bag-dhcpv6d-addr-attrb", ("bag_dhcpv6d_addr_attrb", Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb))])
                                            self._leafs = OrderedDict()

                                            self.bag_dhcpv6d_addr_attrb = YList(self)
                                            self._segment_path = lambda: "addresses"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses, [], name, value)


                                        class BagDhcpv6DAddrAttrb(Entity):
                                            """
                                            bag dhcpv6d addr attrb
                                            
                                            .. attribute:: prefix
                                            
                                            	IPv6 prefix
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: prefix_length
                                            
                                            	Prefix length
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
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
                                            
                                            

                                            """

                                            _prefix = 'ipv6-new-dhcpv6d-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb, self).__init__()

                                                self.yang_name = "bag-dhcpv6d-addr-attrb"
                                                self.yang_parent_name = "addresses"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('prefix', YLeaf(YType.str, 'prefix')),
                                                    ('prefix_length', YLeaf(YType.uint8, 'prefix-length')),
                                                    ('lease_time', YLeaf(YType.uint32, 'lease-time')),
                                                    ('remaining_lease_time', YLeaf(YType.uint32, 'remaining-lease-time')),
                                                ])
                                                self.prefix = None
                                                self.prefix_length = None
                                                self.lease_time = None
                                                self.remaining_lease_time = None
                                                self._segment_path = lambda: "bag-dhcpv6d-addr-attrb"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb, ['prefix', 'prefix_length', 'lease_time', 'remaining_lease_time'], name, value)


                class Vrfs(Entity):
                    """
                    DHCPV6 server list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP server VRF name
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Server.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("vrf", ("vrf", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf))])
                        self._leafs = OrderedDict()

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs, [], name, value)


                    class Vrf(Entity):
                        """
                        IPv6 DHCP server VRF name
                        
                        .. attribute:: vrf_name  (key)
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv6 DHCP server statistics
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_container_classes = OrderedDict([("statistics", ("statistics", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ])
                            self.vrf_name = None

                            self.statistics = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._children_yang_names.add("statistics")
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf, ['vrf_name'], name, value)


                        class Statistics(Entity):
                            """
                            IPv6 DHCP server statistics
                            
                            .. attribute:: solicit
                            
                            	DHCPV6 solicit packets
                            	**type**\:  :py:class:`Solicit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit>`
                            
                            .. attribute:: advertise
                            
                            	DHCPV6 advertise packets
                            	**type**\:  :py:class:`Advertise <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise>`
                            
                            .. attribute:: request
                            
                            	DHCPV6 request packets
                            	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: reply
                            
                            	DHCPV6 reply packets
                            	**type**\:  :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply>`
                            
                            .. attribute:: confirm
                            
                            	DHCPV6 confirm packets
                            	**type**\:  :py:class:`Confirm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm>`
                            
                            .. attribute:: decline
                            
                            	DHCPV6 decline packets
                            	**type**\:  :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: renew
                            
                            	DHCPV6 renew packets
                            	**type**\:  :py:class:`Renew <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew>`
                            
                            .. attribute:: rebind
                            
                            	DHCPV6 rebind packets
                            	**type**\:  :py:class:`Rebind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind>`
                            
                            .. attribute:: release
                            
                            	DHCPV6 release packets
                            	**type**\:  :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: reconfig
                            
                            	DHCPV6 reconfig packets
                            	**type**\:  :py:class:`Reconfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig>`
                            
                            .. attribute:: inform
                            
                            	DHCPV6 inform packets
                            	**type**\:  :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: relay_forward
                            
                            	DHCPV6 relay forward packets
                            	**type**\:  :py:class:`RelayForward <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward>`
                            
                            .. attribute:: relay_reply
                            
                            	DHCPV6 relay reply packets
                            	**type**\:  :py:class:`RelayReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply>`
                            
                            .. attribute:: lease_query
                            
                            	DHCPV6 lease query packets
                            	**type**\:  :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_query_reply
                            
                            	DHCPV6 lease query reply packets
                            	**type**\:  :py:class:`LeaseQueryReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply>`
                            
                            .. attribute:: lease_query_done
                            
                            	DHCPV6 lease query done packets
                            	**type**\:  :py:class:`LeaseQueryDone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone>`
                            
                            .. attribute:: lease_query_data
                            
                            	DHCPV6 lease query data packets
                            	**type**\:  :py:class:`LeaseQueryData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("solicit", ("solicit", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit)), ("advertise", ("advertise", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise)), ("request", ("request", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request)), ("reply", ("reply", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply)), ("confirm", ("confirm", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm)), ("decline", ("decline", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline)), ("renew", ("renew", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew)), ("rebind", ("rebind", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind)), ("release", ("release", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release)), ("reconfig", ("reconfig", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig)), ("inform", ("inform", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform)), ("relay-forward", ("relay_forward", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward)), ("relay-reply", ("relay_reply", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply)), ("lease-query", ("lease_query", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery)), ("lease-query-reply", ("lease_query_reply", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply)), ("lease-query-done", ("lease_query_done", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone)), ("lease-query-data", ("lease_query_data", Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.solicit = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit()
                                self.solicit.parent = self
                                self._children_name_map["solicit"] = "solicit"
                                self._children_yang_names.add("solicit")

                                self.advertise = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise()
                                self.advertise.parent = self
                                self._children_name_map["advertise"] = "advertise"
                                self._children_yang_names.add("advertise")

                                self.request = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self._children_name_map["request"] = "request"
                                self._children_yang_names.add("request")

                                self.reply = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply()
                                self.reply.parent = self
                                self._children_name_map["reply"] = "reply"
                                self._children_yang_names.add("reply")

                                self.confirm = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm()
                                self.confirm.parent = self
                                self._children_name_map["confirm"] = "confirm"
                                self._children_yang_names.add("confirm")

                                self.decline = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self._children_name_map["decline"] = "decline"
                                self._children_yang_names.add("decline")

                                self.renew = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew()
                                self.renew.parent = self
                                self._children_name_map["renew"] = "renew"
                                self._children_yang_names.add("renew")

                                self.rebind = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind()
                                self.rebind.parent = self
                                self._children_name_map["rebind"] = "rebind"
                                self._children_yang_names.add("rebind")

                                self.release = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self._children_name_map["release"] = "release"
                                self._children_yang_names.add("release")

                                self.reconfig = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig()
                                self.reconfig.parent = self
                                self._children_name_map["reconfig"] = "reconfig"
                                self._children_yang_names.add("reconfig")

                                self.inform = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self._children_name_map["inform"] = "inform"
                                self._children_yang_names.add("inform")

                                self.relay_forward = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward()
                                self.relay_forward.parent = self
                                self._children_name_map["relay_forward"] = "relay-forward"
                                self._children_yang_names.add("relay-forward")

                                self.relay_reply = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply()
                                self.relay_reply.parent = self
                                self._children_name_map["relay_reply"] = "relay-reply"
                                self._children_yang_names.add("relay-reply")

                                self.lease_query = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self._children_name_map["lease_query"] = "lease-query"
                                self._children_yang_names.add("lease-query")

                                self.lease_query_reply = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply()
                                self.lease_query_reply.parent = self
                                self._children_name_map["lease_query_reply"] = "lease-query-reply"
                                self._children_yang_names.add("lease-query-reply")

                                self.lease_query_done = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone()
                                self.lease_query_done.parent = self
                                self._children_name_map["lease_query_done"] = "lease-query-done"
                                self._children_yang_names.add("lease-query-done")

                                self.lease_query_data = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData()
                                self.lease_query_data.parent = self
                                self._children_name_map["lease_query_data"] = "lease-query-data"
                                self._children_yang_names.add("lease-query-data")
                                self._segment_path = lambda: "statistics"


                            class Solicit(Entity):
                                """
                                DHCPV6 solicit packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit, self).__init__()

                                    self.yang_name = "solicit"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "solicit"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Advertise(Entity):
                                """
                                DHCPV6 advertise packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise, self).__init__()

                                    self.yang_name = "advertise"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "advertise"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Request(Entity):
                                """
                                DHCPV6 request packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request, self).__init__()

                                    self.yang_name = "request"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "request"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Reply(Entity):
                                """
                                DHCPV6 reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply, self).__init__()

                                    self.yang_name = "reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "reply"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Confirm(Entity):
                                """
                                DHCPV6 confirm packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm, self).__init__()

                                    self.yang_name = "confirm"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "confirm"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Decline(Entity):
                                """
                                DHCPV6 decline packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline, self).__init__()

                                    self.yang_name = "decline"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "decline"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Renew(Entity):
                                """
                                DHCPV6 renew packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew, self).__init__()

                                    self.yang_name = "renew"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "renew"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Rebind(Entity):
                                """
                                DHCPV6 rebind packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind, self).__init__()

                                    self.yang_name = "rebind"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "rebind"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Release(Entity):
                                """
                                DHCPV6 release packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release, self).__init__()

                                    self.yang_name = "release"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "release"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Reconfig(Entity):
                                """
                                DHCPV6 reconfig packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig, self).__init__()

                                    self.yang_name = "reconfig"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "reconfig"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Inform(Entity):
                                """
                                DHCPV6 inform packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform, self).__init__()

                                    self.yang_name = "inform"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "inform"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class RelayForward(Entity):
                                """
                                DHCPV6 relay forward packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward, self).__init__()

                                    self.yang_name = "relay-forward"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "relay-forward"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class RelayReply(Entity):
                                """
                                DHCPV6 relay reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply, self).__init__()

                                    self.yang_name = "relay-reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "relay-reply"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQuery(Entity):
                                """
                                DHCPV6 lease query packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery, self).__init__()

                                    self.yang_name = "lease-query"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQueryReply(Entity):
                                """
                                DHCPV6 lease query reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply, self).__init__()

                                    self.yang_name = "lease-query-reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query-reply"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQueryDone(Entity):
                                """
                                DHCPV6 lease query done packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone, self).__init__()

                                    self.yang_name = "lease-query-done"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query-done"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQueryData(Entity):
                                """
                                DHCPV6 lease query data packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData, self).__init__()

                                    self.yang_name = "lease-query-data"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query-data"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                class Profiles(Entity):
                    """
                    IPv6 DHCP server profile
                    
                    .. attribute:: profile
                    
                    	IPv6 DHCP server profile
                    	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Server.Profiles, self).__init__()

                        self.yang_name = "profiles"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("profile", ("profile", Dhcpv6.Nodes.Node.Server.Profiles.Profile))])
                        self._leafs = OrderedDict()

                        self.profile = YList(self)
                        self._segment_path = lambda: "profiles"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Server.Profiles, [], name, value)


                    class Profile(Entity):
                        """
                        IPv6 DHCP server profile
                        
                        .. attribute:: profile_name  (key)
                        
                        	Profile name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: info
                        
                        	IPv6 DHCP server profile Info
                        	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info>`
                        
                        .. attribute:: throttle_infos
                        
                        	DHCPV6 throttle table
                        	**type**\:  :py:class:`ThrottleInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Server.Profiles.Profile, self).__init__()

                            self.yang_name = "profile"
                            self.yang_parent_name = "profiles"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['profile_name']
                            self._child_container_classes = OrderedDict([("info", ("info", Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info)), ("throttle-infos", ("throttle_infos", Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('profile_name', YLeaf(YType.str, 'profile-name')),
                            ])
                            self.profile_name = None

                            self.info = Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info()
                            self.info.parent = self
                            self._children_name_map["info"] = "info"
                            self._children_yang_names.add("info")

                            self.throttle_infos = Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos()
                            self.throttle_infos.parent = self
                            self._children_name_map["throttle_infos"] = "throttle-infos"
                            self._children_yang_names.add("throttle-infos")
                            self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Server.Profiles.Profile, ['profile_name'], name, value)


                        class Info(Entity):
                            """
                            IPv6 DHCP server profile Info
                            
                            .. attribute:: lease
                            
                            	Server lease time
                            	**type**\:  :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease>`
                            
                            .. attribute:: interface_references
                            
                            	Interface references
                            	**type**\:  :py:class:`InterfaceReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences>`
                            
                            .. attribute:: profile_name
                            
                            	Server profile name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            .. attribute:: domain_name
                            
                            	Server domain name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            .. attribute:: profile_dns
                            
                            	DNS address count
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: aftr_name
                            
                            	Server aftr name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            .. attribute:: framed_addr_pool_name
                            
                            	Server framed address pool name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            .. attribute:: delegated_prefix_pool_name
                            
                            	Server delegated prefix pool name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            .. attribute:: rapid_commit
                            
                            	Rapid Commit
                            	**type**\: bool
                            
                            .. attribute:: profile_dns_address
                            
                            	DNS addresses
                            	**type**\: list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info, self).__init__()

                                self.yang_name = "info"
                                self.yang_parent_name = "profile"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("lease", ("lease", Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease)), ("interface-references", ("interface_references", Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', YLeaf(YType.str, 'profile-name')),
                                    ('domain_name', YLeaf(YType.str, 'domain-name')),
                                    ('profile_dns', YLeaf(YType.uint8, 'profile-dns')),
                                    ('aftr_name', YLeaf(YType.str, 'aftr-name')),
                                    ('framed_addr_pool_name', YLeaf(YType.str, 'framed-addr-pool-name')),
                                    ('delegated_prefix_pool_name', YLeaf(YType.str, 'delegated-prefix-pool-name')),
                                    ('rapid_commit', YLeaf(YType.boolean, 'rapid-commit')),
                                    ('profile_dns_address', YLeafList(YType.str, 'profile-dns-address')),
                                ])
                                self.profile_name = None
                                self.domain_name = None
                                self.profile_dns = None
                                self.aftr_name = None
                                self.framed_addr_pool_name = None
                                self.delegated_prefix_pool_name = None
                                self.rapid_commit = None
                                self.profile_dns_address = []

                                self.lease = Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease()
                                self.lease.parent = self
                                self._children_name_map["lease"] = "lease"
                                self._children_yang_names.add("lease")

                                self.interface_references = Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences()
                                self.interface_references.parent = self
                                self._children_name_map["interface_references"] = "interface-references"
                                self._children_yang_names.add("interface-references")
                                self._segment_path = lambda: "info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info, ['profile_name', 'domain_name', 'profile_dns', 'aftr_name', 'framed_addr_pool_name', 'delegated_prefix_pool_name', 'rapid_commit', 'profile_dns_address'], name, value)


                            class Lease(Entity):
                                """
                                Server lease time
                                
                                .. attribute:: seconds
                                
                                	DHCPV6 client lease in seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: time
                                
                                	Time in format HH\:MM\:SS
                                	**type**\: str
                                
                                	**length:** 0..10
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease, self).__init__()

                                    self.yang_name = "lease"
                                    self.yang_parent_name = "info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('seconds', YLeaf(YType.uint32, 'seconds')),
                                        ('time', YLeaf(YType.str, 'time')),
                                    ])
                                    self.seconds = None
                                    self.time = None
                                    self._segment_path = lambda: "lease"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease, ['seconds', 'time'], name, value)


                            class InterfaceReferences(Entity):
                                """
                                Interface references
                                
                                .. attribute:: ipv6_dhcpv6d_server_interface_reference
                                
                                	ipv6 dhcpv6d server interface reference
                                	**type**\: list of  		 :py:class:`Ipv6Dhcpv6DServerInterfaceReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences, self).__init__()

                                    self.yang_name = "interface-references"
                                    self.yang_parent_name = "info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("ipv6-dhcpv6d-server-interface-reference", ("ipv6_dhcpv6d_server_interface_reference", Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference))])
                                    self._leafs = OrderedDict()

                                    self.ipv6_dhcpv6d_server_interface_reference = YList(self)
                                    self._segment_path = lambda: "interface-references"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences, [], name, value)


                                class Ipv6Dhcpv6DServerInterfaceReference(Entity):
                                    """
                                    ipv6 dhcpv6d server interface reference
                                    
                                    .. attribute:: server_reference_interface_name
                                    
                                    	Interface name
                                    	**type**\: str
                                    
                                    	**length:** 0..65
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference, self).__init__()

                                        self.yang_name = "ipv6-dhcpv6d-server-interface-reference"
                                        self.yang_parent_name = "interface-references"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('server_reference_interface_name', YLeaf(YType.str, 'server-reference-interface-name')),
                                        ])
                                        self.server_reference_interface_name = None
                                        self._segment_path = lambda: "ipv6-dhcpv6d-server-interface-reference"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference, ['server_reference_interface_name'], name, value)


                        class ThrottleInfos(Entity):
                            """
                            DHCPV6 throttle table
                            
                            .. attribute:: throttle_info
                            
                            	IPv6 DHCP server profile Throttle Info
                            	**type**\: list of  		 :py:class:`ThrottleInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos, self).__init__()

                                self.yang_name = "throttle-infos"
                                self.yang_parent_name = "profile"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("throttle-info", ("throttle_info", Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo))])
                                self._leafs = OrderedDict()

                                self.throttle_info = YList(self)
                                self._segment_path = lambda: "throttle-infos"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos, [], name, value)


                            class ThrottleInfo(Entity):
                                """
                                IPv6 DHCP server profile Throttle Info
                                
                                .. attribute:: mac_address  (key)
                                
                                	MAC address
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: binding_chaddr
                                
                                	Client MAC address
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: ifname
                                
                                	DHCP access interface
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                .. attribute:: state
                                
                                	State of entry
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_left
                                
                                	Time Left in secs
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo, self).__init__()

                                    self.yang_name = "throttle-info"
                                    self.yang_parent_name = "throttle-infos"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mac_address']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mac_address', YLeaf(YType.str, 'mac-address')),
                                        ('binding_chaddr', YLeaf(YType.str, 'binding-chaddr')),
                                        ('ifname', YLeaf(YType.str, 'ifname')),
                                        ('state', YLeaf(YType.uint32, 'state')),
                                        ('time_left', YLeaf(YType.uint32, 'time-left')),
                                    ])
                                    self.mac_address = None
                                    self.binding_chaddr = None
                                    self.ifname = None
                                    self.state = None
                                    self.time_left = None
                                    self._segment_path = lambda: "throttle-info" + "[mac-address='" + str(self.mac_address) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo, ['mac_address', 'binding_chaddr', 'ifname', 'state', 'time_left'], name, value)


                class Interfaces(Entity):
                    """
                    DHCPV6 server interface
                    
                    .. attribute:: interface
                    
                    	IPv6 DHCP server interface
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Server.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("interface", ("interface", Dhcpv6.Nodes.Node.Server.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Server.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        IPv6 DHCP server interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: server_vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        .. attribute:: server_interface_mode
                        
                        	Mode of interface
                        	**type**\:  :py:class:`BagDhcpv6DSubMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DSubMode>`
                        
                        .. attribute:: is_server_interface_ambiguous
                        
                        	Is interface ambiguous
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: server_interface_profile_name
                        
                        	Name of profile attached to the interface
                        	**type**\: str
                        
                        	**length:** 0..65
                        
                        .. attribute:: server_interface_lease_limit_type
                        
                        	Lease limit type on interface
                        	**type**\:  :py:class:`LeaseLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.LeaseLimit>`
                        
                        .. attribute:: server_interface_lease_limits
                        
                        	Lease limit count on interface
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srg_role
                        
                        	DHCPv6 Interface SRG role
                        	**type**\:  :py:class:`BagDhcpv6DIntfSrgRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIntfSrgRole>`
                        
                        .. attribute:: serg_role
                        
                        	DHCPv6 Interface SERG role
                        	**type**\:  :py:class:`BagDhcpv6DIntfSergRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIntfSergRole>`
                        
                        .. attribute:: mac_throttle
                        
                        	Mac Throttle Status
                        	**type**\: bool
                        
                        .. attribute:: srg_vrf_name
                        
                        	SRG VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        .. attribute:: srgp2p
                        
                        	SRG P2P Status
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Server.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('server_vrf_name', YLeaf(YType.str, 'server-vrf-name')),
                                ('server_interface_mode', YLeaf(YType.enumeration, 'server-interface-mode')),
                                ('is_server_interface_ambiguous', YLeaf(YType.uint32, 'is-server-interface-ambiguous')),
                                ('server_interface_profile_name', YLeaf(YType.str, 'server-interface-profile-name')),
                                ('server_interface_lease_limit_type', YLeaf(YType.enumeration, 'server-interface-lease-limit-type')),
                                ('server_interface_lease_limits', YLeaf(YType.uint32, 'server-interface-lease-limits')),
                                ('srg_role', YLeaf(YType.enumeration, 'srg-role')),
                                ('serg_role', YLeaf(YType.enumeration, 'serg-role')),
                                ('mac_throttle', YLeaf(YType.boolean, 'mac-throttle')),
                                ('srg_vrf_name', YLeaf(YType.str, 'srg-vrf-name')),
                                ('srgp2p', YLeaf(YType.boolean, 'srgp2p')),
                            ])
                            self.interface_name = None
                            self.server_vrf_name = None
                            self.server_interface_mode = None
                            self.is_server_interface_ambiguous = None
                            self.server_interface_profile_name = None
                            self.server_interface_lease_limit_type = None
                            self.server_interface_lease_limits = None
                            self.srg_role = None
                            self.serg_role = None
                            self.mac_throttle = None
                            self.srg_vrf_name = None
                            self.srgp2p = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Server.Interfaces.Interface, ['interface_name', 'server_vrf_name', 'server_interface_mode', 'is_server_interface_ambiguous', 'server_interface_profile_name', 'server_interface_lease_limit_type', 'server_interface_lease_limits', 'srg_role', 'serg_role', 'mac_throttle', 'srg_vrf_name', 'srgp2p'], name, value)


                class Statistics(Entity):
                    """
                    DHCPv6 server statistics
                    
                    .. attribute:: ipv6_dhcpv6d_server_stat
                    
                    	ipv6 dhcpv6d server stat
                    	**type**\: list of  		 :py:class:`Ipv6Dhcpv6DServerStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Server.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("ipv6-dhcpv6d-server-stat", ("ipv6_dhcpv6d_server_stat", Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat))])
                        self._leafs = OrderedDict()

                        self.ipv6_dhcpv6d_server_stat = YList(self)
                        self._segment_path = lambda: "statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Server.Statistics, [], name, value)


                    class Ipv6Dhcpv6DServerStat(Entity):
                        """
                        ipv6 dhcpv6d server stat
                        
                        .. attribute:: statistics
                        
                        	Server statistics
                        	**type**\:  :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCPv6 L3 VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat, self).__init__()

                            self.yang_name = "ipv6-dhcpv6d-server-stat"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("statistics", ("statistics", Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ])
                            self.vrf_name = None

                            self.statistics = Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._children_yang_names.add("statistics")
                            self._segment_path = lambda: "ipv6-dhcpv6d-server-stat"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat, ['vrf_name'], name, value)


                        class Statistics_(Entity):
                            """
                            Server statistics
                            
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

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "ipv6-dhcpv6d-server-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                    ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                    ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                ])
                                self.received_packets = None
                                self.transmitted_packets = None
                                self.dropped_packets = None
                                self._segment_path = lambda: "statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                class BindingOptions(Entity):
                    """
                    DHCPv6 server binding with options
                    
                    .. attribute:: mac_bind_options
                    
                    	DHCPv6 server binding from MAC address
                    	**type**\:  :py:class:`MacBindOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions>`
                    
                    .. attribute:: duid_bind_options
                    
                    	DHCPv6 server binding from DUID
                    	**type**\:  :py:class:`DuidBindOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Server.BindingOptions, self).__init__()

                        self.yang_name = "binding-options"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("mac-bind-options", ("mac_bind_options", Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions)), ("duid-bind-options", ("duid_bind_options", Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.mac_bind_options = Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions()
                        self.mac_bind_options.parent = self
                        self._children_name_map["mac_bind_options"] = "mac-bind-options"
                        self._children_yang_names.add("mac-bind-options")

                        self.duid_bind_options = Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions()
                        self.duid_bind_options.parent = self
                        self._children_name_map["duid_bind_options"] = "duid-bind-options"
                        self._children_yang_names.add("duid-bind-options")
                        self._segment_path = lambda: "binding-options"


                    class MacBindOptions(Entity):
                        """
                        DHCPv6 server binding from MAC address
                        
                        .. attribute:: mac_bind_option
                        
                        	DHCPv6 server binding with options
                        	**type**\: list of  		 :py:class:`MacBindOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions.MacBindOption>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions, self).__init__()

                            self.yang_name = "mac-bind-options"
                            self.yang_parent_name = "binding-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("mac-bind-option", ("mac_bind_option", Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions.MacBindOption))])
                            self._leafs = OrderedDict()

                            self.mac_bind_option = YList(self)
                            self._segment_path = lambda: "mac-bind-options"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions, [], name, value)


                        class MacBindOption(Entity):
                            """
                            DHCPv6 server binding with options
                            
                            .. attribute:: mac_address  (key)
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: mac_address_xr
                            
                            	Client MAC address
                            	**type**\: str
                            
                            .. attribute:: duid_xr
                            
                            	Client DUID
                            	**type**\: str
                            
                            .. attribute:: dns_count
                            
                            	DNS address count
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: opt17
                            
                            	Client Option 17 value
                            	**type**\: str
                            
                            .. attribute:: dns_address
                            
                            	DNS addresses
                            	**type**\: list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions.MacBindOption, self).__init__()

                                self.yang_name = "mac-bind-option"
                                self.yang_parent_name = "mac-bind-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['mac_address']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mac_address', YLeaf(YType.str, 'mac-address')),
                                    ('mac_address_xr', YLeaf(YType.str, 'mac-address-xr')),
                                    ('duid_xr', YLeaf(YType.str, 'duid-xr')),
                                    ('dns_count', YLeaf(YType.uint8, 'dns-count')),
                                    ('opt17', YLeaf(YType.str, 'opt17')),
                                    ('dns_address', YLeafList(YType.str, 'dns-address')),
                                ])
                                self.mac_address = None
                                self.mac_address_xr = None
                                self.duid_xr = None
                                self.dns_count = None
                                self.opt17 = None
                                self.dns_address = []
                                self._segment_path = lambda: "mac-bind-option" + "[mac-address='" + str(self.mac_address) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions.MacBindOption, ['mac_address', 'mac_address_xr', 'duid_xr', 'dns_count', 'opt17', 'dns_address'], name, value)


                    class DuidBindOptions(Entity):
                        """
                        DHCPv6 server binding from DUID
                        
                        .. attribute:: duid_bind_option
                        
                        	DHCPv6 server binding with options
                        	**type**\: list of  		 :py:class:`DuidBindOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions.DuidBindOption>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions, self).__init__()

                            self.yang_name = "duid-bind-options"
                            self.yang_parent_name = "binding-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("duid-bind-option", ("duid_bind_option", Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions.DuidBindOption))])
                            self._leafs = OrderedDict()

                            self.duid_bind_option = YList(self)
                            self._segment_path = lambda: "duid-bind-options"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions, [], name, value)


                        class DuidBindOption(Entity):
                            """
                            DHCPv6 server binding with options
                            
                            .. attribute:: duid  (key)
                            
                            	DUID of Binding
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: mac_address_xr
                            
                            	Client MAC address
                            	**type**\: str
                            
                            .. attribute:: duid_xr
                            
                            	Client DUID
                            	**type**\: str
                            
                            .. attribute:: dns_count
                            
                            	DNS address count
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: opt17
                            
                            	Client Option 17 value
                            	**type**\: str
                            
                            .. attribute:: dns_address
                            
                            	DNS addresses
                            	**type**\: list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions.DuidBindOption, self).__init__()

                                self.yang_name = "duid-bind-option"
                                self.yang_parent_name = "duid-bind-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['duid']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('duid', YLeaf(YType.str, 'duid')),
                                    ('mac_address_xr', YLeaf(YType.str, 'mac-address-xr')),
                                    ('duid_xr', YLeaf(YType.str, 'duid-xr')),
                                    ('dns_count', YLeaf(YType.uint8, 'dns-count')),
                                    ('opt17', YLeaf(YType.str, 'opt17')),
                                    ('dns_address', YLeafList(YType.str, 'dns-address')),
                                ])
                                self.duid = None
                                self.mac_address_xr = None
                                self.duid_xr = None
                                self.dns_count = None
                                self.opt17 = None
                                self.dns_address = []
                                self._segment_path = lambda: "duid-bind-option" + "[duid='" + str(self.duid) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions.DuidBindOption, ['duid', 'mac_address_xr', 'duid_xr', 'dns_count', 'opt17', 'dns_address'], name, value)


            class Relay(Entity):
                """
                IPv6 DHCP relay operational data
                
                .. attribute:: statistics
                
                	DHCPv6 relay statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Statistics>`
                
                .. attribute:: binding
                
                	DHCPV6 relay bindings
                	**type**\:  :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding>`
                
                .. attribute:: vrfs
                
                	DHCPV6 relay list of VRF names
                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs>`
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dhcpv6.Nodes.Node.Relay, self).__init__()

                    self.yang_name = "relay"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("statistics", ("statistics", Dhcpv6.Nodes.Node.Relay.Statistics)), ("binding", ("binding", Dhcpv6.Nodes.Node.Relay.Binding)), ("vrfs", ("vrfs", Dhcpv6.Nodes.Node.Relay.Vrfs))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.statistics = Dhcpv6.Nodes.Node.Relay.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")

                    self.binding = Dhcpv6.Nodes.Node.Relay.Binding()
                    self.binding.parent = self
                    self._children_name_map["binding"] = "binding"
                    self._children_yang_names.add("binding")

                    self.vrfs = Dhcpv6.Nodes.Node.Relay.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                    self._children_yang_names.add("vrfs")
                    self._segment_path = lambda: "relay"


                class Statistics(Entity):
                    """
                    DHCPv6 relay statistics
                    
                    .. attribute:: ipv6_dhcpv6d_relay_stat
                    
                    	ipv6 dhcpv6d relay stat
                    	**type**\: list of  		 :py:class:`Ipv6Dhcpv6DRelayStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Relay.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "relay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("ipv6-dhcpv6d-relay-stat", ("ipv6_dhcpv6d_relay_stat", Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat))])
                        self._leafs = OrderedDict()

                        self.ipv6_dhcpv6d_relay_stat = YList(self)
                        self._segment_path = lambda: "statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Statistics, [], name, value)


                    class Ipv6Dhcpv6DRelayStat(Entity):
                        """
                        ipv6 dhcpv6d relay stat
                        
                        .. attribute:: statistics
                        
                        	Relay statistics
                        	**type**\:  :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCPv6 L3 VRF name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat, self).__init__()

                            self.yang_name = "ipv6-dhcpv6d-relay-stat"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("statistics", ("statistics", Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ])
                            self.vrf_name = None

                            self.statistics = Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._children_yang_names.add("statistics")
                            self._segment_path = lambda: "ipv6-dhcpv6d-relay-stat"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat, ['vrf_name'], name, value)


                        class Statistics_(Entity):
                            """
                            Relay statistics
                            
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

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "ipv6-dhcpv6d-relay-stat"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                    ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                    ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                ])
                                self.received_packets = None
                                self.transmitted_packets = None
                                self.dropped_packets = None
                                self._segment_path = lambda: "statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                class Binding(Entity):
                    """
                    DHCPV6 relay bindings
                    
                    .. attribute:: summary
                    
                    	DHCPV6 relay binding summary
                    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding.Summary>`
                    
                    .. attribute:: clients
                    
                    	DHCPV6 relay client bindings
                    	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding.Clients>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Relay.Binding, self).__init__()

                        self.yang_name = "binding"
                        self.yang_parent_name = "relay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("summary", ("summary", Dhcpv6.Nodes.Node.Relay.Binding.Summary)), ("clients", ("clients", Dhcpv6.Nodes.Node.Relay.Binding.Clients))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.summary = Dhcpv6.Nodes.Node.Relay.Binding.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                        self._children_yang_names.add("summary")

                        self.clients = Dhcpv6.Nodes.Node.Relay.Binding.Clients()
                        self.clients.parent = self
                        self._children_name_map["clients"] = "clients"
                        self._children_yang_names.add("clients")
                        self._segment_path = lambda: "binding"


                    class Summary(Entity):
                        """
                        DHCPV6 relay binding summary
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Relay.Binding.Summary, self).__init__()

                            self.yang_name = "summary"
                            self.yang_parent_name = "binding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('clients', YLeaf(YType.uint32, 'clients')),
                            ])
                            self.clients = None
                            self._segment_path = lambda: "summary"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Binding.Summary, ['clients'], name, value)


                    class Clients(Entity):
                        """
                        DHCPV6 relay client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCPV6 relay binding
                        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Relay.Binding.Clients, self).__init__()

                            self.yang_name = "clients"
                            self.yang_parent_name = "binding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("client", ("client", Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client))])
                            self._leafs = OrderedDict()

                            self.client = YList(self)
                            self._segment_path = lambda: "clients"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Binding.Clients, [], name, value)


                        class Client(Entity):
                            """
                            Single DHCPV6 relay binding
                            
                            .. attribute:: client_id  (key)
                            
                            	Client ID
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: duid
                            
                            	Client DUID
                            	**type**\: str
                            
                            .. attribute:: client_id_xr
                            
                            	Client unique identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: prefix_length
                            
                            	length of prefix
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: prefix
                            
                            	DHCPV6 IPv6 Prefix allotted to client
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	DHCPv6 client/subscriber Vrf name
                            	**type**\: str
                            
                            	**length:** 0..33
                            
                            .. attribute:: lifetime
                            
                            	Client route lifetime
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rem_life_time
                            
                            	Client route remaining lifetime
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            .. attribute:: next_hop_addr
                            
                            	Next hop is our address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ia_id
                            
                            	IA\_ID of this IA
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: relay_profile_name
                            
                            	Relay Profile name
                            	**type**\: str
                            
                            	**length:** 0..65
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client, self).__init__()

                                self.yang_name = "client"
                                self.yang_parent_name = "clients"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['client_id']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('client_id', YLeaf(YType.str, 'client-id')),
                                    ('duid', YLeaf(YType.str, 'duid')),
                                    ('client_id_xr', YLeaf(YType.uint32, 'client-id-xr')),
                                    ('prefix_length', YLeaf(YType.uint8, 'prefix-length')),
                                    ('prefix', YLeaf(YType.str, 'prefix')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('lifetime', YLeaf(YType.uint32, 'lifetime')),
                                    ('rem_life_time', YLeaf(YType.uint32, 'rem-life-time')),
                                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                                    ('next_hop_addr', YLeaf(YType.str, 'next-hop-addr')),
                                    ('ia_id', YLeaf(YType.uint32, 'ia-id')),
                                    ('relay_profile_name', YLeaf(YType.str, 'relay-profile-name')),
                                ])
                                self.client_id = None
                                self.duid = None
                                self.client_id_xr = None
                                self.prefix_length = None
                                self.prefix = None
                                self.vrf_name = None
                                self.lifetime = None
                                self.rem_life_time = None
                                self.interface_name = None
                                self.next_hop_addr = None
                                self.ia_id = None
                                self.relay_profile_name = None
                                self._segment_path = lambda: "client" + "[client-id='" + str(self.client_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client, ['client_id', 'duid', 'client_id_xr', 'prefix_length', 'prefix', 'vrf_name', 'lifetime', 'rem_life_time', 'interface_name', 'next_hop_addr', 'ia_id', 'relay_profile_name'], name, value)


                class Vrfs(Entity):
                    """
                    DHCPV6 relay list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP relay VRF name
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dhcpv6.Nodes.Node.Relay.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "relay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("vrf", ("vrf", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf))])
                        self._leafs = OrderedDict()

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs, [], name, value)


                    class Vrf(Entity):
                        """
                        IPv6 DHCP relay VRF name
                        
                        .. attribute:: vrf_name  (key)
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv6 DHCP relay statistics
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_container_classes = OrderedDict([("statistics", ("statistics", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ])
                            self.vrf_name = None

                            self.statistics = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"
                            self._children_yang_names.add("statistics")
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf, ['vrf_name'], name, value)


                        class Statistics(Entity):
                            """
                            IPv6 DHCP relay statistics
                            
                            .. attribute:: solicit
                            
                            	DHCPV6 solicit packets
                            	**type**\:  :py:class:`Solicit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit>`
                            
                            .. attribute:: advertise
                            
                            	DHCPV6 advertise packets
                            	**type**\:  :py:class:`Advertise <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise>`
                            
                            .. attribute:: request
                            
                            	DHCPV6 request packets
                            	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: reply
                            
                            	DHCPV6 reply packets
                            	**type**\:  :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply>`
                            
                            .. attribute:: confirm
                            
                            	DHCPV6 confirm packets
                            	**type**\:  :py:class:`Confirm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm>`
                            
                            .. attribute:: decline
                            
                            	DHCPV6 decline packets
                            	**type**\:  :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: renew
                            
                            	DHCPV6 renew packets
                            	**type**\:  :py:class:`Renew <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew>`
                            
                            .. attribute:: rebind
                            
                            	DHCPV6 rebind packets
                            	**type**\:  :py:class:`Rebind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind>`
                            
                            .. attribute:: release
                            
                            	DHCPV6 release packets
                            	**type**\:  :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: reconfig
                            
                            	DHCPV6 reconfig packets
                            	**type**\:  :py:class:`Reconfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig>`
                            
                            .. attribute:: inform
                            
                            	DHCPV6 inform packets
                            	**type**\:  :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: relay_forward
                            
                            	DHCPV6 relay forward packets
                            	**type**\:  :py:class:`RelayForward <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward>`
                            
                            .. attribute:: relay_reply
                            
                            	DHCPV6 relay reply packets
                            	**type**\:  :py:class:`RelayReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply>`
                            
                            .. attribute:: lease_query
                            
                            	DHCPV6 lease query packets
                            	**type**\:  :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_query_reply
                            
                            	DHCPV6 lease query reply packets
                            	**type**\:  :py:class:`LeaseQueryReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply>`
                            
                            .. attribute:: lease_query_done
                            
                            	DHCPV6 lease query done packets
                            	**type**\:  :py:class:`LeaseQueryDone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone>`
                            
                            .. attribute:: lease_query_data
                            
                            	DHCPV6 lease query data packets
                            	**type**\:  :py:class:`LeaseQueryData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("solicit", ("solicit", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit)), ("advertise", ("advertise", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise)), ("request", ("request", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request)), ("reply", ("reply", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply)), ("confirm", ("confirm", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm)), ("decline", ("decline", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline)), ("renew", ("renew", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew)), ("rebind", ("rebind", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind)), ("release", ("release", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release)), ("reconfig", ("reconfig", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig)), ("inform", ("inform", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform)), ("relay-forward", ("relay_forward", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward)), ("relay-reply", ("relay_reply", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply)), ("lease-query", ("lease_query", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery)), ("lease-query-reply", ("lease_query_reply", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply)), ("lease-query-done", ("lease_query_done", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone)), ("lease-query-data", ("lease_query_data", Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.solicit = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit()
                                self.solicit.parent = self
                                self._children_name_map["solicit"] = "solicit"
                                self._children_yang_names.add("solicit")

                                self.advertise = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise()
                                self.advertise.parent = self
                                self._children_name_map["advertise"] = "advertise"
                                self._children_yang_names.add("advertise")

                                self.request = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self._children_name_map["request"] = "request"
                                self._children_yang_names.add("request")

                                self.reply = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply()
                                self.reply.parent = self
                                self._children_name_map["reply"] = "reply"
                                self._children_yang_names.add("reply")

                                self.confirm = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm()
                                self.confirm.parent = self
                                self._children_name_map["confirm"] = "confirm"
                                self._children_yang_names.add("confirm")

                                self.decline = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self._children_name_map["decline"] = "decline"
                                self._children_yang_names.add("decline")

                                self.renew = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew()
                                self.renew.parent = self
                                self._children_name_map["renew"] = "renew"
                                self._children_yang_names.add("renew")

                                self.rebind = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind()
                                self.rebind.parent = self
                                self._children_name_map["rebind"] = "rebind"
                                self._children_yang_names.add("rebind")

                                self.release = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self._children_name_map["release"] = "release"
                                self._children_yang_names.add("release")

                                self.reconfig = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig()
                                self.reconfig.parent = self
                                self._children_name_map["reconfig"] = "reconfig"
                                self._children_yang_names.add("reconfig")

                                self.inform = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self._children_name_map["inform"] = "inform"
                                self._children_yang_names.add("inform")

                                self.relay_forward = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward()
                                self.relay_forward.parent = self
                                self._children_name_map["relay_forward"] = "relay-forward"
                                self._children_yang_names.add("relay-forward")

                                self.relay_reply = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply()
                                self.relay_reply.parent = self
                                self._children_name_map["relay_reply"] = "relay-reply"
                                self._children_yang_names.add("relay-reply")

                                self.lease_query = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self._children_name_map["lease_query"] = "lease-query"
                                self._children_yang_names.add("lease-query")

                                self.lease_query_reply = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply()
                                self.lease_query_reply.parent = self
                                self._children_name_map["lease_query_reply"] = "lease-query-reply"
                                self._children_yang_names.add("lease-query-reply")

                                self.lease_query_done = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone()
                                self.lease_query_done.parent = self
                                self._children_name_map["lease_query_done"] = "lease-query-done"
                                self._children_yang_names.add("lease-query-done")

                                self.lease_query_data = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData()
                                self.lease_query_data.parent = self
                                self._children_name_map["lease_query_data"] = "lease-query-data"
                                self._children_yang_names.add("lease-query-data")
                                self._segment_path = lambda: "statistics"


                            class Solicit(Entity):
                                """
                                DHCPV6 solicit packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit, self).__init__()

                                    self.yang_name = "solicit"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "solicit"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Advertise(Entity):
                                """
                                DHCPV6 advertise packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise, self).__init__()

                                    self.yang_name = "advertise"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "advertise"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Request(Entity):
                                """
                                DHCPV6 request packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request, self).__init__()

                                    self.yang_name = "request"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "request"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Reply(Entity):
                                """
                                DHCPV6 reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply, self).__init__()

                                    self.yang_name = "reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "reply"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Confirm(Entity):
                                """
                                DHCPV6 confirm packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm, self).__init__()

                                    self.yang_name = "confirm"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "confirm"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Decline(Entity):
                                """
                                DHCPV6 decline packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline, self).__init__()

                                    self.yang_name = "decline"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "decline"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Renew(Entity):
                                """
                                DHCPV6 renew packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew, self).__init__()

                                    self.yang_name = "renew"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "renew"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Rebind(Entity):
                                """
                                DHCPV6 rebind packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind, self).__init__()

                                    self.yang_name = "rebind"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "rebind"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Release(Entity):
                                """
                                DHCPV6 release packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release, self).__init__()

                                    self.yang_name = "release"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "release"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Reconfig(Entity):
                                """
                                DHCPV6 reconfig packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig, self).__init__()

                                    self.yang_name = "reconfig"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "reconfig"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class Inform(Entity):
                                """
                                DHCPV6 inform packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform, self).__init__()

                                    self.yang_name = "inform"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "inform"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class RelayForward(Entity):
                                """
                                DHCPV6 relay forward packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward, self).__init__()

                                    self.yang_name = "relay-forward"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "relay-forward"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class RelayReply(Entity):
                                """
                                DHCPV6 relay reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply, self).__init__()

                                    self.yang_name = "relay-reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "relay-reply"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQuery(Entity):
                                """
                                DHCPV6 lease query packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery, self).__init__()

                                    self.yang_name = "lease-query"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQueryReply(Entity):
                                """
                                DHCPV6 lease query reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply, self).__init__()

                                    self.yang_name = "lease-query-reply"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query-reply"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQueryDone(Entity):
                                """
                                DHCPV6 lease query done packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone, self).__init__()

                                    self.yang_name = "lease-query-done"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query-done"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)


                            class LeaseQueryData(Entity):
                                """
                                DHCPV6 lease query data packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData, self).__init__()

                                    self.yang_name = "lease-query-data"
                                    self.yang_parent_name = "statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                        ('transmitted_packets', YLeaf(YType.uint64, 'transmitted-packets')),
                                        ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                    ])
                                    self.received_packets = None
                                    self.transmitted_packets = None
                                    self.dropped_packets = None
                                    self._segment_path = lambda: "lease-query-data"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData, ['received_packets', 'transmitted_packets', 'dropped_packets'], name, value)

    def clone_ptr(self):
        self._top_entity = Dhcpv6()
        return self._top_entity

