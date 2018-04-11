""" tailf_confd_monitoring 

This module defines status objects for monitoring of ConfD.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ConfdState(Entity):
    """
    
    
    .. attribute:: version
    
    	Tail\-f product version number
    	**type**\: str
    
    .. attribute:: smp
    
    	
    	**type**\:  :py:class:`Smp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Smp>`
    
    	**presence node**\: True
    
    .. attribute:: epoll
    
    	Indicates whether an enhanced poll() function is used
    	**type**\: bool
    
    .. attribute:: daemon_status
    
    	
    	**type**\:  :py:class:`DaemonStatus <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.DaemonStatus>`
    
    .. attribute:: read_only_mode
    
    	
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: upgrade_mode
    
    	Note that if the node is in upgrade mode, it is not possible to get any information from the system over NETCONF. The error\-app\-tag will be upgrade\-in\-progress.  Existing CLI sessions can get system information
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: ha
    
    	
    	**type**\:  :py:class:`Ha <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Ha>`
    
    	**presence node**\: True
    
    .. attribute:: loaded_data_models
    
    	
    	**type**\:  :py:class:`LoadedDataModels <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.LoadedDataModels>`
    
    .. attribute:: netconf
    
    	
    	**type**\:  :py:class:`Netconf <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Netconf>`
    
    	**presence node**\: True
    
    .. attribute:: cli
    
    	
    	**type**\:  :py:class:`Cli <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Cli>`
    
    	**presence node**\: True
    
    .. attribute:: webui
    
    	
    	**type**\:  :py:class:`Webui <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Webui>`
    
    	**presence node**\: True
    
    .. attribute:: rest
    
    	
    	**type**\:  :py:class:`Rest <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Rest>`
    
    	**presence node**\: True
    
    .. attribute:: snmp
    
    	
    	**type**\:  :py:class:`Snmp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Snmp>`
    
    	**presence node**\: True
    
    .. attribute:: internal
    
    	
    	**type**\:  :py:class:`Internal <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal>`
    
    

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
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("smp", ("smp", ConfdState.Smp)), ("ha", ("ha", ConfdState.Ha)), ("loaded-data-models", ("loaded_data_models", ConfdState.LoadedDataModels)), ("netconf", ("netconf", ConfdState.Netconf)), ("cli", ("cli", ConfdState.Cli)), ("webui", ("webui", ConfdState.Webui)), ("rest", ("rest", ConfdState.Rest)), ("snmp", ("snmp", ConfdState.Snmp)), ("internal", ("internal", ConfdState.Internal))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('version', YLeaf(YType.str, 'version')),
            ('epoll', YLeaf(YType.boolean, 'epoll')),
            ('daemon_status', YLeaf(YType.enumeration, 'daemon-status')),
            ('read_only_mode', YLeaf(YType.empty, 'read-only-mode')),
            ('upgrade_mode', YLeaf(YType.empty, 'upgrade-mode')),
        ])
        self.version = None
        self.epoll = None
        self.daemon_status = None
        self.read_only_mode = None
        self.upgrade_mode = None

        self.smp = None
        self._children_name_map["smp"] = "smp"
        self._children_yang_names.add("smp")

        self.ha = None
        self._children_name_map["ha"] = "ha"
        self._children_yang_names.add("ha")

        self.loaded_data_models = ConfdState.LoadedDataModels()
        self.loaded_data_models.parent = self
        self._children_name_map["loaded_data_models"] = "loaded-data-models"
        self._children_yang_names.add("loaded-data-models")

        self.netconf = None
        self._children_name_map["netconf"] = "netconf"
        self._children_yang_names.add("netconf")

        self.cli = None
        self._children_name_map["cli"] = "cli"
        self._children_yang_names.add("cli")

        self.webui = None
        self._children_name_map["webui"] = "webui"
        self._children_yang_names.add("webui")

        self.rest = None
        self._children_name_map["rest"] = "rest"
        self._children_yang_names.add("rest")

        self.snmp = None
        self._children_name_map["snmp"] = "snmp"
        self._children_yang_names.add("snmp")

        self.internal = ConfdState.Internal()
        self.internal.parent = self
        self._children_name_map["internal"] = "internal"
        self._children_yang_names.add("internal")
        self._segment_path = lambda: "tailf-confd-monitoring:confd-state"

    def __setattr__(self, name, value):
        self._perform_setattr(ConfdState, ['version', 'epoll', 'daemon_status', 'read_only_mode', 'upgrade_mode'], name, value)

    class DaemonStatus(Enum):
        """
        DaemonStatus (Enum Class)

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



    class Smp(Entity):
        """
        
        
        .. attribute:: number_of_threads
        
        	Number of threads used by the daemon
        	**type**\: int
        
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
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('number_of_threads', YLeaf(YType.uint16, 'number-of-threads')),
            ])
            self.number_of_threads = None
            self._segment_path = lambda: "smp"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ConfdState.Smp, ['number_of_threads'], name, value)


    class Ha(Entity):
        """
        
        
        .. attribute:: mode
        
        	The current HA mode of the node in the HA cluster
        	**type**\:  :py:class:`Mode <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Ha.Mode>`
        
        .. attribute:: node_id
        
        	The node identifier of this node in the HA cluster
        	**type**\: str
        
        .. attribute:: master_node_id
        
        	The node identifier of this node's parent node. This is the HA cluster's master node unless relay slaves are used
        	**type**\: str
        
        .. attribute:: connected_slave
        
        	The node identifiers of the currently connected slaves
        	**type**\: list of str
        
        .. attribute:: pending_slave
        
        	The node identifiers of slaves with pending acknowledgement of synchronous replication
        	**type**\: list of str
        
        

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
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('mode', YLeaf(YType.enumeration, 'mode')),
                ('node_id', YLeaf(YType.str, 'node-id')),
                ('master_node_id', YLeaf(YType.str, 'master-node-id')),
                ('connected_slave', YLeafList(YType.str, 'connected-slave')),
                ('pending_slave', YLeafList(YType.str, 'pending-slave')),
            ])
            self.mode = None
            self.node_id = None
            self.master_node_id = None
            self.connected_slave = []
            self.pending_slave = []
            self._segment_path = lambda: "ha"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ConfdState.Ha, ['mode', 'node_id', 'master_node_id', 'connected_slave', 'pending_slave'], name, value)

        class Mode(Enum):
            """
            Mode (Enum Class)

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



    class LoadedDataModels(Entity):
        """
        
        
        .. attribute:: data_model
        
        	This list contains all loaded YANG data modules.  This list is a superset of the 'schema' list defined in ietf\-netconf\-monitoring, which only lists modules exported through NETCONF
        	**type**\: list of  		 :py:class:`DataModel <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.LoadedDataModels.DataModel>`
        
        

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            super(ConfdState.LoadedDataModels, self).__init__()

            self.yang_name = "loaded-data-models"
            self.yang_parent_name = "confd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("data-model", ("data_model", ConfdState.LoadedDataModels.DataModel))])
            self._leafs = OrderedDict()

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
            
            .. attribute:: name  (key)
            
            	The YANG module name
            	**type**\: str
            
            .. attribute:: revision
            
            	The YANG module revision
            	**type**\: str
            
            .. attribute:: namespace
            
            	The YANG module namespace
            	**type**\: str
            
            .. attribute:: prefix
            
            	The prefix defined in the YANG module
            	**type**\: str
            
            .. attribute:: exported_to_all
            
            	This leaf is present if the module is exported to all northbound interfaces
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: exported_to
            
            	A list of the contexts (northbound interfaces) this module is exported to
            	**type**\: union of the below types:
            
            		**type**\: list of   :py:class:`ExportedTo <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.LoadedDataModels.DataModel.ExportedTo>`
            
            		**type**\: list of str
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.LoadedDataModels.DataModel, self).__init__()

                self.yang_name = "data-model"
                self.yang_parent_name = "loaded-data-models"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('revision', YLeaf(YType.str, 'revision')),
                    ('namespace', YLeaf(YType.str, 'namespace')),
                    ('prefix', YLeaf(YType.str, 'prefix')),
                    ('exported_to_all', YLeaf(YType.empty, 'exported-to-all')),
                    ('exported_to', YLeafList(YType.str, 'exported-to')),
                ])
                self.name = None
                self.revision = None
                self.namespace = None
                self.prefix = None
                self.exported_to_all = None
                self.exported_to = []
                self._segment_path = lambda: "data-model" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/loaded-data-models/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.LoadedDataModels.DataModel, ['name', 'revision', 'namespace', 'prefix', 'exported_to_all', 'exported_to'], name, value)

            class ExportedTo(Enum):
                """
                ExportedTo (Enum Class)

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
        	**type**\:  :py:class:`Listen <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Netconf.Listen>`
        
        

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
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("listen", ("listen", ConfdState.Netconf.Listen))])
            self._child_list_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict()

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
            
            .. attribute:: tcp
            
            	
            	**type**\: list of  		 :py:class:`Tcp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Netconf.Listen.Tcp>`
            
            .. attribute:: ssh
            
            	
            	**type**\: list of  		 :py:class:`Ssh <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Netconf.Listen.Ssh>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Netconf.Listen, self).__init__()

                self.yang_name = "listen"
                self.yang_parent_name = "netconf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("tcp", ("tcp", ConfdState.Netconf.Listen.Tcp)), ("ssh", ("ssh", ConfdState.Netconf.Listen.Ssh))])
                self._leafs = OrderedDict()

                self.tcp = YList(self)
                self.ssh = YList(self)
                self._segment_path = lambda: "listen"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/netconf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Netconf.Listen, [], name, value)


            class Tcp(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: port
                
                	
                	**type**\: int
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip', YLeaf(YType.str, 'ip')),
                        ('port', YLeaf(YType.uint16, 'port')),
                    ])
                    self.ip = None
                    self.port = None
                    self._segment_path = lambda: "tcp"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/netconf/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Netconf.Listen.Tcp, ['ip', 'port'], name, value)


            class Ssh(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: port
                
                	
                	**type**\: int
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip', YLeaf(YType.str, 'ip')),
                        ('port', YLeaf(YType.uint16, 'port')),
                    ])
                    self.ip = None
                    self.port = None
                    self._segment_path = lambda: "ssh"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/netconf/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Netconf.Listen.Ssh, ['ip', 'port'], name, value)


    class Cli(Entity):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the CLI server is listening on.  In addition to the SSH addresses listen below, the CLI can always be invoked through the daemons IPC port.  Note that other mechanisms can be put in front of the IPC port, e.g., an OpenSSH server.  Such mechanisms are not known to the daemon and not listed here
        	**type**\:  :py:class:`Listen <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Cli.Listen>`
        
        

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
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("listen", ("listen", ConfdState.Cli.Listen))])
            self._child_list_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict()

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
            
            	
            	**type**\: list of  		 :py:class:`Ssh <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Cli.Listen.Ssh>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Cli.Listen, self).__init__()

                self.yang_name = "listen"
                self.yang_parent_name = "cli"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("ssh", ("ssh", ConfdState.Cli.Listen.Ssh))])
                self._leafs = OrderedDict()

                self.ssh = YList(self)
                self._segment_path = lambda: "listen"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/cli/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Cli.Listen, [], name, value)


            class Ssh(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: port
                
                	
                	**type**\: int
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip', YLeaf(YType.str, 'ip')),
                        ('port', YLeaf(YType.uint16, 'port')),
                    ])
                    self.ip = None
                    self.port = None
                    self._segment_path = lambda: "ssh"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/cli/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Cli.Listen.Ssh, ['ip', 'port'], name, value)


    class Webui(Entity):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the WebUI server is listening on
        	**type**\:  :py:class:`Listen <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Webui.Listen>`
        
        

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
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("listen", ("listen", ConfdState.Webui.Listen))])
            self._child_list_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict()

            self.listen = ConfdState.Webui.Listen()
            self.listen.parent = self
            self._children_name_map["listen"] = "listen"
            self._children_yang_names.add("listen")
            self._segment_path = lambda: "webui"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()


        class Listen(Entity):
            """
            The transport addresses the WebUI server is listening on.
            
            .. attribute:: tcp
            
            	
            	**type**\: list of  		 :py:class:`Tcp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Webui.Listen.Tcp>`
            
            .. attribute:: ssl
            
            	
            	**type**\: list of  		 :py:class:`Ssl <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Webui.Listen.Ssl>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Webui.Listen, self).__init__()

                self.yang_name = "listen"
                self.yang_parent_name = "webui"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("tcp", ("tcp", ConfdState.Webui.Listen.Tcp)), ("ssl", ("ssl", ConfdState.Webui.Listen.Ssl))])
                self._leafs = OrderedDict()

                self.tcp = YList(self)
                self.ssl = YList(self)
                self._segment_path = lambda: "listen"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/webui/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Webui.Listen, [], name, value)


            class Tcp(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: port
                
                	
                	**type**\: int
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip', YLeaf(YType.str, 'ip')),
                        ('port', YLeaf(YType.uint16, 'port')),
                    ])
                    self.ip = None
                    self.port = None
                    self._segment_path = lambda: "tcp"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/webui/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Webui.Listen.Tcp, ['ip', 'port'], name, value)


            class Ssl(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: port
                
                	
                	**type**\: int
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip', YLeaf(YType.str, 'ip')),
                        ('port', YLeaf(YType.uint16, 'port')),
                    ])
                    self.ip = None
                    self.port = None
                    self._segment_path = lambda: "ssl"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/webui/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Webui.Listen.Ssl, ['ip', 'port'], name, value)


    class Rest(Entity):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the REST server is listening on
        	**type**\:  :py:class:`Listen <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Rest.Listen>`
        
        

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
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("listen", ("listen", ConfdState.Rest.Listen))])
            self._child_list_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict()

            self.listen = ConfdState.Rest.Listen()
            self.listen.parent = self
            self._children_name_map["listen"] = "listen"
            self._children_yang_names.add("listen")
            self._segment_path = lambda: "rest"
            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/%s" % self._segment_path()


        class Listen(Entity):
            """
            The transport addresses the REST server is listening on.
            
            .. attribute:: tcp
            
            	
            	**type**\: list of  		 :py:class:`Tcp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Rest.Listen.Tcp>`
            
            .. attribute:: ssl
            
            	
            	**type**\: list of  		 :py:class:`Ssl <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Rest.Listen.Ssl>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Rest.Listen, self).__init__()

                self.yang_name = "listen"
                self.yang_parent_name = "rest"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("tcp", ("tcp", ConfdState.Rest.Listen.Tcp)), ("ssl", ("ssl", ConfdState.Rest.Listen.Ssl))])
                self._leafs = OrderedDict()

                self.tcp = YList(self)
                self.ssl = YList(self)
                self._segment_path = lambda: "listen"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/rest/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Rest.Listen, [], name, value)


            class Tcp(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: port
                
                	
                	**type**\: int
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip', YLeaf(YType.str, 'ip')),
                        ('port', YLeaf(YType.uint16, 'port')),
                    ])
                    self.ip = None
                    self.port = None
                    self._segment_path = lambda: "tcp"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/rest/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Rest.Listen.Tcp, ['ip', 'port'], name, value)


            class Ssl(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: port
                
                	
                	**type**\: int
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip', YLeaf(YType.str, 'ip')),
                        ('port', YLeaf(YType.uint16, 'port')),
                    ])
                    self.ip = None
                    self.port = None
                    self._segment_path = lambda: "ssl"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/rest/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Rest.Listen.Ssl, ['ip', 'port'], name, value)


    class Snmp(Entity):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the SNMP agent is listening on
        	**type**\:  :py:class:`Listen <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Snmp.Listen>`
        
        .. attribute:: mib
        
        	MIBs loaded by the SNMP agent
        	**type**\: list of str
        
        .. attribute:: version
        
        	SNMP version used by the engine
        	**type**\:  :py:class:`Version <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Snmp.Version>`
        
        .. attribute:: engine_id
        
        	The local Engine ID specified as a list of colon\-specified hexadecimal octets e.g. '4F\:4C\:41\:71'
        	**type**\: str
        
        	**pattern:** ([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2}){4,31}
        
        

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
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("listen", ("listen", ConfdState.Snmp.Listen)), ("version", ("version", ConfdState.Snmp.Version))])
            self._child_list_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('mib', YLeafList(YType.str, 'mib')),
                ('engine_id', YLeaf(YType.str, 'engine-id')),
            ])
            self.mib = []
            self.engine_id = None

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
            self._perform_setattr(ConfdState.Snmp, ['mib', 'engine_id'], name, value)


        class Listen(Entity):
            """
            The transport addresses the SNMP agent is listening on.
            
            .. attribute:: udp
            
            	
            	**type**\: list of  		 :py:class:`Udp <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Snmp.Listen.Udp>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Snmp.Listen, self).__init__()

                self.yang_name = "listen"
                self.yang_parent_name = "snmp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("udp", ("udp", ConfdState.Snmp.Listen.Udp))])
                self._leafs = OrderedDict()

                self.udp = YList(self)
                self._segment_path = lambda: "listen"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/snmp/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Snmp.Listen, [], name, value)


            class Udp(Entity):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: port
                
                	
                	**type**\: int
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip', YLeaf(YType.str, 'ip')),
                        ('port', YLeaf(YType.uint16, 'port')),
                    ])
                    self.ip = None
                    self.port = None
                    self._segment_path = lambda: "udp"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/snmp/listen/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Snmp.Listen.Udp, ['ip', 'port'], name, value)


        class Version(Entity):
            """
            SNMP version used by the engine.
            
            .. attribute:: v1
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: v2c
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: v3
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Snmp.Version, self).__init__()

                self.yang_name = "version"
                self.yang_parent_name = "snmp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('v1', YLeaf(YType.empty, 'v1')),
                    ('v2c', YLeaf(YType.empty, 'v2c')),
                    ('v3', YLeaf(YType.empty, 'v3')),
                ])
                self.v1 = None
                self.v2c = None
                self.v3 = None
                self._segment_path = lambda: "version"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/snmp/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Snmp.Version, ['v1', 'v2c', 'v3'], name, value)


    class Internal(Entity):
        """
        
        
        .. attribute:: callpoints
        
        	
        	**type**\:  :py:class:`Callpoints <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints>`
        
        .. attribute:: cdb
        
        	
        	**type**\:  :py:class:`Cdb <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb>`
        
        

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            super(ConfdState.Internal, self).__init__()

            self.yang_name = "internal"
            self.yang_parent_name = "confd-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("callpoints", ("callpoints", ConfdState.Internal.Callpoints)), ("cdb", ("cdb", ConfdState.Internal.Cdb))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

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
            DatastoreName (Enum Class)

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
            
            
            .. attribute:: callpoint
            
            	
            	**type**\: list of  		 :py:class:`Callpoint <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint>`
            
            .. attribute:: validationpoint
            
            	
            	**type**\: list of  		 :py:class:`Validationpoint <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint>`
            
            .. attribute:: actionpoint
            
            	
            	**type**\: list of  		 :py:class:`Actionpoint <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint>`
            
            .. attribute:: snmp_inform_callback
            
            	
            	**type**\: list of  		 :py:class:`SnmpInformCallback <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback>`
            
            .. attribute:: snmp_notification_subscription
            
            	
            	**type**\: list of  		 :py:class:`SnmpNotificationSubscription <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription>`
            
            .. attribute:: error_formatting_callback
            
            	
            	**type**\: list of  		 :py:class:`ErrorFormattingCallback <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback>`
            
            .. attribute:: typepoint
            
            	
            	**type**\: list of  		 :py:class:`Typepoint <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint>`
            
            .. attribute:: notification_stream_replay
            
            	
            	**type**\: list of  		 :py:class:`NotificationStreamReplay <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay>`
            
            .. attribute:: authentication_callback
            
            	
            	**type**\:  :py:class:`AuthenticationCallback <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback>`
            
            	**presence node**\: True
            
            .. attribute:: authorization_callbacks
            
            	
            	**type**\:  :py:class:`AuthorizationCallbacks <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Internal.Callpoints, self).__init__()

                self.yang_name = "callpoints"
                self.yang_parent_name = "internal"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("authentication-callback", ("authentication_callback", ConfdState.Internal.Callpoints.AuthenticationCallback)), ("authorization-callbacks", ("authorization_callbacks", ConfdState.Internal.Callpoints.AuthorizationCallbacks))])
                self._child_list_classes = OrderedDict([("callpoint", ("callpoint", ConfdState.Internal.Callpoints.Callpoint)), ("validationpoint", ("validationpoint", ConfdState.Internal.Callpoints.Validationpoint)), ("actionpoint", ("actionpoint", ConfdState.Internal.Callpoints.Actionpoint)), ("snmp-inform-callback", ("snmp_inform_callback", ConfdState.Internal.Callpoints.SnmpInformCallback)), ("snmp-notification-subscription", ("snmp_notification_subscription", ConfdState.Internal.Callpoints.SnmpNotificationSubscription)), ("error-formatting-callback", ("error_formatting_callback", ConfdState.Internal.Callpoints.ErrorFormattingCallback)), ("typepoint", ("typepoint", ConfdState.Internal.Callpoints.Typepoint)), ("notification-stream-replay", ("notification_stream_replay", ConfdState.Internal.Callpoints.NotificationStreamReplay))])
                self._leafs = OrderedDict()

                self.authentication_callback = None
                self._children_name_map["authentication_callback"] = "authentication-callback"
                self._children_yang_names.add("authentication-callback")

                self.authorization_callbacks = None
                self._children_name_map["authorization_callbacks"] = "authorization-callbacks"
                self._children_yang_names.add("authorization-callbacks")

                self.callpoint = YList(self)
                self.validationpoint = YList(self)
                self.actionpoint = YList(self)
                self.snmp_inform_callback = YList(self)
                self.snmp_notification_subscription = YList(self)
                self.error_formatting_callback = YList(self)
                self.typepoint = YList(self)
                self.notification_stream_replay = YList(self)
                self._segment_path = lambda: "callpoints"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Internal.Callpoints, [], name, value)


            class Callpoint(Entity):
                """
                
                
                .. attribute:: id  (key)
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Daemon>`
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Range>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Error>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.Callpoint, self).__init__()

                    self.yang_name = "callpoint"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['id']
                    self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.Callpoint.Daemon))])
                    self._child_list_classes = OrderedDict([("range", ("range", ConfdState.Internal.Callpoints.Callpoint.Range))])
                    self._leafs = OrderedDict([
                        ('id', YLeaf(YType.str, 'id')),
                        ('path', YLeaf(YType.str, 'path')),
                        ('file', YLeaf(YType.str, 'file')),
                        ('error', YLeaf(YType.enumeration, 'error')),
                    ])
                    self.id = None
                    self.path = None
                    self.file = None
                    self.error = None

                    self.daemon = ConfdState.Internal.Callpoints.Callpoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "callpoint" + "[id='" + str(self.id) + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.Callpoint, ['id', 'path', 'file', 'error'], name, value)

                class Error(Enum):
                    """
                    Error (Enum Class)

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
                    
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Daemon.Error>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Callpoint.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "callpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.uint32, 'id')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('error', YLeaf(YType.enumeration, 'error')),
                        ])
                        self.id = None
                        self.name = None
                        self.error = None
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Callpoint.Daemon, ['id', 'name', 'error'], name, value)

                    class Error(Enum):
                        """
                        Error (Enum Class)

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Range.Daemon>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Callpoint.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "callpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.Callpoint.Range.Daemon))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lower', YLeaf(YType.str, 'lower')),
                            ('upper', YLeaf(YType.str, 'upper')),
                            ('default', YLeaf(YType.empty, 'default')),
                        ])
                        self.lower = None
                        self.upper = None
                        self.default = None

                        self.daemon = ConfdState.Internal.Callpoints.Callpoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Callpoint.Range, ['lower', 'upper', 'default'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Range.Daemon.Error>`
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.Callpoint.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.uint32, 'id')),
                                ('name', YLeaf(YType.str, 'name')),
                                ('error', YLeaf(YType.enumeration, 'error')),
                            ])
                            self.id = None
                            self.name = None
                            self.error = None
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.Callpoint.Range.Daemon, ['id', 'name', 'error'], name, value)

                        class Error(Enum):
                            """
                            Error (Enum Class)

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class Validationpoint(Entity):
                """
                
                
                .. attribute:: id  (key)
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Daemon>`
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Range>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Error>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.Validationpoint, self).__init__()

                    self.yang_name = "validationpoint"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['id']
                    self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.Validationpoint.Daemon))])
                    self._child_list_classes = OrderedDict([("range", ("range", ConfdState.Internal.Callpoints.Validationpoint.Range))])
                    self._leafs = OrderedDict([
                        ('id', YLeaf(YType.str, 'id')),
                        ('path', YLeaf(YType.str, 'path')),
                        ('file', YLeaf(YType.str, 'file')),
                        ('error', YLeaf(YType.enumeration, 'error')),
                    ])
                    self.id = None
                    self.path = None
                    self.file = None
                    self.error = None

                    self.daemon = ConfdState.Internal.Callpoints.Validationpoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "validationpoint" + "[id='" + str(self.id) + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.Validationpoint, ['id', 'path', 'file', 'error'], name, value)

                class Error(Enum):
                    """
                    Error (Enum Class)

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
                    
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Daemon.Error>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Validationpoint.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "validationpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.uint32, 'id')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('error', YLeaf(YType.enumeration, 'error')),
                        ])
                        self.id = None
                        self.name = None
                        self.error = None
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Validationpoint.Daemon, ['id', 'name', 'error'], name, value)

                    class Error(Enum):
                        """
                        Error (Enum Class)

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Validationpoint.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "validationpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lower', YLeaf(YType.str, 'lower')),
                            ('upper', YLeaf(YType.str, 'upper')),
                            ('default', YLeaf(YType.empty, 'default')),
                        ])
                        self.lower = None
                        self.upper = None
                        self.default = None

                        self.daemon = ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Validationpoint.Range, ['lower', 'upper', 'default'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon.Error>`
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.uint32, 'id')),
                                ('name', YLeaf(YType.str, 'name')),
                                ('error', YLeaf(YType.enumeration, 'error')),
                            ])
                            self.id = None
                            self.name = None
                            self.error = None
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon, ['id', 'name', 'error'], name, value)

                        class Error(Enum):
                            """
                            Error (Enum Class)

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class Actionpoint(Entity):
                """
                
                
                .. attribute:: id  (key)
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Daemon>`
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Range>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Error>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.Actionpoint, self).__init__()

                    self.yang_name = "actionpoint"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['id']
                    self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.Actionpoint.Daemon))])
                    self._child_list_classes = OrderedDict([("range", ("range", ConfdState.Internal.Callpoints.Actionpoint.Range))])
                    self._leafs = OrderedDict([
                        ('id', YLeaf(YType.str, 'id')),
                        ('path', YLeaf(YType.str, 'path')),
                        ('file', YLeaf(YType.str, 'file')),
                        ('error', YLeaf(YType.enumeration, 'error')),
                    ])
                    self.id = None
                    self.path = None
                    self.file = None
                    self.error = None

                    self.daemon = ConfdState.Internal.Callpoints.Actionpoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "actionpoint" + "[id='" + str(self.id) + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.Actionpoint, ['id', 'path', 'file', 'error'], name, value)

                class Error(Enum):
                    """
                    Error (Enum Class)

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
                    
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Daemon.Error>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Actionpoint.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "actionpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.uint32, 'id')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('error', YLeaf(YType.enumeration, 'error')),
                        ])
                        self.id = None
                        self.name = None
                        self.error = None
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Actionpoint.Daemon, ['id', 'name', 'error'], name, value)

                    class Error(Enum):
                        """
                        Error (Enum Class)

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Actionpoint.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "actionpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lower', YLeaf(YType.str, 'lower')),
                            ('upper', YLeaf(YType.str, 'upper')),
                            ('default', YLeaf(YType.empty, 'default')),
                        ])
                        self.lower = None
                        self.upper = None
                        self.default = None

                        self.daemon = ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Actionpoint.Range, ['lower', 'upper', 'default'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon.Error>`
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.uint32, 'id')),
                                ('name', YLeaf(YType.str, 'name')),
                                ('error', YLeaf(YType.enumeration, 'error')),
                            ])
                            self.id = None
                            self.name = None
                            self.error = None
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon, ['id', 'name', 'error'], name, value)

                        class Error(Enum):
                            """
                            Error (Enum Class)

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class SnmpInformCallback(Entity):
                """
                
                
                .. attribute:: id  (key)
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon>`
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Range>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Error>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.SnmpInformCallback, self).__init__()

                    self.yang_name = "snmp-inform-callback"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['id']
                    self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon))])
                    self._child_list_classes = OrderedDict([("range", ("range", ConfdState.Internal.Callpoints.SnmpInformCallback.Range))])
                    self._leafs = OrderedDict([
                        ('id', YLeaf(YType.str, 'id')),
                        ('path', YLeaf(YType.str, 'path')),
                        ('file', YLeaf(YType.str, 'file')),
                        ('error', YLeaf(YType.enumeration, 'error')),
                    ])
                    self.id = None
                    self.path = None
                    self.file = None
                    self.error = None

                    self.daemon = ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "snmp-inform-callback" + "[id='" + str(self.id) + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.SnmpInformCallback, ['id', 'path', 'file', 'error'], name, value)

                class Error(Enum):
                    """
                    Error (Enum Class)

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
                    
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon.Error>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "snmp-inform-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.uint32, 'id')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('error', YLeaf(YType.enumeration, 'error')),
                        ])
                        self.id = None
                        self.name = None
                        self.error = None
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon, ['id', 'name', 'error'], name, value)

                    class Error(Enum):
                        """
                        Error (Enum Class)

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.SnmpInformCallback.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "snmp-inform-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lower', YLeaf(YType.str, 'lower')),
                            ('upper', YLeaf(YType.str, 'upper')),
                            ('default', YLeaf(YType.empty, 'default')),
                        ])
                        self.lower = None
                        self.upper = None
                        self.default = None

                        self.daemon = ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.SnmpInformCallback.Range, ['lower', 'upper', 'default'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon.Error>`
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.uint32, 'id')),
                                ('name', YLeaf(YType.str, 'name')),
                                ('error', YLeaf(YType.enumeration, 'error')),
                            ])
                            self.id = None
                            self.name = None
                            self.error = None
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon, ['id', 'name', 'error'], name, value)

                        class Error(Enum):
                            """
                            Error (Enum Class)

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class SnmpNotificationSubscription(Entity):
                """
                
                
                .. attribute:: id  (key)
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon>`
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Error>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription, self).__init__()

                    self.yang_name = "snmp-notification-subscription"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['id']
                    self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon))])
                    self._child_list_classes = OrderedDict([("range", ("range", ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range))])
                    self._leafs = OrderedDict([
                        ('id', YLeaf(YType.str, 'id')),
                        ('path', YLeaf(YType.str, 'path')),
                        ('file', YLeaf(YType.str, 'file')),
                        ('error', YLeaf(YType.enumeration, 'error')),
                    ])
                    self.id = None
                    self.path = None
                    self.file = None
                    self.error = None

                    self.daemon = ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "snmp-notification-subscription" + "[id='" + str(self.id) + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.SnmpNotificationSubscription, ['id', 'path', 'file', 'error'], name, value)

                class Error(Enum):
                    """
                    Error (Enum Class)

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
                    
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon.Error>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "snmp-notification-subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.uint32, 'id')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('error', YLeaf(YType.enumeration, 'error')),
                        ])
                        self.id = None
                        self.name = None
                        self.error = None
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon, ['id', 'name', 'error'], name, value)

                    class Error(Enum):
                        """
                        Error (Enum Class)

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "snmp-notification-subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lower', YLeaf(YType.str, 'lower')),
                            ('upper', YLeaf(YType.str, 'upper')),
                            ('default', YLeaf(YType.empty, 'default')),
                        ])
                        self.lower = None
                        self.upper = None
                        self.default = None

                        self.daemon = ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range, ['lower', 'upper', 'default'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon.Error>`
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.uint32, 'id')),
                                ('name', YLeaf(YType.str, 'name')),
                                ('error', YLeaf(YType.enumeration, 'error')),
                            ])
                            self.id = None
                            self.name = None
                            self.error = None
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon, ['id', 'name', 'error'], name, value)

                        class Error(Enum):
                            """
                            Error (Enum Class)

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class ErrorFormattingCallback(Entity):
                """
                
                
                .. attribute:: id  (key)
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon>`
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Error>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.ErrorFormattingCallback, self).__init__()

                    self.yang_name = "error-formatting-callback"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['id']
                    self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon))])
                    self._child_list_classes = OrderedDict([("range", ("range", ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range))])
                    self._leafs = OrderedDict([
                        ('id', YLeaf(YType.str, 'id')),
                        ('path', YLeaf(YType.str, 'path')),
                        ('file', YLeaf(YType.str, 'file')),
                        ('error', YLeaf(YType.enumeration, 'error')),
                    ])
                    self.id = None
                    self.path = None
                    self.file = None
                    self.error = None

                    self.daemon = ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "error-formatting-callback" + "[id='" + str(self.id) + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.ErrorFormattingCallback, ['id', 'path', 'file', 'error'], name, value)

                class Error(Enum):
                    """
                    Error (Enum Class)

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
                    
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon.Error>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "error-formatting-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.uint32, 'id')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('error', YLeaf(YType.enumeration, 'error')),
                        ])
                        self.id = None
                        self.name = None
                        self.error = None
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon, ['id', 'name', 'error'], name, value)

                    class Error(Enum):
                        """
                        Error (Enum Class)

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "error-formatting-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lower', YLeaf(YType.str, 'lower')),
                            ('upper', YLeaf(YType.str, 'upper')),
                            ('default', YLeaf(YType.empty, 'default')),
                        ])
                        self.lower = None
                        self.upper = None
                        self.default = None

                        self.daemon = ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range, ['lower', 'upper', 'default'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon.Error>`
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.uint32, 'id')),
                                ('name', YLeaf(YType.str, 'name')),
                                ('error', YLeaf(YType.enumeration, 'error')),
                            ])
                            self.id = None
                            self.name = None
                            self.error = None
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon, ['id', 'name', 'error'], name, value)

                        class Error(Enum):
                            """
                            Error (Enum Class)

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class Typepoint(Entity):
                """
                
                
                .. attribute:: id  (key)
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Daemon>`
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Range>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Error>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.Typepoint, self).__init__()

                    self.yang_name = "typepoint"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['id']
                    self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.Typepoint.Daemon))])
                    self._child_list_classes = OrderedDict([("range", ("range", ConfdState.Internal.Callpoints.Typepoint.Range))])
                    self._leafs = OrderedDict([
                        ('id', YLeaf(YType.str, 'id')),
                        ('path', YLeaf(YType.str, 'path')),
                        ('file', YLeaf(YType.str, 'file')),
                        ('error', YLeaf(YType.enumeration, 'error')),
                    ])
                    self.id = None
                    self.path = None
                    self.file = None
                    self.error = None

                    self.daemon = ConfdState.Internal.Callpoints.Typepoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "typepoint" + "[id='" + str(self.id) + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.Typepoint, ['id', 'path', 'file', 'error'], name, value)

                class Error(Enum):
                    """
                    Error (Enum Class)

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
                    
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Daemon.Error>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Typepoint.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "typepoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.uint32, 'id')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('error', YLeaf(YType.enumeration, 'error')),
                        ])
                        self.id = None
                        self.name = None
                        self.error = None
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Typepoint.Daemon, ['id', 'name', 'error'], name, value)

                    class Error(Enum):
                        """
                        Error (Enum Class)

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Range.Daemon>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.Typepoint.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "typepoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.Typepoint.Range.Daemon))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lower', YLeaf(YType.str, 'lower')),
                            ('upper', YLeaf(YType.str, 'upper')),
                            ('default', YLeaf(YType.empty, 'default')),
                        ])
                        self.lower = None
                        self.upper = None
                        self.default = None

                        self.daemon = ConfdState.Internal.Callpoints.Typepoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.Typepoint.Range, ['lower', 'upper', 'default'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Range.Daemon.Error>`
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.Typepoint.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.uint32, 'id')),
                                ('name', YLeaf(YType.str, 'name')),
                                ('error', YLeaf(YType.enumeration, 'error')),
                            ])
                            self.id = None
                            self.name = None
                            self.error = None
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.Typepoint.Range.Daemon, ['id', 'name', 'error'], name, value)

                        class Error(Enum):
                            """
                            Error (Enum Class)

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class NotificationStreamReplay(Entity):
                """
                
                
                .. attribute:: name  (key)
                
                	Name of the notification stream
                	**type**\: str
                
                .. attribute:: replay_support
                
                	
                	**type**\:  :py:class:`ReplaySupport <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.ReplaySupport>`
                
                .. attribute:: daemon
                
                	
                	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon>`
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Range>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Error>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Callpoints.NotificationStreamReplay, self).__init__()

                    self.yang_name = "notification-stream-replay"
                    self.yang_parent_name = "callpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon))])
                    self._child_list_classes = OrderedDict([("range", ("range", ConfdState.Internal.Callpoints.NotificationStreamReplay.Range))])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('replay_support', YLeaf(YType.enumeration, 'replay-support')),
                        ('path', YLeaf(YType.str, 'path')),
                        ('file', YLeaf(YType.str, 'file')),
                        ('error', YLeaf(YType.enumeration, 'error')),
                    ])
                    self.name = None
                    self.replay_support = None
                    self.path = None
                    self.file = None
                    self.error = None

                    self.daemon = ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "notification-stream-replay" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.NotificationStreamReplay, ['name', 'replay_support', 'path', 'file', 'error'], name, value)

                class Error(Enum):
                    """
                    Error (Enum Class)

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
                    ReplaySupport (Enum Class)

                    .. data:: none = 0

                    .. data:: builtin = 1

                    .. data:: external = 2

                    """

                    none = Enum.YLeaf(0, "none")

                    builtin = Enum.YLeaf(1, "builtin")

                    external = Enum.YLeaf(2, "external")



                class Daemon(Entity):
                    """
                    
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon.Error>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "notification-stream-replay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.uint32, 'id')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('error', YLeaf(YType.enumeration, 'error')),
                        ])
                        self.id = None
                        self.name = None
                        self.error = None
                        self._segment_path = lambda: "daemon"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon, ['id', 'name', 'error'], name, value)

                    class Error(Enum):
                        """
                        Error (Enum Class)

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "notification-stream-replay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lower', YLeaf(YType.str, 'lower')),
                            ('upper', YLeaf(YType.str, 'upper')),
                            ('default', YLeaf(YType.empty, 'default')),
                        ])
                        self.lower = None
                        self.upper = None
                        self.default = None

                        self.daemon = ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range, ['lower', 'upper', 'default'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon.Error>`
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.uint32, 'id')),
                                ('name', YLeaf(YType.str, 'name')),
                                ('error', YLeaf(YType.enumeration, 'error')),
                            ])
                            self.id = None
                            self.name = None
                            self.error = None
                            self._segment_path = lambda: "daemon"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon, ['id', 'name', 'error'], name, value)

                        class Error(Enum):
                            """
                            Error (Enum Class)

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class AuthenticationCallback(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\: bool
                
                .. attribute:: daemon
                
                	
                	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon>`
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Range>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Error>`
                
                

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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon))])
                    self._child_list_classes = OrderedDict([("range", ("range", ConfdState.Internal.Callpoints.AuthenticationCallback.Range))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ('path', YLeaf(YType.str, 'path')),
                        ('file', YLeaf(YType.str, 'file')),
                        ('error', YLeaf(YType.enumeration, 'error')),
                    ])
                    self.enabled = None
                    self.path = None
                    self.file = None
                    self.error = None

                    self.daemon = ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "authentication-callback"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.AuthenticationCallback, ['enabled', 'path', 'file', 'error'], name, value)

                class Error(Enum):
                    """
                    Error (Enum Class)

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
                    
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon.Error>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "authentication-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.uint32, 'id')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('error', YLeaf(YType.enumeration, 'error')),
                        ])
                        self.id = None
                        self.name = None
                        self.error = None
                        self._segment_path = lambda: "daemon"
                        self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authentication-callback/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon, ['id', 'name', 'error'], name, value)

                    class Error(Enum):
                        """
                        Error (Enum Class)

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.AuthenticationCallback.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "authentication-callback"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lower', YLeaf(YType.str, 'lower')),
                            ('upper', YLeaf(YType.str, 'upper')),
                            ('default', YLeaf(YType.empty, 'default')),
                        ])
                        self.lower = None
                        self.upper = None
                        self.default = None

                        self.daemon = ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"
                        self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authentication-callback/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.AuthenticationCallback.Range, ['lower', 'upper', 'default'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon.Error>`
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.uint32, 'id')),
                                ('name', YLeaf(YType.str, 'name')),
                                ('error', YLeaf(YType.enumeration, 'error')),
                            ])
                            self.id = None
                            self.name = None
                            self.error = None
                            self._segment_path = lambda: "daemon"
                            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authentication-callback/range/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon, ['id', 'name', 'error'], name, value)

                        class Error(Enum):
                            """
                            Error (Enum Class)

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



            class AuthorizationCallbacks(Entity):
                """
                
                
                .. attribute:: enabled
                
                	
                	**type**\: bool
                
                .. attribute:: daemon
                
                	
                	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon>`
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Error>`
                
                

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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon))])
                    self._child_list_classes = OrderedDict([("range", ("range", ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ('path', YLeaf(YType.str, 'path')),
                        ('file', YLeaf(YType.str, 'file')),
                        ('error', YLeaf(YType.enumeration, 'error')),
                    ])
                    self.enabled = None
                    self.path = None
                    self.file = None
                    self.error = None

                    self.daemon = ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)
                    self._segment_path = lambda: "authorization-callbacks"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Callpoints.AuthorizationCallbacks, ['enabled', 'path', 'file', 'error'], name, value)

                class Error(Enum):
                    """
                    Error (Enum Class)

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
                    
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon.Error>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon, self).__init__()

                        self.yang_name = "daemon"
                        self.yang_parent_name = "authorization-callbacks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.uint32, 'id')),
                            ('name', YLeaf(YType.str, 'name')),
                            ('error', YLeaf(YType.enumeration, 'error')),
                        ])
                        self.id = None
                        self.name = None
                        self.error = None
                        self._segment_path = lambda: "daemon"
                        self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authorization-callbacks/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon, ['id', 'name', 'error'], name, value)

                    class Error(Enum):
                        """
                        Error (Enum Class)

                        If this leaf exists, there is a problem

                        with the daemon registration.

                        .. data:: PENDING = 0

                        	This value means that the application daemon has not

                        	completed the registration (with confd_register_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")



                class Range(Entity):
                    """
                    
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\:  :py:class:`Daemon <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range, self).__init__()

                        self.yang_name = "range"
                        self.yang_parent_name = "authorization-callbacks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("daemon", ("daemon", ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lower', YLeaf(YType.str, 'lower')),
                            ('upper', YLeaf(YType.str, 'upper')),
                            ('default', YLeaf(YType.empty, 'default')),
                        ])
                        self.lower = None
                        self.upper = None
                        self.default = None

                        self.daemon = ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")
                        self._segment_path = lambda: "range"
                        self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authorization-callbacks/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range, ['lower', 'upper', 'default'], name, value)


                    class Daemon(Entity):
                        """
                        
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon.Error>`
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon, self).__init__()

                            self.yang_name = "daemon"
                            self.yang_parent_name = "range"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.uint32, 'id')),
                                ('name', YLeaf(YType.str, 'name')),
                                ('error', YLeaf(YType.enumeration, 'error')),
                            ])
                            self.id = None
                            self.name = None
                            self.error = None
                            self._segment_path = lambda: "daemon"
                            self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/callpoints/authorization-callbacks/range/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon, ['id', 'name', 'error'], name, value)

                        class Error(Enum):
                            """
                            Error (Enum Class)

                            If this leaf exists, there is a problem

                            with the daemon registration.

                            .. data:: PENDING = 0

                            	This value means that the application daemon has not

                            	completed the registration (with confd_register_done()).

                            """

                            PENDING = Enum.YLeaf(0, "PENDING")



        class Cdb(Entity):
            """
            
            
            .. attribute:: datastore
            
            	
            	**type**\: list of  		 :py:class:`Datastore <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore>`
            
            .. attribute:: client
            
            	
            	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                super(ConfdState.Internal.Cdb, self).__init__()

                self.yang_name = "cdb"
                self.yang_parent_name = "internal"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("datastore", ("datastore", ConfdState.Internal.Cdb.Datastore)), ("client", ("client", ConfdState.Internal.Cdb.Client))])
                self._leafs = OrderedDict()

                self.datastore = YList(self)
                self.client = YList(self)
                self._segment_path = lambda: "cdb"
                self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ConfdState.Internal.Cdb, [], name, value)


            class Datastore(Entity):
                """
                
                
                .. attribute:: name  (key)
                
                	
                	**type**\:  :py:class:`DatastoreName <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.DatastoreName>`
                
                .. attribute:: transaction_id
                
                	The id of the last committed transaction for the 'running' datastore, or the last update for the 'operational' datastore. For the 'operational' datastore, it is only present when HA is enabled
                	**type**\: str
                
                .. attribute:: write_queue
                
                	Number of pending write requests for the 'operational' datastore on a HA slave that is in the process of syncronizing with the master
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: filename
                
                	The pathname of the file that is used for persistent storage for the datastore. Not present for 'running' when 'startup' exists
                	**type**\: str
                
                .. attribute:: disk_size
                
                	The size of the file that is used for persistent storage for the datastore. Only present if 'filename' is present
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ram_size
                
                	The size of the in\-memory representation of the datastore
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: read_locks
                
                	The number of read locks on the datastore. Not present for the 'operational' data store
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: write_lock_set
                
                	Indicates whether a write lock is in effect for the datastore. Not present for the 'operational' datastore
                	**type**\: bool
                
                .. attribute:: subscription_lock_set
                
                	Indicates whether a subscription lock is in effect for the 'operational' datastore
                	**type**\: bool
                
                .. attribute:: waiting_for_replication_sync
                
                	Indicates whether synchronous replication from HA master to HA slave is in progress for the datastore. Not present for the 'operational' datastore
                	**type**\: bool
                
                .. attribute:: pending_subscription_sync
                
                	Information pertaining to subscription notifications that have been delivered to, but not yet acknowledged by, subscribing clients. Not present for the 'startup' datastore
                	**type**\:  :py:class:`PendingSubscriptionSync <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync>`
                
                	**presence node**\: True
                
                .. attribute:: pending_notification_queue
                
                	Queues of notifications that have been generated but not yet delivered to subscribing clients. Not present for the 'startup' datastore
                	**type**\: list of  		 :py:class:`PendingNotificationQueue <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Cdb.Datastore, self).__init__()

                    self.yang_name = "datastore"
                    self.yang_parent_name = "cdb"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([("pending-subscription-sync", ("pending_subscription_sync", ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync))])
                    self._child_list_classes = OrderedDict([("pending-notification-queue", ("pending_notification_queue", ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue))])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.enumeration, 'name')),
                        ('transaction_id', YLeaf(YType.str, 'transaction-id')),
                        ('write_queue', YLeaf(YType.uint32, 'write-queue')),
                        ('filename', YLeaf(YType.str, 'filename')),
                        ('disk_size', YLeaf(YType.uint64, 'disk-size')),
                        ('ram_size', YLeaf(YType.uint64, 'ram-size')),
                        ('read_locks', YLeaf(YType.uint32, 'read-locks')),
                        ('write_lock_set', YLeaf(YType.boolean, 'write-lock-set')),
                        ('subscription_lock_set', YLeaf(YType.boolean, 'subscription-lock-set')),
                        ('waiting_for_replication_sync', YLeaf(YType.boolean, 'waiting-for-replication-sync')),
                    ])
                    self.name = None
                    self.transaction_id = None
                    self.write_queue = None
                    self.filename = None
                    self.disk_size = None
                    self.ram_size = None
                    self.read_locks = None
                    self.write_lock_set = None
                    self.subscription_lock_set = None
                    self.waiting_for_replication_sync = None

                    self.pending_subscription_sync = None
                    self._children_name_map["pending_subscription_sync"] = "pending-subscription-sync"
                    self._children_yang_names.add("pending-subscription-sync")

                    self.pending_notification_queue = YList(self)
                    self._segment_path = lambda: "datastore" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/cdb/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Cdb.Datastore, ['name', 'transaction_id', 'write_queue', 'filename', 'disk_size', 'ram_size', 'read_locks', 'write_lock_set', 'subscription_lock_set', 'waiting_for_replication_sync'], name, value)


                class PendingSubscriptionSync(Entity):
                    """
                    Information pertaining to subscription notifications that have
                    been delivered to, but not yet acknowledged by, subscribing
                    clients. Not present for the 'startup' datastore.
                    
                    .. attribute:: priority
                    
                    	The priority of the subscriptions that generated the notifications that are waiting for acknowledgement. Not present for the 'operational' datastore
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: notification
                    
                    	
                    	**type**\: list of  		 :py:class:`Notification <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification>`
                    
                    .. attribute:: time_remaining
                    
                    	The remaining time in seconds until subscribing clients that have not acknowledged their notifications are considered unresponsive and will be disconnected. See /confdConfig/cdb/clientTimeout in the confd.conf(5) manual page. The value 'infinity' means that no timeout has been configured in confd.conf
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 0..18446744073709551615
                    
                    		**type**\:  :py:class:`TimeRemaining <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.TimeRemaining>`
                    
                    

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
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("notification", ("notification", ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification))])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('priority', YLeaf(YType.int32, 'priority')),
                            ('time_remaining', YLeaf(YType.str, 'time-remaining')),
                        ])
                        self.priority = None
                        self.time_remaining = None

                        self.notification = YList(self)
                        self._segment_path = lambda: "pending-subscription-sync"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync, ['priority', 'time_remaining'], name, value)

                    class TimeRemaining(Enum):
                        """
                        TimeRemaining (Enum Class)

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
                        	**type**\: str
                        
                        .. attribute:: subscription_ids
                        
                        	The subscription identifiers for the subscriptions that generated the notification
                        	**type**\: list of int
                        
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
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('client_name', YLeaf(YType.str, 'client-name')),
                                ('subscription_ids', YLeafList(YType.uint32, 'subscription-ids')),
                            ])
                            self.client_name = None
                            self.subscription_ids = []
                            self._segment_path = lambda: "notification"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification, ['client_name', 'subscription_ids'], name, value)


                class PendingNotificationQueue(Entity):
                    """
                    Queues of notifications that have been generated but not
                    yet delivered to subscribing clients. Not present for the
                    'startup' datastore.
                    
                    .. attribute:: notification
                    
                    	
                    	**type**\: list of  		 :py:class:`Notification <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue, self).__init__()

                        self.yang_name = "pending-notification-queue"
                        self.yang_parent_name = "datastore"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("notification", ("notification", ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification))])
                        self._leafs = OrderedDict()

                        self.notification = YList(self)
                        self._segment_path = lambda: "pending-notification-queue"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue, [], name, value)


                    class Notification(Entity):
                        """
                        
                        
                        .. attribute:: priority
                        
                        	The priority of the subscriptions that generated the notification. Not present for the the 'operational' datastore
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: client_name
                        
                        	The name of the client that is the recipient of the notification
                        	**type**\: str
                        
                        .. attribute:: subscription_ids
                        
                        	The subscription identifiers for the subscriptions that generated the notification
                        	**type**\: list of int
                        
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
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('priority', YLeaf(YType.int32, 'priority')),
                                ('client_name', YLeaf(YType.str, 'client-name')),
                                ('subscription_ids', YLeafList(YType.uint32, 'subscription-ids')),
                            ])
                            self.priority = None
                            self.client_name = None
                            self.subscription_ids = []
                            self._segment_path = lambda: "notification"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification, ['priority', 'client_name', 'subscription_ids'], name, value)


            class Client(Entity):
                """
                
                
                .. attribute:: name
                
                	The client name
                	**type**\: str
                
                .. attribute:: info
                
                	Additional information about the client obtained at connect time. If present, it consists of client PID and socket file descriptor number
                	**type**\: str
                
                .. attribute:: type
                
                	The type of client\: 'inactive' is a client connection without any specific state. 'client' means that the client has an active session towards a datastore. A 'subscriber' has made one or more subscriptions. 'waiting' means that the client is waiting for completion of a call such as cdb\_wait\_start()
                	**type**\:  :py:class:`Type <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Type>`
                
                .. attribute:: datastore
                
                	The name of the datastore when 'type' = 'client'. The value 'pre\_commit\_running' is the 'pseudo' datastore representing 'running' before a commit
                	**type**\: union of the below types:
                
                		**type**\:  :py:class:`DatastoreName <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.DatastoreName>`
                
                		**type**\:  :py:class:`Datastore <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Datastore>`
                
                .. attribute:: lock
                
                	Set when 'type' = 'client' and the client has requested or acquired a lock on the datastore. The 'pending\-read' and 'pending\-subscription' values indicate that the client has requested but not yet acquired the corresponding lock. A 'read' lock is never taken for the 'operational' datastore, a 'subscription' lock is never taken for any other datastore than 'operational'
                	**type**\:  :py:class:`Lock <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Lock>`
                
                .. attribute:: subscription
                
                	
                	**type**\: list of  		 :py:class:`Subscription <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Subscription>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    super(ConfdState.Internal.Cdb.Client, self).__init__()

                    self.yang_name = "client"
                    self.yang_parent_name = "cdb"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("subscription", ("subscription", ConfdState.Internal.Cdb.Client.Subscription))])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('info', YLeaf(YType.str, 'info')),
                        ('type', YLeaf(YType.enumeration, 'type')),
                        ('datastore', YLeaf(YType.str, 'datastore')),
                        ('lock', YLeaf(YType.enumeration, 'lock')),
                    ])
                    self.name = None
                    self.info = None
                    self.type = None
                    self.datastore = None
                    self.lock = None

                    self.subscription = YList(self)
                    self._segment_path = lambda: "client"
                    self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/cdb/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ConfdState.Internal.Cdb.Client, ['name', 'info', 'type', 'datastore', 'lock'], name, value)

                class Datastore(Enum):
                    """
                    Datastore (Enum Class)

                    The name of the datastore when 'type' = 'client'. The value

                    'pre\_commit\_running' is the 'pseudo' datastore representing

                    'running' before a commit.

                    .. data:: pre_commit_running = 9

                    """

                    pre_commit_running = Enum.YLeaf(9, "pre_commit_running")


                class Lock(Enum):
                    """
                    Lock (Enum Class)

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
                    Type (Enum Class)

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
                    	**type**\:  :py:class:`DatastoreName <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.DatastoreName>`
                    
                    .. attribute:: twophase
                    
                    	Present if this is a 'twophase' subscription, i.e. notifications will be delivered at 'prepare' in addition to 'commit'. Only for the 'running' datastore
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: priority
                    
                    	The priority of the subscription
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: id
                    
                    	The subscription identifier for the subscription
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: path
                    
                    	The path that the subscription pertains to
                    	**type**\: str
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem  with the subscription
                    	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xe.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Subscription.Error>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        super(ConfdState.Internal.Cdb.Client.Subscription, self).__init__()

                        self.yang_name = "subscription"
                        self.yang_parent_name = "client"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('datastore', YLeaf(YType.enumeration, 'datastore')),
                            ('twophase', YLeaf(YType.empty, 'twophase')),
                            ('priority', YLeaf(YType.int32, 'priority')),
                            ('id', YLeaf(YType.uint32, 'id')),
                            ('path', YLeaf(YType.str, 'path')),
                            ('error', YLeaf(YType.enumeration, 'error')),
                        ])
                        self.datastore = None
                        self.twophase = None
                        self.priority = None
                        self.id = None
                        self.path = None
                        self.error = None
                        self._segment_path = lambda: "subscription"
                        self._absolute_path = lambda: "tailf-confd-monitoring:confd-state/internal/cdb/client/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ConfdState.Internal.Cdb.Client.Subscription, ['datastore', 'twophase', 'priority', 'id', 'path', 'error'], name, value)

                    class Error(Enum):
                        """
                        Error (Enum Class)

                        If this leaf exists, there is a problem

                         with the subscription.

                        .. data:: PENDING = 0

                        	This value means that the subscribing client has not

                        	completed the subscription (with cdb_subscribe_done()).

                        """

                        PENDING = Enum.YLeaf(0, "PENDING")


    def clone_ptr(self):
        self._top_entity = ConfdState()
        return self._top_entity

