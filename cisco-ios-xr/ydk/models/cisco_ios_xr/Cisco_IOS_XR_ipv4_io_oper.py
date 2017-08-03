""" Cisco_IOS_XR_ipv4_io_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-io package operational data.

This module contains definitions
for the following management objects\:
  ipv4\-network\: IPv4 network operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ipv4MaOperLineState(Enum):
    """
    Ipv4MaOperLineState

    Interface line states

    .. data:: unknown = 0

    	Interface state is unknown

    .. data:: shutdown = 1

    	Interface has been shutdown

    .. data:: down = 2

    	Interface state is down

    .. data:: up = 3

    	Interface state is up

    """

    unknown = Enum.YLeaf(0, "unknown")

    shutdown = Enum.YLeaf(1, "shutdown")

    down = Enum.YLeaf(2, "down")

    up = Enum.YLeaf(3, "up")


class RpfMode(Enum):
    """
    RpfMode

    Interface line states

    .. data:: strict = 0

    	Strict RPF

    .. data:: loose = 1

    	Loose RPF

    """

    strict = Enum.YLeaf(0, "strict")

    loose = Enum.YLeaf(1, "loose")



class Ipv4Network(Entity):
    """
    IPv4 network operational data
    
    .. attribute:: interfaces
    
    	IPv4 network operational interface data
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces>`
    
    .. attribute:: nodes
    
    	Node\-specific IPv4 network operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes>`
    
    

    """

    _prefix = 'ipv4-io-oper'
    _revision = '2015-10-20'

    def __init__(self):
        super(Ipv4Network, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-network"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-io-oper"

        self.interfaces = Ipv4Network.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.nodes = Ipv4Network.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Node\-specific IPv4 network operational data
        
        .. attribute:: node
        
        	IPv4 network operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node>`
        
        

        """

        _prefix = 'ipv4-io-oper'
        _revision = '2015-10-20'

        def __init__(self):
            super(Ipv4Network.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ipv4-network"

            self.node = YList(self)

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
                        super(Ipv4Network.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Network.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            IPv4 network operational data for a particular
            node
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_data
            
            	IPv4 network operational interface data
            	**type**\:   :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData>`
            
            .. attribute:: statistics
            
            	Statistical IPv4 network operational data for a node
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ipv4-io-oper'
            _revision = '2015-10-20'

            def __init__(self):
                super(Ipv4Network.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.interface_data = Ipv4Network.Nodes.Node.InterfaceData()
                self.interface_data.parent = self
                self._children_name_map["interface_data"] = "interface-data"
                self._children_yang_names.add("interface-data")

                self.statistics = Ipv4Network.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv4Network.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4Network.Nodes.Node, self).__setattr__(name, value)


            class InterfaceData(Entity):
                """
                IPv4 network operational interface data
                
                .. attribute:: summary
                
                	Summary of IPv4 network operational interface data on a node
                	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary>`
                
                .. attribute:: vrfs
                
                	VRF specific IPv4 network operational interface data
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs>`
                
                

                """

                _prefix = 'ipv4-io-oper'
                _revision = '2015-10-20'

                def __init__(self):
                    super(Ipv4Network.Nodes.Node.InterfaceData, self).__init__()

                    self.yang_name = "interface-data"
                    self.yang_parent_name = "node"

                    self.summary = Ipv4Network.Nodes.Node.InterfaceData.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"
                    self._children_yang_names.add("summary")

                    self.vrfs = Ipv4Network.Nodes.Node.InterfaceData.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                    self._children_yang_names.add("vrfs")


                class Vrfs(Entity):
                    """
                    VRF specific IPv4 network operational
                    interface data
                    
                    .. attribute:: vrf
                    
                    	VRF name of an interface belong to
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv4-io-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "interface-data"

                        self.vrf = YList(self)

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
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs, self).__setattr__(name, value)


                    class Vrf(Entity):
                        """
                        VRF name of an interface belong to
                        
                        .. attribute:: vrf_name  <key>
                        
                        	The VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: briefs
                        
                        	Brief interface IPv4 network operational data for a node
                        	**type**\:   :py:class:`Briefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs>`
                        
                        .. attribute:: details
                        
                        	Detail interface IPv4 network operational data for a node
                        	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details>`
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.briefs = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs()
                            self.briefs.parent = self
                            self._children_name_map["briefs"] = "briefs"
                            self._children_yang_names.add("briefs")

                            self.details = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details()
                            self.details.parent = self
                            self._children_name_map["details"] = "details"
                            self._children_yang_names.add("details")

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
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf, self).__setattr__(name, value)


                        class Briefs(Entity):
                            """
                            Brief interface IPv4 network operational
                            data for a node
                            
                            .. attribute:: brief
                            
                            	Brief interface IPv4 network operational data for an interface
                            	**type**\: list of    :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief>`
                            
                            

                            """

                            _prefix = 'ipv4-io-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, self).__init__()

                                self.yang_name = "briefs"
                                self.yang_parent_name = "vrf"

                                self.brief = YList(self)

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
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs, self).__setattr__(name, value)


                            class Brief(Entity):
                                """
                                Brief interface IPv4 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: line_state
                                
                                	Line state of the interface
                                	**type**\:   :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4MaOperLineState>`
                                
                                .. attribute:: primary_address
                                
                                	Primary address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_id
                                
                                	VRF ID of the interface
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ipv4-io-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, self).__init__()

                                    self.yang_name = "brief"
                                    self.yang_parent_name = "briefs"

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.line_state = YLeaf(YType.enumeration, "line-state")

                                    self.primary_address = YLeaf(YType.str, "primary-address")

                                    self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("interface_name",
                                                    "line_state",
                                                    "primary_address",
                                                    "vrf_id") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.interface_name.is_set or
                                        self.line_state.is_set or
                                        self.primary_address.is_set or
                                        self.vrf_id.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.line_state.yfilter != YFilter.not_set or
                                        self.primary_address.yfilter != YFilter.not_set or
                                        self.vrf_id.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "brief" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                                    if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.line_state.get_name_leafdata())
                                    if (self.primary_address.is_set or self.primary_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.primary_address.get_name_leafdata())
                                    if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vrf_id.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "interface-name" or name == "line-state" or name == "primary-address" or name == "vrf-id"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "line-state"):
                                        self.line_state = value
                                        self.line_state.value_namespace = name_space
                                        self.line_state.value_namespace_prefix = name_space_prefix
                                    if(value_path == "primary-address"):
                                        self.primary_address = value
                                        self.primary_address.value_namespace = name_space
                                        self.primary_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vrf-id"):
                                        self.vrf_id = value
                                        self.vrf_id.value_namespace = name_space
                                        self.vrf_id.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.brief:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.brief:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "briefs" + path_buffer

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

                                if (child_yang_name == "brief"):
                                    for c in self.brief:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.brief.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "brief"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Details(Entity):
                            """
                            Detail interface IPv4 network operational
                            data for a node
                            
                            .. attribute:: detail
                            
                            	Detail interface IPv4 network operational data for an interface
                            	**type**\: list of    :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail>`
                            
                            

                            """

                            _prefix = 'ipv4-io-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, self).__init__()

                                self.yang_name = "details"
                                self.yang_parent_name = "vrf"

                                self.detail = YList(self)

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
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details, self).__setattr__(name, value)


                            class Detail(Entity):
                                """
                                Detail interface IPv4 network operational
                                data for an interface
                                
                                .. attribute:: interface_name  <key>
                                
                                	The name of the interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: acl
                                
                                	ACLs configured on the interface
                                	**type**\:   :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl>`
                                
                                .. attribute:: bgp_pa
                                
                                	BGP PA config on the interface
                                	**type**\:   :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa>`
                                
                                .. attribute:: caps_utime
                                
                                	CAPS Add Time
                                	**type**\:   :py:class:`CapsUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime>`
                                
                                .. attribute:: direct_broadcast
                                
                                	Are direct broadcasts sent on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: flow_tag_dst
                                
                                	Is BGP Flow Tag Destination is enable
                                	**type**\:  bool
                                
                                .. attribute:: flow_tag_src
                                
                                	Is BGP Flow Tag Source is enable
                                	**type**\:  bool
                                
                                .. attribute:: fwd_dis_utime
                                
                                	FWD DISABLE Time
                                	**type**\:   :py:class:`FwdDisUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime>`
                                
                                .. attribute:: fwd_en_utime
                                
                                	FWD ENABLE Time
                                	**type**\:   :py:class:`FwdEnUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime>`
                                
                                .. attribute:: helper_address
                                
                                	Helper Addresses configured on the interface
                                	**type**\:   :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress>`
                                
                                .. attribute:: idb_utime
                                
                                	IDB Create Time
                                	**type**\:   :py:class:`IdbUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime>`
                                
                                .. attribute:: line_state
                                
                                	Line state of the interface
                                	**type**\:   :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4MaOperLineState>`
                                
                                .. attribute:: mask_reply
                                
                                	Are mask replies sent on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: mlacp_active
                                
                                	Is mLACP state Active (valid if RG ID exists)
                                	**type**\:  bool
                                
                                .. attribute:: mtu
                                
                                	IP MTU of the interface
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: multi_acl
                                
                                	Multi ACLs configured on the interface
                                	**type**\:   :py:class:`MultiAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl>`
                                
                                .. attribute:: multicast_group
                                
                                	Multicast groups joined on the interface
                                	**type**\: list of    :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup>`
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length of primary address
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: primary_address
                                
                                	Primary address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: proxy_arp_disabled
                                
                                	Is Proxy ARP disabled on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: pub_utime
                                
                                	Address Publish Time
                                	**type**\:   :py:class:`PubUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime>`
                                
                                .. attribute:: redirect
                                
                                	Are ICMP redirects sent on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: rg_id_exists
                                
                                	Does ICCP RG ID exist on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: route_tag
                                
                                	Route tag associated with the primary address (0 = no tag)
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rpf
                                
                                	RPF config on the interface
                                	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf>`
                                
                                .. attribute:: secondary_address
                                
                                	Secondary addresses on the interface
                                	**type**\: list of    :py:class:`SecondaryAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress>`
                                
                                .. attribute:: unnumbered_interface_name
                                
                                	Name of referenced interface (valid if unnumbered)
                                	**type**\:  str
                                
                                .. attribute:: unreachable
                                
                                	Are ICMP unreachables sent on the interface?
                                	**type**\:  bool
                                
                                .. attribute:: vrf_id
                                
                                	VRF ID of the interface
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ipv4-io-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "details"

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.direct_broadcast = YLeaf(YType.boolean, "direct-broadcast")

                                    self.flow_tag_dst = YLeaf(YType.boolean, "flow-tag-dst")

                                    self.flow_tag_src = YLeaf(YType.boolean, "flow-tag-src")

                                    self.line_state = YLeaf(YType.enumeration, "line-state")

                                    self.mask_reply = YLeaf(YType.boolean, "mask-reply")

                                    self.mlacp_active = YLeaf(YType.boolean, "mlacp-active")

                                    self.mtu = YLeaf(YType.uint32, "mtu")

                                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                    self.primary_address = YLeaf(YType.str, "primary-address")

                                    self.proxy_arp_disabled = YLeaf(YType.boolean, "proxy-arp-disabled")

                                    self.redirect = YLeaf(YType.boolean, "redirect")

                                    self.rg_id_exists = YLeaf(YType.boolean, "rg-id-exists")

                                    self.route_tag = YLeaf(YType.uint32, "route-tag")

                                    self.unnumbered_interface_name = YLeaf(YType.str, "unnumbered-interface-name")

                                    self.unreachable = YLeaf(YType.boolean, "unreachable")

                                    self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                                    self.acl = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl()
                                    self.acl.parent = self
                                    self._children_name_map["acl"] = "acl"
                                    self._children_yang_names.add("acl")

                                    self.bgp_pa = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa()
                                    self.bgp_pa.parent = self
                                    self._children_name_map["bgp_pa"] = "bgp-pa"
                                    self._children_yang_names.add("bgp-pa")

                                    self.caps_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime()
                                    self.caps_utime.parent = self
                                    self._children_name_map["caps_utime"] = "caps-utime"
                                    self._children_yang_names.add("caps-utime")

                                    self.fwd_dis_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime()
                                    self.fwd_dis_utime.parent = self
                                    self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"
                                    self._children_yang_names.add("fwd-dis-utime")

                                    self.fwd_en_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime()
                                    self.fwd_en_utime.parent = self
                                    self._children_name_map["fwd_en_utime"] = "fwd-en-utime"
                                    self._children_yang_names.add("fwd-en-utime")

                                    self.helper_address = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress()
                                    self.helper_address.parent = self
                                    self._children_name_map["helper_address"] = "helper-address"
                                    self._children_yang_names.add("helper-address")

                                    self.idb_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime()
                                    self.idb_utime.parent = self
                                    self._children_name_map["idb_utime"] = "idb-utime"
                                    self._children_yang_names.add("idb-utime")

                                    self.multi_acl = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl()
                                    self.multi_acl.parent = self
                                    self._children_name_map["multi_acl"] = "multi-acl"
                                    self._children_yang_names.add("multi-acl")

                                    self.pub_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime()
                                    self.pub_utime.parent = self
                                    self._children_name_map["pub_utime"] = "pub-utime"
                                    self._children_yang_names.add("pub-utime")

                                    self.rpf = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf()
                                    self.rpf.parent = self
                                    self._children_name_map["rpf"] = "rpf"
                                    self._children_yang_names.add("rpf")

                                    self.multicast_group = YList(self)
                                    self.secondary_address = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("interface_name",
                                                    "direct_broadcast",
                                                    "flow_tag_dst",
                                                    "flow_tag_src",
                                                    "line_state",
                                                    "mask_reply",
                                                    "mlacp_active",
                                                    "mtu",
                                                    "prefix_length",
                                                    "primary_address",
                                                    "proxy_arp_disabled",
                                                    "redirect",
                                                    "rg_id_exists",
                                                    "route_tag",
                                                    "unnumbered_interface_name",
                                                    "unreachable",
                                                    "vrf_id") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail, self).__setattr__(name, value)


                                class Acl(Entity):
                                    """
                                    ACLs configured on the interface
                                    
                                    .. attribute:: common_in_bound
                                    
                                    	Common ACL applied to incoming packets
                                    	**type**\:  str
                                    
                                    .. attribute:: common_out_bound
                                    
                                    	Common ACL applied to outgoing packets
                                    	**type**\:  str
                                    
                                    .. attribute:: inbound
                                    
                                    	ACL applied to incoming packets
                                    	**type**\:  str
                                    
                                    .. attribute:: outbound
                                    
                                    	ACL applied to outgoing packets
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl, self).__init__()

                                        self.yang_name = "acl"
                                        self.yang_parent_name = "detail"

                                        self.common_in_bound = YLeaf(YType.str, "common-in-bound")

                                        self.common_out_bound = YLeaf(YType.str, "common-out-bound")

                                        self.inbound = YLeaf(YType.str, "inbound")

                                        self.outbound = YLeaf(YType.str, "outbound")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("common_in_bound",
                                                        "common_out_bound",
                                                        "inbound",
                                                        "outbound") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.common_in_bound.is_set or
                                            self.common_out_bound.is_set or
                                            self.inbound.is_set or
                                            self.outbound.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.common_in_bound.yfilter != YFilter.not_set or
                                            self.common_out_bound.yfilter != YFilter.not_set or
                                            self.inbound.yfilter != YFilter.not_set or
                                            self.outbound.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "acl" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.common_in_bound.is_set or self.common_in_bound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.common_in_bound.get_name_leafdata())
                                        if (self.common_out_bound.is_set or self.common_out_bound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.common_out_bound.get_name_leafdata())
                                        if (self.inbound.is_set or self.inbound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.inbound.get_name_leafdata())
                                        if (self.outbound.is_set or self.outbound.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.outbound.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "common-in-bound" or name == "common-out-bound" or name == "inbound" or name == "outbound"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "common-in-bound"):
                                            self.common_in_bound = value
                                            self.common_in_bound.value_namespace = name_space
                                            self.common_in_bound.value_namespace_prefix = name_space_prefix
                                        if(value_path == "common-out-bound"):
                                            self.common_out_bound = value
                                            self.common_out_bound.value_namespace = name_space
                                            self.common_out_bound.value_namespace_prefix = name_space_prefix
                                        if(value_path == "inbound"):
                                            self.inbound = value
                                            self.inbound.value_namespace = name_space
                                            self.inbound.value_namespace_prefix = name_space_prefix
                                        if(value_path == "outbound"):
                                            self.outbound = value
                                            self.outbound.value_namespace = name_space
                                            self.outbound.value_namespace_prefix = name_space_prefix


                                class MultiAcl(Entity):
                                    """
                                    Multi ACLs configured on the interface
                                    
                                    .. attribute:: common
                                    
                                    	Common ACLs
                                    	**type**\:  list of str
                                    
                                    .. attribute:: inbound
                                    
                                    	Inbound ACLs
                                    	**type**\:  list of str
                                    
                                    .. attribute:: outbound
                                    
                                    	Outbound ACLs
                                    	**type**\:  list of str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl, self).__init__()

                                        self.yang_name = "multi-acl"
                                        self.yang_parent_name = "detail"

                                        self.common = YLeafList(YType.str, "common")

                                        self.inbound = YLeafList(YType.str, "inbound")

                                        self.outbound = YLeafList(YType.str, "outbound")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("common",
                                                        "inbound",
                                                        "outbound") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.common.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        for leaf in self.inbound.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        for leaf in self.outbound.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.common.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        for leaf in self.inbound.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        for leaf in self.outbound.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.common.yfilter != YFilter.not_set or
                                            self.inbound.yfilter != YFilter.not_set or
                                            self.outbound.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "multi-acl" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.common.get_name_leafdata())

                                        leaf_name_data.extend(self.inbound.get_name_leafdata())

                                        leaf_name_data.extend(self.outbound.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "common" or name == "inbound" or name == "outbound"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "common"):
                                            self.common.append(value)
                                        if(value_path == "inbound"):
                                            self.inbound.append(value)
                                        if(value_path == "outbound"):
                                            self.outbound.append(value)


                                class HelperAddress(Entity):
                                    """
                                    Helper Addresses configured on the interface
                                    
                                    .. attribute:: address_array
                                    
                                    	Helper address
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress, self).__init__()

                                        self.yang_name = "helper-address"
                                        self.yang_parent_name = "detail"

                                        self.address_array = YLeafList(YType.str, "address-array")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address_array") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.address_array.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.address_array.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address_array.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "helper-address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.address_array.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address-array"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address-array"):
                                            self.address_array.append(value)


                                class Rpf(Entity):
                                    """
                                    RPF config on the interface
                                    
                                    .. attribute:: allow_default_route
                                    
                                    	Allow Default Route
                                    	**type**\:  bool
                                    
                                    .. attribute:: allow_self_ping
                                    
                                    	Allow Self Ping
                                    	**type**\:  bool
                                    
                                    .. attribute:: enable
                                    
                                    	Enable RPF config
                                    	**type**\:  bool
                                    
                                    .. attribute:: mode
                                    
                                    	RPF Mode (loose/strict)
                                    	**type**\:   :py:class:`RpfMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.RpfMode>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, self).__init__()

                                        self.yang_name = "rpf"
                                        self.yang_parent_name = "detail"

                                        self.allow_default_route = YLeaf(YType.boolean, "allow-default-route")

                                        self.allow_self_ping = YLeaf(YType.boolean, "allow-self-ping")

                                        self.enable = YLeaf(YType.boolean, "enable")

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
                                            if name in ("allow_default_route",
                                                        "allow_self_ping",
                                                        "enable",
                                                        "mode") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.allow_default_route.is_set or
                                            self.allow_self_ping.is_set or
                                            self.enable.is_set or
                                            self.mode.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.allow_default_route.yfilter != YFilter.not_set or
                                            self.allow_self_ping.yfilter != YFilter.not_set or
                                            self.enable.yfilter != YFilter.not_set or
                                            self.mode.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "rpf" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.allow_default_route.is_set or self.allow_default_route.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.allow_default_route.get_name_leafdata())
                                        if (self.allow_self_ping.is_set or self.allow_self_ping.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.allow_self_ping.get_name_leafdata())
                                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.enable.get_name_leafdata())
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
                                        if(name == "allow-default-route" or name == "allow-self-ping" or name == "enable" or name == "mode"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "allow-default-route"):
                                            self.allow_default_route = value
                                            self.allow_default_route.value_namespace = name_space
                                            self.allow_default_route.value_namespace_prefix = name_space_prefix
                                        if(value_path == "allow-self-ping"):
                                            self.allow_self_ping = value
                                            self.allow_self_ping.value_namespace = name_space
                                            self.allow_self_ping.value_namespace_prefix = name_space_prefix
                                        if(value_path == "enable"):
                                            self.enable = value
                                            self.enable.value_namespace = name_space
                                            self.enable.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mode"):
                                            self.mode = value
                                            self.mode.value_namespace = name_space
                                            self.mode.value_namespace_prefix = name_space_prefix


                                class BgpPa(Entity):
                                    """
                                    BGP PA config on the interface
                                    
                                    .. attribute:: input
                                    
                                    	BGP PA input config
                                    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input>`
                                    
                                    .. attribute:: output
                                    
                                    	BGP PA output config
                                    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa, self).__init__()

                                        self.yang_name = "bgp-pa"
                                        self.yang_parent_name = "detail"

                                        self.input = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input()
                                        self.input.parent = self
                                        self._children_name_map["input"] = "input"
                                        self._children_yang_names.add("input")

                                        self.output = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output()
                                        self.output.parent = self
                                        self._children_name_map["output"] = "output"
                                        self._children_yang_names.add("output")


                                    class Input(Entity):
                                        """
                                        BGP PA input config
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\:  bool
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\:  bool
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, self).__init__()

                                            self.yang_name = "input"
                                            self.yang_parent_name = "bgp-pa"

                                            self.destination = YLeaf(YType.boolean, "destination")

                                            self.enable = YLeaf(YType.boolean, "enable")

                                            self.source = YLeaf(YType.boolean, "source")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("destination",
                                                            "enable",
                                                            "source") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.destination.is_set or
                                                self.enable.is_set or
                                                self.source.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.destination.yfilter != YFilter.not_set or
                                                self.enable.yfilter != YFilter.not_set or
                                                self.source.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "input" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.destination.get_name_leafdata())
                                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.enable.get_name_leafdata())
                                            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.source.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "destination" or name == "enable" or name == "source"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "destination"):
                                                self.destination = value
                                                self.destination.value_namespace = name_space
                                                self.destination.value_namespace_prefix = name_space_prefix
                                            if(value_path == "enable"):
                                                self.enable = value
                                                self.enable.value_namespace = name_space
                                                self.enable.value_namespace_prefix = name_space_prefix
                                            if(value_path == "source"):
                                                self.source = value
                                                self.source.value_namespace = name_space
                                                self.source.value_namespace_prefix = name_space_prefix


                                    class Output(Entity):
                                        """
                                        BGP PA output config
                                        
                                        .. attribute:: destination
                                        
                                        	Enable destination accouting
                                        	**type**\:  bool
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP PA for ingress/egress
                                        	**type**\:  bool
                                        
                                        .. attribute:: source
                                        
                                        	Enable source accouting
                                        	**type**\:  bool
                                        
                                        

                                        """

                                        _prefix = 'ipv4-io-oper'
                                        _revision = '2015-10-20'

                                        def __init__(self):
                                            super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, self).__init__()

                                            self.yang_name = "output"
                                            self.yang_parent_name = "bgp-pa"

                                            self.destination = YLeaf(YType.boolean, "destination")

                                            self.enable = YLeaf(YType.boolean, "enable")

                                            self.source = YLeaf(YType.boolean, "source")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("destination",
                                                            "enable",
                                                            "source") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.destination.is_set or
                                                self.enable.is_set or
                                                self.source.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.destination.yfilter != YFilter.not_set or
                                                self.enable.yfilter != YFilter.not_set or
                                                self.source.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "output" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.destination.get_name_leafdata())
                                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.enable.get_name_leafdata())
                                            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.source.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "destination" or name == "enable" or name == "source"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "destination"):
                                                self.destination = value
                                                self.destination.value_namespace = name_space
                                                self.destination.value_namespace_prefix = name_space_prefix
                                            if(value_path == "enable"):
                                                self.enable = value
                                                self.enable.value_namespace = name_space
                                                self.enable.value_namespace_prefix = name_space_prefix
                                            if(value_path == "source"):
                                                self.source = value
                                                self.source.value_namespace = name_space
                                                self.source.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            (self.input is not None and self.input.has_data()) or
                                            (self.output is not None and self.output.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            (self.input is not None and self.input.has_operation()) or
                                            (self.output is not None and self.output.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "bgp-pa" + path_buffer

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

                                        if (child_yang_name == "input"):
                                            if (self.input is None):
                                                self.input = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input()
                                                self.input.parent = self
                                                self._children_name_map["input"] = "input"
                                            return self.input

                                        if (child_yang_name == "output"):
                                            if (self.output is None):
                                                self.output = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output()
                                                self.output.parent = self
                                                self._children_name_map["output"] = "output"
                                            return self.output

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "input" or name == "output"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class PubUtime(Entity):
                                    """
                                    Address Publish Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime, self).__init__()

                                        self.yang_name = "pub-utime"
                                        self.yang_parent_name = "detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "pub-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class IdbUtime(Entity):
                                    """
                                    IDB Create Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime, self).__init__()

                                        self.yang_name = "idb-utime"
                                        self.yang_parent_name = "detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "idb-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class CapsUtime(Entity):
                                    """
                                    CAPS Add Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime, self).__init__()

                                        self.yang_name = "caps-utime"
                                        self.yang_parent_name = "detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "caps-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class FwdEnUtime(Entity):
                                    """
                                    FWD ENABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime, self).__init__()

                                        self.yang_name = "fwd-en-utime"
                                        self.yang_parent_name = "detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "fwd-en-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class FwdDisUtime(Entity):
                                    """
                                    FWD DISABLE Time
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime, self).__init__()

                                        self.yang_name = "fwd-dis-utime"
                                        self.yang_parent_name = "detail"

                                    def has_data(self):
                                        return False

                                    def has_operation(self):
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "fwd-dis-utime" + path_buffer

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

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class MulticastGroup(Entity):
                                    """
                                    Multicast groups joined on the interface
                                    
                                    .. attribute:: group_address
                                    
                                    	Address of multicast group
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, self).__init__()

                                        self.yang_name = "multicast-group"
                                        self.yang_parent_name = "detail"

                                        self.group_address = YLeaf(YType.str, "group-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("group_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.group_address.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.group_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "multicast-group" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.group_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "group-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "group-address"):
                                            self.group_address = value
                                            self.group_address.value_namespace = name_space
                                            self.group_address.value_namespace_prefix = name_space_prefix


                                class SecondaryAddress(Entity):
                                    """
                                    Secondary addresses on the interface
                                    
                                    .. attribute:: address
                                    
                                    	Address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix length of address
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: route_tag
                                    
                                    	Route Tag associated with this address (0 = no tag)
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv4-io-oper'
                                    _revision = '2015-10-20'

                                    def __init__(self):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress, self).__init__()

                                        self.yang_name = "secondary-address"
                                        self.yang_parent_name = "detail"

                                        self.address = YLeaf(YType.str, "address")

                                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                        self.route_tag = YLeaf(YType.uint32, "route-tag")

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
                                                        "prefix_length",
                                                        "route_tag") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.prefix_length.is_set or
                                            self.route_tag.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.prefix_length.yfilter != YFilter.not_set or
                                            self.route_tag.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "secondary-address" + path_buffer

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
                                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                        if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.route_tag.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "prefix-length" or name == "route-tag"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-length"):
                                            self.prefix_length = value
                                            self.prefix_length.value_namespace = name_space
                                            self.prefix_length.value_namespace_prefix = name_space_prefix
                                        if(value_path == "route-tag"):
                                            self.route_tag = value
                                            self.route_tag.value_namespace = name_space
                                            self.route_tag.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.multicast_group:
                                        if (c.has_data()):
                                            return True
                                    for c in self.secondary_address:
                                        if (c.has_data()):
                                            return True
                                    return (
                                        self.interface_name.is_set or
                                        self.direct_broadcast.is_set or
                                        self.flow_tag_dst.is_set or
                                        self.flow_tag_src.is_set or
                                        self.line_state.is_set or
                                        self.mask_reply.is_set or
                                        self.mlacp_active.is_set or
                                        self.mtu.is_set or
                                        self.prefix_length.is_set or
                                        self.primary_address.is_set or
                                        self.proxy_arp_disabled.is_set or
                                        self.redirect.is_set or
                                        self.rg_id_exists.is_set or
                                        self.route_tag.is_set or
                                        self.unnumbered_interface_name.is_set or
                                        self.unreachable.is_set or
                                        self.vrf_id.is_set or
                                        (self.acl is not None and self.acl.has_data()) or
                                        (self.bgp_pa is not None and self.bgp_pa.has_data()) or
                                        (self.caps_utime is not None and self.caps_utime.has_data()) or
                                        (self.fwd_dis_utime is not None and self.fwd_dis_utime.has_data()) or
                                        (self.fwd_en_utime is not None and self.fwd_en_utime.has_data()) or
                                        (self.helper_address is not None and self.helper_address.has_data()) or
                                        (self.idb_utime is not None and self.idb_utime.has_data()) or
                                        (self.multi_acl is not None and self.multi_acl.has_data()) or
                                        (self.pub_utime is not None and self.pub_utime.has_data()) or
                                        (self.rpf is not None and self.rpf.has_data()))

                                def has_operation(self):
                                    for c in self.multicast_group:
                                        if (c.has_operation()):
                                            return True
                                    for c in self.secondary_address:
                                        if (c.has_operation()):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.direct_broadcast.yfilter != YFilter.not_set or
                                        self.flow_tag_dst.yfilter != YFilter.not_set or
                                        self.flow_tag_src.yfilter != YFilter.not_set or
                                        self.line_state.yfilter != YFilter.not_set or
                                        self.mask_reply.yfilter != YFilter.not_set or
                                        self.mlacp_active.yfilter != YFilter.not_set or
                                        self.mtu.yfilter != YFilter.not_set or
                                        self.prefix_length.yfilter != YFilter.not_set or
                                        self.primary_address.yfilter != YFilter.not_set or
                                        self.proxy_arp_disabled.yfilter != YFilter.not_set or
                                        self.redirect.yfilter != YFilter.not_set or
                                        self.rg_id_exists.yfilter != YFilter.not_set or
                                        self.route_tag.yfilter != YFilter.not_set or
                                        self.unnumbered_interface_name.yfilter != YFilter.not_set or
                                        self.unreachable.yfilter != YFilter.not_set or
                                        self.vrf_id.yfilter != YFilter.not_set or
                                        (self.acl is not None and self.acl.has_operation()) or
                                        (self.bgp_pa is not None and self.bgp_pa.has_operation()) or
                                        (self.caps_utime is not None and self.caps_utime.has_operation()) or
                                        (self.fwd_dis_utime is not None and self.fwd_dis_utime.has_operation()) or
                                        (self.fwd_en_utime is not None and self.fwd_en_utime.has_operation()) or
                                        (self.helper_address is not None and self.helper_address.has_operation()) or
                                        (self.idb_utime is not None and self.idb_utime.has_operation()) or
                                        (self.multi_acl is not None and self.multi_acl.has_operation()) or
                                        (self.pub_utime is not None and self.pub_utime.has_operation()) or
                                        (self.rpf is not None and self.rpf.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "detail" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                                    if (self.direct_broadcast.is_set or self.direct_broadcast.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.direct_broadcast.get_name_leafdata())
                                    if (self.flow_tag_dst.is_set or self.flow_tag_dst.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.flow_tag_dst.get_name_leafdata())
                                    if (self.flow_tag_src.is_set or self.flow_tag_src.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.flow_tag_src.get_name_leafdata())
                                    if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.line_state.get_name_leafdata())
                                    if (self.mask_reply.is_set or self.mask_reply.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mask_reply.get_name_leafdata())
                                    if (self.mlacp_active.is_set or self.mlacp_active.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mlacp_active.get_name_leafdata())
                                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mtu.get_name_leafdata())
                                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                    if (self.primary_address.is_set or self.primary_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.primary_address.get_name_leafdata())
                                    if (self.proxy_arp_disabled.is_set or self.proxy_arp_disabled.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.proxy_arp_disabled.get_name_leafdata())
                                    if (self.redirect.is_set or self.redirect.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.redirect.get_name_leafdata())
                                    if (self.rg_id_exists.is_set or self.rg_id_exists.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rg_id_exists.get_name_leafdata())
                                    if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.route_tag.get_name_leafdata())
                                    if (self.unnumbered_interface_name.is_set or self.unnumbered_interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.unnumbered_interface_name.get_name_leafdata())
                                    if (self.unreachable.is_set or self.unreachable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.unreachable.get_name_leafdata())
                                    if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vrf_id.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "acl"):
                                        if (self.acl is None):
                                            self.acl = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl()
                                            self.acl.parent = self
                                            self._children_name_map["acl"] = "acl"
                                        return self.acl

                                    if (child_yang_name == "bgp-pa"):
                                        if (self.bgp_pa is None):
                                            self.bgp_pa = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa()
                                            self.bgp_pa.parent = self
                                            self._children_name_map["bgp_pa"] = "bgp-pa"
                                        return self.bgp_pa

                                    if (child_yang_name == "caps-utime"):
                                        if (self.caps_utime is None):
                                            self.caps_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime()
                                            self.caps_utime.parent = self
                                            self._children_name_map["caps_utime"] = "caps-utime"
                                        return self.caps_utime

                                    if (child_yang_name == "fwd-dis-utime"):
                                        if (self.fwd_dis_utime is None):
                                            self.fwd_dis_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime()
                                            self.fwd_dis_utime.parent = self
                                            self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"
                                        return self.fwd_dis_utime

                                    if (child_yang_name == "fwd-en-utime"):
                                        if (self.fwd_en_utime is None):
                                            self.fwd_en_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime()
                                            self.fwd_en_utime.parent = self
                                            self._children_name_map["fwd_en_utime"] = "fwd-en-utime"
                                        return self.fwd_en_utime

                                    if (child_yang_name == "helper-address"):
                                        if (self.helper_address is None):
                                            self.helper_address = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress()
                                            self.helper_address.parent = self
                                            self._children_name_map["helper_address"] = "helper-address"
                                        return self.helper_address

                                    if (child_yang_name == "idb-utime"):
                                        if (self.idb_utime is None):
                                            self.idb_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime()
                                            self.idb_utime.parent = self
                                            self._children_name_map["idb_utime"] = "idb-utime"
                                        return self.idb_utime

                                    if (child_yang_name == "multi-acl"):
                                        if (self.multi_acl is None):
                                            self.multi_acl = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl()
                                            self.multi_acl.parent = self
                                            self._children_name_map["multi_acl"] = "multi-acl"
                                        return self.multi_acl

                                    if (child_yang_name == "multicast-group"):
                                        for c in self.multicast_group:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.multicast_group.append(c)
                                        return c

                                    if (child_yang_name == "pub-utime"):
                                        if (self.pub_utime is None):
                                            self.pub_utime = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime()
                                            self.pub_utime.parent = self
                                            self._children_name_map["pub_utime"] = "pub-utime"
                                        return self.pub_utime

                                    if (child_yang_name == "rpf"):
                                        if (self.rpf is None):
                                            self.rpf = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf()
                                            self.rpf.parent = self
                                            self._children_name_map["rpf"] = "rpf"
                                        return self.rpf

                                    if (child_yang_name == "secondary-address"):
                                        for c in self.secondary_address:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.secondary_address.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "acl" or name == "bgp-pa" or name == "caps-utime" or name == "fwd-dis-utime" or name == "fwd-en-utime" or name == "helper-address" or name == "idb-utime" or name == "multi-acl" or name == "multicast-group" or name == "pub-utime" or name == "rpf" or name == "secondary-address" or name == "interface-name" or name == "direct-broadcast" or name == "flow-tag-dst" or name == "flow-tag-src" or name == "line-state" or name == "mask-reply" or name == "mlacp-active" or name == "mtu" or name == "prefix-length" or name == "primary-address" or name == "proxy-arp-disabled" or name == "redirect" or name == "rg-id-exists" or name == "route-tag" or name == "unnumbered-interface-name" or name == "unreachable" or name == "vrf-id"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "direct-broadcast"):
                                        self.direct_broadcast = value
                                        self.direct_broadcast.value_namespace = name_space
                                        self.direct_broadcast.value_namespace_prefix = name_space_prefix
                                    if(value_path == "flow-tag-dst"):
                                        self.flow_tag_dst = value
                                        self.flow_tag_dst.value_namespace = name_space
                                        self.flow_tag_dst.value_namespace_prefix = name_space_prefix
                                    if(value_path == "flow-tag-src"):
                                        self.flow_tag_src = value
                                        self.flow_tag_src.value_namespace = name_space
                                        self.flow_tag_src.value_namespace_prefix = name_space_prefix
                                    if(value_path == "line-state"):
                                        self.line_state = value
                                        self.line_state.value_namespace = name_space
                                        self.line_state.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mask-reply"):
                                        self.mask_reply = value
                                        self.mask_reply.value_namespace = name_space
                                        self.mask_reply.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mlacp-active"):
                                        self.mlacp_active = value
                                        self.mlacp_active.value_namespace = name_space
                                        self.mlacp_active.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mtu"):
                                        self.mtu = value
                                        self.mtu.value_namespace = name_space
                                        self.mtu.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix-length"):
                                        self.prefix_length = value
                                        self.prefix_length.value_namespace = name_space
                                        self.prefix_length.value_namespace_prefix = name_space_prefix
                                    if(value_path == "primary-address"):
                                        self.primary_address = value
                                        self.primary_address.value_namespace = name_space
                                        self.primary_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "proxy-arp-disabled"):
                                        self.proxy_arp_disabled = value
                                        self.proxy_arp_disabled.value_namespace = name_space
                                        self.proxy_arp_disabled.value_namespace_prefix = name_space_prefix
                                    if(value_path == "redirect"):
                                        self.redirect = value
                                        self.redirect.value_namespace = name_space
                                        self.redirect.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rg-id-exists"):
                                        self.rg_id_exists = value
                                        self.rg_id_exists.value_namespace = name_space
                                        self.rg_id_exists.value_namespace_prefix = name_space_prefix
                                    if(value_path == "route-tag"):
                                        self.route_tag = value
                                        self.route_tag.value_namespace = name_space
                                        self.route_tag.value_namespace_prefix = name_space_prefix
                                    if(value_path == "unnumbered-interface-name"):
                                        self.unnumbered_interface_name = value
                                        self.unnumbered_interface_name.value_namespace = name_space
                                        self.unnumbered_interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "unreachable"):
                                        self.unreachable = value
                                        self.unreachable.value_namespace = name_space
                                        self.unreachable.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vrf-id"):
                                        self.vrf_id = value
                                        self.vrf_id.value_namespace = name_space
                                        self.vrf_id.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.detail:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.detail:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "details" + path_buffer

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

                                if (child_yang_name == "detail"):
                                    for c in self.detail:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.detail.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "detail"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.vrf_name.is_set or
                                (self.briefs is not None and self.briefs.has_data()) or
                                (self.details is not None and self.details.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set or
                                (self.briefs is not None and self.briefs.has_operation()) or
                                (self.details is not None and self.details.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                            if (child_yang_name == "briefs"):
                                if (self.briefs is None):
                                    self.briefs = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs()
                                    self.briefs.parent = self
                                    self._children_name_map["briefs"] = "briefs"
                                return self.briefs

                            if (child_yang_name == "details"):
                                if (self.details is None):
                                    self.details = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details()
                                    self.details.parent = self
                                    self._children_name_map["details"] = "details"
                                return self.details

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "briefs" or name == "details" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.vrf:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.vrf:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrfs" + path_buffer

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

                        if (child_yang_name == "vrf"):
                            for c in self.vrf:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.vrf.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vrf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Summary(Entity):
                    """
                    Summary of IPv4 network operational interface
                    data on a node
                    
                    .. attribute:: if_down_down
                    
                    	Number of interfaces (down,down)
                    	**type**\:   :py:class:`IfDownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown>`
                    
                    .. attribute:: if_shutdown_down
                    
                    	Number of interfaces (shutdown,down)
                    	**type**\:   :py:class:`IfShutdownDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown>`
                    
                    .. attribute:: if_up_down
                    
                    	Number of interfaces (up,down)
                    	**type**\:   :py:class:`IfUpDown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown>`
                    
                    .. attribute:: if_up_down_basecaps_up
                    
                    	Number of interfaces (up,down) with basecaps up
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: if_up_up
                    
                    	Number of interfaces (up,up)
                    	**type**\:   :py:class:`IfUpUp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp>`
                    
                    

                    """

                    _prefix = 'ipv4-io-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        super(Ipv4Network.Nodes.Node.InterfaceData.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "interface-data"

                        self.if_up_down_basecaps_up = YLeaf(YType.uint32, "if-up-down-basecaps-up")

                        self.if_down_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown()
                        self.if_down_down.parent = self
                        self._children_name_map["if_down_down"] = "if-down-down"
                        self._children_yang_names.add("if-down-down")

                        self.if_shutdown_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown()
                        self.if_shutdown_down.parent = self
                        self._children_name_map["if_shutdown_down"] = "if-shutdown-down"
                        self._children_yang_names.add("if-shutdown-down")

                        self.if_up_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown()
                        self.if_up_down.parent = self
                        self._children_name_map["if_up_down"] = "if-up-down"
                        self._children_yang_names.add("if-up-down")

                        self.if_up_up = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp()
                        self.if_up_up.parent = self
                        self._children_name_map["if_up_up"] = "if-up-up"
                        self._children_yang_names.add("if-up-up")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("if_up_down_basecaps_up") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Summary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Network.Nodes.Node.InterfaceData.Summary, self).__setattr__(name, value)


                    class IfUpUp(Entity):
                        """
                        Number of interfaces (up,up)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp, self).__init__()

                            self.yang_name = "if-up-up"
                            self.yang_parent_name = "summary"

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ip_assigned",
                                            "ip_unassigned",
                                            "ip_unnumbered") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ip_assigned.is_set or
                                self.ip_unassigned.is_set or
                                self.ip_unnumbered.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ip_assigned.yfilter != YFilter.not_set or
                                self.ip_unassigned.yfilter != YFilter.not_set or
                                self.ip_unnumbered.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "if-up-up" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ip_assigned.is_set or self.ip_assigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_assigned.get_name_leafdata())
                            if (self.ip_unassigned.is_set or self.ip_unassigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unassigned.get_name_leafdata())
                            if (self.ip_unnumbered.is_set or self.ip_unnumbered.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unnumbered.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ip-assigned" or name == "ip-unassigned" or name == "ip-unnumbered"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ip-assigned"):
                                self.ip_assigned = value
                                self.ip_assigned.value_namespace = name_space
                                self.ip_assigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unassigned"):
                                self.ip_unassigned = value
                                self.ip_unassigned.value_namespace = name_space
                                self.ip_unassigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unnumbered"):
                                self.ip_unnumbered = value
                                self.ip_unnumbered.value_namespace = name_space
                                self.ip_unnumbered.value_namespace_prefix = name_space_prefix


                    class IfUpDown(Entity):
                        """
                        Number of interfaces (up,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown, self).__init__()

                            self.yang_name = "if-up-down"
                            self.yang_parent_name = "summary"

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ip_assigned",
                                            "ip_unassigned",
                                            "ip_unnumbered") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ip_assigned.is_set or
                                self.ip_unassigned.is_set or
                                self.ip_unnumbered.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ip_assigned.yfilter != YFilter.not_set or
                                self.ip_unassigned.yfilter != YFilter.not_set or
                                self.ip_unnumbered.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "if-up-down" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ip_assigned.is_set or self.ip_assigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_assigned.get_name_leafdata())
                            if (self.ip_unassigned.is_set or self.ip_unassigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unassigned.get_name_leafdata())
                            if (self.ip_unnumbered.is_set or self.ip_unnumbered.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unnumbered.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ip-assigned" or name == "ip-unassigned" or name == "ip-unnumbered"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ip-assigned"):
                                self.ip_assigned = value
                                self.ip_assigned.value_namespace = name_space
                                self.ip_assigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unassigned"):
                                self.ip_unassigned = value
                                self.ip_unassigned.value_namespace = name_space
                                self.ip_unassigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unnumbered"):
                                self.ip_unnumbered = value
                                self.ip_unnumbered.value_namespace = name_space
                                self.ip_unnumbered.value_namespace_prefix = name_space_prefix


                    class IfDownDown(Entity):
                        """
                        Number of interfaces (down,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown, self).__init__()

                            self.yang_name = "if-down-down"
                            self.yang_parent_name = "summary"

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ip_assigned",
                                            "ip_unassigned",
                                            "ip_unnumbered") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ip_assigned.is_set or
                                self.ip_unassigned.is_set or
                                self.ip_unnumbered.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ip_assigned.yfilter != YFilter.not_set or
                                self.ip_unassigned.yfilter != YFilter.not_set or
                                self.ip_unnumbered.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "if-down-down" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ip_assigned.is_set or self.ip_assigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_assigned.get_name_leafdata())
                            if (self.ip_unassigned.is_set or self.ip_unassigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unassigned.get_name_leafdata())
                            if (self.ip_unnumbered.is_set or self.ip_unnumbered.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unnumbered.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ip-assigned" or name == "ip-unassigned" or name == "ip-unnumbered"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ip-assigned"):
                                self.ip_assigned = value
                                self.ip_assigned.value_namespace = name_space
                                self.ip_assigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unassigned"):
                                self.ip_unassigned = value
                                self.ip_unassigned.value_namespace = name_space
                                self.ip_unassigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unnumbered"):
                                self.ip_unnumbered = value
                                self.ip_unnumbered.value_namespace = name_space
                                self.ip_unnumbered.value_namespace_prefix = name_space_prefix


                    class IfShutdownDown(Entity):
                        """
                        Number of interfaces (shutdown,down)
                        
                        .. attribute:: ip_assigned
                        
                        	Number of interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unassigned
                        
                        	Number of unassigned interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_unnumbered
                        
                        	Number of unnumbered interfaces with explicit addresses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, self).__init__()

                            self.yang_name = "if-shutdown-down"
                            self.yang_parent_name = "summary"

                            self.ip_assigned = YLeaf(YType.uint32, "ip-assigned")

                            self.ip_unassigned = YLeaf(YType.uint32, "ip-unassigned")

                            self.ip_unnumbered = YLeaf(YType.uint32, "ip-unnumbered")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ip_assigned",
                                            "ip_unassigned",
                                            "ip_unnumbered") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ip_assigned.is_set or
                                self.ip_unassigned.is_set or
                                self.ip_unnumbered.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ip_assigned.yfilter != YFilter.not_set or
                                self.ip_unassigned.yfilter != YFilter.not_set or
                                self.ip_unnumbered.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "if-shutdown-down" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ip_assigned.is_set or self.ip_assigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_assigned.get_name_leafdata())
                            if (self.ip_unassigned.is_set or self.ip_unassigned.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unassigned.get_name_leafdata())
                            if (self.ip_unnumbered.is_set or self.ip_unnumbered.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_unnumbered.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ip-assigned" or name == "ip-unassigned" or name == "ip-unnumbered"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ip-assigned"):
                                self.ip_assigned = value
                                self.ip_assigned.value_namespace = name_space
                                self.ip_assigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unassigned"):
                                self.ip_unassigned = value
                                self.ip_unassigned.value_namespace = name_space
                                self.ip_unassigned.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-unnumbered"):
                                self.ip_unnumbered = value
                                self.ip_unnumbered.value_namespace = name_space
                                self.ip_unnumbered.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.if_up_down_basecaps_up.is_set or
                            (self.if_down_down is not None and self.if_down_down.has_data()) or
                            (self.if_shutdown_down is not None and self.if_shutdown_down.has_data()) or
                            (self.if_up_down is not None and self.if_up_down.has_data()) or
                            (self.if_up_up is not None and self.if_up_up.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.if_up_down_basecaps_up.yfilter != YFilter.not_set or
                            (self.if_down_down is not None and self.if_down_down.has_operation()) or
                            (self.if_shutdown_down is not None and self.if_shutdown_down.has_operation()) or
                            (self.if_up_down is not None and self.if_up_down.has_operation()) or
                            (self.if_up_up is not None and self.if_up_up.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "summary" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.if_up_down_basecaps_up.is_set or self.if_up_down_basecaps_up.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.if_up_down_basecaps_up.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "if-down-down"):
                            if (self.if_down_down is None):
                                self.if_down_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown()
                                self.if_down_down.parent = self
                                self._children_name_map["if_down_down"] = "if-down-down"
                            return self.if_down_down

                        if (child_yang_name == "if-shutdown-down"):
                            if (self.if_shutdown_down is None):
                                self.if_shutdown_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown()
                                self.if_shutdown_down.parent = self
                                self._children_name_map["if_shutdown_down"] = "if-shutdown-down"
                            return self.if_shutdown_down

                        if (child_yang_name == "if-up-down"):
                            if (self.if_up_down is None):
                                self.if_up_down = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown()
                                self.if_up_down.parent = self
                                self._children_name_map["if_up_down"] = "if-up-down"
                            return self.if_up_down

                        if (child_yang_name == "if-up-up"):
                            if (self.if_up_up is None):
                                self.if_up_up = Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp()
                                self.if_up_up.parent = self
                                self._children_name_map["if_up_up"] = "if-up-up"
                            return self.if_up_up

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "if-down-down" or name == "if-shutdown-down" or name == "if-up-down" or name == "if-up-up" or name == "if-up-down-basecaps-up"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "if-up-down-basecaps-up"):
                            self.if_up_down_basecaps_up = value
                            self.if_up_down_basecaps_up.value_namespace = name_space
                            self.if_up_down_basecaps_up.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.summary is not None and self.summary.has_data()) or
                        (self.vrfs is not None and self.vrfs.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.summary is not None and self.summary.has_operation()) or
                        (self.vrfs is not None and self.vrfs.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-data" + path_buffer

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

                    if (child_yang_name == "summary"):
                        if (self.summary is None):
                            self.summary = Ipv4Network.Nodes.Node.InterfaceData.Summary()
                            self.summary.parent = self
                            self._children_name_map["summary"] = "summary"
                        return self.summary

                    if (child_yang_name == "vrfs"):
                        if (self.vrfs is None):
                            self.vrfs = Ipv4Network.Nodes.Node.InterfaceData.Vrfs()
                            self.vrfs.parent = self
                            self._children_name_map["vrfs"] = "vrfs"
                        return self.vrfs

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "summary" or name == "vrfs"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Statistics(Entity):
                """
                Statistical IPv4 network operational data for
                a node
                
                .. attribute:: traffic
                
                	Traffic statistics for a node
                	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics.Traffic>`
                
                

                """

                _prefix = 'ipv4-io-oper'
                _revision = '2015-10-20'

                def __init__(self):
                    super(Ipv4Network.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"

                    self.traffic = Ipv4Network.Nodes.Node.Statistics.Traffic()
                    self.traffic.parent = self
                    self._children_name_map["traffic"] = "traffic"
                    self._children_yang_names.add("traffic")


                class Traffic(Entity):
                    """
                    Traffic statistics for a node
                    
                    .. attribute:: icmp_stats
                    
                    	ICMP Stats
                    	**type**\:   :py:class:`IcmpStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats>`
                    
                    .. attribute:: ipv4_stats
                    
                    	IPv4 Network Stats
                    	**type**\:   :py:class:`Ipv4Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats>`
                    
                    

                    """

                    _prefix = 'ipv4-io-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        super(Ipv4Network.Nodes.Node.Statistics.Traffic, self).__init__()

                        self.yang_name = "traffic"
                        self.yang_parent_name = "statistics"

                        self.icmp_stats = Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats()
                        self.icmp_stats.parent = self
                        self._children_name_map["icmp_stats"] = "icmp-stats"
                        self._children_yang_names.add("icmp-stats")

                        self.ipv4_stats = Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats()
                        self.ipv4_stats.parent = self
                        self._children_name_map["ipv4_stats"] = "ipv4-stats"
                        self._children_yang_names.add("ipv4-stats")


                    class Ipv4Stats(Entity):
                        """
                        IPv4 Network Stats
                        
                        .. attribute:: bad_header
                        
                        	Bad Header
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_hop_count
                        
                        	Bad Hop Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_option
                        
                        	Bad Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_security_option
                        
                        	Bad Security Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_source_address
                        
                        	Bad Source Address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: basic_security_option
                        
                        	Basic Security Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: broadcast_in
                        
                        	Broadcast In
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: broadcast_out
                        
                        	Broadcast Out
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cipso_option
                        
                        	Cipso Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: encapsulation_failed
                        
                        	Encapsulation Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_option
                        
                        	End Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: extended_security_option
                        
                        	Extended Security Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: format_errors
                        
                        	Format Errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_count
                        
                        	Fragment Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: input_packets
                        
                        	Input Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_decap_error
                        
                        	Lisp decap errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_encap_error
                        
                        	Lisp encap errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v4_decap
                        
                        	Lisp IPv4 decapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v4_encap
                        
                        	Lisp IPv4 encapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v6_decap
                        
                        	Lisp IPv6 decapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lisp_v6_encap
                        
                        	Lisp IPv6 encapped packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: loose_source_route_option
                        
                        	Loose Source Route Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: multicast_in
                        
                        	Multicast In
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: multicast_out
                        
                        	Multicast Out
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_gateway
                        
                        	No Gateway
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_protocol
                        
                        	No Protocol
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_router
                        
                        	No Router
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: noop_option
                        
                        	Noop Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: options_present
                        
                        	IP Options Present
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packet_too_big
                        
                        	Packet Too Big
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packets_forwarded
                        
                        	Packets Forwarded
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packets_fragmented
                        
                        	Packets Fragmented
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packets_output
                        
                        	Packets Output
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_failed
                        
                        	Reassembly Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_input
                        
                        	RaInput
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_max_drop
                        
                        	Reassembly Max Drop
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassemble_timeout
                        
                        	Reassembly Timeout
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembled
                        
                        	Reassembled
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_packets
                        
                        	Received Packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: record_route_option
                        
                        	Record Route Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: router_alert_option
                        
                        	Router Alert Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sid_option
                        
                        	SID Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: strict_source_route_option
                        
                        	Strict Source Route Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_option
                        
                        	Timestamp Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_option
                        
                        	Unknown Option
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats, self).__init__()

                            self.yang_name = "ipv4-stats"
                            self.yang_parent_name = "traffic"

                            self.bad_header = YLeaf(YType.uint32, "bad-header")

                            self.bad_hop_count = YLeaf(YType.uint32, "bad-hop-count")

                            self.bad_option = YLeaf(YType.uint32, "bad-option")

                            self.bad_security_option = YLeaf(YType.uint32, "bad-security-option")

                            self.bad_source_address = YLeaf(YType.uint32, "bad-source-address")

                            self.basic_security_option = YLeaf(YType.uint32, "basic-security-option")

                            self.broadcast_in = YLeaf(YType.uint32, "broadcast-in")

                            self.broadcast_out = YLeaf(YType.uint32, "broadcast-out")

                            self.cipso_option = YLeaf(YType.uint32, "cipso-option")

                            self.encapsulation_failed = YLeaf(YType.uint32, "encapsulation-failed")

                            self.end_option = YLeaf(YType.uint32, "end-option")

                            self.extended_security_option = YLeaf(YType.uint32, "extended-security-option")

                            self.format_errors = YLeaf(YType.uint32, "format-errors")

                            self.fragment_count = YLeaf(YType.uint32, "fragment-count")

                            self.input_packets = YLeaf(YType.uint32, "input-packets")

                            self.lisp_decap_error = YLeaf(YType.uint32, "lisp-decap-error")

                            self.lisp_encap_error = YLeaf(YType.uint32, "lisp-encap-error")

                            self.lisp_v4_decap = YLeaf(YType.uint32, "lisp-v4-decap")

                            self.lisp_v4_encap = YLeaf(YType.uint32, "lisp-v4-encap")

                            self.lisp_v6_decap = YLeaf(YType.uint32, "lisp-v6-decap")

                            self.lisp_v6_encap = YLeaf(YType.uint32, "lisp-v6-encap")

                            self.loose_source_route_option = YLeaf(YType.uint32, "loose-source-route-option")

                            self.multicast_in = YLeaf(YType.uint32, "multicast-in")

                            self.multicast_out = YLeaf(YType.uint32, "multicast-out")

                            self.no_gateway = YLeaf(YType.uint32, "no-gateway")

                            self.no_protocol = YLeaf(YType.uint32, "no-protocol")

                            self.no_router = YLeaf(YType.uint32, "no-router")

                            self.noop_option = YLeaf(YType.uint32, "noop-option")

                            self.options_present = YLeaf(YType.uint32, "options-present")

                            self.packet_too_big = YLeaf(YType.uint32, "packet-too-big")

                            self.packets_forwarded = YLeaf(YType.uint32, "packets-forwarded")

                            self.packets_fragmented = YLeaf(YType.uint32, "packets-fragmented")

                            self.packets_output = YLeaf(YType.uint32, "packets-output")

                            self.reassemble_failed = YLeaf(YType.uint32, "reassemble-failed")

                            self.reassemble_input = YLeaf(YType.uint32, "reassemble-input")

                            self.reassemble_max_drop = YLeaf(YType.uint32, "reassemble-max-drop")

                            self.reassemble_timeout = YLeaf(YType.uint32, "reassemble-timeout")

                            self.reassembled = YLeaf(YType.uint32, "reassembled")

                            self.received_packets = YLeaf(YType.uint32, "received-packets")

                            self.record_route_option = YLeaf(YType.uint32, "record-route-option")

                            self.router_alert_option = YLeaf(YType.uint32, "router-alert-option")

                            self.sid_option = YLeaf(YType.uint32, "sid-option")

                            self.strict_source_route_option = YLeaf(YType.uint32, "strict-source-route-option")

                            self.timestamp_option = YLeaf(YType.uint32, "timestamp-option")

                            self.unknown_option = YLeaf(YType.uint32, "unknown-option")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("bad_header",
                                            "bad_hop_count",
                                            "bad_option",
                                            "bad_security_option",
                                            "bad_source_address",
                                            "basic_security_option",
                                            "broadcast_in",
                                            "broadcast_out",
                                            "cipso_option",
                                            "encapsulation_failed",
                                            "end_option",
                                            "extended_security_option",
                                            "format_errors",
                                            "fragment_count",
                                            "input_packets",
                                            "lisp_decap_error",
                                            "lisp_encap_error",
                                            "lisp_v4_decap",
                                            "lisp_v4_encap",
                                            "lisp_v6_decap",
                                            "lisp_v6_encap",
                                            "loose_source_route_option",
                                            "multicast_in",
                                            "multicast_out",
                                            "no_gateway",
                                            "no_protocol",
                                            "no_router",
                                            "noop_option",
                                            "options_present",
                                            "packet_too_big",
                                            "packets_forwarded",
                                            "packets_fragmented",
                                            "packets_output",
                                            "reassemble_failed",
                                            "reassemble_input",
                                            "reassemble_max_drop",
                                            "reassemble_timeout",
                                            "reassembled",
                                            "received_packets",
                                            "record_route_option",
                                            "router_alert_option",
                                            "sid_option",
                                            "strict_source_route_option",
                                            "timestamp_option",
                                            "unknown_option") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.bad_header.is_set or
                                self.bad_hop_count.is_set or
                                self.bad_option.is_set or
                                self.bad_security_option.is_set or
                                self.bad_source_address.is_set or
                                self.basic_security_option.is_set or
                                self.broadcast_in.is_set or
                                self.broadcast_out.is_set or
                                self.cipso_option.is_set or
                                self.encapsulation_failed.is_set or
                                self.end_option.is_set or
                                self.extended_security_option.is_set or
                                self.format_errors.is_set or
                                self.fragment_count.is_set or
                                self.input_packets.is_set or
                                self.lisp_decap_error.is_set or
                                self.lisp_encap_error.is_set or
                                self.lisp_v4_decap.is_set or
                                self.lisp_v4_encap.is_set or
                                self.lisp_v6_decap.is_set or
                                self.lisp_v6_encap.is_set or
                                self.loose_source_route_option.is_set or
                                self.multicast_in.is_set or
                                self.multicast_out.is_set or
                                self.no_gateway.is_set or
                                self.no_protocol.is_set or
                                self.no_router.is_set or
                                self.noop_option.is_set or
                                self.options_present.is_set or
                                self.packet_too_big.is_set or
                                self.packets_forwarded.is_set or
                                self.packets_fragmented.is_set or
                                self.packets_output.is_set or
                                self.reassemble_failed.is_set or
                                self.reassemble_input.is_set or
                                self.reassemble_max_drop.is_set or
                                self.reassemble_timeout.is_set or
                                self.reassembled.is_set or
                                self.received_packets.is_set or
                                self.record_route_option.is_set or
                                self.router_alert_option.is_set or
                                self.sid_option.is_set or
                                self.strict_source_route_option.is_set or
                                self.timestamp_option.is_set or
                                self.unknown_option.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.bad_header.yfilter != YFilter.not_set or
                                self.bad_hop_count.yfilter != YFilter.not_set or
                                self.bad_option.yfilter != YFilter.not_set or
                                self.bad_security_option.yfilter != YFilter.not_set or
                                self.bad_source_address.yfilter != YFilter.not_set or
                                self.basic_security_option.yfilter != YFilter.not_set or
                                self.broadcast_in.yfilter != YFilter.not_set or
                                self.broadcast_out.yfilter != YFilter.not_set or
                                self.cipso_option.yfilter != YFilter.not_set or
                                self.encapsulation_failed.yfilter != YFilter.not_set or
                                self.end_option.yfilter != YFilter.not_set or
                                self.extended_security_option.yfilter != YFilter.not_set or
                                self.format_errors.yfilter != YFilter.not_set or
                                self.fragment_count.yfilter != YFilter.not_set or
                                self.input_packets.yfilter != YFilter.not_set or
                                self.lisp_decap_error.yfilter != YFilter.not_set or
                                self.lisp_encap_error.yfilter != YFilter.not_set or
                                self.lisp_v4_decap.yfilter != YFilter.not_set or
                                self.lisp_v4_encap.yfilter != YFilter.not_set or
                                self.lisp_v6_decap.yfilter != YFilter.not_set or
                                self.lisp_v6_encap.yfilter != YFilter.not_set or
                                self.loose_source_route_option.yfilter != YFilter.not_set or
                                self.multicast_in.yfilter != YFilter.not_set or
                                self.multicast_out.yfilter != YFilter.not_set or
                                self.no_gateway.yfilter != YFilter.not_set or
                                self.no_protocol.yfilter != YFilter.not_set or
                                self.no_router.yfilter != YFilter.not_set or
                                self.noop_option.yfilter != YFilter.not_set or
                                self.options_present.yfilter != YFilter.not_set or
                                self.packet_too_big.yfilter != YFilter.not_set or
                                self.packets_forwarded.yfilter != YFilter.not_set or
                                self.packets_fragmented.yfilter != YFilter.not_set or
                                self.packets_output.yfilter != YFilter.not_set or
                                self.reassemble_failed.yfilter != YFilter.not_set or
                                self.reassemble_input.yfilter != YFilter.not_set or
                                self.reassemble_max_drop.yfilter != YFilter.not_set or
                                self.reassemble_timeout.yfilter != YFilter.not_set or
                                self.reassembled.yfilter != YFilter.not_set or
                                self.received_packets.yfilter != YFilter.not_set or
                                self.record_route_option.yfilter != YFilter.not_set or
                                self.router_alert_option.yfilter != YFilter.not_set or
                                self.sid_option.yfilter != YFilter.not_set or
                                self.strict_source_route_option.yfilter != YFilter.not_set or
                                self.timestamp_option.yfilter != YFilter.not_set or
                                self.unknown_option.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv4-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.bad_header.is_set or self.bad_header.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_header.get_name_leafdata())
                            if (self.bad_hop_count.is_set or self.bad_hop_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_hop_count.get_name_leafdata())
                            if (self.bad_option.is_set or self.bad_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_option.get_name_leafdata())
                            if (self.bad_security_option.is_set or self.bad_security_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_security_option.get_name_leafdata())
                            if (self.bad_source_address.is_set or self.bad_source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_source_address.get_name_leafdata())
                            if (self.basic_security_option.is_set or self.basic_security_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.basic_security_option.get_name_leafdata())
                            if (self.broadcast_in.is_set or self.broadcast_in.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.broadcast_in.get_name_leafdata())
                            if (self.broadcast_out.is_set or self.broadcast_out.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.broadcast_out.get_name_leafdata())
                            if (self.cipso_option.is_set or self.cipso_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.cipso_option.get_name_leafdata())
                            if (self.encapsulation_failed.is_set or self.encapsulation_failed.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.encapsulation_failed.get_name_leafdata())
                            if (self.end_option.is_set or self.end_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.end_option.get_name_leafdata())
                            if (self.extended_security_option.is_set or self.extended_security_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.extended_security_option.get_name_leafdata())
                            if (self.format_errors.is_set or self.format_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.format_errors.get_name_leafdata())
                            if (self.fragment_count.is_set or self.fragment_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragment_count.get_name_leafdata())
                            if (self.input_packets.is_set or self.input_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.input_packets.get_name_leafdata())
                            if (self.lisp_decap_error.is_set or self.lisp_decap_error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_decap_error.get_name_leafdata())
                            if (self.lisp_encap_error.is_set or self.lisp_encap_error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_encap_error.get_name_leafdata())
                            if (self.lisp_v4_decap.is_set or self.lisp_v4_decap.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_v4_decap.get_name_leafdata())
                            if (self.lisp_v4_encap.is_set or self.lisp_v4_encap.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_v4_encap.get_name_leafdata())
                            if (self.lisp_v6_decap.is_set or self.lisp_v6_decap.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_v6_decap.get_name_leafdata())
                            if (self.lisp_v6_encap.is_set or self.lisp_v6_encap.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lisp_v6_encap.get_name_leafdata())
                            if (self.loose_source_route_option.is_set or self.loose_source_route_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.loose_source_route_option.get_name_leafdata())
                            if (self.multicast_in.is_set or self.multicast_in.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.multicast_in.get_name_leafdata())
                            if (self.multicast_out.is_set or self.multicast_out.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.multicast_out.get_name_leafdata())
                            if (self.no_gateway.is_set or self.no_gateway.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_gateway.get_name_leafdata())
                            if (self.no_protocol.is_set or self.no_protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_protocol.get_name_leafdata())
                            if (self.no_router.is_set or self.no_router.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_router.get_name_leafdata())
                            if (self.noop_option.is_set or self.noop_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.noop_option.get_name_leafdata())
                            if (self.options_present.is_set or self.options_present.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.options_present.get_name_leafdata())
                            if (self.packet_too_big.is_set or self.packet_too_big.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet_too_big.get_name_leafdata())
                            if (self.packets_forwarded.is_set or self.packets_forwarded.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets_forwarded.get_name_leafdata())
                            if (self.packets_fragmented.is_set or self.packets_fragmented.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets_fragmented.get_name_leafdata())
                            if (self.packets_output.is_set or self.packets_output.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packets_output.get_name_leafdata())
                            if (self.reassemble_failed.is_set or self.reassemble_failed.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reassemble_failed.get_name_leafdata())
                            if (self.reassemble_input.is_set or self.reassemble_input.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reassemble_input.get_name_leafdata())
                            if (self.reassemble_max_drop.is_set or self.reassemble_max_drop.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reassemble_max_drop.get_name_leafdata())
                            if (self.reassemble_timeout.is_set or self.reassemble_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reassemble_timeout.get_name_leafdata())
                            if (self.reassembled.is_set or self.reassembled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reassembled.get_name_leafdata())
                            if (self.received_packets.is_set or self.received_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received_packets.get_name_leafdata())
                            if (self.record_route_option.is_set or self.record_route_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.record_route_option.get_name_leafdata())
                            if (self.router_alert_option.is_set or self.router_alert_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.router_alert_option.get_name_leafdata())
                            if (self.sid_option.is_set or self.sid_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sid_option.get_name_leafdata())
                            if (self.strict_source_route_option.is_set or self.strict_source_route_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.strict_source_route_option.get_name_leafdata())
                            if (self.timestamp_option.is_set or self.timestamp_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.timestamp_option.get_name_leafdata())
                            if (self.unknown_option.is_set or self.unknown_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unknown_option.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bad-header" or name == "bad-hop-count" or name == "bad-option" or name == "bad-security-option" or name == "bad-source-address" or name == "basic-security-option" or name == "broadcast-in" or name == "broadcast-out" or name == "cipso-option" or name == "encapsulation-failed" or name == "end-option" or name == "extended-security-option" or name == "format-errors" or name == "fragment-count" or name == "input-packets" or name == "lisp-decap-error" or name == "lisp-encap-error" or name == "lisp-v4-decap" or name == "lisp-v4-encap" or name == "lisp-v6-decap" or name == "lisp-v6-encap" or name == "loose-source-route-option" or name == "multicast-in" or name == "multicast-out" or name == "no-gateway" or name == "no-protocol" or name == "no-router" or name == "noop-option" or name == "options-present" or name == "packet-too-big" or name == "packets-forwarded" or name == "packets-fragmented" or name == "packets-output" or name == "reassemble-failed" or name == "reassemble-input" or name == "reassemble-max-drop" or name == "reassemble-timeout" or name == "reassembled" or name == "received-packets" or name == "record-route-option" or name == "router-alert-option" or name == "sid-option" or name == "strict-source-route-option" or name == "timestamp-option" or name == "unknown-option"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "bad-header"):
                                self.bad_header = value
                                self.bad_header.value_namespace = name_space
                                self.bad_header.value_namespace_prefix = name_space_prefix
                            if(value_path == "bad-hop-count"):
                                self.bad_hop_count = value
                                self.bad_hop_count.value_namespace = name_space
                                self.bad_hop_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "bad-option"):
                                self.bad_option = value
                                self.bad_option.value_namespace = name_space
                                self.bad_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "bad-security-option"):
                                self.bad_security_option = value
                                self.bad_security_option.value_namespace = name_space
                                self.bad_security_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "bad-source-address"):
                                self.bad_source_address = value
                                self.bad_source_address.value_namespace = name_space
                                self.bad_source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "basic-security-option"):
                                self.basic_security_option = value
                                self.basic_security_option.value_namespace = name_space
                                self.basic_security_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "broadcast-in"):
                                self.broadcast_in = value
                                self.broadcast_in.value_namespace = name_space
                                self.broadcast_in.value_namespace_prefix = name_space_prefix
                            if(value_path == "broadcast-out"):
                                self.broadcast_out = value
                                self.broadcast_out.value_namespace = name_space
                                self.broadcast_out.value_namespace_prefix = name_space_prefix
                            if(value_path == "cipso-option"):
                                self.cipso_option = value
                                self.cipso_option.value_namespace = name_space
                                self.cipso_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "encapsulation-failed"):
                                self.encapsulation_failed = value
                                self.encapsulation_failed.value_namespace = name_space
                                self.encapsulation_failed.value_namespace_prefix = name_space_prefix
                            if(value_path == "end-option"):
                                self.end_option = value
                                self.end_option.value_namespace = name_space
                                self.end_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "extended-security-option"):
                                self.extended_security_option = value
                                self.extended_security_option.value_namespace = name_space
                                self.extended_security_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "format-errors"):
                                self.format_errors = value
                                self.format_errors.value_namespace = name_space
                                self.format_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragment-count"):
                                self.fragment_count = value
                                self.fragment_count.value_namespace = name_space
                                self.fragment_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "input-packets"):
                                self.input_packets = value
                                self.input_packets.value_namespace = name_space
                                self.input_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-decap-error"):
                                self.lisp_decap_error = value
                                self.lisp_decap_error.value_namespace = name_space
                                self.lisp_decap_error.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-encap-error"):
                                self.lisp_encap_error = value
                                self.lisp_encap_error.value_namespace = name_space
                                self.lisp_encap_error.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-v4-decap"):
                                self.lisp_v4_decap = value
                                self.lisp_v4_decap.value_namespace = name_space
                                self.lisp_v4_decap.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-v4-encap"):
                                self.lisp_v4_encap = value
                                self.lisp_v4_encap.value_namespace = name_space
                                self.lisp_v4_encap.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-v6-decap"):
                                self.lisp_v6_decap = value
                                self.lisp_v6_decap.value_namespace = name_space
                                self.lisp_v6_decap.value_namespace_prefix = name_space_prefix
                            if(value_path == "lisp-v6-encap"):
                                self.lisp_v6_encap = value
                                self.lisp_v6_encap.value_namespace = name_space
                                self.lisp_v6_encap.value_namespace_prefix = name_space_prefix
                            if(value_path == "loose-source-route-option"):
                                self.loose_source_route_option = value
                                self.loose_source_route_option.value_namespace = name_space
                                self.loose_source_route_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "multicast-in"):
                                self.multicast_in = value
                                self.multicast_in.value_namespace = name_space
                                self.multicast_in.value_namespace_prefix = name_space_prefix
                            if(value_path == "multicast-out"):
                                self.multicast_out = value
                                self.multicast_out.value_namespace = name_space
                                self.multicast_out.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-gateway"):
                                self.no_gateway = value
                                self.no_gateway.value_namespace = name_space
                                self.no_gateway.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-protocol"):
                                self.no_protocol = value
                                self.no_protocol.value_namespace = name_space
                                self.no_protocol.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-router"):
                                self.no_router = value
                                self.no_router.value_namespace = name_space
                                self.no_router.value_namespace_prefix = name_space_prefix
                            if(value_path == "noop-option"):
                                self.noop_option = value
                                self.noop_option.value_namespace = name_space
                                self.noop_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "options-present"):
                                self.options_present = value
                                self.options_present.value_namespace = name_space
                                self.options_present.value_namespace_prefix = name_space_prefix
                            if(value_path == "packet-too-big"):
                                self.packet_too_big = value
                                self.packet_too_big.value_namespace = name_space
                                self.packet_too_big.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets-forwarded"):
                                self.packets_forwarded = value
                                self.packets_forwarded.value_namespace = name_space
                                self.packets_forwarded.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets-fragmented"):
                                self.packets_fragmented = value
                                self.packets_fragmented.value_namespace = name_space
                                self.packets_fragmented.value_namespace_prefix = name_space_prefix
                            if(value_path == "packets-output"):
                                self.packets_output = value
                                self.packets_output.value_namespace = name_space
                                self.packets_output.value_namespace_prefix = name_space_prefix
                            if(value_path == "reassemble-failed"):
                                self.reassemble_failed = value
                                self.reassemble_failed.value_namespace = name_space
                                self.reassemble_failed.value_namespace_prefix = name_space_prefix
                            if(value_path == "reassemble-input"):
                                self.reassemble_input = value
                                self.reassemble_input.value_namespace = name_space
                                self.reassemble_input.value_namespace_prefix = name_space_prefix
                            if(value_path == "reassemble-max-drop"):
                                self.reassemble_max_drop = value
                                self.reassemble_max_drop.value_namespace = name_space
                                self.reassemble_max_drop.value_namespace_prefix = name_space_prefix
                            if(value_path == "reassemble-timeout"):
                                self.reassemble_timeout = value
                                self.reassemble_timeout.value_namespace = name_space
                                self.reassemble_timeout.value_namespace_prefix = name_space_prefix
                            if(value_path == "reassembled"):
                                self.reassembled = value
                                self.reassembled.value_namespace = name_space
                                self.reassembled.value_namespace_prefix = name_space_prefix
                            if(value_path == "received-packets"):
                                self.received_packets = value
                                self.received_packets.value_namespace = name_space
                                self.received_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "record-route-option"):
                                self.record_route_option = value
                                self.record_route_option.value_namespace = name_space
                                self.record_route_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "router-alert-option"):
                                self.router_alert_option = value
                                self.router_alert_option.value_namespace = name_space
                                self.router_alert_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "sid-option"):
                                self.sid_option = value
                                self.sid_option.value_namespace = name_space
                                self.sid_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "strict-source-route-option"):
                                self.strict_source_route_option = value
                                self.strict_source_route_option.value_namespace = name_space
                                self.strict_source_route_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "timestamp-option"):
                                self.timestamp_option = value
                                self.timestamp_option.value_namespace = name_space
                                self.timestamp_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "unknown-option"):
                                self.unknown_option = value
                                self.unknown_option.value_namespace = name_space
                                self.unknown_option.value_namespace_prefix = name_space_prefix


                    class IcmpStats(Entity):
                        """
                        ICMP Stats
                        
                        .. attribute:: admin_unreachable_received
                        
                        	ICMP Admin Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: admin_unreachable_sent
                        
                        	ICMP Admin Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: checksum_error
                        
                        	ICMP Checksum Errors
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_reply_received
                        
                        	ICMP Echo Reply Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_reply_sent
                        
                        	ICMP Echo Reply Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_request_received
                        
                        	ICMP Echo Request Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: echo_request_sent
                        
                        	ICMP Echo Request Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_unreachable_received
                        
                        	ICMP Fragment Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fragment_unreachable_sent
                        
                        	ICMP Fragment Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hopcount_received
                        
                        	ICMP Hopcount Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hopcount_sent
                        
                        	ICMP Hopcount Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: host_unreachable_received
                        
                        	ICMP Host Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: host_unreachable_sent
                        
                        	ICMP Host Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_reply_received
                        
                        	ICMP Mask Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_reply_sent
                        
                        	ICMP Mask Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_request_received
                        
                        	ICMP Mask Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask_request_sent
                        
                        	ICMP Mask Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_unreachable_received
                        
                        	ICMP Network Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_unreachable_sent
                        
                        	ICMP Network Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: output
                        
                        	ICMP Transmitted
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: param_error_received
                        
                        	ICMP Parameter Error Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: param_error_send
                        
                        	ICMP Parameter Error Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_unreachable_received
                        
                        	ICMP Port Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: port_unreachable_sent
                        
                        	ICMP Port Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: protocol_unreachable_received
                        
                        	ICMP Protocol Unreachable Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: protocol_unreachable_sent
                        
                        	ICMP Protocol Unreachable Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassebly_received
                        
                        	ICMP Reassembly Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reassembly_sent
                        
                        	ICMP Reassembly Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	ICMP Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: redirect_received
                        
                        	ICMP Redirect Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: redirect_send
                        
                        	ICMP Redirect Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: router_advert_received
                        
                        	ICMP Router Advertisement Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: router_solicit_received
                        
                        	ICMP Router Solicited Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: source_quench_received
                        
                        	ICMP Source Quench
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_received
                        
                        	ICMP Timestamp Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_reply_received
                        
                        	ICMP Timestamp Reply Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown
                        
                        	ICMP Unknown
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-io-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats, self).__init__()

                            self.yang_name = "icmp-stats"
                            self.yang_parent_name = "traffic"

                            self.admin_unreachable_received = YLeaf(YType.uint32, "admin-unreachable-received")

                            self.admin_unreachable_sent = YLeaf(YType.uint32, "admin-unreachable-sent")

                            self.checksum_error = YLeaf(YType.uint32, "checksum-error")

                            self.echo_reply_received = YLeaf(YType.uint32, "echo-reply-received")

                            self.echo_reply_sent = YLeaf(YType.uint32, "echo-reply-sent")

                            self.echo_request_received = YLeaf(YType.uint32, "echo-request-received")

                            self.echo_request_sent = YLeaf(YType.uint32, "echo-request-sent")

                            self.fragment_unreachable_received = YLeaf(YType.uint32, "fragment-unreachable-received")

                            self.fragment_unreachable_sent = YLeaf(YType.uint32, "fragment-unreachable-sent")

                            self.hopcount_received = YLeaf(YType.uint32, "hopcount-received")

                            self.hopcount_sent = YLeaf(YType.uint32, "hopcount-sent")

                            self.host_unreachable_received = YLeaf(YType.uint32, "host-unreachable-received")

                            self.host_unreachable_sent = YLeaf(YType.uint32, "host-unreachable-sent")

                            self.mask_reply_received = YLeaf(YType.uint32, "mask-reply-received")

                            self.mask_reply_sent = YLeaf(YType.uint32, "mask-reply-sent")

                            self.mask_request_received = YLeaf(YType.uint32, "mask-request-received")

                            self.mask_request_sent = YLeaf(YType.uint32, "mask-request-sent")

                            self.network_unreachable_received = YLeaf(YType.uint32, "network-unreachable-received")

                            self.network_unreachable_sent = YLeaf(YType.uint32, "network-unreachable-sent")

                            self.output = YLeaf(YType.uint32, "output")

                            self.param_error_received = YLeaf(YType.uint32, "param-error-received")

                            self.param_error_send = YLeaf(YType.uint32, "param-error-send")

                            self.port_unreachable_received = YLeaf(YType.uint32, "port-unreachable-received")

                            self.port_unreachable_sent = YLeaf(YType.uint32, "port-unreachable-sent")

                            self.protocol_unreachable_received = YLeaf(YType.uint32, "protocol-unreachable-received")

                            self.protocol_unreachable_sent = YLeaf(YType.uint32, "protocol-unreachable-sent")

                            self.reassebly_received = YLeaf(YType.uint32, "reassebly-received")

                            self.reassembly_sent = YLeaf(YType.uint32, "reassembly-sent")

                            self.received = YLeaf(YType.uint32, "received")

                            self.redirect_received = YLeaf(YType.uint32, "redirect-received")

                            self.redirect_send = YLeaf(YType.uint32, "redirect-send")

                            self.router_advert_received = YLeaf(YType.uint32, "router-advert-received")

                            self.router_solicit_received = YLeaf(YType.uint32, "router-solicit-received")

                            self.source_quench_received = YLeaf(YType.uint32, "source-quench-received")

                            self.timestamp_received = YLeaf(YType.uint32, "timestamp-received")

                            self.timestamp_reply_received = YLeaf(YType.uint32, "timestamp-reply-received")

                            self.unknown = YLeaf(YType.uint32, "unknown")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("admin_unreachable_received",
                                            "admin_unreachable_sent",
                                            "checksum_error",
                                            "echo_reply_received",
                                            "echo_reply_sent",
                                            "echo_request_received",
                                            "echo_request_sent",
                                            "fragment_unreachable_received",
                                            "fragment_unreachable_sent",
                                            "hopcount_received",
                                            "hopcount_sent",
                                            "host_unreachable_received",
                                            "host_unreachable_sent",
                                            "mask_reply_received",
                                            "mask_reply_sent",
                                            "mask_request_received",
                                            "mask_request_sent",
                                            "network_unreachable_received",
                                            "network_unreachable_sent",
                                            "output",
                                            "param_error_received",
                                            "param_error_send",
                                            "port_unreachable_received",
                                            "port_unreachable_sent",
                                            "protocol_unreachable_received",
                                            "protocol_unreachable_sent",
                                            "reassebly_received",
                                            "reassembly_sent",
                                            "received",
                                            "redirect_received",
                                            "redirect_send",
                                            "router_advert_received",
                                            "router_solicit_received",
                                            "source_quench_received",
                                            "timestamp_received",
                                            "timestamp_reply_received",
                                            "unknown") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.admin_unreachable_received.is_set or
                                self.admin_unreachable_sent.is_set or
                                self.checksum_error.is_set or
                                self.echo_reply_received.is_set or
                                self.echo_reply_sent.is_set or
                                self.echo_request_received.is_set or
                                self.echo_request_sent.is_set or
                                self.fragment_unreachable_received.is_set or
                                self.fragment_unreachable_sent.is_set or
                                self.hopcount_received.is_set or
                                self.hopcount_sent.is_set or
                                self.host_unreachable_received.is_set or
                                self.host_unreachable_sent.is_set or
                                self.mask_reply_received.is_set or
                                self.mask_reply_sent.is_set or
                                self.mask_request_received.is_set or
                                self.mask_request_sent.is_set or
                                self.network_unreachable_received.is_set or
                                self.network_unreachable_sent.is_set or
                                self.output.is_set or
                                self.param_error_received.is_set or
                                self.param_error_send.is_set or
                                self.port_unreachable_received.is_set or
                                self.port_unreachable_sent.is_set or
                                self.protocol_unreachable_received.is_set or
                                self.protocol_unreachable_sent.is_set or
                                self.reassebly_received.is_set or
                                self.reassembly_sent.is_set or
                                self.received.is_set or
                                self.redirect_received.is_set or
                                self.redirect_send.is_set or
                                self.router_advert_received.is_set or
                                self.router_solicit_received.is_set or
                                self.source_quench_received.is_set or
                                self.timestamp_received.is_set or
                                self.timestamp_reply_received.is_set or
                                self.unknown.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.admin_unreachable_received.yfilter != YFilter.not_set or
                                self.admin_unreachable_sent.yfilter != YFilter.not_set or
                                self.checksum_error.yfilter != YFilter.not_set or
                                self.echo_reply_received.yfilter != YFilter.not_set or
                                self.echo_reply_sent.yfilter != YFilter.not_set or
                                self.echo_request_received.yfilter != YFilter.not_set or
                                self.echo_request_sent.yfilter != YFilter.not_set or
                                self.fragment_unreachable_received.yfilter != YFilter.not_set or
                                self.fragment_unreachable_sent.yfilter != YFilter.not_set or
                                self.hopcount_received.yfilter != YFilter.not_set or
                                self.hopcount_sent.yfilter != YFilter.not_set or
                                self.host_unreachable_received.yfilter != YFilter.not_set or
                                self.host_unreachable_sent.yfilter != YFilter.not_set or
                                self.mask_reply_received.yfilter != YFilter.not_set or
                                self.mask_reply_sent.yfilter != YFilter.not_set or
                                self.mask_request_received.yfilter != YFilter.not_set or
                                self.mask_request_sent.yfilter != YFilter.not_set or
                                self.network_unreachable_received.yfilter != YFilter.not_set or
                                self.network_unreachable_sent.yfilter != YFilter.not_set or
                                self.output.yfilter != YFilter.not_set or
                                self.param_error_received.yfilter != YFilter.not_set or
                                self.param_error_send.yfilter != YFilter.not_set or
                                self.port_unreachable_received.yfilter != YFilter.not_set or
                                self.port_unreachable_sent.yfilter != YFilter.not_set or
                                self.protocol_unreachable_received.yfilter != YFilter.not_set or
                                self.protocol_unreachable_sent.yfilter != YFilter.not_set or
                                self.reassebly_received.yfilter != YFilter.not_set or
                                self.reassembly_sent.yfilter != YFilter.not_set or
                                self.received.yfilter != YFilter.not_set or
                                self.redirect_received.yfilter != YFilter.not_set or
                                self.redirect_send.yfilter != YFilter.not_set or
                                self.router_advert_received.yfilter != YFilter.not_set or
                                self.router_solicit_received.yfilter != YFilter.not_set or
                                self.source_quench_received.yfilter != YFilter.not_set or
                                self.timestamp_received.yfilter != YFilter.not_set or
                                self.timestamp_reply_received.yfilter != YFilter.not_set or
                                self.unknown.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "icmp-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.admin_unreachable_received.is_set or self.admin_unreachable_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.admin_unreachable_received.get_name_leafdata())
                            if (self.admin_unreachable_sent.is_set or self.admin_unreachable_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.admin_unreachable_sent.get_name_leafdata())
                            if (self.checksum_error.is_set or self.checksum_error.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.checksum_error.get_name_leafdata())
                            if (self.echo_reply_received.is_set or self.echo_reply_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.echo_reply_received.get_name_leafdata())
                            if (self.echo_reply_sent.is_set or self.echo_reply_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.echo_reply_sent.get_name_leafdata())
                            if (self.echo_request_received.is_set or self.echo_request_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.echo_request_received.get_name_leafdata())
                            if (self.echo_request_sent.is_set or self.echo_request_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.echo_request_sent.get_name_leafdata())
                            if (self.fragment_unreachable_received.is_set or self.fragment_unreachable_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragment_unreachable_received.get_name_leafdata())
                            if (self.fragment_unreachable_sent.is_set or self.fragment_unreachable_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragment_unreachable_sent.get_name_leafdata())
                            if (self.hopcount_received.is_set or self.hopcount_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hopcount_received.get_name_leafdata())
                            if (self.hopcount_sent.is_set or self.hopcount_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hopcount_sent.get_name_leafdata())
                            if (self.host_unreachable_received.is_set or self.host_unreachable_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.host_unreachable_received.get_name_leafdata())
                            if (self.host_unreachable_sent.is_set or self.host_unreachable_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.host_unreachable_sent.get_name_leafdata())
                            if (self.mask_reply_received.is_set or self.mask_reply_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mask_reply_received.get_name_leafdata())
                            if (self.mask_reply_sent.is_set or self.mask_reply_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mask_reply_sent.get_name_leafdata())
                            if (self.mask_request_received.is_set or self.mask_request_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mask_request_received.get_name_leafdata())
                            if (self.mask_request_sent.is_set or self.mask_request_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mask_request_sent.get_name_leafdata())
                            if (self.network_unreachable_received.is_set or self.network_unreachable_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.network_unreachable_received.get_name_leafdata())
                            if (self.network_unreachable_sent.is_set or self.network_unreachable_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.network_unreachable_sent.get_name_leafdata())
                            if (self.output.is_set or self.output.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output.get_name_leafdata())
                            if (self.param_error_received.is_set or self.param_error_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.param_error_received.get_name_leafdata())
                            if (self.param_error_send.is_set or self.param_error_send.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.param_error_send.get_name_leafdata())
                            if (self.port_unreachable_received.is_set or self.port_unreachable_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port_unreachable_received.get_name_leafdata())
                            if (self.port_unreachable_sent.is_set or self.port_unreachable_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port_unreachable_sent.get_name_leafdata())
                            if (self.protocol_unreachable_received.is_set or self.protocol_unreachable_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol_unreachable_received.get_name_leafdata())
                            if (self.protocol_unreachable_sent.is_set or self.protocol_unreachable_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol_unreachable_sent.get_name_leafdata())
                            if (self.reassebly_received.is_set or self.reassebly_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reassebly_received.get_name_leafdata())
                            if (self.reassembly_sent.is_set or self.reassembly_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reassembly_sent.get_name_leafdata())
                            if (self.received.is_set or self.received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.received.get_name_leafdata())
                            if (self.redirect_received.is_set or self.redirect_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.redirect_received.get_name_leafdata())
                            if (self.redirect_send.is_set or self.redirect_send.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.redirect_send.get_name_leafdata())
                            if (self.router_advert_received.is_set or self.router_advert_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.router_advert_received.get_name_leafdata())
                            if (self.router_solicit_received.is_set or self.router_solicit_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.router_solicit_received.get_name_leafdata())
                            if (self.source_quench_received.is_set or self.source_quench_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_quench_received.get_name_leafdata())
                            if (self.timestamp_received.is_set or self.timestamp_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.timestamp_received.get_name_leafdata())
                            if (self.timestamp_reply_received.is_set or self.timestamp_reply_received.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.timestamp_reply_received.get_name_leafdata())
                            if (self.unknown.is_set or self.unknown.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unknown.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "admin-unreachable-received" or name == "admin-unreachable-sent" or name == "checksum-error" or name == "echo-reply-received" or name == "echo-reply-sent" or name == "echo-request-received" or name == "echo-request-sent" or name == "fragment-unreachable-received" or name == "fragment-unreachable-sent" or name == "hopcount-received" or name == "hopcount-sent" or name == "host-unreachable-received" or name == "host-unreachable-sent" or name == "mask-reply-received" or name == "mask-reply-sent" or name == "mask-request-received" or name == "mask-request-sent" or name == "network-unreachable-received" or name == "network-unreachable-sent" or name == "output" or name == "param-error-received" or name == "param-error-send" or name == "port-unreachable-received" or name == "port-unreachable-sent" or name == "protocol-unreachable-received" or name == "protocol-unreachable-sent" or name == "reassebly-received" or name == "reassembly-sent" or name == "received" or name == "redirect-received" or name == "redirect-send" or name == "router-advert-received" or name == "router-solicit-received" or name == "source-quench-received" or name == "timestamp-received" or name == "timestamp-reply-received" or name == "unknown"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "admin-unreachable-received"):
                                self.admin_unreachable_received = value
                                self.admin_unreachable_received.value_namespace = name_space
                                self.admin_unreachable_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "admin-unreachable-sent"):
                                self.admin_unreachable_sent = value
                                self.admin_unreachable_sent.value_namespace = name_space
                                self.admin_unreachable_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "checksum-error"):
                                self.checksum_error = value
                                self.checksum_error.value_namespace = name_space
                                self.checksum_error.value_namespace_prefix = name_space_prefix
                            if(value_path == "echo-reply-received"):
                                self.echo_reply_received = value
                                self.echo_reply_received.value_namespace = name_space
                                self.echo_reply_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "echo-reply-sent"):
                                self.echo_reply_sent = value
                                self.echo_reply_sent.value_namespace = name_space
                                self.echo_reply_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "echo-request-received"):
                                self.echo_request_received = value
                                self.echo_request_received.value_namespace = name_space
                                self.echo_request_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "echo-request-sent"):
                                self.echo_request_sent = value
                                self.echo_request_sent.value_namespace = name_space
                                self.echo_request_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragment-unreachable-received"):
                                self.fragment_unreachable_received = value
                                self.fragment_unreachable_received.value_namespace = name_space
                                self.fragment_unreachable_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragment-unreachable-sent"):
                                self.fragment_unreachable_sent = value
                                self.fragment_unreachable_sent.value_namespace = name_space
                                self.fragment_unreachable_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "hopcount-received"):
                                self.hopcount_received = value
                                self.hopcount_received.value_namespace = name_space
                                self.hopcount_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "hopcount-sent"):
                                self.hopcount_sent = value
                                self.hopcount_sent.value_namespace = name_space
                                self.hopcount_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "host-unreachable-received"):
                                self.host_unreachable_received = value
                                self.host_unreachable_received.value_namespace = name_space
                                self.host_unreachable_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "host-unreachable-sent"):
                                self.host_unreachable_sent = value
                                self.host_unreachable_sent.value_namespace = name_space
                                self.host_unreachable_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "mask-reply-received"):
                                self.mask_reply_received = value
                                self.mask_reply_received.value_namespace = name_space
                                self.mask_reply_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "mask-reply-sent"):
                                self.mask_reply_sent = value
                                self.mask_reply_sent.value_namespace = name_space
                                self.mask_reply_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "mask-request-received"):
                                self.mask_request_received = value
                                self.mask_request_received.value_namespace = name_space
                                self.mask_request_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "mask-request-sent"):
                                self.mask_request_sent = value
                                self.mask_request_sent.value_namespace = name_space
                                self.mask_request_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "network-unreachable-received"):
                                self.network_unreachable_received = value
                                self.network_unreachable_received.value_namespace = name_space
                                self.network_unreachable_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "network-unreachable-sent"):
                                self.network_unreachable_sent = value
                                self.network_unreachable_sent.value_namespace = name_space
                                self.network_unreachable_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "output"):
                                self.output = value
                                self.output.value_namespace = name_space
                                self.output.value_namespace_prefix = name_space_prefix
                            if(value_path == "param-error-received"):
                                self.param_error_received = value
                                self.param_error_received.value_namespace = name_space
                                self.param_error_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "param-error-send"):
                                self.param_error_send = value
                                self.param_error_send.value_namespace = name_space
                                self.param_error_send.value_namespace_prefix = name_space_prefix
                            if(value_path == "port-unreachable-received"):
                                self.port_unreachable_received = value
                                self.port_unreachable_received.value_namespace = name_space
                                self.port_unreachable_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "port-unreachable-sent"):
                                self.port_unreachable_sent = value
                                self.port_unreachable_sent.value_namespace = name_space
                                self.port_unreachable_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "protocol-unreachable-received"):
                                self.protocol_unreachable_received = value
                                self.protocol_unreachable_received.value_namespace = name_space
                                self.protocol_unreachable_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "protocol-unreachable-sent"):
                                self.protocol_unreachable_sent = value
                                self.protocol_unreachable_sent.value_namespace = name_space
                                self.protocol_unreachable_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "reassebly-received"):
                                self.reassebly_received = value
                                self.reassebly_received.value_namespace = name_space
                                self.reassebly_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "reassembly-sent"):
                                self.reassembly_sent = value
                                self.reassembly_sent.value_namespace = name_space
                                self.reassembly_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "received"):
                                self.received = value
                                self.received.value_namespace = name_space
                                self.received.value_namespace_prefix = name_space_prefix
                            if(value_path == "redirect-received"):
                                self.redirect_received = value
                                self.redirect_received.value_namespace = name_space
                                self.redirect_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "redirect-send"):
                                self.redirect_send = value
                                self.redirect_send.value_namespace = name_space
                                self.redirect_send.value_namespace_prefix = name_space_prefix
                            if(value_path == "router-advert-received"):
                                self.router_advert_received = value
                                self.router_advert_received.value_namespace = name_space
                                self.router_advert_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "router-solicit-received"):
                                self.router_solicit_received = value
                                self.router_solicit_received.value_namespace = name_space
                                self.router_solicit_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-quench-received"):
                                self.source_quench_received = value
                                self.source_quench_received.value_namespace = name_space
                                self.source_quench_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "timestamp-received"):
                                self.timestamp_received = value
                                self.timestamp_received.value_namespace = name_space
                                self.timestamp_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "timestamp-reply-received"):
                                self.timestamp_reply_received = value
                                self.timestamp_reply_received.value_namespace = name_space
                                self.timestamp_reply_received.value_namespace_prefix = name_space_prefix
                            if(value_path == "unknown"):
                                self.unknown = value
                                self.unknown.value_namespace = name_space
                                self.unknown.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.icmp_stats is not None and self.icmp_stats.has_data()) or
                            (self.ipv4_stats is not None and self.ipv4_stats.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.icmp_stats is not None and self.icmp_stats.has_operation()) or
                            (self.ipv4_stats is not None and self.ipv4_stats.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "traffic" + path_buffer

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

                        if (child_yang_name == "icmp-stats"):
                            if (self.icmp_stats is None):
                                self.icmp_stats = Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats()
                                self.icmp_stats.parent = self
                                self._children_name_map["icmp_stats"] = "icmp-stats"
                            return self.icmp_stats

                        if (child_yang_name == "ipv4-stats"):
                            if (self.ipv4_stats is None):
                                self.ipv4_stats = Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats()
                                self.ipv4_stats.parent = self
                                self._children_name_map["ipv4_stats"] = "ipv4-stats"
                            return self.ipv4_stats

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "icmp-stats" or name == "ipv4-stats"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.traffic is not None and self.traffic.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.traffic is not None and self.traffic.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics" + path_buffer

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

                    if (child_yang_name == "traffic"):
                        if (self.traffic is None):
                            self.traffic = Ipv4Network.Nodes.Node.Statistics.Traffic()
                            self.traffic.parent = self
                            self._children_name_map["traffic"] = "traffic"
                        return self.traffic

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "traffic"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.interface_data is not None and self.interface_data.has_data()) or
                    (self.statistics is not None and self.statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.interface_data is not None and self.interface_data.has_operation()) or
                    (self.statistics is not None and self.statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface-data"):
                    if (self.interface_data is None):
                        self.interface_data = Ipv4Network.Nodes.Node.InterfaceData()
                        self.interface_data.parent = self
                        self._children_name_map["interface_data"] = "interface-data"
                    return self.interface_data

                if (child_yang_name == "statistics"):
                    if (self.statistics is None):
                        self.statistics = Ipv4Network.Nodes.Node.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                    return self.statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-data" or name == "statistics" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ipv4Network.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Interfaces(Entity):
        """
        IPv4 network operational interface data
        
        .. attribute:: interface
        
        	Interface names with VRF
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-ma-oper'
        _revision = '2015-10-20'

        def __init__(self):
            super(Ipv4Network.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "ipv4-network"

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
                        super(Ipv4Network.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Network.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            Interface names with VRF
            
            .. attribute:: interface_name  <key>
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: vrfs
            
            	List of VRF on the interface
            	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs>`
            
            

            """

            _prefix = 'ipv4-ma-oper'
            _revision = '2015-10-20'

            def __init__(self):
                super(Ipv4Network.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.vrfs = Ipv4Network.Interfaces.Interface.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._children_yang_names.add("vrfs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv4Network.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4Network.Interfaces.Interface, self).__setattr__(name, value)


            class Vrfs(Entity):
                """
                List of VRF on the interface
                
                .. attribute:: vrf
                
                	VRF information on the interface
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf>`
                
                

                """

                _prefix = 'ipv4-ma-oper'
                _revision = '2015-10-20'

                def __init__(self):
                    super(Ipv4Network.Interfaces.Interface.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "interface"

                    self.vrf = YList(self)

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
                                super(Ipv4Network.Interfaces.Interface.Vrfs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4Network.Interfaces.Interface.Vrfs, self).__setattr__(name, value)


                class Vrf(Entity):
                    """
                    VRF information on the interface
                    
                    .. attribute:: vrf_name  <key>
                    
                    	The VRF name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: brief
                    
                    	Brief IPv4 network operational data for an interface
                    	**type**\:   :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief>`
                    
                    .. attribute:: detail
                    
                    	Detail IPv4 network operational data for an interface
                    	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail>`
                    
                    

                    """

                    _prefix = 'ipv4-ma-oper'
                    _revision = '2015-10-20'

                    def __init__(self):
                        super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.brief = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief()
                        self.brief.parent = self
                        self._children_name_map["brief"] = "brief"
                        self._children_yang_names.add("brief")

                        self.detail = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"
                        self._children_yang_names.add("detail")

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
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf, self).__setattr__(name, value)


                    class Detail(Entity):
                        """
                        Detail IPv4 network operational data for an
                        interface
                        
                        .. attribute:: acl
                        
                        	ACLs configured on the interface
                        	**type**\:   :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl>`
                        
                        .. attribute:: bgp_pa
                        
                        	BGP PA config on the interface
                        	**type**\:   :py:class:`BgpPa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa>`
                        
                        .. attribute:: caps_utime
                        
                        	CAPS Add Time
                        	**type**\:   :py:class:`CapsUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime>`
                        
                        .. attribute:: direct_broadcast
                        
                        	Are direct broadcasts sent on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: flow_tag_dst
                        
                        	Is BGP Flow Tag Destination is enable
                        	**type**\:  bool
                        
                        .. attribute:: flow_tag_src
                        
                        	Is BGP Flow Tag Source is enable
                        	**type**\:  bool
                        
                        .. attribute:: fwd_dis_utime
                        
                        	FWD DISABLE Time
                        	**type**\:   :py:class:`FwdDisUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime>`
                        
                        .. attribute:: fwd_en_utime
                        
                        	FWD ENABLE Time
                        	**type**\:   :py:class:`FwdEnUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime>`
                        
                        .. attribute:: helper_address
                        
                        	Helper Addresses configured on the interface
                        	**type**\:   :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress>`
                        
                        .. attribute:: idb_utime
                        
                        	IDB Create Time
                        	**type**\:   :py:class:`IdbUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime>`
                        
                        .. attribute:: line_state
                        
                        	Line state of the interface
                        	**type**\:   :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.Ipv4MaOperLineState>`
                        
                        .. attribute:: mask_reply
                        
                        	Are mask replies sent on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: mlacp_active
                        
                        	Is mLACP state Active (valid if RG ID exists)
                        	**type**\:  bool
                        
                        .. attribute:: mtu
                        
                        	IP MTU of the interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: multi_acl
                        
                        	Multi ACLs configured on the interface
                        	**type**\:   :py:class:`MultiAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl>`
                        
                        .. attribute:: multicast_group
                        
                        	Multicast groups joined on the interface
                        	**type**\: list of    :py:class:`MulticastGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup>`
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length of primary address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: primary_address
                        
                        	Primary address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: proxy_arp_disabled
                        
                        	Is Proxy ARP disabled on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: pub_utime
                        
                        	Address Publish Time
                        	**type**\:   :py:class:`PubUtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime>`
                        
                        .. attribute:: redirect
                        
                        	Are ICMP redirects sent on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: rg_id_exists
                        
                        	Does ICCP RG ID exist on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: route_tag
                        
                        	Route tag associated with the primary address (0 = no tag)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rpf
                        
                        	RPF config on the interface
                        	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf>`
                        
                        .. attribute:: secondary_address
                        
                        	Secondary addresses on the interface
                        	**type**\: list of    :py:class:`SecondaryAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress>`
                        
                        .. attribute:: unnumbered_interface_name
                        
                        	Name of referenced interface (valid if unnumbered)
                        	**type**\:  str
                        
                        .. attribute:: unreachable
                        
                        	Are ICMP unreachables sent on the interface?
                        	**type**\:  bool
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID of the interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-ma-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail, self).__init__()

                            self.yang_name = "detail"
                            self.yang_parent_name = "vrf"

                            self.direct_broadcast = YLeaf(YType.boolean, "direct-broadcast")

                            self.flow_tag_dst = YLeaf(YType.boolean, "flow-tag-dst")

                            self.flow_tag_src = YLeaf(YType.boolean, "flow-tag-src")

                            self.line_state = YLeaf(YType.enumeration, "line-state")

                            self.mask_reply = YLeaf(YType.boolean, "mask-reply")

                            self.mlacp_active = YLeaf(YType.boolean, "mlacp-active")

                            self.mtu = YLeaf(YType.uint32, "mtu")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.primary_address = YLeaf(YType.str, "primary-address")

                            self.proxy_arp_disabled = YLeaf(YType.boolean, "proxy-arp-disabled")

                            self.redirect = YLeaf(YType.boolean, "redirect")

                            self.rg_id_exists = YLeaf(YType.boolean, "rg-id-exists")

                            self.route_tag = YLeaf(YType.uint32, "route-tag")

                            self.unnumbered_interface_name = YLeaf(YType.str, "unnumbered-interface-name")

                            self.unreachable = YLeaf(YType.boolean, "unreachable")

                            self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                            self.acl = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl()
                            self.acl.parent = self
                            self._children_name_map["acl"] = "acl"
                            self._children_yang_names.add("acl")

                            self.bgp_pa = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa()
                            self.bgp_pa.parent = self
                            self._children_name_map["bgp_pa"] = "bgp-pa"
                            self._children_yang_names.add("bgp-pa")

                            self.caps_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime()
                            self.caps_utime.parent = self
                            self._children_name_map["caps_utime"] = "caps-utime"
                            self._children_yang_names.add("caps-utime")

                            self.fwd_dis_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime()
                            self.fwd_dis_utime.parent = self
                            self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"
                            self._children_yang_names.add("fwd-dis-utime")

                            self.fwd_en_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime()
                            self.fwd_en_utime.parent = self
                            self._children_name_map["fwd_en_utime"] = "fwd-en-utime"
                            self._children_yang_names.add("fwd-en-utime")

                            self.helper_address = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress()
                            self.helper_address.parent = self
                            self._children_name_map["helper_address"] = "helper-address"
                            self._children_yang_names.add("helper-address")

                            self.idb_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime()
                            self.idb_utime.parent = self
                            self._children_name_map["idb_utime"] = "idb-utime"
                            self._children_yang_names.add("idb-utime")

                            self.multi_acl = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl()
                            self.multi_acl.parent = self
                            self._children_name_map["multi_acl"] = "multi-acl"
                            self._children_yang_names.add("multi-acl")

                            self.pub_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime()
                            self.pub_utime.parent = self
                            self._children_name_map["pub_utime"] = "pub-utime"
                            self._children_yang_names.add("pub-utime")

                            self.rpf = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf()
                            self.rpf.parent = self
                            self._children_name_map["rpf"] = "rpf"
                            self._children_yang_names.add("rpf")

                            self.multicast_group = YList(self)
                            self.secondary_address = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("direct_broadcast",
                                            "flow_tag_dst",
                                            "flow_tag_src",
                                            "line_state",
                                            "mask_reply",
                                            "mlacp_active",
                                            "mtu",
                                            "prefix_length",
                                            "primary_address",
                                            "proxy_arp_disabled",
                                            "redirect",
                                            "rg_id_exists",
                                            "route_tag",
                                            "unnumbered_interface_name",
                                            "unreachable",
                                            "vrf_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail, self).__setattr__(name, value)


                        class Acl(Entity):
                            """
                            ACLs configured on the interface
                            
                            .. attribute:: common_in_bound
                            
                            	Common ACL applied to incoming packets
                            	**type**\:  str
                            
                            .. attribute:: common_out_bound
                            
                            	Common ACL applied to outgoing packets
                            	**type**\:  str
                            
                            .. attribute:: inbound
                            
                            	ACL applied to incoming packets
                            	**type**\:  str
                            
                            .. attribute:: outbound
                            
                            	ACL applied to outgoing packets
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl, self).__init__()

                                self.yang_name = "acl"
                                self.yang_parent_name = "detail"

                                self.common_in_bound = YLeaf(YType.str, "common-in-bound")

                                self.common_out_bound = YLeaf(YType.str, "common-out-bound")

                                self.inbound = YLeaf(YType.str, "inbound")

                                self.outbound = YLeaf(YType.str, "outbound")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("common_in_bound",
                                                "common_out_bound",
                                                "inbound",
                                                "outbound") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.common_in_bound.is_set or
                                    self.common_out_bound.is_set or
                                    self.inbound.is_set or
                                    self.outbound.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.common_in_bound.yfilter != YFilter.not_set or
                                    self.common_out_bound.yfilter != YFilter.not_set or
                                    self.inbound.yfilter != YFilter.not_set or
                                    self.outbound.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "acl" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.common_in_bound.is_set or self.common_in_bound.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.common_in_bound.get_name_leafdata())
                                if (self.common_out_bound.is_set or self.common_out_bound.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.common_out_bound.get_name_leafdata())
                                if (self.inbound.is_set or self.inbound.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inbound.get_name_leafdata())
                                if (self.outbound.is_set or self.outbound.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.outbound.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "common-in-bound" or name == "common-out-bound" or name == "inbound" or name == "outbound"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "common-in-bound"):
                                    self.common_in_bound = value
                                    self.common_in_bound.value_namespace = name_space
                                    self.common_in_bound.value_namespace_prefix = name_space_prefix
                                if(value_path == "common-out-bound"):
                                    self.common_out_bound = value
                                    self.common_out_bound.value_namespace = name_space
                                    self.common_out_bound.value_namespace_prefix = name_space_prefix
                                if(value_path == "inbound"):
                                    self.inbound = value
                                    self.inbound.value_namespace = name_space
                                    self.inbound.value_namespace_prefix = name_space_prefix
                                if(value_path == "outbound"):
                                    self.outbound = value
                                    self.outbound.value_namespace = name_space
                                    self.outbound.value_namespace_prefix = name_space_prefix


                        class MultiAcl(Entity):
                            """
                            Multi ACLs configured on the interface
                            
                            .. attribute:: common
                            
                            	Common ACLs
                            	**type**\:  list of str
                            
                            .. attribute:: inbound
                            
                            	Inbound ACLs
                            	**type**\:  list of str
                            
                            .. attribute:: outbound
                            
                            	Outbound ACLs
                            	**type**\:  list of str
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl, self).__init__()

                                self.yang_name = "multi-acl"
                                self.yang_parent_name = "detail"

                                self.common = YLeafList(YType.str, "common")

                                self.inbound = YLeafList(YType.str, "inbound")

                                self.outbound = YLeafList(YType.str, "outbound")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("common",
                                                "inbound",
                                                "outbound") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.common.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                for leaf in self.inbound.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                for leaf in self.outbound.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.common.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                for leaf in self.inbound.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                for leaf in self.outbound.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.common.yfilter != YFilter.not_set or
                                    self.inbound.yfilter != YFilter.not_set or
                                    self.outbound.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "multi-acl" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.common.get_name_leafdata())

                                leaf_name_data.extend(self.inbound.get_name_leafdata())

                                leaf_name_data.extend(self.outbound.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "common" or name == "inbound" or name == "outbound"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "common"):
                                    self.common.append(value)
                                if(value_path == "inbound"):
                                    self.inbound.append(value)
                                if(value_path == "outbound"):
                                    self.outbound.append(value)


                        class HelperAddress(Entity):
                            """
                            Helper Addresses configured on the interface
                            
                            .. attribute:: address_array
                            
                            	Helper address
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress, self).__init__()

                                self.yang_name = "helper-address"
                                self.yang_parent_name = "detail"

                                self.address_array = YLeafList(YType.str, "address-array")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("address_array") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.address_array.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.address_array.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.address_array.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "helper-address" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.address_array.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "address-array"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "address-array"):
                                    self.address_array.append(value)


                        class Rpf(Entity):
                            """
                            RPF config on the interface
                            
                            .. attribute:: allow_default_route
                            
                            	Allow Default Route
                            	**type**\:  bool
                            
                            .. attribute:: allow_self_ping
                            
                            	Allow Self Ping
                            	**type**\:  bool
                            
                            .. attribute:: enable
                            
                            	Enable RPF config
                            	**type**\:  bool
                            
                            .. attribute:: mode
                            
                            	RPF Mode (loose/strict)
                            	**type**\:   :py:class:`RpfMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.RpfMode>`
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf, self).__init__()

                                self.yang_name = "rpf"
                                self.yang_parent_name = "detail"

                                self.allow_default_route = YLeaf(YType.boolean, "allow-default-route")

                                self.allow_self_ping = YLeaf(YType.boolean, "allow-self-ping")

                                self.enable = YLeaf(YType.boolean, "enable")

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
                                    if name in ("allow_default_route",
                                                "allow_self_ping",
                                                "enable",
                                                "mode") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.allow_default_route.is_set or
                                    self.allow_self_ping.is_set or
                                    self.enable.is_set or
                                    self.mode.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.allow_default_route.yfilter != YFilter.not_set or
                                    self.allow_self_ping.yfilter != YFilter.not_set or
                                    self.enable.yfilter != YFilter.not_set or
                                    self.mode.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "rpf" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.allow_default_route.is_set or self.allow_default_route.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.allow_default_route.get_name_leafdata())
                                if (self.allow_self_ping.is_set or self.allow_self_ping.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.allow_self_ping.get_name_leafdata())
                                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enable.get_name_leafdata())
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
                                if(name == "allow-default-route" or name == "allow-self-ping" or name == "enable" or name == "mode"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "allow-default-route"):
                                    self.allow_default_route = value
                                    self.allow_default_route.value_namespace = name_space
                                    self.allow_default_route.value_namespace_prefix = name_space_prefix
                                if(value_path == "allow-self-ping"):
                                    self.allow_self_ping = value
                                    self.allow_self_ping.value_namespace = name_space
                                    self.allow_self_ping.value_namespace_prefix = name_space_prefix
                                if(value_path == "enable"):
                                    self.enable = value
                                    self.enable.value_namespace = name_space
                                    self.enable.value_namespace_prefix = name_space_prefix
                                if(value_path == "mode"):
                                    self.mode = value
                                    self.mode.value_namespace = name_space
                                    self.mode.value_namespace_prefix = name_space_prefix


                        class BgpPa(Entity):
                            """
                            BGP PA config on the interface
                            
                            .. attribute:: input
                            
                            	BGP PA input config
                            	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input>`
                            
                            .. attribute:: output
                            
                            	BGP PA output config
                            	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper.Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output>`
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa, self).__init__()

                                self.yang_name = "bgp-pa"
                                self.yang_parent_name = "detail"

                                self.input = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input()
                                self.input.parent = self
                                self._children_name_map["input"] = "input"
                                self._children_yang_names.add("input")

                                self.output = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output()
                                self.output.parent = self
                                self._children_name_map["output"] = "output"
                                self._children_yang_names.add("output")


                            class Input(Entity):
                                """
                                BGP PA input config
                                
                                .. attribute:: destination
                                
                                	Enable destination accouting
                                	**type**\:  bool
                                
                                .. attribute:: enable
                                
                                	Enable BGP PA for ingress/egress
                                	**type**\:  bool
                                
                                .. attribute:: source
                                
                                	Enable source accouting
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'ipv4-ma-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input, self).__init__()

                                    self.yang_name = "input"
                                    self.yang_parent_name = "bgp-pa"

                                    self.destination = YLeaf(YType.boolean, "destination")

                                    self.enable = YLeaf(YType.boolean, "enable")

                                    self.source = YLeaf(YType.boolean, "source")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("destination",
                                                    "enable",
                                                    "source") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.destination.is_set or
                                        self.enable.is_set or
                                        self.source.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.destination.yfilter != YFilter.not_set or
                                        self.enable.yfilter != YFilter.not_set or
                                        self.source.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "input" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.destination.get_name_leafdata())
                                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enable.get_name_leafdata())
                                    if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.source.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "destination" or name == "enable" or name == "source"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "destination"):
                                        self.destination = value
                                        self.destination.value_namespace = name_space
                                        self.destination.value_namespace_prefix = name_space_prefix
                                    if(value_path == "enable"):
                                        self.enable = value
                                        self.enable.value_namespace = name_space
                                        self.enable.value_namespace_prefix = name_space_prefix
                                    if(value_path == "source"):
                                        self.source = value
                                        self.source.value_namespace = name_space
                                        self.source.value_namespace_prefix = name_space_prefix


                            class Output(Entity):
                                """
                                BGP PA output config
                                
                                .. attribute:: destination
                                
                                	Enable destination accouting
                                	**type**\:  bool
                                
                                .. attribute:: enable
                                
                                	Enable BGP PA for ingress/egress
                                	**type**\:  bool
                                
                                .. attribute:: source
                                
                                	Enable source accouting
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'ipv4-ma-oper'
                                _revision = '2015-10-20'

                                def __init__(self):
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output, self).__init__()

                                    self.yang_name = "output"
                                    self.yang_parent_name = "bgp-pa"

                                    self.destination = YLeaf(YType.boolean, "destination")

                                    self.enable = YLeaf(YType.boolean, "enable")

                                    self.source = YLeaf(YType.boolean, "source")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("destination",
                                                    "enable",
                                                    "source") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.destination.is_set or
                                        self.enable.is_set or
                                        self.source.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.destination.yfilter != YFilter.not_set or
                                        self.enable.yfilter != YFilter.not_set or
                                        self.source.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "output" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.destination.get_name_leafdata())
                                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enable.get_name_leafdata())
                                    if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.source.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "destination" or name == "enable" or name == "source"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "destination"):
                                        self.destination = value
                                        self.destination.value_namespace = name_space
                                        self.destination.value_namespace_prefix = name_space_prefix
                                    if(value_path == "enable"):
                                        self.enable = value
                                        self.enable.value_namespace = name_space
                                        self.enable.value_namespace_prefix = name_space_prefix
                                    if(value_path == "source"):
                                        self.source = value
                                        self.source.value_namespace = name_space
                                        self.source.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    (self.input is not None and self.input.has_data()) or
                                    (self.output is not None and self.output.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.input is not None and self.input.has_operation()) or
                                    (self.output is not None and self.output.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bgp-pa" + path_buffer

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

                                if (child_yang_name == "input"):
                                    if (self.input is None):
                                        self.input = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input()
                                        self.input.parent = self
                                        self._children_name_map["input"] = "input"
                                    return self.input

                                if (child_yang_name == "output"):
                                    if (self.output is None):
                                        self.output = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output()
                                        self.output.parent = self
                                        self._children_name_map["output"] = "output"
                                    return self.output

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "input" or name == "output"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class PubUtime(Entity):
                            """
                            Address Publish Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime, self).__init__()

                                self.yang_name = "pub-utime"
                                self.yang_parent_name = "detail"

                            def has_data(self):
                                return False

                            def has_operation(self):
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pub-utime" + path_buffer

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

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class IdbUtime(Entity):
                            """
                            IDB Create Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime, self).__init__()

                                self.yang_name = "idb-utime"
                                self.yang_parent_name = "detail"

                            def has_data(self):
                                return False

                            def has_operation(self):
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "idb-utime" + path_buffer

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

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class CapsUtime(Entity):
                            """
                            CAPS Add Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime, self).__init__()

                                self.yang_name = "caps-utime"
                                self.yang_parent_name = "detail"

                            def has_data(self):
                                return False

                            def has_operation(self):
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "caps-utime" + path_buffer

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

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class FwdEnUtime(Entity):
                            """
                            FWD ENABLE Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime, self).__init__()

                                self.yang_name = "fwd-en-utime"
                                self.yang_parent_name = "detail"

                            def has_data(self):
                                return False

                            def has_operation(self):
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "fwd-en-utime" + path_buffer

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

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class FwdDisUtime(Entity):
                            """
                            FWD DISABLE Time
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime, self).__init__()

                                self.yang_name = "fwd-dis-utime"
                                self.yang_parent_name = "detail"

                            def has_data(self):
                                return False

                            def has_operation(self):
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "fwd-dis-utime" + path_buffer

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

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class MulticastGroup(Entity):
                            """
                            Multicast groups joined on the interface
                            
                            .. attribute:: group_address
                            
                            	Address of multicast group
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup, self).__init__()

                                self.yang_name = "multicast-group"
                                self.yang_parent_name = "detail"

                                self.group_address = YLeaf(YType.str, "group-address")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_address") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup, self).__setattr__(name, value)

                            def has_data(self):
                                return self.group_address.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_address.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "multicast-group" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_address.is_set or self.group_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_address.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-address"):
                                    self.group_address = value
                                    self.group_address.value_namespace = name_space
                                    self.group_address.value_namespace_prefix = name_space_prefix


                        class SecondaryAddress(Entity):
                            """
                            Secondary addresses on the interface
                            
                            .. attribute:: address
                            
                            	Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length of address
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: route_tag
                            
                            	Route Tag associated with this address (0 = no tag)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv4-ma-oper'
                            _revision = '2015-10-20'

                            def __init__(self):
                                super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress, self).__init__()

                                self.yang_name = "secondary-address"
                                self.yang_parent_name = "detail"

                                self.address = YLeaf(YType.str, "address")

                                self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                self.route_tag = YLeaf(YType.uint32, "route-tag")

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
                                                "prefix_length",
                                                "route_tag") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.address.is_set or
                                    self.prefix_length.is_set or
                                    self.route_tag.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.address.yfilter != YFilter.not_set or
                                    self.prefix_length.yfilter != YFilter.not_set or
                                    self.route_tag.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "secondary-address" + path_buffer

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
                                if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_length.get_name_leafdata())
                                if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.route_tag.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "address" or name == "prefix-length" or name == "route-tag"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "address"):
                                    self.address = value
                                    self.address.value_namespace = name_space
                                    self.address.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-length"):
                                    self.prefix_length = value
                                    self.prefix_length.value_namespace = name_space
                                    self.prefix_length.value_namespace_prefix = name_space_prefix
                                if(value_path == "route-tag"):
                                    self.route_tag = value
                                    self.route_tag.value_namespace = name_space
                                    self.route_tag.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.multicast_group:
                                if (c.has_data()):
                                    return True
                            for c in self.secondary_address:
                                if (c.has_data()):
                                    return True
                            return (
                                self.direct_broadcast.is_set or
                                self.flow_tag_dst.is_set or
                                self.flow_tag_src.is_set or
                                self.line_state.is_set or
                                self.mask_reply.is_set or
                                self.mlacp_active.is_set or
                                self.mtu.is_set or
                                self.prefix_length.is_set or
                                self.primary_address.is_set or
                                self.proxy_arp_disabled.is_set or
                                self.redirect.is_set or
                                self.rg_id_exists.is_set or
                                self.route_tag.is_set or
                                self.unnumbered_interface_name.is_set or
                                self.unreachable.is_set or
                                self.vrf_id.is_set or
                                (self.acl is not None and self.acl.has_data()) or
                                (self.bgp_pa is not None and self.bgp_pa.has_data()) or
                                (self.caps_utime is not None and self.caps_utime.has_data()) or
                                (self.fwd_dis_utime is not None and self.fwd_dis_utime.has_data()) or
                                (self.fwd_en_utime is not None and self.fwd_en_utime.has_data()) or
                                (self.helper_address is not None and self.helper_address.has_data()) or
                                (self.idb_utime is not None and self.idb_utime.has_data()) or
                                (self.multi_acl is not None and self.multi_acl.has_data()) or
                                (self.pub_utime is not None and self.pub_utime.has_data()) or
                                (self.rpf is not None and self.rpf.has_data()))

                        def has_operation(self):
                            for c in self.multicast_group:
                                if (c.has_operation()):
                                    return True
                            for c in self.secondary_address:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.direct_broadcast.yfilter != YFilter.not_set or
                                self.flow_tag_dst.yfilter != YFilter.not_set or
                                self.flow_tag_src.yfilter != YFilter.not_set or
                                self.line_state.yfilter != YFilter.not_set or
                                self.mask_reply.yfilter != YFilter.not_set or
                                self.mlacp_active.yfilter != YFilter.not_set or
                                self.mtu.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set or
                                self.primary_address.yfilter != YFilter.not_set or
                                self.proxy_arp_disabled.yfilter != YFilter.not_set or
                                self.redirect.yfilter != YFilter.not_set or
                                self.rg_id_exists.yfilter != YFilter.not_set or
                                self.route_tag.yfilter != YFilter.not_set or
                                self.unnumbered_interface_name.yfilter != YFilter.not_set or
                                self.unreachable.yfilter != YFilter.not_set or
                                self.vrf_id.yfilter != YFilter.not_set or
                                (self.acl is not None and self.acl.has_operation()) or
                                (self.bgp_pa is not None and self.bgp_pa.has_operation()) or
                                (self.caps_utime is not None and self.caps_utime.has_operation()) or
                                (self.fwd_dis_utime is not None and self.fwd_dis_utime.has_operation()) or
                                (self.fwd_en_utime is not None and self.fwd_en_utime.has_operation()) or
                                (self.helper_address is not None and self.helper_address.has_operation()) or
                                (self.idb_utime is not None and self.idb_utime.has_operation()) or
                                (self.multi_acl is not None and self.multi_acl.has_operation()) or
                                (self.pub_utime is not None and self.pub_utime.has_operation()) or
                                (self.rpf is not None and self.rpf.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "detail" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.direct_broadcast.is_set or self.direct_broadcast.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.direct_broadcast.get_name_leafdata())
                            if (self.flow_tag_dst.is_set or self.flow_tag_dst.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_tag_dst.get_name_leafdata())
                            if (self.flow_tag_src.is_set or self.flow_tag_src.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_tag_src.get_name_leafdata())
                            if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.line_state.get_name_leafdata())
                            if (self.mask_reply.is_set or self.mask_reply.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mask_reply.get_name_leafdata())
                            if (self.mlacp_active.is_set or self.mlacp_active.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mlacp_active.get_name_leafdata())
                            if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mtu.get_name_leafdata())
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())
                            if (self.primary_address.is_set or self.primary_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.primary_address.get_name_leafdata())
                            if (self.proxy_arp_disabled.is_set or self.proxy_arp_disabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.proxy_arp_disabled.get_name_leafdata())
                            if (self.redirect.is_set or self.redirect.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.redirect.get_name_leafdata())
                            if (self.rg_id_exists.is_set or self.rg_id_exists.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rg_id_exists.get_name_leafdata())
                            if (self.route_tag.is_set or self.route_tag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.route_tag.get_name_leafdata())
                            if (self.unnumbered_interface_name.is_set or self.unnumbered_interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unnumbered_interface_name.get_name_leafdata())
                            if (self.unreachable.is_set or self.unreachable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unreachable.get_name_leafdata())
                            if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "acl"):
                                if (self.acl is None):
                                    self.acl = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl()
                                    self.acl.parent = self
                                    self._children_name_map["acl"] = "acl"
                                return self.acl

                            if (child_yang_name == "bgp-pa"):
                                if (self.bgp_pa is None):
                                    self.bgp_pa = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa()
                                    self.bgp_pa.parent = self
                                    self._children_name_map["bgp_pa"] = "bgp-pa"
                                return self.bgp_pa

                            if (child_yang_name == "caps-utime"):
                                if (self.caps_utime is None):
                                    self.caps_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime()
                                    self.caps_utime.parent = self
                                    self._children_name_map["caps_utime"] = "caps-utime"
                                return self.caps_utime

                            if (child_yang_name == "fwd-dis-utime"):
                                if (self.fwd_dis_utime is None):
                                    self.fwd_dis_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime()
                                    self.fwd_dis_utime.parent = self
                                    self._children_name_map["fwd_dis_utime"] = "fwd-dis-utime"
                                return self.fwd_dis_utime

                            if (child_yang_name == "fwd-en-utime"):
                                if (self.fwd_en_utime is None):
                                    self.fwd_en_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime()
                                    self.fwd_en_utime.parent = self
                                    self._children_name_map["fwd_en_utime"] = "fwd-en-utime"
                                return self.fwd_en_utime

                            if (child_yang_name == "helper-address"):
                                if (self.helper_address is None):
                                    self.helper_address = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress()
                                    self.helper_address.parent = self
                                    self._children_name_map["helper_address"] = "helper-address"
                                return self.helper_address

                            if (child_yang_name == "idb-utime"):
                                if (self.idb_utime is None):
                                    self.idb_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime()
                                    self.idb_utime.parent = self
                                    self._children_name_map["idb_utime"] = "idb-utime"
                                return self.idb_utime

                            if (child_yang_name == "multi-acl"):
                                if (self.multi_acl is None):
                                    self.multi_acl = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl()
                                    self.multi_acl.parent = self
                                    self._children_name_map["multi_acl"] = "multi-acl"
                                return self.multi_acl

                            if (child_yang_name == "multicast-group"):
                                for c in self.multicast_group:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.multicast_group.append(c)
                                return c

                            if (child_yang_name == "pub-utime"):
                                if (self.pub_utime is None):
                                    self.pub_utime = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime()
                                    self.pub_utime.parent = self
                                    self._children_name_map["pub_utime"] = "pub-utime"
                                return self.pub_utime

                            if (child_yang_name == "rpf"):
                                if (self.rpf is None):
                                    self.rpf = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf()
                                    self.rpf.parent = self
                                    self._children_name_map["rpf"] = "rpf"
                                return self.rpf

                            if (child_yang_name == "secondary-address"):
                                for c in self.secondary_address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.secondary_address.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "acl" or name == "bgp-pa" or name == "caps-utime" or name == "fwd-dis-utime" or name == "fwd-en-utime" or name == "helper-address" or name == "idb-utime" or name == "multi-acl" or name == "multicast-group" or name == "pub-utime" or name == "rpf" or name == "secondary-address" or name == "direct-broadcast" or name == "flow-tag-dst" or name == "flow-tag-src" or name == "line-state" or name == "mask-reply" or name == "mlacp-active" or name == "mtu" or name == "prefix-length" or name == "primary-address" or name == "proxy-arp-disabled" or name == "redirect" or name == "rg-id-exists" or name == "route-tag" or name == "unnumbered-interface-name" or name == "unreachable" or name == "vrf-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "direct-broadcast"):
                                self.direct_broadcast = value
                                self.direct_broadcast.value_namespace = name_space
                                self.direct_broadcast.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-tag-dst"):
                                self.flow_tag_dst = value
                                self.flow_tag_dst.value_namespace = name_space
                                self.flow_tag_dst.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-tag-src"):
                                self.flow_tag_src = value
                                self.flow_tag_src.value_namespace = name_space
                                self.flow_tag_src.value_namespace_prefix = name_space_prefix
                            if(value_path == "line-state"):
                                self.line_state = value
                                self.line_state.value_namespace = name_space
                                self.line_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "mask-reply"):
                                self.mask_reply = value
                                self.mask_reply.value_namespace = name_space
                                self.mask_reply.value_namespace_prefix = name_space_prefix
                            if(value_path == "mlacp-active"):
                                self.mlacp_active = value
                                self.mlacp_active.value_namespace = name_space
                                self.mlacp_active.value_namespace_prefix = name_space_prefix
                            if(value_path == "mtu"):
                                self.mtu = value
                                self.mtu.value_namespace = name_space
                                self.mtu.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "primary-address"):
                                self.primary_address = value
                                self.primary_address.value_namespace = name_space
                                self.primary_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "proxy-arp-disabled"):
                                self.proxy_arp_disabled = value
                                self.proxy_arp_disabled.value_namespace = name_space
                                self.proxy_arp_disabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "redirect"):
                                self.redirect = value
                                self.redirect.value_namespace = name_space
                                self.redirect.value_namespace_prefix = name_space_prefix
                            if(value_path == "rg-id-exists"):
                                self.rg_id_exists = value
                                self.rg_id_exists.value_namespace = name_space
                                self.rg_id_exists.value_namespace_prefix = name_space_prefix
                            if(value_path == "route-tag"):
                                self.route_tag = value
                                self.route_tag.value_namespace = name_space
                                self.route_tag.value_namespace_prefix = name_space_prefix
                            if(value_path == "unnumbered-interface-name"):
                                self.unnumbered_interface_name = value
                                self.unnumbered_interface_name.value_namespace = name_space
                                self.unnumbered_interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "unreachable"):
                                self.unreachable = value
                                self.unreachable.value_namespace = name_space
                                self.unreachable.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-id"):
                                self.vrf_id = value
                                self.vrf_id.value_namespace = name_space
                                self.vrf_id.value_namespace_prefix = name_space_prefix


                    class Brief(Entity):
                        """
                        Brief IPv4 network operational data for an
                        interface
                        
                        .. attribute:: line_state
                        
                        	Line state of the interface
                        	**type**\:   :py:class:`Ipv4MaOperLineState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper.Ipv4MaOperLineState>`
                        
                        .. attribute:: primary_address
                        
                        	Primary address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID of the interface
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv4-ma-oper'
                        _revision = '2015-10-20'

                        def __init__(self):
                            super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief, self).__init__()

                            self.yang_name = "brief"
                            self.yang_parent_name = "vrf"

                            self.line_state = YLeaf(YType.enumeration, "line-state")

                            self.primary_address = YLeaf(YType.str, "primary-address")

                            self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("line_state",
                                            "primary_address",
                                            "vrf_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.line_state.is_set or
                                self.primary_address.is_set or
                                self.vrf_id.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.line_state.yfilter != YFilter.not_set or
                                self.primary_address.yfilter != YFilter.not_set or
                                self.vrf_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "brief" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.line_state.is_set or self.line_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.line_state.get_name_leafdata())
                            if (self.primary_address.is_set or self.primary_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.primary_address.get_name_leafdata())
                            if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "line-state" or name == "primary-address" or name == "vrf-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "line-state"):
                                self.line_state = value
                                self.line_state.value_namespace = name_space
                                self.line_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "primary-address"):
                                self.primary_address = value
                                self.primary_address.value_namespace = name_space
                                self.primary_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-id"):
                                self.vrf_id = value
                                self.vrf_id.value_namespace = name_space
                                self.vrf_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.vrf_name.is_set or
                            (self.brief is not None and self.brief.has_data()) or
                            (self.detail is not None and self.detail.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            (self.brief is not None and self.brief.has_operation()) or
                            (self.detail is not None and self.detail.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                        if (child_yang_name == "brief"):
                            if (self.brief is None):
                                self.brief = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief()
                                self.brief.parent = self
                                self._children_name_map["brief"] = "brief"
                            return self.brief

                        if (child_yang_name == "detail"):
                            if (self.detail is None):
                                self.detail = Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                            return self.detail

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "brief" or name == "detail" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vrf:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.vrf:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrfs" + path_buffer

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

                    if (child_yang_name == "vrf"):
                        for c in self.vrf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ipv4Network.Interfaces.Interface.Vrfs.Vrf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vrf.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    (self.vrfs is not None and self.vrfs.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    (self.vrfs is not None and self.vrfs.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/Cisco-IOS-XR-ipv4-ma-oper:interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "vrfs"):
                    if (self.vrfs is None):
                        self.vrfs = Ipv4Network.Interfaces.Interface.Vrfs()
                        self.vrfs.parent = self
                        self._children_name_map["vrfs"] = "vrfs"
                    return self.vrfs

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vrfs" or name == "interface-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix

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
            path_buffer = "Cisco-IOS-XR-ipv4-ma-oper:interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-io-oper:ipv4-network/%s" % self.get_segment_path()
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
                c = Ipv4Network.Interfaces.Interface()
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
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.nodes is not None and self.nodes.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-io-oper:ipv4-network" + path_buffer

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

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = Ipv4Network.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Ipv4Network.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "interfaces" or name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ipv4Network()
        return self._top_entity

