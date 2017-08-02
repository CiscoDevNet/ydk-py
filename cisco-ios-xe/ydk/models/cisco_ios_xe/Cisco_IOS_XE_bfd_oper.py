""" Cisco_IOS_XE_bfd_oper 

This module contains a collection of YANG definitions for
monitoring BFD neighbours.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BfdLspType(Enum):
    """
    BfdLspType

    BFD lsp type

    .. data:: working = 0

    .. data:: protect = 1

    .. data:: unknown = 2

    """

    working = Enum.YLeaf(0, "working")

    protect = Enum.YLeaf(1, "protect")

    unknown = Enum.YLeaf(2, "unknown")


class BfdOperSessionType(Enum):
    """
    BfdOperSessionType

    BFD session type

    .. data:: ipv4 = 0

    .. data:: ipv6 = 1

    .. data:: vccv = 2

    .. data:: mpls_tp = 3

    .. data:: ipv4_multihop = 4

    .. data:: ipv6_multihop = 5

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")

    vccv = Enum.YLeaf(2, "vccv")

    mpls_tp = Enum.YLeaf(3, "mpls-tp")

    ipv4_multihop = Enum.YLeaf(4, "ipv4-multihop")

    ipv6_multihop = Enum.YLeaf(5, "ipv6-multihop")


class BfdRemoteStateType(Enum):
    """
    BfdRemoteStateType

    BFD remote state type

    .. data:: up = 0

    .. data:: down = 1

    .. data:: init = 2

    .. data:: admindown = 3

    .. data:: invalid = 4

    """

    up = Enum.YLeaf(0, "up")

    down = Enum.YLeaf(1, "down")

    init = Enum.YLeaf(2, "init")

    admindown = Enum.YLeaf(3, "admindown")

    invalid = Enum.YLeaf(4, "invalid")


class BfdStateType(Enum):
    """
    BfdStateType

    BFD state type

    .. data:: admindown = 0

    .. data:: down = 1

    .. data:: fail = 2

    .. data:: init = 3

    .. data:: up = 4

    .. data:: invalid = 5

    """

    admindown = Enum.YLeaf(0, "admindown")

    down = Enum.YLeaf(1, "down")

    fail = Enum.YLeaf(2, "fail")

    init = Enum.YLeaf(3, "init")

    up = Enum.YLeaf(4, "up")

    invalid = Enum.YLeaf(5, "invalid")



