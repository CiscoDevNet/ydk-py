""" Cisco_IOS_XR_ip_ntp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-ntp package configuration.

This module contains definitions
for the following management objects\:
  ntp\: NTP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NtpAccess(Enum):
    """
    NtpAccess (Enum Class)

    Ntp access

    .. data:: peer = 0

    	Peer

    .. data:: serve = 1

    	Serve

    .. data:: serve_only = 2

    	Serve Only

    .. data:: query_only = 3

    	Query Only

    """

    peer = Enum.YLeaf(0, "peer")

    serve = Enum.YLeaf(1, "serve")

    serve_only = Enum.YLeaf(2, "serve-only")

    query_only = Enum.YLeaf(3, "query-only")


class NtpAccessAf(Enum):
    """
    NtpAccessAf (Enum Class)

    Ntp access af

    .. data:: ipv4 = 0

    	IPv4

    .. data:: ipv6 = 1

    	IPv6

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")


class NtpPeer(Enum):
    """
    NtpPeer (Enum Class)

    Ntp peer

    .. data:: peer = 0

    	Peer

    .. data:: server = 1

    	Server

    """

    peer = Enum.YLeaf(0, "peer")

    server = Enum.YLeaf(1, "server")


class Ntpdscp(Enum):
    """
    Ntpdscp (Enum Class)

    Ntpdscp

    .. data:: ntp_precedence = 0

    	Precedence Value

    .. data:: ntpdscp = 1

    	DSCP Value

    """

    ntp_precedence = Enum.YLeaf(0, "ntp-precedence")

    ntpdscp = Enum.YLeaf(1, "ntpdscp")



