""" tailf_confd_monitoring 

This module defines status objects for monitoring of ConfD.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("daemon_status",
                        "epoll",
                        "read_only_mode",
                        "upgrade_mode",
                        "version") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(ConfdState, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(ConfdState, self).__setattr__(name, value)

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
            self.is_presence_container = True

            self.number_of_threads = YLeaf(YType.uint16, "number-of-threads")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("number_of_threads") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ConfdState.Smp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ConfdState.Smp, self).__setattr__(name, value)

        def has_data(self):
            return self.number_of_threads.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.number_of_threads.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "smp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-confd-monitoring:confd-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.number_of_threads.is_set or self.number_of_threads.yfilter != YFilter.not_set):
                leaf_name_data.append(self.number_of_threads.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "number-of-threads"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "number-of-threads"):
                self.number_of_threads = value
                self.number_of_threads.value_namespace = name_space
                self.number_of_threads.value_namespace_prefix = name_space_prefix


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
            self.is_presence_container = True

            self.connected_slave = YLeafList(YType.str, "connected-slave")

            self.master_node_id = YLeaf(YType.str, "master-node-id")

            self.mode = YLeaf(YType.enumeration, "mode")

            self.node_id = YLeaf(YType.str, "node-id")

            self.pending_slave = YLeafList(YType.str, "pending-slave")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("connected_slave",
                            "master_node_id",
                            "mode",
                            "node_id",
                            "pending_slave") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ConfdState.Ha, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ConfdState.Ha, self).__setattr__(name, value)

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


        def has_data(self):
            for leaf in self.connected_slave.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            for leaf in self.pending_slave.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.master_node_id.is_set or
                self.mode.is_set or
                self.node_id.is_set)

        def has_operation(self):
            for leaf in self.connected_slave.getYLeafs():
                if (leaf.is_set):
                    return True
            for leaf in self.pending_slave.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.connected_slave.yfilter != YFilter.not_set or
                self.master_node_id.yfilter != YFilter.not_set or
                self.mode.yfilter != YFilter.not_set or
                self.node_id.yfilter != YFilter.not_set or
                self.pending_slave.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ha" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-confd-monitoring:confd-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.master_node_id.is_set or self.master_node_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.master_node_id.get_name_leafdata())
            if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mode.get_name_leafdata())
            if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.node_id.get_name_leafdata())

            leaf_name_data.extend(self.connected_slave.get_name_leafdata())

            leaf_name_data.extend(self.pending_slave.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "connected-slave" or name == "master-node-id" or name == "mode" or name == "node-id" or name == "pending-slave"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "connected-slave"):
                self.connected_slave.append(value)
            if(value_path == "master-node-id"):
                self.master_node_id = value
                self.master_node_id.value_namespace = name_space
                self.master_node_id.value_namespace_prefix = name_space_prefix
            if(value_path == "mode"):
                self.mode = value
                self.mode.value_namespace = name_space
                self.mode.value_namespace_prefix = name_space_prefix
            if(value_path == "node-id"):
                self.node_id = value
                self.node_id.value_namespace = name_space
                self.node_id.value_namespace_prefix = name_space_prefix
            if(value_path == "pending-slave"):
                self.pending_slave.append(value)


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

            self.data_model = YList(self)

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
                        super(ConfdState.LoadedDataModels, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ConfdState.LoadedDataModels, self).__setattr__(name, value)


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

                self.name = YLeaf(YType.str, "name")

                self.exported_to = YLeafList(YType.str, "exported-to")

                self.exported_to_all = YLeaf(YType.empty, "exported-to-all")

                self.namespace = YLeaf(YType.str, "namespace")

                self.prefix = YLeaf(YType.str, "prefix")

                self.revision = YLeaf(YType.str, "revision")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "exported_to",
                                "exported_to_all",
                                "namespace",
                                "prefix",
                                "revision") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ConfdState.LoadedDataModels.DataModel, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ConfdState.LoadedDataModels.DataModel, self).__setattr__(name, value)

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


            def has_data(self):
                for leaf in self.exported_to.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.name.is_set or
                    self.exported_to_all.is_set or
                    self.namespace.is_set or
                    self.prefix.is_set or
                    self.revision.is_set)

            def has_operation(self):
                for leaf in self.exported_to.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.exported_to.yfilter != YFilter.not_set or
                    self.exported_to_all.yfilter != YFilter.not_set or
                    self.namespace.yfilter != YFilter.not_set or
                    self.prefix.yfilter != YFilter.not_set or
                    self.revision.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "data-model" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-confd-monitoring:confd-state/loaded-data-models/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.exported_to_all.is_set or self.exported_to_all.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.exported_to_all.get_name_leafdata())
                if (self.namespace.is_set or self.namespace.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.namespace.get_name_leafdata())
                if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prefix.get_name_leafdata())
                if (self.revision.is_set or self.revision.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.revision.get_name_leafdata())

                leaf_name_data.extend(self.exported_to.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "exported-to" or name == "exported-to-all" or name == "namespace" or name == "prefix" or name == "revision"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "exported-to"):
                    self.exported_to.append(value)
                if(value_path == "exported-to-all"):
                    self.exported_to_all = value
                    self.exported_to_all.value_namespace = name_space
                    self.exported_to_all.value_namespace_prefix = name_space_prefix
                if(value_path == "namespace"):
                    self.namespace = value
                    self.namespace.value_namespace = name_space
                    self.namespace.value_namespace_prefix = name_space_prefix
                if(value_path == "prefix"):
                    self.prefix = value
                    self.prefix.value_namespace = name_space
                    self.prefix.value_namespace_prefix = name_space_prefix
                if(value_path == "revision"):
                    self.revision = value
                    self.revision.value_namespace = name_space
                    self.revision.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.data_model:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.data_model:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "loaded-data-models" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-confd-monitoring:confd-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "data-model"):
                for c in self.data_model:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ConfdState.LoadedDataModels.DataModel()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.data_model.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "data-model"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
            self.is_presence_container = True

            self.listen = ConfdState.Netconf.Listen()
            self.listen.parent = self
            self._children_name_map["listen"] = "listen"
            self._children_yang_names.add("listen")


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

                self.ssh = YList(self)
                self.tcp = YList(self)

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
                            super(ConfdState.Netconf.Listen, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ConfdState.Netconf.Listen, self).__setattr__(name, value)


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

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Netconf.Listen.Tcp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Netconf.Listen.Tcp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.port.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tcp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/netconf/listen/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix


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

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Netconf.Listen.Ssh, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Netconf.Listen.Ssh, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.port.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ssh" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/netconf/listen/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ssh:
                    if (c.has_data()):
                        return True
                for c in self.tcp:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ssh:
                    if (c.has_operation()):
                        return True
                for c in self.tcp:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "listen" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-confd-monitoring:confd-state/netconf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ssh"):
                    for c in self.ssh:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Netconf.Listen.Ssh()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ssh.append(c)
                    return c

                if (child_yang_name == "tcp"):
                    for c in self.tcp:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Netconf.Listen.Tcp()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.tcp.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ssh" or name == "tcp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.listen is not None and self.listen.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.listen is not None and self.listen.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "netconf" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-confd-monitoring:confd-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "listen"):
                if (self.listen is None):
                    self.listen = ConfdState.Netconf.Listen()
                    self.listen.parent = self
                    self._children_name_map["listen"] = "listen"
                return self.listen

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "listen"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
            self.is_presence_container = True

            self.listen = ConfdState.Cli.Listen()
            self.listen.parent = self
            self._children_name_map["listen"] = "listen"
            self._children_yang_names.add("listen")


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

                self.ssh = YList(self)

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
                            super(ConfdState.Cli.Listen, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ConfdState.Cli.Listen, self).__setattr__(name, value)


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

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Cli.Listen.Ssh, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Cli.Listen.Ssh, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.port.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ssh" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/cli/listen/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ssh:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ssh:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "listen" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-confd-monitoring:confd-state/cli/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ssh"):
                    for c in self.ssh:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Cli.Listen.Ssh()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ssh.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ssh"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.listen is not None and self.listen.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.listen is not None and self.listen.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cli" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-confd-monitoring:confd-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "listen"):
                if (self.listen is None):
                    self.listen = ConfdState.Cli.Listen()
                    self.listen.parent = self
                    self._children_name_map["listen"] = "listen"
                return self.listen

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "listen"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
            self.is_presence_container = True

            self.listen = ConfdState.Webui.Listen()
            self.listen.parent = self
            self._children_name_map["listen"] = "listen"
            self._children_yang_names.add("listen")


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

                self.ssl = YList(self)
                self.tcp = YList(self)

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
                            super(ConfdState.Webui.Listen, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ConfdState.Webui.Listen, self).__setattr__(name, value)


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

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Webui.Listen.Tcp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Webui.Listen.Tcp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.port.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tcp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/webui/listen/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix


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

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Webui.Listen.Ssl, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Webui.Listen.Ssl, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.port.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ssl" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/webui/listen/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ssl:
                    if (c.has_data()):
                        return True
                for c in self.tcp:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ssl:
                    if (c.has_operation()):
                        return True
                for c in self.tcp:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "listen" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-confd-monitoring:confd-state/webui/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ssl"):
                    for c in self.ssl:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Webui.Listen.Ssl()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ssl.append(c)
                    return c

                if (child_yang_name == "tcp"):
                    for c in self.tcp:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Webui.Listen.Tcp()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.tcp.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ssl" or name == "tcp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.listen is not None and self.listen.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.listen is not None and self.listen.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "webui" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-confd-monitoring:confd-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "listen"):
                if (self.listen is None):
                    self.listen = ConfdState.Webui.Listen()
                    self.listen.parent = self
                    self._children_name_map["listen"] = "listen"
                return self.listen

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "listen"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
            self.is_presence_container = True

            self.listen = ConfdState.Rest.Listen()
            self.listen.parent = self
            self._children_name_map["listen"] = "listen"
            self._children_yang_names.add("listen")


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

                self.ssl = YList(self)
                self.tcp = YList(self)

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
                            super(ConfdState.Rest.Listen, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ConfdState.Rest.Listen, self).__setattr__(name, value)


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

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Rest.Listen.Tcp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Rest.Listen.Tcp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.port.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tcp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/rest/listen/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix


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

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Rest.Listen.Ssl, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Rest.Listen.Ssl, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.port.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ssl" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/rest/listen/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ssl:
                    if (c.has_data()):
                        return True
                for c in self.tcp:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ssl:
                    if (c.has_operation()):
                        return True
                for c in self.tcp:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "listen" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-confd-monitoring:confd-state/rest/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ssl"):
                    for c in self.ssl:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Rest.Listen.Ssl()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ssl.append(c)
                    return c

                if (child_yang_name == "tcp"):
                    for c in self.tcp:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Rest.Listen.Tcp()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.tcp.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ssl" or name == "tcp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.listen is not None and self.listen.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.listen is not None and self.listen.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rest" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-confd-monitoring:confd-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "listen"):
                if (self.listen is None):
                    self.listen = ConfdState.Rest.Listen()
                    self.listen.parent = self
                    self._children_name_map["listen"] = "listen"
                return self.listen

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "listen"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("engine_id",
                            "mib") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ConfdState.Snmp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ConfdState.Snmp, self).__setattr__(name, value)


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

                self.udp = YList(self)

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
                            super(ConfdState.Snmp.Listen, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ConfdState.Snmp.Listen, self).__setattr__(name, value)


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

                    self.ip = YLeaf(YType.str, "ip")

                    self.port = YLeaf(YType.uint16, "port")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "port") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Snmp.Listen.Udp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Snmp.Listen.Udp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.port.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "udp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/snmp/listen/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "port"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.udp:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.udp:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "listen" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-confd-monitoring:confd-state/snmp/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "udp"):
                    for c in self.udp:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Snmp.Listen.Udp()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.udp.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "udp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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

                self.v1 = YLeaf(YType.empty, "v1")

                self.v2c = YLeaf(YType.empty, "v2c")

                self.v3 = YLeaf(YType.empty, "v3")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("v1",
                                "v2c",
                                "v3") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ConfdState.Snmp.Version, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ConfdState.Snmp.Version, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.v1.is_set or
                    self.v2c.is_set or
                    self.v3.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.v1.yfilter != YFilter.not_set or
                    self.v2c.yfilter != YFilter.not_set or
                    self.v3.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "version" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-confd-monitoring:confd-state/snmp/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.v1.is_set or self.v1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.v1.get_name_leafdata())
                if (self.v2c.is_set or self.v2c.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.v2c.get_name_leafdata())
                if (self.v3.is_set or self.v3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.v3.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "v1" or name == "v2c" or name == "v3"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "v1"):
                    self.v1 = value
                    self.v1.value_namespace = name_space
                    self.v1.value_namespace_prefix = name_space_prefix
                if(value_path == "v2c"):
                    self.v2c = value
                    self.v2c.value_namespace = name_space
                    self.v2c.value_namespace_prefix = name_space_prefix
                if(value_path == "v3"):
                    self.v3 = value
                    self.v3.value_namespace = name_space
                    self.v3.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for leaf in self.mib.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.engine_id.is_set or
                (self.listen is not None and self.listen.has_data()) or
                (self.version is not None and self.version.has_data()))

        def has_operation(self):
            for leaf in self.mib.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.engine_id.yfilter != YFilter.not_set or
                self.mib.yfilter != YFilter.not_set or
                (self.listen is not None and self.listen.has_operation()) or
                (self.version is not None and self.version.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "snmp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-confd-monitoring:confd-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.engine_id.is_set or self.engine_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.engine_id.get_name_leafdata())

            leaf_name_data.extend(self.mib.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "listen"):
                if (self.listen is None):
                    self.listen = ConfdState.Snmp.Listen()
                    self.listen.parent = self
                    self._children_name_map["listen"] = "listen"
                return self.listen

            if (child_yang_name == "version"):
                if (self.version is None):
                    self.version = ConfdState.Snmp.Version()
                    self.version.parent = self
                    self._children_name_map["version"] = "version"
                return self.version

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "listen" or name == "version" or name == "engine-id" or name == "mib"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "engine-id"):
                self.engine_id = value
                self.engine_id.value_namespace = name_space
                self.engine_id.value_namespace_prefix = name_space_prefix
            if(value_path == "mib"):
                self.mib.append(value)


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

            self.callpoints = ConfdState.Internal.Callpoints()
            self.callpoints.parent = self
            self._children_name_map["callpoints"] = "callpoints"
            self._children_yang_names.add("callpoints")

            self.cdb = ConfdState.Internal.Cdb()
            self.cdb.parent = self
            self._children_name_map["cdb"] = "cdb"
            self._children_yang_names.add("cdb")

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
                            super(ConfdState.Internal.Callpoints, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ConfdState.Internal.Callpoints, self).__setattr__(name, value)


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

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.Callpoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("id",
                                    "error",
                                    "file",
                                    "path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Callpoints.Callpoint, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Callpoints.Callpoint, self).__setattr__(name, value)

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

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("error",
                                        "id",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.Callpoint.Daemon, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.Callpoint.Daemon, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.error.is_set or
                            self.id.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.error.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "daemon" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.error.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "error" or name == "id" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "error"):
                            self.error = value
                            self.error.value_namespace = name_space
                            self.error.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.Callpoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default",
                                        "lower",
                                        "upper") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.Callpoint.Range, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.Callpoint.Range, self).__setattr__(name, value)


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

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("error",
                                            "id",
                                            "name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Callpoints.Callpoint.Range.Daemon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Callpoints.Callpoint.Range.Daemon, self).__setattr__(name, value)

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


                        def has_data(self):
                            return (
                                self.error.is_set or
                                self.id.is_set or
                                self.name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "daemon" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "error" or name == "id" or name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.default.is_set or
                            self.lower.is_set or
                            self.upper.is_set or
                            (self.daemon is not None and self.daemon.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default.yfilter != YFilter.not_set or
                            self.lower.yfilter != YFilter.not_set or
                            self.upper.yfilter != YFilter.not_set or
                            (self.daemon is not None and self.daemon.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "range" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default.get_name_leafdata())
                        if (self.lower.is_set or self.lower.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lower.get_name_leafdata())
                        if (self.upper.is_set or self.upper.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.upper.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "daemon"):
                            if (self.daemon is None):
                                self.daemon = ConfdState.Internal.Callpoints.Callpoint.Range.Daemon()
                                self.daemon.parent = self
                                self._children_name_map["daemon"] = "daemon"
                            return self.daemon

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "daemon" or name == "default" or name == "lower" or name == "upper"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default"):
                            self.default = value
                            self.default.value_namespace = name_space
                            self.default.value_namespace_prefix = name_space_prefix
                        if(value_path == "lower"):
                            self.lower = value
                            self.lower.value_namespace = name_space
                            self.lower.value_namespace_prefix = name_space_prefix
                        if(value_path == "upper"):
                            self.upper = value
                            self.upper.value_namespace = name_space
                            self.upper.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.range:
                        if (c.has_data()):
                            return True
                    return (
                        self.id.is_set or
                        self.error.is_set or
                        self.file.is_set or
                        self.path.is_set or
                        (self.daemon is not None and self.daemon.has_data()))

                def has_operation(self):
                    for c in self.range:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set or
                        self.error.yfilter != YFilter.not_set or
                        self.file.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        (self.daemon is not None and self.daemon.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "callpoint" + "[id='" + self.id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())
                    if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error.get_name_leafdata())
                    if (self.file.is_set or self.file.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.file.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "daemon"):
                        if (self.daemon is None):
                            self.daemon = ConfdState.Internal.Callpoints.Callpoint.Daemon()
                            self.daemon.parent = self
                            self._children_name_map["daemon"] = "daemon"
                        return self.daemon

                    if (child_yang_name == "range"):
                        for c in self.range:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Callpoints.Callpoint.Range()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.range.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "daemon" or name == "range" or name == "id" or name == "error" or name == "file" or name == "path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix
                    if(value_path == "error"):
                        self.error = value
                        self.error.value_namespace = name_space
                        self.error.value_namespace_prefix = name_space_prefix
                    if(value_path == "file"):
                        self.file = value
                        self.file.value_namespace = name_space
                        self.file.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix


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

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.Validationpoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("id",
                                    "error",
                                    "file",
                                    "path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Callpoints.Validationpoint, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Callpoints.Validationpoint, self).__setattr__(name, value)

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

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("error",
                                        "id",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.Validationpoint.Daemon, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.Validationpoint.Daemon, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.error.is_set or
                            self.id.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.error.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "daemon" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.error.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "error" or name == "id" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "error"):
                            self.error = value
                            self.error.value_namespace = name_space
                            self.error.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default",
                                        "lower",
                                        "upper") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.Validationpoint.Range, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.Validationpoint.Range, self).__setattr__(name, value)


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

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("error",
                                            "id",
                                            "name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon, self).__setattr__(name, value)

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


                        def has_data(self):
                            return (
                                self.error.is_set or
                                self.id.is_set or
                                self.name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "daemon" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "error" or name == "id" or name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.default.is_set or
                            self.lower.is_set or
                            self.upper.is_set or
                            (self.daemon is not None and self.daemon.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default.yfilter != YFilter.not_set or
                            self.lower.yfilter != YFilter.not_set or
                            self.upper.yfilter != YFilter.not_set or
                            (self.daemon is not None and self.daemon.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "range" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default.get_name_leafdata())
                        if (self.lower.is_set or self.lower.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lower.get_name_leafdata())
                        if (self.upper.is_set or self.upper.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.upper.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "daemon"):
                            if (self.daemon is None):
                                self.daemon = ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon()
                                self.daemon.parent = self
                                self._children_name_map["daemon"] = "daemon"
                            return self.daemon

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "daemon" or name == "default" or name == "lower" or name == "upper"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default"):
                            self.default = value
                            self.default.value_namespace = name_space
                            self.default.value_namespace_prefix = name_space_prefix
                        if(value_path == "lower"):
                            self.lower = value
                            self.lower.value_namespace = name_space
                            self.lower.value_namespace_prefix = name_space_prefix
                        if(value_path == "upper"):
                            self.upper = value
                            self.upper.value_namespace = name_space
                            self.upper.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.range:
                        if (c.has_data()):
                            return True
                    return (
                        self.id.is_set or
                        self.error.is_set or
                        self.file.is_set or
                        self.path.is_set or
                        (self.daemon is not None and self.daemon.has_data()))

                def has_operation(self):
                    for c in self.range:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set or
                        self.error.yfilter != YFilter.not_set or
                        self.file.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        (self.daemon is not None and self.daemon.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "validationpoint" + "[id='" + self.id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())
                    if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error.get_name_leafdata())
                    if (self.file.is_set or self.file.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.file.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "daemon"):
                        if (self.daemon is None):
                            self.daemon = ConfdState.Internal.Callpoints.Validationpoint.Daemon()
                            self.daemon.parent = self
                            self._children_name_map["daemon"] = "daemon"
                        return self.daemon

                    if (child_yang_name == "range"):
                        for c in self.range:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Callpoints.Validationpoint.Range()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.range.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "daemon" or name == "range" or name == "id" or name == "error" or name == "file" or name == "path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix
                    if(value_path == "error"):
                        self.error = value
                        self.error.value_namespace = name_space
                        self.error.value_namespace_prefix = name_space_prefix
                    if(value_path == "file"):
                        self.file = value
                        self.file.value_namespace = name_space
                        self.file.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix


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

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.Actionpoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("id",
                                    "error",
                                    "file",
                                    "path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Callpoints.Actionpoint, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Callpoints.Actionpoint, self).__setattr__(name, value)

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

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("error",
                                        "id",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.Actionpoint.Daemon, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.Actionpoint.Daemon, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.error.is_set or
                            self.id.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.error.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "daemon" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.error.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "error" or name == "id" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "error"):
                            self.error = value
                            self.error.value_namespace = name_space
                            self.error.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default",
                                        "lower",
                                        "upper") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.Actionpoint.Range, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.Actionpoint.Range, self).__setattr__(name, value)


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

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("error",
                                            "id",
                                            "name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon, self).__setattr__(name, value)

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


                        def has_data(self):
                            return (
                                self.error.is_set or
                                self.id.is_set or
                                self.name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "daemon" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "error" or name == "id" or name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.default.is_set or
                            self.lower.is_set or
                            self.upper.is_set or
                            (self.daemon is not None and self.daemon.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default.yfilter != YFilter.not_set or
                            self.lower.yfilter != YFilter.not_set or
                            self.upper.yfilter != YFilter.not_set or
                            (self.daemon is not None and self.daemon.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "range" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default.get_name_leafdata())
                        if (self.lower.is_set or self.lower.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lower.get_name_leafdata())
                        if (self.upper.is_set or self.upper.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.upper.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "daemon"):
                            if (self.daemon is None):
                                self.daemon = ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon()
                                self.daemon.parent = self
                                self._children_name_map["daemon"] = "daemon"
                            return self.daemon

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "daemon" or name == "default" or name == "lower" or name == "upper"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default"):
                            self.default = value
                            self.default.value_namespace = name_space
                            self.default.value_namespace_prefix = name_space_prefix
                        if(value_path == "lower"):
                            self.lower = value
                            self.lower.value_namespace = name_space
                            self.lower.value_namespace_prefix = name_space_prefix
                        if(value_path == "upper"):
                            self.upper = value
                            self.upper.value_namespace = name_space
                            self.upper.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.range:
                        if (c.has_data()):
                            return True
                    return (
                        self.id.is_set or
                        self.error.is_set or
                        self.file.is_set or
                        self.path.is_set or
                        (self.daemon is not None and self.daemon.has_data()))

                def has_operation(self):
                    for c in self.range:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set or
                        self.error.yfilter != YFilter.not_set or
                        self.file.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        (self.daemon is not None and self.daemon.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "actionpoint" + "[id='" + self.id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())
                    if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error.get_name_leafdata())
                    if (self.file.is_set or self.file.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.file.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "daemon"):
                        if (self.daemon is None):
                            self.daemon = ConfdState.Internal.Callpoints.Actionpoint.Daemon()
                            self.daemon.parent = self
                            self._children_name_map["daemon"] = "daemon"
                        return self.daemon

                    if (child_yang_name == "range"):
                        for c in self.range:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Callpoints.Actionpoint.Range()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.range.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "daemon" or name == "range" or name == "id" or name == "error" or name == "file" or name == "path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix
                    if(value_path == "error"):
                        self.error = value
                        self.error.value_namespace = name_space
                        self.error.value_namespace_prefix = name_space_prefix
                    if(value_path == "file"):
                        self.file = value
                        self.file.value_namespace = name_space
                        self.file.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix


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

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("id",
                                    "error",
                                    "file",
                                    "path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Callpoints.SnmpInformCallback, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Callpoints.SnmpInformCallback, self).__setattr__(name, value)

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

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("error",
                                        "id",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.error.is_set or
                            self.id.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.error.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "daemon" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.error.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "error" or name == "id" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "error"):
                            self.error = value
                            self.error.value_namespace = name_space
                            self.error.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default",
                                        "lower",
                                        "upper") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.SnmpInformCallback.Range, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.SnmpInformCallback.Range, self).__setattr__(name, value)


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

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("error",
                                            "id",
                                            "name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon, self).__setattr__(name, value)

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


                        def has_data(self):
                            return (
                                self.error.is_set or
                                self.id.is_set or
                                self.name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "daemon" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "error" or name == "id" or name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.default.is_set or
                            self.lower.is_set or
                            self.upper.is_set or
                            (self.daemon is not None and self.daemon.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default.yfilter != YFilter.not_set or
                            self.lower.yfilter != YFilter.not_set or
                            self.upper.yfilter != YFilter.not_set or
                            (self.daemon is not None and self.daemon.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "range" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default.get_name_leafdata())
                        if (self.lower.is_set or self.lower.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lower.get_name_leafdata())
                        if (self.upper.is_set or self.upper.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.upper.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "daemon"):
                            if (self.daemon is None):
                                self.daemon = ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon()
                                self.daemon.parent = self
                                self._children_name_map["daemon"] = "daemon"
                            return self.daemon

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "daemon" or name == "default" or name == "lower" or name == "upper"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default"):
                            self.default = value
                            self.default.value_namespace = name_space
                            self.default.value_namespace_prefix = name_space_prefix
                        if(value_path == "lower"):
                            self.lower = value
                            self.lower.value_namespace = name_space
                            self.lower.value_namespace_prefix = name_space_prefix
                        if(value_path == "upper"):
                            self.upper = value
                            self.upper.value_namespace = name_space
                            self.upper.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.range:
                        if (c.has_data()):
                            return True
                    return (
                        self.id.is_set or
                        self.error.is_set or
                        self.file.is_set or
                        self.path.is_set or
                        (self.daemon is not None and self.daemon.has_data()))

                def has_operation(self):
                    for c in self.range:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set or
                        self.error.yfilter != YFilter.not_set or
                        self.file.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        (self.daemon is not None and self.daemon.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "snmp-inform-callback" + "[id='" + self.id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())
                    if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error.get_name_leafdata())
                    if (self.file.is_set or self.file.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.file.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "daemon"):
                        if (self.daemon is None):
                            self.daemon = ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon()
                            self.daemon.parent = self
                            self._children_name_map["daemon"] = "daemon"
                        return self.daemon

                    if (child_yang_name == "range"):
                        for c in self.range:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Callpoints.SnmpInformCallback.Range()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.range.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "daemon" or name == "range" or name == "id" or name == "error" or name == "file" or name == "path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix
                    if(value_path == "error"):
                        self.error = value
                        self.error.value_namespace = name_space
                        self.error.value_namespace_prefix = name_space_prefix
                    if(value_path == "file"):
                        self.file = value
                        self.file.value_namespace = name_space
                        self.file.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix


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

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("id",
                                    "error",
                                    "file",
                                    "path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription, self).__setattr__(name, value)

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

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("error",
                                        "id",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.error.is_set or
                            self.id.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.error.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "daemon" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.error.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "error" or name == "id" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "error"):
                            self.error = value
                            self.error.value_namespace = name_space
                            self.error.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default",
                                        "lower",
                                        "upper") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range, self).__setattr__(name, value)


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

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("error",
                                            "id",
                                            "name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon, self).__setattr__(name, value)

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


                        def has_data(self):
                            return (
                                self.error.is_set or
                                self.id.is_set or
                                self.name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "daemon" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "error" or name == "id" or name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.default.is_set or
                            self.lower.is_set or
                            self.upper.is_set or
                            (self.daemon is not None and self.daemon.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default.yfilter != YFilter.not_set or
                            self.lower.yfilter != YFilter.not_set or
                            self.upper.yfilter != YFilter.not_set or
                            (self.daemon is not None and self.daemon.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "range" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default.get_name_leafdata())
                        if (self.lower.is_set or self.lower.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lower.get_name_leafdata())
                        if (self.upper.is_set or self.upper.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.upper.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "daemon"):
                            if (self.daemon is None):
                                self.daemon = ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon()
                                self.daemon.parent = self
                                self._children_name_map["daemon"] = "daemon"
                            return self.daemon

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "daemon" or name == "default" or name == "lower" or name == "upper"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default"):
                            self.default = value
                            self.default.value_namespace = name_space
                            self.default.value_namespace_prefix = name_space_prefix
                        if(value_path == "lower"):
                            self.lower = value
                            self.lower.value_namespace = name_space
                            self.lower.value_namespace_prefix = name_space_prefix
                        if(value_path == "upper"):
                            self.upper = value
                            self.upper.value_namespace = name_space
                            self.upper.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.range:
                        if (c.has_data()):
                            return True
                    return (
                        self.id.is_set or
                        self.error.is_set or
                        self.file.is_set or
                        self.path.is_set or
                        (self.daemon is not None and self.daemon.has_data()))

                def has_operation(self):
                    for c in self.range:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set or
                        self.error.yfilter != YFilter.not_set or
                        self.file.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        (self.daemon is not None and self.daemon.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "snmp-notification-subscription" + "[id='" + self.id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())
                    if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error.get_name_leafdata())
                    if (self.file.is_set or self.file.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.file.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "daemon"):
                        if (self.daemon is None):
                            self.daemon = ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon()
                            self.daemon.parent = self
                            self._children_name_map["daemon"] = "daemon"
                        return self.daemon

                    if (child_yang_name == "range"):
                        for c in self.range:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.range.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "daemon" or name == "range" or name == "id" or name == "error" or name == "file" or name == "path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix
                    if(value_path == "error"):
                        self.error = value
                        self.error.value_namespace = name_space
                        self.error.value_namespace_prefix = name_space_prefix
                    if(value_path == "file"):
                        self.file = value
                        self.file.value_namespace = name_space
                        self.file.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix


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

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("id",
                                    "error",
                                    "file",
                                    "path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Callpoints.ErrorFormattingCallback, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Callpoints.ErrorFormattingCallback, self).__setattr__(name, value)

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

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("error",
                                        "id",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.error.is_set or
                            self.id.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.error.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "daemon" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.error.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "error" or name == "id" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "error"):
                            self.error = value
                            self.error.value_namespace = name_space
                            self.error.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default",
                                        "lower",
                                        "upper") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range, self).__setattr__(name, value)


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

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("error",
                                            "id",
                                            "name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon, self).__setattr__(name, value)

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


                        def has_data(self):
                            return (
                                self.error.is_set or
                                self.id.is_set or
                                self.name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "daemon" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "error" or name == "id" or name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.default.is_set or
                            self.lower.is_set or
                            self.upper.is_set or
                            (self.daemon is not None and self.daemon.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default.yfilter != YFilter.not_set or
                            self.lower.yfilter != YFilter.not_set or
                            self.upper.yfilter != YFilter.not_set or
                            (self.daemon is not None and self.daemon.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "range" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default.get_name_leafdata())
                        if (self.lower.is_set or self.lower.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lower.get_name_leafdata())
                        if (self.upper.is_set or self.upper.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.upper.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "daemon"):
                            if (self.daemon is None):
                                self.daemon = ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon()
                                self.daemon.parent = self
                                self._children_name_map["daemon"] = "daemon"
                            return self.daemon

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "daemon" or name == "default" or name == "lower" or name == "upper"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default"):
                            self.default = value
                            self.default.value_namespace = name_space
                            self.default.value_namespace_prefix = name_space_prefix
                        if(value_path == "lower"):
                            self.lower = value
                            self.lower.value_namespace = name_space
                            self.lower.value_namespace_prefix = name_space_prefix
                        if(value_path == "upper"):
                            self.upper = value
                            self.upper.value_namespace = name_space
                            self.upper.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.range:
                        if (c.has_data()):
                            return True
                    return (
                        self.id.is_set or
                        self.error.is_set or
                        self.file.is_set or
                        self.path.is_set or
                        (self.daemon is not None and self.daemon.has_data()))

                def has_operation(self):
                    for c in self.range:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set or
                        self.error.yfilter != YFilter.not_set or
                        self.file.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        (self.daemon is not None and self.daemon.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "error-formatting-callback" + "[id='" + self.id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())
                    if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error.get_name_leafdata())
                    if (self.file.is_set or self.file.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.file.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "daemon"):
                        if (self.daemon is None):
                            self.daemon = ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon()
                            self.daemon.parent = self
                            self._children_name_map["daemon"] = "daemon"
                        return self.daemon

                    if (child_yang_name == "range"):
                        for c in self.range:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.range.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "daemon" or name == "range" or name == "id" or name == "error" or name == "file" or name == "path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix
                    if(value_path == "error"):
                        self.error = value
                        self.error.value_namespace = name_space
                        self.error.value_namespace_prefix = name_space_prefix
                    if(value_path == "file"):
                        self.file = value
                        self.file.value_namespace = name_space
                        self.file.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix


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

                    self.id = YLeaf(YType.str, "id")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.file = YLeaf(YType.str, "file")

                    self.path = YLeaf(YType.str, "path")

                    self.daemon = ConfdState.Internal.Callpoints.Typepoint.Daemon()
                    self.daemon.parent = self
                    self._children_name_map["daemon"] = "daemon"
                    self._children_yang_names.add("daemon")

                    self.range = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("id",
                                    "error",
                                    "file",
                                    "path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Callpoints.Typepoint, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Callpoints.Typepoint, self).__setattr__(name, value)

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

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("error",
                                        "id",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.Typepoint.Daemon, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.Typepoint.Daemon, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.error.is_set or
                            self.id.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.error.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "daemon" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.error.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "error" or name == "id" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "error"):
                            self.error = value
                            self.error.value_namespace = name_space
                            self.error.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.Typepoint.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default",
                                        "lower",
                                        "upper") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.Typepoint.Range, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.Typepoint.Range, self).__setattr__(name, value)


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

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("error",
                                            "id",
                                            "name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Callpoints.Typepoint.Range.Daemon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Callpoints.Typepoint.Range.Daemon, self).__setattr__(name, value)

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


                        def has_data(self):
                            return (
                                self.error.is_set or
                                self.id.is_set or
                                self.name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "daemon" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "error" or name == "id" or name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.default.is_set or
                            self.lower.is_set or
                            self.upper.is_set or
                            (self.daemon is not None and self.daemon.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default.yfilter != YFilter.not_set or
                            self.lower.yfilter != YFilter.not_set or
                            self.upper.yfilter != YFilter.not_set or
                            (self.daemon is not None and self.daemon.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "range" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default.get_name_leafdata())
                        if (self.lower.is_set or self.lower.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lower.get_name_leafdata())
                        if (self.upper.is_set or self.upper.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.upper.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "daemon"):
                            if (self.daemon is None):
                                self.daemon = ConfdState.Internal.Callpoints.Typepoint.Range.Daemon()
                                self.daemon.parent = self
                                self._children_name_map["daemon"] = "daemon"
                            return self.daemon

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "daemon" or name == "default" or name == "lower" or name == "upper"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default"):
                            self.default = value
                            self.default.value_namespace = name_space
                            self.default.value_namespace_prefix = name_space_prefix
                        if(value_path == "lower"):
                            self.lower = value
                            self.lower.value_namespace = name_space
                            self.lower.value_namespace_prefix = name_space_prefix
                        if(value_path == "upper"):
                            self.upper = value
                            self.upper.value_namespace = name_space
                            self.upper.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.range:
                        if (c.has_data()):
                            return True
                    return (
                        self.id.is_set or
                        self.error.is_set or
                        self.file.is_set or
                        self.path.is_set or
                        (self.daemon is not None and self.daemon.has_data()))

                def has_operation(self):
                    for c in self.range:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set or
                        self.error.yfilter != YFilter.not_set or
                        self.file.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        (self.daemon is not None and self.daemon.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "typepoint" + "[id='" + self.id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())
                    if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error.get_name_leafdata())
                    if (self.file.is_set or self.file.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.file.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "daemon"):
                        if (self.daemon is None):
                            self.daemon = ConfdState.Internal.Callpoints.Typepoint.Daemon()
                            self.daemon.parent = self
                            self._children_name_map["daemon"] = "daemon"
                        return self.daemon

                    if (child_yang_name == "range"):
                        for c in self.range:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Callpoints.Typepoint.Range()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.range.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "daemon" or name == "range" or name == "id" or name == "error" or name == "file" or name == "path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix
                    if(value_path == "error"):
                        self.error = value
                        self.error.value_namespace = name_space
                        self.error.value_namespace_prefix = name_space_prefix
                    if(value_path == "file"):
                        self.file = value
                        self.file.value_namespace = name_space
                        self.file.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name",
                                    "error",
                                    "file",
                                    "path",
                                    "replay_support") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Callpoints.NotificationStreamReplay, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Callpoints.NotificationStreamReplay, self).__setattr__(name, value)

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

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("error",
                                        "id",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.error.is_set or
                            self.id.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.error.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "daemon" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.error.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "error" or name == "id" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "error"):
                            self.error = value
                            self.error.value_namespace = name_space
                            self.error.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default",
                                        "lower",
                                        "upper") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range, self).__setattr__(name, value)


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

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("error",
                                            "id",
                                            "name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon, self).__setattr__(name, value)

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


                        def has_data(self):
                            return (
                                self.error.is_set or
                                self.id.is_set or
                                self.name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "daemon" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "error" or name == "id" or name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.default.is_set or
                            self.lower.is_set or
                            self.upper.is_set or
                            (self.daemon is not None and self.daemon.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default.yfilter != YFilter.not_set or
                            self.lower.yfilter != YFilter.not_set or
                            self.upper.yfilter != YFilter.not_set or
                            (self.daemon is not None and self.daemon.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "range" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default.get_name_leafdata())
                        if (self.lower.is_set or self.lower.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lower.get_name_leafdata())
                        if (self.upper.is_set or self.upper.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.upper.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "daemon"):
                            if (self.daemon is None):
                                self.daemon = ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon()
                                self.daemon.parent = self
                                self._children_name_map["daemon"] = "daemon"
                            return self.daemon

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "daemon" or name == "default" or name == "lower" or name == "upper"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default"):
                            self.default = value
                            self.default.value_namespace = name_space
                            self.default.value_namespace_prefix = name_space_prefix
                        if(value_path == "lower"):
                            self.lower = value
                            self.lower.value_namespace = name_space
                            self.lower.value_namespace_prefix = name_space_prefix
                        if(value_path == "upper"):
                            self.upper = value
                            self.upper.value_namespace = name_space
                            self.upper.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.range:
                        if (c.has_data()):
                            return True
                    return (
                        self.name.is_set or
                        self.error.is_set or
                        self.file.is_set or
                        self.path.is_set or
                        self.replay_support.is_set or
                        (self.daemon is not None and self.daemon.has_data()))

                def has_operation(self):
                    for c in self.range:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.error.yfilter != YFilter.not_set or
                        self.file.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        self.replay_support.yfilter != YFilter.not_set or
                        (self.daemon is not None and self.daemon.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "notification-stream-replay" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error.get_name_leafdata())
                    if (self.file.is_set or self.file.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.file.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())
                    if (self.replay_support.is_set or self.replay_support.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.replay_support.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "daemon"):
                        if (self.daemon is None):
                            self.daemon = ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon()
                            self.daemon.parent = self
                            self._children_name_map["daemon"] = "daemon"
                        return self.daemon

                    if (child_yang_name == "range"):
                        for c in self.range:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Callpoints.NotificationStreamReplay.Range()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.range.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "daemon" or name == "range" or name == "name" or name == "error" or name == "file" or name == "path" or name == "replay-support"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "error"):
                        self.error = value
                        self.error.value_namespace = name_space
                        self.error.value_namespace_prefix = name_space_prefix
                    if(value_path == "file"):
                        self.file = value
                        self.file.value_namespace = name_space
                        self.file.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix
                    if(value_path == "replay-support"):
                        self.replay_support = value
                        self.replay_support.value_namespace = name_space
                        self.replay_support.value_namespace_prefix = name_space_prefix


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "error",
                                    "file",
                                    "path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Callpoints.AuthenticationCallback, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Callpoints.AuthenticationCallback, self).__setattr__(name, value)

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

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("error",
                                        "id",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.error.is_set or
                            self.id.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.error.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "daemon" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/authentication-callback/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.error.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "error" or name == "id" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "error"):
                            self.error = value
                            self.error.value_namespace = name_space
                            self.error.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default",
                                        "lower",
                                        "upper") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.AuthenticationCallback.Range, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.AuthenticationCallback.Range, self).__setattr__(name, value)


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

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("error",
                                            "id",
                                            "name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon, self).__setattr__(name, value)

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


                        def has_data(self):
                            return (
                                self.error.is_set or
                                self.id.is_set or
                                self.name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "daemon" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/authentication-callback/range/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "error" or name == "id" or name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.default.is_set or
                            self.lower.is_set or
                            self.upper.is_set or
                            (self.daemon is not None and self.daemon.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default.yfilter != YFilter.not_set or
                            self.lower.yfilter != YFilter.not_set or
                            self.upper.yfilter != YFilter.not_set or
                            (self.daemon is not None and self.daemon.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "range" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/authentication-callback/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default.get_name_leafdata())
                        if (self.lower.is_set or self.lower.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lower.get_name_leafdata())
                        if (self.upper.is_set or self.upper.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.upper.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "daemon"):
                            if (self.daemon is None):
                                self.daemon = ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon()
                                self.daemon.parent = self
                                self._children_name_map["daemon"] = "daemon"
                            return self.daemon

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "daemon" or name == "default" or name == "lower" or name == "upper"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default"):
                            self.default = value
                            self.default.value_namespace = name_space
                            self.default.value_namespace_prefix = name_space_prefix
                        if(value_path == "lower"):
                            self.lower = value
                            self.lower.value_namespace = name_space
                            self.lower.value_namespace_prefix = name_space_prefix
                        if(value_path == "upper"):
                            self.upper = value
                            self.upper.value_namespace = name_space
                            self.upper.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.range:
                        if (c.has_data()):
                            return True
                    return (
                        self.enabled.is_set or
                        self.error.is_set or
                        self.file.is_set or
                        self.path.is_set or
                        (self.daemon is not None and self.daemon.has_data()))

                def has_operation(self):
                    for c in self.range:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.error.yfilter != YFilter.not_set or
                        self.file.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        (self.daemon is not None and self.daemon.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "authentication-callback" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error.get_name_leafdata())
                    if (self.file.is_set or self.file.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.file.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "daemon"):
                        if (self.daemon is None):
                            self.daemon = ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon()
                            self.daemon.parent = self
                            self._children_name_map["daemon"] = "daemon"
                        return self.daemon

                    if (child_yang_name == "range"):
                        for c in self.range:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Callpoints.AuthenticationCallback.Range()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.range.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "daemon" or name == "range" or name == "enabled" or name == "error" or name == "file" or name == "path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "error"):
                        self.error = value
                        self.error.value_namespace = name_space
                        self.error.value_namespace_prefix = name_space_prefix
                    if(value_path == "file"):
                        self.file = value
                        self.file.value_namespace = name_space
                        self.file.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "error",
                                    "file",
                                    "path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Callpoints.AuthorizationCallbacks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Callpoints.AuthorizationCallbacks, self).__setattr__(name, value)

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

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("error",
                                        "id",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.error.is_set or
                            self.id.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.error.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "daemon" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/authorization-callbacks/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.error.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "error" or name == "id" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "error"):
                            self.error = value
                            self.error.value_namespace = name_space
                            self.error.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


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

                        self.default = YLeaf(YType.empty, "default")

                        self.lower = YLeaf(YType.str, "lower")

                        self.upper = YLeaf(YType.str, "upper")

                        self.daemon = ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon()
                        self.daemon.parent = self
                        self._children_name_map["daemon"] = "daemon"
                        self._children_yang_names.add("daemon")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default",
                                        "lower",
                                        "upper") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range, self).__setattr__(name, value)


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

                            self.error = YLeaf(YType.enumeration, "error")

                            self.id = YLeaf(YType.uint32, "id")

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("error",
                                            "id",
                                            "name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon, self).__setattr__(name, value)

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


                        def has_data(self):
                            return (
                                self.error.is_set or
                                self.id.is_set or
                                self.name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.error.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "daemon" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/authorization-callbacks/range/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.error.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "error" or name == "id" or name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "error"):
                                self.error = value
                                self.error.value_namespace = name_space
                                self.error.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.default.is_set or
                            self.lower.is_set or
                            self.upper.is_set or
                            (self.daemon is not None and self.daemon.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default.yfilter != YFilter.not_set or
                            self.lower.yfilter != YFilter.not_set or
                            self.upper.yfilter != YFilter.not_set or
                            (self.daemon is not None and self.daemon.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "range" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/authorization-callbacks/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default.get_name_leafdata())
                        if (self.lower.is_set or self.lower.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lower.get_name_leafdata())
                        if (self.upper.is_set or self.upper.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.upper.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "daemon"):
                            if (self.daemon is None):
                                self.daemon = ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon()
                                self.daemon.parent = self
                                self._children_name_map["daemon"] = "daemon"
                            return self.daemon

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "daemon" or name == "default" or name == "lower" or name == "upper"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default"):
                            self.default = value
                            self.default.value_namespace = name_space
                            self.default.value_namespace_prefix = name_space_prefix
                        if(value_path == "lower"):
                            self.lower = value
                            self.lower.value_namespace = name_space
                            self.lower.value_namespace_prefix = name_space_prefix
                        if(value_path == "upper"):
                            self.upper = value
                            self.upper.value_namespace = name_space
                            self.upper.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.range:
                        if (c.has_data()):
                            return True
                    return (
                        self.enabled.is_set or
                        self.error.is_set or
                        self.file.is_set or
                        self.path.is_set or
                        (self.daemon is not None and self.daemon.has_data()))

                def has_operation(self):
                    for c in self.range:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.error.yfilter != YFilter.not_set or
                        self.file.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        (self.daemon is not None and self.daemon.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "authorization-callbacks" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/callpoints/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error.get_name_leafdata())
                    if (self.file.is_set or self.file.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.file.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "daemon"):
                        if (self.daemon is None):
                            self.daemon = ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon()
                            self.daemon.parent = self
                            self._children_name_map["daemon"] = "daemon"
                        return self.daemon

                    if (child_yang_name == "range"):
                        for c in self.range:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.range.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "daemon" or name == "range" or name == "enabled" or name == "error" or name == "file" or name == "path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "error"):
                        self.error = value
                        self.error.value_namespace = name_space
                        self.error.value_namespace_prefix = name_space_prefix
                    if(value_path == "file"):
                        self.file = value
                        self.file.value_namespace = name_space
                        self.file.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.actionpoint:
                    if (c.has_data()):
                        return True
                for c in self.callpoint:
                    if (c.has_data()):
                        return True
                for c in self.error_formatting_callback:
                    if (c.has_data()):
                        return True
                for c in self.notification_stream_replay:
                    if (c.has_data()):
                        return True
                for c in self.snmp_inform_callback:
                    if (c.has_data()):
                        return True
                for c in self.snmp_notification_subscription:
                    if (c.has_data()):
                        return True
                for c in self.typepoint:
                    if (c.has_data()):
                        return True
                for c in self.validationpoint:
                    if (c.has_data()):
                        return True
                return (
                    (self.authentication_callback is not None) or
                    (self.authorization_callbacks is not None))

            def has_operation(self):
                for c in self.actionpoint:
                    if (c.has_operation()):
                        return True
                for c in self.callpoint:
                    if (c.has_operation()):
                        return True
                for c in self.error_formatting_callback:
                    if (c.has_operation()):
                        return True
                for c in self.notification_stream_replay:
                    if (c.has_operation()):
                        return True
                for c in self.snmp_inform_callback:
                    if (c.has_operation()):
                        return True
                for c in self.snmp_notification_subscription:
                    if (c.has_operation()):
                        return True
                for c in self.typepoint:
                    if (c.has_operation()):
                        return True
                for c in self.validationpoint:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    (self.authentication_callback is not None and self.authentication_callback.has_operation()) or
                    (self.authorization_callbacks is not None and self.authorization_callbacks.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "callpoints" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-confd-monitoring:confd-state/internal/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "actionpoint"):
                    for c in self.actionpoint:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Internal.Callpoints.Actionpoint()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.actionpoint.append(c)
                    return c

                if (child_yang_name == "authentication-callback"):
                    if (self.authentication_callback is None):
                        self.authentication_callback = ConfdState.Internal.Callpoints.AuthenticationCallback()
                        self.authentication_callback.parent = self
                        self._children_name_map["authentication_callback"] = "authentication-callback"
                    return self.authentication_callback

                if (child_yang_name == "authorization-callbacks"):
                    if (self.authorization_callbacks is None):
                        self.authorization_callbacks = ConfdState.Internal.Callpoints.AuthorizationCallbacks()
                        self.authorization_callbacks.parent = self
                        self._children_name_map["authorization_callbacks"] = "authorization-callbacks"
                    return self.authorization_callbacks

                if (child_yang_name == "callpoint"):
                    for c in self.callpoint:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Internal.Callpoints.Callpoint()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.callpoint.append(c)
                    return c

                if (child_yang_name == "error-formatting-callback"):
                    for c in self.error_formatting_callback:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Internal.Callpoints.ErrorFormattingCallback()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.error_formatting_callback.append(c)
                    return c

                if (child_yang_name == "notification-stream-replay"):
                    for c in self.notification_stream_replay:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Internal.Callpoints.NotificationStreamReplay()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.notification_stream_replay.append(c)
                    return c

                if (child_yang_name == "snmp-inform-callback"):
                    for c in self.snmp_inform_callback:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Internal.Callpoints.SnmpInformCallback()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.snmp_inform_callback.append(c)
                    return c

                if (child_yang_name == "snmp-notification-subscription"):
                    for c in self.snmp_notification_subscription:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Internal.Callpoints.SnmpNotificationSubscription()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.snmp_notification_subscription.append(c)
                    return c

                if (child_yang_name == "typepoint"):
                    for c in self.typepoint:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Internal.Callpoints.Typepoint()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.typepoint.append(c)
                    return c

                if (child_yang_name == "validationpoint"):
                    for c in self.validationpoint:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Internal.Callpoints.Validationpoint()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.validationpoint.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "actionpoint" or name == "authentication-callback" or name == "authorization-callbacks" or name == "callpoint" or name == "error-formatting-callback" or name == "notification-stream-replay" or name == "snmp-inform-callback" or name == "snmp-notification-subscription" or name == "typepoint" or name == "validationpoint"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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

                self.client = YList(self)
                self.datastore = YList(self)

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
                            super(ConfdState.Internal.Cdb, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ConfdState.Internal.Cdb, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name",
                                    "disk_size",
                                    "filename",
                                    "ram_size",
                                    "read_locks",
                                    "subscription_lock_set",
                                    "transaction_id",
                                    "waiting_for_replication_sync",
                                    "write_lock_set",
                                    "write_queue") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Cdb.Datastore, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Cdb.Datastore, self).__setattr__(name, value)


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
                        self.is_presence_container = True

                        self.priority = YLeaf(YType.int32, "priority")

                        self.time_remaining = YLeaf(YType.str, "time-remaining")

                        self.notification = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("priority",
                                        "time_remaining") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync, self).__setattr__(name, value)

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

                            self.client_name = YLeaf(YType.str, "client-name")

                            self.subscription_ids = YLeafList(YType.uint32, "subscription-ids")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("client_name",
                                            "subscription_ids") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.subscription_ids.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.client_name.is_set

                        def has_operation(self):
                            for leaf in self.subscription_ids.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.client_name.yfilter != YFilter.not_set or
                                self.subscription_ids.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "notification" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.client_name.is_set or self.client_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.client_name.get_name_leafdata())

                            leaf_name_data.extend(self.subscription_ids.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "client-name" or name == "subscription-ids"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "client-name"):
                                self.client_name = value
                                self.client_name.value_namespace = name_space
                                self.client_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "subscription-ids"):
                                self.subscription_ids.append(value)

                    def has_data(self):
                        for c in self.notification:
                            if (c.has_data()):
                                return True
                        return (
                            self.priority.is_set or
                            self.time_remaining.is_set)

                    def has_operation(self):
                        for c in self.notification:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.priority.yfilter != YFilter.not_set or
                            self.time_remaining.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pending-subscription-sync" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.priority.get_name_leafdata())
                        if (self.time_remaining.is_set or self.time_remaining.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_remaining.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "notification"):
                            for c in self.notification:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.notification.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "notification" or name == "priority" or name == "time-remaining"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "priority"):
                            self.priority = value
                            self.priority.value_namespace = name_space
                            self.priority.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-remaining"):
                            self.time_remaining = value
                            self.time_remaining.value_namespace = name_space
                            self.time_remaining.value_namespace_prefix = name_space_prefix


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

                        self.notification = YList(self)

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
                                    super(ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue, self).__setattr__(name, value)


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

                            self.client_name = YLeaf(YType.str, "client-name")

                            self.priority = YLeaf(YType.int32, "priority")

                            self.subscription_ids = YLeafList(YType.uint32, "subscription-ids")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("client_name",
                                            "priority",
                                            "subscription_ids") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.subscription_ids.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return (
                                self.client_name.is_set or
                                self.priority.is_set)

                        def has_operation(self):
                            for leaf in self.subscription_ids.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.client_name.yfilter != YFilter.not_set or
                                self.priority.yfilter != YFilter.not_set or
                                self.subscription_ids.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "notification" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.client_name.is_set or self.client_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.client_name.get_name_leafdata())
                            if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.priority.get_name_leafdata())

                            leaf_name_data.extend(self.subscription_ids.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "client-name" or name == "priority" or name == "subscription-ids"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "client-name"):
                                self.client_name = value
                                self.client_name.value_namespace = name_space
                                self.client_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "priority"):
                                self.priority = value
                                self.priority.value_namespace = name_space
                                self.priority.value_namespace_prefix = name_space_prefix
                            if(value_path == "subscription-ids"):
                                self.subscription_ids.append(value)

                    def has_data(self):
                        for c in self.notification:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.notification:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pending-notification-queue" + path_buffer

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

                        if (child_yang_name == "notification"):
                            for c in self.notification:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.notification.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "notification"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    for c in self.pending_notification_queue:
                        if (c.has_data()):
                            return True
                    return (
                        self.name.is_set or
                        self.disk_size.is_set or
                        self.filename.is_set or
                        self.ram_size.is_set or
                        self.read_locks.is_set or
                        self.subscription_lock_set.is_set or
                        self.transaction_id.is_set or
                        self.waiting_for_replication_sync.is_set or
                        self.write_lock_set.is_set or
                        self.write_queue.is_set or
                        (self.pending_subscription_sync is not None))

                def has_operation(self):
                    for c in self.pending_notification_queue:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.disk_size.yfilter != YFilter.not_set or
                        self.filename.yfilter != YFilter.not_set or
                        self.ram_size.yfilter != YFilter.not_set or
                        self.read_locks.yfilter != YFilter.not_set or
                        self.subscription_lock_set.yfilter != YFilter.not_set or
                        self.transaction_id.yfilter != YFilter.not_set or
                        self.waiting_for_replication_sync.yfilter != YFilter.not_set or
                        self.write_lock_set.yfilter != YFilter.not_set or
                        self.write_queue.yfilter != YFilter.not_set or
                        (self.pending_subscription_sync is not None and self.pending_subscription_sync.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "datastore" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/cdb/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.disk_size.is_set or self.disk_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disk_size.get_name_leafdata())
                    if (self.filename.is_set or self.filename.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.filename.get_name_leafdata())
                    if (self.ram_size.is_set or self.ram_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ram_size.get_name_leafdata())
                    if (self.read_locks.is_set or self.read_locks.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.read_locks.get_name_leafdata())
                    if (self.subscription_lock_set.is_set or self.subscription_lock_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.subscription_lock_set.get_name_leafdata())
                    if (self.transaction_id.is_set or self.transaction_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transaction_id.get_name_leafdata())
                    if (self.waiting_for_replication_sync.is_set or self.waiting_for_replication_sync.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.waiting_for_replication_sync.get_name_leafdata())
                    if (self.write_lock_set.is_set or self.write_lock_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.write_lock_set.get_name_leafdata())
                    if (self.write_queue.is_set or self.write_queue.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.write_queue.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "pending-notification-queue"):
                        for c in self.pending_notification_queue:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.pending_notification_queue.append(c)
                        return c

                    if (child_yang_name == "pending-subscription-sync"):
                        if (self.pending_subscription_sync is None):
                            self.pending_subscription_sync = ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync()
                            self.pending_subscription_sync.parent = self
                            self._children_name_map["pending_subscription_sync"] = "pending-subscription-sync"
                        return self.pending_subscription_sync

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "pending-notification-queue" or name == "pending-subscription-sync" or name == "name" or name == "disk-size" or name == "filename" or name == "ram-size" or name == "read-locks" or name == "subscription-lock-set" or name == "transaction-id" or name == "waiting-for-replication-sync" or name == "write-lock-set" or name == "write-queue"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "disk-size"):
                        self.disk_size = value
                        self.disk_size.value_namespace = name_space
                        self.disk_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "filename"):
                        self.filename = value
                        self.filename.value_namespace = name_space
                        self.filename.value_namespace_prefix = name_space_prefix
                    if(value_path == "ram-size"):
                        self.ram_size = value
                        self.ram_size.value_namespace = name_space
                        self.ram_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "read-locks"):
                        self.read_locks = value
                        self.read_locks.value_namespace = name_space
                        self.read_locks.value_namespace_prefix = name_space_prefix
                    if(value_path == "subscription-lock-set"):
                        self.subscription_lock_set = value
                        self.subscription_lock_set.value_namespace = name_space
                        self.subscription_lock_set.value_namespace_prefix = name_space_prefix
                    if(value_path == "transaction-id"):
                        self.transaction_id = value
                        self.transaction_id.value_namespace = name_space
                        self.transaction_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "waiting-for-replication-sync"):
                        self.waiting_for_replication_sync = value
                        self.waiting_for_replication_sync.value_namespace = name_space
                        self.waiting_for_replication_sync.value_namespace_prefix = name_space_prefix
                    if(value_path == "write-lock-set"):
                        self.write_lock_set = value
                        self.write_lock_set.value_namespace = name_space
                        self.write_lock_set.value_namespace_prefix = name_space_prefix
                    if(value_path == "write-queue"):
                        self.write_queue = value
                        self.write_queue.value_namespace = name_space
                        self.write_queue.value_namespace_prefix = name_space_prefix


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

                    self.datastore = YLeaf(YType.str, "datastore")

                    self.info = YLeaf(YType.str, "info")

                    self.lock = YLeaf(YType.enumeration, "lock")

                    self.name = YLeaf(YType.str, "name")

                    self.type = YLeaf(YType.enumeration, "type")

                    self.subscription = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("datastore",
                                    "info",
                                    "lock",
                                    "name",
                                    "type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ConfdState.Internal.Cdb.Client, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ConfdState.Internal.Cdb.Client, self).__setattr__(name, value)

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

                        self.datastore = YLeaf(YType.enumeration, "datastore")

                        self.error = YLeaf(YType.enumeration, "error")

                        self.id = YLeaf(YType.uint32, "id")

                        self.path = YLeaf(YType.str, "path")

                        self.priority = YLeaf(YType.int32, "priority")

                        self.twophase = YLeaf(YType.empty, "twophase")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("datastore",
                                        "error",
                                        "id",
                                        "path",
                                        "priority",
                                        "twophase") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ConfdState.Internal.Cdb.Client.Subscription, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ConfdState.Internal.Cdb.Client.Subscription, self).__setattr__(name, value)

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


                    def has_data(self):
                        return (
                            self.datastore.is_set or
                            self.error.is_set or
                            self.id.is_set or
                            self.path.is_set or
                            self.priority.is_set or
                            self.twophase.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.datastore.yfilter != YFilter.not_set or
                            self.error.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.path.yfilter != YFilter.not_set or
                            self.priority.yfilter != YFilter.not_set or
                            self.twophase.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "subscription" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "tailf-confd-monitoring:confd-state/internal/cdb/client/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.datastore.is_set or self.datastore.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.datastore.get_name_leafdata())
                        if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.error.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.path.get_name_leafdata())
                        if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.priority.get_name_leafdata())
                        if (self.twophase.is_set or self.twophase.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.twophase.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "datastore" or name == "error" or name == "id" or name == "path" or name == "priority" or name == "twophase"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "datastore"):
                            self.datastore = value
                            self.datastore.value_namespace = name_space
                            self.datastore.value_namespace_prefix = name_space_prefix
                        if(value_path == "error"):
                            self.error = value
                            self.error.value_namespace = name_space
                            self.error.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "path"):
                            self.path = value
                            self.path.value_namespace = name_space
                            self.path.value_namespace_prefix = name_space_prefix
                        if(value_path == "priority"):
                            self.priority = value
                            self.priority.value_namespace = name_space
                            self.priority.value_namespace_prefix = name_space_prefix
                        if(value_path == "twophase"):
                            self.twophase = value
                            self.twophase.value_namespace = name_space
                            self.twophase.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.subscription:
                        if (c.has_data()):
                            return True
                    return (
                        self.datastore.is_set or
                        self.info.is_set or
                        self.lock.is_set or
                        self.name.is_set or
                        self.type.is_set)

                def has_operation(self):
                    for c in self.subscription:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.datastore.yfilter != YFilter.not_set or
                        self.info.yfilter != YFilter.not_set or
                        self.lock.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "client" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "tailf-confd-monitoring:confd-state/internal/cdb/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.datastore.is_set or self.datastore.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.datastore.get_name_leafdata())
                    if (self.info.is_set or self.info.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.info.get_name_leafdata())
                    if (self.lock.is_set or self.lock.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lock.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "subscription"):
                        for c in self.subscription:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ConfdState.Internal.Cdb.Client.Subscription()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.subscription.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "subscription" or name == "datastore" or name == "info" or name == "lock" or name == "name" or name == "type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "datastore"):
                        self.datastore = value
                        self.datastore.value_namespace = name_space
                        self.datastore.value_namespace_prefix = name_space_prefix
                    if(value_path == "info"):
                        self.info = value
                        self.info.value_namespace = name_space
                        self.info.value_namespace_prefix = name_space_prefix
                    if(value_path == "lock"):
                        self.lock = value
                        self.lock.value_namespace = name_space
                        self.lock.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.client:
                    if (c.has_data()):
                        return True
                for c in self.datastore:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.client:
                    if (c.has_operation()):
                        return True
                for c in self.datastore:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cdb" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-confd-monitoring:confd-state/internal/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "client"):
                    for c in self.client:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Internal.Cdb.Client()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.client.append(c)
                    return c

                if (child_yang_name == "datastore"):
                    for c in self.datastore:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ConfdState.Internal.Cdb.Datastore()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.datastore.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "client" or name == "datastore"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.callpoints is not None and self.callpoints.has_data()) or
                (self.cdb is not None and self.cdb.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.callpoints is not None and self.callpoints.has_operation()) or
                (self.cdb is not None and self.cdb.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "internal" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-confd-monitoring:confd-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "callpoints"):
                if (self.callpoints is None):
                    self.callpoints = ConfdState.Internal.Callpoints()
                    self.callpoints.parent = self
                    self._children_name_map["callpoints"] = "callpoints"
                return self.callpoints

            if (child_yang_name == "cdb"):
                if (self.cdb is None):
                    self.cdb = ConfdState.Internal.Cdb()
                    self.cdb.parent = self
                    self._children_name_map["cdb"] = "cdb"
                return self.cdb

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "callpoints" or name == "cdb"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.daemon_status.is_set or
            self.epoll.is_set or
            self.read_only_mode.is_set or
            self.upgrade_mode.is_set or
            self.version.is_set or
            (self.internal is not None and self.internal.has_data()) or
            (self.loaded_data_models is not None and self.loaded_data_models.has_data()) or
            (self.cli is not None) or
            (self.ha is not None) or
            (self.netconf is not None) or
            (self.rest is not None) or
            (self.smp is not None) or
            (self.snmp is not None) or
            (self.webui is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.daemon_status.yfilter != YFilter.not_set or
            self.epoll.yfilter != YFilter.not_set or
            self.read_only_mode.yfilter != YFilter.not_set or
            self.upgrade_mode.yfilter != YFilter.not_set or
            self.version.yfilter != YFilter.not_set or
            (self.cli is not None and self.cli.has_operation()) or
            (self.ha is not None and self.ha.has_operation()) or
            (self.internal is not None and self.internal.has_operation()) or
            (self.loaded_data_models is not None and self.loaded_data_models.has_operation()) or
            (self.netconf is not None and self.netconf.has_operation()) or
            (self.rest is not None and self.rest.has_operation()) or
            (self.smp is not None and self.smp.has_operation()) or
            (self.snmp is not None and self.snmp.has_operation()) or
            (self.webui is not None and self.webui.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "tailf-confd-monitoring:confd-state" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.daemon_status.is_set or self.daemon_status.yfilter != YFilter.not_set):
            leaf_name_data.append(self.daemon_status.get_name_leafdata())
        if (self.epoll.is_set or self.epoll.yfilter != YFilter.not_set):
            leaf_name_data.append(self.epoll.get_name_leafdata())
        if (self.read_only_mode.is_set or self.read_only_mode.yfilter != YFilter.not_set):
            leaf_name_data.append(self.read_only_mode.get_name_leafdata())
        if (self.upgrade_mode.is_set or self.upgrade_mode.yfilter != YFilter.not_set):
            leaf_name_data.append(self.upgrade_mode.get_name_leafdata())
        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
            leaf_name_data.append(self.version.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "cli"):
            if (self.cli is None):
                self.cli = ConfdState.Cli()
                self.cli.parent = self
                self._children_name_map["cli"] = "cli"
            return self.cli

        if (child_yang_name == "ha"):
            if (self.ha is None):
                self.ha = ConfdState.Ha()
                self.ha.parent = self
                self._children_name_map["ha"] = "ha"
            return self.ha

        if (child_yang_name == "internal"):
            if (self.internal is None):
                self.internal = ConfdState.Internal()
                self.internal.parent = self
                self._children_name_map["internal"] = "internal"
            return self.internal

        if (child_yang_name == "loaded-data-models"):
            if (self.loaded_data_models is None):
                self.loaded_data_models = ConfdState.LoadedDataModels()
                self.loaded_data_models.parent = self
                self._children_name_map["loaded_data_models"] = "loaded-data-models"
            return self.loaded_data_models

        if (child_yang_name == "netconf"):
            if (self.netconf is None):
                self.netconf = ConfdState.Netconf()
                self.netconf.parent = self
                self._children_name_map["netconf"] = "netconf"
            return self.netconf

        if (child_yang_name == "rest"):
            if (self.rest is None):
                self.rest = ConfdState.Rest()
                self.rest.parent = self
                self._children_name_map["rest"] = "rest"
            return self.rest

        if (child_yang_name == "smp"):
            if (self.smp is None):
                self.smp = ConfdState.Smp()
                self.smp.parent = self
                self._children_name_map["smp"] = "smp"
            return self.smp

        if (child_yang_name == "snmp"):
            if (self.snmp is None):
                self.snmp = ConfdState.Snmp()
                self.snmp.parent = self
                self._children_name_map["snmp"] = "snmp"
            return self.snmp

        if (child_yang_name == "webui"):
            if (self.webui is None):
                self.webui = ConfdState.Webui()
                self.webui.parent = self
                self._children_name_map["webui"] = "webui"
            return self.webui

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cli" or name == "ha" or name == "internal" or name == "loaded-data-models" or name == "netconf" or name == "rest" or name == "smp" or name == "snmp" or name == "webui" or name == "daemon-status" or name == "epoll" or name == "read-only-mode" or name == "upgrade-mode" or name == "version"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "daemon-status"):
            self.daemon_status = value
            self.daemon_status.value_namespace = name_space
            self.daemon_status.value_namespace_prefix = name_space_prefix
        if(value_path == "epoll"):
            self.epoll = value
            self.epoll.value_namespace = name_space
            self.epoll.value_namespace_prefix = name_space_prefix
        if(value_path == "read-only-mode"):
            self.read_only_mode = value
            self.read_only_mode.value_namespace = name_space
            self.read_only_mode.value_namespace_prefix = name_space_prefix
        if(value_path == "upgrade-mode"):
            self.upgrade_mode = value
            self.upgrade_mode.value_namespace = name_space
            self.upgrade_mode.value_namespace_prefix = name_space_prefix
        if(value_path == "version"):
            self.version = value
            self.version.value_namespace = name_space
            self.version.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = ConfdState()
        return self._top_entity

