""" Cisco_IOS_XE_dhcp_oper 

This module contains a collection of YANG definitions
for DHCP Server and Client operational data.
Copyright (c) 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DhcpClientIdType(Enum):
    """
    DhcpClientIdType (Enum Class)

    DHCP Client id hardware types 

    .. data:: dhcp_htype_ethernet = 0

    	DHCP Client hardware type Ethernet

    .. data:: dhcp_htype_ieee802 = 1

    	DHCP Client hardware type 802

    .. data:: dhcp_htype_rfclimit = 2

    	DHCP Client hardware type RFCLIMIT

    .. data:: dhcp_htype_clientid = 3

    	DHCP Client hardware type CLIENTID

    """

    dhcp_htype_ethernet = Enum.YLeaf(0, "dhcp-htype-ethernet")

    dhcp_htype_ieee802 = Enum.YLeaf(1, "dhcp-htype-ieee802")

    dhcp_htype_rfclimit = Enum.YLeaf(2, "dhcp-htype-rfclimit")

    dhcp_htype_clientid = Enum.YLeaf(3, "dhcp-htype-clientid")


class DhcpClientState(Enum):
    """
    DhcpClientState (Enum Class)

    DHCP Client state

    .. data:: dhcp_client_state_temp_from_client = 0

    	Client state address/sync from other client

    .. data:: dhcp_client_state_temp_from_sync = 1

    	Client state Sync

    .. data:: dhcp_client_state_initial = 2

    	Client state Initialing

    .. data:: dhcp_client_state_selecting = 3

    	Client state Selecting

    .. data:: dhcp_client_state_requesting = 4

    	Client state Requesting

    .. data:: dhcp_client_state_bound = 5

    	Client state bound

    .. data:: dhcp_client_state_rebinding = 6

    	Client state rebinding

    .. data:: dhcp_client_state_renewing = 7

    	Client state renewing

    .. data:: dhcp_client_state_holdtime = 8

    	Client state holdtime

    .. data:: dhcp_client_state_ddns_wait = 9

    	Client state DDNS wait

    .. data:: dhcp_client_state_releasing = 10

    	Client state releasing

    .. data:: dhcp_client_state_purging = 11

    	Client state purging

    .. data:: dhcp_client_state_leasequery = 12

    	Client state leasequery

    .. data:: dhcp_client_state_unknown = 13

    	Client state unknown

    """

    dhcp_client_state_temp_from_client = Enum.YLeaf(0, "dhcp-client-state-temp-from-client")

    dhcp_client_state_temp_from_sync = Enum.YLeaf(1, "dhcp-client-state-temp-from-sync")

    dhcp_client_state_initial = Enum.YLeaf(2, "dhcp-client-state-initial")

    dhcp_client_state_selecting = Enum.YLeaf(3, "dhcp-client-state-selecting")

    dhcp_client_state_requesting = Enum.YLeaf(4, "dhcp-client-state-requesting")

    dhcp_client_state_bound = Enum.YLeaf(5, "dhcp-client-state-bound")

    dhcp_client_state_rebinding = Enum.YLeaf(6, "dhcp-client-state-rebinding")

    dhcp_client_state_renewing = Enum.YLeaf(7, "dhcp-client-state-renewing")

    dhcp_client_state_holdtime = Enum.YLeaf(8, "dhcp-client-state-holdtime")

    dhcp_client_state_ddns_wait = Enum.YLeaf(9, "dhcp-client-state-ddns-wait")

    dhcp_client_state_releasing = Enum.YLeaf(10, "dhcp-client-state-releasing")

    dhcp_client_state_purging = Enum.YLeaf(11, "dhcp-client-state-purging")

    dhcp_client_state_leasequery = Enum.YLeaf(12, "dhcp-client-state-leasequery")

    dhcp_client_state_unknown = Enum.YLeaf(13, "dhcp-client-state-unknown")


class DhcpExpiryOption(Enum):
    """
    DhcpExpiryOption (Enum Class)

    DHCP expiration option 

    .. data:: dhcp_expiration_time = 0

    	Expiration option time

    .. data:: dhcp_expiration_infinite = 1

    	Expiration option infinite

    """

    dhcp_expiration_time = Enum.YLeaf(0, "dhcp-expiration-time")

    dhcp_expiration_infinite = Enum.YLeaf(1, "dhcp-expiration-infinite")


class DhcpServerBindingState(Enum):
    """
    DhcpServerBindingState (Enum Class)

    DHCP server binding states 

    .. data:: dhcp_server_binding_state_selecting = 0

    	Server state is in Selecting mode

    .. data:: dhcp_server_binding_state_active = 1

    	Server state Active new address provided

    .. data:: dhcp_server_binding_state_terminated = 2

    	Server terminated the connection with a client

    .. data:: dhcp_server_binding_state_unknown = 3

    	Server state unknown

    """

    dhcp_server_binding_state_selecting = Enum.YLeaf(0, "dhcp-server-binding-state-selecting")

    dhcp_server_binding_state_active = Enum.YLeaf(1, "dhcp-server-binding-state-active")

    dhcp_server_binding_state_terminated = Enum.YLeaf(2, "dhcp-server-binding-state-terminated")

    dhcp_server_binding_state_unknown = Enum.YLeaf(3, "dhcp-server-binding-state-unknown")


class DhcpServerBindingType(Enum):
    """
    DhcpServerBindingType (Enum Class)

    DHCP server binding type

    .. data:: dhcp_server_binding_type_manual = 0

    	Server binding Type Manual

    .. data:: dhcp_server_binding_type_static = 1

    	Sever binding type Static

    .. data:: dhcp_server_binding_type_relay = 2

    	Server binding type relay

    .. data:: dhcp_server_binding_type_automatic = 3

    	Server binding type automatic

    .. data:: dhcp_server_binding_type_odap = 4

    	Server binding Type ODAP

    .. data:: dhcp_server_binding_type_from_aaa = 5

    	Sever binding type from AAA

    .. data:: dhcp_server_binding_type_remembered = 6

    	Server binding type remembered

    """

    dhcp_server_binding_type_manual = Enum.YLeaf(0, "dhcp-server-binding-type-manual")

    dhcp_server_binding_type_static = Enum.YLeaf(1, "dhcp-server-binding-type-static")

    dhcp_server_binding_type_relay = Enum.YLeaf(2, "dhcp-server-binding-type-relay")

    dhcp_server_binding_type_automatic = Enum.YLeaf(3, "dhcp-server-binding-type-automatic")

    dhcp_server_binding_type_odap = Enum.YLeaf(4, "dhcp-server-binding-type-odap")

    dhcp_server_binding_type_from_aaa = Enum.YLeaf(5, "dhcp-server-binding-type-from-aaa")

    dhcp_server_binding_type_remembered = Enum.YLeaf(6, "dhcp-server-binding-type-remembered")



class DhcpOperData(Entity):
    """
    Operational state of DHCP
    
    .. attribute:: dhcpv4_server_oper
    
    	List of DHCP server bidning
    	**type**\: list of  		 :py:class:`Dhcpv4ServerOper <ydk.models.cisco_ios_xe.Cisco_IOS_XE_dhcp_oper.DhcpOperData.Dhcpv4ServerOper>`
    
    .. attribute:: dhcpv4_client_oper
    
    	List of DHCP clients
    	**type**\: list of  		 :py:class:`Dhcpv4ClientOper <ydk.models.cisco_ios_xe.Cisco_IOS_XE_dhcp_oper.DhcpOperData.Dhcpv4ClientOper>`
    
    

    """

    _prefix = 'dhcp-ios-xe-oper'
    _revision = '2017-11-01'

    def __init__(self):
        super(DhcpOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "dhcp-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-dhcp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("dhcpv4-server-oper", ("dhcpv4_server_oper", DhcpOperData.Dhcpv4ServerOper)), ("dhcpv4-client-oper", ("dhcpv4_client_oper", DhcpOperData.Dhcpv4ClientOper))])
        self._leafs = OrderedDict()

        self.dhcpv4_server_oper = YList(self)
        self.dhcpv4_client_oper = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-dhcp-oper:dhcp-oper-data"

    def __setattr__(self, name, value):
        self._perform_setattr(DhcpOperData, [], name, value)


    class Dhcpv4ServerOper(Entity):
        """
        List of DHCP server bidning
        
        .. attribute:: pool_name  (key)
        
        	Server Pool name from where the Client  ip is provided
        	**type**\: str
        
        .. attribute:: client_ip  (key)
        
        	ipaddress released for a speicfic Client  from Server
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: vrf_name  (key)
        
        	Query based on the vrfname speicfic to that pool and Client ip address as key
        	**type**\: str
        
        .. attribute:: client_id_type
        
        	Client identification Hardware types
        	**type**\:  :py:class:`DhcpClientIdType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_dhcp_oper.DhcpClientIdType>`
        
        .. attribute:: client_id
        
        	Client identification can be based on Hardware types/Mac
        	**type**\: str
        
        .. attribute:: expiration
        
        	Expiration time infomation
        	**type**\:  :py:class:`Expiration <ydk.models.cisco_ios_xe.Cisco_IOS_XE_dhcp_oper.DhcpOperData.Dhcpv4ServerOper.Expiration>`
        
        .. attribute:: type
        
        	Server binding type
        	**type**\:  :py:class:`DhcpServerBindingType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_dhcp_oper.DhcpServerBindingType>`
        
        .. attribute:: state
        
        	Server binding states
        	**type**\:  :py:class:`DhcpServerBindingState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_dhcp_oper.DhcpServerBindingState>`
        
        .. attribute:: interface
        
        	interface name of the pool
        	**type**\: str
        
        

        """

        _prefix = 'dhcp-ios-xe-oper'
        _revision = '2017-11-01'

        def __init__(self):
            super(DhcpOperData.Dhcpv4ServerOper, self).__init__()

            self.yang_name = "dhcpv4-server-oper"
            self.yang_parent_name = "dhcp-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['pool_name','client_ip','vrf_name']
            self._child_container_classes = OrderedDict([("expiration", ("expiration", DhcpOperData.Dhcpv4ServerOper.Expiration))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('pool_name', YLeaf(YType.str, 'pool-name')),
                ('client_ip', YLeaf(YType.str, 'client-ip')),
                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                ('client_id_type', YLeaf(YType.enumeration, 'client-id-type')),
                ('client_id', YLeaf(YType.str, 'client-id')),
                ('type', YLeaf(YType.enumeration, 'type')),
                ('state', YLeaf(YType.enumeration, 'state')),
                ('interface', YLeaf(YType.str, 'interface')),
            ])
            self.pool_name = None
            self.client_ip = None
            self.vrf_name = None
            self.client_id_type = None
            self.client_id = None
            self.type = None
            self.state = None
            self.interface = None

            self.expiration = DhcpOperData.Dhcpv4ServerOper.Expiration()
            self.expiration.parent = self
            self._children_name_map["expiration"] = "expiration"
            self._children_yang_names.add("expiration")
            self._segment_path = lambda: "dhcpv4-server-oper" + "[pool-name='" + str(self.pool_name) + "']" + "[client-ip='" + str(self.client_ip) + "']" + "[vrf-name='" + str(self.vrf_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-dhcp-oper:dhcp-oper-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DhcpOperData.Dhcpv4ServerOper, ['pool_name', 'client_ip', 'vrf_name', 'client_id_type', 'client_id', 'type', 'state', 'interface'], name, value)


        class Expiration(Entity):
            """
            Expiration time infomation
            
            .. attribute:: time
            
            	Date and time of expiry 
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: infinite
            
            	Expiry time infinite
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'dhcp-ios-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(DhcpOperData.Dhcpv4ServerOper.Expiration, self).__init__()

                self.yang_name = "expiration"
                self.yang_parent_name = "dhcpv4-server-oper"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('time', YLeaf(YType.str, 'time')),
                    ('infinite', YLeaf(YType.empty, 'infinite')),
                ])
                self.time = None
                self.infinite = None
                self._segment_path = lambda: "expiration"

            def __setattr__(self, name, value):
                self._perform_setattr(DhcpOperData.Dhcpv4ServerOper.Expiration, ['time', 'infinite'], name, value)


    class Dhcpv4ClientOper(Entity):
        """
        List of DHCP clients
        
        .. attribute:: if_name  (key)
        
        	Interface infomation where dhcp Client is configured
        	**type**\: str
        
        .. attribute:: client_addr  (key)
        
        	Client\_addr address Allocated from Server
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: vrf_name  (key)
        
        	Vrfname infomation related to Client
        	**type**\: str
        
        .. attribute:: state
        
        	DHCP Client States 
        	**type**\:  :py:class:`DhcpClientState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_dhcp_oper.DhcpClientState>`
        
        .. attribute:: lease_server_addr
        
        	IP address of Server from where we got IP
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: gateway_addr
        
        	Gateway Address we got from Server
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: lease_time
        
        	Total Lease Time in Seconds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lease_expiry
        
        	Lease Expiry time for the IP address we got
        	**type**\:  :py:class:`LeaseExpiry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_dhcp_oper.DhcpOperData.Dhcpv4ClientOper.LeaseExpiry>`
        
        .. attribute:: lease_remaining
        
        	Lease remaining time for the IP address
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: dns_list
        
        	DNS list based on index
        	**type**\: union of the below types:
        
        		**type**\: list of str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: list of str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        

        """

        _prefix = 'dhcp-ios-xe-oper'
        _revision = '2017-11-01'

        def __init__(self):
            super(DhcpOperData.Dhcpv4ClientOper, self).__init__()

            self.yang_name = "dhcpv4-client-oper"
            self.yang_parent_name = "dhcp-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['if_name','client_addr','vrf_name']
            self._child_container_classes = OrderedDict([("lease-expiry", ("lease_expiry", DhcpOperData.Dhcpv4ClientOper.LeaseExpiry))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('if_name', YLeaf(YType.str, 'if-name')),
                ('client_addr', YLeaf(YType.str, 'client-addr')),
                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                ('state', YLeaf(YType.enumeration, 'state')),
                ('lease_server_addr', YLeaf(YType.str, 'lease-server-addr')),
                ('gateway_addr', YLeaf(YType.str, 'gateway-addr')),
                ('lease_time', YLeaf(YType.uint32, 'lease-time')),
                ('lease_remaining', YLeaf(YType.uint32, 'lease-remaining')),
                ('dns_list', YLeafList(YType.str, 'dns-list')),
            ])
            self.if_name = None
            self.client_addr = None
            self.vrf_name = None
            self.state = None
            self.lease_server_addr = None
            self.gateway_addr = None
            self.lease_time = None
            self.lease_remaining = None
            self.dns_list = []

            self.lease_expiry = DhcpOperData.Dhcpv4ClientOper.LeaseExpiry()
            self.lease_expiry.parent = self
            self._children_name_map["lease_expiry"] = "lease-expiry"
            self._children_yang_names.add("lease-expiry")
            self._segment_path = lambda: "dhcpv4-client-oper" + "[if-name='" + str(self.if_name) + "']" + "[client-addr='" + str(self.client_addr) + "']" + "[vrf-name='" + str(self.vrf_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-dhcp-oper:dhcp-oper-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DhcpOperData.Dhcpv4ClientOper, ['if_name', 'client_addr', 'vrf_name', 'state', 'lease_server_addr', 'gateway_addr', 'lease_time', 'lease_remaining', 'dns_list'], name, value)


        class LeaseExpiry(Entity):
            """
            Lease Expiry time for the IP address we got
            
            .. attribute:: time
            
            	Date and time of expiry 
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: infinite
            
            	Expiry time infinite
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'dhcp-ios-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(DhcpOperData.Dhcpv4ClientOper.LeaseExpiry, self).__init__()

                self.yang_name = "lease-expiry"
                self.yang_parent_name = "dhcpv4-client-oper"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('time', YLeaf(YType.str, 'time')),
                    ('infinite', YLeaf(YType.empty, 'infinite')),
                ])
                self.time = None
                self.infinite = None
                self._segment_path = lambda: "lease-expiry"

            def __setattr__(self, name, value):
                self._perform_setattr(DhcpOperData.Dhcpv4ClientOper.LeaseExpiry, ['time', 'infinite'], name, value)

    def clone_ptr(self):
        self._top_entity = DhcpOperData()
        return self._top_entity

