""" tailf_confd_monitoring 

This module defines status objects for monitoring of ConfD.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ConfdState(Entity):
    """
    
    
    .. attribute:: cli
    
    	
    	**type**\:   :py:class:`Cli <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Cli>`
    
    	**presence node**\: True
    
    .. attribute:: daemon_status
    
    	
    	**type**\:   :py:class:`DaemonStatus <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.DaemonStatus>`
    
    .. attribute:: epoll
    
    	Indicates whether an enhanced poll() function is used
    	**type**\:  bool
    
    .. attribute:: ha
    
    	
    	**type**\:   :py:class:`Ha <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Ha>`
    
    	**presence node**\: True
    
    .. attribute:: internal
    
    	
    	**type**\:   :py:class:`Internal <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal>`
    
    .. attribute:: loaded_data_models
    
    	
    	**type**\:   :py:class:`LoadedDataModels <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.LoadedDataModels>`
    
    .. attribute:: netconf
    
    	
    	**type**\:   :py:class:`Netconf <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Netconf>`
    
    	**presence node**\: True
    
    .. attribute:: read_only_mode
    
    	
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: rest
    
    	
    	**type**\:   :py:class:`Rest <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Rest>`
    
    	**presence node**\: True
    
    .. attribute:: smp
    
    	
    	**type**\:   :py:class:`Smp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Smp>`
    
    	**presence node**\: True
    
    .. attribute:: snmp
    
    	
    	**type**\:   :py:class:`Snmp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Snmp>`
    
    	**presence node**\: True
    
    .. attribute:: upgrade_mode
    
    	Note that if the node is in upgrade mode, it is not possible to get any information from the system over NETCONF. The error\-app\-tag will be upgrade\-in\-progress.  Existing CLI sessions can get system information
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: version
    
    	Tail\-f product version number
    	**type**\:  str
    
    .. attribute:: webui
    
    	
    	**type**\:   :py:class:`Webui <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Webui>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'tfcm'
    _revision = '2013-06-14'

    def __init__(self):
        super(ConfdState, self).__init__()
        self._top_entity = None

        self.yang_name = "confd-state"
        self.yang_parent_name = "tailf-confd-monitoring"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"cli" : ("cli", ConfdState.Cli), "ha" : ("ha", ConfdState.Ha), "internal" : ("internal", ConfdState.Internal), "loaded-data-models" : ("loaded_data_models", ConfdState.LoadedDataModels), "netconf" : ("netconf", ConfdState.Netconf), "rest" : ("rest", ConfdState.Rest), "smp" : ("smp", ConfdState.Smp), "snmp" : ("snmp", ConfdState.Snmp), "webui" : ("webui", ConfdState.Webui)}
        self._child_list_classes = {}

        self.daemon_status = YLeaf(YType.enumeration, "daemon-status")

        self.epoll = YLeaf(YType.boolean, "epoll")

        self.read_only_mode = YLeaf(YType.empty, "read-only-mode")

        self.upgrade_mode = YLeaf(YType.empty, "upgrade-mode")

        self.version = YLeaf(YType.str, "version")

        self.cli = None
        self._children_name_map["cli"] = "cli"
        self._children_yang_names.add("cli")

        self.ha = None
        self._children_name_map["ha"] = "ha"
        self._children_yang_names.add("ha")

        self.internal = ConfdState.Internal()
        self.internal.parent = self
        self._children_name_map["internal"] = "internal"
        self._children_yang_names.add("internal")

        self.loaded_data_models = ConfdState.LoadedDataModels()
        self.loaded_data_models.parent = self
        self._children_name_map["loaded_data_models"] = "loaded-data-models"
        self._children_yang_names.add("loaded-data-models")

        self.netconf = None
        self._children_name_map["netconf"] = "netconf"
        self._children_yang_names.add("netconf")

        self.rest = None
        self._children_name_map["rest"] = "rest"
        self._children_yang_names.add("rest")

        self.smp = None
        self._children_name_map["smp"] = "smp"
        self._children_yang_names.add("smp")

        self.snmp = None
        self._children_name_map["snmp"] = "snmp"
        self._children_yang_names.add("snmp")

        self.webui = None
        self._children_name_map["webui"] = "webui"
        self._children_yang_names.add("webui")
        self._segment_path = lambda: "tailf-confd-monitoring:confd-state"

    def __setattr__(self, name, value):
        self._perform_setattr(ConfdState, ['daemon_status', 'epoll', 'read_only_mode', 'upgrade_mode', 'version'], name, value)

    class DaemonStatus(Enum):
        """
        DaemonStatus

        .. data:: starting = 0

        	The daemon is starting up.

        .. data:: phase0 = 1

        	The daemon is running in start phase 0.

        .. data:: phase1 = 2

        	The daemon is running in start phase 1.

        .. data:: started = 3

        	The daemon is started.

        .. data:: stopping = 4

        	The daemon is stopping.

        """

        starting = Enum.YLeaf(0, "starting")

        phase0 = Enum.YLeaf(1, "phase0")

        phase1 = Enum.YLeaf(2, "phase1")

        started = Enum.YLeaf(3, "started")

        stopping = Enum.YLeaf(4, "stopping")



    class Cli(Entity):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the CLI server is listening on.  In addition to the SSH addresses listen below, the CLI can always be invoked through the daemons IPC port.  Note that other mechanisms can be put in front of the IPC port, e.g., an OpenSSH server.  Such mechanisms are not known to the daemon and not listed here
        	**type**\:   :py:class:`Listen <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Cli.Listen>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            super(ConfdState.Cli, self).__init__()

            self.yang_name = "cli"
            self.yang_parent_name = "confd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"listen" : ("listen", ConfdState.Cli.Listen)}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.listen = ConfdState.Cli.Listen()
            self.listen.parent = self
            self._children_name_map["listen"] = "listen"
            self._children_yang_names.add("listen")
            self._segment_path = lambda: "cli"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()


        class Listen(Entity):
            """
            The transport addresses the CLI server is listening on.
            
            In addition to the SSH addresses listen below, the CLI can
            always be invoked through the daemons IPC port.
            
            Note that other mechanisms can be put in front of the IPC
            port, e.g., an OpenSSH server.  Such mechanisms are not
            known to the daemon and not listed here.
            
            .. attribute:: ssh
            
            	
            	**type**\: list of    :py:class:`Ssh <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Cli.Listen.Ssh>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Cli.Listen, self).__init__()

                self.yang_name = "listen"
                self.yang_parent_name = "cli"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"ssh" : ("ssh", ConfdState.Cli.Listen.Ssh)}

                self.ssh = YList(self)
                self._segment_path = lambda: "listen"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/cli/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Cli.Listen, [], name, value)


            class Ssh(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Cli.Listen.Ssh, self).__init__()

                    self.yang_name = "ssh"
                    self.yang_parent_name = "listen"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")
                    self._segment_path = lambda: "ssh"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/cli/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Cli.Listen.Ssh, ['ip', 'port'], name, value)


    class Ha(Entity):
        """
        
        
        .. attribute:: connected_slave
        
        	The node identifiers of the currently connected slaves
        	**type**\:  list of str
        
        .. attribute:: master_node_id
        
        	The node identifier of this node's parent node. This is the HA cluster's master node unless relay slaves are used
        	**type**\:  str
        
        .. attribute:: mode
        
        	The current HA mode of the node in the HA cluster
        	**type**\:   :py:class:`Mode <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Ha.Mode>`
        
        .. attribute:: node_id
        
        	The node identifier of this node in the HA cluster
        	**type**\:  str
        
        .. attribute:: pending_slave
        
        	The node identifiers of slaves with pending acknowledgement of synchronous replication
        	**type**\:  list of str
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            super(ConfdState.Ha, self).__init__()

            self.yang_name = "ha"
            self.yang_parent_name = "confd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.connected_slave = YLeafList(YType.str, "connected-slave")

            self.master_node_id = YLeaf(YType.str, "master-node-id")

            self.mode = YLeaf(YType.enumeration, "mode")

            self.node_id = YLeaf(YType.str, "node-id")

            self.pending_slave = YLeafList(YType.str, "pending-slave")
            self._segment_path = lambda: "ha"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ConfdState.Ha, ['connected_slave', 'master_node_id', 'mode', 'node_id', 'pending_slave'], name, value)

        class Mode(Enum):
            """
            Mode

            The current HA mode of the node in the HA cluster.

            .. data:: none = 0

            .. data:: slave = 1

            .. data:: master = 2

            .. data:: relay_slave = 3

            """

            none = Enum.YLeaf(0, "none")

            slave = Enum.YLeaf(1, "slave")

            master = Enum.YLeaf(2, "master")

            relay_slave = Enum.YLeaf(3, "relay-slave")



    class Internal(Entity):
        """
        
        
        .. attribute:: callpoints
        
        	
        	**type**\:   :py:class:`Callpoints <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints>`
        
        .. attribute:: cdb
        
        	
        	**type**\:   :py:class:`Cdb <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb>`
        
        

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            super(ConfdState.Internal, self).__init__()

            self.yang_name = "internal"
            self.yang_parent_name = "confd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"callpoints" : ("callpoints", ConfdState.Internal.Callpoints), "cdb" : ("cdb", ConfdState.Internal.Cdb)}
            self._child_list_classes = {}

            self.callpoints = ConfdState.Internal.Callpoints()
            self.callpoints.parent = self
            self._children_name_map["callpoints"] = "callpoints"
            self._children_yang_names.add("callpoints")

            self.cdb = ConfdState.Internal.Cdb()
            self.cdb.parent = self
            self._children_name_map["cdb"] = "cdb"
            self._children_yang_names.add("cdb")
            self._segment_path = lambda: "internal"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()

        class DatastoreName(Enum):
            """
            DatastoreName

            Name of one of the datastores implemented by CDB.

            .. data:: running = 0

            .. data:: startup = 1

            .. data:: operational = 2

            """

            running = Enum.YLeaf(0, "running")

            startup = Enum.YLeaf(1, "startup")

            operational = Enum.YLeaf(2, "operational")



        class Callpoints(Entity):
            """
            
            
            .. attribute:: actionpoint
            
            	
            	**type**\: list of    :py:class:`Actionpoint <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint>`
            
            .. attribute:: authentication_callback
            
            	
            	**type**\:   :py:class:`AuthenticationCallback <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback>`
            
            	**presence node**\: True
            
            .. attribute:: authorization_callbacks
            
            	
            	**type**\:   :py:class:`AuthorizationCallbacks <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks>`
            
            	**presence node**\: True
            
            .. attribute:: callpoint
            
            	
            	**type**\: list of    :py:class:`Callpoint <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint>`
            
            .. attribute:: error_formatting_callback
            
            	
            	**type**\: list of    :py:class:`ErrorFormattingCallback <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback>`
            
            .. attribute:: notification_stream_replay
            
            	
            	**type**\: list of    :py:class:`NotificationStreamReplay <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay>`
            
            .. attribute:: snmp_inform_callback
            
            	
            	**type**\: list of    :py:class:`SnmpInformCallback <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback>`
            
            .. attribute:: snmp_notification_subscription
            
            	
            	**type**\: list of    :py:class:`SnmpNotificationSubscription <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription>`
            
            .. attribute:: typepoint
            
            	
            	**type**\: list of    :py:class:`Typepoint <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint>`
            
            .. attribute:: validationpoint
            
            	
            	**type**\: list of    :py:class:`Validationpoint <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Internal.Callpoints, self).__init__()

                self.yang_name = "callpoints"
                self.yang_parent_name = "internal"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"authentication-callback" : ("authentication_callback", ConfdState.Internal.Callpoints.AuthenticationCallback), "authorization-callbacks" : ("authorization_callbacks", ConfdState.Internal.Callpoints.AuthorizationCallbacks)}
                self._child_list_classes = {"actionpoint" : ("actionpoint", ConfdState.Internal.Callpoints.Actionpoint), "callpoint" : ("callpoint", ConfdState.Internal.Callpoints.Callpoint), "error-formatting-callback" : ("error_formatting_callback", ConfdState.Internal.Callpoints.ErrorFormattingCallback), "notification-stream-replay" : ("notification_stream_replay", ConfdState.Internal.Callpoints.NotificationStreamReplay), "snmp-inform-callback" : ("snmp_inform_callback", ConfdState.Internal.Callpoints.SnmpInformCallback), "snmp-notification-subscription" : ("snmp_notification_subscription", ConfdState.Internal.Callpoints.SnmpNotificationSubscription), "typepoint" : ("typepoint", ConfdState.Internal.Callpoints.Typepoint), "validationpoint" : ("validationpoint", ConfdState.Internal.Callpoints.Validationpoint)}

                self.authentication_callback = None
                self._children_name_map["authentication_callback"] = "authentication-callback"
                self._children_yang_names.add("authentication-callback")

                self.authorization_callbacks = None
                self._children_name_map["authorization_callbacks"] = "authorization-callbacks"
                self._children_yang_names.add("authorization-callbacks")

                self.actionpoint = YList(self)
                self.callpoint = YList(self)
                self.error_formatting_callback = YList(self)
                self.notification_stream_replay = YList(self)
                self.snmp_inform_callback = YList(self)
                self.snmp_notification_subscription = YList(self)
                self.typepoint = YList(self)
                self.validationpoint = YList(self)
                self._segment_path = lambda: "callpoints"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Internal.Callpoints, [], name, value)


            class Actionpoint(Entity):
                """
                
                
                .. attribute:: id  <key>
                
                	Callpoint id
                	**type**\:  str
                
                .. attribute:: daemon
                
                	
                	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Error>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\:  str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\:  str
                
                .. attribute:: range
                
                	
                	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.Actionpoint, self).__init__()

                    self.yang_name = "actionpoint"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.Actionpoint.Daemon)}
                    self._child_list_classes = {"range" : ("range", ConfdState.Internal.Callpoints.Actionpoint.Range)}

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.Actionpoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "actionpoint" + "[id='" + self.id.get() + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.Actionpoint, ['id', 'error', 'file', 'path'], name, value)

                class Error(Enum):
                    """
                    Error

                    If this leaf exists, there is a problem

                    with the callpoint registration.

                    .. data:: NOT_REGISTERED = 0

                    	This value means that there is no registration

                    	for the callpoint.

                    .. data:: UNKNOWN = 1

                    	This value means that the callpoint does not exist,

                    	but there is a registration for it.

                    """

                    NOT_REGISTERED = Enum.YLeaf(0, "NOT-REGISTERED")

                    UNKNOWN = Enum.YLeaf(1, "UNKNOWN")



                class Daemon(Entity):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Daemon.Error>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Actionpoint.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "actionpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Actionpoint.Daemon, ['error', 'id', 'name'], name, value)

                    class Error(Enum):
                        """
                        Error

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Actionpoint.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "actionpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon)}
                        self._child_list_classes = {}

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Actionpoint.Range, ['default', 'lower', 'upper'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon.Error>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon, ['error', 'id', 'name'], name, value)

                        class Error(Enum):
                            """
                            Error

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class AuthenticationCallback(Entity):
                """
                
                
                .. attribute:: daemon
                
                	
                	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon>`
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Error>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\:  str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\:  str
                
                .. attribute:: range
                
                	
                	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Range>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.AuthenticationCallback, self).__init__()

                    self.yang_name = "authentication-callback"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon)}
                    self._child_list_classes = {"range" : ("range", ConfdState.Internal.Callpoints.AuthenticationCallback.Range)}
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "authentication-callback"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.AuthenticationCallback, ['enabled', 'error', 'file', 'path'], name, value)

                class Error(Enum):
                    """
                    Error

                    If this leaf exists, there is a problem

                    with the callpoint registration.

                    .. data:: NOT_REGISTERED = 0

                    	This value means that there is no registration

                    	for the callpoint.

                    .. data:: UNKNOWN = 1

                    	This value means that the callpoint does not exist,

                    	but there is a registration for it.

                    """

                    NOT_REGISTERED = Enum.YLeaf(0, "NOT-REGISTERED")

                    UNKNOWN = Enum.YLeaf(1, "UNKNOWN")



                class Daemon(Entity):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon.Error>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "authentication-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "daemon"
                        self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authentication-callback/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon, ['error', 'id', 'name'], name, value)

                    class Error(Enum):
                        """
                        Error

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.AuthenticationCallback.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "authentication-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon)}
                        self._child_list_classes = {}

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"
                        self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authentication-callback/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.AuthenticationCallback.Range, ['default', 'lower', 'upper'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon.Error>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "daemon"
                            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authentication-callback/range/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon, ['error', 'id', 'name'], name, value)

                        class Error(Enum):
                            """
                            Error

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class AuthorizationCallbacks(Entity):
                """
                
                
                .. attribute:: daemon
                
                	
                	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon>`
                
                .. attribute:: enabled
                
                	
                	**type**\:  bool
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Error>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\:  str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\:  str
                
                .. attribute:: range
                
                	
                	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.AuthorizationCallbacks, self).__init__()

                    self.yang_name = "authorization-callbacks"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon)}
                    self._child_list_classes = {"range" : ("range", ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range)}
                    self.is_presence_container = True

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "authorization-callbacks"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.AuthorizationCallbacks, ['enabled', 'error', 'file', 'path'], name, value)

                class Error(Enum):
                    """
                    Error

                    If this leaf exists, there is a problem

                    with the callpoint registration.

                    .. data:: NOT_REGISTERED = 0

                    	This value means that there is no registration

                    	for the callpoint.

                    .. data:: UNKNOWN = 1

                    	This value means that the callpoint does not exist,

                    	but there is a registration for it.

                    """

                    NOT_REGISTERED = Enum.YLeaf(0, "NOT-REGISTERED")

                    UNKNOWN = Enum.YLeaf(1, "UNKNOWN")



                class Daemon(Entity):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon.Error>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "authorization-callbacks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "daemon"
                        self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authorization-callbacks/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon, ['error', 'id', 'name'], name, value)

                    class Error(Enum):
                        """
                        Error

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "authorization-callbacks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon)}
                        self._child_list_classes = {}

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"
                        self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authorization-callbacks/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range, ['default', 'lower', 'upper'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon.Error>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "daemon"
                            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authorization-callbacks/range/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon, ['error', 'id', 'name'], name, value)

                        class Error(Enum):
                            """
                            Error

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class Callpoint(Entity):
                """
                
                
                .. attribute:: id  <key>
                
                	Callpoint id
                	**type**\:  str
                
                .. attribute:: daemon
                
                	
                	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Error>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\:  str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\:  str
                
                .. attribute:: range
                
                	
                	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.Callpoint, self).__init__()

                    self.yang_name = "callpoint"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.Callpoint.Daemon)}
                    self._child_list_classes = {"range" : ("range", ConfdState.Internal.Callpoints.Callpoint.Range)}

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.Callpoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "callpoint" + "[id='" + self.id.get() + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.Callpoint, ['id', 'error', 'file', 'path'], name, value)

                class Error(Enum):
                    """
                    Error

                    If this leaf exists, there is a problem

                    with the callpoint registration.

                    .. data:: NOT_REGISTERED = 0

                    	This value means that there is no registration

                    	for the callpoint.

                    .. data:: UNKNOWN = 1

                    	This value means that the callpoint does not exist,

                    	but there is a registration for it.

                    """

                    NOT_REGISTERED = Enum.YLeaf(0, "NOT-REGISTERED")

                    UNKNOWN = Enum.YLeaf(1, "UNKNOWN")



                class Daemon(Entity):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Daemon.Error>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Callpoint.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "callpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Callpoint.Daemon, ['error', 'id', 'name'], name, value)

                    class Error(Enum):
                        """
                        Error

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Callpoint.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "callpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.Callpoint.Range.Daemon)}
                        self._child_list_classes = {}

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.Callpoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Callpoint.Range, ['default', 'lower', 'upper'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Range.Daemon.Error>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.Callpoint.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.Callpoint.Range.Daemon, ['error', 'id', 'name'], name, value)

                        class Error(Enum):
                            """
                            Error

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class ErrorFormattingCallback(Entity):
                """
                
                
                .. attribute:: id  <key>
                
                	Callpoint id
                	**type**\:  str
                
                .. attribute:: daemon
                
                	
                	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Error>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\:  str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\:  str
                
                .. attribute:: range
                
                	
                	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.ErrorFormattingCallback, self).__init__()

                    self.yang_name = "error-formatting-callback"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon)}
                    self._child_list_classes = {"range" : ("range", ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range)}

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "error-formatting-callback" + "[id='" + self.id.get() + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.ErrorFormattingCallback, ['id', 'error', 'file', 'path'], name, value)

                class Error(Enum):
                    """
                    Error

                    If this leaf exists, there is a problem

                    with the callpoint registration.

                    .. data:: NOT_REGISTERED = 0

                    	This value means that there is no registration

                    	for the callpoint.

                    .. data:: UNKNOWN = 1

                    	This value means that the callpoint does not exist,

                    	but there is a registration for it.

                    """

                    NOT_REGISTERED = Enum.YLeaf(0, "NOT-REGISTERED")

                    UNKNOWN = Enum.YLeaf(1, "UNKNOWN")



                class Daemon(Entity):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon.Error>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "error-formatting-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon, ['error', 'id', 'name'], name, value)

                    class Error(Enum):
                        """
                        Error

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "error-formatting-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon)}
                        self._child_list_classes = {}

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range, ['default', 'lower', 'upper'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon.Error>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon, ['error', 'id', 'name'], name, value)

                        class Error(Enum):
                            """
                            Error

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class NotificationStreamReplay(Entity):
                """
                
                
                .. attribute:: name  <key>
                
                	Name of the notification stream
                	**type**\:  str
                
                .. attribute:: daemon
                
                	
                	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Error>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\:  str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\:  str
                
                .. attribute:: range
                
                	
                	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Range>`
                
                .. attribute:: replay_support
                
                	
                	**type**\:   :py:class:`ReplaySupport <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.ReplaySupport>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.NotificationStreamReplay, self).__init__()

                    self.yang_name = "notification-stream-replay"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon)}
                    self._child_list_classes = {"range" : ("range", ConfdState.Internal.Callpoints.NotificationStreamReplay.Range)}

                    self.name = YLeaf(YType.str, "name")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.replay_support = YLeaf(YType.enumeration, "replay-support")

                    self.daemon = ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "notification-stream-replay" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.NotificationStreamReplay, ['name', 'error', 'file', 'path', 'replay_support'], name, value)

                class Error(Enum):
                    """
                    Error

                    If this leaf exists, there is a problem

                    with the callpoint registration.

                    .. data:: NOT_REGISTERED = 0

                    	This value means that there is no registration

                    	for the callpoint.

                    .. data:: UNKNOWN = 1

                    	This value means that the callpoint does not exist,

                    	but there is a registration for it.

                    """

                    NOT_REGISTERED = Enum.YLeaf(0, "NOT-REGISTERED")

                    UNKNOWN = Enum.YLeaf(1, "UNKNOWN")


                class ReplaySupport(Enum):
                    """
                    ReplaySupport

                    .. data:: none = 0

                    .. data:: builtin = 1

                    .. data:: external = 2

                    """

                    none = Enum.YLeaf(0, "none")

                    builtin = Enum.YLeaf(1, "builtin")

                    external = Enum.YLeaf(2, "external")



                class Daemon(Entity):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon.Error>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "notification-stream-replay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon, ['error', 'id', 'name'], name, value)

                    class Error(Enum):
                        """
                        Error

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "notification-stream-replay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon)}
                        self._child_list_classes = {}

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range, ['default', 'lower', 'upper'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon.Error>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon, ['error', 'id', 'name'], name, value)

                        class Error(Enum):
                            """
                            Error

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class SnmpInformCallback(Entity):
                """
                
                
                .. attribute:: id  <key>
                
                	Callpoint id
                	**type**\:  str
                
                .. attribute:: daemon
                
                	
                	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Error>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\:  str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\:  str
                
                .. attribute:: range
                
                	
                	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.SnmpInformCallback, self).__init__()

                    self.yang_name = "snmp-inform-callback"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon)}
                    self._child_list_classes = {"range" : ("range", ConfdState.Internal.Callpoints.SnmpInformCallback.Range)}

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "snmp-inform-callback" + "[id='" + self.id.get() + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.SnmpInformCallback, ['id', 'error', 'file', 'path'], name, value)

                class Error(Enum):
                    """
                    Error

                    If this leaf exists, there is a problem

                    with the callpoint registration.

                    .. data:: NOT_REGISTERED = 0

                    	This value means that there is no registration

                    	for the callpoint.

                    .. data:: UNKNOWN = 1

                    	This value means that the callpoint does not exist,

                    	but there is a registration for it.

                    """

                    NOT_REGISTERED = Enum.YLeaf(0, "NOT-REGISTERED")

                    UNKNOWN = Enum.YLeaf(1, "UNKNOWN")



                class Daemon(Entity):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon.Error>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "snmp-inform-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon, ['error', 'id', 'name'], name, value)

                    class Error(Enum):
                        """
                        Error

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.SnmpInformCallback.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "snmp-inform-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon)}
                        self._child_list_classes = {}

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.SnmpInformCallback.Range, ['default', 'lower', 'upper'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon.Error>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon, ['error', 'id', 'name'], name, value)

                        class Error(Enum):
                            """
                            Error

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class SnmpNotificationSubscription(Entity):
                """
                
                
                .. attribute:: id  <key>
                
                	Callpoint id
                	**type**\:  str
                
                .. attribute:: daemon
                
                	
                	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Error>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\:  str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\:  str
                
                .. attribute:: range
                
                	
                	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription, self).__init__()

                    self.yang_name = "snmp-notification-subscription"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon)}
                    self._child_list_classes = {"range" : ("range", ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range)}

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "snmp-notification-subscription" + "[id='" + self.id.get() + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.SnmpNotificationSubscription, ['id', 'error', 'file', 'path'], name, value)

                class Error(Enum):
                    """
                    Error

                    If this leaf exists, there is a problem

                    with the callpoint registration.

                    .. data:: NOT_REGISTERED = 0

                    	This value means that there is no registration

                    	for the callpoint.

                    .. data:: UNKNOWN = 1

                    	This value means that the callpoint does not exist,

                    	but there is a registration for it.

                    """

                    NOT_REGISTERED = Enum.YLeaf(0, "NOT-REGISTERED")

                    UNKNOWN = Enum.YLeaf(1, "UNKNOWN")



                class Daemon(Entity):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon.Error>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "snmp-notification-subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon, ['error', 'id', 'name'], name, value)

                    class Error(Enum):
                        """
                        Error

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "snmp-notification-subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon)}
                        self._child_list_classes = {}

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range, ['default', 'lower', 'upper'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon.Error>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon, ['error', 'id', 'name'], name, value)

                        class Error(Enum):
                            """
                            Error

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class Typepoint(Entity):
                """
                
                
                .. attribute:: id  <key>
                
                	Callpoint id
                	**type**\:  str
                
                .. attribute:: daemon
                
                	
                	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Error>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\:  str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\:  str
                
                .. attribute:: range
                
                	
                	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.Typepoint, self).__init__()

                    self.yang_name = "typepoint"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.Typepoint.Daemon)}
                    self._child_list_classes = {"range" : ("range", ConfdState.Internal.Callpoints.Typepoint.Range)}

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.Typepoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "typepoint" + "[id='" + self.id.get() + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.Typepoint, ['id', 'error', 'file', 'path'], name, value)

                class Error(Enum):
                    """
                    Error

                    If this leaf exists, there is a problem

                    with the callpoint registration.

                    .. data:: NOT_REGISTERED = 0

                    	This value means that there is no registration

                    	for the callpoint.

                    .. data:: UNKNOWN = 1

                    	This value means that the callpoint does not exist,

                    	but there is a registration for it.

                    """

                    NOT_REGISTERED = Enum.YLeaf(0, "NOT-REGISTERED")

                    UNKNOWN = Enum.YLeaf(1, "UNKNOWN")



                class Daemon(Entity):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Daemon.Error>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Typepoint.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "typepoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Typepoint.Daemon, ['error', 'id', 'name'], name, value)

                    class Error(Enum):
                        """
                        Error

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Typepoint.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "typepoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.Typepoint.Range.Daemon)}
                        self._child_list_classes = {}

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.Typepoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Typepoint.Range, ['default', 'lower', 'upper'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Range.Daemon.Error>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.Typepoint.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.Typepoint.Range.Daemon, ['error', 'id', 'name'], name, value)

                        class Error(Enum):
                            """
                            Error

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class Validationpoint(Entity):
                """
                
                
                .. attribute:: id  <key>
                
                	Callpoint id
                	**type**\:  str
                
                .. attribute:: daemon
                
                	
                	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Error>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\:  str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\:  str
                
                .. attribute:: range
                
                	
                	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.Validationpoint, self).__init__()

                    self.yang_name = "validationpoint"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.Validationpoint.Daemon)}
                    self._child_list_classes = {"range" : ("range", ConfdState.Internal.Callpoints.Validationpoint.Range)}

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.Validationpoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "validationpoint" + "[id='" + self.id.get() + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.Validationpoint, ['id', 'error', 'file', 'path'], name, value)

                class Error(Enum):
                    """
                    Error

                    If this leaf exists, there is a problem

                    with the callpoint registration.

                    .. data:: NOT_REGISTERED = 0

                    	This value means that there is no registration

                    	for the callpoint.

                    .. data:: UNKNOWN = 1

                    	This value means that the callpoint does not exist,

                    	but there is a registration for it.

                    """

                    NOT_REGISTERED = Enum.YLeaf(0, "NOT-REGISTERED")

                    UNKNOWN = Enum.YLeaf(1, "UNKNOWN")



                class Daemon(Entity):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Daemon.Error>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Validationpoint.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "validationpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Validationpoint.Daemon, ['error', 'id', 'name'], name, value)

                    class Error(Enum):
                        """
                        Error

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:   :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Validationpoint.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "validationpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"daemon" : ("daemon", ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon)}
                        self._child_list_classes = {}

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Validationpoint.Range, ['default', 'lower', 'upper'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon.Error>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon, ['error', 'id', 'name'], name, value)

                        class Error(Enum):
                            """
                            Error

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



        class Cdb(Entity):
            """
            
            
            .. attribute:: client
            
            	
            	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client>`
            
            .. attribute:: datastore
            
            	
            	**type**\: list of    :py:class:`Datastore <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Internal.Cdb, self).__init__()

                self.yang_name = "cdb"
                self.yang_parent_name = "internal"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"client" : ("client", ConfdState.Internal.Cdb.Client), "datastore" : ("datastore", ConfdState.Internal.Cdb.Datastore)}

                self.client = YList(self)
                self.datastore = YList(self)
                self._segment_path = lambda: "cdb"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Internal.Cdb, [], name, value)


            class Client(Entity):
                """
                
                
                .. attribute:: datastore
                
                	The name of the datastore when 'type' = 'client'. The value 'pre\_commit\_running' is the 'pseudo' datastore representing 'running' before a commit
                	**type**\: one of the below types:
                
                	**type**\:   :py:class:`DatastoreName <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.DatastoreName>`
                
                
                ----
                	**type**\:   :py:class:`Datastore <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Datastore>`
                
                
                ----
                .. attribute:: info
                
                	Additional information about the client obtained at connect time. If present, it consists of client PID and socket file descriptor number
                	**type**\:  str
                
                .. attribute:: lock
                
                	Set when 'type' = 'client' and the client has requested or acquired a lock on the datastore. The 'pending\-read' and 'pending\-subscription' values indicate that the client has requested but not yet acquired the corresponding lock. A 'read' lock is never taken for the 'operational' datastore, a 'subscription' lock is never taken for any other datastore than 'operational'
                	**type**\:   :py:class:`Lock <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Lock>`
                
                .. attribute:: name
                
                	The client name
                	**type**\:  str
                
                .. attribute:: subscription
                
                	
                	**type**\: list of    :py:class:`Subscription <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Subscription>`
                
                .. attribute:: type
                
                	The type of client\: 'inactive' is a client connection without any specific state. 'client' means that the client has an active session towards a datastore. A 'subscriber' has made one or more subscriptions. 'waiting' means that the client is waiting for completion of a call such as cdb\_wait\_start()
                	**type**\:   :py:class:`Type <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Type>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Cdb.Client, self).__init__()

                    self.yang_name = "client"
                    self.yang_parent_name = "cdb"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"subscription" : ("subscription", ConfdState.Internal.Cdb.Client.Subscription)}

                    self.datastore = YLeaf(YType.str, "datastore")

                    self.info = YLeaf(YType.str, "info")

                    self.lock = YLeaf(YType.enumeration, "lock")

                    self.name = YLeaf(YType.str, "name")

                    self.type = YLeaf(YType.enumeration, "type")

                    self.subscription = YList(self)
                    self._segment_path = lambda: "client"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/cdb/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Cdb.Client, ['datastore', 'info', 'lock', 'name', 'type'], name, value)

                class Datastore(Enum):
                    """
                    Datastore

                    The name of the datastore when 'type' = 'client'. The value

                    'pre\_commit\_running' is the 'pseudo' datastore representing

                    'running' before a commit.

                    .. data:: pre_commit_running = 9

                    """

                    pre_commit_running = Enum.YLeaf(9, "pre_commit_running")


                class Lock(Enum):
                    """
                    Lock

                    Set when 'type' = 'client' and the client has requested or

                    acquired a lock on the datastore. The 'pending\-read' and

                    'pending\-subscription' values indicate that the client has

                    requested but not yet acquired the corresponding lock.

                    A 'read' lock is never taken for the 'operational' datastore,

                    a 'subscription' lock is never taken for any other datastore

                    than 'operational'.

                    .. data:: read = 0

                    .. data:: subscription = 1

                    .. data:: pending_read = 2

                    .. data:: pending_subscription = 3

                    """

                    read = Enum.YLeaf(0, "read")

                    subscription = Enum.YLeaf(1, "subscription")

                    pending_read = Enum.YLeaf(2, "pending-read")

                    pending_subscription = Enum.YLeaf(3, "pending-subscription")


                class Type(Enum):
                    """
                    Type

                    The type of client\: 'inactive' is a client connection without

                    any specific state. 'client' means that the client has an

                    active session towards a datastore. A 'subscriber' has made

                    one or more subscriptions. 'waiting' means that the client is

                    waiting for completion of a call such as cdb\_wait\_start().

                    .. data:: inactive = 0

                    .. data:: client = 1

                    .. data:: subscriber = 2

                    .. data:: waiting = 3

                    """

                    inactive = Enum.YLeaf(0, "inactive")

                    client = Enum.YLeaf(1, "client")

                    subscriber = Enum.YLeaf(2, "subscriber")

                    waiting = Enum.YLeaf(3, "waiting")



                class Subscription(Entity):
                    """
                    
                    
                    .. attribute:: datastore
                    
                    	The name of the datastore for the subscription \- only 'running' and 'operational' can have subscriptions
                    	**type**\:   :py:class:`DatastoreName <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.DatastoreName>`
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem  with the subscription
                    	**type**\:   :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Subscription.Error>`
                    
                    .. attribute:: id
                    
                    	The subscription identifier for the subscription
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: path
                    
                    	The path that the subscription pertains to
                    	**type**\:  str
                    
                    .. attribute:: priority
                    
                    	The priority of the subscription
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: twophase
                    
                    	Present if this is a 'twophase' subscription, i.e. notifications will be delivered at 'prepare' in addition to 'commit'. Only for the 'running' datastore
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Cdb.Client.Subscription, self).__init__()

                        self.yang_name = "subscription"
                        self.yang_parent_name = "client"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.datastore = YLeaf(YType.enumeration, "datastore")

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.path = YLeaf(YType.str, "path")

                        self.priority = YLeaf(YType.int32, "priority")

                        self.twophase = YLeaf(YType.empty, "twophase")
                        self._segment_path = lambda: "subscription"
                        self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/cdb/client/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Cdb.Client.Subscription, ['datastore', 'error', 'id', 'path', 'priority', 'twophase'], name, value)

                    class Error(Enum):
                        """
                        Error

                        If this leaf exists, there is a problem

                         with the subscription.

                        .. data:: PENDING = 0

                        	This value means that the subscribing client has not

                        	completed the subscription (with cdb_subscribe_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



            class Datastore(Entity):
                """
                
                
                .. attribute:: name  <key>
                
                	
                	**type**\:   :py:class:`DatastoreName <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.DatastoreName>`
                
                .. attribute:: disk_size
                
                	The size of the file that is used for persistent storage for the datastore. Only present if 'filename' is present
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: filename
                
                	The pathname of the file that is used for persistent storage for the datastore. Not present for 'running' when 'startup' exists
                	**type**\:  str
                
                .. attribute:: pending_notification_queue
                
                	Queues of notifications that have been generated but not yet delivered to subscribing clients. Not present for the 'startup' datastore
                	**type**\: list of    :py:class:`PendingNotificationQueue <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue>`
                
                .. attribute:: pending_subscription_sync
                
                	Information pertaining to subscription notifications that have been delivered to, but not yet acknowledged by, subscribing clients. Not present for the 'startup' datastore
                	**type**\:   :py:class:`PendingSubscriptionSync <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync>`
                
                	**presence node**\: True
                
                .. attribute:: ram_size
                
                	The size of the in\-memory representation of the datastore
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: read_locks
                
                	The number of read locks on the datastore. Not present for the 'operational' data store
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: subscription_lock_set
                
                	Indicates whether a subscription lock is in effect for the 'operational' datastore
                	**type**\:  bool
                
                .. attribute:: transaction_id
                
                	The id of the last committed transaction for the 'running' datastore, or the last update for the 'operational' datastore. For the 'operational' datastore, it is only present when HA is enabled
                	**type**\:  str
                
                .. attribute:: waiting_for_replication_sync
                
                	Indicates whether synchronous replication from HA master to HA slave is in progress for the datastore. Not present for the 'operational' datastore
                	**type**\:  bool
                
                .. attribute:: write_lock_set
                
                	Indicates whether a write lock is in effect for the datastore. Not present for the 'operational' datastore
                	**type**\:  bool
                
                .. attribute:: write_queue
                
                	Number of pending write requests for the 'operational' datastore on a HA slave that is in the process of syncronizing with the master
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Cdb.Datastore, self).__init__()

                    self.yang_name = "datastore"
                    self.yang_parent_name = "cdb"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"pending-subscription-sync" : ("pending_subscription_sync", ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync)}
                    self._child_list_classes = {"pending-notification-queue" : ("pending_notification_queue", ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue)}

                    self.name = YLeaf(YType.enumeration, "name")

                    self.disk_size = YLeaf(YType.uint64, "disk-size")

                    self.filename = YLeaf(YType.str, "filename")

                    self.ram_size = YLeaf(YType.uint64, "ram-size")

                    self.read_locks = YLeaf(YType.uint32, "read-locks")

                    self.subscription_lock_set = YLeaf(YType.boolean, "subscription-lock-set")

                    self.transaction_id = YLeaf(YType.str, "transaction-id")

                    self.waiting_for_replication_sync = YLeaf(YType.boolean, "waiting-for-replication-sync")

                    self.write_lock_set = YLeaf(YType.boolean, "write-lock-set")

                    self.write_queue = YLeaf(YType.uint32, "write-queue")

                    self.pending_subscription_sync = None
                    self._children_name_map["pending_subscription_sync"] = "pending-subscription-sync"
                    self._children_yang_names.add("pending-subscription-sync")

                    self.pending_notification_queue = YList(self)
                    self._segment_path = lambda: "datastore" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/cdb/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Cdb.Datastore, ['name', 'disk_size', 'filename', 'ram_size', 'read_locks', 'subscription_lock_set', 'transaction_id', 'waiting_for_replication_sync', 'write_lock_set', 'write_queue'], name, value)


                class PendingNotificationQueue(Entity):
                    """
                    Queues of notifications that have been generated but not
                    yet delivered to subscribing clients. Not present for the
                    'startup' datastore.
                    
                    .. attribute:: notification
                    
                    	
                    	**type**\: list of    :py:class:`Notification <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue, self).__init__()

                        self.yang_name = "pending-notification-queue"
                        self.yang_parent_name = "datastore"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"notification" : ("notification", ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification)}

                        self.notification = YList(self)
                        self._segment_path = lambda: "pending-notification-queue"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue, [], name, value)


                    class Notification(Entity):
                        """
                        
                        
                        .. attribute:: client_name
                        
                        	The name of the client that is the recipient of the notification
                        	**type**\:  str
                        
                        .. attribute:: priority
                        
                        	The priority of the subscriptions that generated the notification. Not present for the the 'operational' datastore
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: subscription_ids
                        
                        	The subscription identifiers for the subscriptions that generated the notification
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification, self).__init__()

                            self.yang_name = "notification"
                            self.yang_parent_name = "pending-notification-queue"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.client_name = YLeaf(YType.str, "client-name")

                            self.priority = YLeaf(YType.int32, "priority")

                            self.subscription_ids = YLeafList(YType.uint32, "subscription-ids")
                            self._segment_path = lambda: "notification"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification, ['client_name', 'priority', 'subscription_ids'], name, value)


                class PendingSubscriptionSync(Entity):
                    """
                    Information pertaining to subscription notifications that have
                    been delivered to, but not yet acknowledged by, subscribing
                    clients. Not present for the 'startup' datastore.
                    
                    .. attribute:: notification
                    
                    	
                    	**type**\: list of    :py:class:`Notification <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification>`
                    
                    .. attribute:: priority
                    
                    	The priority of the subscriptions that generated the notifications that are waiting for acknowledgement. Not present for the 'operational' datastore
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: time_remaining
                    
                    	The remaining time in seconds until subscribing clients that have not acknowledged their notifications are considered unresponsive and will be disconnected. See /confdConfig/cdb/clientTimeout in the confd.conf(5) manual page. The value 'infinity' means that no timeout has been configured in confd.conf
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    
                    ----
                    	**type**\:   :py:class:`TimeRemaining <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.TimeRemaining>`
                    
                    
                    ----
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync, self).__init__()

                        self.yang_name = "pending-subscription-sync"
                        self.yang_parent_name = "datastore"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"notification" : ("notification", ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification)}
                        self.is_presence_container = True

                        self.priority = YLeaf(YType.int32, "priority")

                        self.time_remaining = YLeaf(YType.str, "time-remaining")

                        self.notification = YList(self)
                        self._segment_path = lambda: "pending-subscription-sync"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync, ['priority', 'time_remaining'], name, value)

                    class TimeRemaining(Enum):
                        """
                        TimeRemaining

                        The remaining time in seconds until subscribing clients

                        that have not acknowledged their notifications are

                        considered unresponsive and will be disconnected. See

                        /confdConfig/cdb/clientTimeout in the confd.conf(5) manual

                        page. The value 'infinity' means that no timeout has been

                        configured in confd.conf.

                        .. data:: infinity = 0

                        """

                        infinity = Enum.YLeaf(0, "infinity")



                    class Notification(Entity):
                        """
                        
                        
                        .. attribute:: client_name
                        
                        	The name of the client that is the recipient of the notification
                        	**type**\:  str
                        
                        .. attribute:: subscription_ids
                        
                        	The subscription identifiers for the subscriptions that generated the notification
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification, self).__init__()

                            self.yang_name = "notification"
                            self.yang_parent_name = "pending-subscription-sync"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.client_name = YLeaf(YType.str, "client-name")

                            self.subscription_ids = YLeafList(YType.uint32, "subscription-ids")
                            self._segment_path = lambda: "notification"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification, ['client_name', 'subscription_ids'], name, value)


    class LoadedDataModels(Entity):
        """
        
        
        .. attribute:: data_model
        
        	This list contains all loaded YANG data modules.  This list is a superset of the 'schema' list defined in ietf\-netconf\-monitoring, which only lists modules exported through NETCONF
        	**type**\: list of    :py:class:`DataModel <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.LoadedDataModels.DataModel>`
        
        

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            super(ConfdState.LoadedDataModels, self).__init__()

            self.yang_name = "loaded-data-models"
            self.yang_parent_name = "confd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"data-model" : ("data_model", ConfdState.LoadedDataModels.DataModel)}

            self.data_model = YList(self)
            self._segment_path = lambda: "loaded-data-models"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ConfdState.LoadedDataModels, [], name, value)


        class DataModel(Entity):
            """
            This list contains all loaded YANG data modules.
            
            This list is a superset of the 'schema' list defined in
            ietf\-netconf\-monitoring, which only lists modules exported
            through NETCONF.
            
            .. attribute:: name  <key>
            
            	The YANG module name
            	**type**\:  str
            
            .. attribute:: exported_to
            
            	A list of the contexts (northbound interfaces) this module is exported to
            	**type**\: one of the below types:
            
            	**type**\:  list of   :py:class:`ExportedTo <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.LoadedDataModels.DataModel.ExportedTo>`
            
            
            ----
            	**type**\:  list of str
            
            
            ----
            .. attribute:: exported_to_all
            
            	This leaf is present if the module is exported to all northbound interfaces
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: namespace
            
            	The YANG module namespace
            	**type**\:  str
            
            .. attribute:: prefix
            
            	The prefix defined in the YANG module
            	**type**\:  str
            
            .. attribute:: revision
            
            	The YANG module revision
            	**type**\:  str
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.LoadedDataModels.DataModel, self).__init__()

                self.yang_name = "data-model"
                self.yang_parent_name = "loaded-data-models"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.exported_to = YLeafList(YType.str, "exported-to")

                self.exported_to_all = YLeaf(YType.empty, "exported-to-all")

                self.namespace = YLeaf(YType.str, "namespace")

                self.prefix = YLeaf(YType.str, "prefix")

                self.revision = YLeaf(YType.str, "revision")
                self._segment_path = lambda: "data-model" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/loaded-data-models/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.LoadedDataModels.DataModel, ['name', 'exported_to', 'exported_to_all', 'namespace', 'prefix', 'revision'], name, value)

            class ExportedTo(Enum):
                """
                ExportedTo

                A list of the contexts (northbound interfaces) this module

                is exported to.

                .. data:: netconf = 0

                .. data:: cli = 1

                .. data:: webui = 2

                .. data:: rest = 3

                .. data:: snmp = 4

                """

                netconf = Enum.YLeaf(0, "netconf")

                cli = Enum.YLeaf(1, "cli")

                webui = Enum.YLeaf(2, "webui")

                rest = Enum.YLeaf(3, "rest")

                snmp = Enum.YLeaf(4, "snmp")



    class Netconf(Entity):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the NETCONF server is listening on.  Note that other mechanisms can be put in front of the TCP addresses below, e.g., an OpenSSH server.  Such mechanisms are not known to the daemon and not listed here
        	**type**\:   :py:class:`Listen <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Netconf.Listen>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            super(ConfdState.Netconf, self).__init__()

            self.yang_name = "netconf"
            self.yang_parent_name = "confd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"listen" : ("listen", ConfdState.Netconf.Listen)}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.listen = ConfdState.Netconf.Listen()
            self.listen.parent = self
            self._children_name_map["listen"] = "listen"
            self._children_yang_names.add("listen")
            self._segment_path = lambda: "netconf"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()


        class Listen(Entity):
            """
            The transport addresses the NETCONF server is listening on.
            
            Note that other mechanisms can be put in front of the TCP
            addresses below, e.g., an OpenSSH server.  Such mechanisms
            are not known to the daemon and not listed here.
            
            .. attribute:: ssh
            
            	
            	**type**\: list of    :py:class:`Ssh <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Netconf.Listen.Ssh>`
            
            .. attribute:: tcp
            
            	
            	**type**\: list of    :py:class:`Tcp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Netconf.Listen.Tcp>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Netconf.Listen, self).__init__()

                self.yang_name = "listen"
                self.yang_parent_name = "netconf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"ssh" : ("ssh", ConfdState.Netconf.Listen.Ssh), "tcp" : ("tcp", ConfdState.Netconf.Listen.Tcp)}

                self.ssh = YList(self)
                self.tcp = YList(self)
                self._segment_path = lambda: "listen"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/netconf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Netconf.Listen, [], name, value)


            class Ssh(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Netconf.Listen.Ssh, self).__init__()

                    self.yang_name = "ssh"
                    self.yang_parent_name = "listen"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")
                    self._segment_path = lambda: "ssh"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/netconf/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Netconf.Listen.Ssh, ['ip', 'port'], name, value)


            class Tcp(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Netconf.Listen.Tcp, self).__init__()

                    self.yang_name = "tcp"
                    self.yang_parent_name = "listen"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")
                    self._segment_path = lambda: "tcp"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/netconf/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Netconf.Listen.Tcp, ['ip', 'port'], name, value)


    class Rest(Entity):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the REST server is listening on
        	**type**\:   :py:class:`Listen <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Rest.Listen>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            super(ConfdState.Rest, self).__init__()

            self.yang_name = "rest"
            self.yang_parent_name = "confd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"listen" : ("listen", ConfdState.Rest.Listen)}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.listen = ConfdState.Rest.Listen()
            self.listen.parent = self
            self._children_name_map["listen"] = "listen"
            self._children_yang_names.add("listen")
            self._segment_path = lambda: "rest"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()


        class Listen(Entity):
            """
            The transport addresses the REST server is listening on.
            
            .. attribute:: ssl
            
            	
            	**type**\: list of    :py:class:`Ssl <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Rest.Listen.Ssl>`
            
            .. attribute:: tcp
            
            	
            	**type**\: list of    :py:class:`Tcp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Rest.Listen.Tcp>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Rest.Listen, self).__init__()

                self.yang_name = "listen"
                self.yang_parent_name = "rest"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"ssl" : ("ssl", ConfdState.Rest.Listen.Ssl), "tcp" : ("tcp", ConfdState.Rest.Listen.Tcp)}

                self.ssl = YList(self)
                self.tcp = YList(self)
                self._segment_path = lambda: "listen"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/rest/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Rest.Listen, [], name, value)


            class Ssl(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Rest.Listen.Ssl, self).__init__()

                    self.yang_name = "ssl"
                    self.yang_parent_name = "listen"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")
                    self._segment_path = lambda: "ssl"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/rest/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Rest.Listen.Ssl, ['ip', 'port'], name, value)


            class Tcp(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Rest.Listen.Tcp, self).__init__()

                    self.yang_name = "tcp"
                    self.yang_parent_name = "listen"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")
                    self._segment_path = lambda: "tcp"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/rest/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Rest.Listen.Tcp, ['ip', 'port'], name, value)


    class Smp(Entity):
        """
        
        
        .. attribute:: number_of_threads
        
        	Number of threads used by the daemon
        	**type**\:  int
        
        	**range:** 0..65535
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            super(ConfdState.Smp, self).__init__()

            self.yang_name = "smp"
            self.yang_parent_name = "confd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.number_of_threads = YLeaf(YType.uint16, "number-of-threads")
            self._segment_path = lambda: "smp"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ConfdState.Smp, ['number_of_threads'], name, value)


    class Snmp(Entity):
        """
        
        
        .. attribute:: engine_id
        
        	The local Engine ID specified as a list of colon\-specified hexadecimal octets e.g. '4F\:4C\:41\:71'
        	**type**\:  str
        
        	**pattern:** ([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2}){4,31}
        
        .. attribute:: listen
        
        	The transport addresses the SNMP agent is listening on
        	**type**\:   :py:class:`Listen <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Snmp.Listen>`
        
        .. attribute:: mib
        
        	MIBs loaded by the SNMP agent
        	**type**\:  list of str
        
        .. attribute:: version
        
        	SNMP version used by the engine
        	**type**\:   :py:class:`Version <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Snmp.Version>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            super(ConfdState.Snmp, self).__init__()

            self.yang_name = "snmp"
            self.yang_parent_name = "confd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"listen" : ("listen", ConfdState.Snmp.Listen), "version" : ("version", ConfdState.Snmp.Version)}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.engine_id = YLeaf(YType.str, "engine-id")

            self.mib = YLeafList(YType.str, "mib")

            self.listen = ConfdState.Snmp.Listen()
            self.listen.parent = self
            self._children_name_map["listen"] = "listen"
            self._children_yang_names.add("listen")

            self.version = ConfdState.Snmp.Version()
            self.version.parent = self
            self._children_name_map["version"] = "version"
            self._children_yang_names.add("version")
            self._segment_path = lambda: "snmp"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ConfdState.Snmp, ['engine_id', 'mib'], name, value)


        class Listen(Entity):
            """
            The transport addresses the SNMP agent is listening on.
            
            .. attribute:: udp
            
            	
            	**type**\: list of    :py:class:`Udp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Snmp.Listen.Udp>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Snmp.Listen, self).__init__()

                self.yang_name = "listen"
                self.yang_parent_name = "snmp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"udp" : ("udp", ConfdState.Snmp.Listen.Udp)}

                self.udp = YList(self)
                self._segment_path = lambda: "listen"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/snmp/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Snmp.Listen, [], name, value)


            class Udp(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Snmp.Listen.Udp, self).__init__()

                    self.yang_name = "udp"
                    self.yang_parent_name = "listen"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")
                    self._segment_path = lambda: "udp"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/snmp/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Snmp.Listen.Udp, ['ip', 'port'], name, value)


        class Version(Entity):
            """
            SNMP version used by the engine.
            
            .. attribute:: v1
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: v2c
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: v3
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Snmp.Version, self).__init__()

                self.yang_name = "version"
                self.yang_parent_name = "snmp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.v1 = YLeaf(YType.empty, "v1")

                self.v2c = YLeaf(YType.empty, "v2c")

                self.v3 = YLeaf(YType.empty, "v3")
                self._segment_path = lambda: "version"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/snmp/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Snmp.Version, ['v1', 'v2c', 'v3'], name, value)


    class Webui(Entity):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the WebUI server is listening on
        	**type**\:   :py:class:`Listen <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Webui.Listen>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            super(ConfdState.Webui, self).__init__()

            self.yang_name = "webui"
            self.yang_parent_name = "confd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"listen" : ("listen", ConfdState.Webui.Listen)}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.listen = ConfdState.Webui.Listen()
            self.listen.parent = self
            self._children_name_map["listen"] = "listen"
            self._children_yang_names.add("listen")
            self._segment_path = lambda: "webui"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()


        class Listen(Entity):
            """
            The transport addresses the WebUI server is listening on.
            
            .. attribute:: ssl
            
            	
            	**type**\: list of    :py:class:`Ssl <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Webui.Listen.Ssl>`
            
            .. attribute:: tcp
            
            	
            	**type**\: list of    :py:class:`Tcp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Webui.Listen.Tcp>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Webui.Listen, self).__init__()

                self.yang_name = "listen"
                self.yang_parent_name = "webui"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"ssl" : ("ssl", ConfdState.Webui.Listen.Ssl), "tcp" : ("tcp", ConfdState.Webui.Listen.Tcp)}

                self.ssl = YList(self)
                self.tcp = YList(self)
                self._segment_path = lambda: "listen"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/webui/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Webui.Listen, [], name, value)


            class Ssl(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Webui.Listen.Ssl, self).__init__()

                    self.yang_name = "ssl"
                    self.yang_parent_name = "listen"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")
                    self._segment_path = lambda: "ssl"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/webui/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Webui.Listen.Ssl, ['ip', 'port'], name, value)


            class Tcp(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: port
                
                	
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Webui.Listen.Tcp, self).__init__()

                    self.yang_name = "tcp"
                    self.yang_parent_name = "listen"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")
                    self._segment_path = lambda: "tcp"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/webui/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Webui.Listen.Tcp, ['ip', 'port'], name, value)

    def clone_ptr(self):
        self._top_entity = ConfdState()
        return self._top_entity

