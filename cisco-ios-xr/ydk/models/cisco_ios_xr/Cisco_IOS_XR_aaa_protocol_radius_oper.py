""" Cisco_IOS_XR_aaa_protocol_radius_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-protocol\-radius package operational data.

This module contains definitions
for the following management objects\:
  radius\: RADIUS operational data

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-locald\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Radius(Entity):
    """
    RADIUS operational data
    
    .. attribute:: nodes
    
    	Contains all the nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes>`
    
    

    """

    _prefix = 'aaa-protocol-radius-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Radius, self).__init__()
        self._top_entity = None

        self.yang_name = "radius"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-protocol-radius-oper"

        self.nodes = Radius.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Contains all the nodes
        
        .. attribute:: node
        
        	RADIUS operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node>`
        
        

        """

        _prefix = 'aaa-protocol-radius-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Radius.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "radius"

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
                        super(Radius.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Radius.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            RADIUS operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: accounting
            
            	RADIUS accounting data
            	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Accounting>`
            
            .. attribute:: authentication
            
            	RADIUS authentication data
            	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Authentication>`
            
            .. attribute:: client
            
            	RADIUS client data
            	**type**\:   :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Client>`
            
            .. attribute:: dead_criteria
            
            	RADIUS dead criteria information
            	**type**\:   :py:class:`DeadCriteria <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria>`
            
            .. attribute:: dynamic_authorization
            
            	Dynamic authorization data
            	**type**\:   :py:class:`DynamicAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DynamicAuthorization>`
            
            .. attribute:: server_groups
            
            	RADIUS server group table
            	**type**\:   :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups>`
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Radius.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.accounting = Radius.Nodes.Node.Accounting()
                self.accounting.parent = self
                self._children_name_map["accounting"] = "accounting"
                self._children_yang_names.add("accounting")

                self.authentication = Radius.Nodes.Node.Authentication()
                self.authentication.parent = self
                self._children_name_map["authentication"] = "authentication"
                self._children_yang_names.add("authentication")

                self.client = Radius.Nodes.Node.Client()
                self.client.parent = self
                self._children_name_map["client"] = "client"
                self._children_yang_names.add("client")

                self.dead_criteria = Radius.Nodes.Node.DeadCriteria()
                self.dead_criteria.parent = self
                self._children_name_map["dead_criteria"] = "dead-criteria"
                self._children_yang_names.add("dead-criteria")

                self.dynamic_authorization = Radius.Nodes.Node.DynamicAuthorization()
                self.dynamic_authorization.parent = self
                self._children_name_map["dynamic_authorization"] = "dynamic-authorization"
                self._children_yang_names.add("dynamic-authorization")

                self.server_groups = Radius.Nodes.Node.ServerGroups()
                self.server_groups.parent = self
                self._children_name_map["server_groups"] = "server-groups"
                self._children_yang_names.add("server-groups")

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
                            super(Radius.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Radius.Nodes.Node, self).__setattr__(name, value)


            class Client(Entity):
                """
                RADIUS client data
                
                .. attribute:: authentication_nas_id
                
                	NAS\-Identifier of the RADIUS authentication client
                	**type**\:  str
                
                .. attribute:: unknown_accounting_responses
                
                	Number of RADIUS accounting responses packets received from unknown addresses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_authentication_responses
                
                	Number of RADIUS access responses packets received from unknown addresses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Radius.Nodes.Node.Client, self).__init__()

                    self.yang_name = "client"
                    self.yang_parent_name = "node"

                    self.authentication_nas_id = YLeaf(YType.str, "authentication-nas-id")

                    self.unknown_accounting_responses = YLeaf(YType.uint32, "unknown-accounting-responses")

                    self.unknown_authentication_responses = YLeaf(YType.uint32, "unknown-authentication-responses")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("authentication_nas_id",
                                    "unknown_accounting_responses",
                                    "unknown_authentication_responses") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Radius.Nodes.Node.Client, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Radius.Nodes.Node.Client, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.authentication_nas_id.is_set or
                        self.unknown_accounting_responses.is_set or
                        self.unknown_authentication_responses.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.authentication_nas_id.yfilter != YFilter.not_set or
                        self.unknown_accounting_responses.yfilter != YFilter.not_set or
                        self.unknown_authentication_responses.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "client" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.authentication_nas_id.is_set or self.authentication_nas_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_nas_id.get_name_leafdata())
                    if (self.unknown_accounting_responses.is_set or self.unknown_accounting_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unknown_accounting_responses.get_name_leafdata())
                    if (self.unknown_authentication_responses.is_set or self.unknown_authentication_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unknown_authentication_responses.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "authentication-nas-id" or name == "unknown-accounting-responses" or name == "unknown-authentication-responses"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "authentication-nas-id"):
                        self.authentication_nas_id = value
                        self.authentication_nas_id.value_namespace = name_space
                        self.authentication_nas_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "unknown-accounting-responses"):
                        self.unknown_accounting_responses = value
                        self.unknown_accounting_responses.value_namespace = name_space
                        self.unknown_accounting_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "unknown-authentication-responses"):
                        self.unknown_authentication_responses = value
                        self.unknown_authentication_responses.value_namespace = name_space
                        self.unknown_authentication_responses.value_namespace_prefix = name_space_prefix


            class DeadCriteria(Entity):
                """
                RADIUS dead criteria information
                
                .. attribute:: hosts
                
                	RADIUS server dead criteria host table
                	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Radius.Nodes.Node.DeadCriteria, self).__init__()

                    self.yang_name = "dead-criteria"
                    self.yang_parent_name = "node"

                    self.hosts = Radius.Nodes.Node.DeadCriteria.Hosts()
                    self.hosts.parent = self
                    self._children_name_map["hosts"] = "hosts"
                    self._children_yang_names.add("hosts")


                class Hosts(Entity):
                    """
                    RADIUS server dead criteria host table
                    
                    .. attribute:: host
                    
                    	RADIUS Server
                    	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts.Host>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Radius.Nodes.Node.DeadCriteria.Hosts, self).__init__()

                        self.yang_name = "hosts"
                        self.yang_parent_name = "dead-criteria"

                        self.host = YList(self)

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
                                    super(Radius.Nodes.Node.DeadCriteria.Hosts, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Radius.Nodes.Node.DeadCriteria.Hosts, self).__setattr__(name, value)


                    class Host(Entity):
                        """
                        RADIUS Server
                        
                        .. attribute:: acct_port_number
                        
                        	Accounting Port number (standard port 1646)
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: auth_port_number
                        
                        	Authentication Port number (standard port 1645)
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: ip_address
                        
                        	IP address of RADIUS server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: time
                        
                        	Time in seconds
                        	**type**\:   :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time>`
                        
                        .. attribute:: tries
                        
                        	Number of tries
                        	**type**\:   :py:class:`Tries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries>`
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Radius.Nodes.Node.DeadCriteria.Hosts.Host, self).__init__()

                            self.yang_name = "host"
                            self.yang_parent_name = "hosts"

                            self.acct_port_number = YLeaf(YType.uint32, "acct-port-number")

                            self.auth_port_number = YLeaf(YType.uint32, "auth-port-number")

                            self.ip_address = YLeaf(YType.str, "ip-address")

                            self.time = Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time()
                            self.time.parent = self
                            self._children_name_map["time"] = "time"
                            self._children_yang_names.add("time")

                            self.tries = Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries()
                            self.tries.parent = self
                            self._children_name_map["tries"] = "tries"
                            self._children_yang_names.add("tries")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("acct_port_number",
                                            "auth_port_number",
                                            "ip_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Radius.Nodes.Node.DeadCriteria.Hosts.Host, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Radius.Nodes.Node.DeadCriteria.Hosts.Host, self).__setattr__(name, value)


                        class Time(Entity):
                            """
                            Time in seconds
                            
                            .. attribute:: is_computed
                            
                            	True if computed; false if not
                            	**type**\:  bool
                            
                            .. attribute:: value
                            
                            	Value for time or tries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time, self).__init__()

                                self.yang_name = "time"
                                self.yang_parent_name = "host"

                                self.is_computed = YLeaf(YType.boolean, "is-computed")

                                self.value = YLeaf(YType.uint32, "value")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("is_computed",
                                                "value") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.is_computed.is_set or
                                    self.value.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.is_computed.yfilter != YFilter.not_set or
                                    self.value.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "time" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.is_computed.is_set or self.is_computed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_computed.get_name_leafdata())
                                if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.value.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "is-computed" or name == "value"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "is-computed"):
                                    self.is_computed = value
                                    self.is_computed.value_namespace = name_space
                                    self.is_computed.value_namespace_prefix = name_space_prefix
                                if(value_path == "value"):
                                    self.value = value
                                    self.value.value_namespace = name_space
                                    self.value.value_namespace_prefix = name_space_prefix


                        class Tries(Entity):
                            """
                            Number of tries
                            
                            .. attribute:: is_computed
                            
                            	True if computed; false if not
                            	**type**\:  bool
                            
                            .. attribute:: value
                            
                            	Value for time or tries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries, self).__init__()

                                self.yang_name = "tries"
                                self.yang_parent_name = "host"

                                self.is_computed = YLeaf(YType.boolean, "is-computed")

                                self.value = YLeaf(YType.uint32, "value")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("is_computed",
                                                "value") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.is_computed.is_set or
                                    self.value.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.is_computed.yfilter != YFilter.not_set or
                                    self.value.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "tries" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.is_computed.is_set or self.is_computed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_computed.get_name_leafdata())
                                if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.value.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "is-computed" or name == "value"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "is-computed"):
                                    self.is_computed = value
                                    self.is_computed.value_namespace = name_space
                                    self.is_computed.value_namespace_prefix = name_space_prefix
                                if(value_path == "value"):
                                    self.value = value
                                    self.value.value_namespace = name_space
                                    self.value.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.acct_port_number.is_set or
                                self.auth_port_number.is_set or
                                self.ip_address.is_set or
                                (self.time is not None and self.time.has_data()) or
                                (self.tries is not None and self.tries.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.acct_port_number.yfilter != YFilter.not_set or
                                self.auth_port_number.yfilter != YFilter.not_set or
                                self.ip_address.yfilter != YFilter.not_set or
                                (self.time is not None and self.time.has_operation()) or
                                (self.tries is not None and self.tries.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "host" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.acct_port_number.is_set or self.acct_port_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acct_port_number.get_name_leafdata())
                            if (self.auth_port_number.is_set or self.auth_port_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.auth_port_number.get_name_leafdata())
                            if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "time"):
                                if (self.time is None):
                                    self.time = Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time()
                                    self.time.parent = self
                                    self._children_name_map["time"] = "time"
                                return self.time

                            if (child_yang_name == "tries"):
                                if (self.tries is None):
                                    self.tries = Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries()
                                    self.tries.parent = self
                                    self._children_name_map["tries"] = "tries"
                                return self.tries

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "time" or name == "tries" or name == "acct-port-number" or name == "auth-port-number" or name == "ip-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "acct-port-number"):
                                self.acct_port_number = value
                                self.acct_port_number.value_namespace = name_space
                                self.acct_port_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "auth-port-number"):
                                self.auth_port_number = value
                                self.auth_port_number.value_namespace = name_space
                                self.auth_port_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-address"):
                                self.ip_address = value
                                self.ip_address.value_namespace = name_space
                                self.ip_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.host:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.host:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "hosts" + path_buffer

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

                        if (child_yang_name == "host"):
                            for c in self.host:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Radius.Nodes.Node.DeadCriteria.Hosts.Host()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.host.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "host"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.hosts is not None and self.hosts.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.hosts is not None and self.hosts.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "dead-criteria" + path_buffer

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

                    if (child_yang_name == "hosts"):
                        if (self.hosts is None):
                            self.hosts = Radius.Nodes.Node.DeadCriteria.Hosts()
                            self.hosts.parent = self
                            self._children_name_map["hosts"] = "hosts"
                        return self.hosts

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hosts"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Authentication(Entity):
                """
                RADIUS authentication data
                
                .. attribute:: authentication_group
                
                	List of authentication groups
                	**type**\: list of    :py:class:`AuthenticationGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Authentication.AuthenticationGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Radius.Nodes.Node.Authentication, self).__init__()

                    self.yang_name = "authentication"
                    self.yang_parent_name = "node"

                    self.authentication_group = YList(self)

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
                                super(Radius.Nodes.Node.Authentication, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Radius.Nodes.Node.Authentication, self).__setattr__(name, value)


                class AuthenticationGroup(Entity):
                    """
                    List of authentication groups
                    
                    .. attribute:: authentication
                    
                    	Authentication data
                    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication>`
                    
                    .. attribute:: family
                    
                    	IP address Family
                    	**type**\:  str
                    
                    .. attribute:: ip_address
                    
                    	IP address buffer
                    	**type**\:  str
                    
                    .. attribute:: port
                    
                    	Authentication port number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: server_address
                    
                    	IP address of RADIUS server
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Radius.Nodes.Node.Authentication.AuthenticationGroup, self).__init__()

                        self.yang_name = "authentication-group"
                        self.yang_parent_name = "authentication"

                        self.family = YLeaf(YType.str, "family")

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.port = YLeaf(YType.uint32, "port")

                        self.server_address = YLeaf(YType.str, "server-address")

                        self.authentication = Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"
                        self._children_yang_names.add("authentication")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("family",
                                        "ip_address",
                                        "port",
                                        "server_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Radius.Nodes.Node.Authentication.AuthenticationGroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Radius.Nodes.Node.Authentication.AuthenticationGroup, self).__setattr__(name, value)


                    class Authentication(Entity):
                        """
                        Authentication data
                        
                        .. attribute:: access_accepts
                        
                        	Number of access accepts
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_challenges
                        
                        	Number of access challenges
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_rejects
                        
                        	Number of access rejects
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_request_retransmits
                        
                        	Number of retransmitted access requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_requests
                        
                        	Number of access requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: access_timeouts
                        
                        	Number of access packets timed out
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_incorrect_responses
                        
                        	Number of incorrect authentication responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_response_time
                        
                        	Average response time for authentication requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_server_error_responses
                        
                        	Number of server error authentication responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_transaction_failure
                        
                        	Number of failed authentication transactions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_transaction_successess
                        
                        	Number of succeeded authentication transactions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_unexpected_responses
                        
                        	Number of unexpected authentication responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_access_authenticators
                        
                        	Number of bad access authenticators
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_access_responses
                        
                        	Number of bad access responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_access_responses
                        
                        	Number of access responses dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pending_access_requests
                        
                        	Number of pending access requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rtt
                        
                        	Round trip time for authentication in milliseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: unknown_access_types
                        
                        	Number of packets received with unknown type from authentication server
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication, self).__init__()

                            self.yang_name = "authentication"
                            self.yang_parent_name = "authentication-group"

                            self.access_accepts = YLeaf(YType.uint32, "access-accepts")

                            self.access_challenges = YLeaf(YType.uint32, "access-challenges")

                            self.access_rejects = YLeaf(YType.uint32, "access-rejects")

                            self.access_request_retransmits = YLeaf(YType.uint32, "access-request-retransmits")

                            self.access_requests = YLeaf(YType.uint32, "access-requests")

                            self.access_timeouts = YLeaf(YType.uint32, "access-timeouts")

                            self.authen_incorrect_responses = YLeaf(YType.uint32, "authen-incorrect-responses")

                            self.authen_response_time = YLeaf(YType.uint32, "authen-response-time")

                            self.authen_server_error_responses = YLeaf(YType.uint32, "authen-server-error-responses")

                            self.authen_transaction_failure = YLeaf(YType.uint32, "authen-transaction-failure")

                            self.authen_transaction_successess = YLeaf(YType.uint32, "authen-transaction-successess")

                            self.authen_unexpected_responses = YLeaf(YType.uint32, "authen-unexpected-responses")

                            self.bad_access_authenticators = YLeaf(YType.uint32, "bad-access-authenticators")

                            self.bad_access_responses = YLeaf(YType.uint32, "bad-access-responses")

                            self.dropped_access_responses = YLeaf(YType.uint32, "dropped-access-responses")

                            self.pending_access_requests = YLeaf(YType.uint32, "pending-access-requests")

                            self.rtt = YLeaf(YType.uint32, "rtt")

                            self.unknown_access_types = YLeaf(YType.uint32, "unknown-access-types")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("access_accepts",
                                            "access_challenges",
                                            "access_rejects",
                                            "access_request_retransmits",
                                            "access_requests",
                                            "access_timeouts",
                                            "authen_incorrect_responses",
                                            "authen_response_time",
                                            "authen_server_error_responses",
                                            "authen_transaction_failure",
                                            "authen_transaction_successess",
                                            "authen_unexpected_responses",
                                            "bad_access_authenticators",
                                            "bad_access_responses",
                                            "dropped_access_responses",
                                            "pending_access_requests",
                                            "rtt",
                                            "unknown_access_types") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.access_accepts.is_set or
                                self.access_challenges.is_set or
                                self.access_rejects.is_set or
                                self.access_request_retransmits.is_set or
                                self.access_requests.is_set or
                                self.access_timeouts.is_set or
                                self.authen_incorrect_responses.is_set or
                                self.authen_response_time.is_set or
                                self.authen_server_error_responses.is_set or
                                self.authen_transaction_failure.is_set or
                                self.authen_transaction_successess.is_set or
                                self.authen_unexpected_responses.is_set or
                                self.bad_access_authenticators.is_set or
                                self.bad_access_responses.is_set or
                                self.dropped_access_responses.is_set or
                                self.pending_access_requests.is_set or
                                self.rtt.is_set or
                                self.unknown_access_types.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.access_accepts.yfilter != YFilter.not_set or
                                self.access_challenges.yfilter != YFilter.not_set or
                                self.access_rejects.yfilter != YFilter.not_set or
                                self.access_request_retransmits.yfilter != YFilter.not_set or
                                self.access_requests.yfilter != YFilter.not_set or
                                self.access_timeouts.yfilter != YFilter.not_set or
                                self.authen_incorrect_responses.yfilter != YFilter.not_set or
                                self.authen_response_time.yfilter != YFilter.not_set or
                                self.authen_server_error_responses.yfilter != YFilter.not_set or
                                self.authen_transaction_failure.yfilter != YFilter.not_set or
                                self.authen_transaction_successess.yfilter != YFilter.not_set or
                                self.authen_unexpected_responses.yfilter != YFilter.not_set or
                                self.bad_access_authenticators.yfilter != YFilter.not_set or
                                self.bad_access_responses.yfilter != YFilter.not_set or
                                self.dropped_access_responses.yfilter != YFilter.not_set or
                                self.pending_access_requests.yfilter != YFilter.not_set or
                                self.rtt.yfilter != YFilter.not_set or
                                self.unknown_access_types.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "authentication" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.access_accepts.is_set or self.access_accepts.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_accepts.get_name_leafdata())
                            if (self.access_challenges.is_set or self.access_challenges.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_challenges.get_name_leafdata())
                            if (self.access_rejects.is_set or self.access_rejects.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_rejects.get_name_leafdata())
                            if (self.access_request_retransmits.is_set or self.access_request_retransmits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_request_retransmits.get_name_leafdata())
                            if (self.access_requests.is_set or self.access_requests.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_requests.get_name_leafdata())
                            if (self.access_timeouts.is_set or self.access_timeouts.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.access_timeouts.get_name_leafdata())
                            if (self.authen_incorrect_responses.is_set or self.authen_incorrect_responses.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authen_incorrect_responses.get_name_leafdata())
                            if (self.authen_response_time.is_set or self.authen_response_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authen_response_time.get_name_leafdata())
                            if (self.authen_server_error_responses.is_set or self.authen_server_error_responses.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authen_server_error_responses.get_name_leafdata())
                            if (self.authen_transaction_failure.is_set or self.authen_transaction_failure.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authen_transaction_failure.get_name_leafdata())
                            if (self.authen_transaction_successess.is_set or self.authen_transaction_successess.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authen_transaction_successess.get_name_leafdata())
                            if (self.authen_unexpected_responses.is_set or self.authen_unexpected_responses.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authen_unexpected_responses.get_name_leafdata())
                            if (self.bad_access_authenticators.is_set or self.bad_access_authenticators.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_access_authenticators.get_name_leafdata())
                            if (self.bad_access_responses.is_set or self.bad_access_responses.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_access_responses.get_name_leafdata())
                            if (self.dropped_access_responses.is_set or self.dropped_access_responses.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_access_responses.get_name_leafdata())
                            if (self.pending_access_requests.is_set or self.pending_access_requests.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pending_access_requests.get_name_leafdata())
                            if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rtt.get_name_leafdata())
                            if (self.unknown_access_types.is_set or self.unknown_access_types.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unknown_access_types.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "access-accepts" or name == "access-challenges" or name == "access-rejects" or name == "access-request-retransmits" or name == "access-requests" or name == "access-timeouts" or name == "authen-incorrect-responses" or name == "authen-response-time" or name == "authen-server-error-responses" or name == "authen-transaction-failure" or name == "authen-transaction-successess" or name == "authen-unexpected-responses" or name == "bad-access-authenticators" or name == "bad-access-responses" or name == "dropped-access-responses" or name == "pending-access-requests" or name == "rtt" or name == "unknown-access-types"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "access-accepts"):
                                self.access_accepts = value
                                self.access_accepts.value_namespace = name_space
                                self.access_accepts.value_namespace_prefix = name_space_prefix
                            if(value_path == "access-challenges"):
                                self.access_challenges = value
                                self.access_challenges.value_namespace = name_space
                                self.access_challenges.value_namespace_prefix = name_space_prefix
                            if(value_path == "access-rejects"):
                                self.access_rejects = value
                                self.access_rejects.value_namespace = name_space
                                self.access_rejects.value_namespace_prefix = name_space_prefix
                            if(value_path == "access-request-retransmits"):
                                self.access_request_retransmits = value
                                self.access_request_retransmits.value_namespace = name_space
                                self.access_request_retransmits.value_namespace_prefix = name_space_prefix
                            if(value_path == "access-requests"):
                                self.access_requests = value
                                self.access_requests.value_namespace = name_space
                                self.access_requests.value_namespace_prefix = name_space_prefix
                            if(value_path == "access-timeouts"):
                                self.access_timeouts = value
                                self.access_timeouts.value_namespace = name_space
                                self.access_timeouts.value_namespace_prefix = name_space_prefix
                            if(value_path == "authen-incorrect-responses"):
                                self.authen_incorrect_responses = value
                                self.authen_incorrect_responses.value_namespace = name_space
                                self.authen_incorrect_responses.value_namespace_prefix = name_space_prefix
                            if(value_path == "authen-response-time"):
                                self.authen_response_time = value
                                self.authen_response_time.value_namespace = name_space
                                self.authen_response_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "authen-server-error-responses"):
                                self.authen_server_error_responses = value
                                self.authen_server_error_responses.value_namespace = name_space
                                self.authen_server_error_responses.value_namespace_prefix = name_space_prefix
                            if(value_path == "authen-transaction-failure"):
                                self.authen_transaction_failure = value
                                self.authen_transaction_failure.value_namespace = name_space
                                self.authen_transaction_failure.value_namespace_prefix = name_space_prefix
                            if(value_path == "authen-transaction-successess"):
                                self.authen_transaction_successess = value
                                self.authen_transaction_successess.value_namespace = name_space
                                self.authen_transaction_successess.value_namespace_prefix = name_space_prefix
                            if(value_path == "authen-unexpected-responses"):
                                self.authen_unexpected_responses = value
                                self.authen_unexpected_responses.value_namespace = name_space
                                self.authen_unexpected_responses.value_namespace_prefix = name_space_prefix
                            if(value_path == "bad-access-authenticators"):
                                self.bad_access_authenticators = value
                                self.bad_access_authenticators.value_namespace = name_space
                                self.bad_access_authenticators.value_namespace_prefix = name_space_prefix
                            if(value_path == "bad-access-responses"):
                                self.bad_access_responses = value
                                self.bad_access_responses.value_namespace = name_space
                                self.bad_access_responses.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-access-responses"):
                                self.dropped_access_responses = value
                                self.dropped_access_responses.value_namespace = name_space
                                self.dropped_access_responses.value_namespace_prefix = name_space_prefix
                            if(value_path == "pending-access-requests"):
                                self.pending_access_requests = value
                                self.pending_access_requests.value_namespace = name_space
                                self.pending_access_requests.value_namespace_prefix = name_space_prefix
                            if(value_path == "rtt"):
                                self.rtt = value
                                self.rtt.value_namespace = name_space
                                self.rtt.value_namespace_prefix = name_space_prefix
                            if(value_path == "unknown-access-types"):
                                self.unknown_access_types = value
                                self.unknown_access_types.value_namespace = name_space
                                self.unknown_access_types.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.family.is_set or
                            self.ip_address.is_set or
                            self.port.is_set or
                            self.server_address.is_set or
                            (self.authentication is not None and self.authentication.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.family.yfilter != YFilter.not_set or
                            self.ip_address.yfilter != YFilter.not_set or
                            self.port.yfilter != YFilter.not_set or
                            self.server_address.yfilter != YFilter.not_set or
                            (self.authentication is not None and self.authentication.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "authentication-group" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.family.is_set or self.family.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.family.get_name_leafdata())
                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_address.get_name_leafdata())
                        if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port.get_name_leafdata())
                        if (self.server_address.is_set or self.server_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.server_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "authentication"):
                            if (self.authentication is None):
                                self.authentication = Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication()
                                self.authentication.parent = self
                                self._children_name_map["authentication"] = "authentication"
                            return self.authentication

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "authentication" or name == "family" or name == "ip-address" or name == "port" or name == "server-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "family"):
                            self.family = value
                            self.family.value_namespace = name_space
                            self.family.value_namespace_prefix = name_space_prefix
                        if(value_path == "ip-address"):
                            self.ip_address = value
                            self.ip_address.value_namespace = name_space
                            self.ip_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "port"):
                            self.port = value
                            self.port.value_namespace = name_space
                            self.port.value_namespace_prefix = name_space_prefix
                        if(value_path == "server-address"):
                            self.server_address = value
                            self.server_address.value_namespace = name_space
                            self.server_address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.authentication_group:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.authentication_group:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "authentication" + path_buffer

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

                    if (child_yang_name == "authentication-group"):
                        for c in self.authentication_group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Radius.Nodes.Node.Authentication.AuthenticationGroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.authentication_group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "authentication-group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Accounting(Entity):
                """
                RADIUS accounting data
                
                .. attribute:: accounting_group
                
                	List of accounting groups
                	**type**\: list of    :py:class:`AccountingGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Accounting.AccountingGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Radius.Nodes.Node.Accounting, self).__init__()

                    self.yang_name = "accounting"
                    self.yang_parent_name = "node"

                    self.accounting_group = YList(self)

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
                                super(Radius.Nodes.Node.Accounting, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Radius.Nodes.Node.Accounting, self).__setattr__(name, value)


                class AccountingGroup(Entity):
                    """
                    List of accounting groups
                    
                    .. attribute:: accounting
                    
                    	Accounting data
                    	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.Accounting.AccountingGroup.Accounting>`
                    
                    .. attribute:: family
                    
                    	IP address Family
                    	**type**\:  str
                    
                    .. attribute:: ip_address
                    
                    	IP address buffer
                    	**type**\:  str
                    
                    .. attribute:: port
                    
                    	Accounting port number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: server_address
                    
                    	IP address of RADIUS server
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Radius.Nodes.Node.Accounting.AccountingGroup, self).__init__()

                        self.yang_name = "accounting-group"
                        self.yang_parent_name = "accounting"

                        self.family = YLeaf(YType.str, "family")

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.port = YLeaf(YType.uint32, "port")

                        self.server_address = YLeaf(YType.str, "server-address")

                        self.accounting = Radius.Nodes.Node.Accounting.AccountingGroup.Accounting()
                        self.accounting.parent = self
                        self._children_name_map["accounting"] = "accounting"
                        self._children_yang_names.add("accounting")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("family",
                                        "ip_address",
                                        "port",
                                        "server_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Radius.Nodes.Node.Accounting.AccountingGroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Radius.Nodes.Node.Accounting.AccountingGroup, self).__setattr__(name, value)


                    class Accounting(Entity):
                        """
                        Accounting data
                        
                        .. attribute:: acct_incorrect_responses
                        
                        	Number of incorrect accounting responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_response_time
                        
                        	Average response time for authentication requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_server_error_responses
                        
                        	Number of server error accounting responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_transaction_failure
                        
                        	Number of failed authentication transactions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_transaction_successess
                        
                        	Number of succeeded authentication transactions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acct_unexpected_responses
                        
                        	Number of unexpected accounting responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_authenticators
                        
                        	Number of bad accounting authenticators
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_responses
                        
                        	Number of bad accounting responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_responses
                        
                        	Number of accounting responses dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pending_requests
                        
                        	Number of pending accounting requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: requests
                        
                        	Number of accounting requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: responses
                        
                        	Number of accounting responses
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: retransmits
                        
                        	Number of retransmitted accounting requests
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rtt
                        
                        	Round trip time for accounting in milliseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: millisecond
                        
                        .. attribute:: timeouts
                        
                        	Number of accounting packets timed\-out
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_packet_types
                        
                        	Number of packets received with unknown type from accounting server
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Radius.Nodes.Node.Accounting.AccountingGroup.Accounting, self).__init__()

                            self.yang_name = "accounting"
                            self.yang_parent_name = "accounting-group"

                            self.acct_incorrect_responses = YLeaf(YType.uint32, "acct-incorrect-responses")

                            self.acct_response_time = YLeaf(YType.uint32, "acct-response-time")

                            self.acct_server_error_responses = YLeaf(YType.uint32, "acct-server-error-responses")

                            self.acct_transaction_failure = YLeaf(YType.uint32, "acct-transaction-failure")

                            self.acct_transaction_successess = YLeaf(YType.uint32, "acct-transaction-successess")

                            self.acct_unexpected_responses = YLeaf(YType.uint32, "acct-unexpected-responses")

                            self.bad_authenticators = YLeaf(YType.uint32, "bad-authenticators")

                            self.bad_responses = YLeaf(YType.uint32, "bad-responses")

                            self.dropped_responses = YLeaf(YType.uint32, "dropped-responses")

                            self.pending_requests = YLeaf(YType.uint32, "pending-requests")

                            self.requests = YLeaf(YType.uint32, "requests")

                            self.responses = YLeaf(YType.uint32, "responses")

                            self.retransmits = YLeaf(YType.uint32, "retransmits")

                            self.rtt = YLeaf(YType.uint32, "rtt")

                            self.timeouts = YLeaf(YType.uint32, "timeouts")

                            self.unknown_packet_types = YLeaf(YType.uint32, "unknown-packet-types")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("acct_incorrect_responses",
                                            "acct_response_time",
                                            "acct_server_error_responses",
                                            "acct_transaction_failure",
                                            "acct_transaction_successess",
                                            "acct_unexpected_responses",
                                            "bad_authenticators",
                                            "bad_responses",
                                            "dropped_responses",
                                            "pending_requests",
                                            "requests",
                                            "responses",
                                            "retransmits",
                                            "rtt",
                                            "timeouts",
                                            "unknown_packet_types") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Radius.Nodes.Node.Accounting.AccountingGroup.Accounting, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Radius.Nodes.Node.Accounting.AccountingGroup.Accounting, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.acct_incorrect_responses.is_set or
                                self.acct_response_time.is_set or
                                self.acct_server_error_responses.is_set or
                                self.acct_transaction_failure.is_set or
                                self.acct_transaction_successess.is_set or
                                self.acct_unexpected_responses.is_set or
                                self.bad_authenticators.is_set or
                                self.bad_responses.is_set or
                                self.dropped_responses.is_set or
                                self.pending_requests.is_set or
                                self.requests.is_set or
                                self.responses.is_set or
                                self.retransmits.is_set or
                                self.rtt.is_set or
                                self.timeouts.is_set or
                                self.unknown_packet_types.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.acct_incorrect_responses.yfilter != YFilter.not_set or
                                self.acct_response_time.yfilter != YFilter.not_set or
                                self.acct_server_error_responses.yfilter != YFilter.not_set or
                                self.acct_transaction_failure.yfilter != YFilter.not_set or
                                self.acct_transaction_successess.yfilter != YFilter.not_set or
                                self.acct_unexpected_responses.yfilter != YFilter.not_set or
                                self.bad_authenticators.yfilter != YFilter.not_set or
                                self.bad_responses.yfilter != YFilter.not_set or
                                self.dropped_responses.yfilter != YFilter.not_set or
                                self.pending_requests.yfilter != YFilter.not_set or
                                self.requests.yfilter != YFilter.not_set or
                                self.responses.yfilter != YFilter.not_set or
                                self.retransmits.yfilter != YFilter.not_set or
                                self.rtt.yfilter != YFilter.not_set or
                                self.timeouts.yfilter != YFilter.not_set or
                                self.unknown_packet_types.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "accounting" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.acct_incorrect_responses.is_set or self.acct_incorrect_responses.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acct_incorrect_responses.get_name_leafdata())
                            if (self.acct_response_time.is_set or self.acct_response_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acct_response_time.get_name_leafdata())
                            if (self.acct_server_error_responses.is_set or self.acct_server_error_responses.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acct_server_error_responses.get_name_leafdata())
                            if (self.acct_transaction_failure.is_set or self.acct_transaction_failure.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acct_transaction_failure.get_name_leafdata())
                            if (self.acct_transaction_successess.is_set or self.acct_transaction_successess.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acct_transaction_successess.get_name_leafdata())
                            if (self.acct_unexpected_responses.is_set or self.acct_unexpected_responses.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acct_unexpected_responses.get_name_leafdata())
                            if (self.bad_authenticators.is_set or self.bad_authenticators.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_authenticators.get_name_leafdata())
                            if (self.bad_responses.is_set or self.bad_responses.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.bad_responses.get_name_leafdata())
                            if (self.dropped_responses.is_set or self.dropped_responses.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dropped_responses.get_name_leafdata())
                            if (self.pending_requests.is_set or self.pending_requests.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pending_requests.get_name_leafdata())
                            if (self.requests.is_set or self.requests.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.requests.get_name_leafdata())
                            if (self.responses.is_set or self.responses.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.responses.get_name_leafdata())
                            if (self.retransmits.is_set or self.retransmits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.retransmits.get_name_leafdata())
                            if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rtt.get_name_leafdata())
                            if (self.timeouts.is_set or self.timeouts.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.timeouts.get_name_leafdata())
                            if (self.unknown_packet_types.is_set or self.unknown_packet_types.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unknown_packet_types.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "acct-incorrect-responses" or name == "acct-response-time" or name == "acct-server-error-responses" or name == "acct-transaction-failure" or name == "acct-transaction-successess" or name == "acct-unexpected-responses" or name == "bad-authenticators" or name == "bad-responses" or name == "dropped-responses" or name == "pending-requests" or name == "requests" or name == "responses" or name == "retransmits" or name == "rtt" or name == "timeouts" or name == "unknown-packet-types"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "acct-incorrect-responses"):
                                self.acct_incorrect_responses = value
                                self.acct_incorrect_responses.value_namespace = name_space
                                self.acct_incorrect_responses.value_namespace_prefix = name_space_prefix
                            if(value_path == "acct-response-time"):
                                self.acct_response_time = value
                                self.acct_response_time.value_namespace = name_space
                                self.acct_response_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "acct-server-error-responses"):
                                self.acct_server_error_responses = value
                                self.acct_server_error_responses.value_namespace = name_space
                                self.acct_server_error_responses.value_namespace_prefix = name_space_prefix
                            if(value_path == "acct-transaction-failure"):
                                self.acct_transaction_failure = value
                                self.acct_transaction_failure.value_namespace = name_space
                                self.acct_transaction_failure.value_namespace_prefix = name_space_prefix
                            if(value_path == "acct-transaction-successess"):
                                self.acct_transaction_successess = value
                                self.acct_transaction_successess.value_namespace = name_space
                                self.acct_transaction_successess.value_namespace_prefix = name_space_prefix
                            if(value_path == "acct-unexpected-responses"):
                                self.acct_unexpected_responses = value
                                self.acct_unexpected_responses.value_namespace = name_space
                                self.acct_unexpected_responses.value_namespace_prefix = name_space_prefix
                            if(value_path == "bad-authenticators"):
                                self.bad_authenticators = value
                                self.bad_authenticators.value_namespace = name_space
                                self.bad_authenticators.value_namespace_prefix = name_space_prefix
                            if(value_path == "bad-responses"):
                                self.bad_responses = value
                                self.bad_responses.value_namespace = name_space
                                self.bad_responses.value_namespace_prefix = name_space_prefix
                            if(value_path == "dropped-responses"):
                                self.dropped_responses = value
                                self.dropped_responses.value_namespace = name_space
                                self.dropped_responses.value_namespace_prefix = name_space_prefix
                            if(value_path == "pending-requests"):
                                self.pending_requests = value
                                self.pending_requests.value_namespace = name_space
                                self.pending_requests.value_namespace_prefix = name_space_prefix
                            if(value_path == "requests"):
                                self.requests = value
                                self.requests.value_namespace = name_space
                                self.requests.value_namespace_prefix = name_space_prefix
                            if(value_path == "responses"):
                                self.responses = value
                                self.responses.value_namespace = name_space
                                self.responses.value_namespace_prefix = name_space_prefix
                            if(value_path == "retransmits"):
                                self.retransmits = value
                                self.retransmits.value_namespace = name_space
                                self.retransmits.value_namespace_prefix = name_space_prefix
                            if(value_path == "rtt"):
                                self.rtt = value
                                self.rtt.value_namespace = name_space
                                self.rtt.value_namespace_prefix = name_space_prefix
                            if(value_path == "timeouts"):
                                self.timeouts = value
                                self.timeouts.value_namespace = name_space
                                self.timeouts.value_namespace_prefix = name_space_prefix
                            if(value_path == "unknown-packet-types"):
                                self.unknown_packet_types = value
                                self.unknown_packet_types.value_namespace = name_space
                                self.unknown_packet_types.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.family.is_set or
                            self.ip_address.is_set or
                            self.port.is_set or
                            self.server_address.is_set or
                            (self.accounting is not None and self.accounting.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.family.yfilter != YFilter.not_set or
                            self.ip_address.yfilter != YFilter.not_set or
                            self.port.yfilter != YFilter.not_set or
                            self.server_address.yfilter != YFilter.not_set or
                            (self.accounting is not None and self.accounting.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "accounting-group" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.family.is_set or self.family.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.family.get_name_leafdata())
                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_address.get_name_leafdata())
                        if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port.get_name_leafdata())
                        if (self.server_address.is_set or self.server_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.server_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "accounting"):
                            if (self.accounting is None):
                                self.accounting = Radius.Nodes.Node.Accounting.AccountingGroup.Accounting()
                                self.accounting.parent = self
                                self._children_name_map["accounting"] = "accounting"
                            return self.accounting

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accounting" or name == "family" or name == "ip-address" or name == "port" or name == "server-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "family"):
                            self.family = value
                            self.family.value_namespace = name_space
                            self.family.value_namespace_prefix = name_space_prefix
                        if(value_path == "ip-address"):
                            self.ip_address = value
                            self.ip_address.value_namespace = name_space
                            self.ip_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "port"):
                            self.port = value
                            self.port.value_namespace = name_space
                            self.port.value_namespace_prefix = name_space_prefix
                        if(value_path == "server-address"):
                            self.server_address = value
                            self.server_address.value_namespace = name_space
                            self.server_address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.accounting_group:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.accounting_group:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "accounting" + path_buffer

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

                    if (child_yang_name == "accounting-group"):
                        for c in self.accounting_group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Radius.Nodes.Node.Accounting.AccountingGroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.accounting_group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "accounting-group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ServerGroups(Entity):
                """
                RADIUS server group table
                
                .. attribute:: server_group
                
                	RADIUS server group data
                	**type**\: list of    :py:class:`ServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup>`
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Radius.Nodes.Node.ServerGroups, self).__init__()

                    self.yang_name = "server-groups"
                    self.yang_parent_name = "node"

                    self.server_group = YList(self)

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
                                super(Radius.Nodes.Node.ServerGroups, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Radius.Nodes.Node.ServerGroups, self).__setattr__(name, value)


                class ServerGroup(Entity):
                    """
                    RADIUS server group data
                    
                    .. attribute:: server_group_name  <key>
                    
                    	Group name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: dead_time
                    
                    	Dead time in minutes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: minute
                    
                    .. attribute:: groups
                    
                    	Number of groups
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: server_group
                    
                    	Server groups
                    	**type**\: list of    :py:class:`ServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup>`
                    
                    .. attribute:: servers
                    
                    	Number of servers
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Radius.Nodes.Node.ServerGroups.ServerGroup, self).__init__()

                        self.yang_name = "server-group"
                        self.yang_parent_name = "server-groups"

                        self.server_group_name = YLeaf(YType.str, "server-group-name")

                        self.dead_time = YLeaf(YType.uint32, "dead-time")

                        self.groups = YLeaf(YType.uint32, "groups")

                        self.servers = YLeaf(YType.uint32, "servers")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.server_group = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("server_group_name",
                                        "dead_time",
                                        "groups",
                                        "servers",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Radius.Nodes.Node.ServerGroups.ServerGroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Radius.Nodes.Node.ServerGroups.ServerGroup, self).__setattr__(name, value)


                    class ServerGroup(Entity):
                        """
                        Server groups
                        
                        .. attribute:: accounting
                        
                        	Accounting data
                        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Accounting>`
                        
                        .. attribute:: accounting_port
                        
                        	Accounting port
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authentication
                        
                        	Authentication data
                        	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authentication>`
                        
                        .. attribute:: authentication_port
                        
                        	Authentication port
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authorization
                        
                        	Authorization data
                        	**type**\:   :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper.Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authorization>`
                        
                        .. attribute:: family
                        
                        	IP address Family
                        	**type**\:  str
                        
                        .. attribute:: ip_address
                        
                        	IP address buffer
                        	**type**\:  str
                        
                        .. attribute:: is_private
                        
                        	True if private
                        	**type**\:  bool
                        
                        .. attribute:: server_address
                        
                        	Server address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup, self).__init__()

                            self.yang_name = "server-group"
                            self.yang_parent_name = "server-group"

                            self.accounting_port = YLeaf(YType.uint32, "accounting-port")

                            self.authentication_port = YLeaf(YType.uint32, "authentication-port")

                            self.family = YLeaf(YType.str, "family")

                            self.ip_address = YLeaf(YType.str, "ip-address")

                            self.is_private = YLeaf(YType.boolean, "is-private")

                            self.server_address = YLeaf(YType.str, "server-address")

                            self.accounting = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Accounting()
                            self.accounting.parent = self
                            self._children_name_map["accounting"] = "accounting"
                            self._children_yang_names.add("accounting")

                            self.authentication = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authentication()
                            self.authentication.parent = self
                            self._children_name_map["authentication"] = "authentication"
                            self._children_yang_names.add("authentication")

                            self.authorization = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authorization()
                            self.authorization.parent = self
                            self._children_name_map["authorization"] = "authorization"
                            self._children_yang_names.add("authorization")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("accounting_port",
                                            "authentication_port",
                                            "family",
                                            "ip_address",
                                            "is_private",
                                            "server_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup, self).__setattr__(name, value)


                        class Accounting(Entity):
                            """
                            Accounting data
                            
                            .. attribute:: acct_incorrect_responses
                            
                            	Number of incorrect accounting responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_response_time
                            
                            	Average response time for authentication requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_server_error_responses
                            
                            	Number of server error accounting responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_transaction_failure
                            
                            	Number of failed authentication transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_transaction_successess
                            
                            	Number of succeeded authentication transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acct_unexpected_responses
                            
                            	Number of unexpected accounting responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_authenticators
                            
                            	Number of bad accounting authenticators
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_responses
                            
                            	Number of bad accounting responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dropped_responses
                            
                            	Number of accounting responses dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pending_requests
                            
                            	Number of pending accounting requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: requests
                            
                            	Number of accounting requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: responses
                            
                            	Number of accounting responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: retransmits
                            
                            	Number of retransmitted accounting requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rtt
                            
                            	Round trip time for accounting in milliseconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: millisecond
                            
                            .. attribute:: timeouts
                            
                            	Number of accounting packets timed\-out
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_packet_types
                            
                            	Number of packets received with unknown type from accounting server
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Accounting, self).__init__()

                                self.yang_name = "accounting"
                                self.yang_parent_name = "server-group"

                                self.acct_incorrect_responses = YLeaf(YType.uint32, "acct-incorrect-responses")

                                self.acct_response_time = YLeaf(YType.uint32, "acct-response-time")

                                self.acct_server_error_responses = YLeaf(YType.uint32, "acct-server-error-responses")

                                self.acct_transaction_failure = YLeaf(YType.uint32, "acct-transaction-failure")

                                self.acct_transaction_successess = YLeaf(YType.uint32, "acct-transaction-successess")

                                self.acct_unexpected_responses = YLeaf(YType.uint32, "acct-unexpected-responses")

                                self.bad_authenticators = YLeaf(YType.uint32, "bad-authenticators")

                                self.bad_responses = YLeaf(YType.uint32, "bad-responses")

                                self.dropped_responses = YLeaf(YType.uint32, "dropped-responses")

                                self.pending_requests = YLeaf(YType.uint32, "pending-requests")

                                self.requests = YLeaf(YType.uint32, "requests")

                                self.responses = YLeaf(YType.uint32, "responses")

                                self.retransmits = YLeaf(YType.uint32, "retransmits")

                                self.rtt = YLeaf(YType.uint32, "rtt")

                                self.timeouts = YLeaf(YType.uint32, "timeouts")

                                self.unknown_packet_types = YLeaf(YType.uint32, "unknown-packet-types")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("acct_incorrect_responses",
                                                "acct_response_time",
                                                "acct_server_error_responses",
                                                "acct_transaction_failure",
                                                "acct_transaction_successess",
                                                "acct_unexpected_responses",
                                                "bad_authenticators",
                                                "bad_responses",
                                                "dropped_responses",
                                                "pending_requests",
                                                "requests",
                                                "responses",
                                                "retransmits",
                                                "rtt",
                                                "timeouts",
                                                "unknown_packet_types") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Accounting, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Accounting, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.acct_incorrect_responses.is_set or
                                    self.acct_response_time.is_set or
                                    self.acct_server_error_responses.is_set or
                                    self.acct_transaction_failure.is_set or
                                    self.acct_transaction_successess.is_set or
                                    self.acct_unexpected_responses.is_set or
                                    self.bad_authenticators.is_set or
                                    self.bad_responses.is_set or
                                    self.dropped_responses.is_set or
                                    self.pending_requests.is_set or
                                    self.requests.is_set or
                                    self.responses.is_set or
                                    self.retransmits.is_set or
                                    self.rtt.is_set or
                                    self.timeouts.is_set or
                                    self.unknown_packet_types.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.acct_incorrect_responses.yfilter != YFilter.not_set or
                                    self.acct_response_time.yfilter != YFilter.not_set or
                                    self.acct_server_error_responses.yfilter != YFilter.not_set or
                                    self.acct_transaction_failure.yfilter != YFilter.not_set or
                                    self.acct_transaction_successess.yfilter != YFilter.not_set or
                                    self.acct_unexpected_responses.yfilter != YFilter.not_set or
                                    self.bad_authenticators.yfilter != YFilter.not_set or
                                    self.bad_responses.yfilter != YFilter.not_set or
                                    self.dropped_responses.yfilter != YFilter.not_set or
                                    self.pending_requests.yfilter != YFilter.not_set or
                                    self.requests.yfilter != YFilter.not_set or
                                    self.responses.yfilter != YFilter.not_set or
                                    self.retransmits.yfilter != YFilter.not_set or
                                    self.rtt.yfilter != YFilter.not_set or
                                    self.timeouts.yfilter != YFilter.not_set or
                                    self.unknown_packet_types.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "accounting" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.acct_incorrect_responses.is_set or self.acct_incorrect_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.acct_incorrect_responses.get_name_leafdata())
                                if (self.acct_response_time.is_set or self.acct_response_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.acct_response_time.get_name_leafdata())
                                if (self.acct_server_error_responses.is_set or self.acct_server_error_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.acct_server_error_responses.get_name_leafdata())
                                if (self.acct_transaction_failure.is_set or self.acct_transaction_failure.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.acct_transaction_failure.get_name_leafdata())
                                if (self.acct_transaction_successess.is_set or self.acct_transaction_successess.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.acct_transaction_successess.get_name_leafdata())
                                if (self.acct_unexpected_responses.is_set or self.acct_unexpected_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.acct_unexpected_responses.get_name_leafdata())
                                if (self.bad_authenticators.is_set or self.bad_authenticators.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bad_authenticators.get_name_leafdata())
                                if (self.bad_responses.is_set or self.bad_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bad_responses.get_name_leafdata())
                                if (self.dropped_responses.is_set or self.dropped_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dropped_responses.get_name_leafdata())
                                if (self.pending_requests.is_set or self.pending_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pending_requests.get_name_leafdata())
                                if (self.requests.is_set or self.requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.requests.get_name_leafdata())
                                if (self.responses.is_set or self.responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.responses.get_name_leafdata())
                                if (self.retransmits.is_set or self.retransmits.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.retransmits.get_name_leafdata())
                                if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rtt.get_name_leafdata())
                                if (self.timeouts.is_set or self.timeouts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.timeouts.get_name_leafdata())
                                if (self.unknown_packet_types.is_set or self.unknown_packet_types.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unknown_packet_types.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "acct-incorrect-responses" or name == "acct-response-time" or name == "acct-server-error-responses" or name == "acct-transaction-failure" or name == "acct-transaction-successess" or name == "acct-unexpected-responses" or name == "bad-authenticators" or name == "bad-responses" or name == "dropped-responses" or name == "pending-requests" or name == "requests" or name == "responses" or name == "retransmits" or name == "rtt" or name == "timeouts" or name == "unknown-packet-types"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "acct-incorrect-responses"):
                                    self.acct_incorrect_responses = value
                                    self.acct_incorrect_responses.value_namespace = name_space
                                    self.acct_incorrect_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "acct-response-time"):
                                    self.acct_response_time = value
                                    self.acct_response_time.value_namespace = name_space
                                    self.acct_response_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "acct-server-error-responses"):
                                    self.acct_server_error_responses = value
                                    self.acct_server_error_responses.value_namespace = name_space
                                    self.acct_server_error_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "acct-transaction-failure"):
                                    self.acct_transaction_failure = value
                                    self.acct_transaction_failure.value_namespace = name_space
                                    self.acct_transaction_failure.value_namespace_prefix = name_space_prefix
                                if(value_path == "acct-transaction-successess"):
                                    self.acct_transaction_successess = value
                                    self.acct_transaction_successess.value_namespace = name_space
                                    self.acct_transaction_successess.value_namespace_prefix = name_space_prefix
                                if(value_path == "acct-unexpected-responses"):
                                    self.acct_unexpected_responses = value
                                    self.acct_unexpected_responses.value_namespace = name_space
                                    self.acct_unexpected_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "bad-authenticators"):
                                    self.bad_authenticators = value
                                    self.bad_authenticators.value_namespace = name_space
                                    self.bad_authenticators.value_namespace_prefix = name_space_prefix
                                if(value_path == "bad-responses"):
                                    self.bad_responses = value
                                    self.bad_responses.value_namespace = name_space
                                    self.bad_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "dropped-responses"):
                                    self.dropped_responses = value
                                    self.dropped_responses.value_namespace = name_space
                                    self.dropped_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "pending-requests"):
                                    self.pending_requests = value
                                    self.pending_requests.value_namespace = name_space
                                    self.pending_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "requests"):
                                    self.requests = value
                                    self.requests.value_namespace = name_space
                                    self.requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "responses"):
                                    self.responses = value
                                    self.responses.value_namespace = name_space
                                    self.responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "retransmits"):
                                    self.retransmits = value
                                    self.retransmits.value_namespace = name_space
                                    self.retransmits.value_namespace_prefix = name_space_prefix
                                if(value_path == "rtt"):
                                    self.rtt = value
                                    self.rtt.value_namespace = name_space
                                    self.rtt.value_namespace_prefix = name_space_prefix
                                if(value_path == "timeouts"):
                                    self.timeouts = value
                                    self.timeouts.value_namespace = name_space
                                    self.timeouts.value_namespace_prefix = name_space_prefix
                                if(value_path == "unknown-packet-types"):
                                    self.unknown_packet_types = value
                                    self.unknown_packet_types.value_namespace = name_space
                                    self.unknown_packet_types.value_namespace_prefix = name_space_prefix


                        class Authentication(Entity):
                            """
                            Authentication data
                            
                            .. attribute:: access_accepts
                            
                            	Number of access accepts
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_challenges
                            
                            	Number of access challenges
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_rejects
                            
                            	Number of access rejects
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_request_retransmits
                            
                            	Number of retransmitted access requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_requests
                            
                            	Number of access requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: access_timeouts
                            
                            	Number of access packets timed out
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_incorrect_responses
                            
                            	Number of incorrect authentication responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_response_time
                            
                            	Average response time for authentication requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_server_error_responses
                            
                            	Number of server error authentication responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_transaction_failure
                            
                            	Number of failed authentication transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_transaction_successess
                            
                            	Number of succeeded authentication transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_unexpected_responses
                            
                            	Number of unexpected authentication responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_access_authenticators
                            
                            	Number of bad access authenticators
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_access_responses
                            
                            	Number of bad access responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dropped_access_responses
                            
                            	Number of access responses dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pending_access_requests
                            
                            	Number of pending access requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rtt
                            
                            	Round trip time for authentication in milliseconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: millisecond
                            
                            .. attribute:: unknown_access_types
                            
                            	Number of packets received with unknown type from authentication server
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authentication, self).__init__()

                                self.yang_name = "authentication"
                                self.yang_parent_name = "server-group"

                                self.access_accepts = YLeaf(YType.uint32, "access-accepts")

                                self.access_challenges = YLeaf(YType.uint32, "access-challenges")

                                self.access_rejects = YLeaf(YType.uint32, "access-rejects")

                                self.access_request_retransmits = YLeaf(YType.uint32, "access-request-retransmits")

                                self.access_requests = YLeaf(YType.uint32, "access-requests")

                                self.access_timeouts = YLeaf(YType.uint32, "access-timeouts")

                                self.authen_incorrect_responses = YLeaf(YType.uint32, "authen-incorrect-responses")

                                self.authen_response_time = YLeaf(YType.uint32, "authen-response-time")

                                self.authen_server_error_responses = YLeaf(YType.uint32, "authen-server-error-responses")

                                self.authen_transaction_failure = YLeaf(YType.uint32, "authen-transaction-failure")

                                self.authen_transaction_successess = YLeaf(YType.uint32, "authen-transaction-successess")

                                self.authen_unexpected_responses = YLeaf(YType.uint32, "authen-unexpected-responses")

                                self.bad_access_authenticators = YLeaf(YType.uint32, "bad-access-authenticators")

                                self.bad_access_responses = YLeaf(YType.uint32, "bad-access-responses")

                                self.dropped_access_responses = YLeaf(YType.uint32, "dropped-access-responses")

                                self.pending_access_requests = YLeaf(YType.uint32, "pending-access-requests")

                                self.rtt = YLeaf(YType.uint32, "rtt")

                                self.unknown_access_types = YLeaf(YType.uint32, "unknown-access-types")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("access_accepts",
                                                "access_challenges",
                                                "access_rejects",
                                                "access_request_retransmits",
                                                "access_requests",
                                                "access_timeouts",
                                                "authen_incorrect_responses",
                                                "authen_response_time",
                                                "authen_server_error_responses",
                                                "authen_transaction_failure",
                                                "authen_transaction_successess",
                                                "authen_unexpected_responses",
                                                "bad_access_authenticators",
                                                "bad_access_responses",
                                                "dropped_access_responses",
                                                "pending_access_requests",
                                                "rtt",
                                                "unknown_access_types") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authentication, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authentication, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.access_accepts.is_set or
                                    self.access_challenges.is_set or
                                    self.access_rejects.is_set or
                                    self.access_request_retransmits.is_set or
                                    self.access_requests.is_set or
                                    self.access_timeouts.is_set or
                                    self.authen_incorrect_responses.is_set or
                                    self.authen_response_time.is_set or
                                    self.authen_server_error_responses.is_set or
                                    self.authen_transaction_failure.is_set or
                                    self.authen_transaction_successess.is_set or
                                    self.authen_unexpected_responses.is_set or
                                    self.bad_access_authenticators.is_set or
                                    self.bad_access_responses.is_set or
                                    self.dropped_access_responses.is_set or
                                    self.pending_access_requests.is_set or
                                    self.rtt.is_set or
                                    self.unknown_access_types.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.access_accepts.yfilter != YFilter.not_set or
                                    self.access_challenges.yfilter != YFilter.not_set or
                                    self.access_rejects.yfilter != YFilter.not_set or
                                    self.access_request_retransmits.yfilter != YFilter.not_set or
                                    self.access_requests.yfilter != YFilter.not_set or
                                    self.access_timeouts.yfilter != YFilter.not_set or
                                    self.authen_incorrect_responses.yfilter != YFilter.not_set or
                                    self.authen_response_time.yfilter != YFilter.not_set or
                                    self.authen_server_error_responses.yfilter != YFilter.not_set or
                                    self.authen_transaction_failure.yfilter != YFilter.not_set or
                                    self.authen_transaction_successess.yfilter != YFilter.not_set or
                                    self.authen_unexpected_responses.yfilter != YFilter.not_set or
                                    self.bad_access_authenticators.yfilter != YFilter.not_set or
                                    self.bad_access_responses.yfilter != YFilter.not_set or
                                    self.dropped_access_responses.yfilter != YFilter.not_set or
                                    self.pending_access_requests.yfilter != YFilter.not_set or
                                    self.rtt.yfilter != YFilter.not_set or
                                    self.unknown_access_types.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "authentication" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.access_accepts.is_set or self.access_accepts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.access_accepts.get_name_leafdata())
                                if (self.access_challenges.is_set or self.access_challenges.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.access_challenges.get_name_leafdata())
                                if (self.access_rejects.is_set or self.access_rejects.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.access_rejects.get_name_leafdata())
                                if (self.access_request_retransmits.is_set or self.access_request_retransmits.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.access_request_retransmits.get_name_leafdata())
                                if (self.access_requests.is_set or self.access_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.access_requests.get_name_leafdata())
                                if (self.access_timeouts.is_set or self.access_timeouts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.access_timeouts.get_name_leafdata())
                                if (self.authen_incorrect_responses.is_set or self.authen_incorrect_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authen_incorrect_responses.get_name_leafdata())
                                if (self.authen_response_time.is_set or self.authen_response_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authen_response_time.get_name_leafdata())
                                if (self.authen_server_error_responses.is_set or self.authen_server_error_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authen_server_error_responses.get_name_leafdata())
                                if (self.authen_transaction_failure.is_set or self.authen_transaction_failure.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authen_transaction_failure.get_name_leafdata())
                                if (self.authen_transaction_successess.is_set or self.authen_transaction_successess.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authen_transaction_successess.get_name_leafdata())
                                if (self.authen_unexpected_responses.is_set or self.authen_unexpected_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authen_unexpected_responses.get_name_leafdata())
                                if (self.bad_access_authenticators.is_set or self.bad_access_authenticators.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bad_access_authenticators.get_name_leafdata())
                                if (self.bad_access_responses.is_set or self.bad_access_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bad_access_responses.get_name_leafdata())
                                if (self.dropped_access_responses.is_set or self.dropped_access_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dropped_access_responses.get_name_leafdata())
                                if (self.pending_access_requests.is_set or self.pending_access_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pending_access_requests.get_name_leafdata())
                                if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.rtt.get_name_leafdata())
                                if (self.unknown_access_types.is_set or self.unknown_access_types.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unknown_access_types.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "access-accepts" or name == "access-challenges" or name == "access-rejects" or name == "access-request-retransmits" or name == "access-requests" or name == "access-timeouts" or name == "authen-incorrect-responses" or name == "authen-response-time" or name == "authen-server-error-responses" or name == "authen-transaction-failure" or name == "authen-transaction-successess" or name == "authen-unexpected-responses" or name == "bad-access-authenticators" or name == "bad-access-responses" or name == "dropped-access-responses" or name == "pending-access-requests" or name == "rtt" or name == "unknown-access-types"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "access-accepts"):
                                    self.access_accepts = value
                                    self.access_accepts.value_namespace = name_space
                                    self.access_accepts.value_namespace_prefix = name_space_prefix
                                if(value_path == "access-challenges"):
                                    self.access_challenges = value
                                    self.access_challenges.value_namespace = name_space
                                    self.access_challenges.value_namespace_prefix = name_space_prefix
                                if(value_path == "access-rejects"):
                                    self.access_rejects = value
                                    self.access_rejects.value_namespace = name_space
                                    self.access_rejects.value_namespace_prefix = name_space_prefix
                                if(value_path == "access-request-retransmits"):
                                    self.access_request_retransmits = value
                                    self.access_request_retransmits.value_namespace = name_space
                                    self.access_request_retransmits.value_namespace_prefix = name_space_prefix
                                if(value_path == "access-requests"):
                                    self.access_requests = value
                                    self.access_requests.value_namespace = name_space
                                    self.access_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "access-timeouts"):
                                    self.access_timeouts = value
                                    self.access_timeouts.value_namespace = name_space
                                    self.access_timeouts.value_namespace_prefix = name_space_prefix
                                if(value_path == "authen-incorrect-responses"):
                                    self.authen_incorrect_responses = value
                                    self.authen_incorrect_responses.value_namespace = name_space
                                    self.authen_incorrect_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "authen-response-time"):
                                    self.authen_response_time = value
                                    self.authen_response_time.value_namespace = name_space
                                    self.authen_response_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "authen-server-error-responses"):
                                    self.authen_server_error_responses = value
                                    self.authen_server_error_responses.value_namespace = name_space
                                    self.authen_server_error_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "authen-transaction-failure"):
                                    self.authen_transaction_failure = value
                                    self.authen_transaction_failure.value_namespace = name_space
                                    self.authen_transaction_failure.value_namespace_prefix = name_space_prefix
                                if(value_path == "authen-transaction-successess"):
                                    self.authen_transaction_successess = value
                                    self.authen_transaction_successess.value_namespace = name_space
                                    self.authen_transaction_successess.value_namespace_prefix = name_space_prefix
                                if(value_path == "authen-unexpected-responses"):
                                    self.authen_unexpected_responses = value
                                    self.authen_unexpected_responses.value_namespace = name_space
                                    self.authen_unexpected_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "bad-access-authenticators"):
                                    self.bad_access_authenticators = value
                                    self.bad_access_authenticators.value_namespace = name_space
                                    self.bad_access_authenticators.value_namespace_prefix = name_space_prefix
                                if(value_path == "bad-access-responses"):
                                    self.bad_access_responses = value
                                    self.bad_access_responses.value_namespace = name_space
                                    self.bad_access_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "dropped-access-responses"):
                                    self.dropped_access_responses = value
                                    self.dropped_access_responses.value_namespace = name_space
                                    self.dropped_access_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "pending-access-requests"):
                                    self.pending_access_requests = value
                                    self.pending_access_requests.value_namespace = name_space
                                    self.pending_access_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "rtt"):
                                    self.rtt = value
                                    self.rtt.value_namespace = name_space
                                    self.rtt.value_namespace_prefix = name_space_prefix
                                if(value_path == "unknown-access-types"):
                                    self.unknown_access_types = value
                                    self.unknown_access_types.value_namespace = name_space
                                    self.unknown_access_types.value_namespace_prefix = name_space_prefix


                        class Authorization(Entity):
                            """
                            Authorization data
                            
                            .. attribute:: author_incorrect_responses
                            
                            	Number of incorrect authorization responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_request_timeouts
                            
                            	Number of access packets timed out
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_requests
                            
                            	Number of access requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_response_time
                            
                            	Average response time for authorization requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_server_error_responses
                            
                            	Number of server error authorization responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_transaction_failure
                            
                            	Number of failed authorization transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_transaction_successess
                            
                            	Number of succeeded authorization transactions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: author_unexpected_responses
                            
                            	Number of unexpected authorization responses
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authorization, self).__init__()

                                self.yang_name = "authorization"
                                self.yang_parent_name = "server-group"

                                self.author_incorrect_responses = YLeaf(YType.uint32, "author-incorrect-responses")

                                self.author_request_timeouts = YLeaf(YType.uint32, "author-request-timeouts")

                                self.author_requests = YLeaf(YType.uint32, "author-requests")

                                self.author_response_time = YLeaf(YType.uint32, "author-response-time")

                                self.author_server_error_responses = YLeaf(YType.uint32, "author-server-error-responses")

                                self.author_transaction_failure = YLeaf(YType.uint32, "author-transaction-failure")

                                self.author_transaction_successess = YLeaf(YType.uint32, "author-transaction-successess")

                                self.author_unexpected_responses = YLeaf(YType.uint32, "author-unexpected-responses")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("author_incorrect_responses",
                                                "author_request_timeouts",
                                                "author_requests",
                                                "author_response_time",
                                                "author_server_error_responses",
                                                "author_transaction_failure",
                                                "author_transaction_successess",
                                                "author_unexpected_responses") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authorization, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authorization, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.author_incorrect_responses.is_set or
                                    self.author_request_timeouts.is_set or
                                    self.author_requests.is_set or
                                    self.author_response_time.is_set or
                                    self.author_server_error_responses.is_set or
                                    self.author_transaction_failure.is_set or
                                    self.author_transaction_successess.is_set or
                                    self.author_unexpected_responses.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.author_incorrect_responses.yfilter != YFilter.not_set or
                                    self.author_request_timeouts.yfilter != YFilter.not_set or
                                    self.author_requests.yfilter != YFilter.not_set or
                                    self.author_response_time.yfilter != YFilter.not_set or
                                    self.author_server_error_responses.yfilter != YFilter.not_set or
                                    self.author_transaction_failure.yfilter != YFilter.not_set or
                                    self.author_transaction_successess.yfilter != YFilter.not_set or
                                    self.author_unexpected_responses.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "authorization" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.author_incorrect_responses.is_set or self.author_incorrect_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.author_incorrect_responses.get_name_leafdata())
                                if (self.author_request_timeouts.is_set or self.author_request_timeouts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.author_request_timeouts.get_name_leafdata())
                                if (self.author_requests.is_set or self.author_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.author_requests.get_name_leafdata())
                                if (self.author_response_time.is_set or self.author_response_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.author_response_time.get_name_leafdata())
                                if (self.author_server_error_responses.is_set or self.author_server_error_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.author_server_error_responses.get_name_leafdata())
                                if (self.author_transaction_failure.is_set or self.author_transaction_failure.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.author_transaction_failure.get_name_leafdata())
                                if (self.author_transaction_successess.is_set or self.author_transaction_successess.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.author_transaction_successess.get_name_leafdata())
                                if (self.author_unexpected_responses.is_set or self.author_unexpected_responses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.author_unexpected_responses.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "author-incorrect-responses" or name == "author-request-timeouts" or name == "author-requests" or name == "author-response-time" or name == "author-server-error-responses" or name == "author-transaction-failure" or name == "author-transaction-successess" or name == "author-unexpected-responses"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "author-incorrect-responses"):
                                    self.author_incorrect_responses = value
                                    self.author_incorrect_responses.value_namespace = name_space
                                    self.author_incorrect_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "author-request-timeouts"):
                                    self.author_request_timeouts = value
                                    self.author_request_timeouts.value_namespace = name_space
                                    self.author_request_timeouts.value_namespace_prefix = name_space_prefix
                                if(value_path == "author-requests"):
                                    self.author_requests = value
                                    self.author_requests.value_namespace = name_space
                                    self.author_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "author-response-time"):
                                    self.author_response_time = value
                                    self.author_response_time.value_namespace = name_space
                                    self.author_response_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "author-server-error-responses"):
                                    self.author_server_error_responses = value
                                    self.author_server_error_responses.value_namespace = name_space
                                    self.author_server_error_responses.value_namespace_prefix = name_space_prefix
                                if(value_path == "author-transaction-failure"):
                                    self.author_transaction_failure = value
                                    self.author_transaction_failure.value_namespace = name_space
                                    self.author_transaction_failure.value_namespace_prefix = name_space_prefix
                                if(value_path == "author-transaction-successess"):
                                    self.author_transaction_successess = value
                                    self.author_transaction_successess.value_namespace = name_space
                                    self.author_transaction_successess.value_namespace_prefix = name_space_prefix
                                if(value_path == "author-unexpected-responses"):
                                    self.author_unexpected_responses = value
                                    self.author_unexpected_responses.value_namespace = name_space
                                    self.author_unexpected_responses.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.accounting_port.is_set or
                                self.authentication_port.is_set or
                                self.family.is_set or
                                self.ip_address.is_set or
                                self.is_private.is_set or
                                self.server_address.is_set or
                                (self.accounting is not None and self.accounting.has_data()) or
                                (self.authentication is not None and self.authentication.has_data()) or
                                (self.authorization is not None and self.authorization.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.accounting_port.yfilter != YFilter.not_set or
                                self.authentication_port.yfilter != YFilter.not_set or
                                self.family.yfilter != YFilter.not_set or
                                self.ip_address.yfilter != YFilter.not_set or
                                self.is_private.yfilter != YFilter.not_set or
                                self.server_address.yfilter != YFilter.not_set or
                                (self.accounting is not None and self.accounting.has_operation()) or
                                (self.authentication is not None and self.authentication.has_operation()) or
                                (self.authorization is not None and self.authorization.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "server-group" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.accounting_port.is_set or self.accounting_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.accounting_port.get_name_leafdata())
                            if (self.authentication_port.is_set or self.authentication_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.authentication_port.get_name_leafdata())
                            if (self.family.is_set or self.family.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.family.get_name_leafdata())
                            if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_address.get_name_leafdata())
                            if (self.is_private.is_set or self.is_private.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_private.get_name_leafdata())
                            if (self.server_address.is_set or self.server_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.server_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "accounting"):
                                if (self.accounting is None):
                                    self.accounting = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Accounting()
                                    self.accounting.parent = self
                                    self._children_name_map["accounting"] = "accounting"
                                return self.accounting

                            if (child_yang_name == "authentication"):
                                if (self.authentication is None):
                                    self.authentication = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authentication()
                                    self.authentication.parent = self
                                    self._children_name_map["authentication"] = "authentication"
                                return self.authentication

                            if (child_yang_name == "authorization"):
                                if (self.authorization is None):
                                    self.authorization = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup.Authorization()
                                    self.authorization.parent = self
                                    self._children_name_map["authorization"] = "authorization"
                                return self.authorization

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "accounting" or name == "authentication" or name == "authorization" or name == "accounting-port" or name == "authentication-port" or name == "family" or name == "ip-address" or name == "is-private" or name == "server-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "accounting-port"):
                                self.accounting_port = value
                                self.accounting_port.value_namespace = name_space
                                self.accounting_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "authentication-port"):
                                self.authentication_port = value
                                self.authentication_port.value_namespace = name_space
                                self.authentication_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "family"):
                                self.family = value
                                self.family.value_namespace = name_space
                                self.family.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-address"):
                                self.ip_address = value
                                self.ip_address.value_namespace = name_space
                                self.ip_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-private"):
                                self.is_private = value
                                self.is_private.value_namespace = name_space
                                self.is_private.value_namespace_prefix = name_space_prefix
                            if(value_path == "server-address"):
                                self.server_address = value
                                self.server_address.value_namespace = name_space
                                self.server_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.server_group:
                            if (c.has_data()):
                                return True
                        return (
                            self.server_group_name.is_set or
                            self.dead_time.is_set or
                            self.groups.is_set or
                            self.servers.is_set or
                            self.vrf_name.is_set)

                    def has_operation(self):
                        for c in self.server_group:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.server_group_name.yfilter != YFilter.not_set or
                            self.dead_time.yfilter != YFilter.not_set or
                            self.groups.yfilter != YFilter.not_set or
                            self.servers.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "server-group" + "[server-group-name='" + self.server_group_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.server_group_name.is_set or self.server_group_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.server_group_name.get_name_leafdata())
                        if (self.dead_time.is_set or self.dead_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dead_time.get_name_leafdata())
                        if (self.groups.is_set or self.groups.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.groups.get_name_leafdata())
                        if (self.servers.is_set or self.servers.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.servers.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "server-group"):
                            for c in self.server_group:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.server_group.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "server-group" or name == "server-group-name" or name == "dead-time" or name == "groups" or name == "servers" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "server-group-name"):
                            self.server_group_name = value
                            self.server_group_name.value_namespace = name_space
                            self.server_group_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "dead-time"):
                            self.dead_time = value
                            self.dead_time.value_namespace = name_space
                            self.dead_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "groups"):
                            self.groups = value
                            self.groups.value_namespace = name_space
                            self.groups.value_namespace_prefix = name_space_prefix
                        if(value_path == "servers"):
                            self.servers = value
                            self.servers.value_namespace = name_space
                            self.servers.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.server_group:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.server_group:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "server-groups" + path_buffer

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

                    if (child_yang_name == "server-group"):
                        for c in self.server_group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Radius.Nodes.Node.ServerGroups.ServerGroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.server_group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "server-group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class DynamicAuthorization(Entity):
                """
                Dynamic authorization data
                
                .. attribute:: disconnected_invalid_requests
                
                	Invalid disconnected requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_coa_requests
                
                	Invalid change of authorization requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Radius.Nodes.Node.DynamicAuthorization, self).__init__()

                    self.yang_name = "dynamic-authorization"
                    self.yang_parent_name = "node"

                    self.disconnected_invalid_requests = YLeaf(YType.uint32, "disconnected-invalid-requests")

                    self.invalid_coa_requests = YLeaf(YType.uint32, "invalid-coa-requests")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("disconnected_invalid_requests",
                                    "invalid_coa_requests") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Radius.Nodes.Node.DynamicAuthorization, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Radius.Nodes.Node.DynamicAuthorization, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.disconnected_invalid_requests.is_set or
                        self.invalid_coa_requests.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.disconnected_invalid_requests.yfilter != YFilter.not_set or
                        self.invalid_coa_requests.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "dynamic-authorization" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.disconnected_invalid_requests.is_set or self.disconnected_invalid_requests.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disconnected_invalid_requests.get_name_leafdata())
                    if (self.invalid_coa_requests.is_set or self.invalid_coa_requests.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invalid_coa_requests.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "disconnected-invalid-requests" or name == "invalid-coa-requests"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "disconnected-invalid-requests"):
                        self.disconnected_invalid_requests = value
                        self.disconnected_invalid_requests.value_namespace = name_space
                        self.disconnected_invalid_requests.value_namespace_prefix = name_space_prefix
                    if(value_path == "invalid-coa-requests"):
                        self.invalid_coa_requests = value
                        self.invalid_coa_requests.value_namespace = name_space
                        self.invalid_coa_requests.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.accounting is not None and self.accounting.has_data()) or
                    (self.authentication is not None and self.authentication.has_data()) or
                    (self.client is not None and self.client.has_data()) or
                    (self.dead_criteria is not None and self.dead_criteria.has_data()) or
                    (self.dynamic_authorization is not None and self.dynamic_authorization.has_data()) or
                    (self.server_groups is not None and self.server_groups.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.accounting is not None and self.accounting.has_operation()) or
                    (self.authentication is not None and self.authentication.has_operation()) or
                    (self.client is not None and self.client.has_operation()) or
                    (self.dead_criteria is not None and self.dead_criteria.has_operation()) or
                    (self.dynamic_authorization is not None and self.dynamic_authorization.has_operation()) or
                    (self.server_groups is not None and self.server_groups.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-protocol-radius-oper:radius/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "accounting"):
                    if (self.accounting is None):
                        self.accounting = Radius.Nodes.Node.Accounting()
                        self.accounting.parent = self
                        self._children_name_map["accounting"] = "accounting"
                    return self.accounting

                if (child_yang_name == "authentication"):
                    if (self.authentication is None):
                        self.authentication = Radius.Nodes.Node.Authentication()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"
                    return self.authentication

                if (child_yang_name == "client"):
                    if (self.client is None):
                        self.client = Radius.Nodes.Node.Client()
                        self.client.parent = self
                        self._children_name_map["client"] = "client"
                    return self.client

                if (child_yang_name == "dead-criteria"):
                    if (self.dead_criteria is None):
                        self.dead_criteria = Radius.Nodes.Node.DeadCriteria()
                        self.dead_criteria.parent = self
                        self._children_name_map["dead_criteria"] = "dead-criteria"
                    return self.dead_criteria

                if (child_yang_name == "dynamic-authorization"):
                    if (self.dynamic_authorization is None):
                        self.dynamic_authorization = Radius.Nodes.Node.DynamicAuthorization()
                        self.dynamic_authorization.parent = self
                        self._children_name_map["dynamic_authorization"] = "dynamic-authorization"
                    return self.dynamic_authorization

                if (child_yang_name == "server-groups"):
                    if (self.server_groups is None):
                        self.server_groups = Radius.Nodes.Node.ServerGroups()
                        self.server_groups.parent = self
                        self._children_name_map["server_groups"] = "server-groups"
                    return self.server_groups

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "accounting" or name == "authentication" or name == "client" or name == "dead-criteria" or name == "dynamic-authorization" or name == "server-groups" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self.get_segment_path()
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
                c = Radius.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-aaa-protocol-radius-oper:radius" + path_buffer

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
                self.nodes = Radius.Nodes()
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
        self._top_entity = Radius()
        return self._top_entity

