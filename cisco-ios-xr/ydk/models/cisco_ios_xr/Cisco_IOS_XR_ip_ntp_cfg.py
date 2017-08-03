""" Cisco_IOS_XR_ip_ntp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-ntp package configuration.

This module contains definitions
for the following management objects\:
  ntp\: NTP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class NtpAccess(Enum):
    """
    NtpAccess

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
    NtpAccessAf

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
    NtpPeer

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
    Ntpdscp

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
    
    .. attribute:: access_group_tables
    
    	Control NTP access
    	**type**\:   :py:class:`AccessGroupTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables>`
    
    .. attribute:: authentication
    
    	Configure NTP Authentication keys
    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication>`
    
    .. attribute:: broadcast_delay
    
    	Estimated round\-trip delay
    	**type**\:  int
    
    	**range:** 1..999999
    
    .. attribute:: dscp_ipv4
    
    	 Set IP DSCP value for outgoing NTP IPV4 packets
    	**type**\:   :py:class:`DscpIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.DscpIpv4>`
    
    	**presence node**\: True
    
    .. attribute:: dscp_ipv6
    
    	 Set IP DSCP value for outgoing NTP IPV6 packets
    	**type**\:   :py:class:`DscpIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.DscpIpv6>`
    
    	**presence node**\: True
    
    .. attribute:: interface_tables
    
    	NTP per interface configuration
    	**type**\:   :py:class:`InterfaceTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables>`
    
    .. attribute:: log_internal_sync
    
    	To enable logging internal sync conflicts
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: master
    
    	Act as NTP master clock
    	**type**\:  int
    
    	**range:** 1..15
    
    	**default value**\: 8
    
    .. attribute:: max_associations
    
    	Set maximum number of associations
    	**type**\:  int
    
    	**range:** \-2147483648..2147483647
    
    .. attribute:: passive
    
    	Configure NTP passive associations
    	**type**\:   :py:class:`Passive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Passive>`
    
    .. attribute:: peer_vrfs
    
    	Configures NTP Peers or Servers
    	**type**\:   :py:class:`PeerVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs>`
    
    .. attribute:: sources
    
    	Configure  NTP source interface
    	**type**\:   :py:class:`Sources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Sources>`
    
    .. attribute:: update_calendar
    
    	To enable calendar update with NTP time
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ip-ntp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ntp, self).__init__()
        self._top_entity = None

        self.yang_name = "ntp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-ntp-cfg"
        self.is_presence_container = True

        self.broadcast_delay = YLeaf(YType.uint32, "broadcast-delay")

        self.log_internal_sync = YLeaf(YType.empty, "log-internal-sync")

        self.master = YLeaf(YType.uint32, "master")

        self.max_associations = YLeaf(YType.int32, "max-associations")

        self.update_calendar = YLeaf(YType.empty, "update-calendar")

        self.access_group_tables = Ntp.AccessGroupTables()
        self.access_group_tables.parent = self
        self._children_name_map["access_group_tables"] = "access-group-tables"
        self._children_yang_names.add("access-group-tables")

        self.authentication = Ntp.Authentication()
        self.authentication.parent = self
        self._children_name_map["authentication"] = "authentication"
        self._children_yang_names.add("authentication")

        self.dscp_ipv4 = None
        self._children_name_map["dscp_ipv4"] = "dscp-ipv4"
        self._children_yang_names.add("dscp-ipv4")

        self.dscp_ipv6 = None
        self._children_name_map["dscp_ipv6"] = "dscp-ipv6"
        self._children_yang_names.add("dscp-ipv6")

        self.interface_tables = Ntp.InterfaceTables()
        self.interface_tables.parent = self
        self._children_name_map["interface_tables"] = "interface-tables"
        self._children_yang_names.add("interface-tables")

        self.passive = Ntp.Passive()
        self.passive.parent = self
        self._children_name_map["passive"] = "passive"
        self._children_yang_names.add("passive")

        self.peer_vrfs = Ntp.PeerVrfs()
        self.peer_vrfs.parent = self
        self._children_name_map["peer_vrfs"] = "peer-vrfs"
        self._children_yang_names.add("peer-vrfs")

        self.sources = Ntp.Sources()
        self.sources.parent = self
        self._children_name_map["sources"] = "sources"
        self._children_yang_names.add("sources")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("broadcast_delay",
                        "log_internal_sync",
                        "master",
                        "max_associations",
                        "update_calendar") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Ntp, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Ntp, self).__setattr__(name, value)


    class PeerVrfs(Entity):
        """
        Configures NTP Peers or Servers
        
        .. attribute:: peer_vrf
        
        	Configures NTP Peers or Servers for a single VRF. The 'default' must also be specified for default VRF
        	**type**\: list of    :py:class:`PeerVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ntp.PeerVrfs, self).__init__()

            self.yang_name = "peer-vrfs"
            self.yang_parent_name = "ntp"

            self.peer_vrf = YList(self)

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
                        super(Ntp.PeerVrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ntp.PeerVrfs, self).__setattr__(name, value)


        class PeerVrf(Entity):
            """
            Configures NTP Peers or Servers for a single
            VRF. The 'default' must also be specified for
            default VRF
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: peer_ipv4s
            
            	Configures IPv4 NTP Peers or Servers
            	**type**\:   :py:class:`PeerIpv4S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv4S>`
            
            .. attribute:: peer_ipv6s
            
            	Configuration NTP Peers or Servers of IPV6
            	**type**\:   :py:class:`PeerIpv6S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv6S>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ntp.PeerVrfs.PeerVrf, self).__init__()

                self.yang_name = "peer-vrf"
                self.yang_parent_name = "peer-vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.peer_ipv4s = Ntp.PeerVrfs.PeerVrf.PeerIpv4S()
                self.peer_ipv4s.parent = self
                self._children_name_map["peer_ipv4s"] = "peer-ipv4s"
                self._children_yang_names.add("peer-ipv4s")

                self.peer_ipv6s = Ntp.PeerVrfs.PeerVrf.PeerIpv6S()
                self.peer_ipv6s.parent = self
                self._children_name_map["peer_ipv6s"] = "peer-ipv6s"
                self._children_yang_names.add("peer-ipv6s")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ntp.PeerVrfs.PeerVrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ntp.PeerVrfs.PeerVrf, self).__setattr__(name, value)


            class PeerIpv4S(Entity):
                """
                Configures IPv4 NTP Peers or Servers
                
                .. attribute:: peer_ipv4
                
                	Configure an IPv4 NTP server or peer
                	**type**\: list of    :py:class:`PeerIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S, self).__init__()

                    self.yang_name = "peer-ipv4s"
                    self.yang_parent_name = "peer-vrf"

                    self.peer_ipv4 = YList(self)

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
                                super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S, self).__setattr__(name, value)


                class PeerIpv4(Entity):
                    """
                    Configure an IPv4 NTP server or peer
                    
                    .. attribute:: address_ipv4  <key>
                    
                    	IPv4 Address of a peer
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_type_ipv4
                    
                    	Configure an IPv4 NTP server or peer
                    	**type**\: list of    :py:class:`PeerTypeIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4, self).__init__()

                        self.yang_name = "peer-ipv4"
                        self.yang_parent_name = "peer-ipv4s"

                        self.address_ipv4 = YLeaf(YType.str, "address-ipv4")

                        self.peer_type_ipv4 = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address_ipv4") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4, self).__setattr__(name, value)


                    class PeerTypeIpv4(Entity):
                        """
                        Configure an IPv4 NTP server or peer
                        
                        .. attribute:: peer_type  <key>
                        
                        	Peer or Server
                        	**type**\:   :py:class:`NtpPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpPeer>`
                        
                        .. attribute:: authentication_key
                        
                        	Authentication Key
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: burst
                        
                        	Use burst mode
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: iburst
                        
                        	Use iburst mode
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: max_poll
                        
                        	Maxinum poll interval
                        	**type**\:  int
                        
                        	**range:** 4..17
                        
                        .. attribute:: min_poll
                        
                        	Minimum poll interval
                        	**type**\:  int
                        
                        	**range:** 4..17
                        
                        .. attribute:: ntp_version
                        
                        	NTP version
                        	**type**\:  int
                        
                        	**range:** 2..4
                        
                        .. attribute:: preferred_peer
                        
                        	Preferred peer
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: source_interface
                        
                        	Source interface of this peer
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4, self).__init__()

                            self.yang_name = "peer-type-ipv4"
                            self.yang_parent_name = "peer-ipv4"

                            self.peer_type = YLeaf(YType.enumeration, "peer-type")

                            self.authentication_key = YLeaf(YType.uint32, "authentication-key")

                            self.burst = YLeaf(YType.empty, "burst")

                            self.iburst = YLeaf(YType.empty, "iburst")

                            self.max_poll = YLeaf(YType.uint32, "max-poll")

                            self.min_poll = YLeaf(YType.uint32, "min-poll")

                            self.ntp_version = YLeaf(YType.uint32, "ntp-version")

                            self.preferred_peer = YLeaf(YType.empty, "preferred-peer")

                            self.source_interface = YLeaf(YType.str, "source-interface")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("peer_type",
                                            "authentication_key",
                                            "burst",
                                            "iburst",
                                            "max_poll",
                                            "min_poll",
                                            "ntp_version",
                                            "preferred_peer",
                                            "source_interface") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.peer_type.is_set or
                                self.authentication_key.is_set or
                                self.burst.is_set or
                                self.iburst.is_set or
                                self.max_poll.is_set or
                                self.min_poll.is_set or
                                self.ntp_version.is_set or
                                self.preferred_peer.is_set or
                                self.source_interface.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.peer_type.yfilter != YFilter.not_set or
                                self.authentication_key.yfilter != YFilter.not_set or
                                self.burst.yfilter != YFilter.not_set or
                                self.iburst.yfilter != YFilter.not_set or
                                self.max_poll.yfilter != YFilter.not_set or
                                self.min_poll.yfilter != YFilter.not_set or
                                self.ntp_version.yfilter != YFilter.not_set or
                                self.preferred_peer.yfilter != YFilter.not_set or
                                self.source_interface.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "peer-type-ipv4" + "[peer-type='" + self.peer_type.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.peer_type.is_set or self.peer_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_type.get_name_leafdata())
                            if (self.authentication_key.is_set or self.authentication_key.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authentication_key.get_name_leafdata())
                            if (self.burst.is_set or self.burst.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.burst.get_name_leafdata())
                            if (self.iburst.is_set or self.iburst.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.iburst.get_name_leafdata())
                            if (self.max_poll.is_set or self.max_poll.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max_poll.get_name_leafdata())
                            if (self.min_poll.is_set or self.min_poll.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.min_poll.get_name_leafdata())
                            if (self.ntp_version.is_set or self.ntp_version.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ntp_version.get_name_leafdata())
                            if (self.preferred_peer.is_set or self.preferred_peer.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.preferred_peer.get_name_leafdata())
                            if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_interface.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "peer-type" or name == "authentication-key" or name == "burst" or name == "iburst" or name == "max-poll" or name == "min-poll" or name == "ntp-version" or name == "preferred-peer" or name == "source-interface"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "peer-type"):
                                self.peer_type = value
                                self.peer_type.value_namespace = name_space
                                self.peer_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "authentication-key"):
                                self.authentication_key = value
                                self.authentication_key.value_namespace = name_space
                                self.authentication_key.value_namespace_prefix = name_space_prefix
                            if(value_path == "burst"):
                                self.burst = value
                                self.burst.value_namespace = name_space
                                self.burst.value_namespace_prefix = name_space_prefix
                            if(value_path == "iburst"):
                                self.iburst = value
                                self.iburst.value_namespace = name_space
                                self.iburst.value_namespace_prefix = name_space_prefix
                            if(value_path == "max-poll"):
                                self.max_poll = value
                                self.max_poll.value_namespace = name_space
                                self.max_poll.value_namespace_prefix = name_space_prefix
                            if(value_path == "min-poll"):
                                self.min_poll = value
                                self.min_poll.value_namespace = name_space
                                self.min_poll.value_namespace_prefix = name_space_prefix
                            if(value_path == "ntp-version"):
                                self.ntp_version = value
                                self.ntp_version.value_namespace = name_space
                                self.ntp_version.value_namespace_prefix = name_space_prefix
                            if(value_path == "preferred-peer"):
                                self.preferred_peer = value
                                self.preferred_peer.value_namespace = name_space
                                self.preferred_peer.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-interface"):
                                self.source_interface = value
                                self.source_interface.value_namespace = name_space
                                self.source_interface.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.peer_type_ipv4:
                            if (c.has_data()):
                                return True
                        return self.address_ipv4.is_set

                    def has_operation(self):
                        for c in self.peer_type_ipv4:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address_ipv4.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "peer-ipv4" + "[address-ipv4='" + self.address_ipv4.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address_ipv4.is_set or self.address_ipv4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address_ipv4.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "peer-type-ipv4"):
                            for c in self.peer_type_ipv4:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.peer_type_ipv4.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "peer-type-ipv4" or name == "address-ipv4"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address-ipv4"):
                            self.address_ipv4 = value
                            self.address_ipv4.value_namespace = name_space
                            self.address_ipv4.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.peer_ipv4:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.peer_ipv4:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "peer-ipv4s" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "peer-ipv4"):
                        for c in self.peer_ipv4:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.peer_ipv4.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "peer-ipv4"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class PeerIpv6S(Entity):
                """
                Configuration NTP Peers or Servers of IPV6
                
                .. attribute:: peer_ipv6
                
                	Configure a NTP server or peer
                	**type**\: list of    :py:class:`PeerIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S, self).__init__()

                    self.yang_name = "peer-ipv6s"
                    self.yang_parent_name = "peer-vrf"

                    self.peer_ipv6 = YList(self)

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
                                super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S, self).__setattr__(name, value)


                class PeerIpv6(Entity):
                    """
                    Configure a NTP server or peer
                    
                    .. attribute:: address_ipv6  <key>
                    
                    	Address of a peer
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_type_ipv6
                    
                    	Configure a NTP server or peer
                    	**type**\: list of    :py:class:`PeerTypeIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6, self).__init__()

                        self.yang_name = "peer-ipv6"
                        self.yang_parent_name = "peer-ipv6s"

                        self.address_ipv6 = YLeaf(YType.str, "address-ipv6")

                        self.peer_type_ipv6 = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address_ipv6") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6, self).__setattr__(name, value)


                    class PeerTypeIpv6(Entity):
                        """
                        Configure a NTP server or peer
                        
                        .. attribute:: peer_type  <key>
                        
                        	Peer or Server
                        	**type**\:   :py:class:`NtpPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpPeer>`
                        
                        .. attribute:: address_ipv6
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: authentication_key
                        
                        	Authentication Key
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: burst
                        
                        	Use burst mode
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: iburst
                        
                        	Use iburst mode
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: max_poll
                        
                        	Maxinum poll interval
                        	**type**\:  int
                        
                        	**range:** 4..17
                        
                        .. attribute:: min_poll
                        
                        	Minimum poll interval
                        	**type**\:  int
                        
                        	**range:** 4..17
                        
                        .. attribute:: ntp_version
                        
                        	NTP version
                        	**type**\:  int
                        
                        	**range:** 2..4
                        
                        .. attribute:: preferred_peer
                        
                        	Preferred peer
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: source_interface
                        
                        	Source interface of this peer
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6, self).__init__()

                            self.yang_name = "peer-type-ipv6"
                            self.yang_parent_name = "peer-ipv6"

                            self.peer_type = YLeaf(YType.enumeration, "peer-type")

                            self.address_ipv6 = YLeaf(YType.str, "address-ipv6")

                            self.authentication_key = YLeaf(YType.uint32, "authentication-key")

                            self.burst = YLeaf(YType.empty, "burst")

                            self.iburst = YLeaf(YType.empty, "iburst")

                            self.max_poll = YLeaf(YType.uint32, "max-poll")

                            self.min_poll = YLeaf(YType.uint32, "min-poll")

                            self.ntp_version = YLeaf(YType.uint32, "ntp-version")

                            self.preferred_peer = YLeaf(YType.empty, "preferred-peer")

                            self.source_interface = YLeaf(YType.str, "source-interface")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("peer_type",
                                            "address_ipv6",
                                            "authentication_key",
                                            "burst",
                                            "iburst",
                                            "max_poll",
                                            "min_poll",
                                            "ntp_version",
                                            "preferred_peer",
                                            "source_interface") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.peer_type.is_set or
                                self.address_ipv6.is_set or
                                self.authentication_key.is_set or
                                self.burst.is_set or
                                self.iburst.is_set or
                                self.max_poll.is_set or
                                self.min_poll.is_set or
                                self.ntp_version.is_set or
                                self.preferred_peer.is_set or
                                self.source_interface.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.peer_type.yfilter != YFilter.not_set or
                                self.address_ipv6.yfilter != YFilter.not_set or
                                self.authentication_key.yfilter != YFilter.not_set or
                                self.burst.yfilter != YFilter.not_set or
                                self.iburst.yfilter != YFilter.not_set or
                                self.max_poll.yfilter != YFilter.not_set or
                                self.min_poll.yfilter != YFilter.not_set or
                                self.ntp_version.yfilter != YFilter.not_set or
                                self.preferred_peer.yfilter != YFilter.not_set or
                                self.source_interface.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "peer-type-ipv6" + "[peer-type='" + self.peer_type.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.peer_type.is_set or self.peer_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_type.get_name_leafdata())
                            if (self.address_ipv6.is_set or self.address_ipv6.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address_ipv6.get_name_leafdata())
                            if (self.authentication_key.is_set or self.authentication_key.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authentication_key.get_name_leafdata())
                            if (self.burst.is_set or self.burst.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.burst.get_name_leafdata())
                            if (self.iburst.is_set or self.iburst.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.iburst.get_name_leafdata())
                            if (self.max_poll.is_set or self.max_poll.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max_poll.get_name_leafdata())
                            if (self.min_poll.is_set or self.min_poll.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.min_poll.get_name_leafdata())
                            if (self.ntp_version.is_set or self.ntp_version.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ntp_version.get_name_leafdata())
                            if (self.preferred_peer.is_set or self.preferred_peer.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.preferred_peer.get_name_leafdata())
                            if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_interface.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "peer-type" or name == "address-ipv6" or name == "authentication-key" or name == "burst" or name == "iburst" or name == "max-poll" or name == "min-poll" or name == "ntp-version" or name == "preferred-peer" or name == "source-interface"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "peer-type"):
                                self.peer_type = value
                                self.peer_type.value_namespace = name_space
                                self.peer_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "address-ipv6"):
                                self.address_ipv6 = value
                                self.address_ipv6.value_namespace = name_space
                                self.address_ipv6.value_namespace_prefix = name_space_prefix
                            if(value_path == "authentication-key"):
                                self.authentication_key = value
                                self.authentication_key.value_namespace = name_space
                                self.authentication_key.value_namespace_prefix = name_space_prefix
                            if(value_path == "burst"):
                                self.burst = value
                                self.burst.value_namespace = name_space
                                self.burst.value_namespace_prefix = name_space_prefix
                            if(value_path == "iburst"):
                                self.iburst = value
                                self.iburst.value_namespace = name_space
                                self.iburst.value_namespace_prefix = name_space_prefix
                            if(value_path == "max-poll"):
                                self.max_poll = value
                                self.max_poll.value_namespace = name_space
                                self.max_poll.value_namespace_prefix = name_space_prefix
                            if(value_path == "min-poll"):
                                self.min_poll = value
                                self.min_poll.value_namespace = name_space
                                self.min_poll.value_namespace_prefix = name_space_prefix
                            if(value_path == "ntp-version"):
                                self.ntp_version = value
                                self.ntp_version.value_namespace = name_space
                                self.ntp_version.value_namespace_prefix = name_space_prefix
                            if(value_path == "preferred-peer"):
                                self.preferred_peer = value
                                self.preferred_peer.value_namespace = name_space
                                self.preferred_peer.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-interface"):
                                self.source_interface = value
                                self.source_interface.value_namespace = name_space
                                self.source_interface.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.peer_type_ipv6:
                            if (c.has_data()):
                                return True
                        return self.address_ipv6.is_set

                    def has_operation(self):
                        for c in self.peer_type_ipv6:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address_ipv6.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "peer-ipv6" + "[address-ipv6='" + self.address_ipv6.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address_ipv6.is_set or self.address_ipv6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address_ipv6.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "peer-type-ipv6"):
                            for c in self.peer_type_ipv6:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.peer_type_ipv6.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "peer-type-ipv6" or name == "address-ipv6"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address-ipv6"):
                            self.address_ipv6 = value
                            self.address_ipv6.value_namespace = name_space
                            self.address_ipv6.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.peer_ipv6:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.peer_ipv6:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "peer-ipv6s" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "peer-ipv6"):
                        for c in self.peer_ipv6:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.peer_ipv6.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "peer-ipv6"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    (self.peer_ipv4s is not None and self.peer_ipv4s.has_data()) or
                    (self.peer_ipv6s is not None and self.peer_ipv6s.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.peer_ipv4s is not None and self.peer_ipv4s.has_operation()) or
                    (self.peer_ipv6s is not None and self.peer_ipv6s.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "peer-vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/peer-vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "peer-ipv4s"):
                    if (self.peer_ipv4s is None):
                        self.peer_ipv4s = Ntp.PeerVrfs.PeerVrf.PeerIpv4S()
                        self.peer_ipv4s.parent = self
                        self._children_name_map["peer_ipv4s"] = "peer-ipv4s"
                    return self.peer_ipv4s

                if (child_yang_name == "peer-ipv6s"):
                    if (self.peer_ipv6s is None):
                        self.peer_ipv6s = Ntp.PeerVrfs.PeerVrf.PeerIpv6S()
                        self.peer_ipv6s.parent = self
                        self._children_name_map["peer_ipv6s"] = "peer-ipv6s"
                    return self.peer_ipv6s

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "peer-ipv4s" or name == "peer-ipv6s" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.peer_vrf:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.peer_vrf:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "peer-vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "peer-vrf"):
                for c in self.peer_vrf:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ntp.PeerVrfs.PeerVrf()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.peer_vrf.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "peer-vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class DscpIpv4(Entity):
        """
         Set IP DSCP value for outgoing NTP IPV4 packets
        
        .. attribute:: dscp_or_precedence_value
        
        	If Mode is set to 'NTPPRECEDENCE(0)' specify Precedence value , if Mode is set to 'NTPDSCP(1)' specify DSCP
        	**type**\:  int
        
        	**range:** 0..63
        
        	**mandatory**\: True
        
        .. attribute:: mode
        
        	NTPPRECEDENCE (0) to specify Precedence value  NTPDSCP (1) to specify DSCP value
        	**type**\:   :py:class:`Ntpdscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntpdscp>`
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ntp.DscpIpv4, self).__init__()

            self.yang_name = "dscp-ipv4"
            self.yang_parent_name = "ntp"
            self.is_presence_container = True

            self.dscp_or_precedence_value = YLeaf(YType.uint32, "dscp-or-precedence-value")

            self.mode = YLeaf(YType.enumeration, "mode")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dscp_or_precedence_value",
                            "mode") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ntp.DscpIpv4, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ntp.DscpIpv4, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.dscp_or_precedence_value.is_set or
                self.mode.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dscp_or_precedence_value.yfilter != YFilter.not_set or
                self.mode.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dscp-ipv4" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dscp_or_precedence_value.is_set or self.dscp_or_precedence_value.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dscp_or_precedence_value.get_name_leafdata())
            if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mode.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dscp-or-precedence-value" or name == "mode"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dscp-or-precedence-value"):
                self.dscp_or_precedence_value = value
                self.dscp_or_precedence_value.value_namespace = name_space
                self.dscp_or_precedence_value.value_namespace_prefix = name_space_prefix
            if(value_path == "mode"):
                self.mode = value
                self.mode.value_namespace = name_space
                self.mode.value_namespace_prefix = name_space_prefix


    class DscpIpv6(Entity):
        """
         Set IP DSCP value for outgoing NTP IPV6 packets
        
        .. attribute:: dscp_or_precedence_value
        
        	If Mode is set to 'NTPPRECEDENCE(0)' specify Precedence value , if Mode is set to 'NTPDSCP(1)' specify DSCP
        	**type**\:  int
        
        	**range:** 0..63
        
        	**mandatory**\: True
        
        .. attribute:: mode
        
        	NTPPRECEDENCE(0) to specify Precedence value NTPDSCP(1) to specify DSCP value
        	**type**\:   :py:class:`Ntpdscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntpdscp>`
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ntp.DscpIpv6, self).__init__()

            self.yang_name = "dscp-ipv6"
            self.yang_parent_name = "ntp"
            self.is_presence_container = True

            self.dscp_or_precedence_value = YLeaf(YType.uint32, "dscp-or-precedence-value")

            self.mode = YLeaf(YType.enumeration, "mode")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dscp_or_precedence_value",
                            "mode") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ntp.DscpIpv6, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ntp.DscpIpv6, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.dscp_or_precedence_value.is_set or
                self.mode.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dscp_or_precedence_value.yfilter != YFilter.not_set or
                self.mode.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dscp-ipv6" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dscp_or_precedence_value.is_set or self.dscp_or_precedence_value.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dscp_or_precedence_value.get_name_leafdata())
            if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mode.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dscp-or-precedence-value" or name == "mode"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dscp-or-precedence-value"):
                self.dscp_or_precedence_value = value
                self.dscp_or_precedence_value.value_namespace = name_space
                self.dscp_or_precedence_value.value_namespace_prefix = name_space_prefix
            if(value_path == "mode"):
                self.mode = value
                self.mode.value_namespace = name_space
                self.mode.value_namespace_prefix = name_space_prefix


    class Sources(Entity):
        """
        Configure  NTP source interface
        
        .. attribute:: source
        
        	Configure  NTP source interface
        	**type**\: list of    :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Sources.Source>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ntp.Sources, self).__init__()

            self.yang_name = "sources"
            self.yang_parent_name = "ntp"

            self.source = YList(self)

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
                        super(Ntp.Sources, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ntp.Sources, self).__setattr__(name, value)


        class Source(Entity):
            """
            Configure  NTP source interface
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: source_interface
            
            	Source Interface for NTP
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ntp.Sources.Source, self).__init__()

                self.yang_name = "source"
                self.yang_parent_name = "sources"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.source_interface = YLeaf(YType.str, "source-interface")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name",
                                "source_interface") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ntp.Sources.Source, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ntp.Sources.Source, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    self.source_interface.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.source_interface.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "source" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/sources/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_interface.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vrf-name" or name == "source-interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "source-interface"):
                    self.source_interface = value
                    self.source_interface.value_namespace = name_space
                    self.source_interface.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.source:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.source:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sources" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "source"):
                for c in self.source:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ntp.Sources.Source()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.source.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "source"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Authentication(Entity):
        """
        Configure NTP Authentication keys
        
        .. attribute:: enable
        
        	Enable NTP authentication keys
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: keies
        
        	Authentication Key Table
        	**type**\:   :py:class:`Keies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.Keies>`
        
        .. attribute:: trusted_keies
        
        	Key numbers for trusted time sources
        	**type**\:   :py:class:`TrustedKeies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.TrustedKeies>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ntp.Authentication, self).__init__()

            self.yang_name = "authentication"
            self.yang_parent_name = "ntp"

            self.enable = YLeaf(YType.empty, "enable")

            self.keies = Ntp.Authentication.Keies()
            self.keies.parent = self
            self._children_name_map["keies"] = "keies"
            self._children_yang_names.add("keies")

            self.trusted_keies = Ntp.Authentication.TrustedKeies()
            self.trusted_keies.parent = self
            self._children_name_map["trusted_keies"] = "trusted-keies"
            self._children_yang_names.add("trusted-keies")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ntp.Authentication, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ntp.Authentication, self).__setattr__(name, value)


        class Keies(Entity):
            """
            Authentication Key Table
            
            .. attribute:: key
            
            	Authentication key for trusted time sources
            	**type**\: list of    :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.Keies.Key>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ntp.Authentication.Keies, self).__init__()

                self.yang_name = "keies"
                self.yang_parent_name = "authentication"

                self.key = YList(self)

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
                            super(Ntp.Authentication.Keies, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ntp.Authentication.Keies, self).__setattr__(name, value)


            class Key(Entity):
                """
                Authentication key for trusted time sources
                
                .. attribute:: key_number  <key>
                
                	Authentication Key number
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: authentication_key
                
                	Authentication key \- maximum 32 characters
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ntp.Authentication.Keies.Key, self).__init__()

                    self.yang_name = "key"
                    self.yang_parent_name = "keies"

                    self.key_number = YLeaf(YType.uint32, "key-number")

                    self.authentication_key = YLeaf(YType.str, "authentication-key")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("key_number",
                                    "authentication_key") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ntp.Authentication.Keies.Key, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ntp.Authentication.Keies.Key, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.key_number.is_set or
                        self.authentication_key.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.key_number.yfilter != YFilter.not_set or
                        self.authentication_key.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "key" + "[key-number='" + self.key_number.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/keies/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.key_number.is_set or self.key_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.key_number.get_name_leafdata())
                    if (self.authentication_key.is_set or self.authentication_key.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_key.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "key-number" or name == "authentication-key"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "key-number"):
                        self.key_number = value
                        self.key_number.value_namespace = name_space
                        self.key_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-key"):
                        self.authentication_key = value
                        self.authentication_key.value_namespace = name_space
                        self.authentication_key.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.key:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.key:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "keies" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "key"):
                    for c in self.key:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Ntp.Authentication.Keies.Key()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.key.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "key"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class TrustedKeies(Entity):
            """
            Key numbers for trusted time sources
            
            .. attribute:: trusted_key
            
            	Configure NTP trusted key
            	**type**\: list of    :py:class:`TrustedKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.TrustedKeies.TrustedKey>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ntp.Authentication.TrustedKeies, self).__init__()

                self.yang_name = "trusted-keies"
                self.yang_parent_name = "authentication"

                self.trusted_key = YList(self)

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
                            super(Ntp.Authentication.TrustedKeies, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ntp.Authentication.TrustedKeies, self).__setattr__(name, value)


            class TrustedKey(Entity):
                """
                Configure NTP trusted key
                
                .. attribute:: key_number  <key>
                
                	Key number
                	**type**\:  int
                
                	**range:** 1..65535
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ntp.Authentication.TrustedKeies.TrustedKey, self).__init__()

                    self.yang_name = "trusted-key"
                    self.yang_parent_name = "trusted-keies"

                    self.key_number = YLeaf(YType.uint32, "key-number")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("key_number") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ntp.Authentication.TrustedKeies.TrustedKey, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ntp.Authentication.TrustedKeies.TrustedKey, self).__setattr__(name, value)

                def has_data(self):
                    return self.key_number.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.key_number.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "trusted-key" + "[key-number='" + self.key_number.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/trusted-keies/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.key_number.is_set or self.key_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.key_number.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "key-number"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "key-number"):
                        self.key_number = value
                        self.key_number.value_namespace = name_space
                        self.key_number.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.trusted_key:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.trusted_key:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "trusted-keies" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "trusted-key"):
                    for c in self.trusted_key:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Ntp.Authentication.TrustedKeies.TrustedKey()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.trusted_key.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "trusted-key"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.enable.is_set or
                (self.keies is not None and self.keies.has_data()) or
                (self.trusted_keies is not None and self.trusted_keies.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                (self.keies is not None and self.keies.has_operation()) or
                (self.trusted_keies is not None and self.trusted_keies.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "authentication" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "keies"):
                if (self.keies is None):
                    self.keies = Ntp.Authentication.Keies()
                    self.keies.parent = self
                    self._children_name_map["keies"] = "keies"
                return self.keies

            if (child_yang_name == "trusted-keies"):
                if (self.trusted_keies is None):
                    self.trusted_keies = Ntp.Authentication.TrustedKeies()
                    self.trusted_keies.parent = self
                    self._children_name_map["trusted_keies"] = "trusted-keies"
                return self.trusted_keies

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "keies" or name == "trusted-keies" or name == "enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix


    class Passive(Entity):
        """
        Configure NTP passive associations
        
        .. attribute:: enable
        
        	Enable NTP Passive associations
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ntp.Passive, self).__init__()

            self.yang_name = "passive"
            self.yang_parent_name = "ntp"

            self.enable = YLeaf(YType.empty, "enable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ntp.Passive, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ntp.Passive, self).__setattr__(name, value)

        def has_data(self):
            return self.enable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "passive" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix


    class InterfaceTables(Entity):
        """
        NTP per interface configuration
        
        .. attribute:: interface_table
        
        	NTP per interface configuration
        	**type**\: list of    :py:class:`InterfaceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ntp.InterfaceTables, self).__init__()

            self.yang_name = "interface-tables"
            self.yang_parent_name = "ntp"

            self.interface_table = YList(self)

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
                        super(Ntp.InterfaceTables, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ntp.InterfaceTables, self).__setattr__(name, value)


        class InterfaceTable(Entity):
            """
            NTP per interface configuration
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: interface
            
            	Name of the interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ntp.InterfaceTables.InterfaceTable, self).__init__()

                self.yang_name = "interface-table"
                self.yang_parent_name = "interface-tables"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

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
                    if name in ("vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ntp.InterfaceTables.InterfaceTable, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ntp.InterfaceTables.InterfaceTable, self).__setattr__(name, value)


            class Interface(Entity):
                """
                Name of the interface
                
                .. attribute:: interface  <key>
                
                	interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: disable
                
                	Disable NTP
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interface_broadcast
                
                	Configure NTP broadcast service
                	**type**\:   :py:class:`InterfaceBroadcast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast>`
                
                .. attribute:: interface_multicast
                
                	Configure NTP multicast service
                	**type**\:   :py:class:`InterfaceMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ntp.InterfaceTables.InterfaceTable.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interface-table"

                    self.interface = YLeaf(YType.str, "interface")

                    self.disable = YLeaf(YType.empty, "disable")

                    self.interface_broadcast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast()
                    self.interface_broadcast.parent = self
                    self._children_name_map["interface_broadcast"] = "interface-broadcast"
                    self._children_yang_names.add("interface-broadcast")

                    self.interface_multicast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast()
                    self.interface_multicast.parent = self
                    self._children_name_map["interface_multicast"] = "interface-multicast"
                    self._children_yang_names.add("interface-multicast")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface",
                                    "disable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ntp.InterfaceTables.InterfaceTable.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ntp.InterfaceTables.InterfaceTable.Interface, self).__setattr__(name, value)


                class InterfaceMulticast(Entity):
                    """
                    Configure NTP multicast service
                    
                    .. attribute:: multicast_clients
                    
                    	Configures multicast client peers
                    	**type**\:   :py:class:`MulticastClients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients>`
                    
                    .. attribute:: multicast_servers
                    
                    	Configures multicast server peers
                    	**type**\:   :py:class:`MulticastServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast, self).__init__()

                        self.yang_name = "interface-multicast"
                        self.yang_parent_name = "interface"

                        self.multicast_clients = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients()
                        self.multicast_clients.parent = self
                        self._children_name_map["multicast_clients"] = "multicast-clients"
                        self._children_yang_names.add("multicast-clients")

                        self.multicast_servers = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers()
                        self.multicast_servers.parent = self
                        self._children_name_map["multicast_servers"] = "multicast-servers"
                        self._children_yang_names.add("multicast-servers")


                    class MulticastClients(Entity):
                        """
                        Configures multicast client peers
                        
                        .. attribute:: multicast_client
                        
                        	Listen to NTP multicasts
                        	**type**\: list of    :py:class:`MulticastClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient>`
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients, self).__init__()

                            self.yang_name = "multicast-clients"
                            self.yang_parent_name = "interface-multicast"

                            self.multicast_client = YList(self)

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
                                        super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients, self).__setattr__(name, value)


                        class MulticastClient(Entity):
                            """
                            Listen to NTP multicasts
                            
                            .. attribute:: ip_address  <key>
                            
                            	IP address of a multicast group
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'ip-ntp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient, self).__init__()

                                self.yang_name = "multicast-client"
                                self.yang_parent_name = "multicast-clients"

                                self.ip_address = YLeaf(YType.str, "ip-address")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ip_address") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient, self).__setattr__(name, value)

                            def has_data(self):
                                return self.ip_address.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ip_address.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "multicast-client" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ip_address.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ip-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ip-address"):
                                    self.ip_address = value
                                    self.ip_address.value_namespace = name_space
                                    self.ip_address.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.multicast_client:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.multicast_client:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "multicast-clients" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "multicast-client"):
                                for c in self.multicast_client:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.multicast_client.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "multicast-client"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class MulticastServers(Entity):
                        """
                        Configures multicast server peers
                        
                        .. attribute:: multicast_server
                        
                        	Configure NTP multicast group server peer
                        	**type**\: list of    :py:class:`MulticastServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer>`
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers, self).__init__()

                            self.yang_name = "multicast-servers"
                            self.yang_parent_name = "interface-multicast"

                            self.multicast_server = YList(self)

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
                                        super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers, self).__setattr__(name, value)


                        class MulticastServer(Entity):
                            """
                            Configure NTP multicast group server peer
                            
                            .. attribute:: ip_address  <key>
                            
                            	IP address of a multicast group
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: authentication_key
                            
                            	Authentication key
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: ttl
                            
                            	TTL
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: version
                            
                            	NTP version
                            	**type**\:  int
                            
                            	**range:** 2..4
                            
                            

                            """

                            _prefix = 'ip-ntp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer, self).__init__()

                                self.yang_name = "multicast-server"
                                self.yang_parent_name = "multicast-servers"

                                self.ip_address = YLeaf(YType.str, "ip-address")

                                self.authentication_key = YLeaf(YType.uint32, "authentication-key")

                                self.ttl = YLeaf(YType.uint32, "ttl")

                                self.version = YLeaf(YType.uint32, "version")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ip_address",
                                                "authentication_key",
                                                "ttl",
                                                "version") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ip_address.is_set or
                                    self.authentication_key.is_set or
                                    self.ttl.is_set or
                                    self.version.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ip_address.yfilter != YFilter.not_set or
                                    self.authentication_key.yfilter != YFilter.not_set or
                                    self.ttl.yfilter != YFilter.not_set or
                                    self.version.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "multicast-server" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ip_address.get_name_leafdata())
                                if (self.authentication_key.is_set or self.authentication_key.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authentication_key.get_name_leafdata())
                                if (self.ttl.is_set or self.ttl.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ttl.get_name_leafdata())
                                if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.version.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ip-address" or name == "authentication-key" or name == "ttl" or name == "version"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ip-address"):
                                    self.ip_address = value
                                    self.ip_address.value_namespace = name_space
                                    self.ip_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "authentication-key"):
                                    self.authentication_key = value
                                    self.authentication_key.value_namespace = name_space
                                    self.authentication_key.value_namespace_prefix = name_space_prefix
                                if(value_path == "ttl"):
                                    self.ttl = value
                                    self.ttl.value_namespace = name_space
                                    self.ttl.value_namespace_prefix = name_space_prefix
                                if(value_path == "version"):
                                    self.version = value
                                    self.version.value_namespace = name_space
                                    self.version.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.multicast_server:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.multicast_server:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "multicast-servers" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "multicast-server"):
                                for c in self.multicast_server:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.multicast_server.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "multicast-server"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            (self.multicast_clients is not None and self.multicast_clients.has_data()) or
                            (self.multicast_servers is not None and self.multicast_servers.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.multicast_clients is not None and self.multicast_clients.has_operation()) or
                            (self.multicast_servers is not None and self.multicast_servers.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-multicast" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "multicast-clients"):
                            if (self.multicast_clients is None):
                                self.multicast_clients = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients()
                                self.multicast_clients.parent = self
                                self._children_name_map["multicast_clients"] = "multicast-clients"
                            return self.multicast_clients

                        if (child_yang_name == "multicast-servers"):
                            if (self.multicast_servers is None):
                                self.multicast_servers = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers()
                                self.multicast_servers.parent = self
                                self._children_name_map["multicast_servers"] = "multicast-servers"
                            return self.multicast_servers

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "multicast-clients" or name == "multicast-servers"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class InterfaceBroadcast(Entity):
                    """
                    Configure NTP broadcast service
                    
                    .. attribute:: broadcast
                    
                    	Configure NTP broadcast
                    	**type**\:   :py:class:`Broadcast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast>`
                    
                    .. attribute:: broadcast_client
                    
                    	Listen to NTP broadcasts
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast, self).__init__()

                        self.yang_name = "interface-broadcast"
                        self.yang_parent_name = "interface"

                        self.broadcast_client = YLeaf(YType.empty, "broadcast-client")

                        self.broadcast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast()
                        self.broadcast.parent = self
                        self._children_name_map["broadcast"] = "broadcast"
                        self._children_yang_names.add("broadcast")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("broadcast_client") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast, self).__setattr__(name, value)


                    class Broadcast(Entity):
                        """
                        Configure NTP broadcast
                        
                        .. attribute:: address
                        
                        	Destination broadcast IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: authentication_key
                        
                        	Authentication key
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: ntp_version
                        
                        	NTP version
                        	**type**\:  int
                        
                        	**range:** 2..4
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast, self).__init__()

                            self.yang_name = "broadcast"
                            self.yang_parent_name = "interface-broadcast"

                            self.address = YLeaf(YType.str, "address")

                            self.authentication_key = YLeaf(YType.uint32, "authentication-key")

                            self.ntp_version = YLeaf(YType.uint32, "ntp-version")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("address",
                                            "authentication_key",
                                            "ntp_version") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.address.is_set or
                                self.authentication_key.is_set or
                                self.ntp_version.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address.yfilter != YFilter.not_set or
                                self.authentication_key.yfilter != YFilter.not_set or
                                self.ntp_version.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "broadcast" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address.get_name_leafdata())
                            if (self.authentication_key.is_set or self.authentication_key.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authentication_key.get_name_leafdata())
                            if (self.ntp_version.is_set or self.ntp_version.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ntp_version.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address" or name == "authentication-key" or name == "ntp-version"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address"):
                                self.address = value
                                self.address.value_namespace = name_space
                                self.address.value_namespace_prefix = name_space_prefix
                            if(value_path == "authentication-key"):
                                self.authentication_key = value
                                self.authentication_key.value_namespace = name_space
                                self.authentication_key.value_namespace_prefix = name_space_prefix
                            if(value_path == "ntp-version"):
                                self.ntp_version = value
                                self.ntp_version.value_namespace = name_space
                                self.ntp_version.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.broadcast_client.is_set or
                            (self.broadcast is not None and self.broadcast.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.broadcast_client.yfilter != YFilter.not_set or
                            (self.broadcast is not None and self.broadcast.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-broadcast" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.broadcast_client.is_set or self.broadcast_client.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.broadcast_client.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "broadcast"):
                            if (self.broadcast is None):
                                self.broadcast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast()
                                self.broadcast.parent = self
                                self._children_name_map["broadcast"] = "broadcast"
                            return self.broadcast

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "broadcast" or name == "broadcast-client"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "broadcast-client"):
                            self.broadcast_client = value
                            self.broadcast_client.value_namespace = name_space
                            self.broadcast_client.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.interface.is_set or
                        self.disable.is_set or
                        (self.interface_broadcast is not None and self.interface_broadcast.has_data()) or
                        (self.interface_multicast is not None and self.interface_multicast.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.disable.yfilter != YFilter.not_set or
                        (self.interface_broadcast is not None and self.interface_broadcast.has_operation()) or
                        (self.interface_multicast is not None and self.interface_multicast.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface='" + self.interface.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface-broadcast"):
                        if (self.interface_broadcast is None):
                            self.interface_broadcast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast()
                            self.interface_broadcast.parent = self
                            self._children_name_map["interface_broadcast"] = "interface-broadcast"
                        return self.interface_broadcast

                    if (child_yang_name == "interface-multicast"):
                        if (self.interface_multicast is None):
                            self.interface_multicast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast()
                            self.interface_multicast.parent = self
                            self._children_name_map["interface_multicast"] = "interface-multicast"
                        return self.interface_multicast

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-broadcast" or name == "interface-multicast" or name == "interface" or name == "disable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "disable"):
                        self.disable = value
                        self.disable.value_namespace = name_space
                        self.disable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return self.vrf_name.is_set

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface-table" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/interface-tables/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

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
                    c = Ntp.InterfaceTables.InterfaceTable.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface_table:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface_table:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interface-tables" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface-table"):
                for c in self.interface_table:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ntp.InterfaceTables.InterfaceTable()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface_table.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface-table"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class AccessGroupTables(Entity):
        """
        Control NTP access
        
        .. attribute:: access_group_table
        
        	Control NTP access
        	**type**\: list of    :py:class:`AccessGroupTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables.AccessGroupTable>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ntp.AccessGroupTables, self).__init__()

            self.yang_name = "access-group-tables"
            self.yang_parent_name = "ntp"

            self.access_group_table = YList(self)

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
                        super(Ntp.AccessGroupTables, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ntp.AccessGroupTables, self).__setattr__(name, value)


        class AccessGroupTable(Entity):
            """
            Control NTP access
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: access_group_af_table
            
            	Configure NTP access address family
            	**type**\: list of    :py:class:`AccessGroupAfTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ntp.AccessGroupTables.AccessGroupTable, self).__init__()

                self.yang_name = "access-group-table"
                self.yang_parent_name = "access-group-tables"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.access_group_af_table = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ntp.AccessGroupTables.AccessGroupTable, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ntp.AccessGroupTables.AccessGroupTable, self).__setattr__(name, value)


            class AccessGroupAfTable(Entity):
                """
                Configure NTP access address family
                
                .. attribute:: af  <key>
                
                	Address family
                	**type**\:   :py:class:`NtpAccessAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpAccessAf>`
                
                .. attribute:: access_group
                
                	Configure NTP access group
                	**type**\: list of    :py:class:`AccessGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable, self).__init__()

                    self.yang_name = "access-group-af-table"
                    self.yang_parent_name = "access-group-table"

                    self.af = YLeaf(YType.enumeration, "af")

                    self.access_group = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("af") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable, self).__setattr__(name, value)


                class AccessGroup(Entity):
                    """
                    Configure NTP access group
                    
                    .. attribute:: access_group_type  <key>
                    
                    	Access group type
                    	**type**\:   :py:class:`NtpAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.NtpAccess>`
                    
                    .. attribute:: access_list_name
                    
                    	Access list name \- maximum 32 characters
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ip-ntp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup, self).__init__()

                        self.yang_name = "access-group"
                        self.yang_parent_name = "access-group-af-table"

                        self.access_group_type = YLeaf(YType.enumeration, "access-group-type")

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_group_type",
                                        "access_list_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access_group_type.is_set or
                            self.access_list_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_group_type.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "access-group" + "[access-group-type='" + self.access_group_type.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_group_type.is_set or self.access_group_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_group_type.get_name_leafdata())
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-group-type" or name == "access-list-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-group-type"):
                            self.access_group_type = value
                            self.access_group_type.value_namespace = name_space
                            self.access_group_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.access_group:
                        if (c.has_data()):
                            return True
                    return self.af.is_set

                def has_operation(self):
                    for c in self.access_group:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.af.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "access-group-af-table" + "[af='" + self.af.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.af.is_set or self.af.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.af.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "access-group"):
                        for c in self.access_group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.access_group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-group" or name == "af"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "af"):
                        self.af = value
                        self.af.value_namespace = name_space
                        self.af.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.access_group_af_table:
                    if (c.has_data()):
                        return True
                return self.vrf_name.is_set

            def has_operation(self):
                for c in self.access_group_af_table:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "access-group-table" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/access-group-tables/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "access-group-af-table"):
                    for c in self.access_group_af_table:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.access_group_af_table.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "access-group-af-table" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.access_group_table:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.access_group_table:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "access-group-tables" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "access-group-table"):
                for c in self.access_group_table:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ntp.AccessGroupTables.AccessGroupTable()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.access_group_table.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "access-group-table"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.broadcast_delay.is_set or
            self.log_internal_sync.is_set or
            self.master.is_set or
            self.max_associations.is_set or
            self.update_calendar.is_set or
            (self.access_group_tables is not None and self.access_group_tables.has_data()) or
            (self.authentication is not None and self.authentication.has_data()) or
            (self.interface_tables is not None and self.interface_tables.has_data()) or
            (self.passive is not None and self.passive.has_data()) or
            (self.peer_vrfs is not None and self.peer_vrfs.has_data()) or
            (self.sources is not None and self.sources.has_data()) or
            (self.dscp_ipv4 is not None) or
            (self.dscp_ipv6 is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.broadcast_delay.yfilter != YFilter.not_set or
            self.log_internal_sync.yfilter != YFilter.not_set or
            self.master.yfilter != YFilter.not_set or
            self.max_associations.yfilter != YFilter.not_set or
            self.update_calendar.yfilter != YFilter.not_set or
            (self.access_group_tables is not None and self.access_group_tables.has_operation()) or
            (self.authentication is not None and self.authentication.has_operation()) or
            (self.dscp_ipv4 is not None and self.dscp_ipv4.has_operation()) or
            (self.dscp_ipv6 is not None and self.dscp_ipv6.has_operation()) or
            (self.interface_tables is not None and self.interface_tables.has_operation()) or
            (self.passive is not None and self.passive.has_operation()) or
            (self.peer_vrfs is not None and self.peer_vrfs.has_operation()) or
            (self.sources is not None and self.sources.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-ntp-cfg:ntp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.broadcast_delay.is_set or self.broadcast_delay.yfilter != YFilter.not_set):
            leaf_name_data.append(self.broadcast_delay.get_name_leafdata())
        if (self.log_internal_sync.is_set or self.log_internal_sync.yfilter != YFilter.not_set):
            leaf_name_data.append(self.log_internal_sync.get_name_leafdata())
        if (self.master.is_set or self.master.yfilter != YFilter.not_set):
            leaf_name_data.append(self.master.get_name_leafdata())
        if (self.max_associations.is_set or self.max_associations.yfilter != YFilter.not_set):
            leaf_name_data.append(self.max_associations.get_name_leafdata())
        if (self.update_calendar.is_set or self.update_calendar.yfilter != YFilter.not_set):
            leaf_name_data.append(self.update_calendar.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "access-group-tables"):
            if (self.access_group_tables is None):
                self.access_group_tables = Ntp.AccessGroupTables()
                self.access_group_tables.parent = self
                self._children_name_map["access_group_tables"] = "access-group-tables"
            return self.access_group_tables

        if (child_yang_name == "authentication"):
            if (self.authentication is None):
                self.authentication = Ntp.Authentication()
                self.authentication.parent = self
                self._children_name_map["authentication"] = "authentication"
            return self.authentication

        if (child_yang_name == "dscp-ipv4"):
            if (self.dscp_ipv4 is None):
                self.dscp_ipv4 = Ntp.DscpIpv4()
                self.dscp_ipv4.parent = self
                self._children_name_map["dscp_ipv4"] = "dscp-ipv4"
            return self.dscp_ipv4

        if (child_yang_name == "dscp-ipv6"):
            if (self.dscp_ipv6 is None):
                self.dscp_ipv6 = Ntp.DscpIpv6()
                self.dscp_ipv6.parent = self
                self._children_name_map["dscp_ipv6"] = "dscp-ipv6"
            return self.dscp_ipv6

        if (child_yang_name == "interface-tables"):
            if (self.interface_tables is None):
                self.interface_tables = Ntp.InterfaceTables()
                self.interface_tables.parent = self
                self._children_name_map["interface_tables"] = "interface-tables"
            return self.interface_tables

        if (child_yang_name == "passive"):
            if (self.passive is None):
                self.passive = Ntp.Passive()
                self.passive.parent = self
                self._children_name_map["passive"] = "passive"
            return self.passive

        if (child_yang_name == "peer-vrfs"):
            if (self.peer_vrfs is None):
                self.peer_vrfs = Ntp.PeerVrfs()
                self.peer_vrfs.parent = self
                self._children_name_map["peer_vrfs"] = "peer-vrfs"
            return self.peer_vrfs

        if (child_yang_name == "sources"):
            if (self.sources is None):
                self.sources = Ntp.Sources()
                self.sources.parent = self
                self._children_name_map["sources"] = "sources"
            return self.sources

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "access-group-tables" or name == "authentication" or name == "dscp-ipv4" or name == "dscp-ipv6" or name == "interface-tables" or name == "passive" or name == "peer-vrfs" or name == "sources" or name == "broadcast-delay" or name == "log-internal-sync" or name == "master" or name == "max-associations" or name == "update-calendar"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "broadcast-delay"):
            self.broadcast_delay = value
            self.broadcast_delay.value_namespace = name_space
            self.broadcast_delay.value_namespace_prefix = name_space_prefix
        if(value_path == "log-internal-sync"):
            self.log_internal_sync = value
            self.log_internal_sync.value_namespace = name_space
            self.log_internal_sync.value_namespace_prefix = name_space_prefix
        if(value_path == "master"):
            self.master = value
            self.master.value_namespace = name_space
            self.master.value_namespace_prefix = name_space_prefix
        if(value_path == "max-associations"):
            self.max_associations = value
            self.max_associations.value_namespace = name_space
            self.max_associations.value_namespace_prefix = name_space_prefix
        if(value_path == "update-calendar"):
            self.update_calendar = value
            self.update_calendar.value_namespace = name_space
            self.update_calendar.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Ntp()
        return self._top_entity

