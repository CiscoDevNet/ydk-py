""" openconfig_vlan 

This module defines configuration and state variables for VLANs,
in addition to VLAN parameters associated with interfaces

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Vlans(Entity):
    """
    Container for VLAN configuration and state
    variables
    
    .. attribute:: vlan
    
    	Configured VLANs keyed by id
    	**type**\: list of    :py:class:`Vlan <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan>`
    
    

    """

    _prefix = 'oc-vlan'
    _revision = '2016-05-26'

    def __init__(self):
        super(Vlans, self).__init__()
        self._top_entity = None

        self.yang_name = "vlans"
        self.yang_parent_name = "openconfig-vlan"

        self.vlan = YList(self)

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
                    super(Vlans, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Vlans, self).__setattr__(name, value)


    class Vlan(Entity):
        """
        Configured VLANs keyed by id
        
        .. attribute:: vlan_id  <key>
        
        	references the configured vlan\-id
        	**type**\:  int
        
        	**range:** 1..4094
        
        	**refers to**\:  :py:class:`vlan_id <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Config>`
        
        .. attribute:: config
        
        	Configuration parameters for VLANs
        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Config>`
        
        .. attribute:: members
        
        	Enclosing container for list of member interfaces
        	**type**\:   :py:class:`Members <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Members>`
        
        .. attribute:: state
        
        	State variables for VLANs
        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.State>`
        
        

        """

        _prefix = 'oc-vlan'
        _revision = '2016-05-26'

        def __init__(self):
            super(Vlans.Vlan, self).__init__()

            self.yang_name = "vlan"
            self.yang_parent_name = "vlans"

            self.vlan_id = YLeaf(YType.str, "vlan-id")

            self.config = Vlans.Vlan.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"
            self._children_yang_names.add("config")

            self.members = Vlans.Vlan.Members()
            self.members.parent = self
            self._children_name_map["members"] = "members"
            self._children_yang_names.add("members")

            self.state = Vlans.Vlan.State()
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
                if name in ("vlan_id") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vlans.Vlan, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vlans.Vlan, self).__setattr__(name, value)


        class Config(Entity):
            """
            Configuration parameters for VLANs
            
            .. attribute:: name
            
            	Interface VLAN name
            	**type**\:  str
            
            .. attribute:: status
            
            	Admin state of the VLAN
            	**type**\:   :py:class:`Status <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Config.Status>`
            
            	**default value**\: ACTIVE
            
            .. attribute:: tpid
            
            	Optionally set the tag protocol identifier field (TPID) that is accepted on the VLAN
            	**type**\:   :py:class:`Tpid_Types <ydk.models.openconfig.openconfig_vlan_types.Tpid_Types>`
            
            	**default value**\: oc-vlan-types:TPID_0x8100
            
            .. attribute:: vlan_id
            
            	Interface VLAN id
            	**type**\:  int
            
            	**range:** 1..4094
            
            

            """

            _prefix = 'oc-vlan'
            _revision = '2016-05-26'

            def __init__(self):
                super(Vlans.Vlan.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "vlan"

                self.name = YLeaf(YType.str, "name")

                self.status = YLeaf(YType.enumeration, "status")

                self.tpid = YLeaf(YType.identityref, "tpid")

                self.vlan_id = YLeaf(YType.uint16, "vlan-id")

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
                                "status",
                                "tpid",
                                "vlan_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vlans.Vlan.Config, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vlans.Vlan.Config, self).__setattr__(name, value)

            class Status(Enum):
                """
                Status

                Admin state of the VLAN

                .. data:: ACTIVE = 0

                	VLAN is active

                .. data:: SUSPENDED = 1

                	VLAN is inactive / suspended

                """

                ACTIVE = Enum.YLeaf(0, "ACTIVE")

                SUSPENDED = Enum.YLeaf(1, "SUSPENDED")


            def has_data(self):
                return (
                    self.name.is_set or
                    self.status.is_set or
                    self.tpid.is_set or
                    self.vlan_id.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.status.yfilter != YFilter.not_set or
                    self.tpid.yfilter != YFilter.not_set or
                    self.vlan_id.yfilter != YFilter.not_set)

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
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.status.get_name_leafdata())
                if (self.tpid.is_set or self.tpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tpid.get_name_leafdata())
                if (self.vlan_id.is_set or self.vlan_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlan_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "status" or name == "tpid" or name == "vlan-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "status"):
                    self.status = value
                    self.status.value_namespace = name_space
                    self.status.value_namespace_prefix = name_space_prefix
                if(value_path == "tpid"):
                    self.tpid = value
                    self.tpid.value_namespace = name_space
                    self.tpid.value_namespace_prefix = name_space_prefix
                if(value_path == "vlan-id"):
                    self.vlan_id = value
                    self.vlan_id.value_namespace = name_space
                    self.vlan_id.value_namespace_prefix = name_space_prefix


        class State(Entity):
            """
            State variables for VLANs
            
            .. attribute:: name
            
            	Interface VLAN name
            	**type**\:  str
            
            .. attribute:: status
            
            	Admin state of the VLAN
            	**type**\:   :py:class:`Status <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.State.Status>`
            
            	**default value**\: ACTIVE
            
            .. attribute:: tpid
            
            	Optionally set the tag protocol identifier field (TPID) that is accepted on the VLAN
            	**type**\:   :py:class:`Tpid_Types <ydk.models.openconfig.openconfig_vlan_types.Tpid_Types>`
            
            	**default value**\: oc-vlan-types:TPID_0x8100
            
            .. attribute:: vlan_id
            
            	Interface VLAN id
            	**type**\:  int
            
            	**range:** 1..4094
            
            

            """

            _prefix = 'oc-vlan'
            _revision = '2016-05-26'

            def __init__(self):
                super(Vlans.Vlan.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "vlan"

                self.name = YLeaf(YType.str, "name")

                self.status = YLeaf(YType.enumeration, "status")

                self.tpid = YLeaf(YType.identityref, "tpid")

                self.vlan_id = YLeaf(YType.uint16, "vlan-id")

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
                                "status",
                                "tpid",
                                "vlan_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vlans.Vlan.State, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vlans.Vlan.State, self).__setattr__(name, value)

            class Status(Enum):
                """
                Status

                Admin state of the VLAN

                .. data:: ACTIVE = 0

                	VLAN is active

                .. data:: SUSPENDED = 1

                	VLAN is inactive / suspended

                """

                ACTIVE = Enum.YLeaf(0, "ACTIVE")

                SUSPENDED = Enum.YLeaf(1, "SUSPENDED")


            def has_data(self):
                return (
                    self.name.is_set or
                    self.status.is_set or
                    self.tpid.is_set or
                    self.vlan_id.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.status.yfilter != YFilter.not_set or
                    self.tpid.yfilter != YFilter.not_set or
                    self.vlan_id.yfilter != YFilter.not_set)

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
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.status.get_name_leafdata())
                if (self.tpid.is_set or self.tpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tpid.get_name_leafdata())
                if (self.vlan_id.is_set or self.vlan_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlan_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "status" or name == "tpid" or name == "vlan-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "status"):
                    self.status = value
                    self.status.value_namespace = name_space
                    self.status.value_namespace_prefix = name_space_prefix
                if(value_path == "tpid"):
                    self.tpid = value
                    self.tpid.value_namespace = name_space
                    self.tpid.value_namespace_prefix = name_space_prefix
                if(value_path == "vlan-id"):
                    self.vlan_id = value
                    self.vlan_id.value_namespace = name_space
                    self.vlan_id.value_namespace_prefix = name_space_prefix


        class Members(Entity):
            """
            Enclosing container for list of member interfaces
            
            .. attribute:: member
            
            	List of references to interfaces / subinterfaces associated with the VLAN
            	**type**\: list of    :py:class:`Member <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Members.Member>`
            
            

            """

            _prefix = 'oc-vlan'
            _revision = '2016-05-26'

            def __init__(self):
                super(Vlans.Vlan.Members, self).__init__()

                self.yang_name = "members"
                self.yang_parent_name = "vlan"

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
                            super(Vlans.Vlan.Members, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vlans.Vlan.Members, self).__setattr__(name, value)


            class Member(Entity):
                """
                List of references to interfaces / subinterfaces
                associated with the VLAN.
                
                .. attribute:: interface_ref
                
                	Reference to an interface or subinterface
                	**type**\:   :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Members.Member.InterfaceRef>`
                
                

                """

                _prefix = 'oc-vlan'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Vlans.Vlan.Members.Member, self).__init__()

                    self.yang_name = "member"
                    self.yang_parent_name = "members"

                    self.interface_ref = Vlans.Vlan.Members.Member.InterfaceRef()
                    self.interface_ref.parent = self
                    self._children_name_map["interface_ref"] = "interface-ref"
                    self._children_yang_names.add("interface-ref")


                class InterfaceRef(Entity):
                    """
                    Reference to an interface or subinterface
                    
                    .. attribute:: state
                    
                    	Operational state for interface\-ref
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_vlan.Vlans.Vlan.Members.Member.InterfaceRef.State>`
                    
                    

                    """

                    _prefix = 'oc-vlan'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Vlans.Vlan.Members.Member.InterfaceRef, self).__init__()

                        self.yang_name = "interface-ref"
                        self.yang_parent_name = "member"

                        self.state = Vlans.Vlan.Members.Member.InterfaceRef.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")


                    class State(Entity):
                        """
                        Operational state for interface\-ref
                        
                        .. attribute:: interface
                        
                        	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                        
                        .. attribute:: subinterface
                        
                        	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                        
                        

                        """

                        _prefix = 'oc-vlan'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Vlans.Vlan.Members.Member.InterfaceRef.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "interface-ref"

                            self.interface = YLeaf(YType.str, "interface")

                            self.subinterface = YLeaf(YType.str, "subinterface")

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
                                            "subinterface") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vlans.Vlan.Members.Member.InterfaceRef.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vlans.Vlan.Members.Member.InterfaceRef.State, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface.is_set or
                                self.subinterface.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface.yfilter != YFilter.not_set or
                                self.subinterface.yfilter != YFilter.not_set)

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
                            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface.get_name_leafdata())
                            if (self.subinterface.is_set or self.subinterface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.subinterface.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface" or name == "subinterface"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface"):
                                self.interface = value
                                self.interface.value_namespace = name_space
                                self.interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "subinterface"):
                                self.subinterface = value
                                self.subinterface.value_namespace = name_space
                                self.subinterface.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.state is not None and self.state.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-ref" + path_buffer

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

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = Vlans.Vlan.Members.Member.InterfaceRef.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.interface_ref is not None and self.interface_ref.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.interface_ref is not None and self.interface_ref.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "member" + path_buffer

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

                    if (child_yang_name == "interface-ref"):
                        if (self.interface_ref is None):
                            self.interface_ref = Vlans.Vlan.Members.Member.InterfaceRef()
                            self.interface_ref.parent = self
                            self._children_name_map["interface_ref"] = "interface-ref"
                        return self.interface_ref

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-ref"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

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
                    c = Vlans.Vlan.Members.Member()
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
                self.vlan_id.is_set or
                (self.config is not None and self.config.has_data()) or
                (self.members is not None and self.members.has_data()) or
                (self.state is not None and self.state.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vlan_id.yfilter != YFilter.not_set or
                (self.config is not None and self.config.has_operation()) or
                (self.members is not None and self.members.has_operation()) or
                (self.state is not None and self.state.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vlan" + "[vlan-id='" + self.vlan_id.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-vlan:vlans/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vlan_id.is_set or self.vlan_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vlan_id.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "config"):
                if (self.config is None):
                    self.config = Vlans.Vlan.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                return self.config

            if (child_yang_name == "members"):
                if (self.members is None):
                    self.members = Vlans.Vlan.Members()
                    self.members.parent = self
                    self._children_name_map["members"] = "members"
                return self.members

            if (child_yang_name == "state"):
                if (self.state is None):
                    self.state = Vlans.Vlan.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                return self.state

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "config" or name == "members" or name == "state" or name == "vlan-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vlan-id"):
                self.vlan_id = value
                self.vlan_id.value_namespace = name_space
                self.vlan_id.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.vlan:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.vlan:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "openconfig-vlan:vlans" + path_buffer

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

        if (child_yang_name == "vlan"):
            for c in self.vlan:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Vlans.Vlan()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.vlan.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "vlan"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Vlans()
        return self._top_entity