class BfdState(Entity):
    """
    Data nodes for BFD neighbors.
    
    .. attribute:: sessions
    
    	
    	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions>`
    
    

    """

    _prefix = 'bfd-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(BfdState, self).__init__()
        self._top_entity = None

        self.yang_name = "bfd-state"
        self.yang_parent_name = "Cisco-IOS-XE-bfd-oper"

        self.sessions = BfdState.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._children_yang_names.add("sessions")


    class Sessions(Entity):
        """
        
        
        .. attribute:: session
        
        	
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session>`
        
        

        """

        _prefix = 'bfd-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(BfdState.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "bfd-state"

            self.session = YList(self)

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
                        super(BfdState.Sessions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BfdState.Sessions, self).__setattr__(name, value)


        class Session(Entity):
            """
            
            
            .. attribute:: type  <key>
            
            	Session type
            	**type**\:   :py:class:`BfdOperSessionType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdOperSessionType>`
            
            .. attribute:: bfd_circuits
            
            	
            	**type**\:   :py:class:`BfdCircuits <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdCircuits>`
            
            .. attribute:: bfd_mhop_nbrs
            
            	
            	**type**\:   :py:class:`BfdMhopNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopNbrs>`
            
            .. attribute:: bfd_mhop_vrf_nbrs
            
            	
            	**type**\:   :py:class:`BfdMhopVrfNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopVrfNbrs>`
            
            .. attribute:: bfd_nbrs
            
            	
            	**type**\:   :py:class:`BfdNbrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdNbrs>`
            
            .. attribute:: bfd_tunnel_paths
            
            	
            	**type**\:   :py:class:`BfdTunnelPaths <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdTunnelPaths>`
            
            

            """

            _prefix = 'bfd-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(BfdState.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"

                self.type = YLeaf(YType.enumeration, "type")

                self.bfd_circuits = BfdState.Sessions.Session.BfdCircuits()
                self.bfd_circuits.parent = self
                self._children_name_map["bfd_circuits"] = "bfd-circuits"
                self._children_yang_names.add("bfd-circuits")

                self.bfd_mhop_nbrs = BfdState.Sessions.Session.BfdMhopNbrs()
                self.bfd_mhop_nbrs.parent = self
                self._children_name_map["bfd_mhop_nbrs"] = "bfd-mhop-nbrs"
                self._children_yang_names.add("bfd-mhop-nbrs")

                self.bfd_mhop_vrf_nbrs = BfdState.Sessions.Session.BfdMhopVrfNbrs()
                self.bfd_mhop_vrf_nbrs.parent = self
                self._children_name_map["bfd_mhop_vrf_nbrs"] = "bfd-mhop-vrf-nbrs"
                self._children_yang_names.add("bfd-mhop-vrf-nbrs")

                self.bfd_nbrs = BfdState.Sessions.Session.BfdNbrs()
                self.bfd_nbrs.parent = self
                self._children_name_map["bfd_nbrs"] = "bfd-nbrs"
                self._children_yang_names.add("bfd-nbrs")

                self.bfd_tunnel_paths = BfdState.Sessions.Session.BfdTunnelPaths()
                self.bfd_tunnel_paths.parent = self
                self._children_name_map["bfd_tunnel_paths"] = "bfd-tunnel-paths"
                self._children_yang_names.add("bfd-tunnel-paths")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BfdState.Sessions.Session, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BfdState.Sessions.Session, self).__setattr__(name, value)


            class BfdTunnelPaths(Entity):
                """
                
                
                .. attribute:: bfd_tunnel_path
                
                	Tunnel Path
                	**type**\: list of    :py:class:`BfdTunnelPath <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdTunnelPaths, self).__init__()

                    self.yang_name = "bfd-tunnel-paths"
                    self.yang_parent_name = "session"

                    self.bfd_tunnel_path = YList(self)

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
                                super(BfdState.Sessions.Session.BfdTunnelPaths, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BfdState.Sessions.Session.BfdTunnelPaths, self).__setattr__(name, value)


                class BfdTunnelPath(Entity):
                    """
                    Tunnel Path
                    
                    .. attribute:: interface  <key>
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: lsp_type  <key>
                    
                    	
                    	**type**\:   :py:class:`BfdLspType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdLspType>`
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:   :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:   :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath, self).__init__()

                        self.yang_name = "bfd-tunnel-path"
                        self.yang_parent_name = "bfd-tunnel-paths"

                        self.interface = YLeaf(YType.str, "interface")

                        self.lsp_type = YLeaf(YType.enumeration, "lsp-type")

                        self.ld = YLeaf(YType.uint32, "ld")

                        self.rd = YLeaf(YType.uint32, "rd")

                        self.remote_state = YLeaf(YType.enumeration, "remote-state")

                        self.state = YLeaf(YType.enumeration, "state")

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
                                        "lsp_type",
                                        "ld",
                                        "rd",
                                        "remote_state",
                                        "state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            self.lsp_type.is_set or
                            self.ld.is_set or
                            self.rd.is_set or
                            self.remote_state.is_set or
                            self.state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.lsp_type.yfilter != YFilter.not_set or
                            self.ld.yfilter != YFilter.not_set or
                            self.rd.yfilter != YFilter.not_set or
                            self.remote_state.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd-tunnel-path" + "[interface='" + self.interface.get() + "']" + "[lsp-type='" + self.lsp_type.get() + "']" + path_buffer

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
                        if (self.lsp_type.is_set or self.lsp_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lsp_type.get_name_leafdata())
                        if (self.ld.is_set or self.ld.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ld.get_name_leafdata())
                        if (self.rd.is_set or self.rd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rd.get_name_leafdata())
                        if (self.remote_state.is_set or self.remote_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_state.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface" or name == "lsp-type" or name == "ld" or name == "rd" or name == "remote-state" or name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "lsp-type"):
                            self.lsp_type = value
                            self.lsp_type.value_namespace = name_space
                            self.lsp_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "ld"):
                            self.ld = value
                            self.ld.value_namespace = name_space
                            self.ld.value_namespace_prefix = name_space_prefix
                        if(value_path == "rd"):
                            self.rd = value
                            self.rd.value_namespace = name_space
                            self.rd.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-state"):
                            self.remote_state = value
                            self.remote_state.value_namespace = name_space
                            self.remote_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bfd_tunnel_path:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bfd_tunnel_path:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bfd-tunnel-paths" + path_buffer

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

                    if (child_yang_name == "bfd-tunnel-path"):
                        for c in self.bfd_tunnel_path:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bfd_tunnel_path.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd-tunnel-path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class BfdCircuits(Entity):
                """
                
                
                .. attribute:: bfd_circuit
                
                	BFD circuit
                	**type**\: list of    :py:class:`BfdCircuit <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdCircuits.BfdCircuit>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdCircuits, self).__init__()

                    self.yang_name = "bfd-circuits"
                    self.yang_parent_name = "session"

                    self.bfd_circuit = YList(self)

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
                                super(BfdState.Sessions.Session.BfdCircuits, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BfdState.Sessions.Session.BfdCircuits, self).__setattr__(name, value)


                class BfdCircuit(Entity):
                    """
                    BFD circuit
                    
                    .. attribute:: interface  <key>
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: vcid  <key>
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:   :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:   :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdCircuits.BfdCircuit, self).__init__()

                        self.yang_name = "bfd-circuit"
                        self.yang_parent_name = "bfd-circuits"

                        self.interface = YLeaf(YType.str, "interface")

                        self.vcid = YLeaf(YType.uint32, "vcid")

                        self.ld = YLeaf(YType.uint32, "ld")

                        self.rd = YLeaf(YType.uint32, "rd")

                        self.remote_state = YLeaf(YType.enumeration, "remote-state")

                        self.state = YLeaf(YType.enumeration, "state")

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
                                        "vcid",
                                        "ld",
                                        "rd",
                                        "remote_state",
                                        "state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BfdState.Sessions.Session.BfdCircuits.BfdCircuit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BfdState.Sessions.Session.BfdCircuits.BfdCircuit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            self.vcid.is_set or
                            self.ld.is_set or
                            self.rd.is_set or
                            self.remote_state.is_set or
                            self.state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.vcid.yfilter != YFilter.not_set or
                            self.ld.yfilter != YFilter.not_set or
                            self.rd.yfilter != YFilter.not_set or
                            self.remote_state.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd-circuit" + "[interface='" + self.interface.get() + "']" + "[vcid='" + self.vcid.get() + "']" + path_buffer

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
                        if (self.vcid.is_set or self.vcid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vcid.get_name_leafdata())
                        if (self.ld.is_set or self.ld.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ld.get_name_leafdata())
                        if (self.rd.is_set or self.rd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rd.get_name_leafdata())
                        if (self.remote_state.is_set or self.remote_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_state.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface" or name == "vcid" or name == "ld" or name == "rd" or name == "remote-state" or name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "vcid"):
                            self.vcid = value
                            self.vcid.value_namespace = name_space
                            self.vcid.value_namespace_prefix = name_space_prefix
                        if(value_path == "ld"):
                            self.ld = value
                            self.ld.value_namespace = name_space
                            self.ld.value_namespace_prefix = name_space_prefix
                        if(value_path == "rd"):
                            self.rd = value
                            self.rd.value_namespace = name_space
                            self.rd.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-state"):
                            self.remote_state = value
                            self.remote_state.value_namespace = name_space
                            self.remote_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bfd_circuit:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bfd_circuit:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bfd-circuits" + path_buffer

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

                    if (child_yang_name == "bfd-circuit"):
                        for c in self.bfd_circuit:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BfdState.Sessions.Session.BfdCircuits.BfdCircuit()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bfd_circuit.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd-circuit"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class BfdNbrs(Entity):
                """
                
                
                .. attribute:: bfd_nbr
                
                	This is for directly connected neighbor case
                	**type**\: list of    :py:class:`BfdNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdNbrs.BfdNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdNbrs, self).__init__()

                    self.yang_name = "bfd-nbrs"
                    self.yang_parent_name = "session"

                    self.bfd_nbr = YList(self)

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
                                super(BfdState.Sessions.Session.BfdNbrs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BfdState.Sessions.Session.BfdNbrs, self).__setattr__(name, value)


                class BfdNbr(Entity):
                    """
                    This is for directly connected neighbor case
                    
                    .. attribute:: ip  <key>
                    
                    	
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: interface  <key>
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:   :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:   :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdNbrs.BfdNbr, self).__init__()

                        self.yang_name = "bfd-nbr"
                        self.yang_parent_name = "bfd-nbrs"

                        self.ip = YLeaf(YType.str, "ip")

                        self.interface = YLeaf(YType.str, "interface")

                        self.ld = YLeaf(YType.uint32, "ld")

                        self.rd = YLeaf(YType.uint32, "rd")

                        self.remote_state = YLeaf(YType.enumeration, "remote-state")

                        self.state = YLeaf(YType.enumeration, "state")

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
                                        "interface",
                                        "ld",
                                        "rd",
                                        "remote_state",
                                        "state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BfdState.Sessions.Session.BfdNbrs.BfdNbr, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BfdState.Sessions.Session.BfdNbrs.BfdNbr, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ip.is_set or
                            self.interface.is_set or
                            self.ld.is_set or
                            self.rd.is_set or
                            self.remote_state.is_set or
                            self.state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ip.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.ld.yfilter != YFilter.not_set or
                            self.rd.yfilter != YFilter.not_set or
                            self.remote_state.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd-nbr" + "[ip='" + self.ip.get() + "']" + "[interface='" + self.interface.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.ld.is_set or self.ld.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ld.get_name_leafdata())
                        if (self.rd.is_set or self.rd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rd.get_name_leafdata())
                        if (self.remote_state.is_set or self.remote_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_state.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ip" or name == "interface" or name == "ld" or name == "rd" or name == "remote-state" or name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ip"):
                            self.ip = value
                            self.ip.value_namespace = name_space
                            self.ip.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "ld"):
                            self.ld = value
                            self.ld.value_namespace = name_space
                            self.ld.value_namespace_prefix = name_space_prefix
                        if(value_path == "rd"):
                            self.rd = value
                            self.rd.value_namespace = name_space
                            self.rd.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-state"):
                            self.remote_state = value
                            self.remote_state.value_namespace = name_space
                            self.remote_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bfd_nbr:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bfd_nbr:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bfd-nbrs" + path_buffer

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

                    if (child_yang_name == "bfd-nbr"):
                        for c in self.bfd_nbr:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BfdState.Sessions.Session.BfdNbrs.BfdNbr()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bfd_nbr.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd-nbr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class BfdMhopNbrs(Entity):
                """
                
                
                .. attribute:: bfd_mhop_nbr
                
                	This is for multi hop neighbor scenario  for global VRF (no VRF)
                	**type**\: list of    :py:class:`BfdMhopNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdMhopNbrs, self).__init__()

                    self.yang_name = "bfd-mhop-nbrs"
                    self.yang_parent_name = "session"

                    self.bfd_mhop_nbr = YList(self)

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
                                super(BfdState.Sessions.Session.BfdMhopNbrs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BfdState.Sessions.Session.BfdMhopNbrs, self).__setattr__(name, value)


                class BfdMhopNbr(Entity):
                    """
                    This is for multi hop neighbor scenario 
                    for global VRF (no VRF).
                    
                    .. attribute:: ip  <key>
                    
                    	
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:   :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:   :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr, self).__init__()

                        self.yang_name = "bfd-mhop-nbr"
                        self.yang_parent_name = "bfd-mhop-nbrs"

                        self.ip = YLeaf(YType.str, "ip")

                        self.ld = YLeaf(YType.uint32, "ld")

                        self.rd = YLeaf(YType.uint32, "rd")

                        self.remote_state = YLeaf(YType.enumeration, "remote-state")

                        self.state = YLeaf(YType.enumeration, "state")

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
                                        "ld",
                                        "rd",
                                        "remote_state",
                                        "state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ip.is_set or
                            self.ld.is_set or
                            self.rd.is_set or
                            self.remote_state.is_set or
                            self.state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ip.yfilter != YFilter.not_set or
                            self.ld.yfilter != YFilter.not_set or
                            self.rd.yfilter != YFilter.not_set or
                            self.remote_state.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd-mhop-nbr" + "[ip='" + self.ip.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip.get_name_leafdata())
                        if (self.ld.is_set or self.ld.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ld.get_name_leafdata())
                        if (self.rd.is_set or self.rd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rd.get_name_leafdata())
                        if (self.remote_state.is_set or self.remote_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_state.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ip" or name == "ld" or name == "rd" or name == "remote-state" or name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ip"):
                            self.ip = value
                            self.ip.value_namespace = name_space
                            self.ip.value_namespace_prefix = name_space_prefix
                        if(value_path == "ld"):
                            self.ld = value
                            self.ld.value_namespace = name_space
                            self.ld.value_namespace_prefix = name_space_prefix
                        if(value_path == "rd"):
                            self.rd = value
                            self.rd.value_namespace = name_space
                            self.rd.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-state"):
                            self.remote_state = value
                            self.remote_state.value_namespace = name_space
                            self.remote_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bfd_mhop_nbr:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bfd_mhop_nbr:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bfd-mhop-nbrs" + path_buffer

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

                    if (child_yang_name == "bfd-mhop-nbr"):
                        for c in self.bfd_mhop_nbr:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bfd_mhop_nbr.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd-mhop-nbr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class BfdMhopVrfNbrs(Entity):
                """
                
                
                .. attribute:: bfd_mhop_vrf_nbr
                
                	This is for multi hop neighbor scenario  for non\-global VRF
                	**type**\: list of    :py:class:`BfdMhopVrfNbr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr>`
                
                

                """

                _prefix = 'bfd-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(BfdState.Sessions.Session.BfdMhopVrfNbrs, self).__init__()

                    self.yang_name = "bfd-mhop-vrf-nbrs"
                    self.yang_parent_name = "session"

                    self.bfd_mhop_vrf_nbr = YList(self)

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
                                super(BfdState.Sessions.Session.BfdMhopVrfNbrs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BfdState.Sessions.Session.BfdMhopVrfNbrs, self).__setattr__(name, value)


                class BfdMhopVrfNbr(Entity):
                    """
                    This is for multi hop neighbor scenario 
                    for non\-global VRF.
                    
                    .. attribute:: ip  <key>
                    
                    	
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: vrf  <key>
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: ld
                    
                    	local\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rd
                    
                    	remote\-discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_state
                    
                    	 Remote Heard. RH state of BFD version '0'   is also mapped to up/down. 
                    	**type**\:   :py:class:`BfdRemoteStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdRemoteStateType>`
                    
                    .. attribute:: state
                    
                    	BFD state
                    	**type**\:   :py:class:`BfdStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper.BfdStateType>`
                    
                    

                    """

                    _prefix = 'bfd-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr, self).__init__()

                        self.yang_name = "bfd-mhop-vrf-nbr"
                        self.yang_parent_name = "bfd-mhop-vrf-nbrs"

                        self.ip = YLeaf(YType.str, "ip")

                        self.vrf = YLeaf(YType.str, "vrf")

                        self.ld = YLeaf(YType.uint32, "ld")

                        self.rd = YLeaf(YType.uint32, "rd")

                        self.remote_state = YLeaf(YType.enumeration, "remote-state")

                        self.state = YLeaf(YType.enumeration, "state")

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
                                        "vrf",
                                        "ld",
                                        "rd",
                                        "remote_state",
                                        "state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ip.is_set or
                            self.vrf.is_set or
                            self.ld.is_set or
                            self.rd.is_set or
                            self.remote_state.is_set or
                            self.state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ip.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set or
                            self.ld.yfilter != YFilter.not_set or
                            self.rd.yfilter != YFilter.not_set or
                            self.remote_state.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd-mhop-vrf-nbr" + "[ip='" + self.ip.get() + "']" + "[vrf='" + self.vrf.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())
                        if (self.ld.is_set or self.ld.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ld.get_name_leafdata())
                        if (self.rd.is_set or self.rd.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rd.get_name_leafdata())
                        if (self.remote_state.is_set or self.remote_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_state.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ip" or name == "vrf" or name == "ld" or name == "rd" or name == "remote-state" or name == "state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ip"):
                            self.ip = value
                            self.ip.value_namespace = name_space
                            self.ip.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix
                        if(value_path == "ld"):
                            self.ld = value
                            self.ld.value_namespace = name_space
                            self.ld.value_namespace_prefix = name_space_prefix
                        if(value_path == "rd"):
                            self.rd = value
                            self.rd.value_namespace = name_space
                            self.rd.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-state"):
                            self.remote_state = value
                            self.remote_state.value_namespace = name_space
                            self.remote_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bfd_mhop_vrf_nbr:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bfd_mhop_vrf_nbr:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bfd-mhop-vrf-nbrs" + path_buffer

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

                    if (child_yang_name == "bfd-mhop-vrf-nbr"):
                        for c in self.bfd_mhop_vrf_nbr:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bfd_mhop_vrf_nbr.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd-mhop-vrf-nbr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.type.is_set or
                    (self.bfd_circuits is not None and self.bfd_circuits.has_data()) or
                    (self.bfd_mhop_nbrs is not None and self.bfd_mhop_nbrs.has_data()) or
                    (self.bfd_mhop_vrf_nbrs is not None and self.bfd_mhop_vrf_nbrs.has_data()) or
                    (self.bfd_nbrs is not None and self.bfd_nbrs.has_data()) or
                    (self.bfd_tunnel_paths is not None and self.bfd_tunnel_paths.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    (self.bfd_circuits is not None and self.bfd_circuits.has_operation()) or
                    (self.bfd_mhop_nbrs is not None and self.bfd_mhop_nbrs.has_operation()) or
                    (self.bfd_mhop_vrf_nbrs is not None and self.bfd_mhop_vrf_nbrs.has_operation()) or
                    (self.bfd_nbrs is not None and self.bfd_nbrs.has_operation()) or
                    (self.bfd_tunnel_paths is not None and self.bfd_tunnel_paths.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "session" + "[type='" + self.type.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-bfd-oper:bfd-state/sessions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bfd-circuits"):
                    if (self.bfd_circuits is None):
                        self.bfd_circuits = BfdState.Sessions.Session.BfdCircuits()
                        self.bfd_circuits.parent = self
                        self._children_name_map["bfd_circuits"] = "bfd-circuits"
                    return self.bfd_circuits

                if (child_yang_name == "bfd-mhop-nbrs"):
                    if (self.bfd_mhop_nbrs is None):
                        self.bfd_mhop_nbrs = BfdState.Sessions.Session.BfdMhopNbrs()
                        self.bfd_mhop_nbrs.parent = self
                        self._children_name_map["bfd_mhop_nbrs"] = "bfd-mhop-nbrs"
                    return self.bfd_mhop_nbrs

                if (child_yang_name == "bfd-mhop-vrf-nbrs"):
                    if (self.bfd_mhop_vrf_nbrs is None):
                        self.bfd_mhop_vrf_nbrs = BfdState.Sessions.Session.BfdMhopVrfNbrs()
                        self.bfd_mhop_vrf_nbrs.parent = self
                        self._children_name_map["bfd_mhop_vrf_nbrs"] = "bfd-mhop-vrf-nbrs"
                    return self.bfd_mhop_vrf_nbrs

                if (child_yang_name == "bfd-nbrs"):
                    if (self.bfd_nbrs is None):
                        self.bfd_nbrs = BfdState.Sessions.Session.BfdNbrs()
                        self.bfd_nbrs.parent = self
                        self._children_name_map["bfd_nbrs"] = "bfd-nbrs"
                    return self.bfd_nbrs

                if (child_yang_name == "bfd-tunnel-paths"):
                    if (self.bfd_tunnel_paths is None):
                        self.bfd_tunnel_paths = BfdState.Sessions.Session.BfdTunnelPaths()
                        self.bfd_tunnel_paths.parent = self
                        self._children_name_map["bfd_tunnel_paths"] = "bfd-tunnel-paths"
                    return self.bfd_tunnel_paths

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bfd-circuits" or name == "bfd-mhop-nbrs" or name == "bfd-mhop-vrf-nbrs" or name == "bfd-nbrs" or name == "bfd-tunnel-paths" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.session:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.session:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sessions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-bfd-oper:bfd-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "session"):
                for c in self.session:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BfdState.Sessions.Session()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.session.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "session"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.sessions is not None and self.sessions.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.sessions is not None and self.sessions.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-bfd-oper:bfd-state" + path_buffer

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

        if (child_yang_name == "sessions"):
            if (self.sessions is None):
                self.sessions = BfdState.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
            return self.sessions

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "sessions"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = BfdState()
        return self._top_entity