class Ntp(Entity):
    """
    NTP configuration
    
    .. attribute:: admin_types
    
    	Configure NTP server admin\-plane
    	**type**\:  :py:class:`AdminTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AdminTypes>`
    
    .. attribute:: peer_vrfs
    
    	Configures NTP Peers or Servers
    	**type**\:  :py:class:`PeerVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs>`
    
    .. attribute:: dscp_ipv4
    
    	 Set IP DSCP value for outgoing NTP IPV4 packets
    	**type**\:  :py:class:`DscpIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.DscpIpv4>`
    
    	**presence node**\: True
    
    .. attribute:: dscp_ipv6
    
    	 Set IP DSCP value for outgoing NTP IPV6 packets
    	**type**\:  :py:class:`DscpIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.DscpIpv6>`
    
    	**presence node**\: True
    
    .. attribute:: sources
    
    	Configure  NTP source interface
    	**type**\:  :py:class:`Sources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Sources>`
    
    .. attribute:: drift
    
    	NTP drift
    	**type**\:  :py:class:`Drift <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Drift>`
    
    .. attribute:: authentication
    
    	Configure NTP Authentication keys
    	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication>`
    
    .. attribute:: passive
    
    	Configure NTP passive associations
    	**type**\:  :py:class:`Passive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Passive>`
    
    .. attribute:: interface_tables
    
    	NTP per interface configuration
    	**type**\:  :py:class:`InterfaceTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables>`
    
    .. attribute:: access_group_tables
    
    	Control NTP access
    	**type**\:  :py:class:`AccessGroupTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables>`
    
    .. attribute:: max_associations
    
    	Set maximum number of associations
    	**type**\: int
    
    	**range:** 0..4294967295
    
    .. attribute:: master
    
    	Act as NTP master clock
    	**type**\: int
    
    	**range:** 1..15
    
    	**default value**\: 8
    
    .. attribute:: broadcast_delay
    
    	Estimated round\-trip delay
    	**type**\: int
    
    	**range:** 1..999999
    
    .. attribute:: log_internal_sync
    
    	To enable logging internal sync conflicts
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: update_calendar
    
    	To enable calendar update with NTP time
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'ip-ntp-cfg'
    _revision = '2017-10-15'

    def __init__(self):
        super(Ntp, self).__init__()
        self._top_entity = None

        self.yang_name = "ntp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-ntp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("admin-types", ("admin_types", Ntp.AdminTypes)), ("peer-vrfs", ("peer_vrfs", Ntp.PeerVrfs)), ("dscp-ipv4", ("dscp_ipv4", Ntp.DscpIpv4)), ("dscp-ipv6", ("dscp_ipv6", Ntp.DscpIpv6)), ("sources", ("sources", Ntp.Sources)), ("drift", ("drift", Ntp.Drift)), ("authentication", ("authentication", Ntp.Authentication)), ("passive", ("passive", Ntp.Passive)), ("interface-tables", ("interface_tables", Ntp.InterfaceTables)), ("access-group-tables", ("access_group_tables", Ntp.AccessGroupTables))])
        self._leafs = OrderedDict([
            ('max_associations', (YLeaf(YType.uint32, 'max-associations'), ['int'])),
            ('master', (YLeaf(YType.uint32, 'master'), ['int'])),
            ('broadcast_delay', (YLeaf(YType.uint32, 'broadcast-delay'), ['int'])),
            ('log_internal_sync', (YLeaf(YType.empty, 'log-internal-sync'), ['Empty'])),
            ('update_calendar', (YLeaf(YType.empty, 'update-calendar'), ['Empty'])),
        ])
        self.max_associations = None
        self.master = None
        self.broadcast_delay = None
        self.log_internal_sync = None
        self.update_calendar = None

        self.admin_types = Ntp.AdminTypes()
        self.admin_types.parent = self
        self._children_name_map["admin_types"] = "admin-types"

        self.peer_vrfs = Ntp.PeerVrfs()
        self.peer_vrfs.parent = self
        self._children_name_map["peer_vrfs"] = "peer-vrfs"

        self.dscp_ipv4 = None
        self._children_name_map["dscp_ipv4"] = "dscp-ipv4"

        self.dscp_ipv6 = None
        self._children_name_map["dscp_ipv6"] = "dscp-ipv6"

        self.sources = Ntp.Sources()
        self.sources.parent = self
        self._children_name_map["sources"] = "sources"

        self.drift = Ntp.Drift()
        self.drift.parent = self
        self._children_name_map["drift"] = "drift"

        self.authentication = Ntp.Authentication()
        self.authentication.parent = self
        self._children_name_map["authentication"] = "authentication"

        self.passive = Ntp.Passive()
        self.passive.parent = self
        self._children_name_map["passive"] = "passive"

        self.interface_tables = Ntp.InterfaceTables()
        self.interface_tables.parent = self
        self._children_name_map["interface_tables"] = "interface-tables"

        self.access_group_tables = Ntp.AccessGroupTables()
        self.access_group_tables.parent = self
        self._children_name_map["access_group_tables"] = "access-group-tables"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ntp, ['max_associations', 'master', 'broadcast_delay', 'log_internal_sync', 'update_calendar'], name, value)


    class AdminTypes(Entity):
        """
        Configure NTP server admin\-plane
        
        .. attribute:: admin_type
        
        	Configure NTP server admin plane
        	**type**\: list of  		 :py:class:`AdminType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AdminTypes.AdminType>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Ntp.AdminTypes, self).__init__()

            self.yang_name = "admin-types"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("admin-type", ("admin_type", Ntp.AdminTypes.AdminType))])
            self._leafs = OrderedDict()

            self.admin_type = YList(self)
            self._segment_path = lambda: "admin-types"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.AdminTypes, [], name, value)


        class AdminType(Entity):
            """
            Configure NTP server admin plane
            
            .. attribute:: peer_type  (key)
            
            	Peer or Server
            	**type**\:  :py:class:`NtpPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpPeer>`
            
            .. attribute:: ntp_version
            
            	NTP version
            	**type**\: int
            
            	**range:** 2..4
            
            .. attribute:: authentication_key
            
            	Authentication Key
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: min_poll
            
            	Minimum poll interval
            	**type**\: int
            
            	**range:** 4..17
            
            .. attribute:: max_poll
            
            	Maxinum poll interval
            	**type**\: int
            
            	**range:** 4..17
            
            .. attribute:: preferred_peer
            
            	Preferred peer
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: burst
            
            	Use burst mode
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: iburst
            
            	Use iburst mode
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Ntp.AdminTypes.AdminType, self).__init__()

                self.yang_name = "admin-type"
                self.yang_parent_name = "admin-types"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['peer_type']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('peer_type', (YLeaf(YType.enumeration, 'peer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'NtpPeer', '')])),
                    ('ntp_version', (YLeaf(YType.uint32, 'ntp-version'), ['int'])),
                    ('authentication_key', (YLeaf(YType.uint32, 'authentication-key'), ['int'])),
                    ('min_poll', (YLeaf(YType.uint32, 'min-poll'), ['int'])),
                    ('max_poll', (YLeaf(YType.uint32, 'max-poll'), ['int'])),
                    ('preferred_peer', (YLeaf(YType.empty, 'preferred-peer'), ['Empty'])),
                    ('burst', (YLeaf(YType.empty, 'burst'), ['Empty'])),
                    ('iburst', (YLeaf(YType.empty, 'iburst'), ['Empty'])),
                ])
                self.peer_type = None
                self.ntp_version = None
                self.authentication_key = None
                self.min_poll = None
                self.max_poll = None
                self.preferred_peer = None
                self.burst = None
                self.iburst = None
                self._segment_path = lambda: "admin-type" + "[peer-type='" + str(self.peer_type) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/admin-types/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.AdminTypes.AdminType, ['peer_type', 'ntp_version', 'authentication_key', 'min_poll', 'max_poll', 'preferred_peer', 'burst', 'iburst'], name, value)


    class PeerVrfs(Entity):
        """
        Configures NTP Peers or Servers
        
        .. attribute:: peer_vrf
        
        	Configures NTP Peers or Servers for a single VRF. The 'default' must also be specified for default VRF
        	**type**\: list of  		 :py:class:`PeerVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Ntp.PeerVrfs, self).__init__()

            self.yang_name = "peer-vrfs"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("peer-vrf", ("peer_vrf", Ntp.PeerVrfs.PeerVrf))])
            self._leafs = OrderedDict()

            self.peer_vrf = YList(self)
            self._segment_path = lambda: "peer-vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.PeerVrfs, [], name, value)


        class PeerVrf(Entity):
            """
            Configures NTP Peers or Servers for a single
            VRF. The 'default' must also be specified for
            default VRF
            
            .. attribute:: vrf_name  (key)
            
            	VRF name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: peer_ipv4s
            
            	Configures IPv4 NTP Peers or Servers
            	**type**\:  :py:class:`PeerIpv4s <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv4s>`
            
            .. attribute:: peer_ipv6s
            
            	Configuration NTP Peers or Servers of IPV6
            	**type**\:  :py:class:`PeerIpv6s <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv6s>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Ntp.PeerVrfs.PeerVrf, self).__init__()

                self.yang_name = "peer-vrf"
                self.yang_parent_name = "peer-vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("peer-ipv4s", ("peer_ipv4s", Ntp.PeerVrfs.PeerVrf.PeerIpv4s)), ("peer-ipv6s", ("peer_ipv6s", Ntp.PeerVrfs.PeerVrf.PeerIpv6s))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.peer_ipv4s = Ntp.PeerVrfs.PeerVrf.PeerIpv4s()
                self.peer_ipv4s.parent = self
                self._children_name_map["peer_ipv4s"] = "peer-ipv4s"

                self.peer_ipv6s = Ntp.PeerVrfs.PeerVrf.PeerIpv6s()
                self.peer_ipv6s.parent = self
                self._children_name_map["peer_ipv6s"] = "peer-ipv6s"
                self._segment_path = lambda: "peer-vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/peer-vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.PeerVrfs.PeerVrf, ['vrf_name'], name, value)


            class PeerIpv4s(Entity):
                """
                Configures IPv4 NTP Peers or Servers
                
                .. attribute:: peer_ipv4
                
                	Configure an IPv4 NTP server or peer
                	**type**\: list of  		 :py:class:`PeerIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv4s.PeerIpv4>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Ntp.PeerVrfs.PeerVrf.PeerIpv4s, self).__init__()

                    self.yang_name = "peer-ipv4s"
                    self.yang_parent_name = "peer-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("peer-ipv4", ("peer_ipv4", Ntp.PeerVrfs.PeerVrf.PeerIpv4s.PeerIpv4))])
                    self._leafs = OrderedDict()

                    self.peer_ipv4 = YList(self)
                    self._segment_path = lambda: "peer-ipv4s"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv4s, [], name, value)


                class PeerIpv4(Entity):
                    """
                    Configure an IPv4 NTP server or peer
                    
                    .. attribute:: address_ipv4  (key)
                    
                    	IPv4 Address of a peer
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_type_ipv4
                    
                    	Configure an IPv4 NTP server or peer
                    	**type**\: list of  		 :py:class:`PeerTypeIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv4s.PeerIpv4.PeerTypeIpv4>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Ntp.PeerVrfs.PeerVrf.PeerIpv4s.PeerIpv4, self).__init__()

                        self.yang_name = "peer-ipv4"
                        self.yang_parent_name = "peer-ipv4s"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address_ipv4']
                        self._child_classes = OrderedDict([("peer-type-ipv4", ("peer_type_ipv4", Ntp.PeerVrfs.PeerVrf.PeerIpv4s.PeerIpv4.PeerTypeIpv4))])
                        self._leafs = OrderedDict([
                            ('address_ipv4', (YLeaf(YType.str, 'address-ipv4'), ['str'])),
                        ])
                        self.address_ipv4 = None

                        self.peer_type_ipv4 = YList(self)
                        self._segment_path = lambda: "peer-ipv4" + "[address-ipv4='" + str(self.address_ipv4) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv4s.PeerIpv4, ['address_ipv4'], name, value)


                    class PeerTypeIpv4(Entity):
                        """
                        Configure an IPv4 NTP server or peer
                        
                        .. attribute:: peer_type  (key)
                        
                        	Peer or Server
                        	**type**\:  :py:class:`NtpPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpPeer>`
                        
                        .. attribute:: ntp_version
                        
                        	NTP version
                        	**type**\: int
                        
                        	**range:** 2..4
                        
                        .. attribute:: authentication_key
                        
                        	Authentication Key
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: min_poll
                        
                        	Minimum poll interval
                        	**type**\: int
                        
                        	**range:** 4..17
                        
                        .. attribute:: max_poll
                        
                        	Maxinum poll interval
                        	**type**\: int
                        
                        	**range:** 4..17
                        
                        .. attribute:: preferred_peer
                        
                        	Preferred peer
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: source_interface
                        
                        	Source interface of this peer
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: burst
                        
                        	Use burst mode
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: iburst
                        
                        	Use iburst mode
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Ntp.PeerVrfs.PeerVrf.PeerIpv4s.PeerIpv4.PeerTypeIpv4, self).__init__()

                            self.yang_name = "peer-type-ipv4"
                            self.yang_parent_name = "peer-ipv4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['peer_type']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('peer_type', (YLeaf(YType.enumeration, 'peer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'NtpPeer', '')])),
                                ('ntp_version', (YLeaf(YType.uint32, 'ntp-version'), ['int'])),
                                ('authentication_key', (YLeaf(YType.uint32, 'authentication-key'), ['int'])),
                                ('min_poll', (YLeaf(YType.uint32, 'min-poll'), ['int'])),
                                ('max_poll', (YLeaf(YType.uint32, 'max-poll'), ['int'])),
                                ('preferred_peer', (YLeaf(YType.empty, 'preferred-peer'), ['Empty'])),
                                ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                                ('burst', (YLeaf(YType.empty, 'burst'), ['Empty'])),
                                ('iburst', (YLeaf(YType.empty, 'iburst'), ['Empty'])),
                            ])
                            self.peer_type = None
                            self.ntp_version = None
                            self.authentication_key = None
                            self.min_poll = None
                            self.max_poll = None
                            self.preferred_peer = None
                            self.source_interface = None
                            self.burst = None
                            self.iburst = None
                            self._segment_path = lambda: "peer-type-ipv4" + "[peer-type='" + str(self.peer_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv4s.PeerIpv4.PeerTypeIpv4, ['peer_type', 'ntp_version', 'authentication_key', 'min_poll', 'max_poll', 'preferred_peer', 'source_interface', 'burst', 'iburst'], name, value)


            class PeerIpv6s(Entity):
                """
                Configuration NTP Peers or Servers of IPV6
                
                .. attribute:: peer_ipv6
                
                	Configure a NTP server or peer
                	**type**\: list of  		 :py:class:`PeerIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv6s.PeerIpv6>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Ntp.PeerVrfs.PeerVrf.PeerIpv6s, self).__init__()

                    self.yang_name = "peer-ipv6s"
                    self.yang_parent_name = "peer-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("peer-ipv6", ("peer_ipv6", Ntp.PeerVrfs.PeerVrf.PeerIpv6s.PeerIpv6))])
                    self._leafs = OrderedDict()

                    self.peer_ipv6 = YList(self)
                    self._segment_path = lambda: "peer-ipv6s"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv6s, [], name, value)


                class PeerIpv6(Entity):
                    """
                    Configure a NTP server or peer
                    
                    .. attribute:: address_ipv6  (key)
                    
                    	Address of a peer
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_type_ipv6
                    
                    	Configure a NTP server or peer
                    	**type**\: list of  		 :py:class:`PeerTypeIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv6s.PeerIpv6.PeerTypeIpv6>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Ntp.PeerVrfs.PeerVrf.PeerIpv6s.PeerIpv6, self).__init__()

                        self.yang_name = "peer-ipv6"
                        self.yang_parent_name = "peer-ipv6s"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address_ipv6']
                        self._child_classes = OrderedDict([("peer-type-ipv6", ("peer_type_ipv6", Ntp.PeerVrfs.PeerVrf.PeerIpv6s.PeerIpv6.PeerTypeIpv6))])
                        self._leafs = OrderedDict([
                            ('address_ipv6', (YLeaf(YType.str, 'address-ipv6'), ['str'])),
                        ])
                        self.address_ipv6 = None

                        self.peer_type_ipv6 = YList(self)
                        self._segment_path = lambda: "peer-ipv6" + "[address-ipv6='" + str(self.address_ipv6) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv6s.PeerIpv6, ['address_ipv6'], name, value)


                    class PeerTypeIpv6(Entity):
                        """
                        Configure a NTP server or peer
                        
                        .. attribute:: peer_type  (key)
                        
                        	Peer or Server
                        	**type**\:  :py:class:`NtpPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpPeer>`
                        
                        .. attribute:: ntp_version
                        
                        	NTP version
                        	**type**\: int
                        
                        	**range:** 2..4
                        
                        .. attribute:: authentication_key
                        
                        	Authentication Key
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: min_poll
                        
                        	Minimum poll interval
                        	**type**\: int
                        
                        	**range:** 4..17
                        
                        .. attribute:: max_poll
                        
                        	Maxinum poll interval
                        	**type**\: int
                        
                        	**range:** 4..17
                        
                        .. attribute:: preferred_peer
                        
                        	Preferred peer
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: source_interface
                        
                        	Source interface of this peer
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: burst
                        
                        	Use burst mode
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: iburst
                        
                        	Use iburst mode
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: address_ipv6
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Ntp.PeerVrfs.PeerVrf.PeerIpv6s.PeerIpv6.PeerTypeIpv6, self).__init__()

                            self.yang_name = "peer-type-ipv6"
                            self.yang_parent_name = "peer-ipv6"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['peer_type']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('peer_type', (YLeaf(YType.enumeration, 'peer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'NtpPeer', '')])),
                                ('ntp_version', (YLeaf(YType.uint32, 'ntp-version'), ['int'])),
                                ('authentication_key', (YLeaf(YType.uint32, 'authentication-key'), ['int'])),
                                ('min_poll', (YLeaf(YType.uint32, 'min-poll'), ['int'])),
                                ('max_poll', (YLeaf(YType.uint32, 'max-poll'), ['int'])),
                                ('preferred_peer', (YLeaf(YType.empty, 'preferred-peer'), ['Empty'])),
                                ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                                ('burst', (YLeaf(YType.empty, 'burst'), ['Empty'])),
                                ('iburst', (YLeaf(YType.empty, 'iburst'), ['Empty'])),
                                ('address_ipv6', (YLeaf(YType.str, 'address-ipv6'), ['str'])),
                            ])
                            self.peer_type = None
                            self.ntp_version = None
                            self.authentication_key = None
                            self.min_poll = None
                            self.max_poll = None
                            self.preferred_peer = None
                            self.source_interface = None
                            self.burst = None
                            self.iburst = None
                            self.address_ipv6 = None
                            self._segment_path = lambda: "peer-type-ipv6" + "[peer-type='" + str(self.peer_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv6s.PeerIpv6.PeerTypeIpv6, ['peer_type', 'ntp_version', 'authentication_key', 'min_poll', 'max_poll', 'preferred_peer', 'source_interface', 'burst', 'iburst', 'address_ipv6'], name, value)


    class DscpIpv4(Entity):
        """
         Set IP DSCP value for outgoing NTP IPV4 packets
        
        .. attribute:: mode
        
        	NTPPRECEDENCE (0) to specify Precedence value  NTPDSCP (1) to specify DSCP value
        	**type**\:  :py:class:`Ntpdscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntpdscp>`
        
        	**mandatory**\: True
        
        .. attribute:: dscp_or_precedence_value
        
        	If Mode is set to 'NTPPRECEDENCE(0)' specify Precedence value , if Mode is set to 'NTPDSCP(1)' specify DSCP
        	**type**\: int
        
        	**range:** 0..63
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Ntp.DscpIpv4, self).__init__()

            self.yang_name = "dscp-ipv4"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntpdscp', '')])),
                ('dscp_or_precedence_value', (YLeaf(YType.uint32, 'dscp-or-precedence-value'), ['int'])),
            ])
            self.mode = None
            self.dscp_or_precedence_value = None
            self._segment_path = lambda: "dscp-ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.DscpIpv4, ['mode', 'dscp_or_precedence_value'], name, value)


    class DscpIpv6(Entity):
        """
         Set IP DSCP value for outgoing NTP IPV6 packets
        
        .. attribute:: mode
        
        	NTPPRECEDENCE(0) to specify Precedence value NTPDSCP(1) to specify DSCP value
        	**type**\:  :py:class:`Ntpdscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntpdscp>`
        
        	**mandatory**\: True
        
        .. attribute:: dscp_or_precedence_value
        
        	If Mode is set to 'NTPPRECEDENCE(0)' specify Precedence value , if Mode is set to 'NTPDSCP(1)' specify DSCP
        	**type**\: int
        
        	**range:** 0..63
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Ntp.DscpIpv6, self).__init__()

            self.yang_name = "dscp-ipv6"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntpdscp', '')])),
                ('dscp_or_precedence_value', (YLeaf(YType.uint32, 'dscp-or-precedence-value'), ['int'])),
            ])
            self.mode = None
            self.dscp_or_precedence_value = None
            self._segment_path = lambda: "dscp-ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.DscpIpv6, ['mode', 'dscp_or_precedence_value'], name, value)


    class Sources(Entity):
        """
        Configure  NTP source interface
        
        .. attribute:: source
        
        	Configure  NTP source interface
        	**type**\: list of  		 :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Sources.Source>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Ntp.Sources, self).__init__()

            self.yang_name = "sources"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("source", ("source", Ntp.Sources.Source))])
            self._leafs = OrderedDict()

            self.source = YList(self)
            self._segment_path = lambda: "sources"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Sources, [], name, value)


        class Source(Entity):
            """
            Configure  NTP source interface
            
            .. attribute:: vrf_name  (key)
            
            	VRF name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: source_interface
            
            	Source Interface for NTP
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Ntp.Sources.Source, self).__init__()

                self.yang_name = "source"
                self.yang_parent_name = "sources"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                ])
                self.vrf_name = None
                self.source_interface = None
                self._segment_path = lambda: "source" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/sources/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.Sources.Source, ['vrf_name', 'source_interface'], name, value)


    class Drift(Entity):
        """
        NTP drift
        
        .. attribute:: file
        
        	File containing drift value
        	**type**\:  :py:class:`File <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Drift.File>`
        
        .. attribute:: aging_time
        
        	Drift Aging Time
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Ntp.Drift, self).__init__()

            self.yang_name = "drift"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("file", ("file", Ntp.Drift.File))])
            self._leafs = OrderedDict([
                ('aging_time', (YLeaf(YType.uint32, 'aging-time'), ['int'])),
            ])
            self.aging_time = None

            self.file = Ntp.Drift.File()
            self.file.parent = self
            self._children_name_map["file"] = "file"
            self._segment_path = lambda: "drift"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Drift, ['aging_time'], name, value)


        class File(Entity):
            """
            File containing drift value
            
            .. attribute:: location
            
            	disk0 or apphost or config or ftp or harddisk or rootfs or tftp. Defaults to PWD if none specified
            	**type**\: str
            
            	**default value**\: PWD
            
            .. attribute:: filename
            
            	File containing drift value
            	**type**\: str
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Ntp.Drift.File, self).__init__()

                self.yang_name = "file"
                self.yang_parent_name = "drift"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('filename', (YLeaf(YType.str, 'filename'), ['str'])),
                ])
                self.location = None
                self.filename = None
                self._segment_path = lambda: "file"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/drift/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.Drift.File, ['location', 'filename'], name, value)


    class Authentication(Entity):
        """
        Configure NTP Authentication keys
        
        .. attribute:: keys
        
        	Authentication Key Table
        	**type**\:  :py:class:`Keys <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.Keys>`
        
        .. attribute:: trusted_keys
        
        	Key numbers for trusted time sources
        	**type**\:  :py:class:`TrustedKeys <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.TrustedKeys>`
        
        .. attribute:: enable
        
        	Enable NTP authentication keys
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Ntp.Authentication, self).__init__()

            self.yang_name = "authentication"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("keys", ("keys", Ntp.Authentication.Keys)), ("trusted-keys", ("trusted_keys", Ntp.Authentication.TrustedKeys))])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.keys = Ntp.Authentication.Keys()
            self.keys.parent = self
            self._children_name_map["keys"] = "keys"

            self.trusted_keys = Ntp.Authentication.TrustedKeys()
            self.trusted_keys.parent = self
            self._children_name_map["trusted_keys"] = "trusted-keys"
            self._segment_path = lambda: "authentication"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Authentication, ['enable'], name, value)


        class Keys(Entity):
            """
            Authentication Key Table
            
            .. attribute:: key
            
            	Authentication key for trusted time sources
            	**type**\: list of  		 :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.Keys.Key>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Ntp.Authentication.Keys, self).__init__()

                self.yang_name = "keys"
                self.yang_parent_name = "authentication"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("key", ("key", Ntp.Authentication.Keys.Key))])
                self._leafs = OrderedDict()

                self.key = YList(self)
                self._segment_path = lambda: "keys"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.Authentication.Keys, [], name, value)


            class Key(Entity):
                """
                Authentication key for trusted time sources
                
                .. attribute:: key_number  (key)
                
                	Authentication Key number
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: authentication_key
                
                	Authentication key \- maximum 32 characters
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Ntp.Authentication.Keys.Key, self).__init__()

                    self.yang_name = "key"
                    self.yang_parent_name = "keys"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['key_number']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('key_number', (YLeaf(YType.uint32, 'key-number'), ['int'])),
                        ('authentication_key', (YLeaf(YType.str, 'authentication-key'), ['str'])),
                    ])
                    self.key_number = None
                    self.authentication_key = None
                    self._segment_path = lambda: "key" + "[key-number='" + str(self.key_number) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/keys/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.Authentication.Keys.Key, ['key_number', 'authentication_key'], name, value)


        class TrustedKeys(Entity):
            """
            Key numbers for trusted time sources
            
            .. attribute:: trusted_key
            
            	Configure NTP trusted key
            	**type**\: list of  		 :py:class:`TrustedKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.TrustedKeys.TrustedKey>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Ntp.Authentication.TrustedKeys, self).__init__()

                self.yang_name = "trusted-keys"
                self.yang_parent_name = "authentication"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("trusted-key", ("trusted_key", Ntp.Authentication.TrustedKeys.TrustedKey))])
                self._leafs = OrderedDict()

                self.trusted_key = YList(self)
                self._segment_path = lambda: "trusted-keys"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.Authentication.TrustedKeys, [], name, value)


            class TrustedKey(Entity):
                """
                Configure NTP trusted key
                
                .. attribute:: key_number  (key)
                
                	Key number
                	**type**\: int
                
                	**range:** 1..65535
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Ntp.Authentication.TrustedKeys.TrustedKey, self).__init__()

                    self.yang_name = "trusted-key"
                    self.yang_parent_name = "trusted-keys"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['key_number']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('key_number', (YLeaf(YType.uint32, 'key-number'), ['int'])),
                    ])
                    self.key_number = None
                    self._segment_path = lambda: "trusted-key" + "[key-number='" + str(self.key_number) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/trusted-keys/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.Authentication.TrustedKeys.TrustedKey, ['key_number'], name, value)


    class Passive(Entity):
        """
        Configure NTP passive associations
        
        .. attribute:: enable
        
        	Enable NTP Passive associations
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Ntp.Passive, self).__init__()

            self.yang_name = "passive"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None
            self._segment_path = lambda: "passive"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Passive, ['enable'], name, value)


    class InterfaceTables(Entity):
        """
        NTP per interface configuration
        
        .. attribute:: interface_table
        
        	NTP per interface configuration
        	**type**\: list of  		 :py:class:`InterfaceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Ntp.InterfaceTables, self).__init__()

            self.yang_name = "interface-tables"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-table", ("interface_table", Ntp.InterfaceTables.InterfaceTable))])
            self._leafs = OrderedDict()

            self.interface_table = YList(self)
            self._segment_path = lambda: "interface-tables"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.InterfaceTables, [], name, value)


        class InterfaceTable(Entity):
            """
            NTP per interface configuration
            
            .. attribute:: vrf_name  (key)
            
            	VRF name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: interface
            
            	Name of the interface
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Ntp.InterfaceTables.InterfaceTable, self).__init__()

                self.yang_name = "interface-table"
                self.yang_parent_name = "interface-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("interface", ("interface", Ntp.InterfaceTables.InterfaceTable.Interface))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.interface = YList(self)
                self._segment_path = lambda: "interface-table" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/interface-tables/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.InterfaceTables.InterfaceTable, ['vrf_name'], name, value)


            class Interface(Entity):
                """
                Name of the interface
                
                .. attribute:: interface  (key)
                
                	interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: interface_multicast
                
                	Configure NTP multicast service
                	**type**\:  :py:class:`InterfaceMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast>`
                
                .. attribute:: interface_broadcast
                
                	Configure NTP broadcast service
                	**type**\:  :py:class:`InterfaceBroadcast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast>`
                
                .. attribute:: disable
                
                	Disable NTP
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Ntp.InterfaceTables.InterfaceTable.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interface-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['interface']
                    self._child_classes = OrderedDict([("interface-multicast", ("interface_multicast", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast)), ("interface-broadcast", ("interface_broadcast", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast))])
                    self._leafs = OrderedDict([
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                    ])
                    self.interface = None
                    self.disable = None

                    self.interface_multicast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast()
                    self.interface_multicast.parent = self
                    self._children_name_map["interface_multicast"] = "interface-multicast"

                    self.interface_broadcast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast()
                    self.interface_broadcast.parent = self
                    self._children_name_map["interface_broadcast"] = "interface-broadcast"
                    self._segment_path = lambda: "interface" + "[interface='" + str(self.interface) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface, ['interface', 'disable'], name, value)


                class InterfaceMulticast(Entity):
                    """
                    Configure NTP multicast service
                    
                    .. attribute:: multicast_clients
                    
                    	Configures multicast client peers
                    	**type**\:  :py:class:`MulticastClients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients>`
                    
                    .. attribute:: multicast_servers
                    
                    	Configures multicast server peers
                    	**type**\:  :py:class:`MulticastServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast, self).__init__()

                        self.yang_name = "interface-multicast"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("multicast-clients", ("multicast_clients", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients)), ("multicast-servers", ("multicast_servers", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers))])
                        self._leafs = OrderedDict()

                        self.multicast_clients = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients()
                        self.multicast_clients.parent = self
                        self._children_name_map["multicast_clients"] = "multicast-clients"

                        self.multicast_servers = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers()
                        self.multicast_servers.parent = self
                        self._children_name_map["multicast_servers"] = "multicast-servers"
                        self._segment_path = lambda: "interface-multicast"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast, [], name, value)


                    class MulticastClients(Entity):
                        """
                        Configures multicast client peers
                        
                        .. attribute:: multicast_client
                        
                        	Listen to NTP multicasts
                        	**type**\: list of  		 :py:class:`MulticastClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient>`
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients, self).__init__()

                            self.yang_name = "multicast-clients"
                            self.yang_parent_name = "interface-multicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("multicast-client", ("multicast_client", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient))])
                            self._leafs = OrderedDict()

                            self.multicast_client = YList(self)
                            self._segment_path = lambda: "multicast-clients"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients, [], name, value)


                        class MulticastClient(Entity):
                            """
                            Listen to NTP multicasts
                            
                            .. attribute:: ip_address  (key)
                            
                            	IP address of a multicast group
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ip-ntp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient, self).__init__()

                                self.yang_name = "multicast-client"
                                self.yang_parent_name = "multicast-clients"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['ip_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                ])
                                self.ip_address = None
                                self._segment_path = lambda: "multicast-client" + "[ip-address='" + str(self.ip_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient, ['ip_address'], name, value)


                    class MulticastServers(Entity):
                        """
                        Configures multicast server peers
                        
                        .. attribute:: multicast_server
                        
                        	Configure NTP multicast group server peer
                        	**type**\: list of  		 :py:class:`MulticastServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer>`
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers, self).__init__()

                            self.yang_name = "multicast-servers"
                            self.yang_parent_name = "interface-multicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("multicast-server", ("multicast_server", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer))])
                            self._leafs = OrderedDict()

                            self.multicast_server = YList(self)
                            self._segment_path = lambda: "multicast-servers"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers, [], name, value)


                        class MulticastServer(Entity):
                            """
                            Configure NTP multicast group server peer
                            
                            .. attribute:: ip_address  (key)
                            
                            	IP address of a multicast group
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: authentication_key
                            
                            	Authentication key
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: version
                            
                            	NTP version
                            	**type**\: int
                            
                            	**range:** 2..4
                            
                            .. attribute:: ttl
                            
                            	TTL
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            

                            """

                            _prefix = 'ip-ntp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer, self).__init__()

                                self.yang_name = "multicast-server"
                                self.yang_parent_name = "multicast-servers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['ip_address']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                    ('authentication_key', (YLeaf(YType.uint32, 'authentication-key'), ['int'])),
                                    ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                                    ('ttl', (YLeaf(YType.uint32, 'ttl'), ['int'])),
                                ])
                                self.ip_address = None
                                self.authentication_key = None
                                self.version = None
                                self.ttl = None
                                self._segment_path = lambda: "multicast-server" + "[ip-address='" + str(self.ip_address) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer, ['ip_address', 'authentication_key', 'version', 'ttl'], name, value)


                class InterfaceBroadcast(Entity):
                    """
                    Configure NTP broadcast service
                    
                    .. attribute:: broadcast_servers
                    
                    	Configure NTP broadcast
                    	**type**\:  :py:class:`BroadcastServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.BroadcastServers>`
                    
                    .. attribute:: broadcast_client
                    
                    	Listen to NTP broadcasts
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast, self).__init__()

                        self.yang_name = "interface-broadcast"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("broadcast-servers", ("broadcast_servers", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.BroadcastServers))])
                        self._leafs = OrderedDict([
                            ('broadcast_client', (YLeaf(YType.empty, 'broadcast-client'), ['Empty'])),
                        ])
                        self.broadcast_client = None

                        self.broadcast_servers = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.BroadcastServers()
                        self.broadcast_servers.parent = self
                        self._children_name_map["broadcast_servers"] = "broadcast-servers"
                        self._segment_path = lambda: "interface-broadcast"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast, ['broadcast_client'], name, value)


                    class BroadcastServers(Entity):
                        """
                        Configure NTP broadcast
                        
                        .. attribute:: broadcast_server
                        
                        	Configure NTP broadcast server
                        	**type**\: list of  		 :py:class:`BroadcastServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.BroadcastServers.BroadcastServer>`
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.BroadcastServers, self).__init__()

                            self.yang_name = "broadcast-servers"
                            self.yang_parent_name = "interface-broadcast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("broadcast-server", ("broadcast_server", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.BroadcastServers.BroadcastServer))])
                            self._leafs = OrderedDict()

                            self.broadcast_server = YList(self)
                            self._segment_path = lambda: "broadcast-servers"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.BroadcastServers, [], name, value)


                        class BroadcastServer(Entity):
                            """
                            Configure NTP broadcast server
                            
                            .. attribute:: broadcast_type  (key)
                            
                            	Broadcast Type
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: address
                            
                            	Destination broadcast IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: authentication_key
                            
                            	Authentication key
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: ntp_version
                            
                            	NTP version
                            	**type**\: int
                            
                            	**range:** 2..4
                            
                            

                            """

                            _prefix = 'ip-ntp-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.BroadcastServers.BroadcastServer, self).__init__()

                                self.yang_name = "broadcast-server"
                                self.yang_parent_name = "broadcast-servers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['broadcast_type']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('broadcast_type', (YLeaf(YType.str, 'broadcast-type'), ['str'])),
                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                    ('authentication_key', (YLeaf(YType.uint32, 'authentication-key'), ['int'])),
                                    ('ntp_version', (YLeaf(YType.uint32, 'ntp-version'), ['int'])),
                                ])
                                self.broadcast_type = None
                                self.address = None
                                self.authentication_key = None
                                self.ntp_version = None
                                self._segment_path = lambda: "broadcast-server" + "[broadcast-type='" + str(self.broadcast_type) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.BroadcastServers.BroadcastServer, ['broadcast_type', 'address', 'authentication_key', 'ntp_version'], name, value)


    class AccessGroupTables(Entity):
        """
        Control NTP access
        
        .. attribute:: access_group_table
        
        	Control NTP access
        	**type**\: list of  		 :py:class:`AccessGroupTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables.AccessGroupTable>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Ntp.AccessGroupTables, self).__init__()

            self.yang_name = "access-group-tables"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("access-group-table", ("access_group_table", Ntp.AccessGroupTables.AccessGroupTable))])
            self._leafs = OrderedDict()

            self.access_group_table = YList(self)
            self._segment_path = lambda: "access-group-tables"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.AccessGroupTables, [], name, value)


        class AccessGroupTable(Entity):
            """
            Control NTP access
            
            .. attribute:: vrf_name  (key)
            
            	VRF name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: access_group_af_table
            
            	Configure NTP access address family
            	**type**\: list of  		 :py:class:`AccessGroupAfTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Ntp.AccessGroupTables.AccessGroupTable, self).__init__()

                self.yang_name = "access-group-table"
                self.yang_parent_name = "access-group-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("access-group-af-table", ("access_group_af_table", Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.access_group_af_table = YList(self)
                self._segment_path = lambda: "access-group-table" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/access-group-tables/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.AccessGroupTables.AccessGroupTable, ['vrf_name'], name, value)


            class AccessGroupAfTable(Entity):
                """
                Configure NTP access address family
                
                .. attribute:: af  (key)
                
                	Address family
                	**type**\:  :py:class:`NtpAccessAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpAccessAf>`
                
                .. attribute:: access_group
                
                	Configure NTP access group
                	**type**\: list of  		 :py:class:`AccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable, self).__init__()

                    self.yang_name = "access-group-af-table"
                    self.yang_parent_name = "access-group-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['af']
                    self._child_classes = OrderedDict([("access-group", ("access_group", Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup))])
                    self._leafs = OrderedDict([
                        ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'NtpAccessAf', '')])),
                    ])
                    self.af = None

                    self.access_group = YList(self)
                    self._segment_path = lambda: "access-group-af-table" + "[af='" + str(self.af) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable, ['af'], name, value)


                class AccessGroup(Entity):
                    """
                    Configure NTP access group
                    
                    .. attribute:: access_group_type  (key)
                    
                    	Access group type
                    	**type**\:  :py:class:`NtpAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpAccess>`
                    
                    .. attribute:: access_list_name
                    
                    	Access list name \- maximum 32 characters
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup, self).__init__()

                        self.yang_name = "access-group"
                        self.yang_parent_name = "access-group-af-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['access_group_type']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('access_group_type', (YLeaf(YType.enumeration, 'access-group-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'NtpAccess', '')])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.access_group_type = None
                        self.access_list_name = None
                        self._segment_path = lambda: "access-group" + "[access-group-type='" + str(self.access_group_type) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup, ['access_group_type', 'access_list_name'], name, value)

    def clone_ptr(self):
        self._top_entity = Ntp()
        return self._top_entity

