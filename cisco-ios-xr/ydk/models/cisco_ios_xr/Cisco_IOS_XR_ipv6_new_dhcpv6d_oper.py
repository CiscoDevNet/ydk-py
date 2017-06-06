""" Cisco_IOS_XR_ipv6_new_dhcpv6d_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-new\-dhcpv6d package operational data.

This module contains definitions
for the following management objects\:
  dhcpv6\: IPV6 DHCPD operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BagDhcpv6DFsmStateEnum(Enum):
    """
    BagDhcpv6DFsmStateEnum

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

    server_initializing = 0

    server_waiting_dpm = 1

    server_waiting_daps = 2

    server_waiting_client = 3

    server_waiting_subscriber = 4

    server_waiting_rib = 5

    server_bound_client = 6

    proxy_initializing = 10

    proxy_waiting_dpm = 11

    proxy_waiting_daps = 12

    proxy_waiting_client_server = 13

    proxy_waiting_subscriber = 14

    proxy_waiting_rib = 15

    proxy_bound_client = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['BagDhcpv6DFsmStateEnum']


class BagDhcpv6DIaIdEnum(Enum):
    """
    BagDhcpv6DIaIdEnum

    Bag dhcpv6d ia id

    .. data:: iana = 0

    	Non-temporary Addresses assigned 

    .. data:: iapd = 1

    	Prefix delegeated to client      

    .. data:: iata = 2

    	Temporary Addresses - not supported 

    """

    iana = 0

    iapd = 1

    iata = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['BagDhcpv6DIaIdEnum']


class BagDhcpv6DIntfSergRoleEnum(Enum):
    """
    BagDhcpv6DIntfSergRoleEnum

    Bag dhcpv6d intf serg role

    .. data:: none = 0

    	DHCPv6 Interface SERG role NONE

    .. data:: master = 1

    	DHCPv6 Interface SERG role Master

    .. data:: slave = 2

    	DHCPv6 Interface SERG role Slave

    """

    none = 0

    master = 1

    slave = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['BagDhcpv6DIntfSergRoleEnum']


class BagDhcpv6DIntfSrgRoleEnum(Enum):
    """
    BagDhcpv6DIntfSrgRoleEnum

    Bag dhcpv6d intf srg role

    .. data:: none = 0

    	DHCPv6 Interface SRG role NONE

    .. data:: master = 1

    	DHCPv6 Interface SRG role Master

    .. data:: slave = 2

    	DHCPv6 Interface SRG role Slave

    """

    none = 0

    master = 1

    slave = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['BagDhcpv6DIntfSrgRoleEnum']


class BagDhcpv6DSubModeEnum(Enum):
    """
    BagDhcpv6DSubModeEnum

    Bag dhcpv6d sub mode

    .. data:: base = 0

    	DHCPv6 Base mode

    .. data:: server = 1

    	DHCPv6 Server mode

    .. data:: proxy = 2

    	DHCPv6 Proxy mode

    """

    base = 0

    server = 1

    proxy = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['BagDhcpv6DSubModeEnum']


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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['DhcpIssuPhaseEnum']


class Dhcpv6IssuRoleEnum(Enum):
    """
    Dhcpv6IssuRoleEnum

    Dhcpv6 issu role

    .. data:: role_primary = 0

    	Primary role

    .. data:: role_secondary = 1

    	Secondary role

    """

    role_primary = 0

    role_secondary = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['Dhcpv6IssuRoleEnum']


class Dhcpv6IssuVersionEnum(Enum):
    """
    Dhcpv6IssuVersionEnum

    Dhcpv6 issu version

    .. data:: version1 = 0

    	Version 1

    .. data:: version2 = 1

    	Version 2

    """

    version1 = 0

    version2 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['Dhcpv6IssuVersionEnum']


