""" Cisco_IOS_XR_infra_serg_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-serg package operational data.

This module contains definitions
for the following management objects\:
  session\-redundancy\-manager\: Session Redundancy Manager
    information
  session\-redundancy\-agent\: session redundancy agent

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SergPeerStatus(Enum):
    """
    SergPeerStatus

    SERG Peer Status

    .. data:: not_configured = 0

    	Peer not configured

    .. data:: initialize = 1

    	Peer initialization

    .. data:: retry = 2

    	Peer retry pending

    .. data:: connect = 3

    	Connection in Progress

    .. data:: listen = 4

    	Listening in Progress

    .. data:: registration = 5

    	Awaiting Registration from Peer

    .. data:: cleanup = 6

    	Peer cleanup in progress

    .. data:: connected = 7

    	Peer Connected

    .. data:: established = 8

    	Peer Established

    """

    not_configured = Enum.YLeaf(0, "not-configured")

    initialize = Enum.YLeaf(1, "initialize")

    retry = Enum.YLeaf(2, "retry")

    connect = Enum.YLeaf(3, "connect")

    listen = Enum.YLeaf(4, "listen")

    registration = Enum.YLeaf(5, "registration")

    cleanup = Enum.YLeaf(6, "cleanup")

    connected = Enum.YLeaf(7, "connected")

    established = Enum.YLeaf(8, "established")


class SergShowComp(Enum):
    """
    SergShowComp

    SERG Components

    .. data:: serga = 0

    	SERG Agent

    .. data:: ipv6nd = 1

    	IPv6ND

    .. data:: dhcpv6 = 2

    	DHCPv6

    """

    serga = Enum.YLeaf(0, "serga")

    ipv6nd = Enum.YLeaf(1, "ipv6nd")

    dhcpv6 = Enum.YLeaf(2, "dhcpv6")


class SergShowImRole(Enum):
    """
    SergShowImRole

    SERG Interface Management Role

    .. data:: none = 0

    	Not Determined

    .. data:: master = 1

    	Master Role

    .. data:: slave = 2

    	Slave Role

    """

    none = Enum.YLeaf(0, "none")

    master = Enum.YLeaf(1, "master")

    slave = Enum.YLeaf(2, "slave")


class SergShowMem(Enum):
    """
    SergShowMem

    SERG Memory Manager type

    .. data:: standard = 0

    	Standard type

    .. data:: chunk = 1

    	Chunk type

    .. data:: edm = 2

    	EDM type

    .. data:: string = 3

    	String type

    .. data:: static = 4

    	Static type

    .. data:: unknown = 5

    	Unknown type

    """

    standard = Enum.YLeaf(0, "standard")

    chunk = Enum.YLeaf(1, "chunk")

    edm = Enum.YLeaf(2, "edm")

    string = Enum.YLeaf(3, "string")

    static = Enum.YLeaf(4, "static")

    unknown = Enum.YLeaf(5, "unknown")


class SergShowRole(Enum):
    """
    SergShowRole

    SERG Role

    .. data:: none = 0

    	Not Configured

    .. data:: master = 1

    	Master Role

    .. data:: slave = 2

    	Slave Role

    """

    none = Enum.YLeaf(0, "none")

    master = Enum.YLeaf(1, "master")

    slave = Enum.YLeaf(2, "slave")


class SergShowSessionError(Enum):
    """
    SergShowSessionError

    SERG Session Error Operation

    .. data:: none = 0

    	Invalid Error

    .. data:: hard = 1

    	Hard Error

    .. data:: soft = 2

    	Soft Error

    """

    none = Enum.YLeaf(0, "none")

    hard = Enum.YLeaf(1, "hard")

    soft = Enum.YLeaf(2, "soft")


class SergShowSessionOperation(Enum):
    """
    SergShowSessionOperation

    SERG Session Operation

    .. data:: none = 0

    	No Operation

    .. data:: update = 1

    	SERG Session Update Operation

    .. data:: delete = 2

    	SERG Session Delete Operation

    .. data:: in_sync = 3

    	SERG Session In Sync

    """

    none = Enum.YLeaf(0, "none")

    update = Enum.YLeaf(1, "update")

    delete = Enum.YLeaf(2, "delete")

    in_sync = Enum.YLeaf(3, "in-sync")


class SergShowSlaveMode(Enum):
    """
    SergShowSlaveMode

    SERG Slave Mode

    .. data:: none = 0

    	Not Configured

    .. data:: warm = 1

    	Warm Modem

    .. data:: hot = 2

    	Hot Mode

    """

    none = Enum.YLeaf(0, "none")

    warm = Enum.YLeaf(1, "warm")

    hot = Enum.YLeaf(2, "hot")


class SergShowSoReason(Enum):
    """
    SergShowSoReason

    Session Redundancy Switchover Reason

    .. data:: internal = 0

    	SwitchOver for Internal Reason

    .. data:: admin = 1

    	SwitchOver for Admin

    .. data:: peer_up = 2

    	SwitchOver for Peer UP

    .. data:: peer_down = 3

    	SwitchOver for Peer Down

    .. data:: object_tracking_status_change = 4

    	SwitchOver for Object Tracking status change

    .. data:: serg_show_so_reason_max = 5

    	Unknown Switchover Reason

    """

    internal = Enum.YLeaf(0, "internal")

    admin = Enum.YLeaf(1, "admin")

    peer_up = Enum.YLeaf(2, "peer-up")

    peer_down = Enum.YLeaf(3, "peer-down")

    object_tracking_status_change = Enum.YLeaf(4, "object-tracking-status-change")

    serg_show_so_reason_max = Enum.YLeaf(5, "serg-show-so-reason-max")



class SessionRedundancyManager(Entity):
    """
    Session Redundancy Manager information
    
    .. attribute:: groups
    
    	Session Redundancy Manager group table
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Groups>`
    
    .. attribute:: interfaces
    
    	Subscriber Redundancy Manager interface table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Interfaces>`
    
    .. attribute:: summary
    
    	Session redundancy manager summary
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Summary>`
    
    

    """

    _prefix = 'infra-serg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SessionRedundancyManager, self).__init__()
        self._top_entity = None

        self.yang_name = "session-redundancy-manager"
        self.yang_parent_name = "Cisco-IOS-XR-infra-serg-oper"

        self.groups = SessionRedundancyManager.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._children_yang_names.add("groups")

        self.interfaces = SessionRedundancyManager.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.summary = SessionRedundancyManager.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")


    class Interfaces(Entity):
        """
        Subscriber Redundancy Manager interface table
        
        .. attribute:: interface
        
        	interface redundancy manager interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancyManager.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "session-redundancy-manager"

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
                        super(SessionRedundancyManager.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SessionRedundancyManager.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            interface redundancy manager interface
            
            .. attribute:: interface  <key>
            
            	Interface
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: forward_referenced
            
            	Forward Referenced
            	**type**\:  bool
            
            .. attribute:: group_id
            
            	Group ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_mapping_id
            
            	Interface Mapping ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name
            
            	Interface Name
            	**type**\:  str
            
            .. attribute:: role
            
            	SERG Role
            	**type**\:   :py:class:`SergShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRole>`
            
            

            """

            _prefix = 'infra-serg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SessionRedundancyManager.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface = YLeaf(YType.str, "interface")

                self.forward_referenced = YLeaf(YType.boolean, "forward-referenced")

                self.group_id = YLeaf(YType.uint32, "group-id")

                self.interface_mapping_id = YLeaf(YType.uint32, "interface-mapping-id")

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.role = YLeaf(YType.enumeration, "role")

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
                                "forward_referenced",
                                "group_id",
                                "interface_mapping_id",
                                "interface_name",
                                "role") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SessionRedundancyManager.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SessionRedundancyManager.Interfaces.Interface, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.interface.is_set or
                    self.forward_referenced.is_set or
                    self.group_id.is_set or
                    self.interface_mapping_id.is_set or
                    self.interface_name.is_set or
                    self.role.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface.yfilter != YFilter.not_set or
                    self.forward_referenced.yfilter != YFilter.not_set or
                    self.group_id.yfilter != YFilter.not_set or
                    self.interface_mapping_id.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.role.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface='" + self.interface.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface.get_name_leafdata())
                if (self.forward_referenced.is_set or self.forward_referenced.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.forward_referenced.get_name_leafdata())
                if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.group_id.get_name_leafdata())
                if (self.interface_mapping_id.is_set or self.interface_mapping_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_mapping_id.get_name_leafdata())
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.role.is_set or self.role.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.role.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface" or name == "forward-referenced" or name == "group-id" or name == "interface-mapping-id" or name == "interface-name" or name == "role"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface"):
                    self.interface = value
                    self.interface.value_namespace = name_space
                    self.interface.value_namespace_prefix = name_space_prefix
                if(value_path == "forward-referenced"):
                    self.forward_referenced = value
                    self.forward_referenced.value_namespace = name_space
                    self.forward_referenced.value_namespace_prefix = name_space_prefix
                if(value_path == "group-id"):
                    self.group_id = value
                    self.group_id.value_namespace = name_space
                    self.group_id.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-mapping-id"):
                    self.interface_mapping_id = value
                    self.interface_mapping_id.value_namespace = name_space
                    self.interface_mapping_id.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "role"):
                    self.role = value
                    self.role.value_namespace = name_space
                    self.role.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/%s" % self.get_segment_path()
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
                c = SessionRedundancyManager.Interfaces.Interface()
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


    class Groups(Entity):
        """
        Session Redundancy Manager group table
        
        .. attribute:: group
        
        	Session redundancy manager group
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Groups.Group>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancyManager.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "session-redundancy-manager"

            self.group = YList(self)

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
                        super(SessionRedundancyManager.Groups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SessionRedundancyManager.Groups, self).__setattr__(name, value)


        class Group(Entity):
            """
            Session redundancy manager group
            
            .. attribute:: group  <key>
            
            	Group
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: description
            
            	Group Description
            	**type**\:  str
            
            .. attribute:: disabled
            
            	Disabled by Config
            	**type**\:  bool
            
            .. attribute:: group_id
            
            	Group ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_count
            
            	Interface Count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_name
            
            	Node Information
            	**type**\:  str
            
            .. attribute:: object_tracking_status
            
            	Object Tracking Status (Enabled/Disabled)
            	**type**\:  bool
            
            .. attribute:: peer_ipv4_address
            
            	Peer IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_ipv6_address
            
            	Peer IPv6 Address
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: preferred_role
            
            	Preferred Role
            	**type**\:   :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
            
            .. attribute:: role
            
            	SERG Role
            	**type**\:   :py:class:`SergShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRole>`
            
            .. attribute:: slave_mode
            
            	Slave Mode
            	**type**\:   :py:class:`SergShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveMode>`
            
            

            """

            _prefix = 'infra-serg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SessionRedundancyManager.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"

                self.group = YLeaf(YType.str, "group")

                self.description = YLeaf(YType.str, "description")

                self.disabled = YLeaf(YType.boolean, "disabled")

                self.group_id = YLeaf(YType.uint32, "group-id")

                self.interface_count = YLeaf(YType.uint32, "interface-count")

                self.node_name = YLeaf(YType.str, "node-name")

                self.object_tracking_status = YLeaf(YType.boolean, "object-tracking-status")

                self.peer_ipv4_address = YLeaf(YType.str, "peer-ipv4-address")

                self.peer_ipv6_address = YLeaf(YType.str, "peer-ipv6-address")

                self.preferred_role = YLeaf(YType.enumeration, "preferred-role")

                self.role = YLeaf(YType.enumeration, "role")

                self.slave_mode = YLeaf(YType.enumeration, "slave-mode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("group",
                                "description",
                                "disabled",
                                "group_id",
                                "interface_count",
                                "node_name",
                                "object_tracking_status",
                                "peer_ipv4_address",
                                "peer_ipv6_address",
                                "preferred_role",
                                "role",
                                "slave_mode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SessionRedundancyManager.Groups.Group, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SessionRedundancyManager.Groups.Group, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.group.is_set or
                    self.description.is_set or
                    self.disabled.is_set or
                    self.group_id.is_set or
                    self.interface_count.is_set or
                    self.node_name.is_set or
                    self.object_tracking_status.is_set or
                    self.peer_ipv4_address.is_set or
                    self.peer_ipv6_address.is_set or
                    self.preferred_role.is_set or
                    self.role.is_set or
                    self.slave_mode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.group.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    self.disabled.yfilter != YFilter.not_set or
                    self.group_id.yfilter != YFilter.not_set or
                    self.interface_count.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    self.object_tracking_status.yfilter != YFilter.not_set or
                    self.peer_ipv4_address.yfilter != YFilter.not_set or
                    self.peer_ipv6_address.yfilter != YFilter.not_set or
                    self.preferred_role.yfilter != YFilter.not_set or
                    self.role.yfilter != YFilter.not_set or
                    self.slave_mode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "group" + "[group='" + self.group.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.group.get_name_leafdata())
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())
                if (self.disabled.is_set or self.disabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disabled.get_name_leafdata())
                if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.group_id.get_name_leafdata())
                if (self.interface_count.is_set or self.interface_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_count.get_name_leafdata())
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())
                if (self.object_tracking_status.is_set or self.object_tracking_status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.object_tracking_status.get_name_leafdata())
                if (self.peer_ipv4_address.is_set or self.peer_ipv4_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.peer_ipv4_address.get_name_leafdata())
                if (self.peer_ipv6_address.is_set or self.peer_ipv6_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.peer_ipv6_address.get_name_leafdata())
                if (self.preferred_role.is_set or self.preferred_role.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.preferred_role.get_name_leafdata())
                if (self.role.is_set or self.role.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.role.get_name_leafdata())
                if (self.slave_mode.is_set or self.slave_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.slave_mode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "group" or name == "description" or name == "disabled" or name == "group-id" or name == "interface-count" or name == "node-name" or name == "object-tracking-status" or name == "peer-ipv4-address" or name == "peer-ipv6-address" or name == "preferred-role" or name == "role" or name == "slave-mode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "group"):
                    self.group = value
                    self.group.value_namespace = name_space
                    self.group.value_namespace_prefix = name_space_prefix
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix
                if(value_path == "disabled"):
                    self.disabled = value
                    self.disabled.value_namespace = name_space
                    self.disabled.value_namespace_prefix = name_space_prefix
                if(value_path == "group-id"):
                    self.group_id = value
                    self.group_id.value_namespace = name_space
                    self.group_id.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-count"):
                    self.interface_count = value
                    self.interface_count.value_namespace = name_space
                    self.interface_count.value_namespace_prefix = name_space_prefix
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix
                if(value_path == "object-tracking-status"):
                    self.object_tracking_status = value
                    self.object_tracking_status.value_namespace = name_space
                    self.object_tracking_status.value_namespace_prefix = name_space_prefix
                if(value_path == "peer-ipv4-address"):
                    self.peer_ipv4_address = value
                    self.peer_ipv4_address.value_namespace = name_space
                    self.peer_ipv4_address.value_namespace_prefix = name_space_prefix
                if(value_path == "peer-ipv6-address"):
                    self.peer_ipv6_address = value
                    self.peer_ipv6_address.value_namespace = name_space
                    self.peer_ipv6_address.value_namespace_prefix = name_space_prefix
                if(value_path == "preferred-role"):
                    self.preferred_role = value
                    self.preferred_role.value_namespace = name_space
                    self.preferred_role.value_namespace_prefix = name_space_prefix
                if(value_path == "role"):
                    self.role = value
                    self.role.value_namespace = name_space
                    self.role.value_namespace_prefix = name_space_prefix
                if(value_path == "slave-mode"):
                    self.slave_mode = value
                    self.slave_mode.value_namespace = name_space
                    self.slave_mode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.group:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.group:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "groups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "group"):
                for c in self.group:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SessionRedundancyManager.Groups.Group()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.group.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "group"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Summary(Entity):
        """
        Session redundancy manager summary
        
        .. attribute:: active_state
        
        	Process Active State
        	**type**\:  bool
        
        .. attribute:: disabled
        
        	Disabled by Config
        	**type**\:  bool
        
        .. attribute:: disabled_group_count
        
        	No. of Disabled Groups by Config
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: group_count
        
        	No. of Configured Groups
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: hold_timer
        
        	Switch Over Hold Time
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface_count
        
        	No. of Configured Interfaces
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: master_group_count
        
        	No. of Master/Active Groups
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: master_interface_count
        
        	No. of Master/Active Interfaces
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: preferred_role
        
        	Preferred Role
        	**type**\:   :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
        
        .. attribute:: slave_group_count
        
        	No. of Slave Groups
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: slave_interface_count
        
        	No. of Slave Interfaces
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: slave_mode
        
        	Slave Mode
        	**type**\:   :py:class:`SergShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveMode>`
        
        .. attribute:: source_interface_ipv4_address
        
        	Source Interface IPv4 Address
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: source_interface_ipv6_address
        
        	Source Interface IPv6 Address
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: source_interface_name
        
        	Source Interface Name
        	**type**\:  str
        
        .. attribute:: vrf_name
        
        	VRF Name
        	**type**\:  str
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancyManager.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "session-redundancy-manager"

            self.active_state = YLeaf(YType.boolean, "active-state")

            self.disabled = YLeaf(YType.boolean, "disabled")

            self.disabled_group_count = YLeaf(YType.uint32, "disabled-group-count")

            self.group_count = YLeaf(YType.uint32, "group-count")

            self.hold_timer = YLeaf(YType.uint32, "hold-timer")

            self.interface_count = YLeaf(YType.uint32, "interface-count")

            self.master_group_count = YLeaf(YType.uint32, "master-group-count")

            self.master_interface_count = YLeaf(YType.uint32, "master-interface-count")

            self.preferred_role = YLeaf(YType.enumeration, "preferred-role")

            self.slave_group_count = YLeaf(YType.uint32, "slave-group-count")

            self.slave_interface_count = YLeaf(YType.uint32, "slave-interface-count")

            self.slave_mode = YLeaf(YType.enumeration, "slave-mode")

            self.source_interface_ipv4_address = YLeaf(YType.str, "source-interface-ipv4-address")

            self.source_interface_ipv6_address = YLeaf(YType.str, "source-interface-ipv6-address")

            self.source_interface_name = YLeaf(YType.str, "source-interface-name")

            self.vrf_name = YLeaf(YType.str, "vrf-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("active_state",
                            "disabled",
                            "disabled_group_count",
                            "group_count",
                            "hold_timer",
                            "interface_count",
                            "master_group_count",
                            "master_interface_count",
                            "preferred_role",
                            "slave_group_count",
                            "slave_interface_count",
                            "slave_mode",
                            "source_interface_ipv4_address",
                            "source_interface_ipv6_address",
                            "source_interface_name",
                            "vrf_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SessionRedundancyManager.Summary, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SessionRedundancyManager.Summary, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.active_state.is_set or
                self.disabled.is_set or
                self.disabled_group_count.is_set or
                self.group_count.is_set or
                self.hold_timer.is_set or
                self.interface_count.is_set or
                self.master_group_count.is_set or
                self.master_interface_count.is_set or
                self.preferred_role.is_set or
                self.slave_group_count.is_set or
                self.slave_interface_count.is_set or
                self.slave_mode.is_set or
                self.source_interface_ipv4_address.is_set or
                self.source_interface_ipv6_address.is_set or
                self.source_interface_name.is_set or
                self.vrf_name.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.active_state.yfilter != YFilter.not_set or
                self.disabled.yfilter != YFilter.not_set or
                self.disabled_group_count.yfilter != YFilter.not_set or
                self.group_count.yfilter != YFilter.not_set or
                self.hold_timer.yfilter != YFilter.not_set or
                self.interface_count.yfilter != YFilter.not_set or
                self.master_group_count.yfilter != YFilter.not_set or
                self.master_interface_count.yfilter != YFilter.not_set or
                self.preferred_role.yfilter != YFilter.not_set or
                self.slave_group_count.yfilter != YFilter.not_set or
                self.slave_interface_count.yfilter != YFilter.not_set or
                self.slave_mode.yfilter != YFilter.not_set or
                self.source_interface_ipv4_address.yfilter != YFilter.not_set or
                self.source_interface_ipv6_address.yfilter != YFilter.not_set or
                self.source_interface_name.yfilter != YFilter.not_set or
                self.vrf_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "summary" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.active_state.is_set or self.active_state.yfilter != YFilter.not_set):
                leaf_name_data.append(self.active_state.get_name_leafdata())
            if (self.disabled.is_set or self.disabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.disabled.get_name_leafdata())
            if (self.disabled_group_count.is_set or self.disabled_group_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.disabled_group_count.get_name_leafdata())
            if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.group_count.get_name_leafdata())
            if (self.hold_timer.is_set or self.hold_timer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.hold_timer.get_name_leafdata())
            if (self.interface_count.is_set or self.interface_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interface_count.get_name_leafdata())
            if (self.master_group_count.is_set or self.master_group_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.master_group_count.get_name_leafdata())
            if (self.master_interface_count.is_set or self.master_interface_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.master_interface_count.get_name_leafdata())
            if (self.preferred_role.is_set or self.preferred_role.yfilter != YFilter.not_set):
                leaf_name_data.append(self.preferred_role.get_name_leafdata())
            if (self.slave_group_count.is_set or self.slave_group_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.slave_group_count.get_name_leafdata())
            if (self.slave_interface_count.is_set or self.slave_interface_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.slave_interface_count.get_name_leafdata())
            if (self.slave_mode.is_set or self.slave_mode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.slave_mode.get_name_leafdata())
            if (self.source_interface_ipv4_address.is_set or self.source_interface_ipv4_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_interface_ipv4_address.get_name_leafdata())
            if (self.source_interface_ipv6_address.is_set or self.source_interface_ipv6_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_interface_ipv6_address.get_name_leafdata())
            if (self.source_interface_name.is_set or self.source_interface_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_interface_name.get_name_leafdata())
            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vrf_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "active-state" or name == "disabled" or name == "disabled-group-count" or name == "group-count" or name == "hold-timer" or name == "interface-count" or name == "master-group-count" or name == "master-interface-count" or name == "preferred-role" or name == "slave-group-count" or name == "slave-interface-count" or name == "slave-mode" or name == "source-interface-ipv4-address" or name == "source-interface-ipv6-address" or name == "source-interface-name" or name == "vrf-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "active-state"):
                self.active_state = value
                self.active_state.value_namespace = name_space
                self.active_state.value_namespace_prefix = name_space_prefix
            if(value_path == "disabled"):
                self.disabled = value
                self.disabled.value_namespace = name_space
                self.disabled.value_namespace_prefix = name_space_prefix
            if(value_path == "disabled-group-count"):
                self.disabled_group_count = value
                self.disabled_group_count.value_namespace = name_space
                self.disabled_group_count.value_namespace_prefix = name_space_prefix
            if(value_path == "group-count"):
                self.group_count = value
                self.group_count.value_namespace = name_space
                self.group_count.value_namespace_prefix = name_space_prefix
            if(value_path == "hold-timer"):
                self.hold_timer = value
                self.hold_timer.value_namespace = name_space
                self.hold_timer.value_namespace_prefix = name_space_prefix
            if(value_path == "interface-count"):
                self.interface_count = value
                self.interface_count.value_namespace = name_space
                self.interface_count.value_namespace_prefix = name_space_prefix
            if(value_path == "master-group-count"):
                self.master_group_count = value
                self.master_group_count.value_namespace = name_space
                self.master_group_count.value_namespace_prefix = name_space_prefix
            if(value_path == "master-interface-count"):
                self.master_interface_count = value
                self.master_interface_count.value_namespace = name_space
                self.master_interface_count.value_namespace_prefix = name_space_prefix
            if(value_path == "preferred-role"):
                self.preferred_role = value
                self.preferred_role.value_namespace = name_space
                self.preferred_role.value_namespace_prefix = name_space_prefix
            if(value_path == "slave-group-count"):
                self.slave_group_count = value
                self.slave_group_count.value_namespace = name_space
                self.slave_group_count.value_namespace_prefix = name_space_prefix
            if(value_path == "slave-interface-count"):
                self.slave_interface_count = value
                self.slave_interface_count.value_namespace = name_space
                self.slave_interface_count.value_namespace_prefix = name_space_prefix
            if(value_path == "slave-mode"):
                self.slave_mode = value
                self.slave_mode.value_namespace = name_space
                self.slave_mode.value_namespace_prefix = name_space_prefix
            if(value_path == "source-interface-ipv4-address"):
                self.source_interface_ipv4_address = value
                self.source_interface_ipv4_address.value_namespace = name_space
                self.source_interface_ipv4_address.value_namespace_prefix = name_space_prefix
            if(value_path == "source-interface-ipv6-address"):
                self.source_interface_ipv6_address = value
                self.source_interface_ipv6_address.value_namespace = name_space
                self.source_interface_ipv6_address.value_namespace_prefix = name_space_prefix
            if(value_path == "source-interface-name"):
                self.source_interface_name = value
                self.source_interface_name.value_namespace = name_space
                self.source_interface_name.value_namespace_prefix = name_space_prefix
            if(value_path == "vrf-name"):
                self.vrf_name = value
                self.vrf_name.value_namespace = name_space
                self.vrf_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.groups is not None and self.groups.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.summary is not None and self.summary.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.groups is not None and self.groups.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.summary is not None and self.summary.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager" + path_buffer

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

        if (child_yang_name == "groups"):
            if (self.groups is None):
                self.groups = SessionRedundancyManager.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
            return self.groups

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = SessionRedundancyManager.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "summary"):
            if (self.summary is None):
                self.summary = SessionRedundancyManager.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
            return self.summary

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "groups" or name == "interfaces" or name == "summary"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SessionRedundancyManager()
        return self._top_entity

class SessionRedundancyAgent(Entity):
    """
    session redundancy agent
    
    .. attribute:: nodes
    
    	List of nodes for which session data is collected
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes>`
    
    

    """

    _prefix = 'infra-serg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SessionRedundancyAgent, self).__init__()
        self._top_entity = None

        self.yang_name = "session-redundancy-agent"
        self.yang_parent_name = "Cisco-IOS-XR-infra-serg-oper"

        self.nodes = SessionRedundancyAgent.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of nodes for which session data is
        collected
        
        .. attribute:: node
        
        	Session data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionRedundancyAgent.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "session-redundancy-agent"

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
                        super(SessionRedundancyAgent.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SessionRedundancyAgent.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Session data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: client_ids
            
            	Stats Client
            	**type**\:   :py:class:`ClientIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.ClientIds>`
            
            .. attribute:: group_id_xr
            
            	Data for particular subscriber group session
            	**type**\:   :py:class:`GroupIdXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr>`
            
            .. attribute:: group_ids
            
            	Data for particular subscriber group 
            	**type**\:   :py:class:`GroupIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds>`
            
            .. attribute:: group_summaries
            
            	Session data for a particular node
            	**type**\:   :py:class:`GroupSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupSummaries>`
            
            .. attribute:: interfaces
            
            	List of interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces>`
            
            .. attribute:: memory
            
            	Show Memory
            	**type**\:   :py:class:`Memory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory>`
            
            .. attribute:: stats_global
            
            	Stats Global
            	**type**\:   :py:class:`StatsGlobal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal>`
            
            

            """

            _prefix = 'infra-serg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SessionRedundancyAgent.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.client_ids = SessionRedundancyAgent.Nodes.Node.ClientIds()
                self.client_ids.parent = self
                self._children_name_map["client_ids"] = "client-ids"
                self._children_yang_names.add("client-ids")

                self.group_id_xr = SessionRedundancyAgent.Nodes.Node.GroupIdXr()
                self.group_id_xr.parent = self
                self._children_name_map["group_id_xr"] = "group-id-xr"
                self._children_yang_names.add("group-id-xr")

                self.group_ids = SessionRedundancyAgent.Nodes.Node.GroupIds()
                self.group_ids.parent = self
                self._children_name_map["group_ids"] = "group-ids"
                self._children_yang_names.add("group-ids")

                self.group_summaries = SessionRedundancyAgent.Nodes.Node.GroupSummaries()
                self.group_summaries.parent = self
                self._children_name_map["group_summaries"] = "group-summaries"
                self._children_yang_names.add("group-summaries")

                self.interfaces = SessionRedundancyAgent.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.memory = SessionRedundancyAgent.Nodes.Node.Memory()
                self.memory.parent = self
                self._children_name_map["memory"] = "memory"
                self._children_yang_names.add("memory")

                self.stats_global = SessionRedundancyAgent.Nodes.Node.StatsGlobal()
                self.stats_global.parent = self
                self._children_name_map["stats_global"] = "stats-global"
                self._children_yang_names.add("stats-global")

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
                            super(SessionRedundancyAgent.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SessionRedundancyAgent.Nodes.Node, self).__setattr__(name, value)


            class GroupIdXr(Entity):
                """
                Data for particular subscriber group session
                
                .. attribute:: group_id
                
                	Group id for subscriber group session
                	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.GroupIdXr, self).__init__()

                    self.yang_name = "group-id-xr"
                    self.yang_parent_name = "node"

                    self.group_id = YList(self)

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
                                super(SessionRedundancyAgent.Nodes.Node.GroupIdXr, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionRedundancyAgent.Nodes.Node.GroupIdXr, self).__setattr__(name, value)


                class GroupId(Entity):
                    """
                    Group id for subscriber group session
                    
                    .. attribute:: group_id  <key>
                    
                    	GroupId
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    .. attribute:: key_index
                    
                    	Key index
                    	**type**\:  str
                    
                    .. attribute:: negative_acknowledgement_update_all
                    
                    	Negative Acknowledgement Update Flag is Set
                    	**type**\:  bool
                    
                    .. attribute:: role_master
                    
                    	Master Role is Set
                    	**type**\:  bool
                    
                    .. attribute:: session_detailed_information
                    
                    	More Session Information
                    	**type**\: list of    :py:class:`SessionDetailedInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation>`
                    
                    .. attribute:: session_sync_error_information
                    
                    	Session Synchroniation Error Information
                    	**type**\: list of    :py:class:`SessionSyncErrorInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation>`
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, self).__init__()

                        self.yang_name = "group-id"
                        self.yang_parent_name = "group-id-xr"

                        self.group_id = YLeaf(YType.str, "group-id")

                        self.group_id_xr = YLeaf(YType.uint32, "group-id-xr")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.key_index = YLeaf(YType.str, "key-index")

                        self.negative_acknowledgement_update_all = YLeaf(YType.boolean, "negative-acknowledgement-update-all")

                        self.role_master = YLeaf(YType.boolean, "role-master")

                        self.session_detailed_information = YList(self)
                        self.session_sync_error_information = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("group_id",
                                        "group_id_xr",
                                        "interface_name",
                                        "key_index",
                                        "negative_acknowledgement_update_all",
                                        "role_master") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, self).__setattr__(name, value)


                    class SessionDetailedInformation(Entity):
                        """
                        More Session Information
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:   :py:class:`SergShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowComp>`
                        
                        .. attribute:: marked_for_cleanup
                        
                        	Marked For Cleanup
                        	**type**\:  bool
                        
                        .. attribute:: marked_for_sweeping
                        
                        	Marked For Sweeping
                        	**type**\:  bool
                        
                        .. attribute:: operation_
                        
                        	Operation Code
                        	**type**\:   :py:class:`SergShowSessionOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSessionOperation>`
                        
                        .. attribute:: tx_list_queue_fail
                        
                        	Tx List Queue Failed
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, self).__init__()

                            self.yang_name = "session-detailed-information"
                            self.yang_parent_name = "group-id"

                            self.component = YLeaf(YType.enumeration, "component")

                            self.marked_for_cleanup = YLeaf(YType.boolean, "marked-for-cleanup")

                            self.marked_for_sweeping = YLeaf(YType.boolean, "marked-for-sweeping")

                            self.operation_ = YLeaf(YType.enumeration, "operation")

                            self.tx_list_queue_fail = YLeaf(YType.boolean, "tx-list-queue-fail")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("component",
                                            "marked_for_cleanup",
                                            "marked_for_sweeping",
                                            "operation_",
                                            "tx_list_queue_fail") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.component.is_set or
                                self.marked_for_cleanup.is_set or
                                self.marked_for_sweeping.is_set or
                                self.operation_.is_set or
                                self.tx_list_queue_fail.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.component.yfilter != YFilter.not_set or
                                self.marked_for_cleanup.yfilter != YFilter.not_set or
                                self.marked_for_sweeping.yfilter != YFilter.not_set or
                                self.operation_.yfilter != YFilter.not_set or
                                self.tx_list_queue_fail.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "session-detailed-information" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.component.is_set or self.component.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.component.get_name_leafdata())
                            if (self.marked_for_cleanup.is_set or self.marked_for_cleanup.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.marked_for_cleanup.get_name_leafdata())
                            if (self.marked_for_sweeping.is_set or self.marked_for_sweeping.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.marked_for_sweeping.get_name_leafdata())
                            if (self.operation_.is_set or self.operation_.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.operation_.get_name_leafdata())
                            if (self.tx_list_queue_fail.is_set or self.tx_list_queue_fail.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tx_list_queue_fail.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "component" or name == "marked-for-cleanup" or name == "marked-for-sweeping" or name == "operation" or name == "tx-list-queue-fail"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "component"):
                                self.component = value
                                self.component.value_namespace = name_space
                                self.component.value_namespace_prefix = name_space_prefix
                            if(value_path == "marked-for-cleanup"):
                                self.marked_for_cleanup = value
                                self.marked_for_cleanup.value_namespace = name_space
                                self.marked_for_cleanup.value_namespace_prefix = name_space_prefix
                            if(value_path == "marked-for-sweeping"):
                                self.marked_for_sweeping = value
                                self.marked_for_sweeping.value_namespace = name_space
                                self.marked_for_sweeping.value_namespace_prefix = name_space_prefix
                            if(value_path == "operation"):
                                self.operation_ = value
                                self.operation_.value_namespace = name_space
                                self.operation_.value_namespace_prefix = name_space_prefix
                            if(value_path == "tx-list-queue-fail"):
                                self.tx_list_queue_fail = value
                                self.tx_list_queue_fail.value_namespace = name_space
                                self.tx_list_queue_fail.value_namespace_prefix = name_space_prefix


                    class SessionSyncErrorInformation(Entity):
                        """
                        Session Synchroniation Error Information
                        
                        .. attribute:: last_error_code
                        
                        	Last Error Code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_error_type
                        
                        	Last Error Type
                        	**type**\:   :py:class:`SergShowSessionError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSessionError>`
                        
                        .. attribute:: sync_error_count
                        
                        	No. of Errors occured during Synchronization
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, self).__init__()

                            self.yang_name = "session-sync-error-information"
                            self.yang_parent_name = "group-id"

                            self.last_error_code = YLeaf(YType.uint32, "last-error-code")

                            self.last_error_type = YLeaf(YType.enumeration, "last-error-type")

                            self.sync_error_count = YLeaf(YType.uint16, "sync-error-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("last_error_code",
                                            "last_error_type",
                                            "sync_error_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.last_error_code.is_set or
                                self.last_error_type.is_set or
                                self.sync_error_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.last_error_code.yfilter != YFilter.not_set or
                                self.last_error_type.yfilter != YFilter.not_set or
                                self.sync_error_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "session-sync-error-information" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.last_error_code.is_set or self.last_error_code.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.last_error_code.get_name_leafdata())
                            if (self.last_error_type.is_set or self.last_error_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.last_error_type.get_name_leafdata())
                            if (self.sync_error_count.is_set or self.sync_error_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sync_error_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "last-error-code" or name == "last-error-type" or name == "sync-error-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "last-error-code"):
                                self.last_error_code = value
                                self.last_error_code.value_namespace = name_space
                                self.last_error_code.value_namespace_prefix = name_space_prefix
                            if(value_path == "last-error-type"):
                                self.last_error_type = value
                                self.last_error_type.value_namespace = name_space
                                self.last_error_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "sync-error-count"):
                                self.sync_error_count = value
                                self.sync_error_count.value_namespace = name_space
                                self.sync_error_count.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.session_detailed_information:
                            if (c.has_data()):
                                return True
                        for c in self.session_sync_error_information:
                            if (c.has_data()):
                                return True
                        return (
                            self.group_id.is_set or
                            self.group_id_xr.is_set or
                            self.interface_name.is_set or
                            self.key_index.is_set or
                            self.negative_acknowledgement_update_all.is_set or
                            self.role_master.is_set)

                    def has_operation(self):
                        for c in self.session_detailed_information:
                            if (c.has_operation()):
                                return True
                        for c in self.session_sync_error_information:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.group_id.yfilter != YFilter.not_set or
                            self.group_id_xr.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.key_index.yfilter != YFilter.not_set or
                            self.negative_acknowledgement_update_all.yfilter != YFilter.not_set or
                            self.role_master.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "group-id" + "[group-id='" + self.group_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_id.get_name_leafdata())
                        if (self.group_id_xr.is_set or self.group_id_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_id_xr.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.key_index.is_set or self.key_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.key_index.get_name_leafdata())
                        if (self.negative_acknowledgement_update_all.is_set or self.negative_acknowledgement_update_all.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.negative_acknowledgement_update_all.get_name_leafdata())
                        if (self.role_master.is_set or self.role_master.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.role_master.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "session-detailed-information"):
                            for c in self.session_detailed_information:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.session_detailed_information.append(c)
                            return c

                        if (child_yang_name == "session-sync-error-information"):
                            for c in self.session_sync_error_information:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.session_sync_error_information.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "session-detailed-information" or name == "session-sync-error-information" or name == "group-id" or name == "group-id-xr" or name == "interface-name" or name == "key-index" or name == "negative-acknowledgement-update-all" or name == "role-master"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "group-id"):
                            self.group_id = value
                            self.group_id.value_namespace = name_space
                            self.group_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-id-xr"):
                            self.group_id_xr = value
                            self.group_id_xr.value_namespace = name_space
                            self.group_id_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "key-index"):
                            self.key_index = value
                            self.key_index.value_namespace = name_space
                            self.key_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "negative-acknowledgement-update-all"):
                            self.negative_acknowledgement_update_all = value
                            self.negative_acknowledgement_update_all.value_namespace = name_space
                            self.negative_acknowledgement_update_all.value_namespace_prefix = name_space_prefix
                        if(value_path == "role-master"):
                            self.role_master = value
                            self.role_master.value_namespace = name_space
                            self.role_master.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.group_id:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.group_id:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "group-id-xr" + path_buffer

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

                    if (child_yang_name == "group-id"):
                        for c in self.group_id:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.group_id.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ClientIds(Entity):
                """
                Stats Client
                
                .. attribute:: client_id
                
                	Specify stats client
                	**type**\: list of    :py:class:`ClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.ClientIds, self).__init__()

                    self.yang_name = "client-ids"
                    self.yang_parent_name = "node"

                    self.client_id = YList(self)

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
                                super(SessionRedundancyAgent.Nodes.Node.ClientIds, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionRedundancyAgent.Nodes.Node.ClientIds, self).__setattr__(name, value)


                class ClientId(Entity):
                    """
                    Specify stats client
                    
                    .. attribute:: stats_client_id  <key>
                    
                    	Client Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: clean_call_back
                    
                    	CleanCallBack
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_replay_all_count
                    
                    	LastReplayAllCount
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_active_not_ok
                    
                    	TxListActiveNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_active_ok
                    
                    	TxListActiveOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_all_add_not_ok
                    
                    	TxListClearAllAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_all_add_ok
                    
                    	TxListClearAllAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_selected_add_not_ok
                    
                    	TxListClearSelectedAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_selected_add_ok
                    
                    	TxListClearSelectedAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_cleanup
                    
                    	TxListClientCleanup
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_connection_down
                    
                    	TxListClientConnectionDown
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_de_registration
                    
                    	TxListClientDeRegistration
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_registration_not_ok
                    
                    	TxListClientRegistrationNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_registration_ok
                    
                    	TxListClientRegistrationOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_de_active_not_ok
                    
                    	TxListDeActiveNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_de_active_ok
                    
                    	TxListDeActiveOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_session_session_ok
                    
                    	TxListEncodeSessionSessionOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_session_session_partial_write
                    
                    	TxListEncodeSessionSessionPartialWrite
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_download_add_not_ok
                    
                    	TxListEndOfDownloadAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_download_add_ok
                    
                    	TxListEndOfDownloadAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_message_add_not_ok
                    
                    	TxListEndOfMessageAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_message_add_ok
                    
                    	TxListEndOfMessageAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_command_replay_all
                    
                    	TxListReceiveCommandReplayAll
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_command_replay_selected
                    
                    	TxListReceiveCommandReplaySelected
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_clear_all
                    
                    	TxListReceiveSessionSessionClearAll
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_clear_selected
                    
                    	TxListReceiveSessionSessionClearSelected
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_delete_invalid
                    
                    	TxListReceiveSessionSessionDeleteInValid
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_delete_valid
                    
                    	TxListReceiveSessionSessionDeleteValid
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_eod_all
                    
                    	TxListReceiveSessionSessionEODAll
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_eod_selected
                    
                    	TxListReceiveSessionSessionEODSelected
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_eoms
                    
                    	TxListReceiveSessionSessionEOMS
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_neg_ack
                    
                    	TxListReceiveSessionSessionNegAck
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_neg_ack_not_ok
                    
                    	TxListReceiveSessionSessionNegAckNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_sod_all
                    
                    	TxListReceiveSessionSessionSODAll
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_sod_selected
                    
                    	TxListReceiveSessionSessionSODSelected
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_update_invalid
                    
                    	TxListReceiveSessionSessionUpdateInValid
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_update_valid
                    
                    	TxListReceiveSessionSessionUpdateValid
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_all_add_not_ok
                    
                    	TxListReplayAllAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_all_add_ok
                    
                    	TxListReplayAllAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_selected_add_not_ok
                    
                    	TxListReplaySelectedAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_selected_add_ok
                    
                    	TxListReplaySelectedAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_add_not_ok
                    
                    	TxListSessionSessionAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_add_ok
                    
                    	TxListSessionSessionAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_delete
                    
                    	TxListSessionSessionDelete
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_update_not_ok
                    
                    	TxListSessionSessionUpdateNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_update_ok
                    
                    	TxListSessionSessionUpdateOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_start_of_download_add_not_ok
                    
                    	TxListStartOfDownloadAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_start_of_download_add_ok
                    
                    	TxListStartOfDownloadAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId, self).__init__()

                        self.yang_name = "client-id"
                        self.yang_parent_name = "client-ids"

                        self.stats_client_id = YLeaf(YType.int32, "stats-client-id")

                        self.clean_call_back = YLeaf(YType.uint32, "clean-call-back")

                        self.last_replay_all_count = YLeaf(YType.uint32, "last-replay-all-count")

                        self.tx_list_active_not_ok = YLeaf(YType.uint32, "tx-list-active-not-ok")

                        self.tx_list_active_ok = YLeaf(YType.uint32, "tx-list-active-ok")

                        self.tx_list_clear_all_add_not_ok = YLeaf(YType.uint32, "tx-list-clear-all-add-not-ok")

                        self.tx_list_clear_all_add_ok = YLeaf(YType.uint32, "tx-list-clear-all-add-ok")

                        self.tx_list_clear_selected_add_not_ok = YLeaf(YType.uint32, "tx-list-clear-selected-add-not-ok")

                        self.tx_list_clear_selected_add_ok = YLeaf(YType.uint32, "tx-list-clear-selected-add-ok")

                        self.tx_list_client_cleanup = YLeaf(YType.uint32, "tx-list-client-cleanup")

                        self.tx_list_client_connection_down = YLeaf(YType.uint32, "tx-list-client-connection-down")

                        self.tx_list_client_de_registration = YLeaf(YType.uint32, "tx-list-client-de-registration")

                        self.tx_list_client_registration_not_ok = YLeaf(YType.uint32, "tx-list-client-registration-not-ok")

                        self.tx_list_client_registration_ok = YLeaf(YType.uint32, "tx-list-client-registration-ok")

                        self.tx_list_de_active_not_ok = YLeaf(YType.uint32, "tx-list-de-active-not-ok")

                        self.tx_list_de_active_ok = YLeaf(YType.uint32, "tx-list-de-active-ok")

                        self.tx_list_encode_session_session_ok = YLeaf(YType.uint32, "tx-list-encode-session-session-ok")

                        self.tx_list_encode_session_session_partial_write = YLeaf(YType.uint32, "tx-list-encode-session-session-partial-write")

                        self.tx_list_end_of_download_add_not_ok = YLeaf(YType.uint32, "tx-list-end-of-download-add-not-ok")

                        self.tx_list_end_of_download_add_ok = YLeaf(YType.uint32, "tx-list-end-of-download-add-ok")

                        self.tx_list_end_of_message_add_not_ok = YLeaf(YType.uint32, "tx-list-end-of-message-add-not-ok")

                        self.tx_list_end_of_message_add_ok = YLeaf(YType.uint32, "tx-list-end-of-message-add-ok")

                        self.tx_list_receive_command_replay_all = YLeaf(YType.uint32, "tx-list-receive-command-replay-all")

                        self.tx_list_receive_command_replay_selected = YLeaf(YType.uint32, "tx-list-receive-command-replay-selected")

                        self.tx_list_receive_session_session_clear_all = YLeaf(YType.uint32, "tx-list-receive-session-session-clear-all")

                        self.tx_list_receive_session_session_clear_selected = YLeaf(YType.uint32, "tx-list-receive-session-session-clear-selected")

                        self.tx_list_receive_session_session_delete_invalid = YLeaf(YType.uint32, "tx-list-receive-session-session-delete-invalid")

                        self.tx_list_receive_session_session_delete_valid = YLeaf(YType.uint32, "tx-list-receive-session-session-delete-valid")

                        self.tx_list_receive_session_session_eod_all = YLeaf(YType.uint32, "tx-list-receive-session-session-eod-all")

                        self.tx_list_receive_session_session_eod_selected = YLeaf(YType.uint32, "tx-list-receive-session-session-eod-selected")

                        self.tx_list_receive_session_session_eoms = YLeaf(YType.uint32, "tx-list-receive-session-session-eoms")

                        self.tx_list_receive_session_session_neg_ack = YLeaf(YType.uint32, "tx-list-receive-session-session-neg-ack")

                        self.tx_list_receive_session_session_neg_ack_not_ok = YLeaf(YType.uint32, "tx-list-receive-session-session-neg-ack-not-ok")

                        self.tx_list_receive_session_session_sod_all = YLeaf(YType.uint32, "tx-list-receive-session-session-sod-all")

                        self.tx_list_receive_session_session_sod_selected = YLeaf(YType.uint32, "tx-list-receive-session-session-sod-selected")

                        self.tx_list_receive_session_session_update_invalid = YLeaf(YType.uint32, "tx-list-receive-session-session-update-invalid")

                        self.tx_list_receive_session_session_update_valid = YLeaf(YType.uint32, "tx-list-receive-session-session-update-valid")

                        self.tx_list_replay_all_add_not_ok = YLeaf(YType.uint32, "tx-list-replay-all-add-not-ok")

                        self.tx_list_replay_all_add_ok = YLeaf(YType.uint32, "tx-list-replay-all-add-ok")

                        self.tx_list_replay_selected_add_not_ok = YLeaf(YType.uint32, "tx-list-replay-selected-add-not-ok")

                        self.tx_list_replay_selected_add_ok = YLeaf(YType.uint32, "tx-list-replay-selected-add-ok")

                        self.tx_list_session_session_add_not_ok = YLeaf(YType.uint32, "tx-list-session-session-add-not-ok")

                        self.tx_list_session_session_add_ok = YLeaf(YType.uint32, "tx-list-session-session-add-ok")

                        self.tx_list_session_session_delete = YLeaf(YType.uint32, "tx-list-session-session-delete")

                        self.tx_list_session_session_update_not_ok = YLeaf(YType.uint32, "tx-list-session-session-update-not-ok")

                        self.tx_list_session_session_update_ok = YLeaf(YType.uint32, "tx-list-session-session-update-ok")

                        self.tx_list_start_of_download_add_not_ok = YLeaf(YType.uint32, "tx-list-start-of-download-add-not-ok")

                        self.tx_list_start_of_download_add_ok = YLeaf(YType.uint32, "tx-list-start-of-download-add-ok")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("stats_client_id",
                                        "clean_call_back",
                                        "last_replay_all_count",
                                        "tx_list_active_not_ok",
                                        "tx_list_active_ok",
                                        "tx_list_clear_all_add_not_ok",
                                        "tx_list_clear_all_add_ok",
                                        "tx_list_clear_selected_add_not_ok",
                                        "tx_list_clear_selected_add_ok",
                                        "tx_list_client_cleanup",
                                        "tx_list_client_connection_down",
                                        "tx_list_client_de_registration",
                                        "tx_list_client_registration_not_ok",
                                        "tx_list_client_registration_ok",
                                        "tx_list_de_active_not_ok",
                                        "tx_list_de_active_ok",
                                        "tx_list_encode_session_session_ok",
                                        "tx_list_encode_session_session_partial_write",
                                        "tx_list_end_of_download_add_not_ok",
                                        "tx_list_end_of_download_add_ok",
                                        "tx_list_end_of_message_add_not_ok",
                                        "tx_list_end_of_message_add_ok",
                                        "tx_list_receive_command_replay_all",
                                        "tx_list_receive_command_replay_selected",
                                        "tx_list_receive_session_session_clear_all",
                                        "tx_list_receive_session_session_clear_selected",
                                        "tx_list_receive_session_session_delete_invalid",
                                        "tx_list_receive_session_session_delete_valid",
                                        "tx_list_receive_session_session_eod_all",
                                        "tx_list_receive_session_session_eod_selected",
                                        "tx_list_receive_session_session_eoms",
                                        "tx_list_receive_session_session_neg_ack",
                                        "tx_list_receive_session_session_neg_ack_not_ok",
                                        "tx_list_receive_session_session_sod_all",
                                        "tx_list_receive_session_session_sod_selected",
                                        "tx_list_receive_session_session_update_invalid",
                                        "tx_list_receive_session_session_update_valid",
                                        "tx_list_replay_all_add_not_ok",
                                        "tx_list_replay_all_add_ok",
                                        "tx_list_replay_selected_add_not_ok",
                                        "tx_list_replay_selected_add_ok",
                                        "tx_list_session_session_add_not_ok",
                                        "tx_list_session_session_add_ok",
                                        "tx_list_session_session_delete",
                                        "tx_list_session_session_update_not_ok",
                                        "tx_list_session_session_update_ok",
                                        "tx_list_start_of_download_add_not_ok",
                                        "tx_list_start_of_download_add_ok") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.stats_client_id.is_set or
                            self.clean_call_back.is_set or
                            self.last_replay_all_count.is_set or
                            self.tx_list_active_not_ok.is_set or
                            self.tx_list_active_ok.is_set or
                            self.tx_list_clear_all_add_not_ok.is_set or
                            self.tx_list_clear_all_add_ok.is_set or
                            self.tx_list_clear_selected_add_not_ok.is_set or
                            self.tx_list_clear_selected_add_ok.is_set or
                            self.tx_list_client_cleanup.is_set or
                            self.tx_list_client_connection_down.is_set or
                            self.tx_list_client_de_registration.is_set or
                            self.tx_list_client_registration_not_ok.is_set or
                            self.tx_list_client_registration_ok.is_set or
                            self.tx_list_de_active_not_ok.is_set or
                            self.tx_list_de_active_ok.is_set or
                            self.tx_list_encode_session_session_ok.is_set or
                            self.tx_list_encode_session_session_partial_write.is_set or
                            self.tx_list_end_of_download_add_not_ok.is_set or
                            self.tx_list_end_of_download_add_ok.is_set or
                            self.tx_list_end_of_message_add_not_ok.is_set or
                            self.tx_list_end_of_message_add_ok.is_set or
                            self.tx_list_receive_command_replay_all.is_set or
                            self.tx_list_receive_command_replay_selected.is_set or
                            self.tx_list_receive_session_session_clear_all.is_set or
                            self.tx_list_receive_session_session_clear_selected.is_set or
                            self.tx_list_receive_session_session_delete_invalid.is_set or
                            self.tx_list_receive_session_session_delete_valid.is_set or
                            self.tx_list_receive_session_session_eod_all.is_set or
                            self.tx_list_receive_session_session_eod_selected.is_set or
                            self.tx_list_receive_session_session_eoms.is_set or
                            self.tx_list_receive_session_session_neg_ack.is_set or
                            self.tx_list_receive_session_session_neg_ack_not_ok.is_set or
                            self.tx_list_receive_session_session_sod_all.is_set or
                            self.tx_list_receive_session_session_sod_selected.is_set or
                            self.tx_list_receive_session_session_update_invalid.is_set or
                            self.tx_list_receive_session_session_update_valid.is_set or
                            self.tx_list_replay_all_add_not_ok.is_set or
                            self.tx_list_replay_all_add_ok.is_set or
                            self.tx_list_replay_selected_add_not_ok.is_set or
                            self.tx_list_replay_selected_add_ok.is_set or
                            self.tx_list_session_session_add_not_ok.is_set or
                            self.tx_list_session_session_add_ok.is_set or
                            self.tx_list_session_session_delete.is_set or
                            self.tx_list_session_session_update_not_ok.is_set or
                            self.tx_list_session_session_update_ok.is_set or
                            self.tx_list_start_of_download_add_not_ok.is_set or
                            self.tx_list_start_of_download_add_ok.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.stats_client_id.yfilter != YFilter.not_set or
                            self.clean_call_back.yfilter != YFilter.not_set or
                            self.last_replay_all_count.yfilter != YFilter.not_set or
                            self.tx_list_active_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_active_ok.yfilter != YFilter.not_set or
                            self.tx_list_clear_all_add_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_clear_all_add_ok.yfilter != YFilter.not_set or
                            self.tx_list_clear_selected_add_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_clear_selected_add_ok.yfilter != YFilter.not_set or
                            self.tx_list_client_cleanup.yfilter != YFilter.not_set or
                            self.tx_list_client_connection_down.yfilter != YFilter.not_set or
                            self.tx_list_client_de_registration.yfilter != YFilter.not_set or
                            self.tx_list_client_registration_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_client_registration_ok.yfilter != YFilter.not_set or
                            self.tx_list_de_active_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_de_active_ok.yfilter != YFilter.not_set or
                            self.tx_list_encode_session_session_ok.yfilter != YFilter.not_set or
                            self.tx_list_encode_session_session_partial_write.yfilter != YFilter.not_set or
                            self.tx_list_end_of_download_add_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_end_of_download_add_ok.yfilter != YFilter.not_set or
                            self.tx_list_end_of_message_add_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_end_of_message_add_ok.yfilter != YFilter.not_set or
                            self.tx_list_receive_command_replay_all.yfilter != YFilter.not_set or
                            self.tx_list_receive_command_replay_selected.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_clear_all.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_clear_selected.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_delete_invalid.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_delete_valid.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_eod_all.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_eod_selected.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_eoms.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_neg_ack.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_neg_ack_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_sod_all.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_sod_selected.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_update_invalid.yfilter != YFilter.not_set or
                            self.tx_list_receive_session_session_update_valid.yfilter != YFilter.not_set or
                            self.tx_list_replay_all_add_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_replay_all_add_ok.yfilter != YFilter.not_set or
                            self.tx_list_replay_selected_add_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_replay_selected_add_ok.yfilter != YFilter.not_set or
                            self.tx_list_session_session_add_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_session_session_add_ok.yfilter != YFilter.not_set or
                            self.tx_list_session_session_delete.yfilter != YFilter.not_set or
                            self.tx_list_session_session_update_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_session_session_update_ok.yfilter != YFilter.not_set or
                            self.tx_list_start_of_download_add_not_ok.yfilter != YFilter.not_set or
                            self.tx_list_start_of_download_add_ok.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "client-id" + "[stats-client-id='" + self.stats_client_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.stats_client_id.is_set or self.stats_client_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.stats_client_id.get_name_leafdata())
                        if (self.clean_call_back.is_set or self.clean_call_back.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clean_call_back.get_name_leafdata())
                        if (self.last_replay_all_count.is_set or self.last_replay_all_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_replay_all_count.get_name_leafdata())
                        if (self.tx_list_active_not_ok.is_set or self.tx_list_active_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_active_not_ok.get_name_leafdata())
                        if (self.tx_list_active_ok.is_set or self.tx_list_active_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_active_ok.get_name_leafdata())
                        if (self.tx_list_clear_all_add_not_ok.is_set or self.tx_list_clear_all_add_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_clear_all_add_not_ok.get_name_leafdata())
                        if (self.tx_list_clear_all_add_ok.is_set or self.tx_list_clear_all_add_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_clear_all_add_ok.get_name_leafdata())
                        if (self.tx_list_clear_selected_add_not_ok.is_set or self.tx_list_clear_selected_add_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_clear_selected_add_not_ok.get_name_leafdata())
                        if (self.tx_list_clear_selected_add_ok.is_set or self.tx_list_clear_selected_add_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_clear_selected_add_ok.get_name_leafdata())
                        if (self.tx_list_client_cleanup.is_set or self.tx_list_client_cleanup.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_client_cleanup.get_name_leafdata())
                        if (self.tx_list_client_connection_down.is_set or self.tx_list_client_connection_down.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_client_connection_down.get_name_leafdata())
                        if (self.tx_list_client_de_registration.is_set or self.tx_list_client_de_registration.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_client_de_registration.get_name_leafdata())
                        if (self.tx_list_client_registration_not_ok.is_set or self.tx_list_client_registration_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_client_registration_not_ok.get_name_leafdata())
                        if (self.tx_list_client_registration_ok.is_set or self.tx_list_client_registration_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_client_registration_ok.get_name_leafdata())
                        if (self.tx_list_de_active_not_ok.is_set or self.tx_list_de_active_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_de_active_not_ok.get_name_leafdata())
                        if (self.tx_list_de_active_ok.is_set or self.tx_list_de_active_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_de_active_ok.get_name_leafdata())
                        if (self.tx_list_encode_session_session_ok.is_set or self.tx_list_encode_session_session_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_encode_session_session_ok.get_name_leafdata())
                        if (self.tx_list_encode_session_session_partial_write.is_set or self.tx_list_encode_session_session_partial_write.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_encode_session_session_partial_write.get_name_leafdata())
                        if (self.tx_list_end_of_download_add_not_ok.is_set or self.tx_list_end_of_download_add_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_end_of_download_add_not_ok.get_name_leafdata())
                        if (self.tx_list_end_of_download_add_ok.is_set or self.tx_list_end_of_download_add_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_end_of_download_add_ok.get_name_leafdata())
                        if (self.tx_list_end_of_message_add_not_ok.is_set or self.tx_list_end_of_message_add_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_end_of_message_add_not_ok.get_name_leafdata())
                        if (self.tx_list_end_of_message_add_ok.is_set or self.tx_list_end_of_message_add_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_end_of_message_add_ok.get_name_leafdata())
                        if (self.tx_list_receive_command_replay_all.is_set or self.tx_list_receive_command_replay_all.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_command_replay_all.get_name_leafdata())
                        if (self.tx_list_receive_command_replay_selected.is_set or self.tx_list_receive_command_replay_selected.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_command_replay_selected.get_name_leafdata())
                        if (self.tx_list_receive_session_session_clear_all.is_set or self.tx_list_receive_session_session_clear_all.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_clear_all.get_name_leafdata())
                        if (self.tx_list_receive_session_session_clear_selected.is_set or self.tx_list_receive_session_session_clear_selected.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_clear_selected.get_name_leafdata())
                        if (self.tx_list_receive_session_session_delete_invalid.is_set or self.tx_list_receive_session_session_delete_invalid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_delete_invalid.get_name_leafdata())
                        if (self.tx_list_receive_session_session_delete_valid.is_set or self.tx_list_receive_session_session_delete_valid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_delete_valid.get_name_leafdata())
                        if (self.tx_list_receive_session_session_eod_all.is_set or self.tx_list_receive_session_session_eod_all.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_eod_all.get_name_leafdata())
                        if (self.tx_list_receive_session_session_eod_selected.is_set or self.tx_list_receive_session_session_eod_selected.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_eod_selected.get_name_leafdata())
                        if (self.tx_list_receive_session_session_eoms.is_set or self.tx_list_receive_session_session_eoms.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_eoms.get_name_leafdata())
                        if (self.tx_list_receive_session_session_neg_ack.is_set or self.tx_list_receive_session_session_neg_ack.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_neg_ack.get_name_leafdata())
                        if (self.tx_list_receive_session_session_neg_ack_not_ok.is_set or self.tx_list_receive_session_session_neg_ack_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_neg_ack_not_ok.get_name_leafdata())
                        if (self.tx_list_receive_session_session_sod_all.is_set or self.tx_list_receive_session_session_sod_all.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_sod_all.get_name_leafdata())
                        if (self.tx_list_receive_session_session_sod_selected.is_set or self.tx_list_receive_session_session_sod_selected.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_sod_selected.get_name_leafdata())
                        if (self.tx_list_receive_session_session_update_invalid.is_set or self.tx_list_receive_session_session_update_invalid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_update_invalid.get_name_leafdata())
                        if (self.tx_list_receive_session_session_update_valid.is_set or self.tx_list_receive_session_session_update_valid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_receive_session_session_update_valid.get_name_leafdata())
                        if (self.tx_list_replay_all_add_not_ok.is_set or self.tx_list_replay_all_add_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_replay_all_add_not_ok.get_name_leafdata())
                        if (self.tx_list_replay_all_add_ok.is_set or self.tx_list_replay_all_add_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_replay_all_add_ok.get_name_leafdata())
                        if (self.tx_list_replay_selected_add_not_ok.is_set or self.tx_list_replay_selected_add_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_replay_selected_add_not_ok.get_name_leafdata())
                        if (self.tx_list_replay_selected_add_ok.is_set or self.tx_list_replay_selected_add_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_replay_selected_add_ok.get_name_leafdata())
                        if (self.tx_list_session_session_add_not_ok.is_set or self.tx_list_session_session_add_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_session_session_add_not_ok.get_name_leafdata())
                        if (self.tx_list_session_session_add_ok.is_set or self.tx_list_session_session_add_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_session_session_add_ok.get_name_leafdata())
                        if (self.tx_list_session_session_delete.is_set or self.tx_list_session_session_delete.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_session_session_delete.get_name_leafdata())
                        if (self.tx_list_session_session_update_not_ok.is_set or self.tx_list_session_session_update_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_session_session_update_not_ok.get_name_leafdata())
                        if (self.tx_list_session_session_update_ok.is_set or self.tx_list_session_session_update_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_session_session_update_ok.get_name_leafdata())
                        if (self.tx_list_start_of_download_add_not_ok.is_set or self.tx_list_start_of_download_add_not_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_start_of_download_add_not_ok.get_name_leafdata())
                        if (self.tx_list_start_of_download_add_ok.is_set or self.tx_list_start_of_download_add_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_start_of_download_add_ok.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "stats-client-id" or name == "clean-call-back" or name == "last-replay-all-count" or name == "tx-list-active-not-ok" or name == "tx-list-active-ok" or name == "tx-list-clear-all-add-not-ok" or name == "tx-list-clear-all-add-ok" or name == "tx-list-clear-selected-add-not-ok" or name == "tx-list-clear-selected-add-ok" or name == "tx-list-client-cleanup" or name == "tx-list-client-connection-down" or name == "tx-list-client-de-registration" or name == "tx-list-client-registration-not-ok" or name == "tx-list-client-registration-ok" or name == "tx-list-de-active-not-ok" or name == "tx-list-de-active-ok" or name == "tx-list-encode-session-session-ok" or name == "tx-list-encode-session-session-partial-write" or name == "tx-list-end-of-download-add-not-ok" or name == "tx-list-end-of-download-add-ok" or name == "tx-list-end-of-message-add-not-ok" or name == "tx-list-end-of-message-add-ok" or name == "tx-list-receive-command-replay-all" or name == "tx-list-receive-command-replay-selected" or name == "tx-list-receive-session-session-clear-all" or name == "tx-list-receive-session-session-clear-selected" or name == "tx-list-receive-session-session-delete-invalid" or name == "tx-list-receive-session-session-delete-valid" or name == "tx-list-receive-session-session-eod-all" or name == "tx-list-receive-session-session-eod-selected" or name == "tx-list-receive-session-session-eoms" or name == "tx-list-receive-session-session-neg-ack" or name == "tx-list-receive-session-session-neg-ack-not-ok" or name == "tx-list-receive-session-session-sod-all" or name == "tx-list-receive-session-session-sod-selected" or name == "tx-list-receive-session-session-update-invalid" or name == "tx-list-receive-session-session-update-valid" or name == "tx-list-replay-all-add-not-ok" or name == "tx-list-replay-all-add-ok" or name == "tx-list-replay-selected-add-not-ok" or name == "tx-list-replay-selected-add-ok" or name == "tx-list-session-session-add-not-ok" or name == "tx-list-session-session-add-ok" or name == "tx-list-session-session-delete" or name == "tx-list-session-session-update-not-ok" or name == "tx-list-session-session-update-ok" or name == "tx-list-start-of-download-add-not-ok" or name == "tx-list-start-of-download-add-ok"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "stats-client-id"):
                            self.stats_client_id = value
                            self.stats_client_id.value_namespace = name_space
                            self.stats_client_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "clean-call-back"):
                            self.clean_call_back = value
                            self.clean_call_back.value_namespace = name_space
                            self.clean_call_back.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-replay-all-count"):
                            self.last_replay_all_count = value
                            self.last_replay_all_count.value_namespace = name_space
                            self.last_replay_all_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-active-not-ok"):
                            self.tx_list_active_not_ok = value
                            self.tx_list_active_not_ok.value_namespace = name_space
                            self.tx_list_active_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-active-ok"):
                            self.tx_list_active_ok = value
                            self.tx_list_active_ok.value_namespace = name_space
                            self.tx_list_active_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-clear-all-add-not-ok"):
                            self.tx_list_clear_all_add_not_ok = value
                            self.tx_list_clear_all_add_not_ok.value_namespace = name_space
                            self.tx_list_clear_all_add_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-clear-all-add-ok"):
                            self.tx_list_clear_all_add_ok = value
                            self.tx_list_clear_all_add_ok.value_namespace = name_space
                            self.tx_list_clear_all_add_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-clear-selected-add-not-ok"):
                            self.tx_list_clear_selected_add_not_ok = value
                            self.tx_list_clear_selected_add_not_ok.value_namespace = name_space
                            self.tx_list_clear_selected_add_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-clear-selected-add-ok"):
                            self.tx_list_clear_selected_add_ok = value
                            self.tx_list_clear_selected_add_ok.value_namespace = name_space
                            self.tx_list_clear_selected_add_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-client-cleanup"):
                            self.tx_list_client_cleanup = value
                            self.tx_list_client_cleanup.value_namespace = name_space
                            self.tx_list_client_cleanup.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-client-connection-down"):
                            self.tx_list_client_connection_down = value
                            self.tx_list_client_connection_down.value_namespace = name_space
                            self.tx_list_client_connection_down.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-client-de-registration"):
                            self.tx_list_client_de_registration = value
                            self.tx_list_client_de_registration.value_namespace = name_space
                            self.tx_list_client_de_registration.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-client-registration-not-ok"):
                            self.tx_list_client_registration_not_ok = value
                            self.tx_list_client_registration_not_ok.value_namespace = name_space
                            self.tx_list_client_registration_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-client-registration-ok"):
                            self.tx_list_client_registration_ok = value
                            self.tx_list_client_registration_ok.value_namespace = name_space
                            self.tx_list_client_registration_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-de-active-not-ok"):
                            self.tx_list_de_active_not_ok = value
                            self.tx_list_de_active_not_ok.value_namespace = name_space
                            self.tx_list_de_active_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-de-active-ok"):
                            self.tx_list_de_active_ok = value
                            self.tx_list_de_active_ok.value_namespace = name_space
                            self.tx_list_de_active_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-encode-session-session-ok"):
                            self.tx_list_encode_session_session_ok = value
                            self.tx_list_encode_session_session_ok.value_namespace = name_space
                            self.tx_list_encode_session_session_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-encode-session-session-partial-write"):
                            self.tx_list_encode_session_session_partial_write = value
                            self.tx_list_encode_session_session_partial_write.value_namespace = name_space
                            self.tx_list_encode_session_session_partial_write.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-end-of-download-add-not-ok"):
                            self.tx_list_end_of_download_add_not_ok = value
                            self.tx_list_end_of_download_add_not_ok.value_namespace = name_space
                            self.tx_list_end_of_download_add_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-end-of-download-add-ok"):
                            self.tx_list_end_of_download_add_ok = value
                            self.tx_list_end_of_download_add_ok.value_namespace = name_space
                            self.tx_list_end_of_download_add_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-end-of-message-add-not-ok"):
                            self.tx_list_end_of_message_add_not_ok = value
                            self.tx_list_end_of_message_add_not_ok.value_namespace = name_space
                            self.tx_list_end_of_message_add_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-end-of-message-add-ok"):
                            self.tx_list_end_of_message_add_ok = value
                            self.tx_list_end_of_message_add_ok.value_namespace = name_space
                            self.tx_list_end_of_message_add_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-command-replay-all"):
                            self.tx_list_receive_command_replay_all = value
                            self.tx_list_receive_command_replay_all.value_namespace = name_space
                            self.tx_list_receive_command_replay_all.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-command-replay-selected"):
                            self.tx_list_receive_command_replay_selected = value
                            self.tx_list_receive_command_replay_selected.value_namespace = name_space
                            self.tx_list_receive_command_replay_selected.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-clear-all"):
                            self.tx_list_receive_session_session_clear_all = value
                            self.tx_list_receive_session_session_clear_all.value_namespace = name_space
                            self.tx_list_receive_session_session_clear_all.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-clear-selected"):
                            self.tx_list_receive_session_session_clear_selected = value
                            self.tx_list_receive_session_session_clear_selected.value_namespace = name_space
                            self.tx_list_receive_session_session_clear_selected.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-delete-invalid"):
                            self.tx_list_receive_session_session_delete_invalid = value
                            self.tx_list_receive_session_session_delete_invalid.value_namespace = name_space
                            self.tx_list_receive_session_session_delete_invalid.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-delete-valid"):
                            self.tx_list_receive_session_session_delete_valid = value
                            self.tx_list_receive_session_session_delete_valid.value_namespace = name_space
                            self.tx_list_receive_session_session_delete_valid.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-eod-all"):
                            self.tx_list_receive_session_session_eod_all = value
                            self.tx_list_receive_session_session_eod_all.value_namespace = name_space
                            self.tx_list_receive_session_session_eod_all.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-eod-selected"):
                            self.tx_list_receive_session_session_eod_selected = value
                            self.tx_list_receive_session_session_eod_selected.value_namespace = name_space
                            self.tx_list_receive_session_session_eod_selected.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-eoms"):
                            self.tx_list_receive_session_session_eoms = value
                            self.tx_list_receive_session_session_eoms.value_namespace = name_space
                            self.tx_list_receive_session_session_eoms.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-neg-ack"):
                            self.tx_list_receive_session_session_neg_ack = value
                            self.tx_list_receive_session_session_neg_ack.value_namespace = name_space
                            self.tx_list_receive_session_session_neg_ack.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-neg-ack-not-ok"):
                            self.tx_list_receive_session_session_neg_ack_not_ok = value
                            self.tx_list_receive_session_session_neg_ack_not_ok.value_namespace = name_space
                            self.tx_list_receive_session_session_neg_ack_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-sod-all"):
                            self.tx_list_receive_session_session_sod_all = value
                            self.tx_list_receive_session_session_sod_all.value_namespace = name_space
                            self.tx_list_receive_session_session_sod_all.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-sod-selected"):
                            self.tx_list_receive_session_session_sod_selected = value
                            self.tx_list_receive_session_session_sod_selected.value_namespace = name_space
                            self.tx_list_receive_session_session_sod_selected.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-update-invalid"):
                            self.tx_list_receive_session_session_update_invalid = value
                            self.tx_list_receive_session_session_update_invalid.value_namespace = name_space
                            self.tx_list_receive_session_session_update_invalid.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-receive-session-session-update-valid"):
                            self.tx_list_receive_session_session_update_valid = value
                            self.tx_list_receive_session_session_update_valid.value_namespace = name_space
                            self.tx_list_receive_session_session_update_valid.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-replay-all-add-not-ok"):
                            self.tx_list_replay_all_add_not_ok = value
                            self.tx_list_replay_all_add_not_ok.value_namespace = name_space
                            self.tx_list_replay_all_add_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-replay-all-add-ok"):
                            self.tx_list_replay_all_add_ok = value
                            self.tx_list_replay_all_add_ok.value_namespace = name_space
                            self.tx_list_replay_all_add_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-replay-selected-add-not-ok"):
                            self.tx_list_replay_selected_add_not_ok = value
                            self.tx_list_replay_selected_add_not_ok.value_namespace = name_space
                            self.tx_list_replay_selected_add_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-replay-selected-add-ok"):
                            self.tx_list_replay_selected_add_ok = value
                            self.tx_list_replay_selected_add_ok.value_namespace = name_space
                            self.tx_list_replay_selected_add_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-session-session-add-not-ok"):
                            self.tx_list_session_session_add_not_ok = value
                            self.tx_list_session_session_add_not_ok.value_namespace = name_space
                            self.tx_list_session_session_add_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-session-session-add-ok"):
                            self.tx_list_session_session_add_ok = value
                            self.tx_list_session_session_add_ok.value_namespace = name_space
                            self.tx_list_session_session_add_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-session-session-delete"):
                            self.tx_list_session_session_delete = value
                            self.tx_list_session_session_delete.value_namespace = name_space
                            self.tx_list_session_session_delete.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-session-session-update-not-ok"):
                            self.tx_list_session_session_update_not_ok = value
                            self.tx_list_session_session_update_not_ok.value_namespace = name_space
                            self.tx_list_session_session_update_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-session-session-update-ok"):
                            self.tx_list_session_session_update_ok = value
                            self.tx_list_session_session_update_ok.value_namespace = name_space
                            self.tx_list_session_session_update_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-start-of-download-add-not-ok"):
                            self.tx_list_start_of_download_add_not_ok = value
                            self.tx_list_start_of_download_add_not_ok.value_namespace = name_space
                            self.tx_list_start_of_download_add_not_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-start-of-download-add-ok"):
                            self.tx_list_start_of_download_add_ok = value
                            self.tx_list_start_of_download_add_ok.value_namespace = name_space
                            self.tx_list_start_of_download_add_ok.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.client_id:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.client_id:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "client-ids" + path_buffer

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

                    if (child_yang_name == "client-id"):
                        for c in self.client_id:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.client_id.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "client-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Memory(Entity):
                """
                Show Memory
                
                .. attribute:: edm_memory_info
                
                	EDM Memory Info
                	**type**\: list of    :py:class:`EdmMemoryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo>`
                
                .. attribute:: memory_info
                
                	Memory Info
                	**type**\: list of    :py:class:`MemoryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo>`
                
                .. attribute:: string_memory_info
                
                	String Memory Info
                	**type**\: list of    :py:class:`StringMemoryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.Memory, self).__init__()

                    self.yang_name = "memory"
                    self.yang_parent_name = "node"

                    self.edm_memory_info = YList(self)
                    self.memory_info = YList(self)
                    self.string_memory_info = YList(self)

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
                                super(SessionRedundancyAgent.Nodes.Node.Memory, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionRedundancyAgent.Nodes.Node.Memory, self).__setattr__(name, value)


                class MemoryInfo(Entity):
                    """
                    Memory Info
                    
                    .. attribute:: alloc_count
                    
                    	Allocated count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: alloc_fails
                    
                    	Allocation Fails
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: current_count
                    
                    	Current Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: freed_count
                    
                    	Freed Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: memory_type
                    
                    	Memory Type
                    	**type**\:   :py:class:`SergShowMem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowMem>`
                    
                    .. attribute:: size
                    
                    	Size of the datastructure
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: structure_name
                    
                    	Structure Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo, self).__init__()

                        self.yang_name = "memory-info"
                        self.yang_parent_name = "memory"

                        self.alloc_count = YLeaf(YType.uint32, "alloc-count")

                        self.alloc_fails = YLeaf(YType.uint32, "alloc-fails")

                        self.current_count = YLeaf(YType.uint32, "current-count")

                        self.freed_count = YLeaf(YType.uint32, "freed-count")

                        self.memory_type = YLeaf(YType.enumeration, "memory-type")

                        self.size = YLeaf(YType.uint32, "size")

                        self.structure_name = YLeaf(YType.str, "structure-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("alloc_count",
                                        "alloc_fails",
                                        "current_count",
                                        "freed_count",
                                        "memory_type",
                                        "size",
                                        "structure_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.alloc_count.is_set or
                            self.alloc_fails.is_set or
                            self.current_count.is_set or
                            self.freed_count.is_set or
                            self.memory_type.is_set or
                            self.size.is_set or
                            self.structure_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.alloc_count.yfilter != YFilter.not_set or
                            self.alloc_fails.yfilter != YFilter.not_set or
                            self.current_count.yfilter != YFilter.not_set or
                            self.freed_count.yfilter != YFilter.not_set or
                            self.memory_type.yfilter != YFilter.not_set or
                            self.size.yfilter != YFilter.not_set or
                            self.structure_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "memory-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.alloc_count.is_set or self.alloc_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alloc_count.get_name_leafdata())
                        if (self.alloc_fails.is_set or self.alloc_fails.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alloc_fails.get_name_leafdata())
                        if (self.current_count.is_set or self.current_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.current_count.get_name_leafdata())
                        if (self.freed_count.is_set or self.freed_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.freed_count.get_name_leafdata())
                        if (self.memory_type.is_set or self.memory_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.memory_type.get_name_leafdata())
                        if (self.size.is_set or self.size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.size.get_name_leafdata())
                        if (self.structure_name.is_set or self.structure_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.structure_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "alloc-count" or name == "alloc-fails" or name == "current-count" or name == "freed-count" or name == "memory-type" or name == "size" or name == "structure-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "alloc-count"):
                            self.alloc_count = value
                            self.alloc_count.value_namespace = name_space
                            self.alloc_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "alloc-fails"):
                            self.alloc_fails = value
                            self.alloc_fails.value_namespace = name_space
                            self.alloc_fails.value_namespace_prefix = name_space_prefix
                        if(value_path == "current-count"):
                            self.current_count = value
                            self.current_count.value_namespace = name_space
                            self.current_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "freed-count"):
                            self.freed_count = value
                            self.freed_count.value_namespace = name_space
                            self.freed_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "memory-type"):
                            self.memory_type = value
                            self.memory_type.value_namespace = name_space
                            self.memory_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "size"):
                            self.size = value
                            self.size.value_namespace = name_space
                            self.size.value_namespace_prefix = name_space_prefix
                        if(value_path == "structure-name"):
                            self.structure_name = value
                            self.structure_name.value_namespace = name_space
                            self.structure_name.value_namespace_prefix = name_space_prefix


                class EdmMemoryInfo(Entity):
                    """
                    EDM Memory Info
                    
                    .. attribute:: failure
                    
                    	Cache\-hit failure
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: size
                    
                    	Size of the block
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: success
                    
                    	Cache\-hit success
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total
                    
                    	Total request
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo, self).__init__()

                        self.yang_name = "edm-memory-info"
                        self.yang_parent_name = "memory"

                        self.failure = YLeaf(YType.uint32, "failure")

                        self.size = YLeaf(YType.uint32, "size")

                        self.success = YLeaf(YType.uint32, "success")

                        self.total = YLeaf(YType.uint32, "total")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("failure",
                                        "size",
                                        "success",
                                        "total") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.failure.is_set or
                            self.size.is_set or
                            self.success.is_set or
                            self.total.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.failure.yfilter != YFilter.not_set or
                            self.size.yfilter != YFilter.not_set or
                            self.success.yfilter != YFilter.not_set or
                            self.total.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "edm-memory-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.failure.is_set or self.failure.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.failure.get_name_leafdata())
                        if (self.size.is_set or self.size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.size.get_name_leafdata())
                        if (self.success.is_set or self.success.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.success.get_name_leafdata())
                        if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "failure" or name == "size" or name == "success" or name == "total"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "failure"):
                            self.failure = value
                            self.failure.value_namespace = name_space
                            self.failure.value_namespace_prefix = name_space_prefix
                        if(value_path == "size"):
                            self.size = value
                            self.size.value_namespace = name_space
                            self.size.value_namespace_prefix = name_space_prefix
                        if(value_path == "success"):
                            self.success = value
                            self.success.value_namespace = name_space
                            self.success.value_namespace_prefix = name_space_prefix
                        if(value_path == "total"):
                            self.total = value
                            self.total.value_namespace = name_space
                            self.total.value_namespace_prefix = name_space_prefix


                class StringMemoryInfo(Entity):
                    """
                    String Memory Info
                    
                    .. attribute:: failure
                    
                    	Cache\-hit failure
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: size
                    
                    	Size of the block
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: success
                    
                    	Cache\-hit success
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total
                    
                    	Total request
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo, self).__init__()

                        self.yang_name = "string-memory-info"
                        self.yang_parent_name = "memory"

                        self.failure = YLeaf(YType.uint32, "failure")

                        self.size = YLeaf(YType.uint32, "size")

                        self.success = YLeaf(YType.uint32, "success")

                        self.total = YLeaf(YType.uint32, "total")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("failure",
                                        "size",
                                        "success",
                                        "total") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.failure.is_set or
                            self.size.is_set or
                            self.success.is_set or
                            self.total.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.failure.yfilter != YFilter.not_set or
                            self.size.yfilter != YFilter.not_set or
                            self.success.yfilter != YFilter.not_set or
                            self.total.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "string-memory-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.failure.is_set or self.failure.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.failure.get_name_leafdata())
                        if (self.size.is_set or self.size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.size.get_name_leafdata())
                        if (self.success.is_set or self.success.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.success.get_name_leafdata())
                        if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "failure" or name == "size" or name == "success" or name == "total"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "failure"):
                            self.failure = value
                            self.failure.value_namespace = name_space
                            self.failure.value_namespace_prefix = name_space_prefix
                        if(value_path == "size"):
                            self.size = value
                            self.size.value_namespace = name_space
                            self.size.value_namespace_prefix = name_space_prefix
                        if(value_path == "success"):
                            self.success = value
                            self.success.value_namespace = name_space
                            self.success.value_namespace_prefix = name_space_prefix
                        if(value_path == "total"):
                            self.total = value
                            self.total.value_namespace = name_space
                            self.total.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.edm_memory_info:
                        if (c.has_data()):
                            return True
                    for c in self.memory_info:
                        if (c.has_data()):
                            return True
                    for c in self.string_memory_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.edm_memory_info:
                        if (c.has_operation()):
                            return True
                    for c in self.memory_info:
                        if (c.has_operation()):
                            return True
                    for c in self.string_memory_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "memory" + path_buffer

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

                    if (child_yang_name == "edm-memory-info"):
                        for c in self.edm_memory_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.edm_memory_info.append(c)
                        return c

                    if (child_yang_name == "memory-info"):
                        for c in self.memory_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.memory_info.append(c)
                        return c

                    if (child_yang_name == "string-memory-info"):
                        for c in self.string_memory_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.string_memory_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "edm-memory-info" or name == "memory-info" or name == "string-memory-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class GroupIds(Entity):
                """
                Data for particular subscriber group 
                
                .. attribute:: group_id
                
                	Group id for subscriber group
                	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.GroupIds, self).__init__()

                    self.yang_name = "group-ids"
                    self.yang_parent_name = "node"

                    self.group_id = YList(self)

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
                                super(SessionRedundancyAgent.Nodes.Node.GroupIds, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionRedundancyAgent.Nodes.Node.GroupIds, self).__setattr__(name, value)


                class GroupId(Entity):
                    """
                    Group id for subscriber group
                    
                    .. attribute:: group_id  <key>
                    
                    	Group Id
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: access_tracking_object_name
                    
                    	Access Object Tracking Name
                    	**type**\:  str
                    
                    .. attribute:: access_tracking_object_status
                    
                    	Access Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: client_session_count
                    
                    	Client Session Count
                    	**type**\: list of    :py:class:`ClientSessionCount <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount>`
                    
                    .. attribute:: core_tracking_object_name
                    
                    	Core Object Tracking Name
                    	**type**\:  str
                    
                    .. attribute:: core_tracking_object_status
                    
                    	Core Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: current_role
                    
                    	Current Role
                    	**type**\:   :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: description
                    
                    	Group Description
                    	**type**\:  str
                    
                    .. attribute:: disabled
                    
                    	Disabled by Config
                    	**type**\:  bool
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_timer
                    
                    	Switch Over Hold Time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: init_role
                    
                    	Preferred Init Role
                    	**type**\:   :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: interface
                    
                    	Interface List
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface>`
                    
                    .. attribute:: interface_count
                    
                    	No. of Configured Interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_switchover_reason
                    
                    	Last Switchover Reason
                    	**type**\:   :py:class:`SergShowSoReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSoReason>`
                    
                    .. attribute:: last_switchover_time
                    
                    	Last Switchover time
                    	**type**\:  str
                    
                    .. attribute:: negotiating_role
                    
                    	Negotiating Role
                    	**type**\:   :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: object_tracking_status
                    
                    	Object Tracking Status (Enabled/Disabled)
                    	**type**\:  bool
                    
                    .. attribute:: peer_current_role
                    
                    	Peer Current Role
                    	**type**\:   :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: peer_init_role
                    
                    	Peer Preferred Init Role
                    	**type**\:   :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: peer_ipv4_address
                    
                    	Peer IPv4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_ipv6_address
                    
                    	Peer IPv6 Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_last_down_time
                    
                    	Last Down time of Peer
                    	**type**\:  str
                    
                    .. attribute:: peer_last_negotiation_time
                    
                    	Last Negotiation time of Peer
                    	**type**\:  str
                    
                    .. attribute:: peer_last_up_time
                    
                    	Last UP time of Peer
                    	**type**\:  str
                    
                    .. attribute:: peer_negotiating_role
                    
                    	Peer Negotiating Role
                    	**type**\:   :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: peer_object_tracking_status
                    
                    	Peer Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: peer_status
                    
                    	Peer Status
                    	**type**\:   :py:class:`SergPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergPeerStatus>`
                    
                    .. attribute:: pending_session_delete_count
                    
                    	Pending Session Delete Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pending_session_update_count
                    
                    	Pending Session Update Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: revertive_timer
                    
                    	Revertive timer for SWO back
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slave_mode
                    
                    	Slave Mode
                    	**type**\:   :py:class:`SergShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveMode>`
                    
                    .. attribute:: slave_update_failure_count
                    
                    	Slave Session update fail count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: switchover_count
                    
                    	Switchover Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: switchover_hold_time
                    
                    	Switchover Hold Time in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: switchover_revert_time
                    
                    	Switchover Revert Time in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId, self).__init__()

                        self.yang_name = "group-id"
                        self.yang_parent_name = "group-ids"

                        self.group_id = YLeaf(YType.str, "group-id")

                        self.access_tracking_object_name = YLeaf(YType.str, "access-tracking-object-name")

                        self.access_tracking_object_status = YLeaf(YType.boolean, "access-tracking-object-status")

                        self.core_tracking_object_name = YLeaf(YType.str, "core-tracking-object-name")

                        self.core_tracking_object_status = YLeaf(YType.boolean, "core-tracking-object-status")

                        self.current_role = YLeaf(YType.enumeration, "current-role")

                        self.description = YLeaf(YType.str, "description")

                        self.disabled = YLeaf(YType.boolean, "disabled")

                        self.group_id_xr = YLeaf(YType.uint32, "group-id-xr")

                        self.hold_timer = YLeaf(YType.uint32, "hold-timer")

                        self.init_role = YLeaf(YType.enumeration, "init-role")

                        self.interface_count = YLeaf(YType.uint32, "interface-count")

                        self.last_switchover_reason = YLeaf(YType.enumeration, "last-switchover-reason")

                        self.last_switchover_time = YLeaf(YType.str, "last-switchover-time")

                        self.negotiating_role = YLeaf(YType.enumeration, "negotiating-role")

                        self.object_tracking_status = YLeaf(YType.boolean, "object-tracking-status")

                        self.peer_current_role = YLeaf(YType.enumeration, "peer-current-role")

                        self.peer_init_role = YLeaf(YType.enumeration, "peer-init-role")

                        self.peer_ipv4_address = YLeaf(YType.str, "peer-ipv4-address")

                        self.peer_ipv6_address = YLeaf(YType.str, "peer-ipv6-address")

                        self.peer_last_down_time = YLeaf(YType.str, "peer-last-down-time")

                        self.peer_last_negotiation_time = YLeaf(YType.str, "peer-last-negotiation-time")

                        self.peer_last_up_time = YLeaf(YType.str, "peer-last-up-time")

                        self.peer_negotiating_role = YLeaf(YType.enumeration, "peer-negotiating-role")

                        self.peer_object_tracking_status = YLeaf(YType.boolean, "peer-object-tracking-status")

                        self.peer_status = YLeaf(YType.enumeration, "peer-status")

                        self.pending_session_delete_count = YLeaf(YType.uint32, "pending-session-delete-count")

                        self.pending_session_update_count = YLeaf(YType.uint32, "pending-session-update-count")

                        self.revertive_timer = YLeaf(YType.uint32, "revertive-timer")

                        self.session_count = YLeaf(YType.uint32, "session-count")

                        self.slave_mode = YLeaf(YType.enumeration, "slave-mode")

                        self.slave_update_failure_count = YLeaf(YType.uint32, "slave-update-failure-count")

                        self.switchover_count = YLeaf(YType.uint32, "switchover-count")

                        self.switchover_hold_time = YLeaf(YType.uint32, "switchover-hold-time")

                        self.switchover_revert_time = YLeaf(YType.uint32, "switchover-revert-time")

                        self.client_session_count = YList(self)
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
                            if name in ("group_id",
                                        "access_tracking_object_name",
                                        "access_tracking_object_status",
                                        "core_tracking_object_name",
                                        "core_tracking_object_status",
                                        "current_role",
                                        "description",
                                        "disabled",
                                        "group_id_xr",
                                        "hold_timer",
                                        "init_role",
                                        "interface_count",
                                        "last_switchover_reason",
                                        "last_switchover_time",
                                        "negotiating_role",
                                        "object_tracking_status",
                                        "peer_current_role",
                                        "peer_init_role",
                                        "peer_ipv4_address",
                                        "peer_ipv6_address",
                                        "peer_last_down_time",
                                        "peer_last_negotiation_time",
                                        "peer_last_up_time",
                                        "peer_negotiating_role",
                                        "peer_object_tracking_status",
                                        "peer_status",
                                        "pending_session_delete_count",
                                        "pending_session_update_count",
                                        "revertive_timer",
                                        "session_count",
                                        "slave_mode",
                                        "slave_update_failure_count",
                                        "switchover_count",
                                        "switchover_hold_time",
                                        "switchover_revert_time") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId, self).__setattr__(name, value)


                    class ClientSessionCount(Entity):
                        """
                        Client Session Count
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:   :py:class:`SergShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowComp>`
                        
                        .. attribute:: session_count
                        
                        	Session count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount, self).__init__()

                            self.yang_name = "client-session-count"
                            self.yang_parent_name = "group-id"

                            self.component = YLeaf(YType.enumeration, "component")

                            self.session_count = YLeaf(YType.uint32, "session-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("component",
                                            "session_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.component.is_set or
                                self.session_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.component.yfilter != YFilter.not_set or
                                self.session_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "client-session-count" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.component.is_set or self.component.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.component.get_name_leafdata())
                            if (self.session_count.is_set or self.session_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "component" or name == "session-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "component"):
                                self.component = value
                                self.component.value_namespace = name_space
                                self.component.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-count"):
                                self.session_count = value
                                self.session_count.value_namespace = name_space
                                self.session_count.value_namespace_prefix = name_space_prefix


                    class Interface(Entity):
                        """
                        Interface List
                        
                        .. attribute:: forward_referenced
                        
                        	Forward Referenced
                        	**type**\:  bool
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        .. attribute:: interface_synchronization_id
                        
                        	Interface Synchronization ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_count
                        
                        	Session Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "group-id"

                            self.forward_referenced = YLeaf(YType.boolean, "forward-referenced")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interface_synchronization_id = YLeaf(YType.uint32, "interface-synchronization-id")

                            self.session_count = YLeaf(YType.uint32, "session-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("forward_referenced",
                                            "interface_name",
                                            "interface_synchronization_id",
                                            "session_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.forward_referenced.is_set or
                                self.interface_name.is_set or
                                self.interface_synchronization_id.is_set or
                                self.session_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.forward_referenced.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.interface_synchronization_id.yfilter != YFilter.not_set or
                                self.session_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.forward_referenced.is_set or self.forward_referenced.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.forward_referenced.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.interface_synchronization_id.is_set or self.interface_synchronization_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_synchronization_id.get_name_leafdata())
                            if (self.session_count.is_set or self.session_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "forward-referenced" or name == "interface-name" or name == "interface-synchronization-id" or name == "session-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "forward-referenced"):
                                self.forward_referenced = value
                                self.forward_referenced.value_namespace = name_space
                                self.forward_referenced.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-synchronization-id"):
                                self.interface_synchronization_id = value
                                self.interface_synchronization_id.value_namespace = name_space
                                self.interface_synchronization_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-count"):
                                self.session_count = value
                                self.session_count.value_namespace = name_space
                                self.session_count.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.client_session_count:
                            if (c.has_data()):
                                return True
                        for c in self.interface:
                            if (c.has_data()):
                                return True
                        return (
                            self.group_id.is_set or
                            self.access_tracking_object_name.is_set or
                            self.access_tracking_object_status.is_set or
                            self.core_tracking_object_name.is_set or
                            self.core_tracking_object_status.is_set or
                            self.current_role.is_set or
                            self.description.is_set or
                            self.disabled.is_set or
                            self.group_id_xr.is_set or
                            self.hold_timer.is_set or
                            self.init_role.is_set or
                            self.interface_count.is_set or
                            self.last_switchover_reason.is_set or
                            self.last_switchover_time.is_set or
                            self.negotiating_role.is_set or
                            self.object_tracking_status.is_set or
                            self.peer_current_role.is_set or
                            self.peer_init_role.is_set or
                            self.peer_ipv4_address.is_set or
                            self.peer_ipv6_address.is_set or
                            self.peer_last_down_time.is_set or
                            self.peer_last_negotiation_time.is_set or
                            self.peer_last_up_time.is_set or
                            self.peer_negotiating_role.is_set or
                            self.peer_object_tracking_status.is_set or
                            self.peer_status.is_set or
                            self.pending_session_delete_count.is_set or
                            self.pending_session_update_count.is_set or
                            self.revertive_timer.is_set or
                            self.session_count.is_set or
                            self.slave_mode.is_set or
                            self.slave_update_failure_count.is_set or
                            self.switchover_count.is_set or
                            self.switchover_hold_time.is_set or
                            self.switchover_revert_time.is_set)

                    def has_operation(self):
                        for c in self.client_session_count:
                            if (c.has_operation()):
                                return True
                        for c in self.interface:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.group_id.yfilter != YFilter.not_set or
                            self.access_tracking_object_name.yfilter != YFilter.not_set or
                            self.access_tracking_object_status.yfilter != YFilter.not_set or
                            self.core_tracking_object_name.yfilter != YFilter.not_set or
                            self.core_tracking_object_status.yfilter != YFilter.not_set or
                            self.current_role.yfilter != YFilter.not_set or
                            self.description.yfilter != YFilter.not_set or
                            self.disabled.yfilter != YFilter.not_set or
                            self.group_id_xr.yfilter != YFilter.not_set or
                            self.hold_timer.yfilter != YFilter.not_set or
                            self.init_role.yfilter != YFilter.not_set or
                            self.interface_count.yfilter != YFilter.not_set or
                            self.last_switchover_reason.yfilter != YFilter.not_set or
                            self.last_switchover_time.yfilter != YFilter.not_set or
                            self.negotiating_role.yfilter != YFilter.not_set or
                            self.object_tracking_status.yfilter != YFilter.not_set or
                            self.peer_current_role.yfilter != YFilter.not_set or
                            self.peer_init_role.yfilter != YFilter.not_set or
                            self.peer_ipv4_address.yfilter != YFilter.not_set or
                            self.peer_ipv6_address.yfilter != YFilter.not_set or
                            self.peer_last_down_time.yfilter != YFilter.not_set or
                            self.peer_last_negotiation_time.yfilter != YFilter.not_set or
                            self.peer_last_up_time.yfilter != YFilter.not_set or
                            self.peer_negotiating_role.yfilter != YFilter.not_set or
                            self.peer_object_tracking_status.yfilter != YFilter.not_set or
                            self.peer_status.yfilter != YFilter.not_set or
                            self.pending_session_delete_count.yfilter != YFilter.not_set or
                            self.pending_session_update_count.yfilter != YFilter.not_set or
                            self.revertive_timer.yfilter != YFilter.not_set or
                            self.session_count.yfilter != YFilter.not_set or
                            self.slave_mode.yfilter != YFilter.not_set or
                            self.slave_update_failure_count.yfilter != YFilter.not_set or
                            self.switchover_count.yfilter != YFilter.not_set or
                            self.switchover_hold_time.yfilter != YFilter.not_set or
                            self.switchover_revert_time.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "group-id" + "[group-id='" + self.group_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_id.get_name_leafdata())
                        if (self.access_tracking_object_name.is_set or self.access_tracking_object_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_tracking_object_name.get_name_leafdata())
                        if (self.access_tracking_object_status.is_set or self.access_tracking_object_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_tracking_object_status.get_name_leafdata())
                        if (self.core_tracking_object_name.is_set or self.core_tracking_object_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.core_tracking_object_name.get_name_leafdata())
                        if (self.core_tracking_object_status.is_set or self.core_tracking_object_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.core_tracking_object_status.get_name_leafdata())
                        if (self.current_role.is_set or self.current_role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.current_role.get_name_leafdata())
                        if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.description.get_name_leafdata())
                        if (self.disabled.is_set or self.disabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.disabled.get_name_leafdata())
                        if (self.group_id_xr.is_set or self.group_id_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_id_xr.get_name_leafdata())
                        if (self.hold_timer.is_set or self.hold_timer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hold_timer.get_name_leafdata())
                        if (self.init_role.is_set or self.init_role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.init_role.get_name_leafdata())
                        if (self.interface_count.is_set or self.interface_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_count.get_name_leafdata())
                        if (self.last_switchover_reason.is_set or self.last_switchover_reason.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_switchover_reason.get_name_leafdata())
                        if (self.last_switchover_time.is_set or self.last_switchover_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_switchover_time.get_name_leafdata())
                        if (self.negotiating_role.is_set or self.negotiating_role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.negotiating_role.get_name_leafdata())
                        if (self.object_tracking_status.is_set or self.object_tracking_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_tracking_status.get_name_leafdata())
                        if (self.peer_current_role.is_set or self.peer_current_role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_current_role.get_name_leafdata())
                        if (self.peer_init_role.is_set or self.peer_init_role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_init_role.get_name_leafdata())
                        if (self.peer_ipv4_address.is_set or self.peer_ipv4_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_ipv4_address.get_name_leafdata())
                        if (self.peer_ipv6_address.is_set or self.peer_ipv6_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_ipv6_address.get_name_leafdata())
                        if (self.peer_last_down_time.is_set or self.peer_last_down_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_last_down_time.get_name_leafdata())
                        if (self.peer_last_negotiation_time.is_set or self.peer_last_negotiation_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_last_negotiation_time.get_name_leafdata())
                        if (self.peer_last_up_time.is_set or self.peer_last_up_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_last_up_time.get_name_leafdata())
                        if (self.peer_negotiating_role.is_set or self.peer_negotiating_role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_negotiating_role.get_name_leafdata())
                        if (self.peer_object_tracking_status.is_set or self.peer_object_tracking_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_object_tracking_status.get_name_leafdata())
                        if (self.peer_status.is_set or self.peer_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_status.get_name_leafdata())
                        if (self.pending_session_delete_count.is_set or self.pending_session_delete_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pending_session_delete_count.get_name_leafdata())
                        if (self.pending_session_update_count.is_set or self.pending_session_update_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pending_session_update_count.get_name_leafdata())
                        if (self.revertive_timer.is_set or self.revertive_timer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.revertive_timer.get_name_leafdata())
                        if (self.session_count.is_set or self.session_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_count.get_name_leafdata())
                        if (self.slave_mode.is_set or self.slave_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slave_mode.get_name_leafdata())
                        if (self.slave_update_failure_count.is_set or self.slave_update_failure_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slave_update_failure_count.get_name_leafdata())
                        if (self.switchover_count.is_set or self.switchover_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.switchover_count.get_name_leafdata())
                        if (self.switchover_hold_time.is_set or self.switchover_hold_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.switchover_hold_time.get_name_leafdata())
                        if (self.switchover_revert_time.is_set or self.switchover_revert_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.switchover_revert_time.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "client-session-count"):
                            for c in self.client_session_count:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.client_session_count.append(c)
                            return c

                        if (child_yang_name == "interface"):
                            for c in self.interface:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.interface.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "client-session-count" or name == "interface" or name == "group-id" or name == "access-tracking-object-name" or name == "access-tracking-object-status" or name == "core-tracking-object-name" or name == "core-tracking-object-status" or name == "current-role" or name == "description" or name == "disabled" or name == "group-id-xr" or name == "hold-timer" or name == "init-role" or name == "interface-count" or name == "last-switchover-reason" or name == "last-switchover-time" or name == "negotiating-role" or name == "object-tracking-status" or name == "peer-current-role" or name == "peer-init-role" or name == "peer-ipv4-address" or name == "peer-ipv6-address" or name == "peer-last-down-time" or name == "peer-last-negotiation-time" or name == "peer-last-up-time" or name == "peer-negotiating-role" or name == "peer-object-tracking-status" or name == "peer-status" or name == "pending-session-delete-count" or name == "pending-session-update-count" or name == "revertive-timer" or name == "session-count" or name == "slave-mode" or name == "slave-update-failure-count" or name == "switchover-count" or name == "switchover-hold-time" or name == "switchover-revert-time"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "group-id"):
                            self.group_id = value
                            self.group_id.value_namespace = name_space
                            self.group_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-tracking-object-name"):
                            self.access_tracking_object_name = value
                            self.access_tracking_object_name.value_namespace = name_space
                            self.access_tracking_object_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-tracking-object-status"):
                            self.access_tracking_object_status = value
                            self.access_tracking_object_status.value_namespace = name_space
                            self.access_tracking_object_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "core-tracking-object-name"):
                            self.core_tracking_object_name = value
                            self.core_tracking_object_name.value_namespace = name_space
                            self.core_tracking_object_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "core-tracking-object-status"):
                            self.core_tracking_object_status = value
                            self.core_tracking_object_status.value_namespace = name_space
                            self.core_tracking_object_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "current-role"):
                            self.current_role = value
                            self.current_role.value_namespace = name_space
                            self.current_role.value_namespace_prefix = name_space_prefix
                        if(value_path == "description"):
                            self.description = value
                            self.description.value_namespace = name_space
                            self.description.value_namespace_prefix = name_space_prefix
                        if(value_path == "disabled"):
                            self.disabled = value
                            self.disabled.value_namespace = name_space
                            self.disabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-id-xr"):
                            self.group_id_xr = value
                            self.group_id_xr.value_namespace = name_space
                            self.group_id_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "hold-timer"):
                            self.hold_timer = value
                            self.hold_timer.value_namespace = name_space
                            self.hold_timer.value_namespace_prefix = name_space_prefix
                        if(value_path == "init-role"):
                            self.init_role = value
                            self.init_role.value_namespace = name_space
                            self.init_role.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-count"):
                            self.interface_count = value
                            self.interface_count.value_namespace = name_space
                            self.interface_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-switchover-reason"):
                            self.last_switchover_reason = value
                            self.last_switchover_reason.value_namespace = name_space
                            self.last_switchover_reason.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-switchover-time"):
                            self.last_switchover_time = value
                            self.last_switchover_time.value_namespace = name_space
                            self.last_switchover_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "negotiating-role"):
                            self.negotiating_role = value
                            self.negotiating_role.value_namespace = name_space
                            self.negotiating_role.value_namespace_prefix = name_space_prefix
                        if(value_path == "object-tracking-status"):
                            self.object_tracking_status = value
                            self.object_tracking_status.value_namespace = name_space
                            self.object_tracking_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-current-role"):
                            self.peer_current_role = value
                            self.peer_current_role.value_namespace = name_space
                            self.peer_current_role.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-init-role"):
                            self.peer_init_role = value
                            self.peer_init_role.value_namespace = name_space
                            self.peer_init_role.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-ipv4-address"):
                            self.peer_ipv4_address = value
                            self.peer_ipv4_address.value_namespace = name_space
                            self.peer_ipv4_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-ipv6-address"):
                            self.peer_ipv6_address = value
                            self.peer_ipv6_address.value_namespace = name_space
                            self.peer_ipv6_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-last-down-time"):
                            self.peer_last_down_time = value
                            self.peer_last_down_time.value_namespace = name_space
                            self.peer_last_down_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-last-negotiation-time"):
                            self.peer_last_negotiation_time = value
                            self.peer_last_negotiation_time.value_namespace = name_space
                            self.peer_last_negotiation_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-last-up-time"):
                            self.peer_last_up_time = value
                            self.peer_last_up_time.value_namespace = name_space
                            self.peer_last_up_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-negotiating-role"):
                            self.peer_negotiating_role = value
                            self.peer_negotiating_role.value_namespace = name_space
                            self.peer_negotiating_role.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-object-tracking-status"):
                            self.peer_object_tracking_status = value
                            self.peer_object_tracking_status.value_namespace = name_space
                            self.peer_object_tracking_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-status"):
                            self.peer_status = value
                            self.peer_status.value_namespace = name_space
                            self.peer_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "pending-session-delete-count"):
                            self.pending_session_delete_count = value
                            self.pending_session_delete_count.value_namespace = name_space
                            self.pending_session_delete_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "pending-session-update-count"):
                            self.pending_session_update_count = value
                            self.pending_session_update_count.value_namespace = name_space
                            self.pending_session_update_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "revertive-timer"):
                            self.revertive_timer = value
                            self.revertive_timer.value_namespace = name_space
                            self.revertive_timer.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-count"):
                            self.session_count = value
                            self.session_count.value_namespace = name_space
                            self.session_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "slave-mode"):
                            self.slave_mode = value
                            self.slave_mode.value_namespace = name_space
                            self.slave_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "slave-update-failure-count"):
                            self.slave_update_failure_count = value
                            self.slave_update_failure_count.value_namespace = name_space
                            self.slave_update_failure_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "switchover-count"):
                            self.switchover_count = value
                            self.switchover_count.value_namespace = name_space
                            self.switchover_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "switchover-hold-time"):
                            self.switchover_hold_time = value
                            self.switchover_hold_time.value_namespace = name_space
                            self.switchover_hold_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "switchover-revert-time"):
                            self.switchover_revert_time = value
                            self.switchover_revert_time.value_namespace = name_space
                            self.switchover_revert_time.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.group_id:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.group_id:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "group-ids" + path_buffer

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

                    if (child_yang_name == "group-id"):
                        for c in self.group_id:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.group_id.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                List of interfaces
                
                .. attribute:: interface
                
                	Specify interface name
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"

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
                                super(SessionRedundancyAgent.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionRedundancyAgent.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    Specify interface name
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: client_status
                    
                    	Interface status for each client
                    	**type**\: list of    :py:class:`ClientStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus>`
                    
                    .. attribute:: forward_referenced
                    
                    	Forward Referenced
                    	**type**\:  bool
                    
                    .. attribute:: group_id
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_attribute_update_error_count
                    
                    	Interface Attribute Update Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_caps_add_error_count
                    
                    	Interface Caps Add Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_caps_remove_error_count
                    
                    	Interface Caps Remove Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_disable_error_count
                    
                    	Interface Disable Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_enable_error_count
                    
                    	Interface Enable Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    .. attribute:: interface_oper
                    
                    	Interface Batch Operation
                    	**type**\:   :py:class:`InterfaceOper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper>`
                    
                    .. attribute:: interface_status
                    
                    	Interface Status
                    	**type**\:   :py:class:`InterfaceStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus>`
                    
                    .. attribute:: interface_synchronization_id
                    
                    	Interface Sync ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: role
                    
                    	SERG Role
                    	**type**\:   :py:class:`SergShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRole>`
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface = YLeaf(YType.str, "interface")

                        self.forward_referenced = YLeaf(YType.boolean, "forward-referenced")

                        self.group_id = YLeaf(YType.uint32, "group-id")

                        self.interface_attribute_update_error_count = YLeaf(YType.uint32, "interface-attribute-update-error-count")

                        self.interface_caps_add_error_count = YLeaf(YType.uint32, "interface-caps-add-error-count")

                        self.interface_caps_remove_error_count = YLeaf(YType.uint32, "interface-caps-remove-error-count")

                        self.interface_disable_error_count = YLeaf(YType.uint32, "interface-disable-error-count")

                        self.interface_enable_error_count = YLeaf(YType.uint32, "interface-enable-error-count")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface_synchronization_id = YLeaf(YType.uint32, "interface-synchronization-id")

                        self.role = YLeaf(YType.enumeration, "role")

                        self.session_count = YLeaf(YType.uint32, "session-count")

                        self.interface_oper = SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper()
                        self.interface_oper.parent = self
                        self._children_name_map["interface_oper"] = "interface-oper"
                        self._children_yang_names.add("interface-oper")

                        self.interface_status = SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus()
                        self.interface_status.parent = self
                        self._children_name_map["interface_status"] = "interface-status"
                        self._children_yang_names.add("interface-status")

                        self.client_status = YList(self)

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
                                        "forward_referenced",
                                        "group_id",
                                        "interface_attribute_update_error_count",
                                        "interface_caps_add_error_count",
                                        "interface_caps_remove_error_count",
                                        "interface_disable_error_count",
                                        "interface_enable_error_count",
                                        "interface_name",
                                        "interface_synchronization_id",
                                        "role",
                                        "session_count") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)


                    class InterfaceOper(Entity):
                        """
                        Interface Batch Operation
                        
                        .. attribute:: idb_oper_attr_update
                        
                        	Operational Attribute Update
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_caps_add
                        
                        	Operational Caps Add
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_caps_remove
                        
                        	Operational Caps Remove
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_reg_disable
                        
                        	Operational Registration Disabled
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_reg_enable
                        
                        	Operational Registration Enabled
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, self).__init__()

                            self.yang_name = "interface-oper"
                            self.yang_parent_name = "interface"

                            self.idb_oper_attr_update = YLeaf(YType.boolean, "idb-oper-attr-update")

                            self.idb_oper_caps_add = YLeaf(YType.boolean, "idb-oper-caps-add")

                            self.idb_oper_caps_remove = YLeaf(YType.boolean, "idb-oper-caps-remove")

                            self.idb_oper_reg_disable = YLeaf(YType.boolean, "idb-oper-reg-disable")

                            self.idb_oper_reg_enable = YLeaf(YType.boolean, "idb-oper-reg-enable")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("idb_oper_attr_update",
                                            "idb_oper_caps_add",
                                            "idb_oper_caps_remove",
                                            "idb_oper_reg_disable",
                                            "idb_oper_reg_enable") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.idb_oper_attr_update.is_set or
                                self.idb_oper_caps_add.is_set or
                                self.idb_oper_caps_remove.is_set or
                                self.idb_oper_reg_disable.is_set or
                                self.idb_oper_reg_enable.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.idb_oper_attr_update.yfilter != YFilter.not_set or
                                self.idb_oper_caps_add.yfilter != YFilter.not_set or
                                self.idb_oper_caps_remove.yfilter != YFilter.not_set or
                                self.idb_oper_reg_disable.yfilter != YFilter.not_set or
                                self.idb_oper_reg_enable.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface-oper" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.idb_oper_attr_update.is_set or self.idb_oper_attr_update.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_oper_attr_update.get_name_leafdata())
                            if (self.idb_oper_caps_add.is_set or self.idb_oper_caps_add.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_oper_caps_add.get_name_leafdata())
                            if (self.idb_oper_caps_remove.is_set or self.idb_oper_caps_remove.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_oper_caps_remove.get_name_leafdata())
                            if (self.idb_oper_reg_disable.is_set or self.idb_oper_reg_disable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_oper_reg_disable.get_name_leafdata())
                            if (self.idb_oper_reg_enable.is_set or self.idb_oper_reg_enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_oper_reg_enable.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "idb-oper-attr-update" or name == "idb-oper-caps-add" or name == "idb-oper-caps-remove" or name == "idb-oper-reg-disable" or name == "idb-oper-reg-enable"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "idb-oper-attr-update"):
                                self.idb_oper_attr_update = value
                                self.idb_oper_attr_update.value_namespace = name_space
                                self.idb_oper_attr_update.value_namespace_prefix = name_space_prefix
                            if(value_path == "idb-oper-caps-add"):
                                self.idb_oper_caps_add = value
                                self.idb_oper_caps_add.value_namespace = name_space
                                self.idb_oper_caps_add.value_namespace_prefix = name_space_prefix
                            if(value_path == "idb-oper-caps-remove"):
                                self.idb_oper_caps_remove = value
                                self.idb_oper_caps_remove.value_namespace = name_space
                                self.idb_oper_caps_remove.value_namespace_prefix = name_space_prefix
                            if(value_path == "idb-oper-reg-disable"):
                                self.idb_oper_reg_disable = value
                                self.idb_oper_reg_disable.value_namespace = name_space
                                self.idb_oper_reg_disable.value_namespace_prefix = name_space_prefix
                            if(value_path == "idb-oper-reg-enable"):
                                self.idb_oper_reg_enable = value
                                self.idb_oper_reg_enable.value_namespace = name_space
                                self.idb_oper_reg_enable.value_namespace_prefix = name_space_prefix


                    class InterfaceStatus(Entity):
                        """
                        Interface Status
                        
                        .. attribute:: idb_client_eoms_pending
                        
                        	Interface Client EOMS Pending
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_caps_added
                        
                        	Interface State Caps Added
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_fwd_ref
                        
                        	Interface Forward Referenced
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_owned_re_source
                        
                        	Interface State Owned Resource
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_p_end_caps_rem
                        
                        	Interface Caps Remove Pending
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_p_end_reg_disable
                        
                        	Interface Registration Disable Pending
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_registered
                        
                        	Interface State Registered
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_stale
                        
                        	Interface State Stale
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, self).__init__()

                            self.yang_name = "interface-status"
                            self.yang_parent_name = "interface"

                            self.idb_client_eoms_pending = YLeaf(YType.boolean, "idb-client-eoms-pending")

                            self.idb_state_caps_added = YLeaf(YType.boolean, "idb-state-caps-added")

                            self.idb_state_fwd_ref = YLeaf(YType.boolean, "idb-state-fwd-ref")

                            self.idb_state_owned_re_source = YLeaf(YType.boolean, "idb-state-owned-re-source")

                            self.idb_state_p_end_caps_rem = YLeaf(YType.boolean, "idb-state-p-end-caps-rem")

                            self.idb_state_p_end_reg_disable = YLeaf(YType.boolean, "idb-state-p-end-reg-disable")

                            self.idb_state_registered = YLeaf(YType.boolean, "idb-state-registered")

                            self.idb_state_stale = YLeaf(YType.boolean, "idb-state-stale")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("idb_client_eoms_pending",
                                            "idb_state_caps_added",
                                            "idb_state_fwd_ref",
                                            "idb_state_owned_re_source",
                                            "idb_state_p_end_caps_rem",
                                            "idb_state_p_end_reg_disable",
                                            "idb_state_registered",
                                            "idb_state_stale") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.idb_client_eoms_pending.is_set or
                                self.idb_state_caps_added.is_set or
                                self.idb_state_fwd_ref.is_set or
                                self.idb_state_owned_re_source.is_set or
                                self.idb_state_p_end_caps_rem.is_set or
                                self.idb_state_p_end_reg_disable.is_set or
                                self.idb_state_registered.is_set or
                                self.idb_state_stale.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.idb_client_eoms_pending.yfilter != YFilter.not_set or
                                self.idb_state_caps_added.yfilter != YFilter.not_set or
                                self.idb_state_fwd_ref.yfilter != YFilter.not_set or
                                self.idb_state_owned_re_source.yfilter != YFilter.not_set or
                                self.idb_state_p_end_caps_rem.yfilter != YFilter.not_set or
                                self.idb_state_p_end_reg_disable.yfilter != YFilter.not_set or
                                self.idb_state_registered.yfilter != YFilter.not_set or
                                self.idb_state_stale.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface-status" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.idb_client_eoms_pending.is_set or self.idb_client_eoms_pending.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_client_eoms_pending.get_name_leafdata())
                            if (self.idb_state_caps_added.is_set or self.idb_state_caps_added.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_state_caps_added.get_name_leafdata())
                            if (self.idb_state_fwd_ref.is_set or self.idb_state_fwd_ref.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_state_fwd_ref.get_name_leafdata())
                            if (self.idb_state_owned_re_source.is_set or self.idb_state_owned_re_source.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_state_owned_re_source.get_name_leafdata())
                            if (self.idb_state_p_end_caps_rem.is_set or self.idb_state_p_end_caps_rem.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_state_p_end_caps_rem.get_name_leafdata())
                            if (self.idb_state_p_end_reg_disable.is_set or self.idb_state_p_end_reg_disable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_state_p_end_reg_disable.get_name_leafdata())
                            if (self.idb_state_registered.is_set or self.idb_state_registered.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_state_registered.get_name_leafdata())
                            if (self.idb_state_stale.is_set or self.idb_state_stale.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idb_state_stale.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "idb-client-eoms-pending" or name == "idb-state-caps-added" or name == "idb-state-fwd-ref" or name == "idb-state-owned-re-source" or name == "idb-state-p-end-caps-rem" or name == "idb-state-p-end-reg-disable" or name == "idb-state-registered" or name == "idb-state-stale"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "idb-client-eoms-pending"):
                                self.idb_client_eoms_pending = value
                                self.idb_client_eoms_pending.value_namespace = name_space
                                self.idb_client_eoms_pending.value_namespace_prefix = name_space_prefix
                            if(value_path == "idb-state-caps-added"):
                                self.idb_state_caps_added = value
                                self.idb_state_caps_added.value_namespace = name_space
                                self.idb_state_caps_added.value_namespace_prefix = name_space_prefix
                            if(value_path == "idb-state-fwd-ref"):
                                self.idb_state_fwd_ref = value
                                self.idb_state_fwd_ref.value_namespace = name_space
                                self.idb_state_fwd_ref.value_namespace_prefix = name_space_prefix
                            if(value_path == "idb-state-owned-re-source"):
                                self.idb_state_owned_re_source = value
                                self.idb_state_owned_re_source.value_namespace = name_space
                                self.idb_state_owned_re_source.value_namespace_prefix = name_space_prefix
                            if(value_path == "idb-state-p-end-caps-rem"):
                                self.idb_state_p_end_caps_rem = value
                                self.idb_state_p_end_caps_rem.value_namespace = name_space
                                self.idb_state_p_end_caps_rem.value_namespace_prefix = name_space_prefix
                            if(value_path == "idb-state-p-end-reg-disable"):
                                self.idb_state_p_end_reg_disable = value
                                self.idb_state_p_end_reg_disable.value_namespace = name_space
                                self.idb_state_p_end_reg_disable.value_namespace_prefix = name_space_prefix
                            if(value_path == "idb-state-registered"):
                                self.idb_state_registered = value
                                self.idb_state_registered.value_namespace = name_space
                                self.idb_state_registered.value_namespace_prefix = name_space_prefix
                            if(value_path == "idb-state-stale"):
                                self.idb_state_stale = value
                                self.idb_state_stale.value_namespace = name_space
                                self.idb_state_stale.value_namespace_prefix = name_space_prefix


                    class ClientStatus(Entity):
                        """
                        Interface status for each client
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:   :py:class:`SergShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowComp>`
                        
                        .. attribute:: serg_show_idb_client_eoms_pending
                        
                        	SERG SHOW IDB CLIENT EOMS PENDING
                        	**type**\:  bool
                        
                        .. attribute:: serg_show_idb_client_sync_eod_pending
                        
                        	SERG SHOW IDB CLIENT SYNC EOD PENDING
                        	**type**\:  bool
                        
                        .. attribute:: session_count
                        
                        	session count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, self).__init__()

                            self.yang_name = "client-status"
                            self.yang_parent_name = "interface"

                            self.component = YLeaf(YType.enumeration, "component")

                            self.serg_show_idb_client_eoms_pending = YLeaf(YType.boolean, "serg-show-idb-client-eoms-pending")

                            self.serg_show_idb_client_sync_eod_pending = YLeaf(YType.boolean, "serg-show-idb-client-sync-eod-pending")

                            self.session_count = YLeaf(YType.uint32, "session-count")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("component",
                                            "serg_show_idb_client_eoms_pending",
                                            "serg_show_idb_client_sync_eod_pending",
                                            "session_count") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.component.is_set or
                                self.serg_show_idb_client_eoms_pending.is_set or
                                self.serg_show_idb_client_sync_eod_pending.is_set or
                                self.session_count.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.component.yfilter != YFilter.not_set or
                                self.serg_show_idb_client_eoms_pending.yfilter != YFilter.not_set or
                                self.serg_show_idb_client_sync_eod_pending.yfilter != YFilter.not_set or
                                self.session_count.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "client-status" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.component.is_set or self.component.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.component.get_name_leafdata())
                            if (self.serg_show_idb_client_eoms_pending.is_set or self.serg_show_idb_client_eoms_pending.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.serg_show_idb_client_eoms_pending.get_name_leafdata())
                            if (self.serg_show_idb_client_sync_eod_pending.is_set or self.serg_show_idb_client_sync_eod_pending.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.serg_show_idb_client_sync_eod_pending.get_name_leafdata())
                            if (self.session_count.is_set or self.session_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_count.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "component" or name == "serg-show-idb-client-eoms-pending" or name == "serg-show-idb-client-sync-eod-pending" or name == "session-count"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "component"):
                                self.component = value
                                self.component.value_namespace = name_space
                                self.component.value_namespace_prefix = name_space_prefix
                            if(value_path == "serg-show-idb-client-eoms-pending"):
                                self.serg_show_idb_client_eoms_pending = value
                                self.serg_show_idb_client_eoms_pending.value_namespace = name_space
                                self.serg_show_idb_client_eoms_pending.value_namespace_prefix = name_space_prefix
                            if(value_path == "serg-show-idb-client-sync-eod-pending"):
                                self.serg_show_idb_client_sync_eod_pending = value
                                self.serg_show_idb_client_sync_eod_pending.value_namespace = name_space
                                self.serg_show_idb_client_sync_eod_pending.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-count"):
                                self.session_count = value
                                self.session_count.value_namespace = name_space
                                self.session_count.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.client_status:
                            if (c.has_data()):
                                return True
                        return (
                            self.interface.is_set or
                            self.forward_referenced.is_set or
                            self.group_id.is_set or
                            self.interface_attribute_update_error_count.is_set or
                            self.interface_caps_add_error_count.is_set or
                            self.interface_caps_remove_error_count.is_set or
                            self.interface_disable_error_count.is_set or
                            self.interface_enable_error_count.is_set or
                            self.interface_name.is_set or
                            self.interface_synchronization_id.is_set or
                            self.role.is_set or
                            self.session_count.is_set or
                            (self.interface_oper is not None and self.interface_oper.has_data()) or
                            (self.interface_status is not None and self.interface_status.has_data()))

                    def has_operation(self):
                        for c in self.client_status:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.forward_referenced.yfilter != YFilter.not_set or
                            self.group_id.yfilter != YFilter.not_set or
                            self.interface_attribute_update_error_count.yfilter != YFilter.not_set or
                            self.interface_caps_add_error_count.yfilter != YFilter.not_set or
                            self.interface_caps_remove_error_count.yfilter != YFilter.not_set or
                            self.interface_disable_error_count.yfilter != YFilter.not_set or
                            self.interface_enable_error_count.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.interface_synchronization_id.yfilter != YFilter.not_set or
                            self.role.yfilter != YFilter.not_set or
                            self.session_count.yfilter != YFilter.not_set or
                            (self.interface_oper is not None and self.interface_oper.has_operation()) or
                            (self.interface_status is not None and self.interface_status.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface='" + self.interface.get() + "']" + path_buffer

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
                        if (self.forward_referenced.is_set or self.forward_referenced.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.forward_referenced.get_name_leafdata())
                        if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_id.get_name_leafdata())
                        if (self.interface_attribute_update_error_count.is_set or self.interface_attribute_update_error_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_attribute_update_error_count.get_name_leafdata())
                        if (self.interface_caps_add_error_count.is_set or self.interface_caps_add_error_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_caps_add_error_count.get_name_leafdata())
                        if (self.interface_caps_remove_error_count.is_set or self.interface_caps_remove_error_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_caps_remove_error_count.get_name_leafdata())
                        if (self.interface_disable_error_count.is_set or self.interface_disable_error_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_disable_error_count.get_name_leafdata())
                        if (self.interface_enable_error_count.is_set or self.interface_enable_error_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_enable_error_count.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.interface_synchronization_id.is_set or self.interface_synchronization_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_synchronization_id.get_name_leafdata())
                        if (self.role.is_set or self.role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.role.get_name_leafdata())
                        if (self.session_count.is_set or self.session_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "client-status"):
                            for c in self.client_status:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.client_status.append(c)
                            return c

                        if (child_yang_name == "interface-oper"):
                            if (self.interface_oper is None):
                                self.interface_oper = SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper()
                                self.interface_oper.parent = self
                                self._children_name_map["interface_oper"] = "interface-oper"
                            return self.interface_oper

                        if (child_yang_name == "interface-status"):
                            if (self.interface_status is None):
                                self.interface_status = SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus()
                                self.interface_status.parent = self
                                self._children_name_map["interface_status"] = "interface-status"
                            return self.interface_status

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "client-status" or name == "interface-oper" or name == "interface-status" or name == "interface" or name == "forward-referenced" or name == "group-id" or name == "interface-attribute-update-error-count" or name == "interface-caps-add-error-count" or name == "interface-caps-remove-error-count" or name == "interface-disable-error-count" or name == "interface-enable-error-count" or name == "interface-name" or name == "interface-synchronization-id" or name == "role" or name == "session-count"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "forward-referenced"):
                            self.forward_referenced = value
                            self.forward_referenced.value_namespace = name_space
                            self.forward_referenced.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-id"):
                            self.group_id = value
                            self.group_id.value_namespace = name_space
                            self.group_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-attribute-update-error-count"):
                            self.interface_attribute_update_error_count = value
                            self.interface_attribute_update_error_count.value_namespace = name_space
                            self.interface_attribute_update_error_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-caps-add-error-count"):
                            self.interface_caps_add_error_count = value
                            self.interface_caps_add_error_count.value_namespace = name_space
                            self.interface_caps_add_error_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-caps-remove-error-count"):
                            self.interface_caps_remove_error_count = value
                            self.interface_caps_remove_error_count.value_namespace = name_space
                            self.interface_caps_remove_error_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-disable-error-count"):
                            self.interface_disable_error_count = value
                            self.interface_disable_error_count.value_namespace = name_space
                            self.interface_disable_error_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-enable-error-count"):
                            self.interface_enable_error_count = value
                            self.interface_enable_error_count.value_namespace = name_space
                            self.interface_enable_error_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-synchronization-id"):
                            self.interface_synchronization_id = value
                            self.interface_synchronization_id.value_namespace = name_space
                            self.interface_synchronization_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "role"):
                            self.role = value
                            self.role.value_namespace = name_space
                            self.role.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-count"):
                            self.session_count = value
                            self.session_count.value_namespace = name_space
                            self.session_count.value_namespace_prefix = name_space_prefix

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

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionRedundancyAgent.Nodes.Node.Interfaces.Interface()
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


            class StatsGlobal(Entity):
                """
                Stats Global
                
                .. attribute:: client_init_sync_time_stamp
                
                	Synchronization TimeStamp
                	**type**\:  str
                
                .. attribute:: client_status
                
                	Client Status
                	**type**\: list of    :py:class:`ClientStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus>`
                
                .. attribute:: intf_status_statistics
                
                	intf status statistics
                	**type**\:   :py:class:`IntfStatusStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics>`
                
                .. attribute:: opaque_memory_status
                
                	Opaque memory Stats
                	**type**\: list of    :py:class:`OpaqueMemoryStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus>`
                
                .. attribute:: peer_action_timer
                
                	Value in Seconds to trigger the peer actions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: peer_init_sync_time_stamp
                
                	Synchronization TimeStamp
                	**type**\:  str
                
                .. attribute:: redundancy_role
                
                	Redundancy Role
                	**type**\:  str
                
                .. attribute:: restart_client_sync_in_progress
                
                	Restart Client Sync In Progress Flag
                	**type**\:  bool
                
                .. attribute:: restart_peer_sync_in_progress
                
                	Restart Peer Sync In Progress Flag
                	**type**\:  bool
                
                .. attribute:: retry_timer_remaining
                
                	Value in Seconds to trigger the retry
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: source_interface_ipv4_address
                
                	Source Interface IPv4 Address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: source_interface_ipv6_address
                
                	Source Interface IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: source_interface_name
                
                	Source Interface Name
                	**type**\:  str
                
                .. attribute:: sync_in_progress
                
                	Sync In Progress Flag
                	**type**\:  bool
                
                .. attribute:: tx_list_client_connection_down
                
                	TxListClientConnectionDown
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_connection_up
                
                	TxListClientConnectionUp
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_de_registration_invalid
                
                	TxListClientDeRegistrationInvalid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_message_call_back
                
                	TxListClientMessageCallBack
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_peer_done
                
                	TxListClientPeerDone
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_command_invalid
                
                	TxListClientReceiveCommandInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_command_valid
                
                	TxListClientReceiveCommandValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_invalid
                
                	TxListClientReceiveInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_session_session_invalid
                
                	TxListClientReceiveSessionSessionInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_session_sessionvalid
                
                	TxListClientReceiveSessionSessionValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_valid
                
                	TxListClientReceiveValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_registration_invalid
                
                	TxListClientRegistrationInvalid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_over_tcp_status
                
                	TCP TxList Statistics
                	**type**\: list of    :py:class:`TxListOverTcpStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus>`
                
                .. attribute:: tx_list_peer_cmd_connection_down_not_ok
                
                	TxListPeerCmdConnectionDownNotOk
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_cmd_connection_up_not_ok
                
                	TxListPeerCmdConnectionUpNotOk
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_de_registration_invalid
                
                	TxListPeerDeRegistrationInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_done
                
                	TxListPeerDone
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_message_call_back_invalid
                
                	TxListPeerMessageCallBackInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_message_call_back_valid
                
                	TxListPeerMessageCallBackValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_registration_invalid
                
                	TxListPeerRegistrationInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_session_connection_down_not_ok
                
                	TxListPeerSessionConnectionDownNotOk
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_session_connection_up_not_ok
                
                	TxListPeerSessionConnectionUpNotOk
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_timer_handler
                
                	TxListPeerTimerHandler
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_statistics
                
                	tx list statistics
                	**type**\:   :py:class:`TxListStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics>`
                
                .. attribute:: vrf_name
                
                	VRF Name
                	**type**\:  str
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.StatsGlobal, self).__init__()

                    self.yang_name = "stats-global"
                    self.yang_parent_name = "node"

                    self.client_init_sync_time_stamp = YLeaf(YType.str, "client-init-sync-time-stamp")

                    self.peer_action_timer = YLeaf(YType.uint32, "peer-action-timer")

                    self.peer_init_sync_time_stamp = YLeaf(YType.str, "peer-init-sync-time-stamp")

                    self.redundancy_role = YLeaf(YType.str, "redundancy-role")

                    self.restart_client_sync_in_progress = YLeaf(YType.boolean, "restart-client-sync-in-progress")

                    self.restart_peer_sync_in_progress = YLeaf(YType.boolean, "restart-peer-sync-in-progress")

                    self.retry_timer_remaining = YLeaf(YType.uint32, "retry-timer-remaining")

                    self.source_interface_ipv4_address = YLeaf(YType.str, "source-interface-ipv4-address")

                    self.source_interface_ipv6_address = YLeaf(YType.str, "source-interface-ipv6-address")

                    self.source_interface_name = YLeaf(YType.str, "source-interface-name")

                    self.sync_in_progress = YLeaf(YType.boolean, "sync-in-progress")

                    self.tx_list_client_connection_down = YLeaf(YType.uint32, "tx-list-client-connection-down")

                    self.tx_list_client_connection_up = YLeaf(YType.uint32, "tx-list-client-connection-up")

                    self.tx_list_client_de_registration_invalid = YLeaf(YType.uint32, "tx-list-client-de-registration-invalid")

                    self.tx_list_client_message_call_back = YLeaf(YType.uint32, "tx-list-client-message-call-back")

                    self.tx_list_client_peer_done = YLeaf(YType.uint32, "tx-list-client-peer-done")

                    self.tx_list_client_receive_command_invalid = YLeaf(YType.uint32, "tx-list-client-receive-command-invalid")

                    self.tx_list_client_receive_command_valid = YLeaf(YType.uint32, "tx-list-client-receive-command-valid")

                    self.tx_list_client_receive_invalid = YLeaf(YType.uint32, "tx-list-client-receive-invalid")

                    self.tx_list_client_receive_session_session_invalid = YLeaf(YType.uint32, "tx-list-client-receive-session-session-invalid")

                    self.tx_list_client_receive_session_sessionvalid = YLeaf(YType.uint32, "tx-list-client-receive-session-sessionvalid")

                    self.tx_list_client_receive_valid = YLeaf(YType.uint32, "tx-list-client-receive-valid")

                    self.tx_list_client_registration_invalid = YLeaf(YType.uint32, "tx-list-client-registration-invalid")

                    self.tx_list_peer_cmd_connection_down_not_ok = YLeaf(YType.uint32, "tx-list-peer-cmd-connection-down-not-ok")

                    self.tx_list_peer_cmd_connection_up_not_ok = YLeaf(YType.uint32, "tx-list-peer-cmd-connection-up-not-ok")

                    self.tx_list_peer_de_registration_invalid = YLeaf(YType.uint32, "tx-list-peer-de-registration-invalid")

                    self.tx_list_peer_done = YLeaf(YType.uint32, "tx-list-peer-done")

                    self.tx_list_peer_message_call_back_invalid = YLeaf(YType.uint32, "tx-list-peer-message-call-back-invalid")

                    self.tx_list_peer_message_call_back_valid = YLeaf(YType.uint32, "tx-list-peer-message-call-back-valid")

                    self.tx_list_peer_registration_invalid = YLeaf(YType.uint32, "tx-list-peer-registration-invalid")

                    self.tx_list_peer_session_connection_down_not_ok = YLeaf(YType.uint32, "tx-list-peer-session-connection-down-not-ok")

                    self.tx_list_peer_session_connection_up_not_ok = YLeaf(YType.uint32, "tx-list-peer-session-connection-up-not-ok")

                    self.tx_list_peer_timer_handler = YLeaf(YType.uint32, "tx-list-peer-timer-handler")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.intf_status_statistics = SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics()
                    self.intf_status_statistics.parent = self
                    self._children_name_map["intf_status_statistics"] = "intf-status-statistics"
                    self._children_yang_names.add("intf-status-statistics")

                    self.tx_list_statistics = SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics()
                    self.tx_list_statistics.parent = self
                    self._children_name_map["tx_list_statistics"] = "tx-list-statistics"
                    self._children_yang_names.add("tx-list-statistics")

                    self.client_status = YList(self)
                    self.opaque_memory_status = YList(self)
                    self.tx_list_over_tcp_status = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("client_init_sync_time_stamp",
                                    "peer_action_timer",
                                    "peer_init_sync_time_stamp",
                                    "redundancy_role",
                                    "restart_client_sync_in_progress",
                                    "restart_peer_sync_in_progress",
                                    "retry_timer_remaining",
                                    "source_interface_ipv4_address",
                                    "source_interface_ipv6_address",
                                    "source_interface_name",
                                    "sync_in_progress",
                                    "tx_list_client_connection_down",
                                    "tx_list_client_connection_up",
                                    "tx_list_client_de_registration_invalid",
                                    "tx_list_client_message_call_back",
                                    "tx_list_client_peer_done",
                                    "tx_list_client_receive_command_invalid",
                                    "tx_list_client_receive_command_valid",
                                    "tx_list_client_receive_invalid",
                                    "tx_list_client_receive_session_session_invalid",
                                    "tx_list_client_receive_session_sessionvalid",
                                    "tx_list_client_receive_valid",
                                    "tx_list_client_registration_invalid",
                                    "tx_list_peer_cmd_connection_down_not_ok",
                                    "tx_list_peer_cmd_connection_up_not_ok",
                                    "tx_list_peer_de_registration_invalid",
                                    "tx_list_peer_done",
                                    "tx_list_peer_message_call_back_invalid",
                                    "tx_list_peer_message_call_back_valid",
                                    "tx_list_peer_registration_invalid",
                                    "tx_list_peer_session_connection_down_not_ok",
                                    "tx_list_peer_session_connection_up_not_ok",
                                    "tx_list_peer_timer_handler",
                                    "vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SessionRedundancyAgent.Nodes.Node.StatsGlobal, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionRedundancyAgent.Nodes.Node.StatsGlobal, self).__setattr__(name, value)


                class IntfStatusStatistics(Entity):
                    """
                    intf status statistics
                    
                    .. attribute:: grp_bound_cnt
                    
                    	No. of interface bound to a group
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: non_stale_cnt
                    
                    	No. of non stale interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pend_caps_rem_cnt
                    
                    	No. of interfaces pending caps remove
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pend_other_batch_oper_cnt
                    
                    	No. of interfaces pending for other (except unreg/caps rem) batch oper
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pend_reg_disable_cnt
                    
                    	No. of interfaces pending red disable
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics, self).__init__()

                        self.yang_name = "intf-status-statistics"
                        self.yang_parent_name = "stats-global"

                        self.grp_bound_cnt = YLeaf(YType.uint32, "grp-bound-cnt")

                        self.non_stale_cnt = YLeaf(YType.uint32, "non-stale-cnt")

                        self.pend_caps_rem_cnt = YLeaf(YType.uint32, "pend-caps-rem-cnt")

                        self.pend_other_batch_oper_cnt = YLeaf(YType.uint32, "pend-other-batch-oper-cnt")

                        self.pend_reg_disable_cnt = YLeaf(YType.uint32, "pend-reg-disable-cnt")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("grp_bound_cnt",
                                        "non_stale_cnt",
                                        "pend_caps_rem_cnt",
                                        "pend_other_batch_oper_cnt",
                                        "pend_reg_disable_cnt") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.grp_bound_cnt.is_set or
                            self.non_stale_cnt.is_set or
                            self.pend_caps_rem_cnt.is_set or
                            self.pend_other_batch_oper_cnt.is_set or
                            self.pend_reg_disable_cnt.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.grp_bound_cnt.yfilter != YFilter.not_set or
                            self.non_stale_cnt.yfilter != YFilter.not_set or
                            self.pend_caps_rem_cnt.yfilter != YFilter.not_set or
                            self.pend_other_batch_oper_cnt.yfilter != YFilter.not_set or
                            self.pend_reg_disable_cnt.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "intf-status-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.grp_bound_cnt.is_set or self.grp_bound_cnt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.grp_bound_cnt.get_name_leafdata())
                        if (self.non_stale_cnt.is_set or self.non_stale_cnt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.non_stale_cnt.get_name_leafdata())
                        if (self.pend_caps_rem_cnt.is_set or self.pend_caps_rem_cnt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pend_caps_rem_cnt.get_name_leafdata())
                        if (self.pend_other_batch_oper_cnt.is_set or self.pend_other_batch_oper_cnt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pend_other_batch_oper_cnt.get_name_leafdata())
                        if (self.pend_reg_disable_cnt.is_set or self.pend_reg_disable_cnt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pend_reg_disable_cnt.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "grp-bound-cnt" or name == "non-stale-cnt" or name == "pend-caps-rem-cnt" or name == "pend-other-batch-oper-cnt" or name == "pend-reg-disable-cnt"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "grp-bound-cnt"):
                            self.grp_bound_cnt = value
                            self.grp_bound_cnt.value_namespace = name_space
                            self.grp_bound_cnt.value_namespace_prefix = name_space_prefix
                        if(value_path == "non-stale-cnt"):
                            self.non_stale_cnt = value
                            self.non_stale_cnt.value_namespace = name_space
                            self.non_stale_cnt.value_namespace_prefix = name_space_prefix
                        if(value_path == "pend-caps-rem-cnt"):
                            self.pend_caps_rem_cnt = value
                            self.pend_caps_rem_cnt.value_namespace = name_space
                            self.pend_caps_rem_cnt.value_namespace_prefix = name_space_prefix
                        if(value_path == "pend-other-batch-oper-cnt"):
                            self.pend_other_batch_oper_cnt = value
                            self.pend_other_batch_oper_cnt.value_namespace = name_space
                            self.pend_other_batch_oper_cnt.value_namespace_prefix = name_space_prefix
                        if(value_path == "pend-reg-disable-cnt"):
                            self.pend_reg_disable_cnt = value
                            self.pend_reg_disable_cnt.value_namespace = name_space
                            self.pend_reg_disable_cnt.value_namespace_prefix = name_space_prefix


                class TxListStatistics(Entity):
                    """
                    tx list statistics
                    
                    .. attribute:: tx_list_clean_command
                    
                    	TxListCleanCommand
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clean_marker
                    
                    	TxListCleanMarker
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clean_negotiation
                    
                    	TxListCleanNegotiation
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_command_ok
                    
                    	TxListEncodeCommandOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_command_partial_write
                    
                    	TxListEncodeCommandPartialWrite
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_marker_ok
                    
                    	TxListEncodeMarkerOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_marker_partial_write
                    
                    	TxListEncodeMarkerPartialWrite
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_negotiation_ok
                    
                    	TxListEncodeNegotiationOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_negotiation_partial_write
                    
                    	TxListEncodeNegotiationPartialWrite
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics, self).__init__()

                        self.yang_name = "tx-list-statistics"
                        self.yang_parent_name = "stats-global"

                        self.tx_list_clean_command = YLeaf(YType.uint32, "tx-list-clean-command")

                        self.tx_list_clean_marker = YLeaf(YType.uint32, "tx-list-clean-marker")

                        self.tx_list_clean_negotiation = YLeaf(YType.uint32, "tx-list-clean-negotiation")

                        self.tx_list_encode_command_ok = YLeaf(YType.uint32, "tx-list-encode-command-ok")

                        self.tx_list_encode_command_partial_write = YLeaf(YType.uint32, "tx-list-encode-command-partial-write")

                        self.tx_list_encode_marker_ok = YLeaf(YType.uint32, "tx-list-encode-marker-ok")

                        self.tx_list_encode_marker_partial_write = YLeaf(YType.uint32, "tx-list-encode-marker-partial-write")

                        self.tx_list_encode_negotiation_ok = YLeaf(YType.uint32, "tx-list-encode-negotiation-ok")

                        self.tx_list_encode_negotiation_partial_write = YLeaf(YType.uint32, "tx-list-encode-negotiation-partial-write")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("tx_list_clean_command",
                                        "tx_list_clean_marker",
                                        "tx_list_clean_negotiation",
                                        "tx_list_encode_command_ok",
                                        "tx_list_encode_command_partial_write",
                                        "tx_list_encode_marker_ok",
                                        "tx_list_encode_marker_partial_write",
                                        "tx_list_encode_negotiation_ok",
                                        "tx_list_encode_negotiation_partial_write") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.tx_list_clean_command.is_set or
                            self.tx_list_clean_marker.is_set or
                            self.tx_list_clean_negotiation.is_set or
                            self.tx_list_encode_command_ok.is_set or
                            self.tx_list_encode_command_partial_write.is_set or
                            self.tx_list_encode_marker_ok.is_set or
                            self.tx_list_encode_marker_partial_write.is_set or
                            self.tx_list_encode_negotiation_ok.is_set or
                            self.tx_list_encode_negotiation_partial_write.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.tx_list_clean_command.yfilter != YFilter.not_set or
                            self.tx_list_clean_marker.yfilter != YFilter.not_set or
                            self.tx_list_clean_negotiation.yfilter != YFilter.not_set or
                            self.tx_list_encode_command_ok.yfilter != YFilter.not_set or
                            self.tx_list_encode_command_partial_write.yfilter != YFilter.not_set or
                            self.tx_list_encode_marker_ok.yfilter != YFilter.not_set or
                            self.tx_list_encode_marker_partial_write.yfilter != YFilter.not_set or
                            self.tx_list_encode_negotiation_ok.yfilter != YFilter.not_set or
                            self.tx_list_encode_negotiation_partial_write.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tx-list-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.tx_list_clean_command.is_set or self.tx_list_clean_command.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_clean_command.get_name_leafdata())
                        if (self.tx_list_clean_marker.is_set or self.tx_list_clean_marker.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_clean_marker.get_name_leafdata())
                        if (self.tx_list_clean_negotiation.is_set or self.tx_list_clean_negotiation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_clean_negotiation.get_name_leafdata())
                        if (self.tx_list_encode_command_ok.is_set or self.tx_list_encode_command_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_encode_command_ok.get_name_leafdata())
                        if (self.tx_list_encode_command_partial_write.is_set or self.tx_list_encode_command_partial_write.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_encode_command_partial_write.get_name_leafdata())
                        if (self.tx_list_encode_marker_ok.is_set or self.tx_list_encode_marker_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_encode_marker_ok.get_name_leafdata())
                        if (self.tx_list_encode_marker_partial_write.is_set or self.tx_list_encode_marker_partial_write.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_encode_marker_partial_write.get_name_leafdata())
                        if (self.tx_list_encode_negotiation_ok.is_set or self.tx_list_encode_negotiation_ok.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_encode_negotiation_ok.get_name_leafdata())
                        if (self.tx_list_encode_negotiation_partial_write.is_set or self.tx_list_encode_negotiation_partial_write.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tx_list_encode_negotiation_partial_write.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tx-list-clean-command" or name == "tx-list-clean-marker" or name == "tx-list-clean-negotiation" or name == "tx-list-encode-command-ok" or name == "tx-list-encode-command-partial-write" or name == "tx-list-encode-marker-ok" or name == "tx-list-encode-marker-partial-write" or name == "tx-list-encode-negotiation-ok" or name == "tx-list-encode-negotiation-partial-write"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "tx-list-clean-command"):
                            self.tx_list_clean_command = value
                            self.tx_list_clean_command.value_namespace = name_space
                            self.tx_list_clean_command.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-clean-marker"):
                            self.tx_list_clean_marker = value
                            self.tx_list_clean_marker.value_namespace = name_space
                            self.tx_list_clean_marker.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-clean-negotiation"):
                            self.tx_list_clean_negotiation = value
                            self.tx_list_clean_negotiation.value_namespace = name_space
                            self.tx_list_clean_negotiation.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-encode-command-ok"):
                            self.tx_list_encode_command_ok = value
                            self.tx_list_encode_command_ok.value_namespace = name_space
                            self.tx_list_encode_command_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-encode-command-partial-write"):
                            self.tx_list_encode_command_partial_write = value
                            self.tx_list_encode_command_partial_write.value_namespace = name_space
                            self.tx_list_encode_command_partial_write.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-encode-marker-ok"):
                            self.tx_list_encode_marker_ok = value
                            self.tx_list_encode_marker_ok.value_namespace = name_space
                            self.tx_list_encode_marker_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-encode-marker-partial-write"):
                            self.tx_list_encode_marker_partial_write = value
                            self.tx_list_encode_marker_partial_write.value_namespace = name_space
                            self.tx_list_encode_marker_partial_write.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-encode-negotiation-ok"):
                            self.tx_list_encode_negotiation_ok = value
                            self.tx_list_encode_negotiation_ok.value_namespace = name_space
                            self.tx_list_encode_negotiation_ok.value_namespace_prefix = name_space_prefix
                        if(value_path == "tx-list-encode-negotiation-partial-write"):
                            self.tx_list_encode_negotiation_partial_write = value
                            self.tx_list_encode_negotiation_partial_write.value_namespace = name_space
                            self.tx_list_encode_negotiation_partial_write.value_namespace_prefix = name_space_prefix


                class ClientStatus(Entity):
                    """
                    Client Status
                    
                    .. attribute:: clean_up_timer_remaining
                    
                    	Value in Seconds to trigger the client cleanup
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: client_connection_status
                    
                    	ClientConnectionStatus
                    	**type**\:  bool
                    
                    .. attribute:: client_initialization_synchronization_pending
                    
                    	ClientInitializationSynchronizationPending
                    	**type**\:  bool
                    
                    .. attribute:: client_synchronization_end_of_download_pending
                    
                    	ClientSynchronizationEndOfDownloadPending
                    	**type**\:  bool
                    
                    .. attribute:: component
                    
                    	Component
                    	**type**\:   :py:class:`SergShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowComp>`
                    
                    .. attribute:: down_time_stamp
                    
                    	DownTimeStamp
                    	**type**\:  str
                    
                    .. attribute:: up_time_stamp
                    
                    	UpTimeStamp
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus, self).__init__()

                        self.yang_name = "client-status"
                        self.yang_parent_name = "stats-global"

                        self.clean_up_timer_remaining = YLeaf(YType.uint32, "clean-up-timer-remaining")

                        self.client_connection_status = YLeaf(YType.boolean, "client-connection-status")

                        self.client_initialization_synchronization_pending = YLeaf(YType.boolean, "client-initialization-synchronization-pending")

                        self.client_synchronization_end_of_download_pending = YLeaf(YType.boolean, "client-synchronization-end-of-download-pending")

                        self.component = YLeaf(YType.enumeration, "component")

                        self.down_time_stamp = YLeaf(YType.str, "down-time-stamp")

                        self.up_time_stamp = YLeaf(YType.str, "up-time-stamp")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("clean_up_timer_remaining",
                                        "client_connection_status",
                                        "client_initialization_synchronization_pending",
                                        "client_synchronization_end_of_download_pending",
                                        "component",
                                        "down_time_stamp",
                                        "up_time_stamp") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.clean_up_timer_remaining.is_set or
                            self.client_connection_status.is_set or
                            self.client_initialization_synchronization_pending.is_set or
                            self.client_synchronization_end_of_download_pending.is_set or
                            self.component.is_set or
                            self.down_time_stamp.is_set or
                            self.up_time_stamp.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.clean_up_timer_remaining.yfilter != YFilter.not_set or
                            self.client_connection_status.yfilter != YFilter.not_set or
                            self.client_initialization_synchronization_pending.yfilter != YFilter.not_set or
                            self.client_synchronization_end_of_download_pending.yfilter != YFilter.not_set or
                            self.component.yfilter != YFilter.not_set or
                            self.down_time_stamp.yfilter != YFilter.not_set or
                            self.up_time_stamp.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "client-status" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.clean_up_timer_remaining.is_set or self.clean_up_timer_remaining.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.clean_up_timer_remaining.get_name_leafdata())
                        if (self.client_connection_status.is_set or self.client_connection_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_connection_status.get_name_leafdata())
                        if (self.client_initialization_synchronization_pending.is_set or self.client_initialization_synchronization_pending.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_initialization_synchronization_pending.get_name_leafdata())
                        if (self.client_synchronization_end_of_download_pending.is_set or self.client_synchronization_end_of_download_pending.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_synchronization_end_of_download_pending.get_name_leafdata())
                        if (self.component.is_set or self.component.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.component.get_name_leafdata())
                        if (self.down_time_stamp.is_set or self.down_time_stamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.down_time_stamp.get_name_leafdata())
                        if (self.up_time_stamp.is_set or self.up_time_stamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.up_time_stamp.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "clean-up-timer-remaining" or name == "client-connection-status" or name == "client-initialization-synchronization-pending" or name == "client-synchronization-end-of-download-pending" or name == "component" or name == "down-time-stamp" or name == "up-time-stamp"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "clean-up-timer-remaining"):
                            self.clean_up_timer_remaining = value
                            self.clean_up_timer_remaining.value_namespace = name_space
                            self.clean_up_timer_remaining.value_namespace_prefix = name_space_prefix
                        if(value_path == "client-connection-status"):
                            self.client_connection_status = value
                            self.client_connection_status.value_namespace = name_space
                            self.client_connection_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "client-initialization-synchronization-pending"):
                            self.client_initialization_synchronization_pending = value
                            self.client_initialization_synchronization_pending.value_namespace = name_space
                            self.client_initialization_synchronization_pending.value_namespace_prefix = name_space_prefix
                        if(value_path == "client-synchronization-end-of-download-pending"):
                            self.client_synchronization_end_of_download_pending = value
                            self.client_synchronization_end_of_download_pending.value_namespace = name_space
                            self.client_synchronization_end_of_download_pending.value_namespace_prefix = name_space_prefix
                        if(value_path == "component"):
                            self.component = value
                            self.component.value_namespace = name_space
                            self.component.value_namespace_prefix = name_space_prefix
                        if(value_path == "down-time-stamp"):
                            self.down_time_stamp = value
                            self.down_time_stamp.value_namespace = name_space
                            self.down_time_stamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "up-time-stamp"):
                            self.up_time_stamp = value
                            self.up_time_stamp.value_namespace = name_space
                            self.up_time_stamp.value_namespace_prefix = name_space_prefix


                class OpaqueMemoryStatus(Entity):
                    """
                    Opaque memory Stats
                    
                    .. attribute:: component
                    
                    	Component
                    	**type**\:   :py:class:`SergShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowComp>`
                    
                    .. attribute:: opaque_data_size
                    
                    	Current Opaque Data Size for each component
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opaque_high_size
                    
                    	High Watermark of Opaque Data Size for each component
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opaque_size
                    
                    	Current Opaque Memory Size for each component
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_count
                    
                    	Session count for each component
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus, self).__init__()

                        self.yang_name = "opaque-memory-status"
                        self.yang_parent_name = "stats-global"

                        self.component = YLeaf(YType.enumeration, "component")

                        self.opaque_data_size = YLeaf(YType.uint32, "opaque-data-size")

                        self.opaque_high_size = YLeaf(YType.uint32, "opaque-high-size")

                        self.opaque_size = YLeaf(YType.uint32, "opaque-size")

                        self.session_count = YLeaf(YType.uint32, "session-count")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("component",
                                        "opaque_data_size",
                                        "opaque_high_size",
                                        "opaque_size",
                                        "session_count") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.component.is_set or
                            self.opaque_data_size.is_set or
                            self.opaque_high_size.is_set or
                            self.opaque_size.is_set or
                            self.session_count.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.component.yfilter != YFilter.not_set or
                            self.opaque_data_size.yfilter != YFilter.not_set or
                            self.opaque_high_size.yfilter != YFilter.not_set or
                            self.opaque_size.yfilter != YFilter.not_set or
                            self.session_count.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "opaque-memory-status" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.component.is_set or self.component.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.component.get_name_leafdata())
                        if (self.opaque_data_size.is_set or self.opaque_data_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.opaque_data_size.get_name_leafdata())
                        if (self.opaque_high_size.is_set or self.opaque_high_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.opaque_high_size.get_name_leafdata())
                        if (self.opaque_size.is_set or self.opaque_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.opaque_size.get_name_leafdata())
                        if (self.session_count.is_set or self.session_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "component" or name == "opaque-data-size" or name == "opaque-high-size" or name == "opaque-size" or name == "session-count"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "component"):
                            self.component = value
                            self.component.value_namespace = name_space
                            self.component.value_namespace_prefix = name_space_prefix
                        if(value_path == "opaque-data-size"):
                            self.opaque_data_size = value
                            self.opaque_data_size.value_namespace = name_space
                            self.opaque_data_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "opaque-high-size"):
                            self.opaque_high_size = value
                            self.opaque_high_size.value_namespace = name_space
                            self.opaque_high_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "opaque-size"):
                            self.opaque_size = value
                            self.opaque_size.value_namespace = name_space
                            self.opaque_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-count"):
                            self.session_count = value
                            self.session_count.value_namespace = name_space
                            self.session_count.value_namespace_prefix = name_space_prefix


                class TxListOverTcpStatus(Entity):
                    """
                    TCP TxList Statistics
                    
                    .. attribute:: accept_count
                    
                    	Socket Accept Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_socket_count
                    
                    	Active Socket Count
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: blocked_connect_count
                    
                    	Blocked Socket Connect Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: buffer_cache_hit
                    
                    	Buffer Cache Hit Count
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: buffer_cache_miss
                    
                    	Buffer Cache Miss Count
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: buffer_freed_count
                    
                    	Buffer Free Count
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: buffer_full_occurence_count
                    
                    	Buffer Full on Write Occurence Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes_received
                    
                    	Bytes Received Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes Sent Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: connect_count
                    
                    	Socket Connect Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connect_retry_count
                    
                    	Socket Connect Retry Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_received_message_size
                    
                    	Maximum Size of Received Message
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_requested_buffer_size
                    
                    	Maximum Size of Requested Buffer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_sent_message_size
                    
                    	Maximum Size of Sent Message
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mem_move_bytes_count
                    
                    	Partial Message Memory Move Byte Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mem_move_message_count
                    
                    	Partial Message Memory Move Occurence Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: messages_received
                    
                    	Message Received Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: messages_sent
                    
                    	Message Sent Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_pause_count
                    
                    	Peer Pause Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_node_down_count
                    
                    	Remote Peer DisConnect Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: socket_read_count
                    
                    	Socket Read Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: socket_write_count
                    
                    	Socket Write Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus, self).__init__()

                        self.yang_name = "tx-list-over-tcp-status"
                        self.yang_parent_name = "stats-global"

                        self.accept_count = YLeaf(YType.uint32, "accept-count")

                        self.active_socket_count = YLeaf(YType.uint16, "active-socket-count")

                        self.blocked_connect_count = YLeaf(YType.uint32, "blocked-connect-count")

                        self.buffer_cache_hit = YLeaf(YType.uint16, "buffer-cache-hit")

                        self.buffer_cache_miss = YLeaf(YType.uint16, "buffer-cache-miss")

                        self.buffer_freed_count = YLeaf(YType.uint16, "buffer-freed-count")

                        self.buffer_full_occurence_count = YLeaf(YType.uint32, "buffer-full-occurence-count")

                        self.bytes_received = YLeaf(YType.uint32, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint32, "bytes-sent")

                        self.connect_count = YLeaf(YType.uint32, "connect-count")

                        self.connect_retry_count = YLeaf(YType.uint32, "connect-retry-count")

                        self.maximum_received_message_size = YLeaf(YType.uint32, "maximum-received-message-size")

                        self.maximum_requested_buffer_size = YLeaf(YType.uint32, "maximum-requested-buffer-size")

                        self.maximum_sent_message_size = YLeaf(YType.uint32, "maximum-sent-message-size")

                        self.mem_move_bytes_count = YLeaf(YType.uint32, "mem-move-bytes-count")

                        self.mem_move_message_count = YLeaf(YType.uint32, "mem-move-message-count")

                        self.messages_received = YLeaf(YType.uint32, "messages-received")

                        self.messages_sent = YLeaf(YType.uint32, "messages-sent")

                        self.peer_pause_count = YLeaf(YType.uint32, "peer-pause-count")

                        self.remote_node_down_count = YLeaf(YType.uint32, "remote-node-down-count")

                        self.socket_read_count = YLeaf(YType.uint32, "socket-read-count")

                        self.socket_write_count = YLeaf(YType.uint32, "socket-write-count")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accept_count",
                                        "active_socket_count",
                                        "blocked_connect_count",
                                        "buffer_cache_hit",
                                        "buffer_cache_miss",
                                        "buffer_freed_count",
                                        "buffer_full_occurence_count",
                                        "bytes_received",
                                        "bytes_sent",
                                        "connect_count",
                                        "connect_retry_count",
                                        "maximum_received_message_size",
                                        "maximum_requested_buffer_size",
                                        "maximum_sent_message_size",
                                        "mem_move_bytes_count",
                                        "mem_move_message_count",
                                        "messages_received",
                                        "messages_sent",
                                        "peer_pause_count",
                                        "remote_node_down_count",
                                        "socket_read_count",
                                        "socket_write_count") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accept_count.is_set or
                            self.active_socket_count.is_set or
                            self.blocked_connect_count.is_set or
                            self.buffer_cache_hit.is_set or
                            self.buffer_cache_miss.is_set or
                            self.buffer_freed_count.is_set or
                            self.buffer_full_occurence_count.is_set or
                            self.bytes_received.is_set or
                            self.bytes_sent.is_set or
                            self.connect_count.is_set or
                            self.connect_retry_count.is_set or
                            self.maximum_received_message_size.is_set or
                            self.maximum_requested_buffer_size.is_set or
                            self.maximum_sent_message_size.is_set or
                            self.mem_move_bytes_count.is_set or
                            self.mem_move_message_count.is_set or
                            self.messages_received.is_set or
                            self.messages_sent.is_set or
                            self.peer_pause_count.is_set or
                            self.remote_node_down_count.is_set or
                            self.socket_read_count.is_set or
                            self.socket_write_count.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accept_count.yfilter != YFilter.not_set or
                            self.active_socket_count.yfilter != YFilter.not_set or
                            self.blocked_connect_count.yfilter != YFilter.not_set or
                            self.buffer_cache_hit.yfilter != YFilter.not_set or
                            self.buffer_cache_miss.yfilter != YFilter.not_set or
                            self.buffer_freed_count.yfilter != YFilter.not_set or
                            self.buffer_full_occurence_count.yfilter != YFilter.not_set or
                            self.bytes_received.yfilter != YFilter.not_set or
                            self.bytes_sent.yfilter != YFilter.not_set or
                            self.connect_count.yfilter != YFilter.not_set or
                            self.connect_retry_count.yfilter != YFilter.not_set or
                            self.maximum_received_message_size.yfilter != YFilter.not_set or
                            self.maximum_requested_buffer_size.yfilter != YFilter.not_set or
                            self.maximum_sent_message_size.yfilter != YFilter.not_set or
                            self.mem_move_bytes_count.yfilter != YFilter.not_set or
                            self.mem_move_message_count.yfilter != YFilter.not_set or
                            self.messages_received.yfilter != YFilter.not_set or
                            self.messages_sent.yfilter != YFilter.not_set or
                            self.peer_pause_count.yfilter != YFilter.not_set or
                            self.remote_node_down_count.yfilter != YFilter.not_set or
                            self.socket_read_count.yfilter != YFilter.not_set or
                            self.socket_write_count.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tx-list-over-tcp-status" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accept_count.is_set or self.accept_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accept_count.get_name_leafdata())
                        if (self.active_socket_count.is_set or self.active_socket_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_socket_count.get_name_leafdata())
                        if (self.blocked_connect_count.is_set or self.blocked_connect_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.blocked_connect_count.get_name_leafdata())
                        if (self.buffer_cache_hit.is_set or self.buffer_cache_hit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.buffer_cache_hit.get_name_leafdata())
                        if (self.buffer_cache_miss.is_set or self.buffer_cache_miss.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.buffer_cache_miss.get_name_leafdata())
                        if (self.buffer_freed_count.is_set or self.buffer_freed_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.buffer_freed_count.get_name_leafdata())
                        if (self.buffer_full_occurence_count.is_set or self.buffer_full_occurence_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.buffer_full_occurence_count.get_name_leafdata())
                        if (self.bytes_received.is_set or self.bytes_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_received.get_name_leafdata())
                        if (self.bytes_sent.is_set or self.bytes_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_sent.get_name_leafdata())
                        if (self.connect_count.is_set or self.connect_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.connect_count.get_name_leafdata())
                        if (self.connect_retry_count.is_set or self.connect_retry_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.connect_retry_count.get_name_leafdata())
                        if (self.maximum_received_message_size.is_set or self.maximum_received_message_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum_received_message_size.get_name_leafdata())
                        if (self.maximum_requested_buffer_size.is_set or self.maximum_requested_buffer_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum_requested_buffer_size.get_name_leafdata())
                        if (self.maximum_sent_message_size.is_set or self.maximum_sent_message_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum_sent_message_size.get_name_leafdata())
                        if (self.mem_move_bytes_count.is_set or self.mem_move_bytes_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mem_move_bytes_count.get_name_leafdata())
                        if (self.mem_move_message_count.is_set or self.mem_move_message_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mem_move_message_count.get_name_leafdata())
                        if (self.messages_received.is_set or self.messages_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.messages_received.get_name_leafdata())
                        if (self.messages_sent.is_set or self.messages_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.messages_sent.get_name_leafdata())
                        if (self.peer_pause_count.is_set or self.peer_pause_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_pause_count.get_name_leafdata())
                        if (self.remote_node_down_count.is_set or self.remote_node_down_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_node_down_count.get_name_leafdata())
                        if (self.socket_read_count.is_set or self.socket_read_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.socket_read_count.get_name_leafdata())
                        if (self.socket_write_count.is_set or self.socket_write_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.socket_write_count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accept-count" or name == "active-socket-count" or name == "blocked-connect-count" or name == "buffer-cache-hit" or name == "buffer-cache-miss" or name == "buffer-freed-count" or name == "buffer-full-occurence-count" or name == "bytes-received" or name == "bytes-sent" or name == "connect-count" or name == "connect-retry-count" or name == "maximum-received-message-size" or name == "maximum-requested-buffer-size" or name == "maximum-sent-message-size" or name == "mem-move-bytes-count" or name == "mem-move-message-count" or name == "messages-received" or name == "messages-sent" or name == "peer-pause-count" or name == "remote-node-down-count" or name == "socket-read-count" or name == "socket-write-count"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accept-count"):
                            self.accept_count = value
                            self.accept_count.value_namespace = name_space
                            self.accept_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "active-socket-count"):
                            self.active_socket_count = value
                            self.active_socket_count.value_namespace = name_space
                            self.active_socket_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "blocked-connect-count"):
                            self.blocked_connect_count = value
                            self.blocked_connect_count.value_namespace = name_space
                            self.blocked_connect_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "buffer-cache-hit"):
                            self.buffer_cache_hit = value
                            self.buffer_cache_hit.value_namespace = name_space
                            self.buffer_cache_hit.value_namespace_prefix = name_space_prefix
                        if(value_path == "buffer-cache-miss"):
                            self.buffer_cache_miss = value
                            self.buffer_cache_miss.value_namespace = name_space
                            self.buffer_cache_miss.value_namespace_prefix = name_space_prefix
                        if(value_path == "buffer-freed-count"):
                            self.buffer_freed_count = value
                            self.buffer_freed_count.value_namespace = name_space
                            self.buffer_freed_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "buffer-full-occurence-count"):
                            self.buffer_full_occurence_count = value
                            self.buffer_full_occurence_count.value_namespace = name_space
                            self.buffer_full_occurence_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-received"):
                            self.bytes_received = value
                            self.bytes_received.value_namespace = name_space
                            self.bytes_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-sent"):
                            self.bytes_sent = value
                            self.bytes_sent.value_namespace = name_space
                            self.bytes_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "connect-count"):
                            self.connect_count = value
                            self.connect_count.value_namespace = name_space
                            self.connect_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "connect-retry-count"):
                            self.connect_retry_count = value
                            self.connect_retry_count.value_namespace = name_space
                            self.connect_retry_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "maximum-received-message-size"):
                            self.maximum_received_message_size = value
                            self.maximum_received_message_size.value_namespace = name_space
                            self.maximum_received_message_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "maximum-requested-buffer-size"):
                            self.maximum_requested_buffer_size = value
                            self.maximum_requested_buffer_size.value_namespace = name_space
                            self.maximum_requested_buffer_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "maximum-sent-message-size"):
                            self.maximum_sent_message_size = value
                            self.maximum_sent_message_size.value_namespace = name_space
                            self.maximum_sent_message_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "mem-move-bytes-count"):
                            self.mem_move_bytes_count = value
                            self.mem_move_bytes_count.value_namespace = name_space
                            self.mem_move_bytes_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "mem-move-message-count"):
                            self.mem_move_message_count = value
                            self.mem_move_message_count.value_namespace = name_space
                            self.mem_move_message_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "messages-received"):
                            self.messages_received = value
                            self.messages_received.value_namespace = name_space
                            self.messages_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "messages-sent"):
                            self.messages_sent = value
                            self.messages_sent.value_namespace = name_space
                            self.messages_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-pause-count"):
                            self.peer_pause_count = value
                            self.peer_pause_count.value_namespace = name_space
                            self.peer_pause_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-node-down-count"):
                            self.remote_node_down_count = value
                            self.remote_node_down_count.value_namespace = name_space
                            self.remote_node_down_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "socket-read-count"):
                            self.socket_read_count = value
                            self.socket_read_count.value_namespace = name_space
                            self.socket_read_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "socket-write-count"):
                            self.socket_write_count = value
                            self.socket_write_count.value_namespace = name_space
                            self.socket_write_count.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.client_status:
                        if (c.has_data()):
                            return True
                    for c in self.opaque_memory_status:
                        if (c.has_data()):
                            return True
                    for c in self.tx_list_over_tcp_status:
                        if (c.has_data()):
                            return True
                    return (
                        self.client_init_sync_time_stamp.is_set or
                        self.peer_action_timer.is_set or
                        self.peer_init_sync_time_stamp.is_set or
                        self.redundancy_role.is_set or
                        self.restart_client_sync_in_progress.is_set or
                        self.restart_peer_sync_in_progress.is_set or
                        self.retry_timer_remaining.is_set or
                        self.source_interface_ipv4_address.is_set or
                        self.source_interface_ipv6_address.is_set or
                        self.source_interface_name.is_set or
                        self.sync_in_progress.is_set or
                        self.tx_list_client_connection_down.is_set or
                        self.tx_list_client_connection_up.is_set or
                        self.tx_list_client_de_registration_invalid.is_set or
                        self.tx_list_client_message_call_back.is_set or
                        self.tx_list_client_peer_done.is_set or
                        self.tx_list_client_receive_command_invalid.is_set or
                        self.tx_list_client_receive_command_valid.is_set or
                        self.tx_list_client_receive_invalid.is_set or
                        self.tx_list_client_receive_session_session_invalid.is_set or
                        self.tx_list_client_receive_session_sessionvalid.is_set or
                        self.tx_list_client_receive_valid.is_set or
                        self.tx_list_client_registration_invalid.is_set or
                        self.tx_list_peer_cmd_connection_down_not_ok.is_set or
                        self.tx_list_peer_cmd_connection_up_not_ok.is_set or
                        self.tx_list_peer_de_registration_invalid.is_set or
                        self.tx_list_peer_done.is_set or
                        self.tx_list_peer_message_call_back_invalid.is_set or
                        self.tx_list_peer_message_call_back_valid.is_set or
                        self.tx_list_peer_registration_invalid.is_set or
                        self.tx_list_peer_session_connection_down_not_ok.is_set or
                        self.tx_list_peer_session_connection_up_not_ok.is_set or
                        self.tx_list_peer_timer_handler.is_set or
                        self.vrf_name.is_set or
                        (self.intf_status_statistics is not None and self.intf_status_statistics.has_data()) or
                        (self.tx_list_statistics is not None and self.tx_list_statistics.has_data()))

                def has_operation(self):
                    for c in self.client_status:
                        if (c.has_operation()):
                            return True
                    for c in self.opaque_memory_status:
                        if (c.has_operation()):
                            return True
                    for c in self.tx_list_over_tcp_status:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.client_init_sync_time_stamp.yfilter != YFilter.not_set or
                        self.peer_action_timer.yfilter != YFilter.not_set or
                        self.peer_init_sync_time_stamp.yfilter != YFilter.not_set or
                        self.redundancy_role.yfilter != YFilter.not_set or
                        self.restart_client_sync_in_progress.yfilter != YFilter.not_set or
                        self.restart_peer_sync_in_progress.yfilter != YFilter.not_set or
                        self.retry_timer_remaining.yfilter != YFilter.not_set or
                        self.source_interface_ipv4_address.yfilter != YFilter.not_set or
                        self.source_interface_ipv6_address.yfilter != YFilter.not_set or
                        self.source_interface_name.yfilter != YFilter.not_set or
                        self.sync_in_progress.yfilter != YFilter.not_set or
                        self.tx_list_client_connection_down.yfilter != YFilter.not_set or
                        self.tx_list_client_connection_up.yfilter != YFilter.not_set or
                        self.tx_list_client_de_registration_invalid.yfilter != YFilter.not_set or
                        self.tx_list_client_message_call_back.yfilter != YFilter.not_set or
                        self.tx_list_client_peer_done.yfilter != YFilter.not_set or
                        self.tx_list_client_receive_command_invalid.yfilter != YFilter.not_set or
                        self.tx_list_client_receive_command_valid.yfilter != YFilter.not_set or
                        self.tx_list_client_receive_invalid.yfilter != YFilter.not_set or
                        self.tx_list_client_receive_session_session_invalid.yfilter != YFilter.not_set or
                        self.tx_list_client_receive_session_sessionvalid.yfilter != YFilter.not_set or
                        self.tx_list_client_receive_valid.yfilter != YFilter.not_set or
                        self.tx_list_client_registration_invalid.yfilter != YFilter.not_set or
                        self.tx_list_peer_cmd_connection_down_not_ok.yfilter != YFilter.not_set or
                        self.tx_list_peer_cmd_connection_up_not_ok.yfilter != YFilter.not_set or
                        self.tx_list_peer_de_registration_invalid.yfilter != YFilter.not_set or
                        self.tx_list_peer_done.yfilter != YFilter.not_set or
                        self.tx_list_peer_message_call_back_invalid.yfilter != YFilter.not_set or
                        self.tx_list_peer_message_call_back_valid.yfilter != YFilter.not_set or
                        self.tx_list_peer_registration_invalid.yfilter != YFilter.not_set or
                        self.tx_list_peer_session_connection_down_not_ok.yfilter != YFilter.not_set or
                        self.tx_list_peer_session_connection_up_not_ok.yfilter != YFilter.not_set or
                        self.tx_list_peer_timer_handler.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        (self.intf_status_statistics is not None and self.intf_status_statistics.has_operation()) or
                        (self.tx_list_statistics is not None and self.tx_list_statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "stats-global" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.client_init_sync_time_stamp.is_set or self.client_init_sync_time_stamp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.client_init_sync_time_stamp.get_name_leafdata())
                    if (self.peer_action_timer.is_set or self.peer_action_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_action_timer.get_name_leafdata())
                    if (self.peer_init_sync_time_stamp.is_set or self.peer_init_sync_time_stamp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_init_sync_time_stamp.get_name_leafdata())
                    if (self.redundancy_role.is_set or self.redundancy_role.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redundancy_role.get_name_leafdata())
                    if (self.restart_client_sync_in_progress.is_set or self.restart_client_sync_in_progress.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.restart_client_sync_in_progress.get_name_leafdata())
                    if (self.restart_peer_sync_in_progress.is_set or self.restart_peer_sync_in_progress.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.restart_peer_sync_in_progress.get_name_leafdata())
                    if (self.retry_timer_remaining.is_set or self.retry_timer_remaining.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.retry_timer_remaining.get_name_leafdata())
                    if (self.source_interface_ipv4_address.is_set or self.source_interface_ipv4_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_interface_ipv4_address.get_name_leafdata())
                    if (self.source_interface_ipv6_address.is_set or self.source_interface_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_interface_ipv6_address.get_name_leafdata())
                    if (self.source_interface_name.is_set or self.source_interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_interface_name.get_name_leafdata())
                    if (self.sync_in_progress.is_set or self.sync_in_progress.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sync_in_progress.get_name_leafdata())
                    if (self.tx_list_client_connection_down.is_set or self.tx_list_client_connection_down.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_connection_down.get_name_leafdata())
                    if (self.tx_list_client_connection_up.is_set or self.tx_list_client_connection_up.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_connection_up.get_name_leafdata())
                    if (self.tx_list_client_de_registration_invalid.is_set or self.tx_list_client_de_registration_invalid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_de_registration_invalid.get_name_leafdata())
                    if (self.tx_list_client_message_call_back.is_set or self.tx_list_client_message_call_back.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_message_call_back.get_name_leafdata())
                    if (self.tx_list_client_peer_done.is_set or self.tx_list_client_peer_done.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_peer_done.get_name_leafdata())
                    if (self.tx_list_client_receive_command_invalid.is_set or self.tx_list_client_receive_command_invalid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_receive_command_invalid.get_name_leafdata())
                    if (self.tx_list_client_receive_command_valid.is_set or self.tx_list_client_receive_command_valid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_receive_command_valid.get_name_leafdata())
                    if (self.tx_list_client_receive_invalid.is_set or self.tx_list_client_receive_invalid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_receive_invalid.get_name_leafdata())
                    if (self.tx_list_client_receive_session_session_invalid.is_set or self.tx_list_client_receive_session_session_invalid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_receive_session_session_invalid.get_name_leafdata())
                    if (self.tx_list_client_receive_session_sessionvalid.is_set or self.tx_list_client_receive_session_sessionvalid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_receive_session_sessionvalid.get_name_leafdata())
                    if (self.tx_list_client_receive_valid.is_set or self.tx_list_client_receive_valid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_receive_valid.get_name_leafdata())
                    if (self.tx_list_client_registration_invalid.is_set or self.tx_list_client_registration_invalid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_client_registration_invalid.get_name_leafdata())
                    if (self.tx_list_peer_cmd_connection_down_not_ok.is_set or self.tx_list_peer_cmd_connection_down_not_ok.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_peer_cmd_connection_down_not_ok.get_name_leafdata())
                    if (self.tx_list_peer_cmd_connection_up_not_ok.is_set or self.tx_list_peer_cmd_connection_up_not_ok.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_peer_cmd_connection_up_not_ok.get_name_leafdata())
                    if (self.tx_list_peer_de_registration_invalid.is_set or self.tx_list_peer_de_registration_invalid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_peer_de_registration_invalid.get_name_leafdata())
                    if (self.tx_list_peer_done.is_set or self.tx_list_peer_done.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_peer_done.get_name_leafdata())
                    if (self.tx_list_peer_message_call_back_invalid.is_set or self.tx_list_peer_message_call_back_invalid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_peer_message_call_back_invalid.get_name_leafdata())
                    if (self.tx_list_peer_message_call_back_valid.is_set or self.tx_list_peer_message_call_back_valid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_peer_message_call_back_valid.get_name_leafdata())
                    if (self.tx_list_peer_registration_invalid.is_set or self.tx_list_peer_registration_invalid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_peer_registration_invalid.get_name_leafdata())
                    if (self.tx_list_peer_session_connection_down_not_ok.is_set or self.tx_list_peer_session_connection_down_not_ok.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_peer_session_connection_down_not_ok.get_name_leafdata())
                    if (self.tx_list_peer_session_connection_up_not_ok.is_set or self.tx_list_peer_session_connection_up_not_ok.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_peer_session_connection_up_not_ok.get_name_leafdata())
                    if (self.tx_list_peer_timer_handler.is_set or self.tx_list_peer_timer_handler.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_list_peer_timer_handler.get_name_leafdata())
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "client-status"):
                        for c in self.client_status:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.client_status.append(c)
                        return c

                    if (child_yang_name == "intf-status-statistics"):
                        if (self.intf_status_statistics is None):
                            self.intf_status_statistics = SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics()
                            self.intf_status_statistics.parent = self
                            self._children_name_map["intf_status_statistics"] = "intf-status-statistics"
                        return self.intf_status_statistics

                    if (child_yang_name == "opaque-memory-status"):
                        for c in self.opaque_memory_status:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.opaque_memory_status.append(c)
                        return c

                    if (child_yang_name == "tx-list-over-tcp-status"):
                        for c in self.tx_list_over_tcp_status:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.tx_list_over_tcp_status.append(c)
                        return c

                    if (child_yang_name == "tx-list-statistics"):
                        if (self.tx_list_statistics is None):
                            self.tx_list_statistics = SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics()
                            self.tx_list_statistics.parent = self
                            self._children_name_map["tx_list_statistics"] = "tx-list-statistics"
                        return self.tx_list_statistics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "client-status" or name == "intf-status-statistics" or name == "opaque-memory-status" or name == "tx-list-over-tcp-status" or name == "tx-list-statistics" or name == "client-init-sync-time-stamp" or name == "peer-action-timer" or name == "peer-init-sync-time-stamp" or name == "redundancy-role" or name == "restart-client-sync-in-progress" or name == "restart-peer-sync-in-progress" or name == "retry-timer-remaining" or name == "source-interface-ipv4-address" or name == "source-interface-ipv6-address" or name == "source-interface-name" or name == "sync-in-progress" or name == "tx-list-client-connection-down" or name == "tx-list-client-connection-up" or name == "tx-list-client-de-registration-invalid" or name == "tx-list-client-message-call-back" or name == "tx-list-client-peer-done" or name == "tx-list-client-receive-command-invalid" or name == "tx-list-client-receive-command-valid" or name == "tx-list-client-receive-invalid" or name == "tx-list-client-receive-session-session-invalid" or name == "tx-list-client-receive-session-sessionvalid" or name == "tx-list-client-receive-valid" or name == "tx-list-client-registration-invalid" or name == "tx-list-peer-cmd-connection-down-not-ok" or name == "tx-list-peer-cmd-connection-up-not-ok" or name == "tx-list-peer-de-registration-invalid" or name == "tx-list-peer-done" or name == "tx-list-peer-message-call-back-invalid" or name == "tx-list-peer-message-call-back-valid" or name == "tx-list-peer-registration-invalid" or name == "tx-list-peer-session-connection-down-not-ok" or name == "tx-list-peer-session-connection-up-not-ok" or name == "tx-list-peer-timer-handler" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "client-init-sync-time-stamp"):
                        self.client_init_sync_time_stamp = value
                        self.client_init_sync_time_stamp.value_namespace = name_space
                        self.client_init_sync_time_stamp.value_namespace_prefix = name_space_prefix
                    if(value_path == "peer-action-timer"):
                        self.peer_action_timer = value
                        self.peer_action_timer.value_namespace = name_space
                        self.peer_action_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "peer-init-sync-time-stamp"):
                        self.peer_init_sync_time_stamp = value
                        self.peer_init_sync_time_stamp.value_namespace = name_space
                        self.peer_init_sync_time_stamp.value_namespace_prefix = name_space_prefix
                    if(value_path == "redundancy-role"):
                        self.redundancy_role = value
                        self.redundancy_role.value_namespace = name_space
                        self.redundancy_role.value_namespace_prefix = name_space_prefix
                    if(value_path == "restart-client-sync-in-progress"):
                        self.restart_client_sync_in_progress = value
                        self.restart_client_sync_in_progress.value_namespace = name_space
                        self.restart_client_sync_in_progress.value_namespace_prefix = name_space_prefix
                    if(value_path == "restart-peer-sync-in-progress"):
                        self.restart_peer_sync_in_progress = value
                        self.restart_peer_sync_in_progress.value_namespace = name_space
                        self.restart_peer_sync_in_progress.value_namespace_prefix = name_space_prefix
                    if(value_path == "retry-timer-remaining"):
                        self.retry_timer_remaining = value
                        self.retry_timer_remaining.value_namespace = name_space
                        self.retry_timer_remaining.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-interface-ipv4-address"):
                        self.source_interface_ipv4_address = value
                        self.source_interface_ipv4_address.value_namespace = name_space
                        self.source_interface_ipv4_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-interface-ipv6-address"):
                        self.source_interface_ipv6_address = value
                        self.source_interface_ipv6_address.value_namespace = name_space
                        self.source_interface_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-interface-name"):
                        self.source_interface_name = value
                        self.source_interface_name.value_namespace = name_space
                        self.source_interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "sync-in-progress"):
                        self.sync_in_progress = value
                        self.sync_in_progress.value_namespace = name_space
                        self.sync_in_progress.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-connection-down"):
                        self.tx_list_client_connection_down = value
                        self.tx_list_client_connection_down.value_namespace = name_space
                        self.tx_list_client_connection_down.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-connection-up"):
                        self.tx_list_client_connection_up = value
                        self.tx_list_client_connection_up.value_namespace = name_space
                        self.tx_list_client_connection_up.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-de-registration-invalid"):
                        self.tx_list_client_de_registration_invalid = value
                        self.tx_list_client_de_registration_invalid.value_namespace = name_space
                        self.tx_list_client_de_registration_invalid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-message-call-back"):
                        self.tx_list_client_message_call_back = value
                        self.tx_list_client_message_call_back.value_namespace = name_space
                        self.tx_list_client_message_call_back.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-peer-done"):
                        self.tx_list_client_peer_done = value
                        self.tx_list_client_peer_done.value_namespace = name_space
                        self.tx_list_client_peer_done.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-receive-command-invalid"):
                        self.tx_list_client_receive_command_invalid = value
                        self.tx_list_client_receive_command_invalid.value_namespace = name_space
                        self.tx_list_client_receive_command_invalid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-receive-command-valid"):
                        self.tx_list_client_receive_command_valid = value
                        self.tx_list_client_receive_command_valid.value_namespace = name_space
                        self.tx_list_client_receive_command_valid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-receive-invalid"):
                        self.tx_list_client_receive_invalid = value
                        self.tx_list_client_receive_invalid.value_namespace = name_space
                        self.tx_list_client_receive_invalid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-receive-session-session-invalid"):
                        self.tx_list_client_receive_session_session_invalid = value
                        self.tx_list_client_receive_session_session_invalid.value_namespace = name_space
                        self.tx_list_client_receive_session_session_invalid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-receive-session-sessionvalid"):
                        self.tx_list_client_receive_session_sessionvalid = value
                        self.tx_list_client_receive_session_sessionvalid.value_namespace = name_space
                        self.tx_list_client_receive_session_sessionvalid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-receive-valid"):
                        self.tx_list_client_receive_valid = value
                        self.tx_list_client_receive_valid.value_namespace = name_space
                        self.tx_list_client_receive_valid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-client-registration-invalid"):
                        self.tx_list_client_registration_invalid = value
                        self.tx_list_client_registration_invalid.value_namespace = name_space
                        self.tx_list_client_registration_invalid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-peer-cmd-connection-down-not-ok"):
                        self.tx_list_peer_cmd_connection_down_not_ok = value
                        self.tx_list_peer_cmd_connection_down_not_ok.value_namespace = name_space
                        self.tx_list_peer_cmd_connection_down_not_ok.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-peer-cmd-connection-up-not-ok"):
                        self.tx_list_peer_cmd_connection_up_not_ok = value
                        self.tx_list_peer_cmd_connection_up_not_ok.value_namespace = name_space
                        self.tx_list_peer_cmd_connection_up_not_ok.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-peer-de-registration-invalid"):
                        self.tx_list_peer_de_registration_invalid = value
                        self.tx_list_peer_de_registration_invalid.value_namespace = name_space
                        self.tx_list_peer_de_registration_invalid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-peer-done"):
                        self.tx_list_peer_done = value
                        self.tx_list_peer_done.value_namespace = name_space
                        self.tx_list_peer_done.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-peer-message-call-back-invalid"):
                        self.tx_list_peer_message_call_back_invalid = value
                        self.tx_list_peer_message_call_back_invalid.value_namespace = name_space
                        self.tx_list_peer_message_call_back_invalid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-peer-message-call-back-valid"):
                        self.tx_list_peer_message_call_back_valid = value
                        self.tx_list_peer_message_call_back_valid.value_namespace = name_space
                        self.tx_list_peer_message_call_back_valid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-peer-registration-invalid"):
                        self.tx_list_peer_registration_invalid = value
                        self.tx_list_peer_registration_invalid.value_namespace = name_space
                        self.tx_list_peer_registration_invalid.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-peer-session-connection-down-not-ok"):
                        self.tx_list_peer_session_connection_down_not_ok = value
                        self.tx_list_peer_session_connection_down_not_ok.value_namespace = name_space
                        self.tx_list_peer_session_connection_down_not_ok.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-peer-session-connection-up-not-ok"):
                        self.tx_list_peer_session_connection_up_not_ok = value
                        self.tx_list_peer_session_connection_up_not_ok.value_namespace = name_space
                        self.tx_list_peer_session_connection_up_not_ok.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-list-peer-timer-handler"):
                        self.tx_list_peer_timer_handler = value
                        self.tx_list_peer_timer_handler.value_namespace = name_space
                        self.tx_list_peer_timer_handler.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix


            class GroupSummaries(Entity):
                """
                Session data for a particular node
                
                .. attribute:: group_summary
                
                	Session redundancy agent group summary
                	**type**\: list of    :py:class:`GroupSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionRedundancyAgent.Nodes.Node.GroupSummaries, self).__init__()

                    self.yang_name = "group-summaries"
                    self.yang_parent_name = "node"

                    self.group_summary = YList(self)

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
                                super(SessionRedundancyAgent.Nodes.Node.GroupSummaries, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionRedundancyAgent.Nodes.Node.GroupSummaries, self).__setattr__(name, value)


                class GroupSummary(Entity):
                    """
                    Session redundancy agent group summary
                    
                    .. attribute:: group_id  <key>
                    
                    	GroupId
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: disabled
                    
                    	Disabled by Config
                    	**type**\:  bool
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_count
                    
                    	Interface Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: object_tracking_status
                    
                    	Object Tracking Status (Enabled/Disabled)
                    	**type**\:  bool
                    
                    .. attribute:: peer_ipv4_address
                    
                    	Peer IPv4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_ipv6_address
                    
                    	Peer IPv6 Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_status
                    
                    	Peer Status
                    	**type**\:   :py:class:`SergPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergPeerStatus>`
                    
                    .. attribute:: pending_add_session_count
                    
                    	Pending Session Count for Synchornization
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: preferred_role
                    
                    	Preferred Role
                    	**type**\:   :py:class:`SergShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRole>`
                    
                    .. attribute:: role
                    
                    	SERG Role
                    	**type**\:   :py:class:`SergShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRole>`
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slave_mode
                    
                    	Slave Mode
                    	**type**\:   :py:class:`SergShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveMode>`
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, self).__init__()

                        self.yang_name = "group-summary"
                        self.yang_parent_name = "group-summaries"

                        self.group_id = YLeaf(YType.str, "group-id")

                        self.disabled = YLeaf(YType.boolean, "disabled")

                        self.group_id_xr = YLeaf(YType.uint32, "group-id-xr")

                        self.interface_count = YLeaf(YType.uint32, "interface-count")

                        self.object_tracking_status = YLeaf(YType.boolean, "object-tracking-status")

                        self.peer_ipv4_address = YLeaf(YType.str, "peer-ipv4-address")

                        self.peer_ipv6_address = YLeaf(YType.str, "peer-ipv6-address")

                        self.peer_status = YLeaf(YType.enumeration, "peer-status")

                        self.pending_add_session_count = YLeaf(YType.uint32, "pending-add-session-count")

                        self.preferred_role = YLeaf(YType.enumeration, "preferred-role")

                        self.role = YLeaf(YType.enumeration, "role")

                        self.session_count = YLeaf(YType.uint32, "session-count")

                        self.slave_mode = YLeaf(YType.enumeration, "slave-mode")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("group_id",
                                        "disabled",
                                        "group_id_xr",
                                        "interface_count",
                                        "object_tracking_status",
                                        "peer_ipv4_address",
                                        "peer_ipv6_address",
                                        "peer_status",
                                        "pending_add_session_count",
                                        "preferred_role",
                                        "role",
                                        "session_count",
                                        "slave_mode") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.group_id.is_set or
                            self.disabled.is_set or
                            self.group_id_xr.is_set or
                            self.interface_count.is_set or
                            self.object_tracking_status.is_set or
                            self.peer_ipv4_address.is_set or
                            self.peer_ipv6_address.is_set or
                            self.peer_status.is_set or
                            self.pending_add_session_count.is_set or
                            self.preferred_role.is_set or
                            self.role.is_set or
                            self.session_count.is_set or
                            self.slave_mode.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.group_id.yfilter != YFilter.not_set or
                            self.disabled.yfilter != YFilter.not_set or
                            self.group_id_xr.yfilter != YFilter.not_set or
                            self.interface_count.yfilter != YFilter.not_set or
                            self.object_tracking_status.yfilter != YFilter.not_set or
                            self.peer_ipv4_address.yfilter != YFilter.not_set or
                            self.peer_ipv6_address.yfilter != YFilter.not_set or
                            self.peer_status.yfilter != YFilter.not_set or
                            self.pending_add_session_count.yfilter != YFilter.not_set or
                            self.preferred_role.yfilter != YFilter.not_set or
                            self.role.yfilter != YFilter.not_set or
                            self.session_count.yfilter != YFilter.not_set or
                            self.slave_mode.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "group-summary" + "[group-id='" + self.group_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_id.get_name_leafdata())
                        if (self.disabled.is_set or self.disabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.disabled.get_name_leafdata())
                        if (self.group_id_xr.is_set or self.group_id_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.group_id_xr.get_name_leafdata())
                        if (self.interface_count.is_set or self.interface_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_count.get_name_leafdata())
                        if (self.object_tracking_status.is_set or self.object_tracking_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_tracking_status.get_name_leafdata())
                        if (self.peer_ipv4_address.is_set or self.peer_ipv4_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_ipv4_address.get_name_leafdata())
                        if (self.peer_ipv6_address.is_set or self.peer_ipv6_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_ipv6_address.get_name_leafdata())
                        if (self.peer_status.is_set or self.peer_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_status.get_name_leafdata())
                        if (self.pending_add_session_count.is_set or self.pending_add_session_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pending_add_session_count.get_name_leafdata())
                        if (self.preferred_role.is_set or self.preferred_role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.preferred_role.get_name_leafdata())
                        if (self.role.is_set or self.role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.role.get_name_leafdata())
                        if (self.session_count.is_set or self.session_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_count.get_name_leafdata())
                        if (self.slave_mode.is_set or self.slave_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slave_mode.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "group-id" or name == "disabled" or name == "group-id-xr" or name == "interface-count" or name == "object-tracking-status" or name == "peer-ipv4-address" or name == "peer-ipv6-address" or name == "peer-status" or name == "pending-add-session-count" or name == "preferred-role" or name == "role" or name == "session-count" or name == "slave-mode"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "group-id"):
                            self.group_id = value
                            self.group_id.value_namespace = name_space
                            self.group_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "disabled"):
                            self.disabled = value
                            self.disabled.value_namespace = name_space
                            self.disabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "group-id-xr"):
                            self.group_id_xr = value
                            self.group_id_xr.value_namespace = name_space
                            self.group_id_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-count"):
                            self.interface_count = value
                            self.interface_count.value_namespace = name_space
                            self.interface_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "object-tracking-status"):
                            self.object_tracking_status = value
                            self.object_tracking_status.value_namespace = name_space
                            self.object_tracking_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-ipv4-address"):
                            self.peer_ipv4_address = value
                            self.peer_ipv4_address.value_namespace = name_space
                            self.peer_ipv4_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-ipv6-address"):
                            self.peer_ipv6_address = value
                            self.peer_ipv6_address.value_namespace = name_space
                            self.peer_ipv6_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-status"):
                            self.peer_status = value
                            self.peer_status.value_namespace = name_space
                            self.peer_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "pending-add-session-count"):
                            self.pending_add_session_count = value
                            self.pending_add_session_count.value_namespace = name_space
                            self.pending_add_session_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "preferred-role"):
                            self.preferred_role = value
                            self.preferred_role.value_namespace = name_space
                            self.preferred_role.value_namespace_prefix = name_space_prefix
                        if(value_path == "role"):
                            self.role = value
                            self.role.value_namespace = name_space
                            self.role.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-count"):
                            self.session_count = value
                            self.session_count.value_namespace = name_space
                            self.session_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "slave-mode"):
                            self.slave_mode = value
                            self.slave_mode.value_namespace = name_space
                            self.slave_mode.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.group_summary:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.group_summary:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "group-summaries" + path_buffer

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

                    if (child_yang_name == "group-summary"):
                        for c in self.group_summary:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.group_summary.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group-summary"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.client_ids is not None and self.client_ids.has_data()) or
                    (self.group_id_xr is not None and self.group_id_xr.has_data()) or
                    (self.group_ids is not None and self.group_ids.has_data()) or
                    (self.group_summaries is not None and self.group_summaries.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.memory is not None and self.memory.has_data()) or
                    (self.stats_global is not None and self.stats_global.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.client_ids is not None and self.client_ids.has_operation()) or
                    (self.group_id_xr is not None and self.group_id_xr.has_operation()) or
                    (self.group_ids is not None and self.group_ids.has_operation()) or
                    (self.group_summaries is not None and self.group_summaries.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.memory is not None and self.memory.has_operation()) or
                    (self.stats_global is not None and self.stats_global.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "client-ids"):
                    if (self.client_ids is None):
                        self.client_ids = SessionRedundancyAgent.Nodes.Node.ClientIds()
                        self.client_ids.parent = self
                        self._children_name_map["client_ids"] = "client-ids"
                    return self.client_ids

                if (child_yang_name == "group-id-xr"):
                    if (self.group_id_xr is None):
                        self.group_id_xr = SessionRedundancyAgent.Nodes.Node.GroupIdXr()
                        self.group_id_xr.parent = self
                        self._children_name_map["group_id_xr"] = "group-id-xr"
                    return self.group_id_xr

                if (child_yang_name == "group-ids"):
                    if (self.group_ids is None):
                        self.group_ids = SessionRedundancyAgent.Nodes.Node.GroupIds()
                        self.group_ids.parent = self
                        self._children_name_map["group_ids"] = "group-ids"
                    return self.group_ids

                if (child_yang_name == "group-summaries"):
                    if (self.group_summaries is None):
                        self.group_summaries = SessionRedundancyAgent.Nodes.Node.GroupSummaries()
                        self.group_summaries.parent = self
                        self._children_name_map["group_summaries"] = "group-summaries"
                    return self.group_summaries

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = SessionRedundancyAgent.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "memory"):
                    if (self.memory is None):
                        self.memory = SessionRedundancyAgent.Nodes.Node.Memory()
                        self.memory.parent = self
                        self._children_name_map["memory"] = "memory"
                    return self.memory

                if (child_yang_name == "stats-global"):
                    if (self.stats_global is None):
                        self.stats_global = SessionRedundancyAgent.Nodes.Node.StatsGlobal()
                        self.stats_global.parent = self
                        self._children_name_map["stats_global"] = "stats-global"
                    return self.stats_global

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "client-ids" or name == "group-id-xr" or name == "group-ids" or name == "group-summaries" or name == "interfaces" or name == "memory" or name == "stats-global" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent/%s" % self.get_segment_path()
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
                c = SessionRedundancyAgent.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent" + path_buffer

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
                self.nodes = SessionRedundancyAgent.Nodes()
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
        self._top_entity = SessionRedundancyAgent()
        return self._top_entity

