""" openconfig_lacp 

This module describes configuration and operational state
data for Link Aggregation Control Protocol (LACP) for
managing aggregate interfaces.   It works in conjunction with
the OpenConfig interfaces and aggregate interfaces models.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LacpActivityType(Enum):
    """
    LacpActivityType

    Describes the LACP membership type, active or passive, of the

    interface in the aggregate

    .. data:: ACTIVE = 0

    	Interface is an active member, i.e., will detect and

    	maintain aggregates

    .. data:: PASSIVE = 1

    	Interface is a passive member, i.e., it participates

    	with an active partner

    """

    ACTIVE = Enum.YLeaf(0, "ACTIVE")

    PASSIVE = Enum.YLeaf(1, "PASSIVE")


class LacpPeriodType(Enum):
    """
    LacpPeriodType

    Defines the period options for the time between sending

    LACP messages

    .. data:: FAST = 0

    	Send LACP packets every second

    .. data:: SLOW = 1

    	Send LACP packets every 30 seconds

    """

    FAST = Enum.YLeaf(0, "FAST")

    SLOW = Enum.YLeaf(1, "SLOW")


class LacpSynchronizationType(Enum):
    """
    LacpSynchronizationType

    Indicates LACP synchronization state of participant

    .. data:: IN_SYNC = 0

    	Participant is in sync with the system id and key

    	transmitted

    .. data:: OUT_SYNC = 1

    	Participant is not in sync with the system id and key

    	transmitted

    """

    IN_SYNC = Enum.YLeaf(0, "IN_SYNC")

    OUT_SYNC = Enum.YLeaf(1, "OUT_SYNC")


class LacpTimeoutType(Enum):
    """
    LacpTimeoutType

    Type of timeout used, short or long, by LACP participants

    .. data:: LONG = 0

    	Participant wishes to use long timeouts to detect

    	status of the aggregate, i.e., will expect less frequent

    	transmissions. Long timeout is 90 seconds.

    .. data:: SHORT = 1

    	Participant wishes to use short timeouts, i.e., expects

    	frequent transmissions to aggressively detect status

    	changes. Short timeout is 3 seconds.

    """

    LONG = Enum.YLeaf(0, "LONG")

    SHORT = Enum.YLeaf(1, "SHORT")



class Lacp(Entity):
    """
    Configuration and operational state data for LACP protocol
    operation on the aggregate interface
    
    .. attribute:: config
    
    	Configuration data for LACP
    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_lacp.Lacp.Config>`
    
    .. attribute:: interfaces
    
    	Enclosing container for the list of LACP\-enabled interfaces
    	**type**\:   :py:class:`Interfaces <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces>`
    
    .. attribute:: state
    
    	Operational state data for LACP
    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_lacp.Lacp.State>`
    
    

    """

    _prefix = 'oc-lacp'
    _revision = '2016-05-26'

    def __init__(self):
        super(Lacp, self).__init__()
        self._top_entity = None

        self.yang_name = "lacp"
        self.yang_parent_name = "openconfig-lacp"

        self.config = Lacp.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._children_yang_names.add("config")

        self.interfaces = Lacp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.state = Lacp.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"
        self._children_yang_names.add("state")


    class Config(Entity):
        """
        Configuration data for LACP
        
        .. attribute:: system_priority
        
        	Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system
        	**type**\:  int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'oc-lacp'
        _revision = '2016-05-26'

        def __init__(self):
            super(Lacp.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "lacp"

            self.system_priority = YLeaf(YType.uint16, "system-priority")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("system_priority") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Lacp.Config, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Lacp.Config, self).__setattr__(name, value)

        def has_data(self):
            return self.system_priority.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.system_priority.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "config" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-lacp:lacp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.system_priority.is_set or self.system_priority.yfilter != YFilter.not_set):
                leaf_name_data.append(self.system_priority.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "system-priority"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "system-priority"):
                self.system_priority = value
                self.system_priority.value_namespace = name_space
                self.system_priority.value_namespace_prefix = name_space_prefix


    class State(Entity):
        """
        Operational state data for LACP
        
        .. attribute:: system_priority
        
        	Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system
        	**type**\:  int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'oc-lacp'
        _revision = '2016-05-26'

        def __init__(self):
            super(Lacp.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "lacp"

            self.system_priority = YLeaf(YType.uint16, "system-priority")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("system_priority") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Lacp.State, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Lacp.State, self).__setattr__(name, value)

        def has_data(self):
            return self.system_priority.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.system_priority.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "state" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-lacp:lacp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.system_priority.is_set or self.system_priority.yfilter != YFilter.not_set):
                leaf_name_data.append(self.system_priority.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "system-priority"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "system-priority"):
                self.system_priority = value
                self.system_priority.value_namespace = name_space
                self.system_priority.value_namespace_prefix = name_space_prefix


    class Interfaces(Entity):
        """
        Enclosing container for the list of LACP\-enabled
        interfaces
        
        .. attribute:: interface
        
        	List of aggregate interfaces managed by LACP
        	**type**\: list of    :py:class:`Interface <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface>`
        
        

        """

        _prefix = 'oc-lacp'
        _revision = '2016-05-26'

        def __init__(self):
            super(Lacp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "lacp"

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
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Lacp.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Lacp.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            List of aggregate interfaces managed by LACP
            
            .. attribute:: name  <key>
            
            	Reference to the list key
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Config>`
            
            .. attribute:: config
            
            	Configuration data for each LACP aggregate interface
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Config>`
            
            .. attribute:: members
            
            	Enclosing container for the list of members interfaces of the aggregate. This list is considered operational state only so is labeled config false and has no config container
            	**type**\:   :py:class:`Members <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Members>`
            
            .. attribute:: state
            
            	Operational state data for each LACP aggregate interface
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.State>`
            
            

            """

            _prefix = 'oc-lacp'
            _revision = '2016-05-26'

            def __init__(self):
                super(Lacp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.name = YLeaf(YType.str, "name")

                self.config = Lacp.Interfaces.Interface.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.members = Lacp.Interfaces.Interface.Members()
                self.members.parent = self
                self._children_name_map["members"] = "members"
                self._children_yang_names.add("members")

                self.state = Lacp.Interfaces.Interface.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Lacp.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lacp.Interfaces.Interface, self).__setattr__(name, value)


            class Config(Entity):
                """
                Configuration data for each LACP aggregate interface
                
                .. attribute:: interval
                
                	Set the period between LACP messages \-\- uses the lacp\-period\-type enumeration
                	**type**\:   :py:class:`LacpPeriodType <ydk.models.openconfig.openconfig_lacp.LacpPeriodType>`
                
                	**default value**\: SLOW
                
                .. attribute:: lacp_mode
                
                	ACTIVE is to initiate the transmission of LACP packets. PASSIVE is to wait for peer to initiate the transmission of LACP packets
                	**type**\:   :py:class:`LacpActivityType <ydk.models.openconfig.openconfig_lacp.LacpActivityType>`
                
                	**default value**\: ACTIVE
                
                .. attribute:: name
                
                	Reference to the interface on which LACP should be configured.   The type of the target interface must be ieee8023adLag
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: system_id_mac
                
                	The MAC address portion of the node's System ID. This is combined with the system priority to construct the 8\-octet system\-id
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: system_priority
                
                	Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'oc-lacp'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Lacp.Interfaces.Interface.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "interface"

                    self.interval = YLeaf(YType.enumeration, "interval")

                    self.lacp_mode = YLeaf(YType.enumeration, "lacp-mode")

                    self.name = YLeaf(YType.str, "name")

                    self.system_id_mac = YLeaf(YType.str, "system-id-mac")

                    self.system_priority = YLeaf(YType.uint16, "system-priority")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interval",
                                    "lacp_mode",
                                    "name",
                                    "system_id_mac",
                                    "system_priority") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Lacp.Interfaces.Interface.Config, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Lacp.Interfaces.Interface.Config, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interval.is_set or
                        self.lacp_mode.is_set or
                        self.name.is_set or
                        self.system_id_mac.is_set or
                        self.system_priority.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interval.yfilter != YFilter.not_set or
                        self.lacp_mode.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.system_id_mac.yfilter != YFilter.not_set or
                        self.system_priority.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "config" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interval.get_name_leafdata())
                    if (self.lacp_mode.is_set or self.lacp_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lacp_mode.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.system_id_mac.is_set or self.system_id_mac.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.system_id_mac.get_name_leafdata())
                    if (self.system_priority.is_set or self.system_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.system_priority.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interval" or name == "lacp-mode" or name == "name" or name == "system-id-mac" or name == "system-priority"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interval"):
                        self.interval = value
                        self.interval.value_namespace = name_space
                        self.interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "lacp-mode"):
                        self.lacp_mode = value
                        self.lacp_mode.value_namespace = name_space
                        self.lacp_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "system-id-mac"):
                        self.system_id_mac = value
                        self.system_id_mac.value_namespace = name_space
                        self.system_id_mac.value_namespace_prefix = name_space_prefix
                    if(value_path == "system-priority"):
                        self.system_priority = value
                        self.system_priority.value_namespace = name_space
                        self.system_priority.value_namespace_prefix = name_space_prefix


            class State(Entity):
                """
                Operational state data for each LACP aggregate
                interface
                
                .. attribute:: interval
                
                	Set the period between LACP messages \-\- uses the lacp\-period\-type enumeration
                	**type**\:   :py:class:`LacpPeriodType <ydk.models.openconfig.openconfig_lacp.LacpPeriodType>`
                
                	**default value**\: SLOW
                
                .. attribute:: lacp_mode
                
                	ACTIVE is to initiate the transmission of LACP packets. PASSIVE is to wait for peer to initiate the transmission of LACP packets
                	**type**\:   :py:class:`LacpActivityType <ydk.models.openconfig.openconfig_lacp.LacpActivityType>`
                
                	**default value**\: ACTIVE
                
                .. attribute:: name
                
                	Reference to the interface on which LACP should be configured.   The type of the target interface must be ieee8023adLag
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: system_id_mac
                
                	The MAC address portion of the node's System ID. This is combined with the system priority to construct the 8\-octet system\-id
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: system_priority
                
                	Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'oc-lacp'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Lacp.Interfaces.Interface.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "interface"

                    self.interval = YLeaf(YType.enumeration, "interval")

                    self.lacp_mode = YLeaf(YType.enumeration, "lacp-mode")

                    self.name = YLeaf(YType.str, "name")

                    self.system_id_mac = YLeaf(YType.str, "system-id-mac")

                    self.system_priority = YLeaf(YType.uint16, "system-priority")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interval",
                                    "lacp_mode",
                                    "name",
                                    "system_id_mac",
                                    "system_priority") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Lacp.Interfaces.Interface.State, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Lacp.Interfaces.Interface.State, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interval.is_set or
                        self.lacp_mode.is_set or
                        self.name.is_set or
                        self.system_id_mac.is_set or
                        self.system_priority.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interval.yfilter != YFilter.not_set or
                        self.lacp_mode.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.system_id_mac.yfilter != YFilter.not_set or
                        self.system_priority.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "state" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interval.get_name_leafdata())
                    if (self.lacp_mode.is_set or self.lacp_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lacp_mode.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.system_id_mac.is_set or self.system_id_mac.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.system_id_mac.get_name_leafdata())
                    if (self.system_priority.is_set or self.system_priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.system_priority.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interval" or name == "lacp-mode" or name == "name" or name == "system-id-mac" or name == "system-priority"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interval"):
                        self.interval = value
                        self.interval.value_namespace = name_space
                        self.interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "lacp-mode"):
                        self.lacp_mode = value
                        self.lacp_mode.value_namespace = name_space
                        self.lacp_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "system-id-mac"):
                        self.system_id_mac = value
                        self.system_id_mac.value_namespace = name_space
                        self.system_id_mac.value_namespace_prefix = name_space_prefix
                    if(value_path == "system-priority"):
                        self.system_priority = value
                        self.system_priority.value_namespace = name_space
                        self.system_priority.value_namespace_prefix = name_space_prefix


            class Members(Entity):
                """
                Enclosing container for the list of members interfaces of
                the aggregate. This list is considered operational state
                only so is labeled config false and has no config container
                
                .. attribute:: member
                
                	List of member interfaces and their associated status for a LACP\-controlled aggregate interface.  Member list is not configurable here \-\- each interface indicates items its participation in the LAG
                	**type**\: list of    :py:class:`Member <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Members.Member>`
                
                

                """

                _prefix = 'oc-lacp'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Lacp.Interfaces.Interface.Members, self).__init__()

                    self.yang_name = "members"
                    self.yang_parent_name = "interface"

                    self.member = YList(self)

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
                                super(Lacp.Interfaces.Interface.Members, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Lacp.Interfaces.Interface.Members, self).__setattr__(name, value)


                class Member(Entity):
                    """
                    List of member interfaces and their associated status for
                    a LACP\-controlled aggregate interface.  Member list is not
                    configurable here \-\- each interface indicates items
                    its participation in the LAG.
                    
                    .. attribute:: interface  <key>
                    
                    	Reference to aggregate member interface
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`interface <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Members.Member.State>`
                    
                    .. attribute:: state
                    
                    	Operational state data for aggregate members
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Members.Member.State>`
                    
                    

                    """

                    _prefix = 'oc-lacp'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Lacp.Interfaces.Interface.Members.Member, self).__init__()

                        self.yang_name = "member"
                        self.yang_parent_name = "members"

                        self.interface = YLeaf(YType.str, "interface")

                        self.state = Lacp.Interfaces.Interface.Members.Member.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Lacp.Interfaces.Interface.Members.Member, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Lacp.Interfaces.Interface.Members.Member, self).__setattr__(name, value)


                    class State(Entity):
                        """
                        Operational state data for aggregate members
                        
                        .. attribute:: activity
                        
                        	Indicates participant is active or passive
                        	**type**\:   :py:class:`LacpActivityType <ydk.models.openconfig.openconfig_lacp.LacpActivityType>`
                        
                        .. attribute:: aggregatable
                        
                        	A true value indicates that the participant will allow the link to be used as part of the aggregate. A false value indicates the link should be used as an individual link
                        	**type**\:  bool
                        
                        .. attribute:: collecting
                        
                        	If true, the participant is collecting incoming frames on the link, otherwise false
                        	**type**\:  bool
                        
                        .. attribute:: counters
                        
                        	LACP protocol counters
                        	**type**\:   :py:class:`Counters <ydk.models.openconfig.openconfig_lacp.Lacp.Interfaces.Interface.Members.Member.State.Counters>`
                        
                        .. attribute:: distributing
                        
                        	When true, the participant is distributing outgoing frames; when false, distribution is disabled
                        	**type**\:  bool
                        
                        .. attribute:: interface
                        
                        	Reference to interface member of the LACP aggregate
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                        
                        .. attribute:: oper_key
                        
                        	Current operational value of the key for the aggregate interface
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: partner_id
                        
                        	MAC address representing the protocol partner's interface system ID
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: partner_key
                        
                        	Operational value of the protocol partner's key
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: synchronization
                        
                        	Indicates whether the participant is in\-sync or out\-of\-sync
                        	**type**\:   :py:class:`LacpSynchronizationType <ydk.models.openconfig.openconfig_lacp.LacpSynchronizationType>`
                        
                        .. attribute:: system_id
                        
                        	MAC address that defines the local system ID for the aggregate interface
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: timeout
                        
                        	The timeout type (short or long) used by the participant
                        	**type**\:   :py:class:`LacpTimeoutType <ydk.models.openconfig.openconfig_lacp.LacpTimeoutType>`
                        
                        

                        """

                        _prefix = 'oc-lacp'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Lacp.Interfaces.Interface.Members.Member.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "member"

                            self.activity = YLeaf(YType.enumeration, "activity")

                            self.aggregatable = YLeaf(YType.boolean, "aggregatable")

                            self.collecting = YLeaf(YType.boolean, "collecting")

                            self.distributing = YLeaf(YType.boolean, "distributing")

                            self.interface = YLeaf(YType.str, "interface")

                            self.oper_key = YLeaf(YType.uint16, "oper-key")

                            self.partner_id = YLeaf(YType.str, "partner-id")

                            self.partner_key = YLeaf(YType.uint16, "partner-key")

                            self.synchronization = YLeaf(YType.enumeration, "synchronization")

                            self.system_id = YLeaf(YType.str, "system-id")

                            self.timeout = YLeaf(YType.enumeration, "timeout")

                            self.counters = Lacp.Interfaces.Interface.Members.Member.State.Counters()
                            self.counters.parent = self
                            self._children_name_map["counters"] = "counters"
                            self._children_yang_names.add("counters")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("activity",
                                            "aggregatable",
                                            "collecting",
                                            "distributing",
                                            "interface",
                                            "oper_key",
                                            "partner_id",
                                            "partner_key",
                                            "synchronization",
                                            "system_id",
                                            "timeout") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Lacp.Interfaces.Interface.Members.Member.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Lacp.Interfaces.Interface.Members.Member.State, self).__setattr__(name, value)


                        class Counters(Entity):
                            """
                            LACP protocol counters
                            
                            .. attribute:: lacp_errors
                            
                            	Number of LACPDU illegal packet errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lacp_in_pkts
                            
                            	Number of LACPDUs received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lacp_out_pkts
                            
                            	Number of LACPDUs transmitted
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lacp_rx_errors
                            
                            	Number of LACPDU receive packet errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lacp_tx_errors
                            
                            	Number of LACPDU transmit packet errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: lacp_unknown_errors
                            
                            	Number of LACPDU unknown packet errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'oc-lacp'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Lacp.Interfaces.Interface.Members.Member.State.Counters, self).__init__()

                                self.yang_name = "counters"
                                self.yang_parent_name = "state"

                                self.lacp_errors = YLeaf(YType.uint64, "lacp-errors")

                                self.lacp_in_pkts = YLeaf(YType.uint64, "lacp-in-pkts")

                                self.lacp_out_pkts = YLeaf(YType.uint64, "lacp-out-pkts")

                                self.lacp_rx_errors = YLeaf(YType.uint64, "lacp-rx-errors")

                                self.lacp_tx_errors = YLeaf(YType.uint64, "lacp-tx-errors")

                                self.lacp_unknown_errors = YLeaf(YType.uint64, "lacp-unknown-errors")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("lacp_errors",
                                                "lacp_in_pkts",
                                                "lacp_out_pkts",
                                                "lacp_rx_errors",
                                                "lacp_tx_errors",
                                                "lacp_unknown_errors") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Lacp.Interfaces.Interface.Members.Member.State.Counters, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Lacp.Interfaces.Interface.Members.Member.State.Counters, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.lacp_errors.is_set or
                                    self.lacp_in_pkts.is_set or
                                    self.lacp_out_pkts.is_set or
                                    self.lacp_rx_errors.is_set or
                                    self.lacp_tx_errors.is_set or
                                    self.lacp_unknown_errors.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.lacp_errors.yfilter != YFilter.not_set or
                                    self.lacp_in_pkts.yfilter != YFilter.not_set or
                                    self.lacp_out_pkts.yfilter != YFilter.not_set or
                                    self.lacp_rx_errors.yfilter != YFilter.not_set or
                                    self.lacp_tx_errors.yfilter != YFilter.not_set or
                                    self.lacp_unknown_errors.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "counters" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.lacp_errors.is_set or self.lacp_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lacp_errors.get_name_leafdata())
                                if (self.lacp_in_pkts.is_set or self.lacp_in_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lacp_in_pkts.get_name_leafdata())
                                if (self.lacp_out_pkts.is_set or self.lacp_out_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lacp_out_pkts.get_name_leafdata())
                                if (self.lacp_rx_errors.is_set or self.lacp_rx_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lacp_rx_errors.get_name_leafdata())
                                if (self.lacp_tx_errors.is_set or self.lacp_tx_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lacp_tx_errors.get_name_leafdata())
                                if (self.lacp_unknown_errors.is_set or self.lacp_unknown_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lacp_unknown_errors.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "lacp-errors" or name == "lacp-in-pkts" or name == "lacp-out-pkts" or name == "lacp-rx-errors" or name == "lacp-tx-errors" or name == "lacp-unknown-errors"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "lacp-errors"):
                                    self.lacp_errors = value
                                    self.lacp_errors.value_namespace = name_space
                                    self.lacp_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "lacp-in-pkts"):
                                    self.lacp_in_pkts = value
                                    self.lacp_in_pkts.value_namespace = name_space
                                    self.lacp_in_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "lacp-out-pkts"):
                                    self.lacp_out_pkts = value
                                    self.lacp_out_pkts.value_namespace = name_space
                                    self.lacp_out_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "lacp-rx-errors"):
                                    self.lacp_rx_errors = value
                                    self.lacp_rx_errors.value_namespace = name_space
                                    self.lacp_rx_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "lacp-tx-errors"):
                                    self.lacp_tx_errors = value
                                    self.lacp_tx_errors.value_namespace = name_space
                                    self.lacp_tx_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "lacp-unknown-errors"):
                                    self.lacp_unknown_errors = value
                                    self.lacp_unknown_errors.value_namespace = name_space
                                    self.lacp_unknown_errors.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.activity.is_set or
                                self.aggregatable.is_set or
                                self.collecting.is_set or
                                self.distributing.is_set or
                                self.interface.is_set or
                                self.oper_key.is_set or
                                self.partner_id.is_set or
                                self.partner_key.is_set or
                                self.synchronization.is_set or
                                self.system_id.is_set or
                                self.timeout.is_set or
                                (self.counters is not None and self.counters.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.activity.yfilter != YFilter.not_set or
                                self.aggregatable.yfilter != YFilter.not_set or
                                self.collecting.yfilter != YFilter.not_set or
                                self.distributing.yfilter != YFilter.not_set or
                                self.interface.yfilter != YFilter.not_set or
                                self.oper_key.yfilter != YFilter.not_set or
                                self.partner_id.yfilter != YFilter.not_set or
                                self.partner_key.yfilter != YFilter.not_set or
                                self.synchronization.yfilter != YFilter.not_set or
                                self.system_id.yfilter != YFilter.not_set or
                                self.timeout.yfilter != YFilter.not_set or
                                (self.counters is not None and self.counters.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "state" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.activity.is_set or self.activity.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.activity.get_name_leafdata())
                            if (self.aggregatable.is_set or self.aggregatable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.aggregatable.get_name_leafdata())
                            if (self.collecting.is_set or self.collecting.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.collecting.get_name_leafdata())
                            if (self.distributing.is_set or self.distributing.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.distributing.get_name_leafdata())
                            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface.get_name_leafdata())
                            if (self.oper_key.is_set or self.oper_key.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.oper_key.get_name_leafdata())
                            if (self.partner_id.is_set or self.partner_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.partner_id.get_name_leafdata())
                            if (self.partner_key.is_set or self.partner_key.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.partner_key.get_name_leafdata())
                            if (self.synchronization.is_set or self.synchronization.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.synchronization.get_name_leafdata())
                            if (self.system_id.is_set or self.system_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.system_id.get_name_leafdata())
                            if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.timeout.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "counters"):
                                if (self.counters is None):
                                    self.counters = Lacp.Interfaces.Interface.Members.Member.State.Counters()
                                    self.counters.parent = self
                                    self._children_name_map["counters"] = "counters"
                                return self.counters

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "counters" or name == "activity" or name == "aggregatable" or name == "collecting" or name == "distributing" or name == "interface" or name == "oper-key" or name == "partner-id" or name == "partner-key" or name == "synchronization" or name == "system-id" or name == "timeout"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "activity"):
                                self.activity = value
                                self.activity.value_namespace = name_space
                                self.activity.value_namespace_prefix = name_space_prefix
                            if(value_path == "aggregatable"):
                                self.aggregatable = value
                                self.aggregatable.value_namespace = name_space
                                self.aggregatable.value_namespace_prefix = name_space_prefix
                            if(value_path == "collecting"):
                                self.collecting = value
                                self.collecting.value_namespace = name_space
                                self.collecting.value_namespace_prefix = name_space_prefix
                            if(value_path == "distributing"):
                                self.distributing = value
                                self.distributing.value_namespace = name_space
                                self.distributing.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface"):
                                self.interface = value
                                self.interface.value_namespace = name_space
                                self.interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "oper-key"):
                                self.oper_key = value
                                self.oper_key.value_namespace = name_space
                                self.oper_key.value_namespace_prefix = name_space_prefix
                            if(value_path == "partner-id"):
                                self.partner_id = value
                                self.partner_id.value_namespace = name_space
                                self.partner_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "partner-key"):
                                self.partner_key = value
                                self.partner_key.value_namespace = name_space
                                self.partner_key.value_namespace_prefix = name_space_prefix
                            if(value_path == "synchronization"):
                                self.synchronization = value
                                self.synchronization.value_namespace = name_space
                                self.synchronization.value_namespace_prefix = name_space_prefix
                            if(value_path == "system-id"):
                                self.system_id = value
                                self.system_id.value_namespace = name_space
                                self.system_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "timeout"):
                                self.timeout = value
                                self.timeout.value_namespace = name_space
                                self.timeout.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            (self.state is not None and self.state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "member" + "[interface='" + self.interface.get() + "']" + path_buffer

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

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = Lacp.Interfaces.Interface.Members.Member.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "state" or name == "interface"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.member:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.member:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "members" + path_buffer

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

                    if (child_yang_name == "member"):
                        for c in self.member:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Lacp.Interfaces.Interface.Members.Member()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.member.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "member"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.name.is_set or
                    (self.config is not None and self.config.has_data()) or
                    (self.members is not None and self.members.has_data()) or
                    (self.state is not None and self.state.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()) or
                    (self.members is not None and self.members.has_operation()) or
                    (self.state is not None and self.state.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-lacp:lacp/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = Lacp.Interfaces.Interface.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                if (child_yang_name == "members"):
                    if (self.members is None):
                        self.members = Lacp.Interfaces.Interface.Members()
                        self.members.parent = self
                        self._children_name_map["members"] = "members"
                    return self.members

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = Lacp.Interfaces.Interface.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "members" or name == "state" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-lacp:lacp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

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
                c = Lacp.Interfaces.Interface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.config is not None and self.config.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.state is not None and self.state.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.config is not None and self.config.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.state is not None and self.state.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "openconfig-lacp:lacp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "config"):
            if (self.config is None):
                self.config = Lacp.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
            return self.config

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = Lacp.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "state"):
            if (self.state is None):
                self.state = Lacp.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
            return self.state

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "config" or name == "interfaces" or name == "state"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Lacp()
        return self._top_entity