class LeaseLimitEnum(Enum):
    """
    LeaseLimitEnum

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

    none = 0

    interface = 1

    circuit_id = 2

    remote_id = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['LeaseLimitEnum']



class Dhcpv6(object):
    """
    IPV6 DHCPD operational data
    
    .. attribute:: issu_status
    
    	DHCP IssuStatus
    	**type**\:   :py:class:`IssuStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.IssuStatus>`
    
    .. attribute:: nodes
    
    	IPv6 DHCP list of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes>`
    
    

    """

    _prefix = 'ipv6-new-dhcpv6d-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.issu_status = Dhcpv6.IssuStatus()
        self.issu_status.parent = self
        self.nodes = Dhcpv6.Nodes()
        self.nodes.parent = self


    class IssuStatus(object):
        """
        DHCP IssuStatus
        
        .. attribute:: big_bang_time
        
        	Timestamp for the Big Bang notification time in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: nanosecond
        
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
        	**type**\:   :py:class:`DhcpIssuPhaseEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.DhcpIssuPhaseEnum>`
        
        .. attribute:: primary_role_time
        
        	Timestamp for the change to Primary role notification time in nanoseconds since Epoch, i .e. since 00\:00\:00 UTC, January 1, 1970
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: nanosecond
        
        .. attribute:: process_start_time
        
        	Timestamp for the process start time in nanoseconds since Epoch, i.e. since 00\:00\:00 UTC , January 1, 1970
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: nanosecond
        
        .. attribute:: role
        
        	The current role of the DHCP process
        	**type**\:   :py:class:`Dhcpv6IssuRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6IssuRoleEnum>`
        
        .. attribute:: version
        
        	The current version of the DHCP process in the context of an ISSU
        	**type**\:   :py:class:`Dhcpv6IssuVersionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6IssuVersionEnum>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.big_bang_time = None
            self.issu_ready_issu_mgr_connection = None
            self.issu_ready_time = None
            self.issu_sync_complete_time = None
            self.issu_sync_start_time = None
            self.phase = None
            self.primary_role_time = None
            self.process_start_time = None
            self.role = None
            self.version = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:issu-status'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.big_bang_time is not None:
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

            if self.process_start_time is not None:
                return True

            if self.role is not None:
                return True

            if self.version is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
            return meta._meta_table['Dhcpv6.IssuStatus']['meta_info']


    class Nodes(object):
        """
        IPv6 DHCP list of nodes
        
        .. attribute:: node
        
        	IPv6 DHCP particular node name
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            IPv6 DHCP particular node name
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: base
            
            	IPv6 DHCP Base
            	**type**\:   :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Base>`
            
            .. attribute:: proxy
            
            	IPv6 DHCP proxy operational data
            	**type**\:   :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy>`
            
            .. attribute:: relay
            
            	IPv6 DHCP relay operational data
            	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay>`
            
            .. attribute:: server
            
            	IPv6 DHCP server operational data
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server>`
            
            

            """

            _prefix = 'ipv6-new-dhcpv6d-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.base = Dhcpv6.Nodes.Node.Base()
                self.base.parent = self
                self.proxy = Dhcpv6.Nodes.Node.Proxy()
                self.proxy.parent = self
                self.relay = Dhcpv6.Nodes.Node.Relay()
                self.relay.parent = self
                self.server = Dhcpv6.Nodes.Node.Server()
                self.server.parent = self


            class Proxy(object):
                """
                IPv6 DHCP proxy operational data
                
                .. attribute:: binding
                
                	DHCPV6 proxy bindings
                	**type**\:   :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding>`
                
                .. attribute:: interfaces
                
                	DHCPV6 proxy interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Interfaces>`
                
                .. attribute:: profiles
                
                	IPv6 DHCP proxy profile
                	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles>`
                
                .. attribute:: statistics
                
                	DHCPv6 proxy statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Statistics>`
                
                .. attribute:: vrfs
                
                	DHCPV6 proxy list of VRF names
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs>`
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.binding = Dhcpv6.Nodes.Node.Proxy.Binding()
                    self.binding.parent = self
                    self.interfaces = Dhcpv6.Nodes.Node.Proxy.Interfaces()
                    self.interfaces.parent = self
                    self.profiles = Dhcpv6.Nodes.Node.Proxy.Profiles()
                    self.profiles.parent = self
                    self.statistics = Dhcpv6.Nodes.Node.Proxy.Statistics()
                    self.statistics.parent = self
                    self.vrfs = Dhcpv6.Nodes.Node.Proxy.Vrfs()
                    self.vrfs.parent = self


                class Vrfs(object):
                    """
                    DHCPV6 proxy list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP proxy VRF name
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        IPv6 DHCP proxy VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv6 DHCP proxy statistics
                        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.statistics = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self


                        class Statistics(object):
                            """
                            IPv6 DHCP proxy statistics
                            
                            .. attribute:: advertise
                            
                            	DHCPV6 advertise packets
                            	**type**\:   :py:class:`Advertise <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise>`
                            
                            .. attribute:: confirm
                            
                            	DHCPV6 confirm packets
                            	**type**\:   :py:class:`Confirm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm>`
                            
                            .. attribute:: decline
                            
                            	DHCPV6 decline packets
                            	**type**\:   :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: inform
                            
                            	DHCPV6 inform packets
                            	**type**\:   :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: lease_query
                            
                            	DHCPV6 lease query packets
                            	**type**\:   :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_query_data
                            
                            	DHCPV6 lease query data packets
                            	**type**\:   :py:class:`LeaseQueryData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData>`
                            
                            .. attribute:: lease_query_done
                            
                            	DHCPV6 lease query done packets
                            	**type**\:   :py:class:`LeaseQueryDone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone>`
                            
                            .. attribute:: lease_query_reply
                            
                            	DHCPV6 lease query reply packets
                            	**type**\:   :py:class:`LeaseQueryReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply>`
                            
                            .. attribute:: rebind
                            
                            	DHCPV6 rebind packets
                            	**type**\:   :py:class:`Rebind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind>`
                            
                            .. attribute:: reconfig
                            
                            	DHCPV6 reconfig packets
                            	**type**\:   :py:class:`Reconfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig>`
                            
                            .. attribute:: relay_forward
                            
                            	DHCPV6 relay forward packets
                            	**type**\:   :py:class:`RelayForward <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward>`
                            
                            .. attribute:: relay_reply
                            
                            	DHCPV6 relay reply packets
                            	**type**\:   :py:class:`RelayReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply>`
                            
                            .. attribute:: release
                            
                            	DHCPV6 release packets
                            	**type**\:   :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: renew
                            
                            	DHCPV6 renew packets
                            	**type**\:   :py:class:`Renew <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew>`
                            
                            .. attribute:: reply
                            
                            	DHCPV6 reply packets
                            	**type**\:   :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply>`
                            
                            .. attribute:: request
                            
                            	DHCPV6 request packets
                            	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: solicit
                            
                            	DHCPV6 solicit packets
                            	**type**\:   :py:class:`Solicit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.advertise = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise()
                                self.advertise.parent = self
                                self.confirm = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm()
                                self.confirm.parent = self
                                self.decline = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self.inform = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self.lease_query = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self.lease_query_data = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData()
                                self.lease_query_data.parent = self
                                self.lease_query_done = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone()
                                self.lease_query_done.parent = self
                                self.lease_query_reply = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply()
                                self.lease_query_reply.parent = self
                                self.rebind = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind()
                                self.rebind.parent = self
                                self.reconfig = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig()
                                self.reconfig.parent = self
                                self.relay_forward = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward()
                                self.relay_forward.parent = self
                                self.relay_reply = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply()
                                self.relay_reply.parent = self
                                self.release = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self.renew = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew()
                                self.renew.parent = self
                                self.reply = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply()
                                self.reply.parent = self
                                self.request = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self.solicit = Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit()
                                self.solicit.parent = self


                            class Solicit(object):
                                """
                                DHCPV6 solicit packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:solicit'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit']['meta_info']


                            class Advertise(object):
                                """
                                DHCPV6 advertise packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:advertise'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise']['meta_info']


                            class Request(object):
                                """
                                DHCPV6 request packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:request'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request']['meta_info']


                            class Reply(object):
                                """
                                DHCPV6 reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reply'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply']['meta_info']


                            class Confirm(object):
                                """
                                DHCPV6 confirm packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:confirm'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm']['meta_info']


                            class Decline(object):
                                """
                                DHCPV6 decline packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:decline'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline']['meta_info']


                            class Renew(object):
                                """
                                DHCPV6 renew packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:renew'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew']['meta_info']


                            class Rebind(object):
                                """
                                DHCPV6 rebind packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:rebind'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind']['meta_info']


                            class Release(object):
                                """
                                DHCPV6 release packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:release'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release']['meta_info']


                            class Reconfig(object):
                                """
                                DHCPV6 reconfig packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reconfig'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig']['meta_info']


                            class Inform(object):
                                """
                                DHCPV6 inform packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:inform'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform']['meta_info']


                            class RelayForward(object):
                                """
                                DHCPV6 relay forward packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-forward'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward']['meta_info']


                            class RelayReply(object):
                                """
                                DHCPV6 relay reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-reply'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply']['meta_info']


                            class LeaseQuery(object):
                                """
                                DHCPV6 lease query packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info']


                            class LeaseQueryReply(object):
                                """
                                DHCPV6 lease query reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-reply'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply']['meta_info']


                            class LeaseQueryDone(object):
                                """
                                DHCPV6 lease query done packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-done'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone']['meta_info']


                            class LeaseQueryData(object):
                                """
                                DHCPV6 lease query data packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-data'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.advertise is not None and self.advertise._has_data():
                                    return True

                                if self.confirm is not None and self.confirm._has_data():
                                    return True

                                if self.decline is not None and self.decline._has_data():
                                    return True

                                if self.inform is not None and self.inform._has_data():
                                    return True

                                if self.lease_query is not None and self.lease_query._has_data():
                                    return True

                                if self.lease_query_data is not None and self.lease_query_data._has_data():
                                    return True

                                if self.lease_query_done is not None and self.lease_query_done._has_data():
                                    return True

                                if self.lease_query_reply is not None and self.lease_query_reply._has_data():
                                    return True

                                if self.rebind is not None and self.rebind._has_data():
                                    return True

                                if self.reconfig is not None and self.reconfig._has_data():
                                    return True

                                if self.relay_forward is not None and self.relay_forward._has_data():
                                    return True

                                if self.relay_reply is not None and self.relay_reply._has_data():
                                    return True

                                if self.release is not None and self.release._has_data():
                                    return True

                                if self.renew is not None and self.renew._has_data():
                                    return True

                                if self.reply is not None and self.reply._has_data():
                                    return True

                                if self.request is not None and self.request._has_data():
                                    return True

                                if self.solicit is not None and self.solicit._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf-name = ' + str(self.vrf_name) + ']'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrfs'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs']['meta_info']


                class Profiles(object):
                    """
                    IPv6 DHCP proxy profile
                    
                    .. attribute:: profile
                    
                    	IPv6 DHCP proxy profile
                    	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.profile = YList()
                        self.profile.parent = self
                        self.profile.name = 'profile'


                    class Profile(object):
                        """
                        IPv6 DHCP proxy profile
                        
                        .. attribute:: profile_name  <key>
                        
                        	Profile name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: info
                        
                        	IPv6 DHCP proxy profile Info
                        	**type**\:   :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info>`
                        
                        .. attribute:: throttle_infos
                        
                        	DHCPV6 throttle table
                        	**type**\:   :py:class:`ThrottleInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.profile_name = None
                            self.info = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info()
                            self.info.parent = self
                            self.throttle_infos = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos()
                            self.throttle_infos.parent = self


                        class ThrottleInfos(object):
                            """
                            DHCPV6 throttle table
                            
                            .. attribute:: throttle_info
                            
                            	IPv6 DHCP proxy profile Throttle Info
                            	**type**\: list of    :py:class:`ThrottleInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.throttle_info = YList()
                                self.throttle_info.parent = self
                                self.throttle_info.name = 'throttle_info'


                            class ThrottleInfo(object):
                                """
                                IPv6 DHCP proxy profile Throttle Info
                                
                                .. attribute:: mac_address  <key>
                                
                                	MAC address
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: binding_chaddr
                                
                                	Client MAC address
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: ifname
                                
                                	DHCP access interface
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                .. attribute:: state
                                
                                	State of entry
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_left
                                
                                	Time Left in secs
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mac_address = None
                                    self.binding_chaddr = None
                                    self.ifname = None
                                    self.state = None
                                    self.time_left = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.mac_address is None:
                                        raise YPYModelError('Key property mac_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:throttle-info[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:mac-address = ' + str(self.mac_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.mac_address is not None:
                                        return True

                                    if self.binding_chaddr is not None:
                                        return True

                                    if self.ifname is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    if self.time_left is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:throttle-infos'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.throttle_info is not None:
                                    for child_ref in self.throttle_info:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos']['meta_info']


                        class Info(object):
                            """
                            IPv6 DHCP proxy profile Info
                            
                            .. attribute:: interface_id_references
                            
                            	Interface id references
                            	**type**\:   :py:class:`InterfaceIdReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences>`
                            
                            .. attribute:: interface_name
                            
                            	Interface names
                            	**type**\:  list of str
                            
                            	**length:** 0..65
                            
                            .. attribute:: interface_references
                            
                            	Interface references
                            	**type**\:   :py:class:`InterfaceReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences>`
                            
                            .. attribute:: profile_helper_address
                            
                            	Helper addresses
                            	**type**\:  list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: profile_link_address
                            
                            	Link address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: profile_name
                            
                            	Proxy profile name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            .. attribute:: remote_id
                            
                            	Remote id
                            	**type**\:  str
                            
                            	**length:** 0..257
                            
                            .. attribute:: vrf_name
                            
                            	VRF names
                            	**type**\:  list of str
                            
                            	**length:** 0..33
                            
                            .. attribute:: vrf_references
                            
                            	VRF references
                            	**type**\:   :py:class:`VrfReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface_id_references = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences()
                                self.interface_id_references.parent = self
                                self.interface_name = YLeafList()
                                self.interface_name.parent = self
                                self.interface_name.name = 'interface_name'
                                self.interface_references = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences()
                                self.interface_references.parent = self
                                self.profile_helper_address = YLeafList()
                                self.profile_helper_address.parent = self
                                self.profile_helper_address.name = 'profile_helper_address'
                                self.profile_link_address = None
                                self.profile_name = None
                                self.remote_id = None
                                self.vrf_name = YLeafList()
                                self.vrf_name.parent = self
                                self.vrf_name.name = 'vrf_name'
                                self.vrf_references = Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences()
                                self.vrf_references.parent = self


                            class InterfaceIdReferences(object):
                                """
                                Interface id references
                                
                                .. attribute:: ipv6_dhcpv6d_proxy_iid_reference
                                
                                	ipv6 dhcpv6d proxy iid reference
                                	**type**\: list of    :py:class:`Ipv6Dhcpv6DProxyIidReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv6_dhcpv6d_proxy_iid_reference = YList()
                                    self.ipv6_dhcpv6d_proxy_iid_reference.parent = self
                                    self.ipv6_dhcpv6d_proxy_iid_reference.name = 'ipv6_dhcpv6d_proxy_iid_reference'


                                class Ipv6Dhcpv6DProxyIidReference(object):
                                    """
                                    ipv6 dhcpv6d proxy iid reference
                                    
                                    .. attribute:: proxy_iid_interface_name
                                    
                                    	Interface name for interface id
                                    	**type**\:  str
                                    
                                    	**length:** 0..65
                                    
                                    .. attribute:: proxy_interface_id
                                    
                                    	Interface id
                                    	**type**\:  str
                                    
                                    	**length:** 0..257
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.proxy_iid_interface_name = None
                                        self.proxy_interface_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-proxy-iid-reference'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.proxy_iid_interface_name is not None:
                                            return True

                                        if self.proxy_interface_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interface-id-references'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv6_dhcpv6d_proxy_iid_reference is not None:
                                        for child_ref in self.ipv6_dhcpv6d_proxy_iid_reference:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences']['meta_info']


                            class VrfReferences(object):
                                """
                                VRF references
                                
                                .. attribute:: ipv6_dhcpv6d_proxy_vrf_reference
                                
                                	ipv6 dhcpv6d proxy vrf reference
                                	**type**\: list of    :py:class:`Ipv6Dhcpv6DProxyVrfReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv6_dhcpv6d_proxy_vrf_reference = YList()
                                    self.ipv6_dhcpv6d_proxy_vrf_reference.parent = self
                                    self.ipv6_dhcpv6d_proxy_vrf_reference.name = 'ipv6_dhcpv6d_proxy_vrf_reference'


                                class Ipv6Dhcpv6DProxyVrfReference(object):
                                    """
                                    ipv6 dhcpv6d proxy vrf reference
                                    
                                    .. attribute:: proxy_reference_vrf_name
                                    
                                    	VRF name
                                    	**type**\:  str
                                    
                                    	**length:** 0..33
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.proxy_reference_vrf_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-proxy-vrf-reference'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.proxy_reference_vrf_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf-references'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv6_dhcpv6d_proxy_vrf_reference is not None:
                                        for child_ref in self.ipv6_dhcpv6d_proxy_vrf_reference:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences']['meta_info']


                            class InterfaceReferences(object):
                                """
                                Interface references
                                
                                .. attribute:: ipv6_dhcpv6d_proxy_interface_reference
                                
                                	ipv6 dhcpv6d proxy interface reference
                                	**type**\: list of    :py:class:`Ipv6Dhcpv6DProxyInterfaceReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv6_dhcpv6d_proxy_interface_reference = YList()
                                    self.ipv6_dhcpv6d_proxy_interface_reference.parent = self
                                    self.ipv6_dhcpv6d_proxy_interface_reference.name = 'ipv6_dhcpv6d_proxy_interface_reference'


                                class Ipv6Dhcpv6DProxyInterfaceReference(object):
                                    """
                                    ipv6 dhcpv6d proxy interface reference
                                    
                                    .. attribute:: proxy_reference_interface_name
                                    
                                    	Interface name
                                    	**type**\:  str
                                    
                                    	**length:** 0..65
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.proxy_reference_interface_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-proxy-interface-reference'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.proxy_reference_interface_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interface-references'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv6_dhcpv6d_proxy_interface_reference is not None:
                                        for child_ref in self.ipv6_dhcpv6d_proxy_interface_reference:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface_id_references is not None and self.interface_id_references._has_data():
                                    return True

                                if self.interface_name is not None:
                                    for child in self.interface_name:
                                        if child is not None:
                                            return True

                                if self.interface_references is not None and self.interface_references._has_data():
                                    return True

                                if self.profile_helper_address is not None:
                                    for child in self.profile_helper_address:
                                        if child is not None:
                                            return True

                                if self.profile_link_address is not None:
                                    return True

                                if self.profile_name is not None:
                                    return True

                                if self.remote_id is not None:
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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.profile_name is None:
                                raise YPYModelError('Key property profile_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profile[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profile-name = ' + str(self.profile_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.profile_name is not None:
                                return True

                            if self.info is not None and self.info._has_data():
                                return True

                            if self.throttle_infos is not None and self.throttle_infos._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profiles'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles']['meta_info']


                class Interfaces(object):
                    """
                    DHCPV6 proxy interface
                    
                    .. attribute:: interface
                    
                    	IPv6 DHCP proxy interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        IPv6 DHCP proxy interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface Name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: is_proxy_interface_ambiguous
                        
                        	Is interface ambiguous
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mac_throttle
                        
                        	Mac Throttle Status
                        	**type**\:  bool
                        
                        .. attribute:: proxy_interface_lease_limit_type
                        
                        	Lease limit type on interface
                        	**type**\:   :py:class:`LeaseLimitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.LeaseLimitEnum>`
                        
                        .. attribute:: proxy_interface_lease_limits
                        
                        	Lease limit count on interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: proxy_interface_mode
                        
                        	Mode of interface
                        	**type**\:   :py:class:`BagDhcpv6DSubModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DSubModeEnum>`
                        
                        .. attribute:: proxy_interface_profile_name
                        
                        	Name of profile attached to the interface
                        	**type**\:  str
                        
                        	**length:** 0..65
                        
                        .. attribute:: proxy_vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        .. attribute:: serg_role
                        
                        	DHCPv6 Interface SERG role
                        	**type**\:   :py:class:`BagDhcpv6DIntfSergRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIntfSergRoleEnum>`
                        
                        .. attribute:: srg_role
                        
                        	DHCPv6 Interface SRG role
                        	**type**\:   :py:class:`BagDhcpv6DIntfSrgRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIntfSrgRoleEnum>`
                        
                        .. attribute:: srg_vrf_name
                        
                        	SRG VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        .. attribute:: srgp2p
                        
                        	SRG P2P Status
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.is_proxy_interface_ambiguous = None
                            self.mac_throttle = None
                            self.proxy_interface_lease_limit_type = None
                            self.proxy_interface_lease_limits = None
                            self.proxy_interface_mode = None
                            self.proxy_interface_profile_name = None
                            self.proxy_vrf_name = None
                            self.serg_role = None
                            self.srg_role = None
                            self.srg_vrf_name = None
                            self.srgp2p = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interface[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.is_proxy_interface_ambiguous is not None:
                                return True

                            if self.mac_throttle is not None:
                                return True

                            if self.proxy_interface_lease_limit_type is not None:
                                return True

                            if self.proxy_interface_lease_limits is not None:
                                return True

                            if self.proxy_interface_mode is not None:
                                return True

                            if self.proxy_interface_profile_name is not None:
                                return True

                            if self.proxy_vrf_name is not None:
                                return True

                            if self.serg_role is not None:
                                return True

                            if self.srg_role is not None:
                                return True

                            if self.srg_vrf_name is not None:
                                return True

                            if self.srgp2p is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interfaces'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Interfaces']['meta_info']


                class Statistics(object):
                    """
                    DHCPv6 proxy statistics
                    
                    .. attribute:: ipv6_dhcpv6d_proxy_stat
                    
                    	ipv6 dhcpv6d proxy stat
                    	**type**\: list of    :py:class:`Ipv6Dhcpv6DProxyStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_dhcpv6d_proxy_stat = YList()
                        self.ipv6_dhcpv6d_proxy_stat.parent = self
                        self.ipv6_dhcpv6d_proxy_stat.name = 'ipv6_dhcpv6d_proxy_stat'


                    class Ipv6Dhcpv6DProxyStat(object):
                        """
                        ipv6 dhcpv6d proxy stat
                        
                        .. attribute:: statistics
                        
                        	Proxy statistics
                        	**type**\:   :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCPv6 L3 VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.statistics = Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_()
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

                            _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-proxy-stat'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv6_dhcpv6d_proxy_stat is not None:
                            for child_ref in self.ipv6_dhcpv6d_proxy_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Statistics']['meta_info']


                class Binding(object):
                    """
                    DHCPV6 proxy bindings
                    
                    .. attribute:: clients
                    
                    	DHCPV6 proxy client bindings
                    	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients>`
                    
                    .. attribute:: summary
                    
                    	DHCPV6 proxy binding summary
                    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Summary>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.clients = Dhcpv6.Nodes.Node.Proxy.Binding.Clients()
                        self.clients.parent = self
                        self.summary = Dhcpv6.Nodes.Node.Proxy.Binding.Summary()
                        self.summary.parent = self


                    class Clients(object):
                        """
                        DHCPV6 proxy client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCPV6 proxy binding
                        	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.client = YList()
                            self.client.parent = self
                            self.client.name = 'client'


                        class Client(object):
                            """
                            Single DHCPV6 proxy binding
                            
                            .. attribute:: client_id  <key>
                            
                            	Client ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: access_vrf_name
                            
                            	DHCPV6 access VRF name to client
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: class_name
                            
                            	DHCPV6 class name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: client_flag
                            
                            	DHCPV6 client flag
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duid
                            
                            	Client DUID
                            	**type**\:  str
                            
                            .. attribute:: framed_ipv6_prefix
                            
                            	DHCPV6 framed ipv6 addess used by ND
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: framed_prefix_length
                            
                            	DHCPV6 framed ipv6 prefix length used by ND
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ia_id_p_ds
                            
                            	Number of ia\_id/pd
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ia_id_pd
                            
                            	List of DHCPv6 IA\_ID/PDs
                            	**type**\:   :py:class:`IaIdPd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd>`
                            
                            .. attribute:: interface_name
                            
                            	DHCPV6 access interface to client
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: is_nak_next_renew
                            
                            	Is true if DHCP next renew from client will be NAK'd
                            	**type**\:  bool
                            
                            .. attribute:: mac_address
                            
                            	Client MAC address
                            	**type**\:  str
                            
                            .. attribute:: pool_name
                            
                            	DHCPV6 pool name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: profile_name
                            
                            	DHCPV6 profile name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            .. attribute:: proxy_binding_inner_tag
                            
                            	DHCPV6 VLAN Inner VLAN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_binding_outer_tag
                            
                            	DHCPV6 VLAN Outer VLAN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_binding_tags
                            
                            	DHCPV6 VLAN tag count
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: rx_interface_id
                            
                            	DHCPV6 received Interface ID
                            	**type**\:  str
                            
                            	**length:** 0..771
                            
                            .. attribute:: rx_remote_id
                            
                            	DHCPV6 received Remote ID
                            	**type**\:  str
                            
                            	**length:** 0..771
                            
                            .. attribute:: serg_intf_role
                            
                            	DHCPV6 SERG Intf Role
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: serg_state
                            
                            	DHCPV6 SERG state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: server_ipv6_address
                            
                            	DHCPV6 server IPv6 address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: srg_intf_role
                            
                            	DHCPV6 SRG Intf Role
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srg_state
                            
                            	DHCPV6 SRG state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srg_vrf_name
                            
                            	DHCPV6 SRG VRF NAME
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: srgp2p
                            
                            	SRG P2P Status
                            	**type**\:  bool
                            
                            .. attribute:: subscriber_label
                            
                            	DHCPV6 subscriber label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tx_interface_id
                            
                            	DHCPV6 transmitted Interface ID
                            	**type**\:  str
                            
                            	**length:** 0..771
                            
                            .. attribute:: tx_remote_id
                            
                            	DHCPV6 transmitted Remote ID
                            	**type**\:  str
                            
                            	**length:** 0..771
                            
                            .. attribute:: vrf_name
                            
                            	DHCPVV6 client/subscriber VRF name
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.client_id = None
                                self.access_vrf_name = None
                                self.class_name = None
                                self.client_flag = None
                                self.duid = None
                                self.framed_ipv6_prefix = None
                                self.framed_prefix_length = None
                                self.ia_id_p_ds = None
                                self.ia_id_pd = Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd()
                                self.ia_id_pd.parent = self
                                self.interface_name = None
                                self.is_nak_next_renew = None
                                self.mac_address = None
                                self.pool_name = None
                                self.profile_name = None
                                self.proxy_binding_inner_tag = None
                                self.proxy_binding_outer_tag = None
                                self.proxy_binding_tags = None
                                self.rx_interface_id = None
                                self.rx_remote_id = None
                                self.serg_intf_role = None
                                self.serg_state = None
                                self.server_ipv6_address = None
                                self.srg_intf_role = None
                                self.srg_state = None
                                self.srg_vrf_name = None
                                self.srgp2p = None
                                self.subscriber_label = None
                                self.tx_interface_id = None
                                self.tx_remote_id = None
                                self.vrf_name = None


                            class IaIdPd(object):
                                """
                                List of DHCPv6 IA\_ID/PDs
                                
                                .. attribute:: bag_dhcpv6d_ia_id_pd_info
                                
                                	bag dhcpv6d ia id pd info
                                	**type**\: list of    :py:class:`BagDhcpv6DIaIdPdInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bag_dhcpv6d_ia_id_pd_info = YList()
                                    self.bag_dhcpv6d_ia_id_pd_info.parent = self
                                    self.bag_dhcpv6d_ia_id_pd_info.name = 'bag_dhcpv6d_ia_id_pd_info'


                                class BagDhcpv6DIaIdPdInfo(object):
                                    """
                                    bag dhcpv6d ia id pd info
                                    
                                    .. attribute:: addresses
                                    
                                    	List of addresses in this IA
                                    	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses>`
                                    
                                    .. attribute:: flags
                                    
                                    	FSM Flag for this IA
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: ia_id
                                    
                                    	IA\_ID of this IA
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: ia_type
                                    
                                    	IA type
                                    	**type**\:   :py:class:`BagDhcpv6DIaIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIaIdEnum>`
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\:   :py:class:`BagDhcpv6DFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DFsmStateEnum>`
                                    
                                    .. attribute:: total_address
                                    
                                    	Total address in this IA
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.addresses = Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses()
                                        self.addresses.parent = self
                                        self.flags = None
                                        self.ia_id = None
                                        self.ia_type = None
                                        self.state = None
                                        self.total_address = None


                                    class Addresses(object):
                                        """
                                        List of addresses in this IA
                                        
                                        .. attribute:: bag_dhcpv6d_addr_attrb
                                        
                                        	bag dhcpv6d addr attrb
                                        	**type**\: list of    :py:class:`BagDhcpv6DAddrAttrb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb>`
                                        
                                        

                                        """

                                        _prefix = 'ipv6-new-dhcpv6d-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.bag_dhcpv6d_addr_attrb = YList()
                                            self.bag_dhcpv6d_addr_attrb.parent = self
                                            self.bag_dhcpv6d_addr_attrb.name = 'bag_dhcpv6d_addr_attrb'


                                        class BagDhcpv6DAddrAttrb(object):
                                            """
                                            bag dhcpv6d addr attrb
                                            
                                            .. attribute:: lease_time
                                            
                                            	Lease time in seconds
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**units**\: second
                                            
                                            .. attribute:: prefix
                                            
                                            	IPv6 prefix
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: prefix_length
                                            
                                            	Prefix length
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: remaining_lease_time
                                            
                                            	Remaining lease time in seconds
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**units**\: second
                                            
                                            

                                            """

                                            _prefix = 'ipv6-new-dhcpv6d-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.lease_time = None
                                                self.prefix = None
                                                self.prefix_length = None
                                                self.remaining_lease_time = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:bag-dhcpv6d-addr-attrb'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.lease_time is not None:
                                                    return True

                                                if self.prefix is not None:
                                                    return True

                                                if self.prefix_length is not None:
                                                    return True

                                                if self.remaining_lease_time is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:addresses'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.bag_dhcpv6d_addr_attrb is not None:
                                                for child_ref in self.bag_dhcpv6d_addr_attrb:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:bag-dhcpv6d-ia-id-pd-info'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.addresses is not None and self.addresses._has_data():
                                            return True

                                        if self.flags is not None:
                                            return True

                                        if self.ia_id is not None:
                                            return True

                                        if self.ia_type is not None:
                                            return True

                                        if self.state is not None:
                                            return True

                                        if self.total_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ia-id-pd'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.bag_dhcpv6d_ia_id_pd_info is not None:
                                        for child_ref in self.bag_dhcpv6d_ia_id_pd_info:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.client_id is None:
                                    raise YPYModelError('Key property client_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client-id = ' + str(self.client_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.client_id is not None:
                                    return True

                                if self.access_vrf_name is not None:
                                    return True

                                if self.class_name is not None:
                                    return True

                                if self.client_flag is not None:
                                    return True

                                if self.duid is not None:
                                    return True

                                if self.framed_ipv6_prefix is not None:
                                    return True

                                if self.framed_prefix_length is not None:
                                    return True

                                if self.ia_id_p_ds is not None:
                                    return True

                                if self.ia_id_pd is not None and self.ia_id_pd._has_data():
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.is_nak_next_renew is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.pool_name is not None:
                                    return True

                                if self.profile_name is not None:
                                    return True

                                if self.proxy_binding_inner_tag is not None:
                                    return True

                                if self.proxy_binding_outer_tag is not None:
                                    return True

                                if self.proxy_binding_tags is not None:
                                    return True

                                if self.rx_interface_id is not None:
                                    return True

                                if self.rx_remote_id is not None:
                                    return True

                                if self.serg_intf_role is not None:
                                    return True

                                if self.serg_state is not None:
                                    return True

                                if self.server_ipv6_address is not None:
                                    return True

                                if self.srg_intf_role is not None:
                                    return True

                                if self.srg_state is not None:
                                    return True

                                if self.srg_vrf_name is not None:
                                    return True

                                if self.srgp2p is not None:
                                    return True

                                if self.subscriber_label is not None:
                                    return True

                                if self.tx_interface_id is not None:
                                    return True

                                if self.tx_remote_id is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:clients'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients']['meta_info']


                    class Summary(object):
                        """
                        DHCPV6 proxy binding summary
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: iana
                        
                        	IANA proxy binding summary
                        	**type**\:   :py:class:`Iana <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana>`
                        
                        .. attribute:: iapd
                        
                        	IAPD proxy binding summary
                        	**type**\:   :py:class:`Iapd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.clients = None
                            self.iana = Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana()
                            self.iana.parent = self
                            self.iapd = Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd()
                            self.iapd.parent = self


                        class Iana(object):
                            """
                            IANA proxy binding summary
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free prefix(ND)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting on iedge to subscriber session
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: msg_waiting_clients
                            
                            	Number of clients waiting for a message from the client/server
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting on RIB response
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bound_clients = None
                                self.daps_waiting_clients = None
                                self.dpm_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.initializing_clients = None
                                self.msg_waiting_clients = None
                                self.rib_waiting_clients = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:iana'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bound_clients is not None:
                                    return True

                                if self.daps_waiting_clients is not None:
                                    return True

                                if self.dpm_waiting_clients is not None:
                                    return True

                                if self.iedge_waiting_clients is not None:
                                    return True

                                if self.initializing_clients is not None:
                                    return True

                                if self.msg_waiting_clients is not None:
                                    return True

                                if self.rib_waiting_clients is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana']['meta_info']


                        class Iapd(object):
                            """
                            IAPD proxy binding summary
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free prefix(ND)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting on iedge to subscriber session
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: msg_waiting_clients
                            
                            	Number of clients waiting for a message from the client/server
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting on RIB response
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bound_clients = None
                                self.daps_waiting_clients = None
                                self.dpm_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.initializing_clients = None
                                self.msg_waiting_clients = None
                                self.rib_waiting_clients = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:iapd'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bound_clients is not None:
                                    return True

                                if self.daps_waiting_clients is not None:
                                    return True

                                if self.dpm_waiting_clients is not None:
                                    return True

                                if self.iedge_waiting_clients is not None:
                                    return True

                                if self.initializing_clients is not None:
                                    return True

                                if self.msg_waiting_clients is not None:
                                    return True

                                if self.rib_waiting_clients is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.clients is not None:
                                return True

                            if self.iana is not None and self.iana._has_data():
                                return True

                            if self.iapd is not None and self.iapd._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Summary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:binding'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Proxy.Binding']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:proxy'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.binding is not None and self.binding._has_data():
                        return True

                    if self.interfaces is not None and self.interfaces._has_data():
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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                    return meta._meta_table['Dhcpv6.Nodes.Node.Proxy']['meta_info']


            class Base(object):
                """
                IPv6 DHCP Base
                
                .. attribute:: addr_bindings
                
                	IPv6 DHCP Base Binding
                	**type**\:   :py:class:`AddrBindings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Base.AddrBindings>`
                
                .. attribute:: database
                
                	DHCP database
                	**type**\:   :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Base.Database>`
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.addr_bindings = Dhcpv6.Nodes.Node.Base.AddrBindings()
                    self.addr_bindings.parent = self
                    self.database = Dhcpv6.Nodes.Node.Base.Database()
                    self.database.parent = self


                class Database(object):
                    """
                    DHCP database
                    
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

                    _prefix = 'ipv6-new-dhcpv6d-oper'
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

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:database'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Base.Database']['meta_info']


                class AddrBindings(object):
                    """
                    IPv6 DHCP Base Binding
                    
                    .. attribute:: addr_binding
                    
                    	DHCPv6 base stats debug
                    	**type**\: list of    :py:class:`AddrBinding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Base.AddrBindings.AddrBinding>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.addr_binding = YList()
                        self.addr_binding.parent = self
                        self.addr_binding.name = 'addr_binding'


                    class AddrBinding(object):
                        """
                        DHCPv6 base stats debug
                        
                        .. attribute:: addr_string  <key>
                        
                        	Address String
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: access_vrf_name
                        
                        	DHCPV6 access interface VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        .. attribute:: base_binding_inner_tag
                        
                        	DHCPV6 VLAN Inner VLAN
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: base_binding_outer_tag
                        
                        	DHCPV6 VLAN Outer VLAN
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: base_binding_tags
                        
                        	DHCPV6 VLAN tag count
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: interface_name
                        
                        	DHCPV6 access interface to client
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: ipv6_address
                        
                        	DHCPV6 IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_nak_next_renew
                        
                        	Is true if DHCPV6 next renew from client will be NAK'd
                        	**type**\:  bool
                        
                        .. attribute:: lease_time
                        
                        	Lease time in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: mac_address
                        
                        	DHCPV6 client MAC address
                        	**type**\:  str
                        
                        .. attribute:: old_subscriber_label
                        
                        	DHCPV6 old subscriber label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: profile_name
                        
                        	DHCPV6 profile name
                        	**type**\:  str
                        
                        	**length:** 0..64
                        
                        .. attribute:: remaining_lease_time
                        
                        	Remaining lease time in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: reply_server_ipv6_address
                        
                        	DHCPV6 reply server IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: rx_client_duid
                        
                        	DHCPV6 received client DUID
                        	**type**\:  str
                        
                        	**length:** 0..771
                        
                        .. attribute:: rx_interface_id
                        
                        	DHCPV6 received Interface ID
                        	**type**\:  str
                        
                        	**length:** 0..771
                        
                        .. attribute:: rx_remote_id
                        
                        	DHCPV6 received Remote ID
                        	**type**\:  str
                        
                        	**length:** 0..771
                        
                        .. attribute:: server_ipv6_address
                        
                        	DHCPV6 server IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: server_vrf_name
                        
                        	DHCPV6 server VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        .. attribute:: state
                        
                        	DHCPV6 client state
                        	**type**\:   :py:class:`BagDhcpv6DFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DFsmStateEnum>`
                        
                        .. attribute:: subscriber_label
                        
                        	DHCPV6 subscriber label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tx_client_uid
                        
                        	DHCPV6 transmitted client DUID
                        	**type**\:  str
                        
                        	**length:** 0..771
                        
                        .. attribute:: tx_interface_id
                        
                        	DHCPV6 transmitted Interface ID
                        	**type**\:  str
                        
                        	**length:** 0..771
                        
                        .. attribute:: tx_remote_id
                        
                        	DHCPV6 transmitted Remote ID
                        	**type**\:  str
                        
                        	**length:** 0..771
                        
                        .. attribute:: vrf_name
                        
                        	DHCPV6 client/subscriber VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.addr_string = None
                            self.access_vrf_name = None
                            self.base_binding_inner_tag = None
                            self.base_binding_outer_tag = None
                            self.base_binding_tags = None
                            self.interface_name = None
                            self.ipv6_address = None
                            self.is_nak_next_renew = None
                            self.lease_time = None
                            self.mac_address = None
                            self.old_subscriber_label = None
                            self.profile_name = None
                            self.remaining_lease_time = None
                            self.reply_server_ipv6_address = None
                            self.rx_client_duid = None
                            self.rx_interface_id = None
                            self.rx_remote_id = None
                            self.server_ipv6_address = None
                            self.server_vrf_name = None
                            self.state = None
                            self.subscriber_label = None
                            self.tx_client_uid = None
                            self.tx_interface_id = None
                            self.tx_remote_id = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.addr_string is None:
                                raise YPYModelError('Key property addr_string is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:addr-binding[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:addr-string = ' + str(self.addr_string) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.addr_string is not None:
                                return True

                            if self.access_vrf_name is not None:
                                return True

                            if self.base_binding_inner_tag is not None:
                                return True

                            if self.base_binding_outer_tag is not None:
                                return True

                            if self.base_binding_tags is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            if self.is_nak_next_renew is not None:
                                return True

                            if self.lease_time is not None:
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.old_subscriber_label is not None:
                                return True

                            if self.profile_name is not None:
                                return True

                            if self.remaining_lease_time is not None:
                                return True

                            if self.reply_server_ipv6_address is not None:
                                return True

                            if self.rx_client_duid is not None:
                                return True

                            if self.rx_interface_id is not None:
                                return True

                            if self.rx_remote_id is not None:
                                return True

                            if self.server_ipv6_address is not None:
                                return True

                            if self.server_vrf_name is not None:
                                return True

                            if self.state is not None:
                                return True

                            if self.subscriber_label is not None:
                                return True

                            if self.tx_client_uid is not None:
                                return True

                            if self.tx_interface_id is not None:
                                return True

                            if self.tx_remote_id is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Base.AddrBindings.AddrBinding']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:addr-bindings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.addr_binding is not None:
                            for child_ref in self.addr_binding:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Base.AddrBindings']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:base'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.addr_bindings is not None and self.addr_bindings._has_data():
                        return True

                    if self.database is not None and self.database._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                    return meta._meta_table['Dhcpv6.Nodes.Node.Base']['meta_info']


            class Server(object):
                """
                IPv6 DHCP server operational data
                
                .. attribute:: binding
                
                	DHCPV6 server bindings
                	**type**\:   :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding>`
                
                .. attribute:: binding_options
                
                	DHCPv6 server binding with options
                	**type**\:   :py:class:`BindingOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.BindingOptions>`
                
                .. attribute:: interfaces
                
                	DHCPV6 server interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Interfaces>`
                
                .. attribute:: profiles
                
                	IPv6 DHCP server profile
                	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles>`
                
                .. attribute:: statistics
                
                	DHCPv6 server statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Statistics>`
                
                .. attribute:: vrfs
                
                	DHCPV6 server list of VRF names
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs>`
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.binding = Dhcpv6.Nodes.Node.Server.Binding()
                    self.binding.parent = self
                    self.binding_options = Dhcpv6.Nodes.Node.Server.BindingOptions()
                    self.binding_options.parent = self
                    self.interfaces = Dhcpv6.Nodes.Node.Server.Interfaces()
                    self.interfaces.parent = self
                    self.profiles = Dhcpv6.Nodes.Node.Server.Profiles()
                    self.profiles.parent = self
                    self.statistics = Dhcpv6.Nodes.Node.Server.Statistics()
                    self.statistics.parent = self
                    self.vrfs = Dhcpv6.Nodes.Node.Server.Vrfs()
                    self.vrfs.parent = self


                class Binding(object):
                    """
                    DHCPV6 server bindings
                    
                    .. attribute:: clients
                    
                    	DHCPV6 server client bindings
                    	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients>`
                    
                    .. attribute:: summary
                    
                    	DHCPV6 server binding summary
                    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Summary>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.clients = Dhcpv6.Nodes.Node.Server.Binding.Clients()
                        self.clients.parent = self
                        self.summary = Dhcpv6.Nodes.Node.Server.Binding.Summary()
                        self.summary.parent = self


                    class Summary(object):
                        """
                        DHCPV6 server binding summary
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: iana
                        
                        	IANA server binding summary
                        	**type**\:   :py:class:`Iana <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana>`
                        
                        .. attribute:: iapd
                        
                        	IAPD server binding summary
                        	**type**\:   :py:class:`Iapd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.clients = None
                            self.iana = Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana()
                            self.iana.parent = self
                            self.iapd = Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd()
                            self.iapd.parent = self


                        class Iana(object):
                            """
                            IANA server binding summary
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free addr/prefix
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting for iedge for the session
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_waiting_clients
                            
                            	Number of clients waiting for a request from the client
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting for RIB response
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bound_clients = None
                                self.daps_waiting_clients = None
                                self.dpm_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.initializing_clients = None
                                self.request_waiting_clients = None
                                self.rib_waiting_clients = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:iana'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bound_clients is not None:
                                    return True

                                if self.daps_waiting_clients is not None:
                                    return True

                                if self.dpm_waiting_clients is not None:
                                    return True

                                if self.iedge_waiting_clients is not None:
                                    return True

                                if self.initializing_clients is not None:
                                    return True

                                if self.request_waiting_clients is not None:
                                    return True

                                if self.rib_waiting_clients is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana']['meta_info']


                        class Iapd(object):
                            """
                            IAPD server binding summary
                            
                            .. attribute:: bound_clients
                            
                            	Number of clients in bound state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: daps_waiting_clients
                            
                            	Number of clients waiting on DAPS to assign/free addr/prefix
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dpm_waiting_clients
                            
                            	Number of clients waiting on DPM to validate subscriber
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iedge_waiting_clients
                            
                            	Number of clients waiting for iedge for the session
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initializing_clients
                            
                            	Number of clients in init state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_waiting_clients
                            
                            	Number of clients waiting for a request from the client
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rib_waiting_clients
                            
                            	Number of clients in waiting for RIB response
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bound_clients = None
                                self.daps_waiting_clients = None
                                self.dpm_waiting_clients = None
                                self.iedge_waiting_clients = None
                                self.initializing_clients = None
                                self.request_waiting_clients = None
                                self.rib_waiting_clients = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:iapd'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bound_clients is not None:
                                    return True

                                if self.daps_waiting_clients is not None:
                                    return True

                                if self.dpm_waiting_clients is not None:
                                    return True

                                if self.iedge_waiting_clients is not None:
                                    return True

                                if self.initializing_clients is not None:
                                    return True

                                if self.request_waiting_clients is not None:
                                    return True

                                if self.rib_waiting_clients is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.clients is not None:
                                return True

                            if self.iana is not None and self.iana._has_data():
                                return True

                            if self.iapd is not None and self.iapd._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Summary']['meta_info']


                    class Clients(object):
                        """
                        DHCPV6 server client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCPV6 server binding
                        	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.client = YList()
                            self.client.parent = self
                            self.client.name = 'client'


                        class Client(object):
                            """
                            Single DHCPV6 server binding
                            
                            .. attribute:: client_id  <key>
                            
                            	Client ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: access_vrf_name
                            
                            	DHCPV6 access VRF name to client
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: address_pool_name
                            
                            	DHCPV6 server address pool name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: class_name
                            
                            	DHCPV6 class name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: client_flag
                            
                            	DHCPV6 client flag
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: client_id_xr
                            
                            	Client unique identifier
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dns_server_count
                            
                            	DNS server count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duid
                            
                            	Client DUID
                            	**type**\:  str
                            
                            .. attribute:: framed_ipv6_prefix
                            
                            	DHCPV6 framed ipv6 addess used by ND
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: framed_prefix_length
                            
                            	DHCPV6 framed ipv6 prefix length used by ND
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ia_id_p_ds
                            
                            	Number of ia\_id/pd
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ia_id_pd
                            
                            	List of DHCPv6 IA\_ID/PDs
                            	**type**\:   :py:class:`IaIdPd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd>`
                            
                            .. attribute:: interface_name
                            
                            	DHCPV6 access interface to client
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: is_nak_next_renew
                            
                            	Is true if DHCPv6 next renew from client will be NAK'd
                            	**type**\:  bool
                            
                            .. attribute:: link_local_address
                            
                            	DHCPV6 IPv6 client link local address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: mac_address
                            
                            	Client MAC address
                            	**type**\:  str
                            
                            .. attribute:: pool_name
                            
                            	DHCPV6 pool name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: prefix_pool_name
                            
                            	DHCPV6 server prefix pool name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: profile_name
                            
                            	DHCPV6 profile name
                            	**type**\:  str
                            
                            	**length:** 0..64
                            
                            .. attribute:: rx_interface_id
                            
                            	DHCPV6 received Interface ID
                            	**type**\:  str
                            
                            	**length:** 0..771
                            
                            .. attribute:: rx_remote_id
                            
                            	DHCPV6 received Remote ID
                            	**type**\:  str
                            
                            	**length:** 0..771
                            
                            .. attribute:: serg_intf_role
                            
                            	DHCPV6 SERG Intf Role
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: server_binding_inner_tag
                            
                            	DHCPV6 VLAN Inner VLAN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: server_binding_outer_tag
                            
                            	DHCPV6 VLAN Outer VLAN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: server_binding_tags
                            
                            	DHCPV6 VLAN tag count
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: sesrg_state
                            
                            	DHCPV6 SERG state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srg_intf_role
                            
                            	DHCPV6 SRG Intf Role
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srg_state
                            
                            	DHCPV6 SRG state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srg_vrf_name
                            
                            	DHCPV6 SRG VRF NAME
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: srgp2p
                            
                            	SRG P2P Status
                            	**type**\:  bool
                            
                            .. attribute:: subscriber_label
                            
                            	DHCPV6 subscriber label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_name
                            
                            	DHCPVV6 client/subscriber VRF name
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.client_id = None
                                self.access_vrf_name = None
                                self.address_pool_name = None
                                self.class_name = None
                                self.client_flag = None
                                self.client_id_xr = None
                                self.dns_server_count = None
                                self.duid = None
                                self.framed_ipv6_prefix = None
                                self.framed_prefix_length = None
                                self.ia_id_p_ds = None
                                self.ia_id_pd = Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd()
                                self.ia_id_pd.parent = self
                                self.interface_name = None
                                self.is_nak_next_renew = None
                                self.link_local_address = None
                                self.mac_address = None
                                self.pool_name = None
                                self.prefix_pool_name = None
                                self.profile_name = None
                                self.rx_interface_id = None
                                self.rx_remote_id = None
                                self.serg_intf_role = None
                                self.server_binding_inner_tag = None
                                self.server_binding_outer_tag = None
                                self.server_binding_tags = None
                                self.sesrg_state = None
                                self.srg_intf_role = None
                                self.srg_state = None
                                self.srg_vrf_name = None
                                self.srgp2p = None
                                self.subscriber_label = None
                                self.vrf_name = None


                            class IaIdPd(object):
                                """
                                List of DHCPv6 IA\_ID/PDs
                                
                                .. attribute:: bag_dhcpv6d_ia_id_pd_info
                                
                                	bag dhcpv6d ia id pd info
                                	**type**\: list of    :py:class:`BagDhcpv6DIaIdPdInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bag_dhcpv6d_ia_id_pd_info = YList()
                                    self.bag_dhcpv6d_ia_id_pd_info.parent = self
                                    self.bag_dhcpv6d_ia_id_pd_info.name = 'bag_dhcpv6d_ia_id_pd_info'


                                class BagDhcpv6DIaIdPdInfo(object):
                                    """
                                    bag dhcpv6d ia id pd info
                                    
                                    .. attribute:: addresses
                                    
                                    	List of addresses in this IA
                                    	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses>`
                                    
                                    .. attribute:: flags
                                    
                                    	FSM Flag for this IA
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: ia_id
                                    
                                    	IA\_ID of this IA
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: ia_type
                                    
                                    	IA type
                                    	**type**\:   :py:class:`BagDhcpv6DIaIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIaIdEnum>`
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\:   :py:class:`BagDhcpv6DFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DFsmStateEnum>`
                                    
                                    .. attribute:: total_address
                                    
                                    	Total address in this IA
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.addresses = Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses()
                                        self.addresses.parent = self
                                        self.flags = None
                                        self.ia_id = None
                                        self.ia_type = None
                                        self.state = None
                                        self.total_address = None


                                    class Addresses(object):
                                        """
                                        List of addresses in this IA
                                        
                                        .. attribute:: bag_dhcpv6d_addr_attrb
                                        
                                        	bag dhcpv6d addr attrb
                                        	**type**\: list of    :py:class:`BagDhcpv6DAddrAttrb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb>`
                                        
                                        

                                        """

                                        _prefix = 'ipv6-new-dhcpv6d-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.bag_dhcpv6d_addr_attrb = YList()
                                            self.bag_dhcpv6d_addr_attrb.parent = self
                                            self.bag_dhcpv6d_addr_attrb.name = 'bag_dhcpv6d_addr_attrb'


                                        class BagDhcpv6DAddrAttrb(object):
                                            """
                                            bag dhcpv6d addr attrb
                                            
                                            .. attribute:: lease_time
                                            
                                            	Lease time in seconds
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**units**\: second
                                            
                                            .. attribute:: prefix
                                            
                                            	IPv6 prefix
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: prefix_length
                                            
                                            	Prefix length
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: remaining_lease_time
                                            
                                            	Remaining lease time in seconds
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**units**\: second
                                            
                                            

                                            """

                                            _prefix = 'ipv6-new-dhcpv6d-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.lease_time = None
                                                self.prefix = None
                                                self.prefix_length = None
                                                self.remaining_lease_time = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:bag-dhcpv6d-addr-attrb'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.lease_time is not None:
                                                    return True

                                                if self.prefix is not None:
                                                    return True

                                                if self.prefix_length is not None:
                                                    return True

                                                if self.remaining_lease_time is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:addresses'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.bag_dhcpv6d_addr_attrb is not None:
                                                for child_ref in self.bag_dhcpv6d_addr_attrb:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:bag-dhcpv6d-ia-id-pd-info'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.addresses is not None and self.addresses._has_data():
                                            return True

                                        if self.flags is not None:
                                            return True

                                        if self.ia_id is not None:
                                            return True

                                        if self.ia_type is not None:
                                            return True

                                        if self.state is not None:
                                            return True

                                        if self.total_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ia-id-pd'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.bag_dhcpv6d_ia_id_pd_info is not None:
                                        for child_ref in self.bag_dhcpv6d_ia_id_pd_info:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.client_id is None:
                                    raise YPYModelError('Key property client_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client-id = ' + str(self.client_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.client_id is not None:
                                    return True

                                if self.access_vrf_name is not None:
                                    return True

                                if self.address_pool_name is not None:
                                    return True

                                if self.class_name is not None:
                                    return True

                                if self.client_flag is not None:
                                    return True

                                if self.client_id_xr is not None:
                                    return True

                                if self.dns_server_count is not None:
                                    return True

                                if self.duid is not None:
                                    return True

                                if self.framed_ipv6_prefix is not None:
                                    return True

                                if self.framed_prefix_length is not None:
                                    return True

                                if self.ia_id_p_ds is not None:
                                    return True

                                if self.ia_id_pd is not None and self.ia_id_pd._has_data():
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.is_nak_next_renew is not None:
                                    return True

                                if self.link_local_address is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.pool_name is not None:
                                    return True

                                if self.prefix_pool_name is not None:
                                    return True

                                if self.profile_name is not None:
                                    return True

                                if self.rx_interface_id is not None:
                                    return True

                                if self.rx_remote_id is not None:
                                    return True

                                if self.serg_intf_role is not None:
                                    return True

                                if self.server_binding_inner_tag is not None:
                                    return True

                                if self.server_binding_outer_tag is not None:
                                    return True

                                if self.server_binding_tags is not None:
                                    return True

                                if self.sesrg_state is not None:
                                    return True

                                if self.srg_intf_role is not None:
                                    return True

                                if self.srg_state is not None:
                                    return True

                                if self.srg_vrf_name is not None:
                                    return True

                                if self.srgp2p is not None:
                                    return True

                                if self.subscriber_label is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:clients'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:binding'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Binding']['meta_info']


                class Vrfs(object):
                    """
                    DHCPV6 server list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP server VRF name
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        IPv6 DHCP server VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv6 DHCP server statistics
                        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.statistics = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self


                        class Statistics(object):
                            """
                            IPv6 DHCP server statistics
                            
                            .. attribute:: advertise
                            
                            	DHCPV6 advertise packets
                            	**type**\:   :py:class:`Advertise <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise>`
                            
                            .. attribute:: confirm
                            
                            	DHCPV6 confirm packets
                            	**type**\:   :py:class:`Confirm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm>`
                            
                            .. attribute:: decline
                            
                            	DHCPV6 decline packets
                            	**type**\:   :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: inform
                            
                            	DHCPV6 inform packets
                            	**type**\:   :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: lease_query
                            
                            	DHCPV6 lease query packets
                            	**type**\:   :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_query_data
                            
                            	DHCPV6 lease query data packets
                            	**type**\:   :py:class:`LeaseQueryData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData>`
                            
                            .. attribute:: lease_query_done
                            
                            	DHCPV6 lease query done packets
                            	**type**\:   :py:class:`LeaseQueryDone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone>`
                            
                            .. attribute:: lease_query_reply
                            
                            	DHCPV6 lease query reply packets
                            	**type**\:   :py:class:`LeaseQueryReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply>`
                            
                            .. attribute:: rebind
                            
                            	DHCPV6 rebind packets
                            	**type**\:   :py:class:`Rebind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind>`
                            
                            .. attribute:: reconfig
                            
                            	DHCPV6 reconfig packets
                            	**type**\:   :py:class:`Reconfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig>`
                            
                            .. attribute:: relay_forward
                            
                            	DHCPV6 relay forward packets
                            	**type**\:   :py:class:`RelayForward <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward>`
                            
                            .. attribute:: relay_reply
                            
                            	DHCPV6 relay reply packets
                            	**type**\:   :py:class:`RelayReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply>`
                            
                            .. attribute:: release
                            
                            	DHCPV6 release packets
                            	**type**\:   :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: renew
                            
                            	DHCPV6 renew packets
                            	**type**\:   :py:class:`Renew <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew>`
                            
                            .. attribute:: reply
                            
                            	DHCPV6 reply packets
                            	**type**\:   :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply>`
                            
                            .. attribute:: request
                            
                            	DHCPV6 request packets
                            	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: solicit
                            
                            	DHCPV6 solicit packets
                            	**type**\:   :py:class:`Solicit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.advertise = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise()
                                self.advertise.parent = self
                                self.confirm = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm()
                                self.confirm.parent = self
                                self.decline = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self.inform = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self.lease_query = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self.lease_query_data = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData()
                                self.lease_query_data.parent = self
                                self.lease_query_done = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone()
                                self.lease_query_done.parent = self
                                self.lease_query_reply = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply()
                                self.lease_query_reply.parent = self
                                self.rebind = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind()
                                self.rebind.parent = self
                                self.reconfig = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig()
                                self.reconfig.parent = self
                                self.relay_forward = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward()
                                self.relay_forward.parent = self
                                self.relay_reply = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply()
                                self.relay_reply.parent = self
                                self.release = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self.renew = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew()
                                self.renew.parent = self
                                self.reply = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply()
                                self.reply.parent = self
                                self.request = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self.solicit = Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit()
                                self.solicit.parent = self


                            class Solicit(object):
                                """
                                DHCPV6 solicit packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:solicit'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit']['meta_info']


                            class Advertise(object):
                                """
                                DHCPV6 advertise packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:advertise'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise']['meta_info']


                            class Request(object):
                                """
                                DHCPV6 request packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:request'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request']['meta_info']


                            class Reply(object):
                                """
                                DHCPV6 reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reply'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply']['meta_info']


                            class Confirm(object):
                                """
                                DHCPV6 confirm packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:confirm'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm']['meta_info']


                            class Decline(object):
                                """
                                DHCPV6 decline packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:decline'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline']['meta_info']


                            class Renew(object):
                                """
                                DHCPV6 renew packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:renew'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew']['meta_info']


                            class Rebind(object):
                                """
                                DHCPV6 rebind packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:rebind'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind']['meta_info']


                            class Release(object):
                                """
                                DHCPV6 release packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:release'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release']['meta_info']


                            class Reconfig(object):
                                """
                                DHCPV6 reconfig packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reconfig'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig']['meta_info']


                            class Inform(object):
                                """
                                DHCPV6 inform packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:inform'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform']['meta_info']


                            class RelayForward(object):
                                """
                                DHCPV6 relay forward packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-forward'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward']['meta_info']


                            class RelayReply(object):
                                """
                                DHCPV6 relay reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-reply'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply']['meta_info']


                            class LeaseQuery(object):
                                """
                                DHCPV6 lease query packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info']


                            class LeaseQueryReply(object):
                                """
                                DHCPV6 lease query reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-reply'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply']['meta_info']


                            class LeaseQueryDone(object):
                                """
                                DHCPV6 lease query done packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-done'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone']['meta_info']


                            class LeaseQueryData(object):
                                """
                                DHCPV6 lease query data packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-data'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.advertise is not None and self.advertise._has_data():
                                    return True

                                if self.confirm is not None and self.confirm._has_data():
                                    return True

                                if self.decline is not None and self.decline._has_data():
                                    return True

                                if self.inform is not None and self.inform._has_data():
                                    return True

                                if self.lease_query is not None and self.lease_query._has_data():
                                    return True

                                if self.lease_query_data is not None and self.lease_query_data._has_data():
                                    return True

                                if self.lease_query_done is not None and self.lease_query_done._has_data():
                                    return True

                                if self.lease_query_reply is not None and self.lease_query_reply._has_data():
                                    return True

                                if self.rebind is not None and self.rebind._has_data():
                                    return True

                                if self.reconfig is not None and self.reconfig._has_data():
                                    return True

                                if self.relay_forward is not None and self.relay_forward._has_data():
                                    return True

                                if self.relay_reply is not None and self.relay_reply._has_data():
                                    return True

                                if self.release is not None and self.release._has_data():
                                    return True

                                if self.renew is not None and self.renew._has_data():
                                    return True

                                if self.reply is not None and self.reply._has_data():
                                    return True

                                if self.request is not None and self.request._has_data():
                                    return True

                                if self.solicit is not None and self.solicit._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf-name = ' + str(self.vrf_name) + ']'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrfs'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Vrfs']['meta_info']


                class Profiles(object):
                    """
                    IPv6 DHCP server profile
                    
                    .. attribute:: profile
                    
                    	IPv6 DHCP server profile
                    	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.profile = YList()
                        self.profile.parent = self
                        self.profile.name = 'profile'


                    class Profile(object):
                        """
                        IPv6 DHCP server profile
                        
                        .. attribute:: profile_name  <key>
                        
                        	Profile name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: info
                        
                        	IPv6 DHCP server profile Info
                        	**type**\:   :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info>`
                        
                        .. attribute:: throttle_infos
                        
                        	DHCPV6 throttle table
                        	**type**\:   :py:class:`ThrottleInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.profile_name = None
                            self.info = Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info()
                            self.info.parent = self
                            self.throttle_infos = Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos()
                            self.throttle_infos.parent = self


                        class Info(object):
                            """
                            IPv6 DHCP server profile Info
                            
                            .. attribute:: aftr_name
                            
                            	Server aftr name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            .. attribute:: delegated_prefix_pool_name
                            
                            	Server delegated prefix pool name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            .. attribute:: domain_name
                            
                            	Server domain name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            .. attribute:: framed_addr_pool_name
                            
                            	Server framed address pool name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            .. attribute:: interface_references
                            
                            	Interface references
                            	**type**\:   :py:class:`InterfaceReferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences>`
                            
                            .. attribute:: lease
                            
                            	Server lease time
                            	**type**\:   :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease>`
                            
                            .. attribute:: profile_dns
                            
                            	DNS address count
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: profile_dns_address
                            
                            	DNS addresses
                            	**type**\:  list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: profile_name
                            
                            	Server profile name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            .. attribute:: rapid_commit
                            
                            	Rapid Commit
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.aftr_name = None
                                self.delegated_prefix_pool_name = None
                                self.domain_name = None
                                self.framed_addr_pool_name = None
                                self.interface_references = Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences()
                                self.interface_references.parent = self
                                self.lease = Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease()
                                self.lease.parent = self
                                self.profile_dns = None
                                self.profile_dns_address = YLeafList()
                                self.profile_dns_address.parent = self
                                self.profile_dns_address.name = 'profile_dns_address'
                                self.profile_name = None
                                self.rapid_commit = None


                            class Lease(object):
                                """
                                Server lease time
                                
                                .. attribute:: seconds
                                
                                	DHCPV6 client lease in seconds
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: time
                                
                                	Time in format HH\:MM\:SS
                                	**type**\:  str
                                
                                	**length:** 0..10
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.seconds = None
                                    self.time = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.seconds is not None:
                                        return True

                                    if self.time is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease']['meta_info']


                            class InterfaceReferences(object):
                                """
                                Interface references
                                
                                .. attribute:: ipv6_dhcpv6d_server_interface_reference
                                
                                	ipv6 dhcpv6d server interface reference
                                	**type**\: list of    :py:class:`Ipv6Dhcpv6DServerInterfaceReference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ipv6_dhcpv6d_server_interface_reference = YList()
                                    self.ipv6_dhcpv6d_server_interface_reference.parent = self
                                    self.ipv6_dhcpv6d_server_interface_reference.name = 'ipv6_dhcpv6d_server_interface_reference'


                                class Ipv6Dhcpv6DServerInterfaceReference(object):
                                    """
                                    ipv6 dhcpv6d server interface reference
                                    
                                    .. attribute:: server_reference_interface_name
                                    
                                    	Interface name
                                    	**type**\:  str
                                    
                                    	**length:** 0..65
                                    
                                    

                                    """

                                    _prefix = 'ipv6-new-dhcpv6d-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.server_reference_interface_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-server-interface-reference'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.server_reference_interface_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interface-references'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.ipv6_dhcpv6d_server_interface_reference is not None:
                                        for child_ref in self.ipv6_dhcpv6d_server_interface_reference:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.aftr_name is not None:
                                    return True

                                if self.delegated_prefix_pool_name is not None:
                                    return True

                                if self.domain_name is not None:
                                    return True

                                if self.framed_addr_pool_name is not None:
                                    return True

                                if self.interface_references is not None and self.interface_references._has_data():
                                    return True

                                if self.lease is not None and self.lease._has_data():
                                    return True

                                if self.profile_dns is not None:
                                    return True

                                if self.profile_dns_address is not None:
                                    for child in self.profile_dns_address:
                                        if child is not None:
                                            return True

                                if self.profile_name is not None:
                                    return True

                                if self.rapid_commit is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info']['meta_info']


                        class ThrottleInfos(object):
                            """
                            DHCPV6 throttle table
                            
                            .. attribute:: throttle_info
                            
                            	IPv6 DHCP server profile Throttle Info
                            	**type**\: list of    :py:class:`ThrottleInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.throttle_info = YList()
                                self.throttle_info.parent = self
                                self.throttle_info.name = 'throttle_info'


                            class ThrottleInfo(object):
                                """
                                IPv6 DHCP server profile Throttle Info
                                
                                .. attribute:: mac_address  <key>
                                
                                	MAC address
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: binding_chaddr
                                
                                	Client MAC address
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: ifname
                                
                                	DHCP access interface
                                	**type**\:  str
                                
                                	**length:** 0..65
                                
                                .. attribute:: state
                                
                                	State of entry
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_left
                                
                                	Time Left in secs
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mac_address = None
                                    self.binding_chaddr = None
                                    self.ifname = None
                                    self.state = None
                                    self.time_left = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.mac_address is None:
                                        raise YPYModelError('Key property mac_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:throttle-info[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:mac-address = ' + str(self.mac_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.mac_address is not None:
                                        return True

                                    if self.binding_chaddr is not None:
                                        return True

                                    if self.ifname is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    if self.time_left is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:throttle-infos'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.throttle_info is not None:
                                    for child_ref in self.throttle_info:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.profile_name is None:
                                raise YPYModelError('Key property profile_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profile[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profile-name = ' + str(self.profile_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.profile_name is not None:
                                return True

                            if self.info is not None and self.info._has_data():
                                return True

                            if self.throttle_infos is not None and self.throttle_infos._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:profiles'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Profiles']['meta_info']


                class Interfaces(object):
                    """
                    DHCPV6 server interface
                    
                    .. attribute:: interface
                    
                    	IPv6 DHCP server interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        IPv6 DHCP server interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface Name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: is_server_interface_ambiguous
                        
                        	Is interface ambiguous
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mac_throttle
                        
                        	Mac Throttle Status
                        	**type**\:  bool
                        
                        .. attribute:: serg_role
                        
                        	DHCPv6 Interface SERG role
                        	**type**\:   :py:class:`BagDhcpv6DIntfSergRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIntfSergRoleEnum>`
                        
                        .. attribute:: server_interface_lease_limit_type
                        
                        	Lease limit type on interface
                        	**type**\:   :py:class:`LeaseLimitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.LeaseLimitEnum>`
                        
                        .. attribute:: server_interface_lease_limits
                        
                        	Lease limit count on interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: server_interface_mode
                        
                        	Mode of interface
                        	**type**\:   :py:class:`BagDhcpv6DSubModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DSubModeEnum>`
                        
                        .. attribute:: server_interface_profile_name
                        
                        	Name of profile attached to the interface
                        	**type**\:  str
                        
                        	**length:** 0..65
                        
                        .. attribute:: server_vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        .. attribute:: srg_role
                        
                        	DHCPv6 Interface SRG role
                        	**type**\:   :py:class:`BagDhcpv6DIntfSrgRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.BagDhcpv6DIntfSrgRoleEnum>`
                        
                        .. attribute:: srg_vrf_name
                        
                        	SRG VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        .. attribute:: srgp2p
                        
                        	SRG P2P Status
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.is_server_interface_ambiguous = None
                            self.mac_throttle = None
                            self.serg_role = None
                            self.server_interface_lease_limit_type = None
                            self.server_interface_lease_limits = None
                            self.server_interface_mode = None
                            self.server_interface_profile_name = None
                            self.server_vrf_name = None
                            self.srg_role = None
                            self.srg_vrf_name = None
                            self.srgp2p = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interface[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.is_server_interface_ambiguous is not None:
                                return True

                            if self.mac_throttle is not None:
                                return True

                            if self.serg_role is not None:
                                return True

                            if self.server_interface_lease_limit_type is not None:
                                return True

                            if self.server_interface_lease_limits is not None:
                                return True

                            if self.server_interface_mode is not None:
                                return True

                            if self.server_interface_profile_name is not None:
                                return True

                            if self.server_vrf_name is not None:
                                return True

                            if self.srg_role is not None:
                                return True

                            if self.srg_vrf_name is not None:
                                return True

                            if self.srgp2p is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:interfaces'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Interfaces']['meta_info']


                class Statistics(object):
                    """
                    DHCPv6 server statistics
                    
                    .. attribute:: ipv6_dhcpv6d_server_stat
                    
                    	ipv6 dhcpv6d server stat
                    	**type**\: list of    :py:class:`Ipv6Dhcpv6DServerStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_dhcpv6d_server_stat = YList()
                        self.ipv6_dhcpv6d_server_stat.parent = self
                        self.ipv6_dhcpv6d_server_stat.name = 'ipv6_dhcpv6d_server_stat'


                    class Ipv6Dhcpv6DServerStat(object):
                        """
                        ipv6 dhcpv6d server stat
                        
                        .. attribute:: statistics
                        
                        	Server statistics
                        	**type**\:   :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCPv6 L3 VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.statistics = Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_()
                            self.statistics.parent = self
                            self.vrf_name = None


                        class Statistics_(object):
                            """
                            Server statistics
                            
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

                            _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-server-stat'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv6_dhcpv6d_server_stat is not None:
                            for child_ref in self.ipv6_dhcpv6d_server_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.Statistics']['meta_info']


                class BindingOptions(object):
                    """
                    DHCPv6 server binding with options
                    
                    .. attribute:: duid_bind_options
                    
                    	DHCPv6 server binding from DUID
                    	**type**\:   :py:class:`DuidBindOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions>`
                    
                    .. attribute:: mac_bind_options
                    
                    	DHCPv6 server binding from MAC address
                    	**type**\:   :py:class:`MacBindOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.duid_bind_options = Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions()
                        self.duid_bind_options.parent = self
                        self.mac_bind_options = Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions()
                        self.mac_bind_options.parent = self


                    class MacBindOptions(object):
                        """
                        DHCPv6 server binding from MAC address
                        
                        .. attribute:: mac_bind_option
                        
                        	DHCPv6 server binding with options
                        	**type**\: list of    :py:class:`MacBindOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions.MacBindOption>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.mac_bind_option = YList()
                            self.mac_bind_option.parent = self
                            self.mac_bind_option.name = 'mac_bind_option'


                        class MacBindOption(object):
                            """
                            DHCPv6 server binding with options
                            
                            .. attribute:: mac_address  <key>
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: dns_address
                            
                            	DNS addresses
                            	**type**\:  list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: dns_count
                            
                            	DNS address count
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: duid_xr
                            
                            	Client DUID
                            	**type**\:  str
                            
                            .. attribute:: mac_address_xr
                            
                            	Client MAC address
                            	**type**\:  str
                            
                            .. attribute:: opt17
                            
                            	Client Option 17 value
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mac_address = None
                                self.dns_address = YLeafList()
                                self.dns_address.parent = self
                                self.dns_address.name = 'dns_address'
                                self.dns_count = None
                                self.duid_xr = None
                                self.mac_address_xr = None
                                self.opt17 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.mac_address is None:
                                    raise YPYModelError('Key property mac_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:mac-bind-option[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:mac-address = ' + str(self.mac_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mac_address is not None:
                                    return True

                                if self.dns_address is not None:
                                    for child in self.dns_address:
                                        if child is not None:
                                            return True

                                if self.dns_count is not None:
                                    return True

                                if self.duid_xr is not None:
                                    return True

                                if self.mac_address_xr is not None:
                                    return True

                                if self.opt17 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions.MacBindOption']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:mac-bind-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.mac_bind_option is not None:
                                for child_ref in self.mac_bind_option:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions']['meta_info']


                    class DuidBindOptions(object):
                        """
                        DHCPv6 server binding from DUID
                        
                        .. attribute:: duid_bind_option
                        
                        	DHCPv6 server binding with options
                        	**type**\: list of    :py:class:`DuidBindOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions.DuidBindOption>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.duid_bind_option = YList()
                            self.duid_bind_option.parent = self
                            self.duid_bind_option.name = 'duid_bind_option'


                        class DuidBindOption(object):
                            """
                            DHCPv6 server binding with options
                            
                            .. attribute:: duid  <key>
                            
                            	DUID of Binding
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: dns_address
                            
                            	DNS addresses
                            	**type**\:  list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: dns_count
                            
                            	DNS address count
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: duid_xr
                            
                            	Client DUID
                            	**type**\:  str
                            
                            .. attribute:: mac_address_xr
                            
                            	Client MAC address
                            	**type**\:  str
                            
                            .. attribute:: opt17
                            
                            	Client Option 17 value
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.duid = None
                                self.dns_address = YLeafList()
                                self.dns_address.parent = self
                                self.dns_address.name = 'dns_address'
                                self.dns_count = None
                                self.duid_xr = None
                                self.mac_address_xr = None
                                self.opt17 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.duid is None:
                                    raise YPYModelError('Key property duid is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:duid-bind-option[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:duid = ' + str(self.duid) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.duid is not None:
                                    return True

                                if self.dns_address is not None:
                                    for child in self.dns_address:
                                        if child is not None:
                                            return True

                                if self.dns_count is not None:
                                    return True

                                if self.duid_xr is not None:
                                    return True

                                if self.mac_address_xr is not None:
                                    return True

                                if self.opt17 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions.DuidBindOption']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:duid-bind-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.duid_bind_option is not None:
                                for child_ref in self.duid_bind_option:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:binding-options'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.duid_bind_options is not None and self.duid_bind_options._has_data():
                            return True

                        if self.mac_bind_options is not None and self.mac_bind_options._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.binding is not None and self.binding._has_data():
                        return True

                    if self.binding_options is not None and self.binding_options._has_data():
                        return True

                    if self.interfaces is not None and self.interfaces._has_data():
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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                    return meta._meta_table['Dhcpv6.Nodes.Node.Server']['meta_info']


            class Relay(object):
                """
                IPv6 DHCP relay operational data
                
                .. attribute:: binding
                
                	DHCPV6 relay bindings
                	**type**\:   :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding>`
                
                .. attribute:: statistics
                
                	DHCPv6 relay statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Statistics>`
                
                .. attribute:: vrfs
                
                	DHCPV6 relay list of VRF names
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs>`
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.binding = Dhcpv6.Nodes.Node.Relay.Binding()
                    self.binding.parent = self
                    self.statistics = Dhcpv6.Nodes.Node.Relay.Statistics()
                    self.statistics.parent = self
                    self.vrfs = Dhcpv6.Nodes.Node.Relay.Vrfs()
                    self.vrfs.parent = self


                class Statistics(object):
                    """
                    DHCPv6 relay statistics
                    
                    .. attribute:: ipv6_dhcpv6d_relay_stat
                    
                    	ipv6 dhcpv6d relay stat
                    	**type**\: list of    :py:class:`Ipv6Dhcpv6DRelayStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_dhcpv6d_relay_stat = YList()
                        self.ipv6_dhcpv6d_relay_stat.parent = self
                        self.ipv6_dhcpv6d_relay_stat.name = 'ipv6_dhcpv6d_relay_stat'


                    class Ipv6Dhcpv6DRelayStat(object):
                        """
                        ipv6 dhcpv6d relay stat
                        
                        .. attribute:: statistics
                        
                        	Relay statistics
                        	**type**\:   :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_>`
                        
                        .. attribute:: vrf_name
                        
                        	DHCPv6 L3 VRF name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.statistics = Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_()
                            self.statistics.parent = self
                            self.vrf_name = None


                        class Statistics_(object):
                            """
                            Relay statistics
                            
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

                            _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:ipv6-dhcpv6d-relay-stat'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipv6_dhcpv6d_relay_stat is not None:
                            for child_ref in self.ipv6_dhcpv6d_relay_stat:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Statistics']['meta_info']


                class Binding(object):
                    """
                    DHCPV6 relay bindings
                    
                    .. attribute:: clients
                    
                    	DHCPV6 relay client bindings
                    	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding.Clients>`
                    
                    .. attribute:: summary
                    
                    	DHCPV6 relay binding summary
                    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding.Summary>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.clients = Dhcpv6.Nodes.Node.Relay.Binding.Clients()
                        self.clients.parent = self
                        self.summary = Dhcpv6.Nodes.Node.Relay.Binding.Summary()
                        self.summary.parent = self


                    class Summary(object):
                        """
                        DHCPV6 relay binding summary
                        
                        .. attribute:: clients
                        
                        	Total number of clients
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.clients = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.clients is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Binding.Summary']['meta_info']


                    class Clients(object):
                        """
                        DHCPV6 relay client bindings
                        
                        .. attribute:: client
                        
                        	Single DHCPV6 relay binding
                        	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.client = YList()
                            self.client.parent = self
                            self.client.name = 'client'


                        class Client(object):
                            """
                            Single DHCPV6 relay binding
                            
                            .. attribute:: client_id  <key>
                            
                            	Client ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: client_id_xr
                            
                            	Client unique identifier
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duid
                            
                            	Client DUID
                            	**type**\:  str
                            
                            .. attribute:: ia_id
                            
                            	IA\_ID of this IA
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            .. attribute:: lifetime
                            
                            	Client route lifetime
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: next_hop_addr
                            
                            	Next hop is our address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix
                            
                            	DHCPV6 IPv6 Prefix allotted to client
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	length of prefix
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: relay_profile_name
                            
                            	Relay Profile name
                            	**type**\:  str
                            
                            	**length:** 0..65
                            
                            .. attribute:: rem_life_time
                            
                            	Client route remaining lifetime
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: vrf_name
                            
                            	DHCPv6 client/subscriber Vrf name
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.client_id = None
                                self.client_id_xr = None
                                self.duid = None
                                self.ia_id = None
                                self.interface_name = None
                                self.lifetime = None
                                self.next_hop_addr = None
                                self.prefix = None
                                self.prefix_length = None
                                self.relay_profile_name = None
                                self.rem_life_time = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.client_id is None:
                                    raise YPYModelError('Key property client_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:client-id = ' + str(self.client_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.client_id is not None:
                                    return True

                                if self.client_id_xr is not None:
                                    return True

                                if self.duid is not None:
                                    return True

                                if self.ia_id is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.lifetime is not None:
                                    return True

                                if self.next_hop_addr is not None:
                                    return True

                                if self.prefix is not None:
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                if self.relay_profile_name is not None:
                                    return True

                                if self.rem_life_time is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:clients'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Binding.Clients']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:binding'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Binding']['meta_info']


                class Vrfs(object):
                    """
                    DHCPV6 relay list of VRF names
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP relay VRF name
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        IPv6 DHCP relay VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: statistics
                        
                        	IPv6 DHCP relay statistics
                        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.statistics = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics()
                            self.statistics.parent = self


                        class Statistics(object):
                            """
                            IPv6 DHCP relay statistics
                            
                            .. attribute:: advertise
                            
                            	DHCPV6 advertise packets
                            	**type**\:   :py:class:`Advertise <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise>`
                            
                            .. attribute:: confirm
                            
                            	DHCPV6 confirm packets
                            	**type**\:   :py:class:`Confirm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm>`
                            
                            .. attribute:: decline
                            
                            	DHCPV6 decline packets
                            	**type**\:   :py:class:`Decline <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline>`
                            
                            .. attribute:: inform
                            
                            	DHCPV6 inform packets
                            	**type**\:   :py:class:`Inform <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform>`
                            
                            .. attribute:: lease_query
                            
                            	DHCPV6 lease query packets
                            	**type**\:   :py:class:`LeaseQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery>`
                            
                            .. attribute:: lease_query_data
                            
                            	DHCPV6 lease query data packets
                            	**type**\:   :py:class:`LeaseQueryData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData>`
                            
                            .. attribute:: lease_query_done
                            
                            	DHCPV6 lease query done packets
                            	**type**\:   :py:class:`LeaseQueryDone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone>`
                            
                            .. attribute:: lease_query_reply
                            
                            	DHCPV6 lease query reply packets
                            	**type**\:   :py:class:`LeaseQueryReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply>`
                            
                            .. attribute:: rebind
                            
                            	DHCPV6 rebind packets
                            	**type**\:   :py:class:`Rebind <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind>`
                            
                            .. attribute:: reconfig
                            
                            	DHCPV6 reconfig packets
                            	**type**\:   :py:class:`Reconfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig>`
                            
                            .. attribute:: relay_forward
                            
                            	DHCPV6 relay forward packets
                            	**type**\:   :py:class:`RelayForward <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward>`
                            
                            .. attribute:: relay_reply
                            
                            	DHCPV6 relay reply packets
                            	**type**\:   :py:class:`RelayReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply>`
                            
                            .. attribute:: release
                            
                            	DHCPV6 release packets
                            	**type**\:   :py:class:`Release <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release>`
                            
                            .. attribute:: renew
                            
                            	DHCPV6 renew packets
                            	**type**\:   :py:class:`Renew <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew>`
                            
                            .. attribute:: reply
                            
                            	DHCPV6 reply packets
                            	**type**\:   :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply>`
                            
                            .. attribute:: request
                            
                            	DHCPV6 request packets
                            	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request>`
                            
                            .. attribute:: solicit
                            
                            	DHCPV6 solicit packets
                            	**type**\:   :py:class:`Solicit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper.Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.advertise = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise()
                                self.advertise.parent = self
                                self.confirm = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm()
                                self.confirm.parent = self
                                self.decline = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline()
                                self.decline.parent = self
                                self.inform = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform()
                                self.inform.parent = self
                                self.lease_query = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery()
                                self.lease_query.parent = self
                                self.lease_query_data = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData()
                                self.lease_query_data.parent = self
                                self.lease_query_done = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone()
                                self.lease_query_done.parent = self
                                self.lease_query_reply = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply()
                                self.lease_query_reply.parent = self
                                self.rebind = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind()
                                self.rebind.parent = self
                                self.reconfig = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig()
                                self.reconfig.parent = self
                                self.relay_forward = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward()
                                self.relay_forward.parent = self
                                self.relay_reply = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply()
                                self.relay_reply.parent = self
                                self.release = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release()
                                self.release.parent = self
                                self.renew = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew()
                                self.renew.parent = self
                                self.reply = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply()
                                self.reply.parent = self
                                self.request = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request()
                                self.request.parent = self
                                self.solicit = Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit()
                                self.solicit.parent = self


                            class Solicit(object):
                                """
                                DHCPV6 solicit packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:solicit'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit']['meta_info']


                            class Advertise(object):
                                """
                                DHCPV6 advertise packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:advertise'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise']['meta_info']


                            class Request(object):
                                """
                                DHCPV6 request packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:request'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request']['meta_info']


                            class Reply(object):
                                """
                                DHCPV6 reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reply'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply']['meta_info']


                            class Confirm(object):
                                """
                                DHCPV6 confirm packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:confirm'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm']['meta_info']


                            class Decline(object):
                                """
                                DHCPV6 decline packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:decline'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline']['meta_info']


                            class Renew(object):
                                """
                                DHCPV6 renew packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:renew'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew']['meta_info']


                            class Rebind(object):
                                """
                                DHCPV6 rebind packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:rebind'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind']['meta_info']


                            class Release(object):
                                """
                                DHCPV6 release packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:release'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release']['meta_info']


                            class Reconfig(object):
                                """
                                DHCPV6 reconfig packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:reconfig'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig']['meta_info']


                            class Inform(object):
                                """
                                DHCPV6 inform packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:inform'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform']['meta_info']


                            class RelayForward(object):
                                """
                                DHCPV6 relay forward packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-forward'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward']['meta_info']


                            class RelayReply(object):
                                """
                                DHCPV6 relay reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay-reply'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply']['meta_info']


                            class LeaseQuery(object):
                                """
                                DHCPV6 lease query packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info']


                            class LeaseQueryReply(object):
                                """
                                DHCPV6 lease query reply packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-reply'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply']['meta_info']


                            class LeaseQueryDone(object):
                                """
                                DHCPV6 lease query done packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-done'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone']['meta_info']


                            class LeaseQueryData(object):
                                """
                                DHCPV6 lease query data packets
                                
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

                                _prefix = 'ipv6-new-dhcpv6d-oper'
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

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:lease-query-data'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:statistics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.advertise is not None and self.advertise._has_data():
                                    return True

                                if self.confirm is not None and self.confirm._has_data():
                                    return True

                                if self.decline is not None and self.decline._has_data():
                                    return True

                                if self.inform is not None and self.inform._has_data():
                                    return True

                                if self.lease_query is not None and self.lease_query._has_data():
                                    return True

                                if self.lease_query_data is not None and self.lease_query_data._has_data():
                                    return True

                                if self.lease_query_done is not None and self.lease_query_done._has_data():
                                    return True

                                if self.lease_query_reply is not None and self.lease_query_reply._has_data():
                                    return True

                                if self.rebind is not None and self.rebind._has_data():
                                    return True

                                if self.reconfig is not None and self.reconfig._has_data():
                                    return True

                                if self.relay_forward is not None and self.relay_forward._has_data():
                                    return True

                                if self.relay_reply is not None and self.relay_reply._has_data():
                                    return True

                                if self.release is not None and self.release._has_data():
                                    return True

                                if self.renew is not None and self.renew._has_data():
                                    return True

                                if self.reply is not None and self.reply._has_data():
                                    return True

                                if self.request is not None and self.request._has_data():
                                    return True

                                if self.solicit is not None and self.solicit._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                                return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrf-name = ' + str(self.vrf_name) + ']'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                            return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:vrfs'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                        return meta._meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:relay'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.binding is not None and self.binding._has_data():
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.vrfs is not None and self.vrfs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                    return meta._meta_table['Dhcpv6.Nodes.Node.Relay']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:nodes/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:node[Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.base is not None and self.base._has_data():
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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
                return meta._meta_table['Dhcpv6.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
            return meta._meta_table['Dhcpv6.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-oper:dhcpv6'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.issu_status is not None and self.issu_status._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_oper as meta
        return meta._meta_table['Dhcpv6']['meta_info']


