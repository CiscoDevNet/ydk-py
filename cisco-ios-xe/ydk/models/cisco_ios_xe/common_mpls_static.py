""" common_mpls_static 

YANG module describing configuration and
operational data relating to MPLS Static.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Hoptype(Enum):
    """
    Hoptype

    The Nexthop type

    .. data:: PRIMARY = 0

    	Primary next hop

    .. data:: BACKUP = 1

    	Backup next hop

    """

    PRIMARY = Enum.YLeaf(0, "PRIMARY")

    BACKUP = Enum.YLeaf(1, "BACKUP")



class LspType(Identity):
    """
    The type of Label Switched Path
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(LspType, self).__init__("urn:ietf:params:xml:ns:yang:common-mpls-static", "common-mpls-static", "common-mpls-static:lsp-type")


class NexthopResolutionType(Identity):
    """
    The Routing Protocol from which the nexthop is resolved
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(NexthopResolutionType, self).__init__("urn:ietf:params:xml:ns:yang:common-mpls-static", "common-mpls-static", "common-mpls-static:nexthop-resolution-type")


class MplsStatic(Entity):
    """
    MPLS Static module
    
    .. attribute:: mpls_static_cfg
    
    	MPLS Static configuration commands
    	**type**\:   :py:class:`MplsStaticCfg <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg>`
    
    .. attribute:: mpls_static_state
    
    	MPLS static operational data
    	**type**\:   :py:class:`MplsStaticState <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState>`
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(MplsStatic, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-static"
        self.yang_parent_name = "common-mpls-static"

        self.mpls_static_cfg = MplsStatic.MplsStaticCfg()
        self.mpls_static_cfg.parent = self
        self._children_name_map["mpls_static_cfg"] = "mpls-static-cfg"
        self._children_yang_names.add("mpls-static-cfg")

        self.mpls_static_state = MplsStatic.MplsStaticState()
        self.mpls_static_state.parent = self
        self._children_name_map["mpls_static_state"] = "mpls-static-state"
        self._children_yang_names.add("mpls-static-state")


    class MplsStaticCfg(Entity):
        """
        MPLS Static configuration commands
        
        .. attribute:: in_label_lsps
        
        	The LSPs indexed by in\-label
        	**type**\:   :py:class:`InLabelLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps>`
        
        .. attribute:: interfaces
        
        	The list of interfaces configured with mpls
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Interfaces>`
        
        .. attribute:: ipv4_ingress_lsps
        
        	The LSPs indexed by ipv4 prefix
        	**type**\:   :py:class:`Ipv4IngressLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps>`
        
        .. attribute:: ipv6_ingress_lsps
        
        	The LSPs indexed by ipv6 prefix
        	**type**\:   :py:class:`Ipv6IngressLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps>`
        
        .. attribute:: named_lsps
        
        	The LSPs indexed by name
        	**type**\:   :py:class:`NamedLsps <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps>`
        
        

        """

        _prefix = 'ms'
        _revision = '2015-07-22'

        def __init__(self):
            super(MplsStatic.MplsStaticCfg, self).__init__()

            self.yang_name = "mpls-static-cfg"
            self.yang_parent_name = "mpls-static"

            self.in_label_lsps = MplsStatic.MplsStaticCfg.InLabelLsps()
            self.in_label_lsps.parent = self
            self._children_name_map["in_label_lsps"] = "in-label-lsps"
            self._children_yang_names.add("in-label-lsps")

            self.interfaces = MplsStatic.MplsStaticCfg.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.ipv4_ingress_lsps = MplsStatic.MplsStaticCfg.Ipv4IngressLsps()
            self.ipv4_ingress_lsps.parent = self
            self._children_name_map["ipv4_ingress_lsps"] = "ipv4-ingress-lsps"
            self._children_yang_names.add("ipv4-ingress-lsps")

            self.ipv6_ingress_lsps = MplsStatic.MplsStaticCfg.Ipv6IngressLsps()
            self.ipv6_ingress_lsps.parent = self
            self._children_name_map["ipv6_ingress_lsps"] = "ipv6-ingress-lsps"
            self._children_yang_names.add("ipv6-ingress-lsps")

            self.named_lsps = MplsStatic.MplsStaticCfg.NamedLsps()
            self.named_lsps.parent = self
            self._children_name_map["named_lsps"] = "named-lsps"
            self._children_yang_names.add("named-lsps")


        class Interfaces(Entity):
            """
            The list of interfaces configured with mpls
            
            .. attribute:: interface
            
            	List of interfaces that can be enabled under mpls static
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Interfaces.Interface>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticCfg.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "mpls-static-cfg"

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
                            super(MplsStatic.MplsStaticCfg.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsStatic.MplsStaticCfg.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                List of interfaces that can be enabled under
                mpls static
                
                .. attribute:: name  <key>
                
                	Interface name
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                	**mandatory**\: True
                
                .. attribute:: enabled
                
                	Interface Enabled boolean
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticCfg.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.name = YLeaf(YType.str, "name")

                    self.enabled = YLeaf(YType.uint32, "enabled")

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
                                    "enabled") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.MplsStaticCfg.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.MplsStaticCfg.Interfaces.Interface, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.enabled.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "common-mpls-static:mpls-static/mpls-static-cfg/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "name" or name == "enabled"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix

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
                    path_buffer = "common-mpls-static:mpls-static/mpls-static-cfg/%s" % self.get_segment_path()
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
                    c = MplsStatic.MplsStaticCfg.Interfaces.Interface()
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


        class Ipv4IngressLsps(Entity):
            """
            The LSPs indexed by ipv4 prefix
            
            .. attribute:: ipv4_ingress_lsp
            
            	MPLS Static IPv4 Label Switched Path Configuration at Ingress
            	**type**\: list of    :py:class:`Ipv4IngressLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps, self).__init__()

                self.yang_name = "ipv4-ingress-lsps"
                self.yang_parent_name = "mpls-static-cfg"

                self.ipv4_ingress_lsp = YList(self)

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
                            super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps, self).__setattr__(name, value)


            class Ipv4IngressLsp(Entity):
                """
                MPLS Static IPv4 Label Switched
                Path Configuration at Ingress
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF
                	**type**\:  str
                
                .. attribute:: prefix  <key>
                
                	IPv4 prefix of packets that will ingress on this LSP
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                .. attribute:: in_label
                
                	Value of the local label. Optional for ingress
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 16..1048575
                
                
                ----
                	**type**\:   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                
                
                ----
                .. attribute:: name
                
                	Name of the LSP
                	**type**\:  str
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp, self).__init__()

                    self.yang_name = "ipv4-ingress-lsp"
                    self.yang_parent_name = "ipv4-ingress-lsps"

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.prefix = YLeaf(YType.str, "prefix")

                    self.in_label = YLeaf(YType.str, "in-label")

                    self.name = YLeaf(YType.str, "name")

                    self.path = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path()
                    self.path.parent = self
                    self._children_name_map["path"] = "path"
                    self._children_yang_names.add("path")

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
                                    "prefix",
                                    "in_label",
                                    "name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp, self).__setattr__(name, value)


                class Path(Entity):
                    """
                    Fowarding path
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop>`
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path, self).__init__()

                        self.yang_name = "path"
                        self.yang_parent_name = "ipv4-ingress-lsp"

                        self.auto_protect = YLeaf(YType.boolean, "auto-protect")

                        self.operations = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations()
                        self.operations.parent = self
                        self._children_name_map["operations"] = "operations"
                        self._children_yang_names.add("operations")

                        self.next_hop = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("auto_protect") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path, self).__setattr__(name, value)


                    class Operations(Entity):
                        """
                        The incoming label processing
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push>`
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations, self).__init__()

                            self.yang_name = "operations"
                            self.yang_parent_name = "path"

                            self.pop_and_forward = YLeaf(YType.empty, "pop-and-forward")

                            self.preserve = YLeaf(YType.empty, "preserve")

                            self.push = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push()
                            self.push.parent = self
                            self._children_name_map["push"] = "push"
                            self._children_yang_names.add("push")

                            self.swap = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap()
                            self.swap.parent = self
                            self._children_name_map["swap"] = "swap"
                            self._children_yang_names.add("swap")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("pop_and_forward",
                                            "preserve") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations, self).__setattr__(name, value)


                        class Swap(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap, self).__init__()

                                self.yang_name = "swap"
                                self.yang_parent_name = "operations"

                                self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._children_yang_names.add("stack")


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "swap"

                                    self.label_stack = YLeafList(YType.str, "label-stack")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_stack") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack, self).__setattr__(name, value)

                                def has_data(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return False

                                def has_operation(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_stack.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stack" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-stack"):
                                        self.label_stack.append(value)

                            def has_data(self):
                                return (self.stack is not None and self.stack.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.stack is not None and self.stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "swap" + path_buffer

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

                                if (child_yang_name == "stack"):
                                    if (self.stack is None):
                                        self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack()
                                        self.stack.parent = self
                                        self._children_name_map["stack"] = "stack"
                                    return self.stack

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "stack"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Push(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push, self).__init__()

                                self.yang_name = "push"
                                self.yang_parent_name = "operations"

                                self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._children_yang_names.add("stack")


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "push"

                                    self.label_stack = YLeafList(YType.str, "label-stack")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_stack") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack, self).__setattr__(name, value)

                                def has_data(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return False

                                def has_operation(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_stack.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stack" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-stack"):
                                        self.label_stack.append(value)

                            def has_data(self):
                                return (self.stack is not None and self.stack.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.stack is not None and self.stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "push" + path_buffer

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

                                if (child_yang_name == "stack"):
                                    if (self.stack is None):
                                        self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack()
                                        self.stack.parent = self
                                        self._children_name_map["stack"] = "stack"
                                    return self.stack

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "stack"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.pop_and_forward.is_set or
                                self.preserve.is_set or
                                (self.push is not None and self.push.has_data()) or
                                (self.swap is not None and self.swap.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.pop_and_forward.yfilter != YFilter.not_set or
                                self.preserve.yfilter != YFilter.not_set or
                                (self.push is not None and self.push.has_operation()) or
                                (self.swap is not None and self.swap.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operations" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.pop_and_forward.is_set or self.pop_and_forward.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pop_and_forward.get_name_leafdata())
                            if (self.preserve.is_set or self.preserve.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.preserve.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "push"):
                                if (self.push is None):
                                    self.push = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push()
                                    self.push.parent = self
                                    self._children_name_map["push"] = "push"
                                return self.push

                            if (child_yang_name == "swap"):
                                if (self.swap is None):
                                    self.swap = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap()
                                    self.swap.parent = self
                                    self._children_name_map["swap"] = "swap"
                                return self.swap

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "push" or name == "swap" or name == "pop-and-forward" or name == "preserve"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "pop-and-forward"):
                                self.pop_and_forward = value
                                self.pop_and_forward.value_namespace = name_space
                                self.pop_and_forward.value_namespace_prefix = name_space_prefix
                            if(value_path == "preserve"):
                                self.preserve = value
                                self.preserve.value_namespace = name_space
                                self.preserve.value_namespace_prefix = name_space_prefix


                    class NextHop(Entity):
                        """
                        next\-hops list
                        
                        .. attribute:: index  <key>
                        
                        	Index of the nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations>`
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:   :py:class:`Hoptype <ydk.models.cisco_ios_xe.common_mpls_static.Hoptype>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "path"

                            self.index = YLeaf(YType.uint32, "index")

                            self.protected_by = YLeaf(YType.uint32, "protected-by")

                            self.type = YLeaf(YType.enumeration, "type")

                            self.next_hop_type = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self._children_name_map["next_hop_type"] = "next-hop-type"
                            self._children_yang_names.add("next-hop-type")

                            self.operations = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self._children_name_map["operations"] = "operations"
                            self._children_yang_names.add("operations")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("index",
                                            "protected_by",
                                            "type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop, self).__setattr__(name, value)


                        class Operations(Entity):
                            """
                            The incoming label processing
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations, self).__init__()

                                self.yang_name = "operations"
                                self.yang_parent_name = "next-hop"

                                self.pop_and_forward = YLeaf(YType.empty, "pop-and-forward")

                                self.preserve = YLeaf(YType.empty, "preserve")

                                self.push = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self._children_name_map["push"] = "push"
                                self._children_yang_names.add("push")

                                self.swap = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self
                                self._children_name_map["swap"] = "swap"
                                self._children_yang_names.add("swap")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("pop_and_forward",
                                                "preserve") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations, self).__setattr__(name, value)


                            class Push(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push, self).__init__()

                                    self.yang_name = "push"
                                    self.yang_parent_name = "operations"

                                    self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._children_yang_names.add("stack")


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "push"

                                        self.label_stack = YLeafList(YType.str, "label-stack")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("label_stack") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.label_stack.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "stack" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "label-stack"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "label-stack"):
                                            self.label_stack.append(value)

                                def has_data(self):
                                    return (self.stack is not None and self.stack.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.stack is not None and self.stack.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "push" + path_buffer

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

                                    if (child_yang_name == "stack"):
                                        if (self.stack is None):
                                            self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack()
                                            self.stack.parent = self
                                            self._children_name_map["stack"] = "stack"
                                        return self.stack

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Swap(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap, self).__init__()

                                    self.yang_name = "swap"
                                    self.yang_parent_name = "operations"

                                    self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._children_yang_names.add("stack")


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "swap"

                                        self.label_stack = YLeafList(YType.str, "label-stack")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("label_stack") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.label_stack.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "stack" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "label-stack"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "label-stack"):
                                            self.label_stack.append(value)

                                def has_data(self):
                                    return (self.stack is not None and self.stack.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.stack is not None and self.stack.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "swap" + path_buffer

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

                                    if (child_yang_name == "stack"):
                                        if (self.stack is None):
                                            self.stack = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack()
                                            self.stack.parent = self
                                            self._children_name_map["stack"] = "stack"
                                        return self.stack

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.pop_and_forward.is_set or
                                    self.preserve.is_set or
                                    (self.push is not None and self.push.has_data()) or
                                    (self.swap is not None and self.swap.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.pop_and_forward.yfilter != YFilter.not_set or
                                    self.preserve.yfilter != YFilter.not_set or
                                    (self.push is not None and self.push.has_operation()) or
                                    (self.swap is not None and self.swap.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "operations" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.pop_and_forward.is_set or self.pop_and_forward.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pop_and_forward.get_name_leafdata())
                                if (self.preserve.is_set or self.preserve.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.preserve.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "push"):
                                    if (self.push is None):
                                        self.push = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push()
                                        self.push.parent = self
                                        self._children_name_map["push"] = "push"
                                    return self.push

                                if (child_yang_name == "swap"):
                                    if (self.swap is None):
                                        self.swap = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap()
                                        self.swap.parent = self
                                        self._children_name_map["swap"] = "swap"
                                    return self.swap

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "push" or name == "swap" or name == "pop-and-forward" or name == "preserve"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "pop-and-forward"):
                                    self.pop_and_forward = value
                                    self.pop_and_forward.value_namespace = name_space
                                    self.pop_and_forward.value_namespace_prefix = name_space_prefix
                                if(value_path == "preserve"):
                                    self.preserve = value
                                    self.preserve.value_namespace = name_space
                                    self.preserve.value_namespace_prefix = name_space_prefix


                        class NextHopType(Entity):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType, self).__init__()

                                self.yang_name = "next-hop-type"
                                self.yang_parent_name = "next-hop"

                                self.if_index = YLeaf(YType.uint32, "if-index")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                self.mac_address = YLeaf(YType.str, "mac-address")

                                self.out_interface_name = YLeaf(YType.str, "out-interface-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("if_index",
                                                "ipv4_address",
                                                "ipv6_address",
                                                "mac_address",
                                                "out_interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.if_index.is_set or
                                    self.ipv4_address.is_set or
                                    self.ipv6_address.is_set or
                                    self.mac_address.is_set or
                                    self.out_interface_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.if_index.yfilter != YFilter.not_set or
                                    self.ipv4_address.yfilter != YFilter.not_set or
                                    self.ipv6_address.yfilter != YFilter.not_set or
                                    self.mac_address.yfilter != YFilter.not_set or
                                    self.out_interface_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "next-hop-type" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.if_index.get_name_leafdata())
                                if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                                if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mac_address.get_name_leafdata())
                                if (self.out_interface_name.is_set or self.out_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "if-index" or name == "ipv4-address" or name == "ipv6-address" or name == "mac-address" or name == "out-interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "if-index"):
                                    self.if_index = value
                                    self.if_index.value_namespace = name_space
                                    self.if_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv4-address"):
                                    self.ipv4_address = value
                                    self.ipv4_address.value_namespace = name_space
                                    self.ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv6-address"):
                                    self.ipv6_address = value
                                    self.ipv6_address.value_namespace = name_space
                                    self.ipv6_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "mac-address"):
                                    self.mac_address = value
                                    self.mac_address.value_namespace = name_space
                                    self.mac_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-interface-name"):
                                    self.out_interface_name = value
                                    self.out_interface_name.value_namespace = name_space
                                    self.out_interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.index.is_set or
                                self.protected_by.is_set or
                                self.type.is_set or
                                (self.next_hop_type is not None and self.next_hop_type.has_data()) or
                                (self.operations is not None and self.operations.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.protected_by.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set or
                                (self.next_hop_type is not None and self.next_hop_type.has_operation()) or
                                (self.operations is not None and self.operations.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "next-hop" + "[index='" + self.index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.protected_by.is_set or self.protected_by.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protected_by.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "next-hop-type"):
                                if (self.next_hop_type is None):
                                    self.next_hop_type = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType()
                                    self.next_hop_type.parent = self
                                    self._children_name_map["next_hop_type"] = "next-hop-type"
                                return self.next_hop_type

                            if (child_yang_name == "operations"):
                                if (self.operations is None):
                                    self.operations = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations()
                                    self.operations.parent = self
                                    self._children_name_map["operations"] = "operations"
                                return self.operations

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "next-hop-type" or name == "operations" or name == "index" or name == "protected-by" or name == "type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "protected-by"):
                                self.protected_by = value
                                self.protected_by.value_namespace = name_space
                                self.protected_by.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.next_hop:
                            if (c.has_data()):
                                return True
                        return (
                            self.auto_protect.is_set or
                            (self.operations is not None and self.operations.has_data()))

                    def has_operation(self):
                        for c in self.next_hop:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.auto_protect.yfilter != YFilter.not_set or
                            (self.operations is not None and self.operations.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "path" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.auto_protect.is_set or self.auto_protect.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auto_protect.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "next-hop"):
                            for c in self.next_hop:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.next_hop.append(c)
                            return c

                        if (child_yang_name == "operations"):
                            if (self.operations is None):
                                self.operations = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations()
                                self.operations.parent = self
                                self._children_name_map["operations"] = "operations"
                            return self.operations

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "operations" or name == "auto-protect"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "auto-protect"):
                            self.auto_protect = value
                            self.auto_protect.value_namespace = name_space
                            self.auto_protect.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.vrf_name.is_set or
                        self.prefix.is_set or
                        self.in_label.is_set or
                        self.name.is_set or
                        (self.path is not None and self.path.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        self.prefix.yfilter != YFilter.not_set or
                        self.in_label.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.path is not None and self.path.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4-ingress-lsp" + "[vrf-name='" + self.vrf_name.get() + "']" + "[prefix='" + self.prefix.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "common-mpls-static:mpls-static/mpls-static-cfg/ipv4-ingress-lsps/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())
                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix.get_name_leafdata())
                    if (self.in_label.is_set or self.in_label.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_label.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "path"):
                        if (self.path is None):
                            self.path = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path()
                            self.path.parent = self
                            self._children_name_map["path"] = "path"
                        return self.path

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "path" or name == "vrf-name" or name == "prefix" or name == "in-label" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix"):
                        self.prefix = value
                        self.prefix.value_namespace = name_space
                        self.prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-label"):
                        self.in_label = value
                        self.in_label.value_namespace = name_space
                        self.in_label.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ipv4_ingress_lsp:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ipv4_ingress_lsp:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4-ingress-lsps" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "common-mpls-static:mpls-static/mpls-static-cfg/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv4-ingress-lsp"):
                    for c in self.ipv4_ingress_lsp:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ipv4_ingress_lsp.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4-ingress-lsp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class InLabelLsps(Entity):
            """
            The LSPs indexed by in\-label
            
            .. attribute:: in_label_lsp
            
            	Non\-ingress MPLS Static LSPs, keyed on the incoming label
            	**type**\: list of    :py:class:`InLabelLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticCfg.InLabelLsps, self).__init__()

                self.yang_name = "in-label-lsps"
                self.yang_parent_name = "mpls-static-cfg"

                self.in_label_lsp = YList(self)

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
                            super(MplsStatic.MplsStaticCfg.InLabelLsps, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsStatic.MplsStaticCfg.InLabelLsps, self).__setattr__(name, value)


            class InLabelLsp(Entity):
                """
                Non\-ingress MPLS Static LSPs,
                keyed on the incoming label
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF
                	**type**\:  str
                
                .. attribute:: in_label  <key>
                
                	Value of the local label
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 16..1048575
                
                
                ----
                	**type**\:   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                
                
                ----
                .. attribute:: path
                
                	Fowarding path
                	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp, self).__init__()

                    self.yang_name = "in-label-lsp"
                    self.yang_parent_name = "in-label-lsps"

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.in_label = YLeaf(YType.str, "in-label")

                    self.path = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path()
                    self.path.parent = self
                    self._children_name_map["path"] = "path"
                    self._children_yang_names.add("path")

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
                                    "in_label") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp, self).__setattr__(name, value)


                class Path(Entity):
                    """
                    Fowarding path
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop>`
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path, self).__init__()

                        self.yang_name = "path"
                        self.yang_parent_name = "in-label-lsp"

                        self.auto_protect = YLeaf(YType.boolean, "auto-protect")

                        self.operations = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations()
                        self.operations.parent = self
                        self._children_name_map["operations"] = "operations"
                        self._children_yang_names.add("operations")

                        self.next_hop = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("auto_protect") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path, self).__setattr__(name, value)


                    class Operations(Entity):
                        """
                        The incoming label processing
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push>`
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations, self).__init__()

                            self.yang_name = "operations"
                            self.yang_parent_name = "path"

                            self.pop_and_forward = YLeaf(YType.empty, "pop-and-forward")

                            self.preserve = YLeaf(YType.empty, "preserve")

                            self.push = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push()
                            self.push.parent = self
                            self._children_name_map["push"] = "push"
                            self._children_yang_names.add("push")

                            self.swap = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap()
                            self.swap.parent = self
                            self._children_name_map["swap"] = "swap"
                            self._children_yang_names.add("swap")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("pop_and_forward",
                                            "preserve") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations, self).__setattr__(name, value)


                        class Swap(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap, self).__init__()

                                self.yang_name = "swap"
                                self.yang_parent_name = "operations"

                                self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._children_yang_names.add("stack")


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "swap"

                                    self.label_stack = YLeafList(YType.str, "label-stack")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_stack") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack, self).__setattr__(name, value)

                                def has_data(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return False

                                def has_operation(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_stack.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stack" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-stack"):
                                        self.label_stack.append(value)

                            def has_data(self):
                                return (self.stack is not None and self.stack.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.stack is not None and self.stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "swap" + path_buffer

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

                                if (child_yang_name == "stack"):
                                    if (self.stack is None):
                                        self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack()
                                        self.stack.parent = self
                                        self._children_name_map["stack"] = "stack"
                                    return self.stack

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "stack"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Push(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push, self).__init__()

                                self.yang_name = "push"
                                self.yang_parent_name = "operations"

                                self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._children_yang_names.add("stack")


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "push"

                                    self.label_stack = YLeafList(YType.str, "label-stack")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_stack") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack, self).__setattr__(name, value)

                                def has_data(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return False

                                def has_operation(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_stack.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stack" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-stack"):
                                        self.label_stack.append(value)

                            def has_data(self):
                                return (self.stack is not None and self.stack.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.stack is not None and self.stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "push" + path_buffer

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

                                if (child_yang_name == "stack"):
                                    if (self.stack is None):
                                        self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack()
                                        self.stack.parent = self
                                        self._children_name_map["stack"] = "stack"
                                    return self.stack

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "stack"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.pop_and_forward.is_set or
                                self.preserve.is_set or
                                (self.push is not None and self.push.has_data()) or
                                (self.swap is not None and self.swap.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.pop_and_forward.yfilter != YFilter.not_set or
                                self.preserve.yfilter != YFilter.not_set or
                                (self.push is not None and self.push.has_operation()) or
                                (self.swap is not None and self.swap.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operations" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.pop_and_forward.is_set or self.pop_and_forward.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pop_and_forward.get_name_leafdata())
                            if (self.preserve.is_set or self.preserve.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.preserve.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "push"):
                                if (self.push is None):
                                    self.push = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push()
                                    self.push.parent = self
                                    self._children_name_map["push"] = "push"
                                return self.push

                            if (child_yang_name == "swap"):
                                if (self.swap is None):
                                    self.swap = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap()
                                    self.swap.parent = self
                                    self._children_name_map["swap"] = "swap"
                                return self.swap

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "push" or name == "swap" or name == "pop-and-forward" or name == "preserve"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "pop-and-forward"):
                                self.pop_and_forward = value
                                self.pop_and_forward.value_namespace = name_space
                                self.pop_and_forward.value_namespace_prefix = name_space_prefix
                            if(value_path == "preserve"):
                                self.preserve = value
                                self.preserve.value_namespace = name_space
                                self.preserve.value_namespace_prefix = name_space_prefix


                    class NextHop(Entity):
                        """
                        next\-hops list
                        
                        .. attribute:: index  <key>
                        
                        	Index of the nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations>`
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:   :py:class:`Hoptype <ydk.models.cisco_ios_xe.common_mpls_static.Hoptype>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "path"

                            self.index = YLeaf(YType.uint32, "index")

                            self.protected_by = YLeaf(YType.uint32, "protected-by")

                            self.type = YLeaf(YType.enumeration, "type")

                            self.next_hop_type = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self._children_name_map["next_hop_type"] = "next-hop-type"
                            self._children_yang_names.add("next-hop-type")

                            self.operations = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self._children_name_map["operations"] = "operations"
                            self._children_yang_names.add("operations")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("index",
                                            "protected_by",
                                            "type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop, self).__setattr__(name, value)


                        class NextHopType(Entity):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType, self).__init__()

                                self.yang_name = "next-hop-type"
                                self.yang_parent_name = "next-hop"

                                self.if_index = YLeaf(YType.uint32, "if-index")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                self.mac_address = YLeaf(YType.str, "mac-address")

                                self.out_interface_name = YLeaf(YType.str, "out-interface-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("if_index",
                                                "ipv4_address",
                                                "ipv6_address",
                                                "mac_address",
                                                "out_interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.if_index.is_set or
                                    self.ipv4_address.is_set or
                                    self.ipv6_address.is_set or
                                    self.mac_address.is_set or
                                    self.out_interface_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.if_index.yfilter != YFilter.not_set or
                                    self.ipv4_address.yfilter != YFilter.not_set or
                                    self.ipv6_address.yfilter != YFilter.not_set or
                                    self.mac_address.yfilter != YFilter.not_set or
                                    self.out_interface_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "next-hop-type" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.if_index.get_name_leafdata())
                                if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                                if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mac_address.get_name_leafdata())
                                if (self.out_interface_name.is_set or self.out_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "if-index" or name == "ipv4-address" or name == "ipv6-address" or name == "mac-address" or name == "out-interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "if-index"):
                                    self.if_index = value
                                    self.if_index.value_namespace = name_space
                                    self.if_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv4-address"):
                                    self.ipv4_address = value
                                    self.ipv4_address.value_namespace = name_space
                                    self.ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv6-address"):
                                    self.ipv6_address = value
                                    self.ipv6_address.value_namespace = name_space
                                    self.ipv6_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "mac-address"):
                                    self.mac_address = value
                                    self.mac_address.value_namespace = name_space
                                    self.mac_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-interface-name"):
                                    self.out_interface_name = value
                                    self.out_interface_name.value_namespace = name_space
                                    self.out_interface_name.value_namespace_prefix = name_space_prefix


                        class Operations(Entity):
                            """
                            The incoming label processing
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations, self).__init__()

                                self.yang_name = "operations"
                                self.yang_parent_name = "next-hop"

                                self.pop_and_forward = YLeaf(YType.empty, "pop-and-forward")

                                self.preserve = YLeaf(YType.empty, "preserve")

                                self.push = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self._children_name_map["push"] = "push"
                                self._children_yang_names.add("push")

                                self.swap = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self
                                self._children_name_map["swap"] = "swap"
                                self._children_yang_names.add("swap")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("pop_and_forward",
                                                "preserve") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations, self).__setattr__(name, value)


                            class Swap(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap, self).__init__()

                                    self.yang_name = "swap"
                                    self.yang_parent_name = "operations"

                                    self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._children_yang_names.add("stack")


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "swap"

                                        self.label_stack = YLeafList(YType.str, "label-stack")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("label_stack") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.label_stack.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "stack" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "label-stack"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "label-stack"):
                                            self.label_stack.append(value)

                                def has_data(self):
                                    return (self.stack is not None and self.stack.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.stack is not None and self.stack.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "swap" + path_buffer

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

                                    if (child_yang_name == "stack"):
                                        if (self.stack is None):
                                            self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack()
                                            self.stack.parent = self
                                            self._children_name_map["stack"] = "stack"
                                        return self.stack

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Push(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push, self).__init__()

                                    self.yang_name = "push"
                                    self.yang_parent_name = "operations"

                                    self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._children_yang_names.add("stack")


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "push"

                                        self.label_stack = YLeafList(YType.str, "label-stack")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("label_stack") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.label_stack.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "stack" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "label-stack"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "label-stack"):
                                            self.label_stack.append(value)

                                def has_data(self):
                                    return (self.stack is not None and self.stack.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.stack is not None and self.stack.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "push" + path_buffer

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

                                    if (child_yang_name == "stack"):
                                        if (self.stack is None):
                                            self.stack = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack()
                                            self.stack.parent = self
                                            self._children_name_map["stack"] = "stack"
                                        return self.stack

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.pop_and_forward.is_set or
                                    self.preserve.is_set or
                                    (self.push is not None and self.push.has_data()) or
                                    (self.swap is not None and self.swap.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.pop_and_forward.yfilter != YFilter.not_set or
                                    self.preserve.yfilter != YFilter.not_set or
                                    (self.push is not None and self.push.has_operation()) or
                                    (self.swap is not None and self.swap.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "operations" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.pop_and_forward.is_set or self.pop_and_forward.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pop_and_forward.get_name_leafdata())
                                if (self.preserve.is_set or self.preserve.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.preserve.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "push"):
                                    if (self.push is None):
                                        self.push = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push()
                                        self.push.parent = self
                                        self._children_name_map["push"] = "push"
                                    return self.push

                                if (child_yang_name == "swap"):
                                    if (self.swap is None):
                                        self.swap = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap()
                                        self.swap.parent = self
                                        self._children_name_map["swap"] = "swap"
                                    return self.swap

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "push" or name == "swap" or name == "pop-and-forward" or name == "preserve"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "pop-and-forward"):
                                    self.pop_and_forward = value
                                    self.pop_and_forward.value_namespace = name_space
                                    self.pop_and_forward.value_namespace_prefix = name_space_prefix
                                if(value_path == "preserve"):
                                    self.preserve = value
                                    self.preserve.value_namespace = name_space
                                    self.preserve.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.index.is_set or
                                self.protected_by.is_set or
                                self.type.is_set or
                                (self.next_hop_type is not None and self.next_hop_type.has_data()) or
                                (self.operations is not None and self.operations.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.protected_by.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set or
                                (self.next_hop_type is not None and self.next_hop_type.has_operation()) or
                                (self.operations is not None and self.operations.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "next-hop" + "[index='" + self.index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.protected_by.is_set or self.protected_by.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protected_by.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "next-hop-type"):
                                if (self.next_hop_type is None):
                                    self.next_hop_type = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType()
                                    self.next_hop_type.parent = self
                                    self._children_name_map["next_hop_type"] = "next-hop-type"
                                return self.next_hop_type

                            if (child_yang_name == "operations"):
                                if (self.operations is None):
                                    self.operations = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations()
                                    self.operations.parent = self
                                    self._children_name_map["operations"] = "operations"
                                return self.operations

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "next-hop-type" or name == "operations" or name == "index" or name == "protected-by" or name == "type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "protected-by"):
                                self.protected_by = value
                                self.protected_by.value_namespace = name_space
                                self.protected_by.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.next_hop:
                            if (c.has_data()):
                                return True
                        return (
                            self.auto_protect.is_set or
                            (self.operations is not None and self.operations.has_data()))

                    def has_operation(self):
                        for c in self.next_hop:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.auto_protect.yfilter != YFilter.not_set or
                            (self.operations is not None and self.operations.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "path" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.auto_protect.is_set or self.auto_protect.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auto_protect.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "next-hop"):
                            for c in self.next_hop:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.next_hop.append(c)
                            return c

                        if (child_yang_name == "operations"):
                            if (self.operations is None):
                                self.operations = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations()
                                self.operations.parent = self
                                self._children_name_map["operations"] = "operations"
                            return self.operations

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "operations" or name == "auto-protect"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "auto-protect"):
                            self.auto_protect = value
                            self.auto_protect.value_namespace = name_space
                            self.auto_protect.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.vrf_name.is_set or
                        self.in_label.is_set or
                        (self.path is not None and self.path.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        self.in_label.yfilter != YFilter.not_set or
                        (self.path is not None and self.path.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "in-label-lsp" + "[vrf-name='" + self.vrf_name.get() + "']" + "[in-label='" + self.in_label.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "common-mpls-static:mpls-static/mpls-static-cfg/in-label-lsps/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())
                    if (self.in_label.is_set or self.in_label.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_label.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "path"):
                        if (self.path is None):
                            self.path = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path()
                            self.path.parent = self
                            self._children_name_map["path"] = "path"
                        return self.path

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "path" or name == "vrf-name" or name == "in-label"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-label"):
                        self.in_label = value
                        self.in_label.value_namespace = name_space
                        self.in_label.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.in_label_lsp:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.in_label_lsp:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "in-label-lsps" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "common-mpls-static:mpls-static/mpls-static-cfg/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "in-label-lsp"):
                    for c in self.in_label_lsp:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.in_label_lsp.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "in-label-lsp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Ipv6IngressLsps(Entity):
            """
            The LSPs indexed by ipv6 prefix
            
            .. attribute:: ipv6_ingress_lsp
            
            	MPLS Static IPv6 Label Switched Path Configuration at Ingress
            	**type**\: list of    :py:class:`Ipv6IngressLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps, self).__init__()

                self.yang_name = "ipv6-ingress-lsps"
                self.yang_parent_name = "mpls-static-cfg"

                self.ipv6_ingress_lsp = YList(self)

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
                            super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps, self).__setattr__(name, value)


            class Ipv6IngressLsp(Entity):
                """
                MPLS Static IPv6 Label Switched Path
                Configuration at Ingress
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF
                	**type**\:  str
                
                .. attribute:: prefix  <key>
                
                	IPv6 prefix of packets that will ingress on this LSP
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                .. attribute:: in_label
                
                	Value of the local label. Optional for ingress
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 16..1048575
                
                
                ----
                	**type**\:   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                
                
                ----
                .. attribute:: name
                
                	Name of the LSP
                	**type**\:  str
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp, self).__init__()

                    self.yang_name = "ipv6-ingress-lsp"
                    self.yang_parent_name = "ipv6-ingress-lsps"

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.prefix = YLeaf(YType.str, "prefix")

                    self.in_label = YLeaf(YType.str, "in-label")

                    self.name = YLeaf(YType.str, "name")

                    self.path = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path()
                    self.path.parent = self
                    self._children_name_map["path"] = "path"
                    self._children_yang_names.add("path")

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
                                    "prefix",
                                    "in_label",
                                    "name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp, self).__setattr__(name, value)


                class Path(Entity):
                    """
                    Fowarding path
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop>`
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path, self).__init__()

                        self.yang_name = "path"
                        self.yang_parent_name = "ipv6-ingress-lsp"

                        self.auto_protect = YLeaf(YType.boolean, "auto-protect")

                        self.operations = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations()
                        self.operations.parent = self
                        self._children_name_map["operations"] = "operations"
                        self._children_yang_names.add("operations")

                        self.next_hop = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("auto_protect") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path, self).__setattr__(name, value)


                    class Operations(Entity):
                        """
                        The incoming label processing
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push>`
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations, self).__init__()

                            self.yang_name = "operations"
                            self.yang_parent_name = "path"

                            self.pop_and_forward = YLeaf(YType.empty, "pop-and-forward")

                            self.preserve = YLeaf(YType.empty, "preserve")

                            self.push = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push()
                            self.push.parent = self
                            self._children_name_map["push"] = "push"
                            self._children_yang_names.add("push")

                            self.swap = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap()
                            self.swap.parent = self
                            self._children_name_map["swap"] = "swap"
                            self._children_yang_names.add("swap")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("pop_and_forward",
                                            "preserve") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations, self).__setattr__(name, value)


                        class Swap(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap, self).__init__()

                                self.yang_name = "swap"
                                self.yang_parent_name = "operations"

                                self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._children_yang_names.add("stack")


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "swap"

                                    self.label_stack = YLeafList(YType.str, "label-stack")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_stack") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack, self).__setattr__(name, value)

                                def has_data(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return False

                                def has_operation(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_stack.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stack" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-stack"):
                                        self.label_stack.append(value)

                            def has_data(self):
                                return (self.stack is not None and self.stack.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.stack is not None and self.stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "swap" + path_buffer

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

                                if (child_yang_name == "stack"):
                                    if (self.stack is None):
                                        self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack()
                                        self.stack.parent = self
                                        self._children_name_map["stack"] = "stack"
                                    return self.stack

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "stack"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Push(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push, self).__init__()

                                self.yang_name = "push"
                                self.yang_parent_name = "operations"

                                self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._children_yang_names.add("stack")


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "push"

                                    self.label_stack = YLeafList(YType.str, "label-stack")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_stack") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack, self).__setattr__(name, value)

                                def has_data(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return False

                                def has_operation(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_stack.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stack" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-stack"):
                                        self.label_stack.append(value)

                            def has_data(self):
                                return (self.stack is not None and self.stack.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.stack is not None and self.stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "push" + path_buffer

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

                                if (child_yang_name == "stack"):
                                    if (self.stack is None):
                                        self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack()
                                        self.stack.parent = self
                                        self._children_name_map["stack"] = "stack"
                                    return self.stack

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "stack"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.pop_and_forward.is_set or
                                self.preserve.is_set or
                                (self.push is not None and self.push.has_data()) or
                                (self.swap is not None and self.swap.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.pop_and_forward.yfilter != YFilter.not_set or
                                self.preserve.yfilter != YFilter.not_set or
                                (self.push is not None and self.push.has_operation()) or
                                (self.swap is not None and self.swap.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operations" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.pop_and_forward.is_set or self.pop_and_forward.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pop_and_forward.get_name_leafdata())
                            if (self.preserve.is_set or self.preserve.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.preserve.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "push"):
                                if (self.push is None):
                                    self.push = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push()
                                    self.push.parent = self
                                    self._children_name_map["push"] = "push"
                                return self.push

                            if (child_yang_name == "swap"):
                                if (self.swap is None):
                                    self.swap = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap()
                                    self.swap.parent = self
                                    self._children_name_map["swap"] = "swap"
                                return self.swap

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "push" or name == "swap" or name == "pop-and-forward" or name == "preserve"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "pop-and-forward"):
                                self.pop_and_forward = value
                                self.pop_and_forward.value_namespace = name_space
                                self.pop_and_forward.value_namespace_prefix = name_space_prefix
                            if(value_path == "preserve"):
                                self.preserve = value
                                self.preserve.value_namespace = name_space
                                self.preserve.value_namespace_prefix = name_space_prefix


                    class NextHop(Entity):
                        """
                        next\-hops list
                        
                        .. attribute:: index  <key>
                        
                        	Index of the nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations>`
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:   :py:class:`Hoptype <ydk.models.cisco_ios_xe.common_mpls_static.Hoptype>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "path"

                            self.index = YLeaf(YType.uint32, "index")

                            self.protected_by = YLeaf(YType.uint32, "protected-by")

                            self.type = YLeaf(YType.enumeration, "type")

                            self.next_hop_type = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self._children_name_map["next_hop_type"] = "next-hop-type"
                            self._children_yang_names.add("next-hop-type")

                            self.operations = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self._children_name_map["operations"] = "operations"
                            self._children_yang_names.add("operations")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("index",
                                            "protected_by",
                                            "type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop, self).__setattr__(name, value)


                        class NextHopType(Entity):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType, self).__init__()

                                self.yang_name = "next-hop-type"
                                self.yang_parent_name = "next-hop"

                                self.if_index = YLeaf(YType.uint32, "if-index")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                self.mac_address = YLeaf(YType.str, "mac-address")

                                self.out_interface_name = YLeaf(YType.str, "out-interface-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("if_index",
                                                "ipv4_address",
                                                "ipv6_address",
                                                "mac_address",
                                                "out_interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.if_index.is_set or
                                    self.ipv4_address.is_set or
                                    self.ipv6_address.is_set or
                                    self.mac_address.is_set or
                                    self.out_interface_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.if_index.yfilter != YFilter.not_set or
                                    self.ipv4_address.yfilter != YFilter.not_set or
                                    self.ipv6_address.yfilter != YFilter.not_set or
                                    self.mac_address.yfilter != YFilter.not_set or
                                    self.out_interface_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "next-hop-type" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.if_index.get_name_leafdata())
                                if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                                if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mac_address.get_name_leafdata())
                                if (self.out_interface_name.is_set or self.out_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "if-index" or name == "ipv4-address" or name == "ipv6-address" or name == "mac-address" or name == "out-interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "if-index"):
                                    self.if_index = value
                                    self.if_index.value_namespace = name_space
                                    self.if_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv4-address"):
                                    self.ipv4_address = value
                                    self.ipv4_address.value_namespace = name_space
                                    self.ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv6-address"):
                                    self.ipv6_address = value
                                    self.ipv6_address.value_namespace = name_space
                                    self.ipv6_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "mac-address"):
                                    self.mac_address = value
                                    self.mac_address.value_namespace = name_space
                                    self.mac_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-interface-name"):
                                    self.out_interface_name = value
                                    self.out_interface_name.value_namespace = name_space
                                    self.out_interface_name.value_namespace_prefix = name_space_prefix


                        class Operations(Entity):
                            """
                            The incoming label processing
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations, self).__init__()

                                self.yang_name = "operations"
                                self.yang_parent_name = "next-hop"

                                self.pop_and_forward = YLeaf(YType.empty, "pop-and-forward")

                                self.preserve = YLeaf(YType.empty, "preserve")

                                self.push = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self._children_name_map["push"] = "push"
                                self._children_yang_names.add("push")

                                self.swap = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self
                                self._children_name_map["swap"] = "swap"
                                self._children_yang_names.add("swap")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("pop_and_forward",
                                                "preserve") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations, self).__setattr__(name, value)


                            class Swap(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap, self).__init__()

                                    self.yang_name = "swap"
                                    self.yang_parent_name = "operations"

                                    self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._children_yang_names.add("stack")


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "swap"

                                        self.label_stack = YLeafList(YType.str, "label-stack")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("label_stack") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.label_stack.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "stack" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "label-stack"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "label-stack"):
                                            self.label_stack.append(value)

                                def has_data(self):
                                    return (self.stack is not None and self.stack.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.stack is not None and self.stack.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "swap" + path_buffer

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

                                    if (child_yang_name == "stack"):
                                        if (self.stack is None):
                                            self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack()
                                            self.stack.parent = self
                                            self._children_name_map["stack"] = "stack"
                                        return self.stack

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Push(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push, self).__init__()

                                    self.yang_name = "push"
                                    self.yang_parent_name = "operations"

                                    self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._children_yang_names.add("stack")


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "push"

                                        self.label_stack = YLeafList(YType.str, "label-stack")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("label_stack") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.label_stack.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "stack" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "label-stack"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "label-stack"):
                                            self.label_stack.append(value)

                                def has_data(self):
                                    return (self.stack is not None and self.stack.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.stack is not None and self.stack.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "push" + path_buffer

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

                                    if (child_yang_name == "stack"):
                                        if (self.stack is None):
                                            self.stack = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack()
                                            self.stack.parent = self
                                            self._children_name_map["stack"] = "stack"
                                        return self.stack

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.pop_and_forward.is_set or
                                    self.preserve.is_set or
                                    (self.push is not None and self.push.has_data()) or
                                    (self.swap is not None and self.swap.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.pop_and_forward.yfilter != YFilter.not_set or
                                    self.preserve.yfilter != YFilter.not_set or
                                    (self.push is not None and self.push.has_operation()) or
                                    (self.swap is not None and self.swap.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "operations" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.pop_and_forward.is_set or self.pop_and_forward.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pop_and_forward.get_name_leafdata())
                                if (self.preserve.is_set or self.preserve.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.preserve.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "push"):
                                    if (self.push is None):
                                        self.push = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push()
                                        self.push.parent = self
                                        self._children_name_map["push"] = "push"
                                    return self.push

                                if (child_yang_name == "swap"):
                                    if (self.swap is None):
                                        self.swap = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap()
                                        self.swap.parent = self
                                        self._children_name_map["swap"] = "swap"
                                    return self.swap

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "push" or name == "swap" or name == "pop-and-forward" or name == "preserve"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "pop-and-forward"):
                                    self.pop_and_forward = value
                                    self.pop_and_forward.value_namespace = name_space
                                    self.pop_and_forward.value_namespace_prefix = name_space_prefix
                                if(value_path == "preserve"):
                                    self.preserve = value
                                    self.preserve.value_namespace = name_space
                                    self.preserve.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.index.is_set or
                                self.protected_by.is_set or
                                self.type.is_set or
                                (self.next_hop_type is not None and self.next_hop_type.has_data()) or
                                (self.operations is not None and self.operations.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.protected_by.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set or
                                (self.next_hop_type is not None and self.next_hop_type.has_operation()) or
                                (self.operations is not None and self.operations.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "next-hop" + "[index='" + self.index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.protected_by.is_set or self.protected_by.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protected_by.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "next-hop-type"):
                                if (self.next_hop_type is None):
                                    self.next_hop_type = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType()
                                    self.next_hop_type.parent = self
                                    self._children_name_map["next_hop_type"] = "next-hop-type"
                                return self.next_hop_type

                            if (child_yang_name == "operations"):
                                if (self.operations is None):
                                    self.operations = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations()
                                    self.operations.parent = self
                                    self._children_name_map["operations"] = "operations"
                                return self.operations

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "next-hop-type" or name == "operations" or name == "index" or name == "protected-by" or name == "type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "protected-by"):
                                self.protected_by = value
                                self.protected_by.value_namespace = name_space
                                self.protected_by.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.next_hop:
                            if (c.has_data()):
                                return True
                        return (
                            self.auto_protect.is_set or
                            (self.operations is not None and self.operations.has_data()))

                    def has_operation(self):
                        for c in self.next_hop:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.auto_protect.yfilter != YFilter.not_set or
                            (self.operations is not None and self.operations.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "path" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.auto_protect.is_set or self.auto_protect.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auto_protect.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "next-hop"):
                            for c in self.next_hop:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.next_hop.append(c)
                            return c

                        if (child_yang_name == "operations"):
                            if (self.operations is None):
                                self.operations = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations()
                                self.operations.parent = self
                                self._children_name_map["operations"] = "operations"
                            return self.operations

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "operations" or name == "auto-protect"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "auto-protect"):
                            self.auto_protect = value
                            self.auto_protect.value_namespace = name_space
                            self.auto_protect.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.vrf_name.is_set or
                        self.prefix.is_set or
                        self.in_label.is_set or
                        self.name.is_set or
                        (self.path is not None and self.path.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        self.prefix.yfilter != YFilter.not_set or
                        self.in_label.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.path is not None and self.path.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv6-ingress-lsp" + "[vrf-name='" + self.vrf_name.get() + "']" + "[prefix='" + self.prefix.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "common-mpls-static:mpls-static/mpls-static-cfg/ipv6-ingress-lsps/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())
                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix.get_name_leafdata())
                    if (self.in_label.is_set or self.in_label.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_label.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "path"):
                        if (self.path is None):
                            self.path = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path()
                            self.path.parent = self
                            self._children_name_map["path"] = "path"
                        return self.path

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "path" or name == "vrf-name" or name == "prefix" or name == "in-label" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix"):
                        self.prefix = value
                        self.prefix.value_namespace = name_space
                        self.prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-label"):
                        self.in_label = value
                        self.in_label.value_namespace = name_space
                        self.in_label.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ipv6_ingress_lsp:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.ipv6_ingress_lsp:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6-ingress-lsps" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "common-mpls-static:mpls-static/mpls-static-cfg/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv6-ingress-lsp"):
                    for c in self.ipv6_ingress_lsp:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ipv6_ingress_lsp.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv6-ingress-lsp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class NamedLsps(Entity):
            """
            The LSPs indexed by name
            
            .. attribute:: named_lsp
            
            	MPLS Static Label Switched Path Configuration. The LSPs in this list are referenced by a string name. The LSPs may be ingress/egress/crossconnect, may have v4/v6 prefixes and may be associated with any VRF. The other specialized lists above are for implemetations that are keyed on prefixes or in\-labels instead of the LSP name
            	**type**\: list of    :py:class:`NamedLsp <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticCfg.NamedLsps, self).__init__()

                self.yang_name = "named-lsps"
                self.yang_parent_name = "mpls-static-cfg"

                self.named_lsp = YList(self)

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
                            super(MplsStatic.MplsStaticCfg.NamedLsps, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsStatic.MplsStaticCfg.NamedLsps, self).__setattr__(name, value)


            class NamedLsp(Entity):
                """
                MPLS Static Label Switched Path Configuration.
                The LSPs in this list are referenced by a string name.
                The LSPs may be ingress/egress/crossconnect,
                may have v4/v6 prefixes and may be associated with any
                VRF. The other specialized lists above are for
                implemetations that are keyed on prefixes or in\-labels
                instead of the LSP name.
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF
                	**type**\:  str
                
                .. attribute:: name  <key>
                
                	Name of the LSP
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: in_label
                
                	Value of the local label
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 16..1048575
                
                
                ----
                	**type**\:   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                
                
                ----
                .. attribute:: ipv4_prefix
                
                	ipv4 prefix
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                .. attribute:: ipv6_prefix
                
                	ipv6 prefix
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                .. attribute:: lsp_type
                
                	lsp type
                	**type**\:   :py:class:`LspType <ydk.models.cisco_ios_xe.common_mpls_static.LspType>`
                
                	**mandatory**\: True
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp, self).__init__()

                    self.yang_name = "named-lsp"
                    self.yang_parent_name = "named-lsps"

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.name = YLeaf(YType.str, "name")

                    self.in_label = YLeaf(YType.str, "in-label")

                    self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                    self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                    self.lsp_type = YLeaf(YType.identityref, "lsp-type")

                    self.path = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path()
                    self.path.parent = self
                    self._children_name_map["path"] = "path"
                    self._children_yang_names.add("path")

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
                                    "name",
                                    "in_label",
                                    "ipv4_prefix",
                                    "ipv6_prefix",
                                    "lsp_type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp, self).__setattr__(name, value)


                class Path(Entity):
                    """
                    Fowarding path
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop>`
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path, self).__init__()

                        self.yang_name = "path"
                        self.yang_parent_name = "named-lsp"

                        self.auto_protect = YLeaf(YType.boolean, "auto-protect")

                        self.operations = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations()
                        self.operations.parent = self
                        self._children_name_map["operations"] = "operations"
                        self._children_yang_names.add("operations")

                        self.next_hop = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("auto_protect") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path, self).__setattr__(name, value)


                    class Operations(Entity):
                        """
                        The incoming label processing
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push>`
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations, self).__init__()

                            self.yang_name = "operations"
                            self.yang_parent_name = "path"

                            self.pop_and_forward = YLeaf(YType.empty, "pop-and-forward")

                            self.preserve = YLeaf(YType.empty, "preserve")

                            self.push = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push()
                            self.push.parent = self
                            self._children_name_map["push"] = "push"
                            self._children_yang_names.add("push")

                            self.swap = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap()
                            self.swap.parent = self
                            self._children_name_map["swap"] = "swap"
                            self._children_yang_names.add("swap")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("pop_and_forward",
                                            "preserve") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations, self).__setattr__(name, value)


                        class Swap(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap, self).__init__()

                                self.yang_name = "swap"
                                self.yang_parent_name = "operations"

                                self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._children_yang_names.add("stack")


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "swap"

                                    self.label_stack = YLeafList(YType.str, "label-stack")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_stack") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack, self).__setattr__(name, value)

                                def has_data(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return False

                                def has_operation(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_stack.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stack" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-stack"):
                                        self.label_stack.append(value)

                            def has_data(self):
                                return (self.stack is not None and self.stack.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.stack is not None and self.stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "swap" + path_buffer

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

                                if (child_yang_name == "stack"):
                                    if (self.stack is None):
                                        self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack()
                                        self.stack.parent = self
                                        self._children_name_map["stack"] = "stack"
                                    return self.stack

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "stack"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Push(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push, self).__init__()

                                self.yang_name = "push"
                                self.yang_parent_name = "operations"

                                self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._children_yang_names.add("stack")


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "push"

                                    self.label_stack = YLeafList(YType.str, "label-stack")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_stack") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack, self).__setattr__(name, value)

                                def has_data(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return False

                                def has_operation(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_stack.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stack" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-stack"):
                                        self.label_stack.append(value)

                            def has_data(self):
                                return (self.stack is not None and self.stack.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.stack is not None and self.stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "push" + path_buffer

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

                                if (child_yang_name == "stack"):
                                    if (self.stack is None):
                                        self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack()
                                        self.stack.parent = self
                                        self._children_name_map["stack"] = "stack"
                                    return self.stack

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "stack"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.pop_and_forward.is_set or
                                self.preserve.is_set or
                                (self.push is not None and self.push.has_data()) or
                                (self.swap is not None and self.swap.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.pop_and_forward.yfilter != YFilter.not_set or
                                self.preserve.yfilter != YFilter.not_set or
                                (self.push is not None and self.push.has_operation()) or
                                (self.swap is not None and self.swap.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operations" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.pop_and_forward.is_set or self.pop_and_forward.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pop_and_forward.get_name_leafdata())
                            if (self.preserve.is_set or self.preserve.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.preserve.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "push"):
                                if (self.push is None):
                                    self.push = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push()
                                    self.push.parent = self
                                    self._children_name_map["push"] = "push"
                                return self.push

                            if (child_yang_name == "swap"):
                                if (self.swap is None):
                                    self.swap = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap()
                                    self.swap.parent = self
                                    self._children_name_map["swap"] = "swap"
                                return self.swap

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "push" or name == "swap" or name == "pop-and-forward" or name == "preserve"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "pop-and-forward"):
                                self.pop_and_forward = value
                                self.pop_and_forward.value_namespace = name_space
                                self.pop_and_forward.value_namespace_prefix = name_space_prefix
                            if(value_path == "preserve"):
                                self.preserve = value
                                self.preserve.value_namespace = name_space
                                self.preserve.value_namespace_prefix = name_space_prefix


                    class NextHop(Entity):
                        """
                        next\-hops list
                        
                        .. attribute:: index  <key>
                        
                        	Index of the nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations>`
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:   :py:class:`Hoptype <ydk.models.cisco_ios_xe.common_mpls_static.Hoptype>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "path"

                            self.index = YLeaf(YType.uint32, "index")

                            self.protected_by = YLeaf(YType.uint32, "protected-by")

                            self.type = YLeaf(YType.enumeration, "type")

                            self.next_hop_type = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self._children_name_map["next_hop_type"] = "next-hop-type"
                            self._children_yang_names.add("next-hop-type")

                            self.operations = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations()
                            self.operations.parent = self
                            self._children_name_map["operations"] = "operations"
                            self._children_yang_names.add("operations")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("index",
                                            "protected_by",
                                            "type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop, self).__setattr__(name, value)


                        class NextHopType(Entity):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType, self).__init__()

                                self.yang_name = "next-hop-type"
                                self.yang_parent_name = "next-hop"

                                self.if_index = YLeaf(YType.uint32, "if-index")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                self.mac_address = YLeaf(YType.str, "mac-address")

                                self.out_interface_name = YLeaf(YType.str, "out-interface-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("if_index",
                                                "ipv4_address",
                                                "ipv6_address",
                                                "mac_address",
                                                "out_interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.if_index.is_set or
                                    self.ipv4_address.is_set or
                                    self.ipv6_address.is_set or
                                    self.mac_address.is_set or
                                    self.out_interface_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.if_index.yfilter != YFilter.not_set or
                                    self.ipv4_address.yfilter != YFilter.not_set or
                                    self.ipv6_address.yfilter != YFilter.not_set or
                                    self.mac_address.yfilter != YFilter.not_set or
                                    self.out_interface_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "next-hop-type" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.if_index.get_name_leafdata())
                                if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                                if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mac_address.get_name_leafdata())
                                if (self.out_interface_name.is_set or self.out_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "if-index" or name == "ipv4-address" or name == "ipv6-address" or name == "mac-address" or name == "out-interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "if-index"):
                                    self.if_index = value
                                    self.if_index.value_namespace = name_space
                                    self.if_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv4-address"):
                                    self.ipv4_address = value
                                    self.ipv4_address.value_namespace = name_space
                                    self.ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv6-address"):
                                    self.ipv6_address = value
                                    self.ipv6_address.value_namespace = name_space
                                    self.ipv6_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "mac-address"):
                                    self.mac_address = value
                                    self.mac_address.value_namespace = name_space
                                    self.mac_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-interface-name"):
                                    self.out_interface_name = value
                                    self.out_interface_name.value_namespace = name_space
                                    self.out_interface_name.value_namespace_prefix = name_space_prefix


                        class Operations(Entity):
                            """
                            The incoming label processing
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations, self).__init__()

                                self.yang_name = "operations"
                                self.yang_parent_name = "next-hop"

                                self.pop_and_forward = YLeaf(YType.empty, "pop-and-forward")

                                self.preserve = YLeaf(YType.empty, "preserve")

                                self.push = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self._children_name_map["push"] = "push"
                                self._children_yang_names.add("push")

                                self.swap = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap()
                                self.swap.parent = self
                                self._children_name_map["swap"] = "swap"
                                self._children_yang_names.add("swap")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("pop_and_forward",
                                                "preserve") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations, self).__setattr__(name, value)


                            class Swap(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap, self).__init__()

                                    self.yang_name = "swap"
                                    self.yang_parent_name = "operations"

                                    self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._children_yang_names.add("stack")


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "swap"

                                        self.label_stack = YLeafList(YType.str, "label-stack")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("label_stack") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.label_stack.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "stack" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "label-stack"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "label-stack"):
                                            self.label_stack.append(value)

                                def has_data(self):
                                    return (self.stack is not None and self.stack.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.stack is not None and self.stack.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "swap" + path_buffer

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

                                    if (child_yang_name == "stack"):
                                        if (self.stack is None):
                                            self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack()
                                            self.stack.parent = self
                                            self._children_name_map["stack"] = "stack"
                                        return self.stack

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Push(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push, self).__init__()

                                    self.yang_name = "push"
                                    self.yang_parent_name = "operations"

                                    self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._children_yang_names.add("stack")


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "push"

                                        self.label_stack = YLeafList(YType.str, "label-stack")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("label_stack") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.label_stack.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "stack" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "label-stack"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "label-stack"):
                                            self.label_stack.append(value)

                                def has_data(self):
                                    return (self.stack is not None and self.stack.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.stack is not None and self.stack.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "push" + path_buffer

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

                                    if (child_yang_name == "stack"):
                                        if (self.stack is None):
                                            self.stack = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack()
                                            self.stack.parent = self
                                            self._children_name_map["stack"] = "stack"
                                        return self.stack

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.pop_and_forward.is_set or
                                    self.preserve.is_set or
                                    (self.push is not None and self.push.has_data()) or
                                    (self.swap is not None and self.swap.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.pop_and_forward.yfilter != YFilter.not_set or
                                    self.preserve.yfilter != YFilter.not_set or
                                    (self.push is not None and self.push.has_operation()) or
                                    (self.swap is not None and self.swap.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "operations" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.pop_and_forward.is_set or self.pop_and_forward.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pop_and_forward.get_name_leafdata())
                                if (self.preserve.is_set or self.preserve.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.preserve.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "push"):
                                    if (self.push is None):
                                        self.push = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push()
                                        self.push.parent = self
                                        self._children_name_map["push"] = "push"
                                    return self.push

                                if (child_yang_name == "swap"):
                                    if (self.swap is None):
                                        self.swap = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap()
                                        self.swap.parent = self
                                        self._children_name_map["swap"] = "swap"
                                    return self.swap

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "push" or name == "swap" or name == "pop-and-forward" or name == "preserve"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "pop-and-forward"):
                                    self.pop_and_forward = value
                                    self.pop_and_forward.value_namespace = name_space
                                    self.pop_and_forward.value_namespace_prefix = name_space_prefix
                                if(value_path == "preserve"):
                                    self.preserve = value
                                    self.preserve.value_namespace = name_space
                                    self.preserve.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.index.is_set or
                                self.protected_by.is_set or
                                self.type.is_set or
                                (self.next_hop_type is not None and self.next_hop_type.has_data()) or
                                (self.operations is not None and self.operations.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.protected_by.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set or
                                (self.next_hop_type is not None and self.next_hop_type.has_operation()) or
                                (self.operations is not None and self.operations.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "next-hop" + "[index='" + self.index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.protected_by.is_set or self.protected_by.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protected_by.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "next-hop-type"):
                                if (self.next_hop_type is None):
                                    self.next_hop_type = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType()
                                    self.next_hop_type.parent = self
                                    self._children_name_map["next_hop_type"] = "next-hop-type"
                                return self.next_hop_type

                            if (child_yang_name == "operations"):
                                if (self.operations is None):
                                    self.operations = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations()
                                    self.operations.parent = self
                                    self._children_name_map["operations"] = "operations"
                                return self.operations

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "next-hop-type" or name == "operations" or name == "index" or name == "protected-by" or name == "type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "protected-by"):
                                self.protected_by = value
                                self.protected_by.value_namespace = name_space
                                self.protected_by.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.next_hop:
                            if (c.has_data()):
                                return True
                        return (
                            self.auto_protect.is_set or
                            (self.operations is not None and self.operations.has_data()))

                    def has_operation(self):
                        for c in self.next_hop:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.auto_protect.yfilter != YFilter.not_set or
                            (self.operations is not None and self.operations.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "path" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.auto_protect.is_set or self.auto_protect.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auto_protect.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "next-hop"):
                            for c in self.next_hop:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.next_hop.append(c)
                            return c

                        if (child_yang_name == "operations"):
                            if (self.operations is None):
                                self.operations = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations()
                                self.operations.parent = self
                                self._children_name_map["operations"] = "operations"
                            return self.operations

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "operations" or name == "auto-protect"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "auto-protect"):
                            self.auto_protect = value
                            self.auto_protect.value_namespace = name_space
                            self.auto_protect.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.vrf_name.is_set or
                        self.name.is_set or
                        self.in_label.is_set or
                        self.ipv4_prefix.is_set or
                        self.ipv6_prefix.is_set or
                        self.lsp_type.is_set or
                        (self.path is not None and self.path.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.in_label.yfilter != YFilter.not_set or
                        self.ipv4_prefix.yfilter != YFilter.not_set or
                        self.ipv6_prefix.yfilter != YFilter.not_set or
                        self.lsp_type.yfilter != YFilter.not_set or
                        (self.path is not None and self.path.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "named-lsp" + "[vrf-name='" + self.vrf_name.get() + "']" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "common-mpls-static:mpls-static/mpls-static-cfg/named-lsps/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.in_label.is_set or self.in_label.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_label.get_name_leafdata())
                    if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                    if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())
                    if (self.lsp_type.is_set or self.lsp_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lsp_type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "path"):
                        if (self.path is None):
                            self.path = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path()
                            self.path.parent = self
                            self._children_name_map["path"] = "path"
                        return self.path

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "path" or name == "vrf-name" or name == "name" or name == "in-label" or name == "ipv4-prefix" or name == "ipv6-prefix" or name == "lsp-type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-label"):
                        self.in_label = value
                        self.in_label.value_namespace = name_space
                        self.in_label.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv4-prefix"):
                        self.ipv4_prefix = value
                        self.ipv4_prefix.value_namespace = name_space
                        self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv6-prefix"):
                        self.ipv6_prefix = value
                        self.ipv6_prefix.value_namespace = name_space
                        self.ipv6_prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "lsp-type"):
                        self.lsp_type = value
                        self.lsp_type.value_namespace = name_space
                        self.lsp_type.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.named_lsp:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.named_lsp:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "named-lsps" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "common-mpls-static:mpls-static/mpls-static-cfg/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "named-lsp"):
                    for c in self.named_lsp:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.named_lsp.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "named-lsp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.in_label_lsps is not None and self.in_label_lsps.has_data()) or
                (self.interfaces is not None and self.interfaces.has_data()) or
                (self.ipv4_ingress_lsps is not None and self.ipv4_ingress_lsps.has_data()) or
                (self.ipv6_ingress_lsps is not None and self.ipv6_ingress_lsps.has_data()) or
                (self.named_lsps is not None and self.named_lsps.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.in_label_lsps is not None and self.in_label_lsps.has_operation()) or
                (self.interfaces is not None and self.interfaces.has_operation()) or
                (self.ipv4_ingress_lsps is not None and self.ipv4_ingress_lsps.has_operation()) or
                (self.ipv6_ingress_lsps is not None and self.ipv6_ingress_lsps.has_operation()) or
                (self.named_lsps is not None and self.named_lsps.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mpls-static-cfg" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "common-mpls-static:mpls-static/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "in-label-lsps"):
                if (self.in_label_lsps is None):
                    self.in_label_lsps = MplsStatic.MplsStaticCfg.InLabelLsps()
                    self.in_label_lsps.parent = self
                    self._children_name_map["in_label_lsps"] = "in-label-lsps"
                return self.in_label_lsps

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = MplsStatic.MplsStaticCfg.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            if (child_yang_name == "ipv4-ingress-lsps"):
                if (self.ipv4_ingress_lsps is None):
                    self.ipv4_ingress_lsps = MplsStatic.MplsStaticCfg.Ipv4IngressLsps()
                    self.ipv4_ingress_lsps.parent = self
                    self._children_name_map["ipv4_ingress_lsps"] = "ipv4-ingress-lsps"
                return self.ipv4_ingress_lsps

            if (child_yang_name == "ipv6-ingress-lsps"):
                if (self.ipv6_ingress_lsps is None):
                    self.ipv6_ingress_lsps = MplsStatic.MplsStaticCfg.Ipv6IngressLsps()
                    self.ipv6_ingress_lsps.parent = self
                    self._children_name_map["ipv6_ingress_lsps"] = "ipv6-ingress-lsps"
                return self.ipv6_ingress_lsps

            if (child_yang_name == "named-lsps"):
                if (self.named_lsps is None):
                    self.named_lsps = MplsStatic.MplsStaticCfg.NamedLsps()
                    self.named_lsps.parent = self
                    self._children_name_map["named_lsps"] = "named-lsps"
                return self.named_lsps

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "in-label-lsps" or name == "interfaces" or name == "ipv4-ingress-lsps" or name == "ipv6-ingress-lsps" or name == "named-lsps"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class MplsStaticState(Entity):
        """
        MPLS static operational data
        
        .. attribute:: label_switched_paths
        
        	MPLS Static Label Switched Paths
        	**type**\:   :py:class:`LabelSwitchedPaths <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths>`
        
        

        """

        _prefix = 'ms'
        _revision = '2015-07-22'

        def __init__(self):
            super(MplsStatic.MplsStaticState, self).__init__()

            self.yang_name = "mpls-static-state"
            self.yang_parent_name = "mpls-static"

            self.label_switched_paths = MplsStatic.MplsStaticState.LabelSwitchedPaths()
            self.label_switched_paths.parent = self
            self._children_name_map["label_switched_paths"] = "label-switched-paths"
            self._children_yang_names.add("label-switched-paths")


        class LabelSwitchedPaths(Entity):
            """
            MPLS Static Label Switched Paths
            
            .. attribute:: label_switched_path
            
            	MPLS LSPs list
            	**type**\: list of    :py:class:`LabelSwitchedPath <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath>`
            
            

            """

            _prefix = 'ms'
            _revision = '2015-07-22'

            def __init__(self):
                super(MplsStatic.MplsStaticState.LabelSwitchedPaths, self).__init__()

                self.yang_name = "label-switched-paths"
                self.yang_parent_name = "mpls-static-state"

                self.label_switched_path = YList(self)

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
                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths, self).__setattr__(name, value)


            class LabelSwitchedPath(Entity):
                """
                MPLS LSPs list
                
                .. attribute:: vrf_name  <key>
                
                	Name of the VRF
                	**type**\:  str
                
                .. attribute:: prefix  <key>
                
                	IP v4/v6 prefix
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                .. attribute:: egress_stats
                
                	egress stats
                	**type**\:   :py:class:`EgressStats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats>`
                
                .. attribute:: in_label_value
                
                	Value of the local label
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 16..1048575
                
                
                ----
                	**type**\:   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                
                
                ----
                .. attribute:: ingress_stats
                
                	ingress stats
                	**type**\:   :py:class:`IngressStats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats>`
                
                .. attribute:: name
                
                	Name of the LSP
                	**type**\:  str
                
                .. attribute:: path
                
                	Fowarding path
                	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path>`
                
                

                """

                _prefix = 'ms'
                _revision = '2015-07-22'

                def __init__(self):
                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath, self).__init__()

                    self.yang_name = "label-switched-path"
                    self.yang_parent_name = "label-switched-paths"

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.prefix = YLeaf(YType.str, "prefix")

                    self.in_label_value = YLeaf(YType.str, "in-label-value")

                    self.name = YLeaf(YType.str, "name")

                    self.egress_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats()
                    self.egress_stats.parent = self
                    self._children_name_map["egress_stats"] = "egress-stats"
                    self._children_yang_names.add("egress-stats")

                    self.ingress_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats()
                    self.ingress_stats.parent = self
                    self._children_name_map["ingress_stats"] = "ingress-stats"
                    self._children_yang_names.add("ingress-stats")

                    self.path = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path()
                    self.path.parent = self
                    self._children_name_map["path"] = "path"
                    self._children_yang_names.add("path")

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
                                    "prefix",
                                    "in_label_value",
                                    "name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath, self).__setattr__(name, value)


                class IngressStats(Entity):
                    """
                    ingress stats
                    
                    .. attribute:: stats
                    
                    	Statistics
                    	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats, self).__init__()

                        self.yang_name = "ingress-stats"
                        self.yang_parent_name = "label-switched-path"

                        self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats()
                        self.stats.parent = self
                        self._children_name_map["stats"] = "stats"
                        self._children_yang_names.add("stats")


                    class Stats(Entity):
                        """
                        Statistics
                        
                        .. attribute:: bytes
                        
                        	stats for byte count
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_bytes
                        
                        	stats for dropped\-bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_packets
                        
                        	stats for dropped\-packets
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packets
                        
                        	stats for packet count
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats, self).__init__()

                            self.yang_name = "stats"
                            self.yang_parent_name = "ingress-stats"

                            self.bytes = YLeaf(YType.uint64, "bytes")

                            self.dropped_bytes = YLeaf(YType.uint64, "dropped-bytes")

                            self.dropped_packets = YLeaf(YType.uint64, "dropped-packets")

                            self.packets = YLeaf(YType.uint64, "packets")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bytes",
                                            "dropped_bytes",
                                            "dropped_packets",
                                            "packets") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.bytes.is_set or
                                self.dropped_bytes.is_set or
                                self.dropped_packets.is_set or
                                self.packets.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bytes.yfilter != YFilter.not_set or
                                self.dropped_bytes.yfilter != YFilter.not_set or
                                self.dropped_packets.yfilter != YFilter.not_set or
                                self.packets.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bytes.get_name_leafdata())
                            if (self.dropped_bytes.is_set or self.dropped_bytes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_bytes.get_name_leafdata())
                            if (self.dropped_packets.is_set or self.dropped_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_packets.get_name_leafdata())
                            if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bytes" or name == "dropped-bytes" or name == "dropped-packets" or name == "packets"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bytes"):
                                self.bytes = value
                                self.bytes.value_namespace = name_space
                                self.bytes.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-bytes"):
                                self.dropped_bytes = value
                                self.dropped_bytes.value_namespace = name_space
                                self.dropped_bytes.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-packets"):
                                self.dropped_packets = value
                                self.dropped_packets.value_namespace = name_space
                                self.dropped_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets"):
                                self.packets = value
                                self.packets.value_namespace = name_space
                                self.packets.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.stats is not None and self.stats.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.stats is not None and self.stats.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ingress-stats" + path_buffer

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

                        if (child_yang_name == "stats"):
                            if (self.stats is None):
                                self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats()
                                self.stats.parent = self
                                self._children_name_map["stats"] = "stats"
                            return self.stats

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "stats"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class EgressStats(Entity):
                    """
                    egress stats
                    
                    .. attribute:: stats
                    
                    	Statistics
                    	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats, self).__init__()

                        self.yang_name = "egress-stats"
                        self.yang_parent_name = "label-switched-path"

                        self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats()
                        self.stats.parent = self
                        self._children_name_map["stats"] = "stats"
                        self._children_yang_names.add("stats")


                    class Stats(Entity):
                        """
                        Statistics
                        
                        .. attribute:: bytes
                        
                        	stats for byte count
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_bytes
                        
                        	stats for dropped\-bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_packets
                        
                        	stats for dropped\-packets
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packets
                        
                        	stats for packet count
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats, self).__init__()

                            self.yang_name = "stats"
                            self.yang_parent_name = "egress-stats"

                            self.bytes = YLeaf(YType.uint64, "bytes")

                            self.dropped_bytes = YLeaf(YType.uint64, "dropped-bytes")

                            self.dropped_packets = YLeaf(YType.uint64, "dropped-packets")

                            self.packets = YLeaf(YType.uint64, "packets")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bytes",
                                            "dropped_bytes",
                                            "dropped_packets",
                                            "packets") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.bytes.is_set or
                                self.dropped_bytes.is_set or
                                self.dropped_packets.is_set or
                                self.packets.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bytes.yfilter != YFilter.not_set or
                                self.dropped_bytes.yfilter != YFilter.not_set or
                                self.dropped_packets.yfilter != YFilter.not_set or
                                self.packets.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bytes.get_name_leafdata())
                            if (self.dropped_bytes.is_set or self.dropped_bytes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_bytes.get_name_leafdata())
                            if (self.dropped_packets.is_set or self.dropped_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_packets.get_name_leafdata())
                            if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bytes" or name == "dropped-bytes" or name == "dropped-packets" or name == "packets"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bytes"):
                                self.bytes = value
                                self.bytes.value_namespace = name_space
                                self.bytes.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-bytes"):
                                self.dropped_bytes = value
                                self.dropped_bytes.value_namespace = name_space
                                self.dropped_bytes.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-packets"):
                                self.dropped_packets = value
                                self.dropped_packets.value_namespace = name_space
                                self.dropped_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets"):
                                self.packets = value
                                self.packets.value_namespace = name_space
                                self.packets.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.stats is not None and self.stats.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.stats is not None and self.stats.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "egress-stats" + path_buffer

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

                        if (child_yang_name == "stats"):
                            if (self.stats is None):
                                self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats()
                                self.stats.parent = self
                                self._children_name_map["stats"] = "stats"
                            return self.stats

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "stats"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Path(Entity):
                    """
                    Fowarding path
                    
                    .. attribute:: auto_protect
                    
                    	Enables automatic protection if true
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: next_hop
                    
                    	next\-hops list
                    	**type**\: list of    :py:class:`NextHop <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop>`
                    
                    .. attribute:: operations
                    
                    	The incoming label processing
                    	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations>`
                    
                    

                    """

                    _prefix = 'ms'
                    _revision = '2015-07-22'

                    def __init__(self):
                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path, self).__init__()

                        self.yang_name = "path"
                        self.yang_parent_name = "label-switched-path"

                        self.auto_protect = YLeaf(YType.boolean, "auto-protect")

                        self.operations = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations()
                        self.operations.parent = self
                        self._children_name_map["operations"] = "operations"
                        self._children_yang_names.add("operations")

                        self.next_hop = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("auto_protect") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path, self).__setattr__(name, value)


                    class Operations(Entity):
                        """
                        The incoming label processing
                        
                        .. attribute:: pop_and_forward
                        
                        	Pop the incoming label and forward
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: preserve
                        
                        	preserve incoming label stack
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: push
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push>`
                        
                        .. attribute:: swap
                        
                        	Push outgoing label stack
                        	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap>`
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations, self).__init__()

                            self.yang_name = "operations"
                            self.yang_parent_name = "path"

                            self.pop_and_forward = YLeaf(YType.empty, "pop-and-forward")

                            self.preserve = YLeaf(YType.empty, "preserve")

                            self.push = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push()
                            self.push.parent = self
                            self._children_name_map["push"] = "push"
                            self._children_yang_names.add("push")

                            self.swap = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap()
                            self.swap.parent = self
                            self._children_name_map["swap"] = "swap"
                            self._children_yang_names.add("swap")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("pop_and_forward",
                                            "preserve") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations, self).__setattr__(name, value)


                        class Swap(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap, self).__init__()

                                self.yang_name = "swap"
                                self.yang_parent_name = "operations"

                                self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._children_yang_names.add("stack")


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "swap"

                                    self.label_stack = YLeafList(YType.str, "label-stack")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_stack") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack, self).__setattr__(name, value)

                                def has_data(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return False

                                def has_operation(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_stack.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stack" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-stack"):
                                        self.label_stack.append(value)

                            def has_data(self):
                                return (self.stack is not None and self.stack.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.stack is not None and self.stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "swap" + path_buffer

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

                                if (child_yang_name == "stack"):
                                    if (self.stack is None):
                                        self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack()
                                        self.stack.parent = self
                                        self._children_name_map["stack"] = "stack"
                                    return self.stack

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "stack"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Push(Entity):
                            """
                            Push outgoing label stack
                            
                            .. attribute:: stack
                            
                            	The label stack
                            	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push, self).__init__()

                                self.yang_name = "push"
                                self.yang_parent_name = "operations"

                                self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack()
                                self.stack.parent = self
                                self._children_name_map["stack"] = "stack"
                                self._children_yang_names.add("stack")


                            class Stack(Entity):
                                """
                                The label stack
                                
                                .. attribute:: label_stack
                                
                                	First label in the list is the top of the stack
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 16..1048575
                                
                                
                                ----
                                	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                
                                
                                ----
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack, self).__init__()

                                    self.yang_name = "stack"
                                    self.yang_parent_name = "push"

                                    self.label_stack = YLeafList(YType.str, "label-stack")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_stack") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack, self).__setattr__(name, value)

                                def has_data(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return False

                                def has_operation(self):
                                    for leaf in self.label_stack.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_stack.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stack" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-stack"):
                                        self.label_stack.append(value)

                            def has_data(self):
                                return (self.stack is not None and self.stack.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.stack is not None and self.stack.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "push" + path_buffer

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

                                if (child_yang_name == "stack"):
                                    if (self.stack is None):
                                        self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack()
                                        self.stack.parent = self
                                        self._children_name_map["stack"] = "stack"
                                    return self.stack

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "stack"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.pop_and_forward.is_set or
                                self.preserve.is_set or
                                (self.push is not None and self.push.has_data()) or
                                (self.swap is not None and self.swap.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.pop_and_forward.yfilter != YFilter.not_set or
                                self.preserve.yfilter != YFilter.not_set or
                                (self.push is not None and self.push.has_operation()) or
                                (self.swap is not None and self.swap.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "operations" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.pop_and_forward.is_set or self.pop_and_forward.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pop_and_forward.get_name_leafdata())
                            if (self.preserve.is_set or self.preserve.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.preserve.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "push"):
                                if (self.push is None):
                                    self.push = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push()
                                    self.push.parent = self
                                    self._children_name_map["push"] = "push"
                                return self.push

                            if (child_yang_name == "swap"):
                                if (self.swap is None):
                                    self.swap = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap()
                                    self.swap.parent = self
                                    self._children_name_map["swap"] = "swap"
                                return self.swap

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "push" or name == "swap" or name == "pop-and-forward" or name == "preserve"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "pop-and-forward"):
                                self.pop_and_forward = value
                                self.pop_and_forward.value_namespace = name_space
                                self.pop_and_forward.value_namespace_prefix = name_space_prefix
                            if(value_path == "preserve"):
                                self.preserve = value
                                self.preserve.value_namespace = name_space
                                self.preserve.value_namespace_prefix = name_space_prefix


                    class NextHop(Entity):
                        """
                        next\-hops list
                        
                        .. attribute:: index  <key>
                        
                        	Index of the nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        .. attribute:: next_hop_type
                        
                        	Next\-hop
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType>`
                        
                        .. attribute:: nexthop_stats
                        
                        	lsp stats
                        	**type**\:   :py:class:`NexthopStats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats>`
                        
                        .. attribute:: operations
                        
                        	The incoming label processing
                        	**type**\:   :py:class:`Operations <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations>`
                        
                        .. attribute:: origin
                        
                        	The origin of this nexthop
                        	**type**\:   :py:class:`NexthopResolutionType <ydk.models.cisco_ios_xe.common_mpls_static.NexthopResolutionType>`
                        
                        .. attribute:: protected_by
                        
                        	Index of the nexthop that protects this nexthop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	The forwarding path's hoptype
                        	**type**\:   :py:class:`Hoptype <ydk.models.cisco_ios_xe.common_mpls_static.Hoptype>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ms'
                        _revision = '2015-07-22'

                        def __init__(self):
                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "path"

                            self.index = YLeaf(YType.uint32, "index")

                            self.origin = YLeaf(YType.identityref, "origin")

                            self.protected_by = YLeaf(YType.uint32, "protected-by")

                            self.type = YLeaf(YType.enumeration, "type")

                            self.next_hop_type = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType()
                            self.next_hop_type.parent = self
                            self._children_name_map["next_hop_type"] = "next-hop-type"
                            self._children_yang_names.add("next-hop-type")

                            self.nexthop_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats()
                            self.nexthop_stats.parent = self
                            self._children_name_map["nexthop_stats"] = "nexthop-stats"
                            self._children_yang_names.add("nexthop-stats")

                            self.operations = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations()
                            self.operations.parent = self
                            self._children_name_map["operations"] = "operations"
                            self._children_yang_names.add("operations")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("index",
                                            "origin",
                                            "protected_by",
                                            "type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop, self).__setattr__(name, value)


                        class NextHopType(Entity):
                            """
                            Next\-hop
                            
                            .. attribute:: if_index
                            
                            	The interface index
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: mac_address
                            
                            	MAC address of the nexthop
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            	**mandatory**\: True
                            
                            .. attribute:: out_interface_name
                            
                            	Name of the outgoing interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType, self).__init__()

                                self.yang_name = "next-hop-type"
                                self.yang_parent_name = "next-hop"

                                self.if_index = YLeaf(YType.uint32, "if-index")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                self.mac_address = YLeaf(YType.str, "mac-address")

                                self.out_interface_name = YLeaf(YType.str, "out-interface-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("if_index",
                                                "ipv4_address",
                                                "ipv6_address",
                                                "mac_address",
                                                "out_interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.if_index.is_set or
                                    self.ipv4_address.is_set or
                                    self.ipv6_address.is_set or
                                    self.mac_address.is_set or
                                    self.out_interface_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.if_index.yfilter != YFilter.not_set or
                                    self.ipv4_address.yfilter != YFilter.not_set or
                                    self.ipv6_address.yfilter != YFilter.not_set or
                                    self.mac_address.yfilter != YFilter.not_set or
                                    self.out_interface_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "next-hop-type" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.if_index.get_name_leafdata())
                                if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                                if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mac_address.get_name_leafdata())
                                if (self.out_interface_name.is_set or self.out_interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "if-index" or name == "ipv4-address" or name == "ipv6-address" or name == "mac-address" or name == "out-interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "if-index"):
                                    self.if_index = value
                                    self.if_index.value_namespace = name_space
                                    self.if_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv4-address"):
                                    self.ipv4_address = value
                                    self.ipv4_address.value_namespace = name_space
                                    self.ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv6-address"):
                                    self.ipv6_address = value
                                    self.ipv6_address.value_namespace = name_space
                                    self.ipv6_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "mac-address"):
                                    self.mac_address = value
                                    self.mac_address.value_namespace = name_space
                                    self.mac_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-interface-name"):
                                    self.out_interface_name = value
                                    self.out_interface_name.value_namespace = name_space
                                    self.out_interface_name.value_namespace_prefix = name_space_prefix


                        class Operations(Entity):
                            """
                            The incoming label processing
                            
                            .. attribute:: pop_and_forward
                            
                            	Pop the incoming label and forward
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: preserve
                            
                            	preserve incoming label stack
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: push
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Push <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push>`
                            
                            .. attribute:: swap
                            
                            	Push outgoing label stack
                            	**type**\:   :py:class:`Swap <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations, self).__init__()

                                self.yang_name = "operations"
                                self.yang_parent_name = "next-hop"

                                self.pop_and_forward = YLeaf(YType.empty, "pop-and-forward")

                                self.preserve = YLeaf(YType.empty, "preserve")

                                self.push = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push()
                                self.push.parent = self
                                self._children_name_map["push"] = "push"
                                self._children_yang_names.add("push")

                                self.swap = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap()
                                self.swap.parent = self
                                self._children_name_map["swap"] = "swap"
                                self._children_yang_names.add("swap")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("pop_and_forward",
                                                "preserve") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations, self).__setattr__(name, value)


                            class Swap(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap, self).__init__()

                                    self.yang_name = "swap"
                                    self.yang_parent_name = "operations"

                                    self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._children_yang_names.add("stack")


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "swap"

                                        self.label_stack = YLeafList(YType.str, "label-stack")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("label_stack") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.label_stack.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "stack" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "label-stack"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "label-stack"):
                                            self.label_stack.append(value)

                                def has_data(self):
                                    return (self.stack is not None and self.stack.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.stack is not None and self.stack.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "swap" + path_buffer

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

                                    if (child_yang_name == "stack"):
                                        if (self.stack is None):
                                            self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack()
                                            self.stack.parent = self
                                            self._children_name_map["stack"] = "stack"
                                        return self.stack

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Push(Entity):
                                """
                                Push outgoing label stack
                                
                                .. attribute:: stack
                                
                                	The label stack
                                	**type**\:   :py:class:`Stack <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack>`
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push, self).__init__()

                                    self.yang_name = "push"
                                    self.yang_parent_name = "operations"

                                    self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack()
                                    self.stack.parent = self
                                    self._children_name_map["stack"] = "stack"
                                    self._children_yang_names.add("stack")


                                class Stack(Entity):
                                    """
                                    The label stack
                                    
                                    .. attribute:: label_stack
                                    
                                    	First label in the list is the top of the stack
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of int
                                    
                                    	**range:** 16..1048575
                                    
                                    
                                    ----
                                    	**type**\:  list of   :py:class:`IetfMplsLabel <ydk.models.cisco_ios_xe.common_mpls_types.IetfMplsLabel>`
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ms'
                                    _revision = '2015-07-22'

                                    def __init__(self):
                                        super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack, self).__init__()

                                        self.yang_name = "stack"
                                        self.yang_parent_name = "push"

                                        self.label_stack = YLeafList(YType.str, "label-stack")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("label_stack") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.label_stack.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.label_stack.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "stack" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.label_stack.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "label-stack"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "label-stack"):
                                            self.label_stack.append(value)

                                def has_data(self):
                                    return (self.stack is not None and self.stack.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.stack is not None and self.stack.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "push" + path_buffer

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

                                    if (child_yang_name == "stack"):
                                        if (self.stack is None):
                                            self.stack = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack()
                                            self.stack.parent = self
                                            self._children_name_map["stack"] = "stack"
                                        return self.stack

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "stack"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.pop_and_forward.is_set or
                                    self.preserve.is_set or
                                    (self.push is not None and self.push.has_data()) or
                                    (self.swap is not None and self.swap.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.pop_and_forward.yfilter != YFilter.not_set or
                                    self.preserve.yfilter != YFilter.not_set or
                                    (self.push is not None and self.push.has_operation()) or
                                    (self.swap is not None and self.swap.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "operations" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.pop_and_forward.is_set or self.pop_and_forward.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pop_and_forward.get_name_leafdata())
                                if (self.preserve.is_set or self.preserve.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.preserve.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "push"):
                                    if (self.push is None):
                                        self.push = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push()
                                        self.push.parent = self
                                        self._children_name_map["push"] = "push"
                                    return self.push

                                if (child_yang_name == "swap"):
                                    if (self.swap is None):
                                        self.swap = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap()
                                        self.swap.parent = self
                                        self._children_name_map["swap"] = "swap"
                                    return self.swap

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "push" or name == "swap" or name == "pop-and-forward" or name == "preserve"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "pop-and-forward"):
                                    self.pop_and_forward = value
                                    self.pop_and_forward.value_namespace = name_space
                                    self.pop_and_forward.value_namespace_prefix = name_space_prefix
                                if(value_path == "preserve"):
                                    self.preserve = value
                                    self.preserve.value_namespace = name_space
                                    self.preserve.value_namespace_prefix = name_space_prefix


                        class NexthopStats(Entity):
                            """
                            lsp stats
                            
                            .. attribute:: stats
                            
                            	Statistics
                            	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xe.common_mpls_static.MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats>`
                            
                            

                            """

                            _prefix = 'ms'
                            _revision = '2015-07-22'

                            def __init__(self):
                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats, self).__init__()

                                self.yang_name = "nexthop-stats"
                                self.yang_parent_name = "next-hop"

                                self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats()
                                self.stats.parent = self
                                self._children_name_map["stats"] = "stats"
                                self._children_yang_names.add("stats")


                            class Stats(Entity):
                                """
                                Statistics
                                
                                .. attribute:: bytes
                                
                                	stats for byte count
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_bytes
                                
                                	stats for dropped\-bytes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: dropped_packets
                                
                                	stats for dropped\-packets
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: packets
                                
                                	stats for packet count
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ms'
                                _revision = '2015-07-22'

                                def __init__(self):
                                    super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats, self).__init__()

                                    self.yang_name = "stats"
                                    self.yang_parent_name = "nexthop-stats"

                                    self.bytes = YLeaf(YType.uint64, "bytes")

                                    self.dropped_bytes = YLeaf(YType.uint64, "dropped-bytes")

                                    self.dropped_packets = YLeaf(YType.uint64, "dropped-packets")

                                    self.packets = YLeaf(YType.uint64, "packets")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("bytes",
                                                    "dropped_bytes",
                                                    "dropped_packets",
                                                    "packets") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.bytes.is_set or
                                        self.dropped_bytes.is_set or
                                        self.dropped_packets.is_set or
                                        self.packets.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.bytes.yfilter != YFilter.not_set or
                                        self.dropped_bytes.yfilter != YFilter.not_set or
                                        self.dropped_packets.yfilter != YFilter.not_set or
                                        self.packets.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "stats" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.bytes.get_name_leafdata())
                                    if (self.dropped_bytes.is_set or self.dropped_bytes.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dropped_bytes.get_name_leafdata())
                                    if (self.dropped_packets.is_set or self.dropped_packets.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dropped_packets.get_name_leafdata())
                                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.packets.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "bytes" or name == "dropped-bytes" or name == "dropped-packets" or name == "packets"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "bytes"):
                                        self.bytes = value
                                        self.bytes.value_namespace = name_space
                                        self.bytes.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dropped-bytes"):
                                        self.dropped_bytes = value
                                        self.dropped_bytes.value_namespace = name_space
                                        self.dropped_bytes.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dropped-packets"):
                                        self.dropped_packets = value
                                        self.dropped_packets.value_namespace = name_space
                                        self.dropped_packets.value_namespace_prefix = name_space_prefix
                                    if(value_path == "packets"):
                                        self.packets = value
                                        self.packets.value_namespace = name_space
                                        self.packets.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (self.stats is not None and self.stats.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.stats is not None and self.stats.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "nexthop-stats" + path_buffer

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

                                if (child_yang_name == "stats"):
                                    if (self.stats is None):
                                        self.stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats()
                                        self.stats.parent = self
                                        self._children_name_map["stats"] = "stats"
                                    return self.stats

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "stats"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.index.is_set or
                                self.origin.is_set or
                                self.protected_by.is_set or
                                self.type.is_set or
                                (self.next_hop_type is not None and self.next_hop_type.has_data()) or
                                (self.nexthop_stats is not None and self.nexthop_stats.has_data()) or
                                (self.operations is not None and self.operations.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.origin.yfilter != YFilter.not_set or
                                self.protected_by.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set or
                                (self.next_hop_type is not None and self.next_hop_type.has_operation()) or
                                (self.nexthop_stats is not None and self.nexthop_stats.has_operation()) or
                                (self.operations is not None and self.operations.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "next-hop" + "[index='" + self.index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.origin.get_name_leafdata())
                            if (self.protected_by.is_set or self.protected_by.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protected_by.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "next-hop-type"):
                                if (self.next_hop_type is None):
                                    self.next_hop_type = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType()
                                    self.next_hop_type.parent = self
                                    self._children_name_map["next_hop_type"] = "next-hop-type"
                                return self.next_hop_type

                            if (child_yang_name == "nexthop-stats"):
                                if (self.nexthop_stats is None):
                                    self.nexthop_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats()
                                    self.nexthop_stats.parent = self
                                    self._children_name_map["nexthop_stats"] = "nexthop-stats"
                                return self.nexthop_stats

                            if (child_yang_name == "operations"):
                                if (self.operations is None):
                                    self.operations = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations()
                                    self.operations.parent = self
                                    self._children_name_map["operations"] = "operations"
                                return self.operations

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "next-hop-type" or name == "nexthop-stats" or name == "operations" or name == "index" or name == "origin" or name == "protected-by" or name == "type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "origin"):
                                self.origin = value
                                self.origin.value_namespace = name_space
                                self.origin.value_namespace_prefix = name_space_prefix
                            if(value_path == "protected-by"):
                                self.protected_by = value
                                self.protected_by.value_namespace = name_space
                                self.protected_by.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.next_hop:
                            if (c.has_data()):
                                return True
                        return (
                            self.auto_protect.is_set or
                            (self.operations is not None and self.operations.has_data()))

                    def has_operation(self):
                        for c in self.next_hop:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.auto_protect.yfilter != YFilter.not_set or
                            (self.operations is not None and self.operations.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "path" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.auto_protect.is_set or self.auto_protect.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.auto_protect.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "next-hop"):
                            for c in self.next_hop:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.next_hop.append(c)
                            return c

                        if (child_yang_name == "operations"):
                            if (self.operations is None):
                                self.operations = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations()
                                self.operations.parent = self
                                self._children_name_map["operations"] = "operations"
                            return self.operations

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "operations" or name == "auto-protect"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "auto-protect"):
                            self.auto_protect = value
                            self.auto_protect.value_namespace = name_space
                            self.auto_protect.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.vrf_name.is_set or
                        self.prefix.is_set or
                        self.in_label_value.is_set or
                        self.name.is_set or
                        (self.egress_stats is not None and self.egress_stats.has_data()) or
                        (self.ingress_stats is not None and self.ingress_stats.has_data()) or
                        (self.path is not None and self.path.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        self.prefix.yfilter != YFilter.not_set or
                        self.in_label_value.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.egress_stats is not None and self.egress_stats.has_operation()) or
                        (self.ingress_stats is not None and self.ingress_stats.has_operation()) or
                        (self.path is not None and self.path.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "label-switched-path" + "[vrf-name='" + self.vrf_name.get() + "']" + "[prefix='" + self.prefix.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "common-mpls-static:mpls-static/mpls-static-state/label-switched-paths/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())
                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix.get_name_leafdata())
                    if (self.in_label_value.is_set or self.in_label_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_label_value.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "egress-stats"):
                        if (self.egress_stats is None):
                            self.egress_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats()
                            self.egress_stats.parent = self
                            self._children_name_map["egress_stats"] = "egress-stats"
                        return self.egress_stats

                    if (child_yang_name == "ingress-stats"):
                        if (self.ingress_stats is None):
                            self.ingress_stats = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats()
                            self.ingress_stats.parent = self
                            self._children_name_map["ingress_stats"] = "ingress-stats"
                        return self.ingress_stats

                    if (child_yang_name == "path"):
                        if (self.path is None):
                            self.path = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path()
                            self.path.parent = self
                            self._children_name_map["path"] = "path"
                        return self.path

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "egress-stats" or name == "ingress-stats" or name == "path" or name == "vrf-name" or name == "prefix" or name == "in-label-value" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix"):
                        self.prefix = value
                        self.prefix.value_namespace = name_space
                        self.prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-label-value"):
                        self.in_label_value = value
                        self.in_label_value.value_namespace = name_space
                        self.in_label_value.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.label_switched_path:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.label_switched_path:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "label-switched-paths" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "common-mpls-static:mpls-static/mpls-static-state/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "label-switched-path"):
                    for c in self.label_switched_path:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.label_switched_path.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "label-switched-path"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.label_switched_paths is not None and self.label_switched_paths.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.label_switched_paths is not None and self.label_switched_paths.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mpls-static-state" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "common-mpls-static:mpls-static/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "label-switched-paths"):
                if (self.label_switched_paths is None):
                    self.label_switched_paths = MplsStatic.MplsStaticState.LabelSwitchedPaths()
                    self.label_switched_paths.parent = self
                    self._children_name_map["label_switched_paths"] = "label-switched-paths"
                return self.label_switched_paths

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "label-switched-paths"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.mpls_static_cfg is not None and self.mpls_static_cfg.has_data()) or
            (self.mpls_static_state is not None and self.mpls_static_state.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.mpls_static_cfg is not None and self.mpls_static_cfg.has_operation()) or
            (self.mpls_static_state is not None and self.mpls_static_state.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "common-mpls-static:mpls-static" + path_buffer

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

        if (child_yang_name == "mpls-static-cfg"):
            if (self.mpls_static_cfg is None):
                self.mpls_static_cfg = MplsStatic.MplsStaticCfg()
                self.mpls_static_cfg.parent = self
                self._children_name_map["mpls_static_cfg"] = "mpls-static-cfg"
            return self.mpls_static_cfg

        if (child_yang_name == "mpls-static-state"):
            if (self.mpls_static_state is None):
                self.mpls_static_state = MplsStatic.MplsStaticState()
                self.mpls_static_state.parent = self
                self._children_name_map["mpls_static_state"] = "mpls-static-state"
            return self.mpls_static_state

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mpls-static-cfg" or name == "mpls-static-state"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MplsStatic()
        return self._top_entity

class LspIpv4(Identity):
    """
    The LSP is for an IPv4 prefix
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(LspIpv4, self).__init__("urn:ietf:params:xml:ns:yang:common-mpls-static", "common-mpls-static", "common-mpls-static:lsp-IPv4")


class LspVrf(Identity):
    """
    The LSP is per VRF
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(LspVrf, self).__init__("urn:ietf:params:xml:ns:yang:common-mpls-static", "common-mpls-static", "common-mpls-static:lsp-vrf")


class StaticNexthop(Identity):
    """
    The nexthop resolved from statically configured route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(StaticNexthop, self).__init__("urn:ietf:params:xml:ns:yang:common-mpls-static", "common-mpls-static", "common-mpls-static:static-nexthop")


class LspIpv6(Identity):
    """
    The LSP is for an IPv6 prefix
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(LspIpv6, self).__init__("urn:ietf:params:xml:ns:yang:common-mpls-static", "common-mpls-static", "common-mpls-static:lsp-IPv6")


class Lsp(Identity):
    """
    The LSP is cross\-connect
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(Lsp, self).__init__("urn:ietf:params:xml:ns:yang:common-mpls-static", "common-mpls-static", "common-mpls-static:lsp")


class OspfRouteNexthop(Identity):
    """
    The nexthop resolved from an OSPF route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(OspfRouteNexthop, self).__init__("urn:ietf:params:xml:ns:yang:common-mpls-static", "common-mpls-static", "common-mpls-static:ospf-route-nexthop")


class BgpRouteNexthop(Identity):
    """
    The nexthop resolved from a BGP route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(BgpRouteNexthop, self).__init__("urn:ietf:params:xml:ns:yang:common-mpls-static", "common-mpls-static", "common-mpls-static:bgp-route-nexthop")


class IsisRouteNexthop(Identity):
    """
    The nexthop resolved from an ISIS route
    
    

    """

    _prefix = 'ms'
    _revision = '2015-07-22'

    def __init__(self):
        super(IsisRouteNexthop, self).__init__("urn:ietf:params:xml:ns:yang:common-mpls-static", "common-mpls-static", "common-mpls-static:isis-route-nexthop")


