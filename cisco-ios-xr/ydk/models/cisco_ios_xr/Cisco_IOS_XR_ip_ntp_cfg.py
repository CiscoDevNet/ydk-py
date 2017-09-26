""" Cisco_IOS_XR_ip_ntp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-ntp package configuration.

This module contains definitions
for the following management objects\:
  ntp\: NTP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
    _revision = '2017-05-01'

    def __init__(self):
        super(Ntp, self).__init__()
        self._top_entity = None

        self.yang_name = "ntp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-ntp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"access-group-tables" : ("access_group_tables", Ntp.AccessGroupTables), "authentication" : ("authentication", Ntp.Authentication), "dscp-ipv4" : ("dscp_ipv4", Ntp.DscpIpv4), "dscp-ipv6" : ("dscp_ipv6", Ntp.DscpIpv6), "interface-tables" : ("interface_tables", Ntp.InterfaceTables), "passive" : ("passive", Ntp.Passive), "peer-vrfs" : ("peer_vrfs", Ntp.PeerVrfs), "sources" : ("sources", Ntp.Sources)}
        self._child_list_classes = {}
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
        self._segment_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp"

    def __setattr__(self, name, value):
        self._perform_setattr(Ntp, ['broadcast_delay', 'log_internal_sync', 'master', 'max_associations', 'update_calendar'], name, value)


    class AccessGroupTables(Entity):
        """
        Control NTP access
        
        .. attribute:: access_group_table
        
        	Control NTP access
        	**type**\: list of    :py:class:`AccessGroupTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.AccessGroupTables.AccessGroupTable>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ntp.AccessGroupTables, self).__init__()

            self.yang_name = "access-group-tables"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"access-group-table" : ("access_group_table", Ntp.AccessGroupTables.AccessGroupTable)}

            self.access_group_table = YList(self)
            self._segment_path = lambda: "access-group-tables"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.AccessGroupTables, [], name, value)


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
            _revision = '2017-05-01'

            def __init__(self):
                super(Ntp.AccessGroupTables.AccessGroupTable, self).__init__()

                self.yang_name = "access-group-table"
                self.yang_parent_name = "access-group-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"access-group-af-table" : ("access_group_af_table", Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable)}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.access_group_af_table = YList(self)
                self._segment_path = lambda: "access-group-table" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/access-group-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.AccessGroupTables.AccessGroupTable, ['vrf_name'], name, value)


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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable, self).__init__()

                    self.yang_name = "access-group-af-table"
                    self.yang_parent_name = "access-group-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"access-group" : ("access_group", Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup)}

                    self.af = YLeaf(YType.enumeration, "af")

                    self.access_group = YList(self)
                    self._segment_path = lambda: "access-group-af-table" + "[af='" + self.af.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable, ['af'], name, value)


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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup, self).__init__()

                        self.yang_name = "access-group"
                        self.yang_parent_name = "access-group-af-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.access_group_type = YLeaf(YType.enumeration, "access-group-type")

                        self.access_list_name = YLeaf(YType.str, "access-list-name")
                        self._segment_path = lambda: "access-group" + "[access-group-type='" + self.access_group_type.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup, ['access_group_type', 'access_list_name'], name, value)


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
        _revision = '2017-05-01'

        def __init__(self):
            super(Ntp.Authentication, self).__init__()

            self.yang_name = "authentication"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"keies" : ("keies", Ntp.Authentication.Keies), "trusted-keies" : ("trusted_keies", Ntp.Authentication.TrustedKeies)}
            self._child_list_classes = {}

            self.enable = YLeaf(YType.empty, "enable")

            self.keies = Ntp.Authentication.Keies()
            self.keies.parent = self
            self._children_name_map["keies"] = "keies"
            self._children_yang_names.add("keies")

            self.trusted_keies = Ntp.Authentication.TrustedKeies()
            self.trusted_keies.parent = self
            self._children_name_map["trusted_keies"] = "trusted-keies"
            self._children_yang_names.add("trusted-keies")
            self._segment_path = lambda: "authentication"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Authentication, ['enable'], name, value)


        class Keies(Entity):
            """
            Authentication Key Table
            
            .. attribute:: key
            
            	Authentication key for trusted time sources
            	**type**\: list of    :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.Keies.Key>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ntp.Authentication.Keies, self).__init__()

                self.yang_name = "keies"
                self.yang_parent_name = "authentication"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"key" : ("key", Ntp.Authentication.Keies.Key)}

                self.key = YList(self)
                self._segment_path = lambda: "keies"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.Authentication.Keies, [], name, value)


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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ntp.Authentication.Keies.Key, self).__init__()

                    self.yang_name = "key"
                    self.yang_parent_name = "keies"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.key_number = YLeaf(YType.uint32, "key-number")

                    self.authentication_key = YLeaf(YType.str, "authentication-key")
                    self._segment_path = lambda: "key" + "[key-number='" + self.key_number.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/keies/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.Authentication.Keies.Key, ['key_number', 'authentication_key'], name, value)


        class TrustedKeies(Entity):
            """
            Key numbers for trusted time sources
            
            .. attribute:: trusted_key
            
            	Configure NTP trusted key
            	**type**\: list of    :py:class:`TrustedKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Authentication.TrustedKeies.TrustedKey>`
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ntp.Authentication.TrustedKeies, self).__init__()

                self.yang_name = "trusted-keies"
                self.yang_parent_name = "authentication"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"trusted-key" : ("trusted_key", Ntp.Authentication.TrustedKeies.TrustedKey)}

                self.trusted_key = YList(self)
                self._segment_path = lambda: "trusted-keies"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.Authentication.TrustedKeies, [], name, value)


            class TrustedKey(Entity):
                """
                Configure NTP trusted key
                
                .. attribute:: key_number  <key>
                
                	Key number
                	**type**\:  int
                
                	**range:** 1..65535
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ntp.Authentication.TrustedKeies.TrustedKey, self).__init__()

                    self.yang_name = "trusted-key"
                    self.yang_parent_name = "trusted-keies"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.key_number = YLeaf(YType.uint32, "key-number")
                    self._segment_path = lambda: "trusted-key" + "[key-number='" + self.key_number.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/authentication/trusted-keies/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.Authentication.TrustedKeies.TrustedKey, ['key_number'], name, value)


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
        _revision = '2017-05-01'

        def __init__(self):
            super(Ntp.DscpIpv4, self).__init__()

            self.yang_name = "dscp-ipv4"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.dscp_or_precedence_value = YLeaf(YType.uint32, "dscp-or-precedence-value")

            self.mode = YLeaf(YType.enumeration, "mode")
            self._segment_path = lambda: "dscp-ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.DscpIpv4, ['dscp_or_precedence_value', 'mode'], name, value)


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
        _revision = '2017-05-01'

        def __init__(self):
            super(Ntp.DscpIpv6, self).__init__()

            self.yang_name = "dscp-ipv6"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.dscp_or_precedence_value = YLeaf(YType.uint32, "dscp-or-precedence-value")

            self.mode = YLeaf(YType.enumeration, "mode")
            self._segment_path = lambda: "dscp-ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.DscpIpv6, ['dscp_or_precedence_value', 'mode'], name, value)


    class InterfaceTables(Entity):
        """
        NTP per interface configuration
        
        .. attribute:: interface_table
        
        	NTP per interface configuration
        	**type**\: list of    :py:class:`InterfaceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ntp.InterfaceTables, self).__init__()

            self.yang_name = "interface-tables"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface-table" : ("interface_table", Ntp.InterfaceTables.InterfaceTable)}

            self.interface_table = YList(self)
            self._segment_path = lambda: "interface-tables"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.InterfaceTables, [], name, value)


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
            _revision = '2017-05-01'

            def __init__(self):
                super(Ntp.InterfaceTables.InterfaceTable, self).__init__()

                self.yang_name = "interface-table"
                self.yang_parent_name = "interface-tables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", Ntp.InterfaceTables.InterfaceTable.Interface)}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.interface = YList(self)
                self._segment_path = lambda: "interface-table" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/interface-tables/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.InterfaceTables.InterfaceTable, ['vrf_name'], name, value)


            class Interface(Entity):
                """
                Name of the interface
                
                .. attribute:: interface  <key>
                
                	interface
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ntp.InterfaceTables.InterfaceTable.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interface-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"interface-broadcast" : ("interface_broadcast", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast), "interface-multicast" : ("interface_multicast", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "interface" + "[interface='" + self.interface.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface, ['interface', 'disable'], name, value)


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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast, self).__init__()

                        self.yang_name = "interface-broadcast"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"broadcast" : ("broadcast", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast)}
                        self._child_list_classes = {}

                        self.broadcast_client = YLeaf(YType.empty, "broadcast-client")

                        self.broadcast = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast()
                        self.broadcast.parent = self
                        self._children_name_map["broadcast"] = "broadcast"
                        self._children_yang_names.add("broadcast")
                        self._segment_path = lambda: "interface-broadcast"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast, ['broadcast_client'], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast, self).__init__()

                            self.yang_name = "broadcast"
                            self.yang_parent_name = "interface-broadcast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.authentication_key = YLeaf(YType.uint32, "authentication-key")

                            self.ntp_version = YLeaf(YType.uint32, "ntp-version")
                            self._segment_path = lambda: "broadcast"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast, ['address', 'authentication_key', 'ntp_version'], name, value)


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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast, self).__init__()

                        self.yang_name = "interface-multicast"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"multicast-clients" : ("multicast_clients", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients), "multicast-servers" : ("multicast_servers", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers)}
                        self._child_list_classes = {}

                        self.multicast_clients = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients()
                        self.multicast_clients.parent = self
                        self._children_name_map["multicast_clients"] = "multicast-clients"
                        self._children_yang_names.add("multicast-clients")

                        self.multicast_servers = Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers()
                        self.multicast_servers.parent = self
                        self._children_name_map["multicast_servers"] = "multicast-servers"
                        self._children_yang_names.add("multicast-servers")
                        self._segment_path = lambda: "interface-multicast"


                    class MulticastClients(Entity):
                        """
                        Configures multicast client peers
                        
                        .. attribute:: multicast_client
                        
                        	Listen to NTP multicasts
                        	**type**\: list of    :py:class:`MulticastClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient>`
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients, self).__init__()

                            self.yang_name = "multicast-clients"
                            self.yang_parent_name = "interface-multicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"multicast-client" : ("multicast_client", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient)}

                            self.multicast_client = YList(self)
                            self._segment_path = lambda: "multicast-clients"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients, [], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient, self).__init__()

                                self.yang_name = "multicast-client"
                                self.yang_parent_name = "multicast-clients"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip_address = YLeaf(YType.str, "ip-address")
                                self._segment_path = lambda: "multicast-client" + "[ip-address='" + self.ip_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient, ['ip_address'], name, value)


                    class MulticastServers(Entity):
                        """
                        Configures multicast server peers
                        
                        .. attribute:: multicast_server
                        
                        	Configure NTP multicast group server peer
                        	**type**\: list of    :py:class:`MulticastServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer>`
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers, self).__init__()

                            self.yang_name = "multicast-servers"
                            self.yang_parent_name = "interface-multicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"multicast-server" : ("multicast_server", Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer)}

                            self.multicast_server = YList(self)
                            self._segment_path = lambda: "multicast-servers"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers, [], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer, self).__init__()

                                self.yang_name = "multicast-server"
                                self.yang_parent_name = "multicast-servers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip_address = YLeaf(YType.str, "ip-address")

                                self.authentication_key = YLeaf(YType.uint32, "authentication-key")

                                self.ttl = YLeaf(YType.uint32, "ttl")

                                self.version = YLeaf(YType.uint32, "version")
                                self._segment_path = lambda: "multicast-server" + "[ip-address='" + self.ip_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer, ['ip_address', 'authentication_key', 'ttl', 'version'], name, value)


    class Passive(Entity):
        """
        Configure NTP passive associations
        
        .. attribute:: enable
        
        	Enable NTP Passive associations
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ntp.Passive, self).__init__()

            self.yang_name = "passive"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.enable = YLeaf(YType.empty, "enable")
            self._segment_path = lambda: "passive"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Passive, ['enable'], name, value)


    class PeerVrfs(Entity):
        """
        Configures NTP Peers or Servers
        
        .. attribute:: peer_vrf
        
        	Configures NTP Peers or Servers for a single VRF. The 'default' must also be specified for default VRF
        	**type**\: list of    :py:class:`PeerVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ntp.PeerVrfs, self).__init__()

            self.yang_name = "peer-vrfs"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"peer-vrf" : ("peer_vrf", Ntp.PeerVrfs.PeerVrf)}

            self.peer_vrf = YList(self)
            self._segment_path = lambda: "peer-vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.PeerVrfs, [], name, value)


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
            _revision = '2017-05-01'

            def __init__(self):
                super(Ntp.PeerVrfs.PeerVrf, self).__init__()

                self.yang_name = "peer-vrf"
                self.yang_parent_name = "peer-vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"peer-ipv4s" : ("peer_ipv4s", Ntp.PeerVrfs.PeerVrf.PeerIpv4S), "peer-ipv6s" : ("peer_ipv6s", Ntp.PeerVrfs.PeerVrf.PeerIpv6S)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.peer_ipv4s = Ntp.PeerVrfs.PeerVrf.PeerIpv4S()
                self.peer_ipv4s.parent = self
                self._children_name_map["peer_ipv4s"] = "peer-ipv4s"
                self._children_yang_names.add("peer-ipv4s")

                self.peer_ipv6s = Ntp.PeerVrfs.PeerVrf.PeerIpv6S()
                self.peer_ipv6s.parent = self
                self._children_name_map["peer_ipv6s"] = "peer-ipv6s"
                self._children_yang_names.add("peer-ipv6s")
                self._segment_path = lambda: "peer-vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/peer-vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.PeerVrfs.PeerVrf, ['vrf_name'], name, value)


            class PeerIpv4S(Entity):
                """
                Configures IPv4 NTP Peers or Servers
                
                .. attribute:: peer_ipv4
                
                	Configure an IPv4 NTP server or peer
                	**type**\: list of    :py:class:`PeerIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S, self).__init__()

                    self.yang_name = "peer-ipv4s"
                    self.yang_parent_name = "peer-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"peer-ipv4" : ("peer_ipv4", Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4)}

                    self.peer_ipv4 = YList(self)
                    self._segment_path = lambda: "peer-ipv4s"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv4S, [], name, value)


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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4, self).__init__()

                        self.yang_name = "peer-ipv4"
                        self.yang_parent_name = "peer-ipv4s"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"peer-type-ipv4" : ("peer_type_ipv4", Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4)}

                        self.address_ipv4 = YLeaf(YType.str, "address-ipv4")

                        self.peer_type_ipv4 = YList(self)
                        self._segment_path = lambda: "peer-ipv4" + "[address-ipv4='" + self.address_ipv4.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4, ['address_ipv4'], name, value)


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
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4, self).__init__()

                            self.yang_name = "peer-type-ipv4"
                            self.yang_parent_name = "peer-ipv4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.peer_type = YLeaf(YType.enumeration, "peer-type")

                            self.authentication_key = YLeaf(YType.uint32, "authentication-key")

                            self.burst = YLeaf(YType.empty, "burst")

                            self.iburst = YLeaf(YType.empty, "iburst")

                            self.max_poll = YLeaf(YType.uint32, "max-poll")

                            self.min_poll = YLeaf(YType.uint32, "min-poll")

                            self.ntp_version = YLeaf(YType.uint32, "ntp-version")

                            self.preferred_peer = YLeaf(YType.empty, "preferred-peer")

                            self.source_interface = YLeaf(YType.str, "source-interface")
                            self._segment_path = lambda: "peer-type-ipv4" + "[peer-type='" + self.peer_type.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4, ['peer_type', 'authentication_key', 'burst', 'iburst', 'max_poll', 'min_poll', 'ntp_version', 'preferred_peer', 'source_interface'], name, value)


            class PeerIpv6S(Entity):
                """
                Configuration NTP Peers or Servers of IPV6
                
                .. attribute:: peer_ipv6
                
                	Configure a NTP server or peer
                	**type**\: list of    :py:class:`PeerIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6>`
                
                

                """

                _prefix = 'ip-ntp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S, self).__init__()

                    self.yang_name = "peer-ipv6s"
                    self.yang_parent_name = "peer-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"peer-ipv6" : ("peer_ipv6", Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6)}

                    self.peer_ipv6 = YList(self)
                    self._segment_path = lambda: "peer-ipv6s"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv6S, [], name, value)


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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6, self).__init__()

                        self.yang_name = "peer-ipv6"
                        self.yang_parent_name = "peer-ipv6s"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"peer-type-ipv6" : ("peer_type_ipv6", Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6)}

                        self.address_ipv6 = YLeaf(YType.str, "address-ipv6")

                        self.peer_type_ipv6 = YList(self)
                        self._segment_path = lambda: "peer-ipv6" + "[address-ipv6='" + self.address_ipv6.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6, ['address_ipv6'], name, value)


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
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        

                        """

                        _prefix = 'ip-ntp-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6, self).__init__()

                            self.yang_name = "peer-type-ipv6"
                            self.yang_parent_name = "peer-ipv6"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "peer-type-ipv6" + "[peer-type='" + self.peer_type.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6, ['peer_type', 'address_ipv6', 'authentication_key', 'burst', 'iburst', 'max_poll', 'min_poll', 'ntp_version', 'preferred_peer', 'source_interface'], name, value)


    class Sources(Entity):
        """
        Configure  NTP source interface
        
        .. attribute:: source
        
        	Configure  NTP source interface
        	**type**\: list of    :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg.Ntp.Sources.Source>`
        
        

        """

        _prefix = 'ip-ntp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ntp.Sources, self).__init__()

            self.yang_name = "sources"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"source" : ("source", Ntp.Sources.Source)}

            self.source = YList(self)
            self._segment_path = lambda: "sources"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Sources, [], name, value)


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
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ip-ntp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ntp.Sources.Source, self).__init__()

                self.yang_name = "source"
                self.yang_parent_name = "sources"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.source_interface = YLeaf(YType.str, "source-interface")
                self._segment_path = lambda: "source" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-cfg:ntp/sources/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.Sources.Source, ['vrf_name', 'source_interface'], name, value)

    def clone_ptr(self):
        self._top_entity = Ntp()
        return self._top_entity

