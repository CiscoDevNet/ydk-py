""" Cisco_IOS_XR_fretta_grid_svr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-grid\-svr package operational data.

This module contains definitions
for the following management objects\:
  grid\: GRID operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Grid(Entity):
    """
    GRID operational data
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes>`
    
    

    """

    _prefix = 'fretta-grid-svr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Grid, self).__init__()
        self._top_entity = None

        self.yang_name = "grid"
        self.yang_parent_name = "Cisco-IOS-XR-fretta-grid-svr-oper"

        self.nodes = Grid.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node>`
        
        

        """

        _prefix = 'fretta-grid-svr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grid.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "grid"

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
                        super(Grid.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Grid.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: client_xr
            
            	GRID Client Table
            	**type**\:   :py:class:`ClientXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.ClientXr>`
            
            .. attribute:: clients
            
            	GRID Client Consistency Check
            	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.Clients>`
            
            

            """

            _prefix = 'fretta-grid-svr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Grid.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.client_xr = Grid.Nodes.Node.ClientXr()
                self.client_xr.parent = self
                self._children_name_map["client_xr"] = "client-xr"
                self._children_yang_names.add("client-xr")

                self.clients = Grid.Nodes.Node.Clients()
                self.clients.parent = self
                self._children_name_map["clients"] = "clients"
                self._children_yang_names.add("clients")

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
                            super(Grid.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Grid.Nodes.Node, self).__setattr__(name, value)


            class ClientXr(Entity):
                """
                GRID Client Table
                
                .. attribute:: client
                
                	GRID Client Database
                	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.ClientXr.Client>`
                
                

                """

                _prefix = 'fretta-grid-svr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Grid.Nodes.Node.ClientXr, self).__init__()

                    self.yang_name = "client-xr"
                    self.yang_parent_name = "node"

                    self.client = YList(self)

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
                                super(Grid.Nodes.Node.ClientXr, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Grid.Nodes.Node.ClientXr, self).__setattr__(name, value)


                class Client(Entity):
                    """
                    GRID Client Database
                    
                    .. attribute:: client_name  <key>
                    
                    	Client name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: client_data
                    
                    	Client information
                    	**type**\: list of    :py:class:`ClientData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.ClientXr.Client.ClientData>`
                    
                    

                    """

                    _prefix = 'fretta-grid-svr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Grid.Nodes.Node.ClientXr.Client, self).__init__()

                        self.yang_name = "client"
                        self.yang_parent_name = "client-xr"

                        self.client_name = YLeaf(YType.str, "client-name")

                        self.client_data = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("client_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Grid.Nodes.Node.ClientXr.Client, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Grid.Nodes.Node.ClientXr.Client, self).__setattr__(name, value)


                    class ClientData(Entity):
                        """
                        Client information
                        
                        .. attribute:: res_id
                        
                        	Resource ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'fretta-grid-svr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Grid.Nodes.Node.ClientXr.Client.ClientData, self).__init__()

                            self.yang_name = "client-data"
                            self.yang_parent_name = "client"

                            self.res_id = YLeaf(YType.uint32, "res-id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("res_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Grid.Nodes.Node.ClientXr.Client.ClientData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Grid.Nodes.Node.ClientXr.Client.ClientData, self).__setattr__(name, value)

                        def has_data(self):
                            return self.res_id.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.res_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "client-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.res_id.is_set or self.res_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.res_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "res-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "res-id"):
                                self.res_id = value
                                self.res_id.value_namespace = name_space
                                self.res_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.client_data:
                            if (c.has_data()):
                                return True
                        return self.client_name.is_set

                    def has_operation(self):
                        for c in self.client_data:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.client_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "client" + "[client-name='" + self.client_name.get() + "']" + path_buffer

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

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "client-data"):
                            for c in self.client_data:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Grid.Nodes.Node.ClientXr.Client.ClientData()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.client_data.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "client-data" or name == "client-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "client-name"):
                            self.client_name = value
                            self.client_name.value_namespace = name_space
                            self.client_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.client:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.client:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "client-xr" + path_buffer

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

                    if (child_yang_name == "client"):
                        for c in self.client:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Grid.Nodes.Node.ClientXr.Client()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.client.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "client"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Clients(Entity):
                """
                GRID Client Consistency Check
                
                .. attribute:: client
                
                	GRID Client Consistency Check
                	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.Clients.Client>`
                
                

                """

                _prefix = 'fretta-grid-svr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Grid.Nodes.Node.Clients, self).__init__()

                    self.yang_name = "clients"
                    self.yang_parent_name = "node"

                    self.client = YList(self)

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
                                super(Grid.Nodes.Node.Clients, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Grid.Nodes.Node.Clients, self).__setattr__(name, value)


                class Client(Entity):
                    """
                    GRID Client Consistency Check
                    
                    .. attribute:: client_name  <key>
                    
                    	Client name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: client_data
                    
                    	Client information
                    	**type**\: list of    :py:class:`ClientData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.Clients.Client.ClientData>`
                    
                    

                    """

                    _prefix = 'fretta-grid-svr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Grid.Nodes.Node.Clients.Client, self).__init__()

                        self.yang_name = "client"
                        self.yang_parent_name = "clients"

                        self.client_name = YLeaf(YType.str, "client-name")

                        self.client_data = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("client_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Grid.Nodes.Node.Clients.Client, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Grid.Nodes.Node.Clients.Client, self).__setattr__(name, value)


                    class ClientData(Entity):
                        """
                        Client information
                        
                        .. attribute:: res_id
                        
                        	Resource ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'fretta-grid-svr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Grid.Nodes.Node.Clients.Client.ClientData, self).__init__()

                            self.yang_name = "client-data"
                            self.yang_parent_name = "client"

                            self.res_id = YLeaf(YType.uint32, "res-id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("res_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Grid.Nodes.Node.Clients.Client.ClientData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Grid.Nodes.Node.Clients.Client.ClientData, self).__setattr__(name, value)

                        def has_data(self):
                            return self.res_id.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.res_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "client-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.res_id.is_set or self.res_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.res_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "res-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "res-id"):
                                self.res_id = value
                                self.res_id.value_namespace = name_space
                                self.res_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.client_data:
                            if (c.has_data()):
                                return True
                        return self.client_name.is_set

                    def has_operation(self):
                        for c in self.client_data:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.client_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "client" + "[client-name='" + self.client_name.get() + "']" + path_buffer

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

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "client-data"):
                            for c in self.client_data:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Grid.Nodes.Node.Clients.Client.ClientData()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.client_data.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "client-data" or name == "client-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "client-name"):
                            self.client_name = value
                            self.client_name.value_namespace = name_space
                            self.client_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.client:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.client:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "clients" + path_buffer

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

                    if (child_yang_name == "client"):
                        for c in self.client:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Grid.Nodes.Node.Clients.Client()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.client.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "client"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.client_xr is not None and self.client_xr.has_data()) or
                    (self.clients is not None and self.clients.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.client_xr is not None and self.client_xr.has_operation()) or
                    (self.clients is not None and self.clients.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-fretta-grid-svr-oper:grid/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "client-xr"):
                    if (self.client_xr is None):
                        self.client_xr = Grid.Nodes.Node.ClientXr()
                        self.client_xr.parent = self
                        self._children_name_map["client_xr"] = "client-xr"
                    return self.client_xr

                if (child_yang_name == "clients"):
                    if (self.clients is None):
                        self.clients = Grid.Nodes.Node.Clients()
                        self.clients.parent = self
                        self._children_name_map["clients"] = "clients"
                    return self.clients

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "client-xr" or name == "clients" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-fretta-grid-svr-oper:grid/%s" % self.get_segment_path()
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
                c = Grid.Nodes.Node()
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

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-fretta-grid-svr-oper:grid" + path_buffer

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

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Grid.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Grid()
        return self._top_entity

