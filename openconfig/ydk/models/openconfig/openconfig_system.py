""" openconfig_system 

Model for managing system\-wide services and functions on
network devices.

Portions of this code were derived from IETF RFC 7317.
Please reproduce this note if possible.

IETF code is subject to the following copyright and license\:
Copyright (c) IETF Trust and the persons identified as authors of
the code.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, is permitted pursuant to, and subject to the license
terms contained in, the Simplified BSD License set forth in
Section 4.c of the IETF Trust's Legal Provisions Relating
to IETF Documents (http\://trustee.ietf.org/license\-info).

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class NTPAUTHTYPE(Identity):
    """
    Base identity for encryption schemes supported for NTP
    authentication keys
    
    

    """

    _prefix = 'oc-sys'
    _revision = '2018-07-17'

    def __init__(self, ns="http://openconfig.net/yang/system", pref="openconfig-system", tag="openconfig-system:NTP_AUTH_TYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(NTPAUTHTYPE, self).__init__(ns, pref, tag)



class System(_Entity_):
    """
    Enclosing container for system\-related configuration and
    operational state data
    
    .. attribute:: config
    
    	Global configuration data for the system
    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Config>`
    
    .. attribute:: state
    
    	Global operational state data for the system
    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.State>`
    
    	**config**\: False
    
    .. attribute:: clock
    
    	Top\-level container for clock configuration data
    	**type**\:  :py:class:`Clock <ydk.models.openconfig.openconfig_system.System.Clock>`
    
    .. attribute:: dns
    
    	Enclosing container for DNS resolver data
    	**type**\:  :py:class:`Dns <ydk.models.openconfig.openconfig_system.System.Dns>`
    
    .. attribute:: ntp
    
    	Top\-level container for NTP configuration and state
    	**type**\:  :py:class:`Ntp <ydk.models.openconfig.openconfig_system.System.Ntp>`
    
    .. attribute:: grpc_server
    
    	Top\-level container for the gRPC server
    	**type**\:  :py:class:`GrpcServer <ydk.models.openconfig.openconfig_system.System.GrpcServer>`
    
    .. attribute:: ssh_server
    
    	Top\-level container for ssh server
    	**type**\:  :py:class:`SshServer <ydk.models.openconfig.openconfig_system.System.SshServer>`
    
    .. attribute:: telnet_server
    
    	Top\-level container for telnet terminal servers
    	**type**\:  :py:class:`TelnetServer <ydk.models.openconfig.openconfig_system.System.TelnetServer>`
    
    .. attribute:: logging
    
    	Top\-level container for data related to logging / syslog
    	**type**\:  :py:class:`Logging <ydk.models.openconfig.openconfig_system.System.Logging>`
    
    .. attribute:: aaa
    
    	Top\-level container for AAA services
    	**type**\:  :py:class:`Aaa <ydk.models.openconfig.openconfig_system.System.Aaa>`
    
    .. attribute:: memory
    
    	Top\-level container for system memory data
    	**type**\:  :py:class:`Memory <ydk.models.openconfig.openconfig_system.System.Memory>`
    
    .. attribute:: cpus
    
    	Enclosing container for the list of CPU cores on the system
    	**type**\:  :py:class:`Cpus <ydk.models.openconfig.openconfig_system.System.Cpus>`
    
    	**config**\: False
    
    .. attribute:: processes
    
    	Parameters related to all monitored processes
    	**type**\:  :py:class:`Processes <ydk.models.openconfig.openconfig_system.System.Processes>`
    
    .. attribute:: alarms
    
    	Top\-level container for device alarms
    	**type**\:  :py:class:`Alarms <ydk.models.openconfig.openconfig_system.System.Alarms>`
    
    	**config**\: False
    
    

    """

    _prefix = 'oc-sys'
    _revision = '2018-07-17'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(System, self).__init__()
        self._top_entity = None

        self.yang_name = "system"
        self.yang_parent_name = "openconfig-system"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("config", ("config", System.Config)), ("state", ("state", System.State)), ("clock", ("clock", System.Clock)), ("dns", ("dns", System.Dns)), ("ntp", ("ntp", System.Ntp)), ("grpc-server", ("grpc_server", System.GrpcServer)), ("ssh-server", ("ssh_server", System.SshServer)), ("telnet-server", ("telnet_server", System.TelnetServer)), ("logging", ("logging", System.Logging)), ("aaa", ("aaa", System.Aaa)), ("memory", ("memory", System.Memory)), ("cpus", ("cpus", System.Cpus)), ("processes", ("processes", System.Processes)), ("alarms", ("alarms", System.Alarms))])
        self._leafs = OrderedDict()

        self.config = System.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"

        self.state = System.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"

        self.clock = System.Clock()
        self.clock.parent = self
        self._children_name_map["clock"] = "clock"

        self.dns = System.Dns()
        self.dns.parent = self
        self._children_name_map["dns"] = "dns"

        self.ntp = System.Ntp()
        self.ntp.parent = self
        self._children_name_map["ntp"] = "ntp"

        self.grpc_server = System.GrpcServer()
        self.grpc_server.parent = self
        self._children_name_map["grpc_server"] = "grpc-server"

        self.ssh_server = System.SshServer()
        self.ssh_server.parent = self
        self._children_name_map["ssh_server"] = "ssh-server"

        self.telnet_server = System.TelnetServer()
        self.telnet_server.parent = self
        self._children_name_map["telnet_server"] = "telnet-server"

        self.logging = System.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"

        self.aaa = System.Aaa()
        self.aaa.parent = self
        self._children_name_map["aaa"] = "aaa"

        self.memory = System.Memory()
        self.memory.parent = self
        self._children_name_map["memory"] = "memory"

        self.cpus = System.Cpus()
        self.cpus.parent = self
        self._children_name_map["cpus"] = "cpus"

        self.processes = System.Processes()
        self.processes.parent = self
        self._children_name_map["processes"] = "processes"

        self.alarms = System.Alarms()
        self.alarms.parent = self
        self._children_name_map["alarms"] = "alarms"
        self._segment_path = lambda: "openconfig-system:system"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(System, [], name, value)


    class Config(_Entity_):
        """
        Global configuration data for the system
        
        .. attribute:: hostname
        
        	The hostname of the device \-\- should be a single domain label, without the domain
        	**type**\: str
        
        	**length:** 1..253
        
        .. attribute:: domain_name
        
        	Specifies the domain name used to form fully qualified name for unqualified hostnames
        	**type**\: str
        
        	**length:** 1..253
        
        .. attribute:: login_banner
        
        	The console login message displayed before the login prompt, i.e., before a user logs into the system
        	**type**\: str
        
        .. attribute:: motd_banner
        
        	The console message displayed after a user logs into the system.  They system may append additional standard information such as the current system date and time, uptime, last login timestamp, etc
        	**type**\: str
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('hostname', (YLeaf(YType.str, 'hostname'), ['str'])),
                ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                ('login_banner', (YLeaf(YType.str, 'login-banner'), ['str'])),
                ('motd_banner', (YLeaf(YType.str, 'motd-banner'), ['str'])),
            ])
            self.hostname = None
            self.domain_name = None
            self.login_banner = None
            self.motd_banner = None
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.Config, ['hostname', 'domain_name', 'login_banner', 'motd_banner'], name, value)



    class State(_Entity_):
        """
        Global operational state data for the system
        
        .. attribute:: hostname
        
        	The hostname of the device \-\- should be a single domain label, without the domain
        	**type**\: str
        
        	**length:** 1..253
        
        	**config**\: False
        
        .. attribute:: domain_name
        
        	Specifies the domain name used to form fully qualified name for unqualified hostnames
        	**type**\: str
        
        	**length:** 1..253
        
        	**config**\: False
        
        .. attribute:: login_banner
        
        	The console login message displayed before the login prompt, i.e., before a user logs into the system
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: motd_banner
        
        	The console message displayed after a user logs into the system.  They system may append additional standard information such as the current system date and time, uptime, last login timestamp, etc
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: current_datetime
        
        	The current system date and time
        	**type**\: str
        
        	**pattern:** ^[0\-9]{4}\\\-[0\-9]{2}\\\-[0\-9]{2}T[0\-9]{2}\:[0\-9]{2}\:[0\-9]{2}(\\.[0\-9]+)?Z[+\-][0\-9]{2}\:[0\-9]{2}$
        
        	**config**\: False
        
        .. attribute:: boot_time
        
        	This timestamp indicates the time that the system was last restarted.  The value is the timestamp in seconds relative to the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('hostname', (YLeaf(YType.str, 'hostname'), ['str'])),
                ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                ('login_banner', (YLeaf(YType.str, 'login-banner'), ['str'])),
                ('motd_banner', (YLeaf(YType.str, 'motd-banner'), ['str'])),
                ('current_datetime', (YLeaf(YType.str, 'current-datetime'), ['str'])),
                ('boot_time', (YLeaf(YType.uint64, 'boot-time'), ['int'])),
            ])
            self.hostname = None
            self.domain_name = None
            self.login_banner = None
            self.motd_banner = None
            self.current_datetime = None
            self.boot_time = None
            self._segment_path = lambda: "state"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.State, ['hostname', 'domain_name', 'login_banner', 'motd_banner', 'current_datetime', 'boot_time'], name, value)



    class Clock(_Entity_):
        """
        Top\-level container for clock configuration data
        
        .. attribute:: config
        
        	Configuration data for system clock
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Clock.Config>`
        
        .. attribute:: state
        
        	Operational state data for system clock
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Clock.State>`
        
        	**config**\: False
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.Clock, self).__init__()

            self.yang_name = "clock"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("config", ("config", System.Clock.Config)), ("state", ("state", System.Clock.State))])
            self._leafs = OrderedDict()

            self.config = System.Clock.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.state = System.Clock.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"
            self._segment_path = lambda: "clock"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.Clock, [], name, value)


        class Config(_Entity_):
            """
            Configuration data for system clock
            
            .. attribute:: timezone_name
            
            	The TZ database name to use for the system, such as 'Europe/Stockholm'
            	**type**\: str
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Clock.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('timezone_name', (YLeaf(YType.str, 'timezone-name'), ['str'])),
                ])
                self.timezone_name = None
                self._segment_path = lambda: "config"
                self._absolute_path = lambda: "openconfig-system:system/clock/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Clock.Config, ['timezone_name'], name, value)



        class State(_Entity_):
            """
            Operational state data for system clock
            
            .. attribute:: timezone_name
            
            	The TZ database name to use for the system, such as 'Europe/Stockholm'
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Clock.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('timezone_name', (YLeaf(YType.str, 'timezone-name'), ['str'])),
                ])
                self.timezone_name = None
                self._segment_path = lambda: "state"
                self._absolute_path = lambda: "openconfig-system:system/clock/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Clock.State, ['timezone_name'], name, value)




    class Dns(_Entity_):
        """
        Enclosing container for DNS resolver data
        
        .. attribute:: config
        
        	Configuration data for the DNS resolver
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Dns.Config>`
        
        .. attribute:: state
        
        	Operational state data for the DNS resolver
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Dns.State>`
        
        	**config**\: False
        
        .. attribute:: servers
        
        	Enclosing container for DNS resolver list
        	**type**\:  :py:class:`Servers <ydk.models.openconfig.openconfig_system.System.Dns.Servers>`
        
        .. attribute:: host_entries
        
        	Enclosing container for list of static host entries
        	**type**\:  :py:class:`HostEntries <ydk.models.openconfig.openconfig_system.System.Dns.HostEntries>`
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.Dns, self).__init__()

            self.yang_name = "dns"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("config", ("config", System.Dns.Config)), ("state", ("state", System.Dns.State)), ("servers", ("servers", System.Dns.Servers)), ("host-entries", ("host_entries", System.Dns.HostEntries))])
            self._leafs = OrderedDict()

            self.config = System.Dns.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.state = System.Dns.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"

            self.servers = System.Dns.Servers()
            self.servers.parent = self
            self._children_name_map["servers"] = "servers"

            self.host_entries = System.Dns.HostEntries()
            self.host_entries.parent = self
            self._children_name_map["host_entries"] = "host-entries"
            self._segment_path = lambda: "dns"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.Dns, [], name, value)


        class Config(_Entity_):
            """
            Configuration data for the DNS resolver
            
            .. attribute:: search
            
            	An ordered list of domains to search when resolving a host name
            	**type**\: list of str
            
            	**length:** 1..253
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Dns.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "dns"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('search', (YLeafList(YType.str, 'search'), ['str'])),
                ])
                self.search = []
                self._segment_path = lambda: "config"
                self._absolute_path = lambda: "openconfig-system:system/dns/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Dns.Config, ['search'], name, value)



        class State(_Entity_):
            """
            Operational state data for the DNS resolver
            
            .. attribute:: search
            
            	An ordered list of domains to search when resolving a host name
            	**type**\: list of str
            
            	**length:** 1..253
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Dns.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "dns"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('search', (YLeafList(YType.str, 'search'), ['str'])),
                ])
                self.search = []
                self._segment_path = lambda: "state"
                self._absolute_path = lambda: "openconfig-system:system/dns/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Dns.State, ['search'], name, value)



        class Servers(_Entity_):
            """
            Enclosing container for DNS resolver list
            
            .. attribute:: server
            
            	List of the DNS servers that the resolver should query.  When the resolver is invoked by a calling application, it sends the query to the first name server in this list.  If no response has been received within 'timeout' seconds, the resolver continues with the next server in the list. If no response is received from any server, the resolver continues with the first server again.  When the resolver has traversed the list 'attempts' times without receiving any response, it gives up and returns an error to the calling application.  Implementations MAY limit the number of entries in this list
            	**type**\: list of  		 :py:class:`Server <ydk.models.openconfig.openconfig_system.System.Dns.Servers.Server>`
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Dns.Servers, self).__init__()

                self.yang_name = "servers"
                self.yang_parent_name = "dns"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("server", ("server", System.Dns.Servers.Server))])
                self._leafs = OrderedDict()

                self.server = YList(self)
                self._segment_path = lambda: "servers"
                self._absolute_path = lambda: "openconfig-system:system/dns/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Dns.Servers, [], name, value)


            class Server(_Entity_):
                """
                List of the DNS servers that the resolver should query.
                
                When the resolver is invoked by a calling application, it
                sends the query to the first name server in this list.  If
                no response has been received within 'timeout' seconds,
                the resolver continues with the next server in the list.
                If no response is received from any server, the resolver
                continues with the first server again.  When the resolver
                has traversed the list 'attempts' times without receiving
                any response, it gives up and returns an error to the
                calling application.
                
                Implementations MAY limit the number of entries in this
                list.
                
                .. attribute:: address  (key)
                
                	References the configured address of the DNS server
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                
                	**refers to**\:  :py:class:`address <ydk.models.openconfig.openconfig_system.System.Dns.Servers.Server.Config>`
                
                .. attribute:: config
                
                	Configuration data for each DNS resolver
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Dns.Servers.Server.Config>`
                
                .. attribute:: state
                
                	Operational state data for each DNS resolver
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Dns.Servers.Server.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Dns.Servers.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "servers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['address']
                    self._child_classes = OrderedDict([("config", ("config", System.Dns.Servers.Server.Config)), ("state", ("state", System.Dns.Servers.Server.State))])
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                    ])
                    self.address = None

                    self.config = System.Dns.Servers.Server.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = System.Dns.Servers.Server.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "server" + "[address='" + str(self.address) + "']"
                    self._absolute_path = lambda: "openconfig-system:system/dns/servers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Dns.Servers.Server, ['address'], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for each DNS resolver
                    
                    .. attribute:: address
                    
                    	The address of the DNS server, can be either IPv4 or IPv6
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                    
                    .. attribute:: port
                    
                    	The port number of the DNS server
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 53
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Dns.Servers.Server.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                            ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                        ])
                        self.address = None
                        self.port = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Dns.Servers.Server.Config, ['address', 'port'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for each DNS resolver
                    
                    .. attribute:: address
                    
                    	The address of the DNS server, can be either IPv4 or IPv6
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                    
                    	**config**\: False
                    
                    .. attribute:: port
                    
                    	The port number of the DNS server
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    	**default value**\: 53
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Dns.Servers.Server.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                            ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                        ])
                        self.address = None
                        self.port = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Dns.Servers.Server.State, ['address', 'port'], name, value)





        class HostEntries(_Entity_):
            """
            Enclosing container for list of static host entries
            
            .. attribute:: host_entry
            
            	List of static host entries
            	**type**\: list of  		 :py:class:`HostEntry <ydk.models.openconfig.openconfig_system.System.Dns.HostEntries.HostEntry>`
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Dns.HostEntries, self).__init__()

                self.yang_name = "host-entries"
                self.yang_parent_name = "dns"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("host-entry", ("host_entry", System.Dns.HostEntries.HostEntry))])
                self._leafs = OrderedDict()

                self.host_entry = YList(self)
                self._segment_path = lambda: "host-entries"
                self._absolute_path = lambda: "openconfig-system:system/dns/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Dns.HostEntries, [], name, value)


            class HostEntry(_Entity_):
                """
                List of static host entries
                
                .. attribute:: hostname  (key)
                
                	Reference to the hostname list key
                	**type**\: str
                
                	**refers to**\:  :py:class:`hostname <ydk.models.openconfig.openconfig_system.System.Dns.HostEntries.HostEntry.Config>`
                
                .. attribute:: config
                
                	Configuration data for static host entries
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Dns.HostEntries.HostEntry.Config>`
                
                .. attribute:: state
                
                	Operational state data for static host entries
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Dns.HostEntries.HostEntry.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Dns.HostEntries.HostEntry, self).__init__()

                    self.yang_name = "host-entry"
                    self.yang_parent_name = "host-entries"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['hostname']
                    self._child_classes = OrderedDict([("config", ("config", System.Dns.HostEntries.HostEntry.Config)), ("state", ("state", System.Dns.HostEntries.HostEntry.State))])
                    self._leafs = OrderedDict([
                        ('hostname', (YLeaf(YType.str, 'hostname'), ['str'])),
                    ])
                    self.hostname = None

                    self.config = System.Dns.HostEntries.HostEntry.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = System.Dns.HostEntries.HostEntry.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "host-entry" + "[hostname='" + str(self.hostname) + "']"
                    self._absolute_path = lambda: "openconfig-system:system/dns/host-entries/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Dns.HostEntries.HostEntry, ['hostname'], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for static host entries
                    
                    .. attribute:: hostname
                    
                    	Hostname for the static DNS entry
                    	**type**\: str
                    
                    .. attribute:: alias
                    
                    	Additional aliases for the hostname
                    	**type**\: list of str
                    
                    .. attribute:: ipv4_address
                    
                    	List of IPv4 addressses for the host entry
                    	**type**\: list of str
                    
                    	**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                    
                    .. attribute:: ipv6_address
                    
                    	List of IPv6 addresses for the host entry
                    	**type**\: list of str
                    
                    	**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Dns.HostEntries.HostEntry.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "host-entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('hostname', (YLeaf(YType.str, 'hostname'), ['str'])),
                            ('alias', (YLeafList(YType.str, 'alias'), ['str'])),
                            ('ipv4_address', (YLeafList(YType.str, 'ipv4-address'), ['str'])),
                            ('ipv6_address', (YLeafList(YType.str, 'ipv6-address'), ['str'])),
                        ])
                        self.hostname = None
                        self.alias = []
                        self.ipv4_address = []
                        self.ipv6_address = []
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Dns.HostEntries.HostEntry.Config, ['hostname', 'alias', 'ipv4_address', 'ipv6_address'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for static host entries
                    
                    .. attribute:: hostname
                    
                    	Hostname for the static DNS entry
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: alias
                    
                    	Additional aliases for the hostname
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_address
                    
                    	List of IPv4 addressses for the host entry
                    	**type**\: list of str
                    
                    	**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6_address
                    
                    	List of IPv6 addresses for the host entry
                    	**type**\: list of str
                    
                    	**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Dns.HostEntries.HostEntry.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "host-entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('hostname', (YLeaf(YType.str, 'hostname'), ['str'])),
                            ('alias', (YLeafList(YType.str, 'alias'), ['str'])),
                            ('ipv4_address', (YLeafList(YType.str, 'ipv4-address'), ['str'])),
                            ('ipv6_address', (YLeafList(YType.str, 'ipv6-address'), ['str'])),
                        ])
                        self.hostname = None
                        self.alias = []
                        self.ipv4_address = []
                        self.ipv6_address = []
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Dns.HostEntries.HostEntry.State, ['hostname', 'alias', 'ipv4_address', 'ipv6_address'], name, value)






    class Ntp(_Entity_):
        """
        Top\-level container for NTP configuration and state
        
        .. attribute:: config
        
        	Configuration data for NTP client
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Ntp.Config>`
        
        .. attribute:: state
        
        	Operational state data for NTP services
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Ntp.State>`
        
        	**config**\: False
        
        .. attribute:: ntp_keys
        
        	Enclosing container for list of NTP authentication keys
        	**type**\:  :py:class:`NtpKeys <ydk.models.openconfig.openconfig_system.System.Ntp.NtpKeys>`
        
        .. attribute:: servers
        
        	Enclosing container for the list of NTP servers
        	**type**\:  :py:class:`Servers <ydk.models.openconfig.openconfig_system.System.Ntp.Servers>`
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.Ntp, self).__init__()

            self.yang_name = "ntp"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("config", ("config", System.Ntp.Config)), ("state", ("state", System.Ntp.State)), ("ntp-keys", ("ntp_keys", System.Ntp.NtpKeys)), ("servers", ("servers", System.Ntp.Servers))])
            self._leafs = OrderedDict()

            self.config = System.Ntp.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.state = System.Ntp.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"

            self.ntp_keys = System.Ntp.NtpKeys()
            self.ntp_keys.parent = self
            self._children_name_map["ntp_keys"] = "ntp-keys"

            self.servers = System.Ntp.Servers()
            self.servers.parent = self
            self._children_name_map["servers"] = "servers"
            self._segment_path = lambda: "ntp"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.Ntp, [], name, value)


        class Config(_Entity_):
            """
            Configuration data for NTP client.
            
            .. attribute:: enabled
            
            	Enables the NTP protocol and indicates that the system should attempt to synchronize the system clock with an NTP server from the servers defined in the 'ntp/server' list
            	**type**\: bool
            
            	**default value**\: false
            
            .. attribute:: ntp_source_address
            
            	Source address to use on outgoing NTP packets
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
            
            		**type**\: str
            
            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
            
            .. attribute:: enable_ntp_auth
            
            	Enable or disable NTP authentication \-\- when enabled, the system will only use packets containing a trusted authentication key to synchronize the time
            	**type**\: bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Ntp.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "ntp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                    ('ntp_source_address', (YLeaf(YType.str, 'ntp-source-address'), ['str','str'])),
                    ('enable_ntp_auth', (YLeaf(YType.boolean, 'enable-ntp-auth'), ['bool'])),
                ])
                self.enabled = None
                self.ntp_source_address = None
                self.enable_ntp_auth = None
                self._segment_path = lambda: "config"
                self._absolute_path = lambda: "openconfig-system:system/ntp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Ntp.Config, ['enabled', 'ntp_source_address', 'enable_ntp_auth'], name, value)



        class State(_Entity_):
            """
            Operational state data for NTP services.
            
            .. attribute:: enabled
            
            	Enables the NTP protocol and indicates that the system should attempt to synchronize the system clock with an NTP server from the servers defined in the 'ntp/server' list
            	**type**\: bool
            
            	**config**\: False
            
            	**default value**\: false
            
            .. attribute:: ntp_source_address
            
            	Source address to use on outgoing NTP packets
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
            
            		**type**\: str
            
            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
            
            	**config**\: False
            
            .. attribute:: enable_ntp_auth
            
            	Enable or disable NTP authentication \-\- when enabled, the system will only use packets containing a trusted authentication key to synchronize the time
            	**type**\: bool
            
            	**config**\: False
            
            	**default value**\: false
            
            .. attribute:: auth_mismatch
            
            	Count of the number of NTP packets received that were not processed due to authentication mismatch
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Ntp.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "ntp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                    ('ntp_source_address', (YLeaf(YType.str, 'ntp-source-address'), ['str','str'])),
                    ('enable_ntp_auth', (YLeaf(YType.boolean, 'enable-ntp-auth'), ['bool'])),
                    ('auth_mismatch', (YLeaf(YType.uint64, 'auth-mismatch'), ['int'])),
                ])
                self.enabled = None
                self.ntp_source_address = None
                self.enable_ntp_auth = None
                self.auth_mismatch = None
                self._segment_path = lambda: "state"
                self._absolute_path = lambda: "openconfig-system:system/ntp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Ntp.State, ['enabled', 'ntp_source_address', 'enable_ntp_auth', 'auth_mismatch'], name, value)



        class NtpKeys(_Entity_):
            """
            Enclosing container for list of NTP authentication keys
            
            .. attribute:: ntp_key
            
            	List of NTP authentication keys
            	**type**\: list of  		 :py:class:`NtpKey <ydk.models.openconfig.openconfig_system.System.Ntp.NtpKeys.NtpKey>`
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Ntp.NtpKeys, self).__init__()

                self.yang_name = "ntp-keys"
                self.yang_parent_name = "ntp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ntp-key", ("ntp_key", System.Ntp.NtpKeys.NtpKey))])
                self._leafs = OrderedDict()

                self.ntp_key = YList(self)
                self._segment_path = lambda: "ntp-keys"
                self._absolute_path = lambda: "openconfig-system:system/ntp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Ntp.NtpKeys, [], name, value)


            class NtpKey(_Entity_):
                """
                List of NTP authentication keys
                
                .. attribute:: key_id  (key)
                
                	Reference to auth key\-id list key
                	**type**\: int
                
                	**range:** 0..65535
                
                	**refers to**\:  :py:class:`key_id <ydk.models.openconfig.openconfig_system.System.Ntp.NtpKeys.NtpKey.Config>`
                
                .. attribute:: config
                
                	Configuration data for NTP auth keys
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Ntp.NtpKeys.NtpKey.Config>`
                
                .. attribute:: state
                
                	Operational state data for NTP auth keys
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Ntp.NtpKeys.NtpKey.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Ntp.NtpKeys.NtpKey, self).__init__()

                    self.yang_name = "ntp-key"
                    self.yang_parent_name = "ntp-keys"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['key_id']
                    self._child_classes = OrderedDict([("config", ("config", System.Ntp.NtpKeys.NtpKey.Config)), ("state", ("state", System.Ntp.NtpKeys.NtpKey.State))])
                    self._leafs = OrderedDict([
                        ('key_id', (YLeaf(YType.str, 'key-id'), ['int'])),
                    ])
                    self.key_id = None

                    self.config = System.Ntp.NtpKeys.NtpKey.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = System.Ntp.NtpKeys.NtpKey.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "ntp-key" + "[key-id='" + str(self.key_id) + "']"
                    self._absolute_path = lambda: "openconfig-system:system/ntp/ntp-keys/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Ntp.NtpKeys.NtpKey, ['key_id'], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for NTP auth keys
                    
                    .. attribute:: key_id
                    
                    	Integer identifier used by the client and server to designate a secret key.  The client and server must use the same key id
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: key_type
                    
                    	Encryption type used for the NTP authentication key
                    	**type**\:  :py:class:`NTPAUTHTYPE <ydk.models.openconfig.openconfig_system.NTPAUTHTYPE>`
                    
                    .. attribute:: key_value
                    
                    	NTP authentication key value
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Ntp.NtpKeys.NtpKey.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ntp-key"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('key_id', (YLeaf(YType.uint16, 'key-id'), ['int'])),
                            ('key_type', (YLeaf(YType.identityref, 'key-type'), [('ydk.models.openconfig.openconfig_system', 'NTPAUTHTYPE')])),
                            ('key_value', (YLeaf(YType.str, 'key-value'), ['str'])),
                        ])
                        self.key_id = None
                        self.key_type = None
                        self.key_value = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Ntp.NtpKeys.NtpKey.Config, ['key_id', 'key_type', 'key_value'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for NTP auth keys
                    
                    .. attribute:: key_id
                    
                    	Integer identifier used by the client and server to designate a secret key.  The client and server must use the same key id
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: key_type
                    
                    	Encryption type used for the NTP authentication key
                    	**type**\:  :py:class:`NTPAUTHTYPE <ydk.models.openconfig.openconfig_system.NTPAUTHTYPE>`
                    
                    	**config**\: False
                    
                    .. attribute:: key_value
                    
                    	NTP authentication key value
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Ntp.NtpKeys.NtpKey.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ntp-key"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('key_id', (YLeaf(YType.uint16, 'key-id'), ['int'])),
                            ('key_type', (YLeaf(YType.identityref, 'key-type'), [('ydk.models.openconfig.openconfig_system', 'NTPAUTHTYPE')])),
                            ('key_value', (YLeaf(YType.str, 'key-value'), ['str'])),
                        ])
                        self.key_id = None
                        self.key_type = None
                        self.key_value = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Ntp.NtpKeys.NtpKey.State, ['key_id', 'key_type', 'key_value'], name, value)





        class Servers(_Entity_):
            """
            Enclosing container for the list of NTP servers
            
            .. attribute:: server
            
            	List of NTP servers to use for system clock synchronization.  If '/system/ntp/enabled' is 'true', then the system will attempt to contact and utilize the specified NTP servers
            	**type**\: list of  		 :py:class:`Server <ydk.models.openconfig.openconfig_system.System.Ntp.Servers.Server>`
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Ntp.Servers, self).__init__()

                self.yang_name = "servers"
                self.yang_parent_name = "ntp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("server", ("server", System.Ntp.Servers.Server))])
                self._leafs = OrderedDict()

                self.server = YList(self)
                self._segment_path = lambda: "servers"
                self._absolute_path = lambda: "openconfig-system:system/ntp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Ntp.Servers, [], name, value)


            class Server(_Entity_):
                """
                List of NTP servers to use for system clock
                synchronization.  If '/system/ntp/enabled'
                is 'true', then the system will attempt to
                contact and utilize the specified NTP servers.
                
                .. attribute:: address  (key)
                
                	References the configured address or hostname of the NTP server
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                
                		**type**\: str
                
                			**length:** 1..253
                
                	**refers to**\:  :py:class:`address <ydk.models.openconfig.openconfig_system.System.Ntp.Servers.Server.Config>`
                
                .. attribute:: config
                
                	Configuration data for an NTP server
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Ntp.Servers.Server.Config>`
                
                .. attribute:: state
                
                	Operational state data for an NTP server
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Ntp.Servers.Server.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Ntp.Servers.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "servers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['address']
                    self._child_classes = OrderedDict([("config", ("config", System.Ntp.Servers.Server.Config)), ("state", ("state", System.Ntp.Servers.Server.State))])
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                    ])
                    self.address = None

                    self.config = System.Ntp.Servers.Server.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = System.Ntp.Servers.Server.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "server" + "[address='" + str(self.address) + "']"
                    self._absolute_path = lambda: "openconfig-system:system/ntp/servers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Ntp.Servers.Server, ['address'], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for an NTP server.
                    
                    .. attribute:: address
                    
                    	The address or hostname of the NTP server
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                    
                    		**type**\: str
                    
                    			**length:** 1..253
                    
                    .. attribute:: port
                    
                    	The port number of the NTP server
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 123
                    
                    .. attribute:: version
                    
                    	Version number to put in outgoing NTP packets
                    	**type**\: int
                    
                    	**range:** 1..4
                    
                    	**default value**\: 4
                    
                    .. attribute:: association_type
                    
                    	The desired association type for this NTP server
                    	**type**\:  :py:class:`AssociationType <ydk.models.openconfig.openconfig_system.System.Ntp.Servers.Server.Config.AssociationType>`
                    
                    	**default value**\: SERVER
                    
                    .. attribute:: iburst
                    
                    	Indicates whether this server should enable burst synchronization or not
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: prefer
                    
                    	Indicates whether this server should be preferred or not
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Ntp.Servers.Server.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str','str','str'])),
                            ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                            ('version', (YLeaf(YType.uint8, 'version'), ['int'])),
                            ('association_type', (YLeaf(YType.enumeration, 'association-type'), [('ydk.models.openconfig.openconfig_system', 'System', 'Ntp.Servers.Server.Config.AssociationType')])),
                            ('iburst', (YLeaf(YType.boolean, 'iburst'), ['bool'])),
                            ('prefer', (YLeaf(YType.boolean, 'prefer'), ['bool'])),
                        ])
                        self.address = None
                        self.port = None
                        self.version = None
                        self.association_type = None
                        self.iburst = None
                        self.prefer = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Ntp.Servers.Server.Config, ['address', 'port', 'version', 'association_type', 'iburst', 'prefer'], name, value)

                    class AssociationType(Enum):
                        """
                        AssociationType (Enum Class)

                        The desired association type for this NTP server.

                        .. data:: SERVER = 0

                        	Use client association mode.  This device

                        	will not provide synchronization to the

                        	configured NTP server.

                        .. data:: PEER = 1

                        	Use symmetric active association mode.

                        	This device may provide synchronization

                        	to the configured NTP server.

                        .. data:: POOL = 2

                        	Use client association mode with one or

                        	more of the NTP servers found by DNS

                        	resolution of the domain name given by

                        	the 'address' leaf.  This device will not

                        	provide synchronization to the servers.

                        """

                        SERVER = Enum.YLeaf(0, "SERVER")

                        PEER = Enum.YLeaf(1, "PEER")

                        POOL = Enum.YLeaf(2, "POOL")




                class State(_Entity_):
                    """
                    Operational state data for an NTP server.
                    
                    .. attribute:: address
                    
                    	The address or hostname of the NTP server
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                    
                    		**type**\: str
                    
                    			**length:** 1..253
                    
                    	**config**\: False
                    
                    .. attribute:: port
                    
                    	The port number of the NTP server
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    	**default value**\: 123
                    
                    .. attribute:: version
                    
                    	Version number to put in outgoing NTP packets
                    	**type**\: int
                    
                    	**range:** 1..4
                    
                    	**config**\: False
                    
                    	**default value**\: 4
                    
                    .. attribute:: association_type
                    
                    	The desired association type for this NTP server
                    	**type**\:  :py:class:`AssociationType <ydk.models.openconfig.openconfig_system.System.Ntp.Servers.Server.State.AssociationType>`
                    
                    	**config**\: False
                    
                    	**default value**\: SERVER
                    
                    .. attribute:: iburst
                    
                    	Indicates whether this server should enable burst synchronization or not
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    	**default value**\: false
                    
                    .. attribute:: prefer
                    
                    	Indicates whether this server should be preferred or not
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    	**default value**\: false
                    
                    .. attribute:: stratum
                    
                    	Indicates the level of the server in the NTP hierarchy. As stratum number increases, the accuracy is degraded.  Primary servers are stratum while a maximum value of 16 indicates unsynchronized.  The values have the following specific semantics\:  \| 0      \| unspecified or invalid \| 1      \| primary server (e.g., equipped with a GPS receiver) \| 2\-15   \| secondary server (via NTP) \| 16     \| unsynchronized \| 17\-255 \| reserved
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: root_delay
                    
                    	The round\-trip delay to the server, in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: milliseconds
                    
                    .. attribute:: root_dispersion
                    
                    	Dispersion (epsilon) represents the maximum error inherent in the measurement
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: milliseconds
                    
                    .. attribute:: offset
                    
                    	Estimate of the current time offset from the peer.  This is the time difference between the local and reference clock
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: milliseconds
                    
                    .. attribute:: poll_interval
                    
                    	Polling interval of the peer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: seconds
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Ntp.Servers.Server.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str','str','str'])),
                            ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                            ('version', (YLeaf(YType.uint8, 'version'), ['int'])),
                            ('association_type', (YLeaf(YType.enumeration, 'association-type'), [('ydk.models.openconfig.openconfig_system', 'System', 'Ntp.Servers.Server.State.AssociationType')])),
                            ('iburst', (YLeaf(YType.boolean, 'iburst'), ['bool'])),
                            ('prefer', (YLeaf(YType.boolean, 'prefer'), ['bool'])),
                            ('stratum', (YLeaf(YType.uint8, 'stratum'), ['int'])),
                            ('root_delay', (YLeaf(YType.uint32, 'root-delay'), ['int'])),
                            ('root_dispersion', (YLeaf(YType.uint64, 'root-dispersion'), ['int'])),
                            ('offset', (YLeaf(YType.uint64, 'offset'), ['int'])),
                            ('poll_interval', (YLeaf(YType.uint32, 'poll-interval'), ['int'])),
                        ])
                        self.address = None
                        self.port = None
                        self.version = None
                        self.association_type = None
                        self.iburst = None
                        self.prefer = None
                        self.stratum = None
                        self.root_delay = None
                        self.root_dispersion = None
                        self.offset = None
                        self.poll_interval = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Ntp.Servers.Server.State, ['address', 'port', 'version', 'association_type', 'iburst', 'prefer', 'stratum', 'root_delay', 'root_dispersion', 'offset', 'poll_interval'], name, value)

                    class AssociationType(Enum):
                        """
                        AssociationType (Enum Class)

                        The desired association type for this NTP server.

                        .. data:: SERVER = 0

                        	Use client association mode.  This device

                        	will not provide synchronization to the

                        	configured NTP server.

                        .. data:: PEER = 1

                        	Use symmetric active association mode.

                        	This device may provide synchronization

                        	to the configured NTP server.

                        .. data:: POOL = 2

                        	Use client association mode with one or

                        	more of the NTP servers found by DNS

                        	resolution of the domain name given by

                        	the 'address' leaf.  This device will not

                        	provide synchronization to the servers.

                        """

                        SERVER = Enum.YLeaf(0, "SERVER")

                        PEER = Enum.YLeaf(1, "PEER")

                        POOL = Enum.YLeaf(2, "POOL")







    class GrpcServer(_Entity_):
        """
        Top\-level container for the gRPC server
        
        .. attribute:: config
        
        	Configuration data for the system gRPC server
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.GrpcServer.Config>`
        
        .. attribute:: state
        
        	Operational state data for the system gRPC server
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.GrpcServer.State>`
        
        	**config**\: False
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.GrpcServer, self).__init__()

            self.yang_name = "grpc-server"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("config", ("config", System.GrpcServer.Config)), ("state", ("state", System.GrpcServer.State))])
            self._leafs = OrderedDict()

            self.config = System.GrpcServer.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.state = System.GrpcServer.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"
            self._segment_path = lambda: "grpc-server"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.GrpcServer, [], name, value)


        class Config(_Entity_):
            """
            Configuration data for the system gRPC server
            
            .. attribute:: enable
            
            	Enables the gRPC server. The gRPC server is enabled by default
            	**type**\: bool
            
            	**default value**\: true
            
            .. attribute:: port
            
            	TCP port on which the gRPC server should listen
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: transport_security
            
            	Enables gRPC transport security (e.g., TLS or SSL)
            	**type**\: bool
            
            .. attribute:: certificate_id
            
            	The certificate ID to be used for authentication
            	**type**\: str
            
            .. attribute:: listen_addresses
            
            	The IP addresses that the gRPC server should listen on. This may be an IPv4 or an IPv6 address
            	**type**\: union of the below types:
            
            		**type**\: list of str
            
            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
            
            		**type**\: list of str
            
            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
            
            		**type**\: list of   :py:class:`ListenAddresses <ydk.models.openconfig.openconfig_system.System.GrpcServer.State.ListenAddresses>`
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.GrpcServer.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "grpc-server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                    ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                    ('transport_security', (YLeaf(YType.boolean, 'transport-security'), ['bool'])),
                    ('certificate_id', (YLeaf(YType.str, 'certificate-id'), ['str'])),
                    ('listen_addresses', (YLeafList(YType.str, 'listen-addresses'), ['str','str',('ydk.models.openconfig.openconfig_system', 'System', 'GrpcServer.State.ListenAddresses')])),
                ])
                self.enable = None
                self.port = None
                self.transport_security = None
                self.certificate_id = None
                self.listen_addresses = []
                self._segment_path = lambda: "config"
                self._absolute_path = lambda: "openconfig-system:system/grpc-server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.GrpcServer.Config, ['enable', 'port', 'transport_security', 'certificate_id', 'listen_addresses'], name, value)

            class ListenAddresses(Enum):
                """
                ListenAddresses (Enum Class)

                The IP addresses that the gRPC server should listen

                on. This may be an IPv4 or an IPv6 address

                .. data:: ANY = 0

                	The gRPC daemon should listen on any address

                	bound to an interface on the system.

                """

                ANY = Enum.YLeaf(0, "ANY")




        class State(_Entity_):
            """
            Operational state data for the system gRPC server
            
            .. attribute:: enable
            
            	Enables the gRPC server. The gRPC server is enabled by default
            	**type**\: bool
            
            	**config**\: False
            
            	**default value**\: true
            
            .. attribute:: port
            
            	TCP port on which the gRPC server should listen
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: transport_security
            
            	Enables gRPC transport security (e.g., TLS or SSL)
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: certificate_id
            
            	The certificate ID to be used for authentication
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: listen_addresses
            
            	The IP addresses that the gRPC server should listen on. This may be an IPv4 or an IPv6 address
            	**type**\: union of the below types:
            
            		**type**\: list of str
            
            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
            
            		**type**\: list of str
            
            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
            
            		**type**\: list of   :py:class:`ListenAddresses <ydk.models.openconfig.openconfig_system.System.GrpcServer.State.ListenAddresses>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.GrpcServer.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "grpc-server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                    ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                    ('transport_security', (YLeaf(YType.boolean, 'transport-security'), ['bool'])),
                    ('certificate_id', (YLeaf(YType.str, 'certificate-id'), ['str'])),
                    ('listen_addresses', (YLeafList(YType.str, 'listen-addresses'), ['str','str',('ydk.models.openconfig.openconfig_system', 'System', 'GrpcServer.State.ListenAddresses')])),
                ])
                self.enable = None
                self.port = None
                self.transport_security = None
                self.certificate_id = None
                self.listen_addresses = []
                self._segment_path = lambda: "state"
                self._absolute_path = lambda: "openconfig-system:system/grpc-server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.GrpcServer.State, ['enable', 'port', 'transport_security', 'certificate_id', 'listen_addresses'], name, value)

            class ListenAddresses(Enum):
                """
                ListenAddresses (Enum Class)

                The IP addresses that the gRPC server should listen

                on. This may be an IPv4 or an IPv6 address

                .. data:: ANY = 0

                	The gRPC daemon should listen on any address

                	bound to an interface on the system.

                """

                ANY = Enum.YLeaf(0, "ANY")





    class SshServer(_Entity_):
        """
        Top\-level container for ssh server
        
        .. attribute:: config
        
        	Configuration data for the system ssh server
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.SshServer.Config>`
        
        .. attribute:: state
        
        	Operational state data for the system ssh server
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.SshServer.State>`
        
        	**config**\: False
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.SshServer, self).__init__()

            self.yang_name = "ssh-server"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("config", ("config", System.SshServer.Config)), ("state", ("state", System.SshServer.State))])
            self._leafs = OrderedDict()

            self.config = System.SshServer.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.state = System.SshServer.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"
            self._segment_path = lambda: "ssh-server"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.SshServer, [], name, value)


        class Config(_Entity_):
            """
            Configuration data for the system ssh server
            
            .. attribute:: enable
            
            	Enables the ssh server.  The ssh server is enabled by default
            	**type**\: bool
            
            	**default value**\: true
            
            .. attribute:: protocol_version
            
            	Set the protocol version for SSH connections to the system
            	**type**\:  :py:class:`ProtocolVersion <ydk.models.openconfig.openconfig_system.System.SshServer.Config.ProtocolVersion>`
            
            	**default value**\: V2
            
            .. attribute:: timeout
            
            	Set the idle timeout in seconds on terminal connections to the system for the protocol
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: rate_limit
            
            	Set a limit on the number of connection attempts per minute to the system for the protocol
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: conn/min
            
            .. attribute:: session_limit
            
            	Set a limit on the number of simultaneous active terminal sessions to the system for the protocol (e.g., ssh, telnet, ...) 
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.SshServer.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "ssh-server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                    ('protocol_version', (YLeaf(YType.enumeration, 'protocol-version'), [('ydk.models.openconfig.openconfig_system', 'System', 'SshServer.Config.ProtocolVersion')])),
                    ('timeout', (YLeaf(YType.uint16, 'timeout'), ['int'])),
                    ('rate_limit', (YLeaf(YType.uint16, 'rate-limit'), ['int'])),
                    ('session_limit', (YLeaf(YType.uint16, 'session-limit'), ['int'])),
                ])
                self.enable = None
                self.protocol_version = None
                self.timeout = None
                self.rate_limit = None
                self.session_limit = None
                self._segment_path = lambda: "config"
                self._absolute_path = lambda: "openconfig-system:system/ssh-server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.SshServer.Config, ['enable', 'protocol_version', 'timeout', 'rate_limit', 'session_limit'], name, value)

            class ProtocolVersion(Enum):
                """
                ProtocolVersion (Enum Class)

                Set the protocol version for SSH connections to the system

                .. data:: V2 = 0

                	Use SSH v2 only

                .. data:: V1 = 1

                	Use SSH v1 only

                .. data:: V1_V2 = 2

                	Use either SSH v1 or v2

                """

                V2 = Enum.YLeaf(0, "V2")

                V1 = Enum.YLeaf(1, "V1")

                V1_V2 = Enum.YLeaf(2, "V1_V2")




        class State(_Entity_):
            """
            Operational state data for the system ssh server
            
            .. attribute:: enable
            
            	Enables the ssh server.  The ssh server is enabled by default
            	**type**\: bool
            
            	**config**\: False
            
            	**default value**\: true
            
            .. attribute:: protocol_version
            
            	Set the protocol version for SSH connections to the system
            	**type**\:  :py:class:`ProtocolVersion <ydk.models.openconfig.openconfig_system.System.SshServer.State.ProtocolVersion>`
            
            	**config**\: False
            
            	**default value**\: V2
            
            .. attribute:: timeout
            
            	Set the idle timeout in seconds on terminal connections to the system for the protocol
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rate_limit
            
            	Set a limit on the number of connection attempts per minute to the system for the protocol
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: conn/min
            
            .. attribute:: session_limit
            
            	Set a limit on the number of simultaneous active terminal sessions to the system for the protocol (e.g., ssh, telnet, ...) 
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.SshServer.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "ssh-server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                    ('protocol_version', (YLeaf(YType.enumeration, 'protocol-version'), [('ydk.models.openconfig.openconfig_system', 'System', 'SshServer.State.ProtocolVersion')])),
                    ('timeout', (YLeaf(YType.uint16, 'timeout'), ['int'])),
                    ('rate_limit', (YLeaf(YType.uint16, 'rate-limit'), ['int'])),
                    ('session_limit', (YLeaf(YType.uint16, 'session-limit'), ['int'])),
                ])
                self.enable = None
                self.protocol_version = None
                self.timeout = None
                self.rate_limit = None
                self.session_limit = None
                self._segment_path = lambda: "state"
                self._absolute_path = lambda: "openconfig-system:system/ssh-server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.SshServer.State, ['enable', 'protocol_version', 'timeout', 'rate_limit', 'session_limit'], name, value)

            class ProtocolVersion(Enum):
                """
                ProtocolVersion (Enum Class)

                Set the protocol version for SSH connections to the system

                .. data:: V2 = 0

                	Use SSH v2 only

                .. data:: V1 = 1

                	Use SSH v1 only

                .. data:: V1_V2 = 2

                	Use either SSH v1 or v2

                """

                V2 = Enum.YLeaf(0, "V2")

                V1 = Enum.YLeaf(1, "V1")

                V1_V2 = Enum.YLeaf(2, "V1_V2")





    class TelnetServer(_Entity_):
        """
        Top\-level container for telnet terminal servers
        
        .. attribute:: config
        
        	Configuration data for telnet
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.TelnetServer.Config>`
        
        .. attribute:: state
        
        	Operational state data for telnet
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.TelnetServer.State>`
        
        	**config**\: False
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.TelnetServer, self).__init__()

            self.yang_name = "telnet-server"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("config", ("config", System.TelnetServer.Config)), ("state", ("state", System.TelnetServer.State))])
            self._leafs = OrderedDict()

            self.config = System.TelnetServer.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.state = System.TelnetServer.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"
            self._segment_path = lambda: "telnet-server"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.TelnetServer, [], name, value)


        class Config(_Entity_):
            """
            Configuration data for telnet
            
            .. attribute:: enable
            
            	Enables the telnet server.  Telnet is disabled by default
            	**type**\: bool
            
            	**default value**\: false
            
            .. attribute:: timeout
            
            	Set the idle timeout in seconds on terminal connections to the system for the protocol
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: rate_limit
            
            	Set a limit on the number of connection attempts per minute to the system for the protocol
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: conn/min
            
            .. attribute:: session_limit
            
            	Set a limit on the number of simultaneous active terminal sessions to the system for the protocol (e.g., ssh, telnet, ...) 
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.TelnetServer.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "telnet-server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                    ('timeout', (YLeaf(YType.uint16, 'timeout'), ['int'])),
                    ('rate_limit', (YLeaf(YType.uint16, 'rate-limit'), ['int'])),
                    ('session_limit', (YLeaf(YType.uint16, 'session-limit'), ['int'])),
                ])
                self.enable = None
                self.timeout = None
                self.rate_limit = None
                self.session_limit = None
                self._segment_path = lambda: "config"
                self._absolute_path = lambda: "openconfig-system:system/telnet-server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.TelnetServer.Config, ['enable', 'timeout', 'rate_limit', 'session_limit'], name, value)



        class State(_Entity_):
            """
            Operational state data for telnet
            
            .. attribute:: enable
            
            	Enables the telnet server.  Telnet is disabled by default
            	**type**\: bool
            
            	**config**\: False
            
            	**default value**\: false
            
            .. attribute:: timeout
            
            	Set the idle timeout in seconds on terminal connections to the system for the protocol
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: rate_limit
            
            	Set a limit on the number of connection attempts per minute to the system for the protocol
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: conn/min
            
            .. attribute:: session_limit
            
            	Set a limit on the number of simultaneous active terminal sessions to the system for the protocol (e.g., ssh, telnet, ...) 
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.TelnetServer.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "telnet-server"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                    ('timeout', (YLeaf(YType.uint16, 'timeout'), ['int'])),
                    ('rate_limit', (YLeaf(YType.uint16, 'rate-limit'), ['int'])),
                    ('session_limit', (YLeaf(YType.uint16, 'session-limit'), ['int'])),
                ])
                self.enable = None
                self.timeout = None
                self.rate_limit = None
                self.session_limit = None
                self._segment_path = lambda: "state"
                self._absolute_path = lambda: "openconfig-system:system/telnet-server/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.TelnetServer.State, ['enable', 'timeout', 'rate_limit', 'session_limit'], name, value)




    class Logging(_Entity_):
        """
        Top\-level container for data related to logging / syslog
        
        .. attribute:: console
        
        	Top\-level container for data related to console\-based logging
        	**type**\:  :py:class:`Console <ydk.models.openconfig.openconfig_system.System.Logging.Console>`
        
        .. attribute:: remote_servers
        
        	Enclosing container for the list of remote log servers
        	**type**\:  :py:class:`RemoteServers <ydk.models.openconfig.openconfig_system.System.Logging.RemoteServers>`
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("console", ("console", System.Logging.Console)), ("remote-servers", ("remote_servers", System.Logging.RemoteServers))])
            self._leafs = OrderedDict()

            self.console = System.Logging.Console()
            self.console.parent = self
            self._children_name_map["console"] = "console"

            self.remote_servers = System.Logging.RemoteServers()
            self.remote_servers.parent = self
            self._children_name_map["remote_servers"] = "remote-servers"
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.Logging, [], name, value)


        class Console(_Entity_):
            """
            Top\-level container for data related to console\-based
            logging
            
            .. attribute:: config
            
            	Configuration data for console logging
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Logging.Console.Config>`
            
            .. attribute:: state
            
            	Operational state data for console logging
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Logging.Console.State>`
            
            	**config**\: False
            
            .. attribute:: selectors
            
            	Enclosing container 
            	**type**\:  :py:class:`Selectors <ydk.models.openconfig.openconfig_system.System.Logging.Console.Selectors>`
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Logging.Console, self).__init__()

                self.yang_name = "console"
                self.yang_parent_name = "logging"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", System.Logging.Console.Config)), ("state", ("state", System.Logging.Console.State)), ("selectors", ("selectors", System.Logging.Console.Selectors))])
                self._leafs = OrderedDict()

                self.config = System.Logging.Console.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = System.Logging.Console.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.selectors = System.Logging.Console.Selectors()
                self.selectors.parent = self
                self._children_name_map["selectors"] = "selectors"
                self._segment_path = lambda: "console"
                self._absolute_path = lambda: "openconfig-system:system/logging/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Logging.Console, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for console logging
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Logging.Console.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "console"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-system:system/logging/console/%s" % self._segment_path()
                    self._is_frozen = True



            class State(_Entity_):
                """
                Operational state data for console logging
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Logging.Console.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "console"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-system:system/logging/console/%s" % self._segment_path()
                    self._is_frozen = True



            class Selectors(_Entity_):
                """
                Enclosing container 
                
                .. attribute:: selector
                
                	List of selectors for log messages
                	**type**\: list of  		 :py:class:`Selector <ydk.models.openconfig.openconfig_system.System.Logging.Console.Selectors.Selector>`
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Logging.Console.Selectors, self).__init__()

                    self.yang_name = "selectors"
                    self.yang_parent_name = "console"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("selector", ("selector", System.Logging.Console.Selectors.Selector))])
                    self._leafs = OrderedDict()

                    self.selector = YList(self)
                    self._segment_path = lambda: "selectors"
                    self._absolute_path = lambda: "openconfig-system:system/logging/console/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Logging.Console.Selectors, [], name, value)


                class Selector(_Entity_):
                    """
                    List of selectors for log messages
                    
                    .. attribute:: facility  (key)
                    
                    	Reference to facility list key
                    	**type**\:  :py:class:`SYSLOGFACILITY <ydk.models.openconfig.openconfig_system_logging.SYSLOGFACILITY>`
                    
                    .. attribute:: severity  (key)
                    
                    	Reference to severity list key
                    	**type**\:  :py:class:`SyslogSeverity <ydk.models.openconfig.openconfig_system_logging.SyslogSeverity>`
                    
                    .. attribute:: config
                    
                    	Configuration data 
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Logging.Console.Selectors.Selector.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data 
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Logging.Console.Selectors.Selector.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Logging.Console.Selectors.Selector, self).__init__()

                        self.yang_name = "selector"
                        self.yang_parent_name = "selectors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['facility','severity']
                        self._child_classes = OrderedDict([("config", ("config", System.Logging.Console.Selectors.Selector.Config)), ("state", ("state", System.Logging.Console.Selectors.Selector.State))])
                        self._leafs = OrderedDict([
                            ('facility', (YLeaf(YType.identityref, 'facility'), [('ydk.models.openconfig.openconfig_system_logging', 'SYSLOGFACILITY')])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.openconfig.openconfig_system_logging', 'SyslogSeverity', '')])),
                        ])
                        self.facility = None
                        self.severity = None

                        self.config = System.Logging.Console.Selectors.Selector.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = System.Logging.Console.Selectors.Selector.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "selector" + "[facility='" + str(self.facility) + "']" + "[severity='" + str(self.severity) + "']"
                        self._absolute_path = lambda: "openconfig-system:system/logging/console/selectors/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Logging.Console.Selectors.Selector, ['facility', 'severity'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data 
                        
                        .. attribute:: facility
                        
                        	Specifies the facility, or class of messages to log
                        	**type**\:  :py:class:`SYSLOGFACILITY <ydk.models.openconfig.openconfig_system_logging.SYSLOGFACILITY>`
                        
                        .. attribute:: severity
                        
                        	Specifies that only messages of the given severity (or greater severity) for the corresonding facility are logged
                        	**type**\:  :py:class:`SyslogSeverity <ydk.models.openconfig.openconfig_system_logging.SyslogSeverity>`
                        
                        

                        """

                        _prefix = 'oc-sys'
                        _revision = '2018-07-17'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(System.Logging.Console.Selectors.Selector.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "selector"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('facility', (YLeaf(YType.identityref, 'facility'), [('ydk.models.openconfig.openconfig_system_logging', 'SYSLOGFACILITY')])),
                                ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.openconfig.openconfig_system_logging', 'SyslogSeverity', '')])),
                            ])
                            self.facility = None
                            self.severity = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(System.Logging.Console.Selectors.Selector.Config, ['facility', 'severity'], name, value)



                    class State(_Entity_):
                        """
                        Operational state data 
                        
                        .. attribute:: facility
                        
                        	Specifies the facility, or class of messages to log
                        	**type**\:  :py:class:`SYSLOGFACILITY <ydk.models.openconfig.openconfig_system_logging.SYSLOGFACILITY>`
                        
                        	**config**\: False
                        
                        .. attribute:: severity
                        
                        	Specifies that only messages of the given severity (or greater severity) for the corresonding facility are logged
                        	**type**\:  :py:class:`SyslogSeverity <ydk.models.openconfig.openconfig_system_logging.SyslogSeverity>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-sys'
                        _revision = '2018-07-17'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(System.Logging.Console.Selectors.Selector.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "selector"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('facility', (YLeaf(YType.identityref, 'facility'), [('ydk.models.openconfig.openconfig_system_logging', 'SYSLOGFACILITY')])),
                                ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.openconfig.openconfig_system_logging', 'SyslogSeverity', '')])),
                            ])
                            self.facility = None
                            self.severity = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(System.Logging.Console.Selectors.Selector.State, ['facility', 'severity'], name, value)






        class RemoteServers(_Entity_):
            """
            Enclosing container for the list of remote log servers
            
            .. attribute:: remote_server
            
            	List of remote log servers
            	**type**\: list of  		 :py:class:`RemoteServer <ydk.models.openconfig.openconfig_system.System.Logging.RemoteServers.RemoteServer>`
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Logging.RemoteServers, self).__init__()

                self.yang_name = "remote-servers"
                self.yang_parent_name = "logging"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("remote-server", ("remote_server", System.Logging.RemoteServers.RemoteServer))])
                self._leafs = OrderedDict()

                self.remote_server = YList(self)
                self._segment_path = lambda: "remote-servers"
                self._absolute_path = lambda: "openconfig-system:system/logging/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Logging.RemoteServers, [], name, value)


            class RemoteServer(_Entity_):
                """
                List of remote log servers
                
                .. attribute:: host  (key)
                
                	Reference to the host list key
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                
                		**type**\: str
                
                			**length:** 1..253
                
                	**refers to**\:  :py:class:`host <ydk.models.openconfig.openconfig_system.System.Logging.RemoteServers.RemoteServer.Config>`
                
                .. attribute:: config
                
                	Configuration data for remote log servers
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Logging.RemoteServers.RemoteServer.Config>`
                
                .. attribute:: state
                
                	Operational state data for remote log servers
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Logging.RemoteServers.RemoteServer.State>`
                
                	**config**\: False
                
                .. attribute:: selectors
                
                	Enclosing container 
                	**type**\:  :py:class:`Selectors <ydk.models.openconfig.openconfig_system.System.Logging.RemoteServers.RemoteServer.Selectors>`
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Logging.RemoteServers.RemoteServer, self).__init__()

                    self.yang_name = "remote-server"
                    self.yang_parent_name = "remote-servers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['host']
                    self._child_classes = OrderedDict([("config", ("config", System.Logging.RemoteServers.RemoteServer.Config)), ("state", ("state", System.Logging.RemoteServers.RemoteServer.State)), ("selectors", ("selectors", System.Logging.RemoteServers.RemoteServer.Selectors))])
                    self._leafs = OrderedDict([
                        ('host', (YLeaf(YType.str, 'host'), ['str'])),
                    ])
                    self.host = None

                    self.config = System.Logging.RemoteServers.RemoteServer.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = System.Logging.RemoteServers.RemoteServer.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"

                    self.selectors = System.Logging.RemoteServers.RemoteServer.Selectors()
                    self.selectors.parent = self
                    self._children_name_map["selectors"] = "selectors"
                    self._segment_path = lambda: "remote-server" + "[host='" + str(self.host) + "']"
                    self._absolute_path = lambda: "openconfig-system:system/logging/remote-servers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Logging.RemoteServers.RemoteServer, ['host'], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for remote log servers
                    
                    .. attribute:: host
                    
                    	IP address or hostname of the remote log server
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                    
                    		**type**\: str
                    
                    			**length:** 1..253
                    
                    .. attribute:: source_address
                    
                    	Source IP address for packets to the log server
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                    
                    .. attribute:: remote_port
                    
                    	Sets the destination port number for syslog UDP messages to the server.  The default for syslog is 514
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 514
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Logging.RemoteServers.RemoteServer.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "remote-server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('host', (YLeaf(YType.str, 'host'), ['str','str','str'])),
                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                            ('remote_port', (YLeaf(YType.uint16, 'remote-port'), ['int'])),
                        ])
                        self.host = None
                        self.source_address = None
                        self.remote_port = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Logging.RemoteServers.RemoteServer.Config, ['host', 'source_address', 'remote_port'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for remote log servers
                    
                    .. attribute:: host
                    
                    	IP address or hostname of the remote log server
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                    
                    		**type**\: str
                    
                    			**length:** 1..253
                    
                    	**config**\: False
                    
                    .. attribute:: source_address
                    
                    	Source IP address for packets to the log server
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                    
                    	**config**\: False
                    
                    .. attribute:: remote_port
                    
                    	Sets the destination port number for syslog UDP messages to the server.  The default for syslog is 514
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    	**default value**\: 514
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Logging.RemoteServers.RemoteServer.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "remote-server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('host', (YLeaf(YType.str, 'host'), ['str','str','str'])),
                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                            ('remote_port', (YLeaf(YType.uint16, 'remote-port'), ['int'])),
                        ])
                        self.host = None
                        self.source_address = None
                        self.remote_port = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Logging.RemoteServers.RemoteServer.State, ['host', 'source_address', 'remote_port'], name, value)



                class Selectors(_Entity_):
                    """
                    Enclosing container 
                    
                    .. attribute:: selector
                    
                    	List of selectors for log messages
                    	**type**\: list of  		 :py:class:`Selector <ydk.models.openconfig.openconfig_system.System.Logging.RemoteServers.RemoteServer.Selectors.Selector>`
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Logging.RemoteServers.RemoteServer.Selectors, self).__init__()

                        self.yang_name = "selectors"
                        self.yang_parent_name = "remote-server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("selector", ("selector", System.Logging.RemoteServers.RemoteServer.Selectors.Selector))])
                        self._leafs = OrderedDict()

                        self.selector = YList(self)
                        self._segment_path = lambda: "selectors"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Logging.RemoteServers.RemoteServer.Selectors, [], name, value)


                    class Selector(_Entity_):
                        """
                        List of selectors for log messages
                        
                        .. attribute:: facility  (key)
                        
                        	Reference to facility list key
                        	**type**\:  :py:class:`SYSLOGFACILITY <ydk.models.openconfig.openconfig_system_logging.SYSLOGFACILITY>`
                        
                        .. attribute:: severity  (key)
                        
                        	Reference to severity list key
                        	**type**\:  :py:class:`SyslogSeverity <ydk.models.openconfig.openconfig_system_logging.SyslogSeverity>`
                        
                        .. attribute:: config
                        
                        	Configuration data 
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Logging.RemoteServers.RemoteServer.Selectors.Selector.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data 
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Logging.RemoteServers.RemoteServer.Selectors.Selector.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-sys'
                        _revision = '2018-07-17'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(System.Logging.RemoteServers.RemoteServer.Selectors.Selector, self).__init__()

                            self.yang_name = "selector"
                            self.yang_parent_name = "selectors"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['facility','severity']
                            self._child_classes = OrderedDict([("config", ("config", System.Logging.RemoteServers.RemoteServer.Selectors.Selector.Config)), ("state", ("state", System.Logging.RemoteServers.RemoteServer.Selectors.Selector.State))])
                            self._leafs = OrderedDict([
                                ('facility', (YLeaf(YType.identityref, 'facility'), [('ydk.models.openconfig.openconfig_system_logging', 'SYSLOGFACILITY')])),
                                ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.openconfig.openconfig_system_logging', 'SyslogSeverity', '')])),
                            ])
                            self.facility = None
                            self.severity = None

                            self.config = System.Logging.RemoteServers.RemoteServer.Selectors.Selector.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = System.Logging.RemoteServers.RemoteServer.Selectors.Selector.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "selector" + "[facility='" + str(self.facility) + "']" + "[severity='" + str(self.severity) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(System.Logging.RemoteServers.RemoteServer.Selectors.Selector, ['facility', 'severity'], name, value)


                        class Config(_Entity_):
                            """
                            Configuration data 
                            
                            .. attribute:: facility
                            
                            	Specifies the facility, or class of messages to log
                            	**type**\:  :py:class:`SYSLOGFACILITY <ydk.models.openconfig.openconfig_system_logging.SYSLOGFACILITY>`
                            
                            .. attribute:: severity
                            
                            	Specifies that only messages of the given severity (or greater severity) for the corresonding facility are logged
                            	**type**\:  :py:class:`SyslogSeverity <ydk.models.openconfig.openconfig_system_logging.SyslogSeverity>`
                            
                            

                            """

                            _prefix = 'oc-sys'
                            _revision = '2018-07-17'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(System.Logging.RemoteServers.RemoteServer.Selectors.Selector.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "selector"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('facility', (YLeaf(YType.identityref, 'facility'), [('ydk.models.openconfig.openconfig_system_logging', 'SYSLOGFACILITY')])),
                                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.openconfig.openconfig_system_logging', 'SyslogSeverity', '')])),
                                ])
                                self.facility = None
                                self.severity = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(System.Logging.RemoteServers.RemoteServer.Selectors.Selector.Config, ['facility', 'severity'], name, value)



                        class State(_Entity_):
                            """
                            Operational state data 
                            
                            .. attribute:: facility
                            
                            	Specifies the facility, or class of messages to log
                            	**type**\:  :py:class:`SYSLOGFACILITY <ydk.models.openconfig.openconfig_system_logging.SYSLOGFACILITY>`
                            
                            	**config**\: False
                            
                            .. attribute:: severity
                            
                            	Specifies that only messages of the given severity (or greater severity) for the corresonding facility are logged
                            	**type**\:  :py:class:`SyslogSeverity <ydk.models.openconfig.openconfig_system_logging.SyslogSeverity>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-sys'
                            _revision = '2018-07-17'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(System.Logging.RemoteServers.RemoteServer.Selectors.Selector.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "selector"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('facility', (YLeaf(YType.identityref, 'facility'), [('ydk.models.openconfig.openconfig_system_logging', 'SYSLOGFACILITY')])),
                                    ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.openconfig.openconfig_system_logging', 'SyslogSeverity', '')])),
                                ])
                                self.facility = None
                                self.severity = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(System.Logging.RemoteServers.RemoteServer.Selectors.Selector.State, ['facility', 'severity'], name, value)








    class Aaa(_Entity_):
        """
        Top\-level container for AAA services
        
        .. attribute:: config
        
        	Configuration data for top level AAA services
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.Config>`
        
        .. attribute:: state
        
        	Operational state data for top level AAA services 
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.State>`
        
        	**config**\: False
        
        .. attribute:: authentication
        
        	Top\-level container for global authentication data
        	**type**\:  :py:class:`Authentication <ydk.models.openconfig.openconfig_system.System.Aaa.Authentication>`
        
        .. attribute:: authorization
        
        	Top\-level container for AAA authorization configuration and operational state data
        	**type**\:  :py:class:`Authorization <ydk.models.openconfig.openconfig_system.System.Aaa.Authorization>`
        
        .. attribute:: accounting
        
        	Top\-level container for AAA accounting
        	**type**\:  :py:class:`Accounting <ydk.models.openconfig.openconfig_system.System.Aaa.Accounting>`
        
        .. attribute:: server_groups
        
        	Enclosing container for AAA server groups
        	**type**\:  :py:class:`ServerGroups <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups>`
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.Aaa, self).__init__()

            self.yang_name = "aaa"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("config", ("config", System.Aaa.Config)), ("state", ("state", System.Aaa.State)), ("authentication", ("authentication", System.Aaa.Authentication)), ("authorization", ("authorization", System.Aaa.Authorization)), ("accounting", ("accounting", System.Aaa.Accounting)), ("server-groups", ("server_groups", System.Aaa.ServerGroups))])
            self._leafs = OrderedDict()

            self.config = System.Aaa.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.state = System.Aaa.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"

            self.authentication = System.Aaa.Authentication()
            self.authentication.parent = self
            self._children_name_map["authentication"] = "authentication"

            self.authorization = System.Aaa.Authorization()
            self.authorization.parent = self
            self._children_name_map["authorization"] = "authorization"

            self.accounting = System.Aaa.Accounting()
            self.accounting.parent = self
            self._children_name_map["accounting"] = "accounting"

            self.server_groups = System.Aaa.ServerGroups()
            self.server_groups.parent = self
            self._children_name_map["server_groups"] = "server-groups"
            self._segment_path = lambda: "aaa"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.Aaa, [], name, value)


        class Config(_Entity_):
            """
            Configuration data for top level AAA services
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Aaa.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "aaa"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict()
                self._segment_path = lambda: "config"
                self._absolute_path = lambda: "openconfig-system:system/aaa/%s" % self._segment_path()
                self._is_frozen = True



        class State(_Entity_):
            """
            Operational state data for top level AAA services 
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Aaa.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "aaa"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict()
                self._segment_path = lambda: "state"
                self._absolute_path = lambda: "openconfig-system:system/aaa/%s" % self._segment_path()
                self._is_frozen = True



        class Authentication(_Entity_):
            """
            Top\-level container for global authentication data
            
            .. attribute:: config
            
            	Configuration data for global authentication services
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.Authentication.Config>`
            
            .. attribute:: state
            
            	Operational state data for global authentication services
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.Authentication.State>`
            
            	**config**\: False
            
            .. attribute:: admin_user
            
            	Top\-level container for the system root or admin user configuration and operational state
            	**type**\:  :py:class:`AdminUser <ydk.models.openconfig.openconfig_system.System.Aaa.Authentication.AdminUser>`
            
            .. attribute:: users
            
            	Enclosing container list of local users
            	**type**\:  :py:class:`Users <ydk.models.openconfig.openconfig_system.System.Aaa.Authentication.Users>`
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Aaa.Authentication, self).__init__()

                self.yang_name = "authentication"
                self.yang_parent_name = "aaa"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", System.Aaa.Authentication.Config)), ("state", ("state", System.Aaa.Authentication.State)), ("admin-user", ("admin_user", System.Aaa.Authentication.AdminUser)), ("users", ("users", System.Aaa.Authentication.Users))])
                self._leafs = OrderedDict()

                self.config = System.Aaa.Authentication.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = System.Aaa.Authentication.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.admin_user = System.Aaa.Authentication.AdminUser()
                self.admin_user.parent = self
                self._children_name_map["admin_user"] = "admin-user"

                self.users = System.Aaa.Authentication.Users()
                self.users.parent = self
                self._children_name_map["users"] = "users"
                self._segment_path = lambda: "authentication"
                self._absolute_path = lambda: "openconfig-system:system/aaa/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Aaa.Authentication, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for global authentication services
                
                .. attribute:: authentication_method
                
                	Ordered list of authentication methods for users.  This can be either a reference to a server group, or a well\- defined designation in the AAA\_METHOD\_TYPE identity.  If authentication fails with one method, the next defined method is tried \-\- failure of all methods results in the user being denied access
                	**type**\: union of the below types:
                
                		**type**\: list of   :py:class:`AAAMETHODTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAMETHODTYPE>`
                
                		**type**\: list of str
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Aaa.Authentication.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "authentication"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('authentication_method', (YLeafList(YType.str, 'authentication-method'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAMETHODTYPE'),'str'])),
                    ])
                    self.authentication_method = []
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-system:system/aaa/authentication/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Aaa.Authentication.Config, ['authentication_method'], name, value)



            class State(_Entity_):
                """
                Operational state data for global authentication
                services
                
                .. attribute:: authentication_method
                
                	Ordered list of authentication methods for users.  This can be either a reference to a server group, or a well\- defined designation in the AAA\_METHOD\_TYPE identity.  If authentication fails with one method, the next defined method is tried \-\- failure of all methods results in the user being denied access
                	**type**\: union of the below types:
                
                		**type**\: list of   :py:class:`AAAMETHODTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAMETHODTYPE>`
                
                		**type**\: list of str
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Aaa.Authentication.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "authentication"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('authentication_method', (YLeafList(YType.str, 'authentication-method'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAMETHODTYPE'),'str'])),
                    ])
                    self.authentication_method = []
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-system:system/aaa/authentication/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Aaa.Authentication.State, ['authentication_method'], name, value)



            class AdminUser(_Entity_):
                """
                Top\-level container for the system root or admin user
                configuration and operational state
                
                .. attribute:: config
                
                	Configuration data for the root user account
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.Authentication.AdminUser.Config>`
                
                .. attribute:: state
                
                	Operational state data for the root user account
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.Authentication.AdminUser.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Aaa.Authentication.AdminUser, self).__init__()

                    self.yang_name = "admin-user"
                    self.yang_parent_name = "authentication"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config", ("config", System.Aaa.Authentication.AdminUser.Config)), ("state", ("state", System.Aaa.Authentication.AdminUser.State))])
                    self._leafs = OrderedDict()

                    self.config = System.Aaa.Authentication.AdminUser.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = System.Aaa.Authentication.AdminUser.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "admin-user"
                    self._absolute_path = lambda: "openconfig-system:system/aaa/authentication/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Aaa.Authentication.AdminUser, [], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for the root user account
                    
                    .. attribute:: admin_password
                    
                    	The admin/root password, supplied as a cleartext string. The system should hash and only store the password as a hashed value
                    	**type**\: str
                    
                    .. attribute:: admin_password_hashed
                    
                    	The admin/root password, supplied as a hashed value using the notation described in the definition of the crypt\-password\-type
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Aaa.Authentication.AdminUser.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "admin-user"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('admin_password', (YLeaf(YType.str, 'admin-password'), ['str'])),
                            ('admin_password_hashed', (YLeaf(YType.str, 'admin-password-hashed'), ['str'])),
                        ])
                        self.admin_password = None
                        self.admin_password_hashed = None
                        self._segment_path = lambda: "config"
                        self._absolute_path = lambda: "openconfig-system:system/aaa/authentication/admin-user/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Aaa.Authentication.AdminUser.Config, ['admin_password', 'admin_password_hashed'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for the root user account
                    
                    .. attribute:: admin_password
                    
                    	The admin/root password, supplied as a cleartext string. The system should hash and only store the password as a hashed value
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: admin_password_hashed
                    
                    	The admin/root password, supplied as a hashed value using the notation described in the definition of the crypt\-password\-type
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: admin_username
                    
                    	Name of the administrator user account, e.g., admin, root, etc
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Aaa.Authentication.AdminUser.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "admin-user"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('admin_password', (YLeaf(YType.str, 'admin-password'), ['str'])),
                            ('admin_password_hashed', (YLeaf(YType.str, 'admin-password-hashed'), ['str'])),
                            ('admin_username', (YLeaf(YType.str, 'admin-username'), ['str'])),
                        ])
                        self.admin_password = None
                        self.admin_password_hashed = None
                        self.admin_username = None
                        self._segment_path = lambda: "state"
                        self._absolute_path = lambda: "openconfig-system:system/aaa/authentication/admin-user/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Aaa.Authentication.AdminUser.State, ['admin_password', 'admin_password_hashed', 'admin_username'], name, value)




            class Users(_Entity_):
                """
                Enclosing container list of local users
                
                .. attribute:: user
                
                	List of local users on the system
                	**type**\: list of  		 :py:class:`User <ydk.models.openconfig.openconfig_system.System.Aaa.Authentication.Users.User>`
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Aaa.Authentication.Users, self).__init__()

                    self.yang_name = "users"
                    self.yang_parent_name = "authentication"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("user", ("user", System.Aaa.Authentication.Users.User))])
                    self._leafs = OrderedDict()

                    self.user = YList(self)
                    self._segment_path = lambda: "users"
                    self._absolute_path = lambda: "openconfig-system:system/aaa/authentication/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Aaa.Authentication.Users, [], name, value)


                class User(_Entity_):
                    """
                    List of local users on the system
                    
                    .. attribute:: username  (key)
                    
                    	References the configured username for the user
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`username <ydk.models.openconfig.openconfig_system.System.Aaa.Authentication.Users.User.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for local users
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.Authentication.Users.User.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for local users
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.Authentication.Users.User.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Aaa.Authentication.Users.User, self).__init__()

                        self.yang_name = "user"
                        self.yang_parent_name = "users"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['username']
                        self._child_classes = OrderedDict([("config", ("config", System.Aaa.Authentication.Users.User.Config)), ("state", ("state", System.Aaa.Authentication.Users.User.State))])
                        self._leafs = OrderedDict([
                            ('username', (YLeaf(YType.str, 'username'), ['str'])),
                        ])
                        self.username = None

                        self.config = System.Aaa.Authentication.Users.User.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = System.Aaa.Authentication.Users.User.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "user" + "[username='" + str(self.username) + "']"
                        self._absolute_path = lambda: "openconfig-system:system/aaa/authentication/users/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Aaa.Authentication.Users.User, ['username'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data for local users
                        
                        .. attribute:: username
                        
                        	Assigned username for this user
                        	**type**\: str
                        
                        .. attribute:: password
                        
                        	The user password, supplied as cleartext.  The system must hash the value and only store the hashed value
                        	**type**\: str
                        
                        .. attribute:: password_hashed
                        
                        	The user password, supplied as a hashed value using the notation described in the definition of the crypt\-password\-type
                        	**type**\: str
                        
                        .. attribute:: ssh_key
                        
                        	SSH public key for the user (RSA or DSA)
                        	**type**\: str
                        
                        .. attribute:: role
                        
                        	Role assigned to the user.  The role may be supplied as a string or a role defined by the SYSTEM\_DEFINED\_ROLES identity
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        		**type**\:  :py:class:`SYSTEMDEFINEDROLES <ydk.models.openconfig.openconfig_aaa_types.SYSTEMDEFINEDROLES>`
                        
                        

                        """

                        _prefix = 'oc-sys'
                        _revision = '2018-07-17'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(System.Aaa.Authentication.Users.User.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "user"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('username', (YLeaf(YType.str, 'username'), ['str'])),
                                ('password', (YLeaf(YType.str, 'password'), ['str'])),
                                ('password_hashed', (YLeaf(YType.str, 'password-hashed'), ['str'])),
                                ('ssh_key', (YLeaf(YType.str, 'ssh-key'), ['str'])),
                                ('role', (YLeaf(YType.str, 'role'), ['str',('ydk.models.openconfig.openconfig_aaa_types', 'SYSTEMDEFINEDROLES')])),
                            ])
                            self.username = None
                            self.password = None
                            self.password_hashed = None
                            self.ssh_key = None
                            self.role = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(System.Aaa.Authentication.Users.User.Config, ['username', 'password', 'password_hashed', 'ssh_key', 'role'], name, value)



                    class State(_Entity_):
                        """
                        Operational state data for local users
                        
                        .. attribute:: username
                        
                        	Assigned username for this user
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: password
                        
                        	The user password, supplied as cleartext.  The system must hash the value and only store the hashed value
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: password_hashed
                        
                        	The user password, supplied as a hashed value using the notation described in the definition of the crypt\-password\-type
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: ssh_key
                        
                        	SSH public key for the user (RSA or DSA)
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: role
                        
                        	Role assigned to the user.  The role may be supplied as a string or a role defined by the SYSTEM\_DEFINED\_ROLES identity
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        		**type**\:  :py:class:`SYSTEMDEFINEDROLES <ydk.models.openconfig.openconfig_aaa_types.SYSTEMDEFINEDROLES>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-sys'
                        _revision = '2018-07-17'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(System.Aaa.Authentication.Users.User.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "user"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('username', (YLeaf(YType.str, 'username'), ['str'])),
                                ('password', (YLeaf(YType.str, 'password'), ['str'])),
                                ('password_hashed', (YLeaf(YType.str, 'password-hashed'), ['str'])),
                                ('ssh_key', (YLeaf(YType.str, 'ssh-key'), ['str'])),
                                ('role', (YLeaf(YType.str, 'role'), ['str',('ydk.models.openconfig.openconfig_aaa_types', 'SYSTEMDEFINEDROLES')])),
                            ])
                            self.username = None
                            self.password = None
                            self.password_hashed = None
                            self.ssh_key = None
                            self.role = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(System.Aaa.Authentication.Users.User.State, ['username', 'password', 'password_hashed', 'ssh_key', 'role'], name, value)






        class Authorization(_Entity_):
            """
            Top\-level container for AAA authorization configuration
            and operational state data
            
            .. attribute:: config
            
            	Configuration data for authorization based on AAA methods
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.Authorization.Config>`
            
            .. attribute:: state
            
            	Operational state data for authorization based on AAA
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.Authorization.State>`
            
            	**config**\: False
            
            .. attribute:: events
            
            	Enclosing container for the set of events subject to authorization
            	**type**\:  :py:class:`Events <ydk.models.openconfig.openconfig_system.System.Aaa.Authorization.Events>`
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Aaa.Authorization, self).__init__()

                self.yang_name = "authorization"
                self.yang_parent_name = "aaa"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", System.Aaa.Authorization.Config)), ("state", ("state", System.Aaa.Authorization.State)), ("events", ("events", System.Aaa.Authorization.Events))])
                self._leafs = OrderedDict()

                self.config = System.Aaa.Authorization.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = System.Aaa.Authorization.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.events = System.Aaa.Authorization.Events()
                self.events.parent = self
                self._children_name_map["events"] = "events"
                self._segment_path = lambda: "authorization"
                self._absolute_path = lambda: "openconfig-system:system/aaa/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Aaa.Authorization, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for authorization based on AAA
                methods
                
                .. attribute:: authorization_method
                
                	Ordered list of methods for authorizing commands.  The first method that provides a response (positive or negative) should be used.  The list may contain a well\-defined method such as the set of all TACACS or RADIUS servers, or the name of a defined AAA server group.  The system must validate that the named server group exists
                	**type**\: union of the below types:
                
                		**type**\: list of   :py:class:`AAAMETHODTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAMETHODTYPE>`
                
                		**type**\: list of str
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Aaa.Authorization.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "authorization"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('authorization_method', (YLeafList(YType.str, 'authorization-method'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAMETHODTYPE'),'str'])),
                    ])
                    self.authorization_method = []
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-system:system/aaa/authorization/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Aaa.Authorization.Config, ['authorization_method'], name, value)



            class State(_Entity_):
                """
                Operational state data for authorization based on AAA
                
                .. attribute:: authorization_method
                
                	Ordered list of methods for authorizing commands.  The first method that provides a response (positive or negative) should be used.  The list may contain a well\-defined method such as the set of all TACACS or RADIUS servers, or the name of a defined AAA server group.  The system must validate that the named server group exists
                	**type**\: union of the below types:
                
                		**type**\: list of   :py:class:`AAAMETHODTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAMETHODTYPE>`
                
                		**type**\: list of str
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Aaa.Authorization.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "authorization"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('authorization_method', (YLeafList(YType.str, 'authorization-method'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAMETHODTYPE'),'str'])),
                    ])
                    self.authorization_method = []
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-system:system/aaa/authorization/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Aaa.Authorization.State, ['authorization_method'], name, value)



            class Events(_Entity_):
                """
                Enclosing container for the set of events subject
                to authorization
                
                .. attribute:: event
                
                	List of events subject to AAA authorization
                	**type**\: list of  		 :py:class:`Event <ydk.models.openconfig.openconfig_system.System.Aaa.Authorization.Events.Event>`
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Aaa.Authorization.Events, self).__init__()

                    self.yang_name = "events"
                    self.yang_parent_name = "authorization"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("event", ("event", System.Aaa.Authorization.Events.Event))])
                    self._leafs = OrderedDict()

                    self.event = YList(self)
                    self._segment_path = lambda: "events"
                    self._absolute_path = lambda: "openconfig-system:system/aaa/authorization/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Aaa.Authorization.Events, [], name, value)


                class Event(_Entity_):
                    """
                    List of events subject to AAA authorization
                    
                    .. attribute:: event_type  (key)
                    
                    	Reference to the event\-type list key
                    	**type**\:  :py:class:`AAAAUTHORIZATIONEVENTTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAAUTHORIZATIONEVENTTYPE>`
                    
                    .. attribute:: config
                    
                    	Configuration data for each authorized event
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.Authorization.Events.Event.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for each authorized activity
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.Authorization.Events.Event.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Aaa.Authorization.Events.Event, self).__init__()

                        self.yang_name = "event"
                        self.yang_parent_name = "events"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['event_type']
                        self._child_classes = OrderedDict([("config", ("config", System.Aaa.Authorization.Events.Event.Config)), ("state", ("state", System.Aaa.Authorization.Events.Event.State))])
                        self._leafs = OrderedDict([
                            ('event_type', (YLeaf(YType.identityref, 'event-type'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAAUTHORIZATIONEVENTTYPE')])),
                        ])
                        self.event_type = None

                        self.config = System.Aaa.Authorization.Events.Event.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = System.Aaa.Authorization.Events.Event.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "event" + "[event-type='" + str(self.event_type) + "']"
                        self._absolute_path = lambda: "openconfig-system:system/aaa/authorization/events/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Aaa.Authorization.Events.Event, ['event_type'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data for each authorized event
                        
                        .. attribute:: event_type
                        
                        	The type of event to record at the AAA authorization server
                        	**type**\:  :py:class:`AAAAUTHORIZATIONEVENTTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAAUTHORIZATIONEVENTTYPE>`
                        
                        

                        """

                        _prefix = 'oc-sys'
                        _revision = '2018-07-17'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(System.Aaa.Authorization.Events.Event.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "event"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('event_type', (YLeaf(YType.identityref, 'event-type'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAAUTHORIZATIONEVENTTYPE')])),
                            ])
                            self.event_type = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(System.Aaa.Authorization.Events.Event.Config, ['event_type'], name, value)



                    class State(_Entity_):
                        """
                        Operational state data for each authorized activity
                        
                        .. attribute:: event_type
                        
                        	The type of event to record at the AAA authorization server
                        	**type**\:  :py:class:`AAAAUTHORIZATIONEVENTTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAAUTHORIZATIONEVENTTYPE>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-sys'
                        _revision = '2018-07-17'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(System.Aaa.Authorization.Events.Event.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "event"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('event_type', (YLeaf(YType.identityref, 'event-type'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAAUTHORIZATIONEVENTTYPE')])),
                            ])
                            self.event_type = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(System.Aaa.Authorization.Events.Event.State, ['event_type'], name, value)






        class Accounting(_Entity_):
            """
            Top\-level container for AAA accounting
            
            .. attribute:: config
            
            	Configuration data for user activity accounting
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.Accounting.Config>`
            
            .. attribute:: state
            
            	Operational state data for user accounting
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.Accounting.State>`
            
            	**config**\: False
            
            .. attribute:: events
            
            	Enclosing container for defining handling of events for accounting
            	**type**\:  :py:class:`Events <ydk.models.openconfig.openconfig_system.System.Aaa.Accounting.Events>`
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Aaa.Accounting, self).__init__()

                self.yang_name = "accounting"
                self.yang_parent_name = "aaa"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", System.Aaa.Accounting.Config)), ("state", ("state", System.Aaa.Accounting.State)), ("events", ("events", System.Aaa.Accounting.Events))])
                self._leafs = OrderedDict()

                self.config = System.Aaa.Accounting.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = System.Aaa.Accounting.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.events = System.Aaa.Accounting.Events()
                self.events.parent = self
                self._children_name_map["events"] = "events"
                self._segment_path = lambda: "accounting"
                self._absolute_path = lambda: "openconfig-system:system/aaa/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Aaa.Accounting, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for user activity accounting.
                
                .. attribute:: accounting_method
                
                	An ordered list of methods used for AAA accounting for this event type.  The method is defined by the destination for accounting data, which may be specified as the group of all TACACS+/RADIUS servers, a defined server group, or the local system
                	**type**\: union of the below types:
                
                		**type**\: list of   :py:class:`AAAMETHODTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAMETHODTYPE>`
                
                		**type**\: list of str
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Aaa.Accounting.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "accounting"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('accounting_method', (YLeafList(YType.str, 'accounting-method'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAMETHODTYPE'),'str'])),
                    ])
                    self.accounting_method = []
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-system:system/aaa/accounting/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Aaa.Accounting.Config, ['accounting_method'], name, value)



            class State(_Entity_):
                """
                Operational state data for user accounting.
                
                .. attribute:: accounting_method
                
                	An ordered list of methods used for AAA accounting for this event type.  The method is defined by the destination for accounting data, which may be specified as the group of all TACACS+/RADIUS servers, a defined server group, or the local system
                	**type**\: union of the below types:
                
                		**type**\: list of   :py:class:`AAAMETHODTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAMETHODTYPE>`
                
                		**type**\: list of str
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Aaa.Accounting.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "accounting"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('accounting_method', (YLeafList(YType.str, 'accounting-method'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAMETHODTYPE'),'str'])),
                    ])
                    self.accounting_method = []
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-system:system/aaa/accounting/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Aaa.Accounting.State, ['accounting_method'], name, value)



            class Events(_Entity_):
                """
                Enclosing container for defining handling of events
                for accounting
                
                .. attribute:: event
                
                	List of events subject to accounting
                	**type**\: list of  		 :py:class:`Event <ydk.models.openconfig.openconfig_system.System.Aaa.Accounting.Events.Event>`
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Aaa.Accounting.Events, self).__init__()

                    self.yang_name = "events"
                    self.yang_parent_name = "accounting"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("event", ("event", System.Aaa.Accounting.Events.Event))])
                    self._leafs = OrderedDict()

                    self.event = YList(self)
                    self._segment_path = lambda: "events"
                    self._absolute_path = lambda: "openconfig-system:system/aaa/accounting/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Aaa.Accounting.Events, [], name, value)


                class Event(_Entity_):
                    """
                    List of events subject to accounting
                    
                    .. attribute:: event_type  (key)
                    
                    	Reference to the event\-type being logged at the accounting server
                    	**type**\:  :py:class:`AAAACCOUNTINGEVENTTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAACCOUNTINGEVENTTYPE>`
                    
                    .. attribute:: config
                    
                    	Configuration data for accounting events
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.Accounting.Events.Event.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for accounting events
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.Accounting.Events.Event.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Aaa.Accounting.Events.Event, self).__init__()

                        self.yang_name = "event"
                        self.yang_parent_name = "events"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['event_type']
                        self._child_classes = OrderedDict([("config", ("config", System.Aaa.Accounting.Events.Event.Config)), ("state", ("state", System.Aaa.Accounting.Events.Event.State))])
                        self._leafs = OrderedDict([
                            ('event_type', (YLeaf(YType.identityref, 'event-type'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAACCOUNTINGEVENTTYPE')])),
                        ])
                        self.event_type = None

                        self.config = System.Aaa.Accounting.Events.Event.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = System.Aaa.Accounting.Events.Event.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "event" + "[event-type='" + str(self.event_type) + "']"
                        self._absolute_path = lambda: "openconfig-system:system/aaa/accounting/events/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Aaa.Accounting.Events.Event, ['event_type'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data for accounting events
                        
                        .. attribute:: event_type
                        
                        	The type of activity to record at the AAA accounting server
                        	**type**\:  :py:class:`AAAACCOUNTINGEVENTTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAACCOUNTINGEVENTTYPE>`
                        
                        .. attribute:: record
                        
                        	Type of record to send to the accounting server for this activity type
                        	**type**\:  :py:class:`Record <ydk.models.openconfig.openconfig_system.System.Aaa.Accounting.Events.Event.Config.Record>`
                        
                        

                        """

                        _prefix = 'oc-sys'
                        _revision = '2018-07-17'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(System.Aaa.Accounting.Events.Event.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "event"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('event_type', (YLeaf(YType.identityref, 'event-type'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAACCOUNTINGEVENTTYPE')])),
                                ('record', (YLeaf(YType.enumeration, 'record'), [('ydk.models.openconfig.openconfig_system', 'System', 'Aaa.Accounting.Events.Event.Config.Record')])),
                            ])
                            self.event_type = None
                            self.record = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(System.Aaa.Accounting.Events.Event.Config, ['event_type', 'record'], name, value)

                        class Record(Enum):
                            """
                            Record (Enum Class)

                            Type of record to send to the accounting server for this

                            activity type

                            .. data:: START_STOP = 0

                            	Send START record to the accounting server at the

                            	beginning of the activity, and STOP record at the

                            	end of the activity.

                            .. data:: STOP = 1

                            	Send STOP record to the accounting server when the

                            	user activity completes

                            """

                            START_STOP = Enum.YLeaf(0, "START_STOP")

                            STOP = Enum.YLeaf(1, "STOP")




                    class State(_Entity_):
                        """
                        Operational state data for accounting events
                        
                        .. attribute:: event_type
                        
                        	The type of activity to record at the AAA accounting server
                        	**type**\:  :py:class:`AAAACCOUNTINGEVENTTYPE <ydk.models.openconfig.openconfig_aaa_types.AAAACCOUNTINGEVENTTYPE>`
                        
                        	**config**\: False
                        
                        .. attribute:: record
                        
                        	Type of record to send to the accounting server for this activity type
                        	**type**\:  :py:class:`Record <ydk.models.openconfig.openconfig_system.System.Aaa.Accounting.Events.Event.State.Record>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-sys'
                        _revision = '2018-07-17'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(System.Aaa.Accounting.Events.Event.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "event"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('event_type', (YLeaf(YType.identityref, 'event-type'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAAACCOUNTINGEVENTTYPE')])),
                                ('record', (YLeaf(YType.enumeration, 'record'), [('ydk.models.openconfig.openconfig_system', 'System', 'Aaa.Accounting.Events.Event.State.Record')])),
                            ])
                            self.event_type = None
                            self.record = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(System.Aaa.Accounting.Events.Event.State, ['event_type', 'record'], name, value)

                        class Record(Enum):
                            """
                            Record (Enum Class)

                            Type of record to send to the accounting server for this

                            activity type

                            .. data:: START_STOP = 0

                            	Send START record to the accounting server at the

                            	beginning of the activity, and STOP record at the

                            	end of the activity.

                            .. data:: STOP = 1

                            	Send STOP record to the accounting server when the

                            	user activity completes

                            """

                            START_STOP = Enum.YLeaf(0, "START_STOP")

                            STOP = Enum.YLeaf(1, "STOP")







        class ServerGroups(_Entity_):
            """
            Enclosing container for AAA server groups
            
            .. attribute:: server_group
            
            	List of AAA server groups.  All servers in a group must have the same type as indicated by the server type
            	**type**\: list of  		 :py:class:`ServerGroup <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup>`
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Aaa.ServerGroups, self).__init__()

                self.yang_name = "server-groups"
                self.yang_parent_name = "aaa"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("server-group", ("server_group", System.Aaa.ServerGroups.ServerGroup))])
                self._leafs = OrderedDict()

                self.server_group = YList(self)
                self._segment_path = lambda: "server-groups"
                self._absolute_path = lambda: "openconfig-system:system/aaa/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Aaa.ServerGroups, [], name, value)


            class ServerGroup(_Entity_):
                """
                List of AAA server groups.  All servers in a group
                must have the same type as indicated by the server
                type.
                
                .. attribute:: name  (key)
                
                	Reference to configured name of the server group
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Config>`
                
                .. attribute:: config
                
                	Configuration data for each server group
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Config>`
                
                .. attribute:: state
                
                	Operational state data for each server group
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.State>`
                
                	**config**\: False
                
                .. attribute:: servers
                
                	Enclosing container the list of servers
                	**type**\:  :py:class:`Servers <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers>`
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Aaa.ServerGroups.ServerGroup, self).__init__()

                    self.yang_name = "server-group"
                    self.yang_parent_name = "server-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("config", ("config", System.Aaa.ServerGroups.ServerGroup.Config)), ("state", ("state", System.Aaa.ServerGroups.ServerGroup.State)), ("servers", ("servers", System.Aaa.ServerGroups.ServerGroup.Servers))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.config = System.Aaa.ServerGroups.ServerGroup.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = System.Aaa.ServerGroups.ServerGroup.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"

                    self.servers = System.Aaa.ServerGroups.ServerGroup.Servers()
                    self.servers.parent = self
                    self._children_name_map["servers"] = "servers"
                    self._segment_path = lambda: "server-group" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "openconfig-system:system/aaa/server-groups/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Aaa.ServerGroups.ServerGroup, ['name'], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for each server group
                    
                    .. attribute:: name
                    
                    	Name for the server group
                    	**type**\: str
                    
                    .. attribute:: type
                    
                    	AAA server type \-\- all servers in the group must be of this type
                    	**type**\:  :py:class:`AAASERVERTYPE <ydk.models.openconfig.openconfig_aaa_types.AAASERVERTYPE>`
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Aaa.ServerGroups.ServerGroup.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAASERVERTYPE')])),
                        ])
                        self.name = None
                        self.type = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Config, ['name', 'type'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for each server group
                    
                    .. attribute:: name
                    
                    	Name for the server group
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: type
                    
                    	AAA server type \-\- all servers in the group must be of this type
                    	**type**\:  :py:class:`AAASERVERTYPE <ydk.models.openconfig.openconfig_aaa_types.AAASERVERTYPE>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Aaa.ServerGroups.ServerGroup.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_aaa_types', 'AAASERVERTYPE')])),
                        ])
                        self.name = None
                        self.type = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.State, ['name', 'type'], name, value)



                class Servers(_Entity_):
                    """
                    Enclosing container the list of servers
                    
                    .. attribute:: server
                    
                    	List of AAA servers
                    	**type**\: list of  		 :py:class:`Server <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers.Server>`
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Aaa.ServerGroups.ServerGroup.Servers, self).__init__()

                        self.yang_name = "servers"
                        self.yang_parent_name = "server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("server", ("server", System.Aaa.ServerGroups.ServerGroup.Servers.Server))])
                        self._leafs = OrderedDict()

                        self.server = YList(self)
                        self._segment_path = lambda: "servers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Servers, [], name, value)


                    class Server(_Entity_):
                        """
                        List of AAA servers
                        
                        .. attribute:: address  (key)
                        
                        	Reference to the configured address of the AAA server
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**refers to**\:  :py:class:`address <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers.Server.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration data 
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers.Server.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data 
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers.Server.State>`
                        
                        	**config**\: False
                        
                        .. attribute:: tacacs
                        
                        	Top\-level container for TACACS+ server data
                        	**type**\:  :py:class:`Tacacs <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs>`
                        
                        .. attribute:: radius
                        
                        	Top\-level container for RADIUS server data
                        	**type**\:  :py:class:`Radius <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius>`
                        
                        

                        """

                        _prefix = 'oc-sys'
                        _revision = '2018-07-17'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(System.Aaa.ServerGroups.ServerGroup.Servers.Server, self).__init__()

                            self.yang_name = "server"
                            self.yang_parent_name = "servers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address']
                            self._child_classes = OrderedDict([("config", ("config", System.Aaa.ServerGroups.ServerGroup.Servers.Server.Config)), ("state", ("state", System.Aaa.ServerGroups.ServerGroup.Servers.Server.State)), ("tacacs", ("tacacs", System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs)), ("radius", ("radius", System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius))])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ])
                            self.address = None

                            self.config = System.Aaa.ServerGroups.ServerGroup.Servers.Server.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = System.Aaa.ServerGroups.ServerGroup.Servers.Server.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"

                            self.tacacs = System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs()
                            self.tacacs.parent = self
                            self._children_name_map["tacacs"] = "tacacs"

                            self.radius = System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius()
                            self.radius.parent = self
                            self._children_name_map["radius"] = "radius"
                            self._segment_path = lambda: "server" + "[address='" + str(self.address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Servers.Server, ['address'], name, value)


                        class Config(_Entity_):
                            """
                            Configuration data 
                            
                            .. attribute:: name
                            
                            	Name assigned to the server
                            	**type**\: str
                            
                            .. attribute:: address
                            
                            	Address of the authentication server
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                            
                            .. attribute:: timeout
                            
                            	Set the timeout in seconds on responses from the AAA server
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-sys'
                            _revision = '2018-07-17'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                    ('timeout', (YLeaf(YType.uint16, 'timeout'), ['int'])),
                                ])
                                self.name = None
                                self.address = None
                                self.timeout = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Config, ['name', 'address', 'timeout'], name, value)



                        class State(_Entity_):
                            """
                            Operational state data 
                            
                            .. attribute:: name
                            
                            	Name assigned to the server
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: address
                            
                            	Address of the authentication server
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                            
                            	**config**\: False
                            
                            .. attribute:: timeout
                            
                            	Set the timeout in seconds on responses from the AAA server
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            	**units**\: seconds
                            
                            .. attribute:: connection_opens
                            
                            	Number of new connection requests sent to the server, e.g. socket open
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: connection_closes
                            
                            	Number of connection close requests sent to the server, e.g. socket close
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: connection_aborts
                            
                            	Number of aborted connections to the server.  These do not include connections that are close gracefully
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: connection_failures
                            
                            	Number of connection failures to the server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: connection_timeouts
                            
                            	Number of connection timeouts to the server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: messages_sent
                            
                            	Number of messages sent to the server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: messages_received
                            
                            	Number of messages received by the server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: errors_received
                            
                            	Number of error messages received from the server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-sys'
                            _revision = '2018-07-17'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(System.Aaa.ServerGroups.ServerGroup.Servers.Server.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                    ('timeout', (YLeaf(YType.uint16, 'timeout'), ['int'])),
                                    ('connection_opens', (YLeaf(YType.uint64, 'connection-opens'), ['int'])),
                                    ('connection_closes', (YLeaf(YType.uint64, 'connection-closes'), ['int'])),
                                    ('connection_aborts', (YLeaf(YType.uint64, 'connection-aborts'), ['int'])),
                                    ('connection_failures', (YLeaf(YType.uint64, 'connection-failures'), ['int'])),
                                    ('connection_timeouts', (YLeaf(YType.uint64, 'connection-timeouts'), ['int'])),
                                    ('messages_sent', (YLeaf(YType.uint64, 'messages-sent'), ['int'])),
                                    ('messages_received', (YLeaf(YType.uint64, 'messages-received'), ['int'])),
                                    ('errors_received', (YLeaf(YType.uint64, 'errors-received'), ['int'])),
                                ])
                                self.name = None
                                self.address = None
                                self.timeout = None
                                self.connection_opens = None
                                self.connection_closes = None
                                self.connection_aborts = None
                                self.connection_failures = None
                                self.connection_timeouts = None
                                self.messages_sent = None
                                self.messages_received = None
                                self.errors_received = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Servers.Server.State, ['name', 'address', 'timeout', 'connection_opens', 'connection_closes', 'connection_aborts', 'connection_failures', 'connection_timeouts', 'messages_sent', 'messages_received', 'errors_received'], name, value)



                        class Tacacs(_Entity_):
                            """
                            Top\-level container for TACACS+ server data
                            
                            .. attribute:: config
                            
                            	Configuration data for TACACS+ server
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data for TACACS+ server
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs.State>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-sys'
                            _revision = '2018-07-17'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs, self).__init__()

                                self.yang_name = "tacacs"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("config", ("config", System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs.Config)), ("state", ("state", System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs.State))])
                                self._leafs = OrderedDict()

                                self.config = System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"

                                self.state = System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._segment_path = lambda: "tacacs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs, [], name, value)


                            class Config(_Entity_):
                                """
                                Configuration data for TACACS+ server
                                
                                .. attribute:: port
                                
                                	The port number on which to contact the TACACS server
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**default value**\: 49
                                
                                .. attribute:: secret_key
                                
                                	The unencrypted shared key used between the authentication server and the device
                                	**type**\: str
                                
                                .. attribute:: source_address
                                
                                	Source IP address to use in messages to the TACACS server
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                                
                                

                                """

                                _prefix = 'oc-sys'
                                _revision = '2018-07-17'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "tacacs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                                        ('secret_key', (YLeaf(YType.str, 'secret-key'), ['str'])),
                                        ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ])
                                    self.port = None
                                    self.secret_key = None
                                    self.source_address = None
                                    self._segment_path = lambda: "config"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs.Config, ['port', 'secret_key', 'source_address'], name, value)



                            class State(_Entity_):
                                """
                                Operational state data for TACACS+ server
                                
                                .. attribute:: port
                                
                                	The port number on which to contact the TACACS server
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                	**default value**\: 49
                                
                                .. attribute:: secret_key
                                
                                	The unencrypted shared key used between the authentication server and the device
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: source_address
                                
                                	Source IP address to use in messages to the TACACS server
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-sys'
                                _revision = '2018-07-17'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "tacacs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                                        ('secret_key', (YLeaf(YType.str, 'secret-key'), ['str'])),
                                        ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                    ])
                                    self.port = None
                                    self.secret_key = None
                                    self.source_address = None
                                    self._segment_path = lambda: "state"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Tacacs.State, ['port', 'secret_key', 'source_address'], name, value)




                        class Radius(_Entity_):
                            """
                            Top\-level container for RADIUS server data
                            
                            .. attribute:: config
                            
                            	Configuration data for RADIUS servers
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data for RADIUS servers
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.State>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-sys'
                            _revision = '2018-07-17'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius, self).__init__()

                                self.yang_name = "radius"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("config", ("config", System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.Config)), ("state", ("state", System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.State))])
                                self._leafs = OrderedDict()

                                self.config = System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"

                                self.state = System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._segment_path = lambda: "radius"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius, [], name, value)


                            class Config(_Entity_):
                                """
                                Configuration data for RADIUS servers
                                
                                .. attribute:: auth_port
                                
                                	Port number for authentication requests
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**default value**\: 1812
                                
                                .. attribute:: acct_port
                                
                                	Port number for accounting requests
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**default value**\: 1813
                                
                                .. attribute:: secret_key
                                
                                	The unencrypted shared key used between the authentication server and the device
                                	**type**\: str
                                
                                .. attribute:: source_address
                                
                                	Source IP address to use in messages to the RADIUS server
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                                
                                .. attribute:: retransmit_attempts
                                
                                	Number of times the system may resend a request to the RADIUS server when it is unresponsive
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'oc-sys'
                                _revision = '2018-07-17'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "radius"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('auth_port', (YLeaf(YType.uint16, 'auth-port'), ['int'])),
                                        ('acct_port', (YLeaf(YType.uint16, 'acct-port'), ['int'])),
                                        ('secret_key', (YLeaf(YType.str, 'secret-key'), ['str'])),
                                        ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                        ('retransmit_attempts', (YLeaf(YType.uint8, 'retransmit-attempts'), ['int'])),
                                    ])
                                    self.auth_port = None
                                    self.acct_port = None
                                    self.secret_key = None
                                    self.source_address = None
                                    self.retransmit_attempts = None
                                    self._segment_path = lambda: "config"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.Config, ['auth_port', 'acct_port', 'secret_key', 'source_address', 'retransmit_attempts'], name, value)



                            class State(_Entity_):
                                """
                                Operational state data for RADIUS servers
                                
                                .. attribute:: auth_port
                                
                                	Port number for authentication requests
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                	**default value**\: 1812
                                
                                .. attribute:: acct_port
                                
                                	Port number for accounting requests
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                	**config**\: False
                                
                                	**default value**\: 1813
                                
                                .. attribute:: secret_key
                                
                                	The unencrypted shared key used between the authentication server and the device
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: source_address
                                
                                	Source IP address to use in messages to the RADIUS server
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                                
                                	**config**\: False
                                
                                .. attribute:: retransmit_attempts
                                
                                	Number of times the system may resend a request to the RADIUS server when it is unresponsive
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: counters
                                
                                	A collection of RADIUS related state objects
                                	**type**\:  :py:class:`Counters <ydk.models.openconfig.openconfig_system.System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.State.Counters>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-sys'
                                _revision = '2018-07-17'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "radius"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("counters", ("counters", System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.State.Counters))])
                                    self._leafs = OrderedDict([
                                        ('auth_port', (YLeaf(YType.uint16, 'auth-port'), ['int'])),
                                        ('acct_port', (YLeaf(YType.uint16, 'acct-port'), ['int'])),
                                        ('secret_key', (YLeaf(YType.str, 'secret-key'), ['str'])),
                                        ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                        ('retransmit_attempts', (YLeaf(YType.uint8, 'retransmit-attempts'), ['int'])),
                                    ])
                                    self.auth_port = None
                                    self.acct_port = None
                                    self.secret_key = None
                                    self.source_address = None
                                    self.retransmit_attempts = None

                                    self.counters = System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.State.Counters()
                                    self.counters.parent = self
                                    self._children_name_map["counters"] = "counters"
                                    self._segment_path = lambda: "state"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.State, ['auth_port', 'acct_port', 'secret_key', 'source_address', 'retransmit_attempts'], name, value)


                                class Counters(_Entity_):
                                    """
                                    A collection of RADIUS related state objects.
                                    
                                    .. attribute:: retried_access_requests
                                    
                                    	Retransmitted Access\-Request messages
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: access_accepts
                                    
                                    	Received Access\-Accept messages
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: access_rejects
                                    
                                    	Received Access\-Reject messages
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: timeout_access_requests
                                    
                                    	Access\-Request messages that have timed\-out, requiring retransmission
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'oc-sys'
                                    _revision = '2018-07-17'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.State.Counters, self).__init__()

                                        self.yang_name = "counters"
                                        self.yang_parent_name = "state"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('retried_access_requests', (YLeaf(YType.uint64, 'retried-access-requests'), ['int'])),
                                            ('access_accepts', (YLeaf(YType.uint64, 'access-accepts'), ['int'])),
                                            ('access_rejects', (YLeaf(YType.uint64, 'access-rejects'), ['int'])),
                                            ('timeout_access_requests', (YLeaf(YType.uint64, 'timeout-access-requests'), ['int'])),
                                        ])
                                        self.retried_access_requests = None
                                        self.access_accepts = None
                                        self.access_rejects = None
                                        self.timeout_access_requests = None
                                        self._segment_path = lambda: "counters"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(System.Aaa.ServerGroups.ServerGroup.Servers.Server.Radius.State.Counters, ['retried_access_requests', 'access_accepts', 'access_rejects', 'timeout_access_requests'], name, value)










    class Memory(_Entity_):
        """
        Top\-level container for system memory data
        
        .. attribute:: config
        
        	Configuration data for system memory
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Memory.Config>`
        
        .. attribute:: state
        
        	Operational state data for system memory
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Memory.State>`
        
        	**config**\: False
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.Memory, self).__init__()

            self.yang_name = "memory"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("config", ("config", System.Memory.Config)), ("state", ("state", System.Memory.State))])
            self._leafs = OrderedDict()

            self.config = System.Memory.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.state = System.Memory.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"
            self._segment_path = lambda: "memory"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.Memory, [], name, value)


        class Config(_Entity_):
            """
            Configuration data for system memory
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Memory.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "memory"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict()
                self._segment_path = lambda: "config"
                self._absolute_path = lambda: "openconfig-system:system/memory/%s" % self._segment_path()
                self._is_frozen = True



        class State(_Entity_):
            """
            Operational state data for system memory
            
            .. attribute:: physical
            
            	Reports the total physical memory available on the system
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: reserved
            
            	Memory reserved for system use
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Memory.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "memory"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('physical', (YLeaf(YType.uint64, 'physical'), ['int'])),
                    ('reserved', (YLeaf(YType.uint64, 'reserved'), ['int'])),
                ])
                self.physical = None
                self.reserved = None
                self._segment_path = lambda: "state"
                self._absolute_path = lambda: "openconfig-system:system/memory/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Memory.State, ['physical', 'reserved'], name, value)




    class Cpus(_Entity_):
        """
        Enclosing container for the list of CPU cores on the
        system
        
        .. attribute:: cpu
        
        	List of CPU cores on the system (including logical CPUs on hyperthreaded systems), keyed by either a numerical index, or the ALL value for an entry representing the aggregation across all CPUs
        	**type**\: list of  		 :py:class:`Cpu <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu>`
        
        	**config**\: False
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.Cpus, self).__init__()

            self.yang_name = "cpus"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpu", ("cpu", System.Cpus.Cpu))])
            self._leafs = OrderedDict()

            self.cpu = YList(self)
            self._segment_path = lambda: "cpus"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.Cpus, [], name, value)


        class Cpu(_Entity_):
            """
            List of CPU cores on the system (including logical CPUs
            on hyperthreaded systems), keyed by either a numerical
            index, or the ALL value for an entry representing the
            aggregation across all CPUs.
            
            .. attribute:: index  (key)
            
            	Reference to list key
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`Index <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State.Index>`
            
            		**type**\: int
            
            			**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State>`
            
            	**config**\: False
            
            .. attribute:: state
            
            	Operational state data for the system CPU(s)
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Cpus.Cpu, self).__init__()

                self.yang_name = "cpu"
                self.yang_parent_name = "cpus"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['index']
                self._child_classes = OrderedDict([("state", ("state", System.Cpus.Cpu.State))])
                self._leafs = OrderedDict([
                    ('index', (YLeaf(YType.str, 'index'), ['str'])),
                ])
                self.index = None

                self.state = System.Cpus.Cpu.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "cpu" + "[index='" + str(self.index) + "']"
                self._absolute_path = lambda: "openconfig-system:system/cpus/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Cpus.Cpu, ['index'], name, value)


            class State(_Entity_):
                """
                Operational state data for the system CPU(s)
                
                .. attribute:: index
                
                	The CPU index for each processor core on the system.  On a single\-core system, the index should be zero.  The ALL index signifies an aggregation of the CPU utilization statistics over all cores in the system
                	**type**\: union of the below types:
                
                		**type**\:  :py:class:`Index <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State.Index>`
                
                		**type**\: int
                
                			**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: total
                
                	Total CPU utilization
                	**type**\:  :py:class:`Total <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State.Total>`
                
                	**config**\: False
                
                .. attribute:: user
                
                	Percentage of CPU time spent running in user space
                	**type**\:  :py:class:`User <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State.User>`
                
                	**config**\: False
                
                .. attribute:: kernel
                
                	Percentage of CPU time spent running in kernel space
                	**type**\:  :py:class:`Kernel <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State.Kernel>`
                
                	**config**\: False
                
                .. attribute:: nice
                
                	Percentage of CPU time spent running low\-priority (niced) user processes
                	**type**\:  :py:class:`Nice <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State.Nice>`
                
                	**config**\: False
                
                .. attribute:: idle
                
                	Percentage of CPU time spent idle
                	**type**\:  :py:class:`Idle <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State.Idle>`
                
                	**config**\: False
                
                .. attribute:: wait
                
                	Percentage of CPU time spent waiting for I/O
                	**type**\:  :py:class:`Wait <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State.Wait>`
                
                	**config**\: False
                
                .. attribute:: hardware_interrupt
                
                	Percentage of CPU time spent servicing hardware interrupts
                	**type**\:  :py:class:`HardwareInterrupt <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State.HardwareInterrupt>`
                
                	**config**\: False
                
                .. attribute:: software_interrupt
                
                	Percentage of CPU time spent servicing software interrupts
                	**type**\:  :py:class:`SoftwareInterrupt <ydk.models.openconfig.openconfig_system.System.Cpus.Cpu.State.SoftwareInterrupt>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Cpus.Cpu.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "cpu"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("total", ("total", System.Cpus.Cpu.State.Total)), ("user", ("user", System.Cpus.Cpu.State.User)), ("kernel", ("kernel", System.Cpus.Cpu.State.Kernel)), ("nice", ("nice", System.Cpus.Cpu.State.Nice)), ("idle", ("idle", System.Cpus.Cpu.State.Idle)), ("wait", ("wait", System.Cpus.Cpu.State.Wait)), ("hardware-interrupt", ("hardware_interrupt", System.Cpus.Cpu.State.HardwareInterrupt)), ("software-interrupt", ("software_interrupt", System.Cpus.Cpu.State.SoftwareInterrupt))])
                    self._leafs = OrderedDict([
                        ('index', (YLeaf(YType.str, 'index'), [('ydk.models.openconfig.openconfig_system', 'System', 'Cpus.Cpu.State.Index'),'int'])),
                    ])
                    self.index = None

                    self.total = System.Cpus.Cpu.State.Total()
                    self.total.parent = self
                    self._children_name_map["total"] = "total"

                    self.user = System.Cpus.Cpu.State.User()
                    self.user.parent = self
                    self._children_name_map["user"] = "user"

                    self.kernel = System.Cpus.Cpu.State.Kernel()
                    self.kernel.parent = self
                    self._children_name_map["kernel"] = "kernel"

                    self.nice = System.Cpus.Cpu.State.Nice()
                    self.nice.parent = self
                    self._children_name_map["nice"] = "nice"

                    self.idle = System.Cpus.Cpu.State.Idle()
                    self.idle.parent = self
                    self._children_name_map["idle"] = "idle"

                    self.wait = System.Cpus.Cpu.State.Wait()
                    self.wait.parent = self
                    self._children_name_map["wait"] = "wait"

                    self.hardware_interrupt = System.Cpus.Cpu.State.HardwareInterrupt()
                    self.hardware_interrupt.parent = self
                    self._children_name_map["hardware_interrupt"] = "hardware-interrupt"

                    self.software_interrupt = System.Cpus.Cpu.State.SoftwareInterrupt()
                    self.software_interrupt.parent = self
                    self._children_name_map["software_interrupt"] = "software-interrupt"
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Cpus.Cpu.State, ['index'], name, value)

                class Index(Enum):
                    """
                    Index (Enum Class)

                    The CPU index for each processor core on the system.  On a

                    single\-core system, the index should be zero.  The ALL

                    index signifies an aggregation of the CPU utilization

                    statistics over all cores in the system.

                    .. data:: ALL = 0

                    	Index value indicating all CPUs in the system

                    """

                    ALL = Enum.YLeaf(0, "ALL")



                class Total(_Entity_):
                    """
                    Total CPU utilization.
                    
                    .. attribute:: instant
                    
                    	The instantaneous percentage value
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Cpus.Cpu.State.Total, self).__init__()

                        self.yang_name = "total"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.uint8, 'instant'), ['int'])),
                            ('avg', (YLeaf(YType.uint8, 'avg'), ['int'])),
                            ('min', (YLeaf(YType.uint8, 'min'), ['int'])),
                            ('max', (YLeaf(YType.uint8, 'max'), ['int'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "total"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Cpus.Cpu.State.Total, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class User(_Entity_):
                    """
                    Percentage of CPU time spent running in user space.
                    
                    .. attribute:: instant
                    
                    	The instantaneous percentage value
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Cpus.Cpu.State.User, self).__init__()

                        self.yang_name = "user"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.uint8, 'instant'), ['int'])),
                            ('avg', (YLeaf(YType.uint8, 'avg'), ['int'])),
                            ('min', (YLeaf(YType.uint8, 'min'), ['int'])),
                            ('max', (YLeaf(YType.uint8, 'max'), ['int'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "user"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Cpus.Cpu.State.User, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class Kernel(_Entity_):
                    """
                    Percentage of CPU time spent running in kernel space.
                    
                    .. attribute:: instant
                    
                    	The instantaneous percentage value
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Cpus.Cpu.State.Kernel, self).__init__()

                        self.yang_name = "kernel"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.uint8, 'instant'), ['int'])),
                            ('avg', (YLeaf(YType.uint8, 'avg'), ['int'])),
                            ('min', (YLeaf(YType.uint8, 'min'), ['int'])),
                            ('max', (YLeaf(YType.uint8, 'max'), ['int'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "kernel"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Cpus.Cpu.State.Kernel, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class Nice(_Entity_):
                    """
                    Percentage of CPU time spent running low\-priority (niced)
                    user processes.
                    
                    .. attribute:: instant
                    
                    	The instantaneous percentage value
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Cpus.Cpu.State.Nice, self).__init__()

                        self.yang_name = "nice"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.uint8, 'instant'), ['int'])),
                            ('avg', (YLeaf(YType.uint8, 'avg'), ['int'])),
                            ('min', (YLeaf(YType.uint8, 'min'), ['int'])),
                            ('max', (YLeaf(YType.uint8, 'max'), ['int'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "nice"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Cpus.Cpu.State.Nice, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class Idle(_Entity_):
                    """
                    Percentage of CPU time spent idle.
                    
                    .. attribute:: instant
                    
                    	The instantaneous percentage value
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Cpus.Cpu.State.Idle, self).__init__()

                        self.yang_name = "idle"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.uint8, 'instant'), ['int'])),
                            ('avg', (YLeaf(YType.uint8, 'avg'), ['int'])),
                            ('min', (YLeaf(YType.uint8, 'min'), ['int'])),
                            ('max', (YLeaf(YType.uint8, 'max'), ['int'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "idle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Cpus.Cpu.State.Idle, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class Wait(_Entity_):
                    """
                    Percentage of CPU time spent waiting for I/O.
                    
                    .. attribute:: instant
                    
                    	The instantaneous percentage value
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Cpus.Cpu.State.Wait, self).__init__()

                        self.yang_name = "wait"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.uint8, 'instant'), ['int'])),
                            ('avg', (YLeaf(YType.uint8, 'avg'), ['int'])),
                            ('min', (YLeaf(YType.uint8, 'min'), ['int'])),
                            ('max', (YLeaf(YType.uint8, 'max'), ['int'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "wait"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Cpus.Cpu.State.Wait, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class HardwareInterrupt(_Entity_):
                    """
                    Percentage of CPU time spent servicing hardware interrupts.
                    
                    .. attribute:: instant
                    
                    	The instantaneous percentage value
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Cpus.Cpu.State.HardwareInterrupt, self).__init__()

                        self.yang_name = "hardware-interrupt"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.uint8, 'instant'), ['int'])),
                            ('avg', (YLeaf(YType.uint8, 'avg'), ['int'])),
                            ('min', (YLeaf(YType.uint8, 'min'), ['int'])),
                            ('max', (YLeaf(YType.uint8, 'max'), ['int'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "hardware-interrupt"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Cpus.Cpu.State.HardwareInterrupt, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class SoftwareInterrupt(_Entity_):
                    """
                    Percentage of CPU time spent servicing software interrupts
                    
                    .. attribute:: instant
                    
                    	The instantaneous percentage value
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-sys'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(System.Cpus.Cpu.State.SoftwareInterrupt, self).__init__()

                        self.yang_name = "software-interrupt"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.uint8, 'instant'), ['int'])),
                            ('avg', (YLeaf(YType.uint8, 'avg'), ['int'])),
                            ('min', (YLeaf(YType.uint8, 'min'), ['int'])),
                            ('max', (YLeaf(YType.uint8, 'max'), ['int'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "software-interrupt"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(System.Cpus.Cpu.State.SoftwareInterrupt, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)






    class Processes(_Entity_):
        """
        Parameters related to all monitored processes
        
        .. attribute:: process
        
        	List of monitored processes
        	**type**\: list of  		 :py:class:`Process <ydk.models.openconfig.openconfig_system.System.Processes.Process>`
        
        	**config**\: False
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.Processes, self).__init__()

            self.yang_name = "processes"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("process", ("process", System.Processes.Process))])
            self._leafs = OrderedDict()

            self.process = YList(self)
            self._segment_path = lambda: "processes"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.Processes, [], name, value)


        class Process(_Entity_):
            """
            List of monitored processes
            
            .. attribute:: pid  (key)
            
            	Reference to the process pid key
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**refers to**\:  :py:class:`pid <ydk.models.openconfig.openconfig_system.System.Processes.Process.State>`
            
            	**config**\: False
            
            .. attribute:: state
            
            	State parameters related to monitored processes
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Processes.Process.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Processes.Process, self).__init__()

                self.yang_name = "process"
                self.yang_parent_name = "processes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pid']
                self._child_classes = OrderedDict([("state", ("state", System.Processes.Process.State))])
                self._leafs = OrderedDict([
                    ('pid', (YLeaf(YType.str, 'pid'), ['int'])),
                ])
                self.pid = None

                self.state = System.Processes.Process.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "process" + "[pid='" + str(self.pid) + "']"
                self._absolute_path = lambda: "openconfig-system:system/processes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Processes.Process, ['pid'], name, value)


            class State(_Entity_):
                """
                State parameters related to monitored processes
                
                .. attribute:: pid
                
                	The process pid
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: name
                
                	The process name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: args
                
                	Current process command line arguments.  Arguments with a parameter (e.g., \-\-option 10  or \-option=10) should be represented as a single element of the list with the argument name and parameter together.  Flag arguments, i.e., those without a parameter should also be in their own list element
                	**type**\: list of str
                
                	**config**\: False
                
                .. attribute:: start_time
                
                	The time at which this process started, reported as nanoseconds since the UNIX epoch.  The system must be synchronized such that the start\-time can be reported accurately, otherwise it should not be reported
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: ns
                
                .. attribute:: uptime
                
                	Amount of time elapsed since this process started
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: cpu_usage_user
                
                	CPU time consumed by this process in user mode
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: cpu_usage_system
                
                	CPU time consumed by this process in kernel mode
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: cpu_utilization
                
                	The percentage of CPU that is being used by the process
                	**type**\: int
                
                	**range:** 0..100
                
                	**config**\: False
                
                .. attribute:: memory_usage
                
                	Bytes allocated and still in use by the process
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: bytes
                
                .. attribute:: memory_utilization
                
                	The percentage of RAM that is being used by the process
                	**type**\: int
                
                	**range:** 0..100
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Processes.Process.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('pid', (YLeaf(YType.uint64, 'pid'), ['int'])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('args', (YLeafList(YType.str, 'args'), ['str'])),
                        ('start_time', (YLeaf(YType.uint64, 'start-time'), ['int'])),
                        ('uptime', (YLeaf(YType.uint64, 'uptime'), ['int'])),
                        ('cpu_usage_user', (YLeaf(YType.uint64, 'cpu-usage-user'), ['int'])),
                        ('cpu_usage_system', (YLeaf(YType.uint64, 'cpu-usage-system'), ['int'])),
                        ('cpu_utilization', (YLeaf(YType.uint8, 'cpu-utilization'), ['int'])),
                        ('memory_usage', (YLeaf(YType.uint64, 'memory-usage'), ['int'])),
                        ('memory_utilization', (YLeaf(YType.uint8, 'memory-utilization'), ['int'])),
                    ])
                    self.pid = None
                    self.name = None
                    self.args = []
                    self.start_time = None
                    self.uptime = None
                    self.cpu_usage_user = None
                    self.cpu_usage_system = None
                    self.cpu_utilization = None
                    self.memory_usage = None
                    self.memory_utilization = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Processes.Process.State, ['pid', 'name', 'args', 'start_time', 'uptime', 'cpu_usage_user', 'cpu_usage_system', 'cpu_utilization', 'memory_usage', 'memory_utilization'], name, value)





    class Alarms(_Entity_):
        """
        Top\-level container for device alarms
        
        .. attribute:: alarm
        
        	List of alarms, keyed by a unique id
        	**type**\: list of  		 :py:class:`Alarm <ydk.models.openconfig.openconfig_system.System.Alarms.Alarm>`
        
        	**config**\: False
        
        

        """

        _prefix = 'oc-sys'
        _revision = '2018-07-17'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(System.Alarms, self).__init__()

            self.yang_name = "alarms"
            self.yang_parent_name = "system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("alarm", ("alarm", System.Alarms.Alarm))])
            self._leafs = OrderedDict()

            self.alarm = YList(self)
            self._segment_path = lambda: "alarms"
            self._absolute_path = lambda: "openconfig-system:system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(System.Alarms, [], name, value)


        class Alarm(_Entity_):
            """
            List of alarms, keyed by a unique id
            
            .. attribute:: id  (key)
            
            	References the unique alarm id
            	**type**\: str
            
            	**refers to**\:  :py:class:`id <ydk.models.openconfig.openconfig_system.System.Alarms.Alarm.State>`
            
            	**config**\: False
            
            .. attribute:: config
            
            	Configuration data for each alarm
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_system.System.Alarms.Alarm.Config>`
            
            	**config**\: False
            
            .. attribute:: state
            
            	Operational state data for a device alarm
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_system.System.Alarms.Alarm.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-sys'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(System.Alarms.Alarm, self).__init__()

                self.yang_name = "alarm"
                self.yang_parent_name = "alarms"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_classes = OrderedDict([("config", ("config", System.Alarms.Alarm.Config)), ("state", ("state", System.Alarms.Alarm.State))])
                self._leafs = OrderedDict([
                    ('id', (YLeaf(YType.str, 'id'), ['str'])),
                ])
                self.id = None

                self.config = System.Alarms.Alarm.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = System.Alarms.Alarm.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "alarm" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "openconfig-system:system/alarms/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(System.Alarms.Alarm, ['id'], name, value)


            class Config(_Entity_):
                """
                Configuration data for each alarm
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Alarms.Alarm.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "alarm"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"
                    self._is_frozen = True



            class State(_Entity_):
                """
                Operational state data for a device alarm
                
                .. attribute:: id
                
                	Unique ID for the alarm \-\- this will not be a configurable parameter on many implementations
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: resource
                
                	The item that is under alarm within the device. The resource may be a reference to an item which is defined elsewhere in the model. For example, it may be a platform/component, interfaces/interface, terminal\-device/logical\-channels/channel, etc. In this case the system should match the name of the referenced item exactly. The referenced item could alternatively be the path of the item within the model
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: text
                
                	The string used to inform operators about the alarm. This MUST contain enough information for an operator to be able to understand the problem. If this string contains structure, this format should be clearly documented for programs to be able to parse that information
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: time_created
                
                	The time at which the alarm was raised by the system. This value is expressed as nanoseconds since the Unix Epoch
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: severity
                
                	The severity level indicating the criticality and impact of the alarm
                	**type**\:  :py:class:`OPENCONFIGALARMSEVERITY <ydk.models.openconfig.openconfig_alarm_types.OPENCONFIGALARMSEVERITY>`
                
                	**config**\: False
                
                .. attribute:: type_id
                
                	The abbreviated name of the alarm, for example LOS, EQPT, or OTS. Also referred to in different systems as condition type, alarm identifier, or alarm mnemonic. It is recommended to use the OPENCONFIG\_ALARM\_TYPE\_ID identities where possible and only use the string type when the desired identityref is not yet defined
                	**type**\: union of the below types:
                
                		**type**\: str
                
                		**type**\:  :py:class:`OPENCONFIGALARMTYPEID <ydk.models.openconfig.openconfig_alarm_types.OPENCONFIGALARMTYPEID>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-sys'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(System.Alarms.Alarm.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "alarm"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('id', (YLeaf(YType.str, 'id'), ['str'])),
                        ('resource', (YLeaf(YType.str, 'resource'), ['str'])),
                        ('text', (YLeaf(YType.str, 'text'), ['str'])),
                        ('time_created', (YLeaf(YType.uint64, 'time-created'), ['int'])),
                        ('severity', (YLeaf(YType.identityref, 'severity'), [('ydk.models.openconfig.openconfig_alarm_types', 'OPENCONFIGALARMSEVERITY')])),
                        ('type_id', (YLeaf(YType.str, 'type-id'), ['str',('ydk.models.openconfig.openconfig_alarm_types', 'OPENCONFIGALARMTYPEID')])),
                    ])
                    self.id = None
                    self.resource = None
                    self.text = None
                    self.time_created = None
                    self.severity = None
                    self.type_id = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(System.Alarms.Alarm.State, ['id', 'resource', 'text', 'time_created', 'severity', 'type_id'], name, value)




    def clone_ptr(self):
        self._top_entity = System()
        return self._top_entity



class NTPAUTHMD5(NTPAUTHTYPE):
    """
    MD5 encryption method
    
    

    """

    _prefix = 'oc-sys'
    _revision = '2018-07-17'

    def __init__(self, ns="http://openconfig.net/yang/system", pref="openconfig-system", tag="openconfig-system:NTP_AUTH_MD5"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(NTPAUTHMD5, self).__init__(ns, pref, tag)



