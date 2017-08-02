""" Cisco_IOS_XR_subscriber_srg_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-srg package operational data.

This module contains definitions
for the following management objects\:
  subscriber\-redundancy\-manager\: Subscriber Redundancy Manager
    information
  subscriber\-redundancy\-agent\: subscriber redundancy agent

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SrgPeerStatus(Enum):
    """
    SrgPeerStatus

    SRG Peer Status

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


class SrgShowComp(Enum):
    """
    SrgShowComp

    SRG Components

    .. data:: srga = 0

    	SRG Agent

    .. data:: dhcpv4 = 1

    	DHCPv4

    .. data:: dhcpv6 = 2

    	DHCPv6

    .. data:: pppoe = 3

    	PPPoE

    .. data:: ppp = 4

    	PPP

    .. data:: l2tp = 5

    	L2TP

    .. data:: iedge = 6

    	iEdge

    """

    srga = Enum.YLeaf(0, "srga")

    dhcpv4 = Enum.YLeaf(1, "dhcpv4")

    dhcpv6 = Enum.YLeaf(2, "dhcpv6")

    pppoe = Enum.YLeaf(3, "pppoe")

    ppp = Enum.YLeaf(4, "ppp")

    l2tp = Enum.YLeaf(5, "l2tp")

    iedge = Enum.YLeaf(6, "iedge")


class SrgShowImRole(Enum):
    """
    SrgShowImRole

    SRG Interface Management Role

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


class SrgShowRole(Enum):
    """
    SrgShowRole

    SRG Role

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


class SrgShowSessionError(Enum):
    """
    SrgShowSessionError

    SRG Session Error Operation

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


class SrgShowSessionOperation(Enum):
    """
    SrgShowSessionOperation

    SRG Session Operation

    .. data:: none = 0

    	No Operation

    .. data:: update = 1

    	SRG Session Update Operation

    .. data:: delete = 2

    	SRG Session Delete Operation

    .. data:: in_sync = 3

    	SRG Session In Sync

    """

    none = Enum.YLeaf(0, "none")

    update = Enum.YLeaf(1, "update")

    delete = Enum.YLeaf(2, "delete")

    in_sync = Enum.YLeaf(3, "in-sync")


class SrgShowSlaveMode(Enum):
    """
    SrgShowSlaveMode

    SRG Slave Mode

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


class SrgShowSoReason(Enum):
    """
    SrgShowSoReason

    Subscriber Redundancy Switchover Reason

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

    .. data:: srg_show_so_reason_max = 5

    	Unknown Switchover Reason

    """

    internal = Enum.YLeaf(0, "internal")

    admin = Enum.YLeaf(1, "admin")

    peer_up = Enum.YLeaf(2, "peer-up")

    peer_down = Enum.YLeaf(3, "peer-down")

    object_tracking_status_change = Enum.YLeaf(4, "object-tracking-status-change")

    srg_show_so_reason_max = Enum.YLeaf(5, "srg-show-so-reason-max")



class SubscriberRedundancyManager(Entity):
    """
    Subscriber Redundancy Manager information
    
    .. attribute:: groups
    
    	Subscriber Redundancy Manager group table
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Groups>`
    
    .. attribute:: interfaces
    
    	Subscriber Redundancy Manager interface table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Interfaces>`
    
    .. attribute:: summary
    
    	Subscriber redundancy manager summary
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Summary>`
    
    

    """

    _prefix = 'subscriber-srg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberRedundancyManager, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-redundancy-manager"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-srg-oper"

        self.groups = SubscriberRedundancyManager.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._children_yang_names.add("groups")

        self.interfaces = SubscriberRedundancyManager.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.summary = SubscriberRedundancyManager.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")


    class Groups(Entity):
        """
        Subscriber Redundancy Manager group table
        
        .. attribute:: group
        
        	Subscriber redundancy manager group
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Groups.Group>`
        
        

        """

        _prefix = 'subscriber-srg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberRedundancyManager.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "subscriber-redundancy-manager"

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
                        super(SubscriberRedundancyManager.Groups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubscriberRedundancyManager.Groups, self).__setattr__(name, value)


        class Group(Entity):
            """
            Subscriber redundancy manager group
            
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
            	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
            
            .. attribute:: role
            
            	SRG Role
            	**type**\:   :py:class:`SrgShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRole>`
            
            .. attribute:: slave_mode
            
            	Slave Mode
            	**type**\:   :py:class:`SrgShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveMode>`
            
            .. attribute:: virtual_mac_address
            
            	Virtual MAC Address
            	**type**\:  str
            
            .. attribute:: virtual_mac_address_disable
            
            	Virtual MAC Address Disable
            	**type**\:  bool
            
            

            """

            _prefix = 'subscriber-srg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberRedundancyManager.Groups.Group, self).__init__()

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

                self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                self.virtual_mac_address_disable = YLeaf(YType.boolean, "virtual-mac-address-disable")

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
                                "slave_mode",
                                "virtual_mac_address",
                                "virtual_mac_address_disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SubscriberRedundancyManager.Groups.Group, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SubscriberRedundancyManager.Groups.Group, self).__setattr__(name, value)

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
                    self.slave_mode.is_set or
                    self.virtual_mac_address.is_set or
                    self.virtual_mac_address_disable.is_set)

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
                    self.slave_mode.yfilter != YFilter.not_set or
                    self.virtual_mac_address.yfilter != YFilter.not_set or
                    self.virtual_mac_address_disable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "group" + "[group='" + self.group.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/groups/%s" % self.get_segment_path()
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
                if (self.virtual_mac_address.is_set or self.virtual_mac_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.virtual_mac_address.get_name_leafdata())
                if (self.virtual_mac_address_disable.is_set or self.virtual_mac_address_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.virtual_mac_address_disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "group" or name == "description" or name == "disabled" or name == "group-id" or name == "interface-count" or name == "node-name" or name == "object-tracking-status" or name == "peer-ipv4-address" or name == "peer-ipv6-address" or name == "preferred-role" or name == "role" or name == "slave-mode" or name == "virtual-mac-address" or name == "virtual-mac-address-disable"):
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
                if(value_path == "virtual-mac-address"):
                    self.virtual_mac_address = value
                    self.virtual_mac_address.value_namespace = name_space
                    self.virtual_mac_address.value_namespace_prefix = name_space_prefix
                if(value_path == "virtual-mac-address-disable"):
                    self.virtual_mac_address_disable = value
                    self.virtual_mac_address_disable.value_namespace = name_space
                    self.virtual_mac_address_disable.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/%s" % self.get_segment_path()
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
                c = SubscriberRedundancyManager.Groups.Group()
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
        Subscriber redundancy manager summary
        
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
        	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
        
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
        	**type**\:   :py:class:`SrgShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveMode>`
        
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

        _prefix = 'subscriber-srg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberRedundancyManager.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "subscriber-redundancy-manager"

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
                        super(SubscriberRedundancyManager.Summary, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubscriberRedundancyManager.Summary, self).__setattr__(name, value)

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
                path_buffer = "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/%s" % self.get_segment_path()
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


    class Interfaces(Entity):
        """
        Subscriber Redundancy Manager interface table
        
        .. attribute:: interface
        
        	Subscriber redundancy manager interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Interfaces.Interface>`
        
        

        """

        _prefix = 'subscriber-srg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberRedundancyManager.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "subscriber-redundancy-manager"

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
                        super(SubscriberRedundancyManager.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubscriberRedundancyManager.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            Subscriber redundancy manager interface
            
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
            
            	SRG Role
            	**type**\:   :py:class:`SrgShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRole>`
            
            

            """

            _prefix = 'subscriber-srg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberRedundancyManager.Interfaces.Interface, self).__init__()

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
                            super(SubscriberRedundancyManager.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SubscriberRedundancyManager.Interfaces.Interface, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/interfaces/%s" % self.get_segment_path()
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
                path_buffer = "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/%s" % self.get_segment_path()
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
                c = SubscriberRedundancyManager.Interfaces.Interface()
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
        path_buffer = "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager" + path_buffer

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
                self.groups = SubscriberRedundancyManager.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
            return self.groups

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = SubscriberRedundancyManager.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "summary"):
            if (self.summary is None):
                self.summary = SubscriberRedundancyManager.Summary()
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
        self._top_entity = SubscriberRedundancyManager()
        return self._top_entity

class SubscriberRedundancyAgent(Entity):
    """
    subscriber redundancy agent
    
    .. attribute:: nodes
    
    	List of nodes for which subscriber data is collected
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes>`
    
    

    """

    _prefix = 'subscriber-srg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberRedundancyAgent, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-redundancy-agent"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-srg-oper"

        self.nodes = SubscriberRedundancyAgent.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of nodes for which subscriber data is
        collected
        
        .. attribute:: node
        
        	Subscriber data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-srg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberRedundancyAgent.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "subscriber-redundancy-agent"

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
                        super(SubscriberRedundancyAgent.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubscriberRedundancyAgent.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Subscriber data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: group_id_xr
            
            	Data for particular subscriber group session
            	**type**\:   :py:class:`GroupIdXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr>`
            
            .. attribute:: group_ids
            
            	Data for particular subscriber group 
            	**type**\:   :py:class:`GroupIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIds>`
            
            .. attribute:: group_summaries
            
            	Subscriber data for a particular node
            	**type**\:   :py:class:`GroupSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupSummaries>`
            
            .. attribute:: interfaces
            
            	List of interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'subscriber-srg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberRedundancyAgent.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.group_id_xr = SubscriberRedundancyAgent.Nodes.Node.GroupIdXr()
                self.group_id_xr.parent = self
                self._children_name_map["group_id_xr"] = "group-id-xr"
                self._children_yang_names.add("group-id-xr")

                self.group_ids = SubscriberRedundancyAgent.Nodes.Node.GroupIds()
                self.group_ids.parent = self
                self._children_name_map["group_ids"] = "group-ids"
                self._children_yang_names.add("group-ids")

                self.group_summaries = SubscriberRedundancyAgent.Nodes.Node.GroupSummaries()
                self.group_summaries.parent = self
                self._children_name_map["group_summaries"] = "group-summaries"
                self._children_yang_names.add("group-summaries")

                self.interfaces = SubscriberRedundancyAgent.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

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
                            super(SubscriberRedundancyAgent.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SubscriberRedundancyAgent.Nodes.Node, self).__setattr__(name, value)


            class GroupIdXr(Entity):
                """
                Data for particular subscriber group session
                
                .. attribute:: group_id
                
                	Group id for subscriber group session
                	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr, self).__init__()

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
                                super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr, self).__setattr__(name, value)


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
                    
                    .. attribute:: inner_vlan
                    
                    	Inner VLAN Information
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    .. attribute:: l2tp_tunnel_id
                    
                    	L2TP Tunnel local ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: negative_acknowledgement_update_all
                    
                    	Negative Acknowledgement Update Flag is Set
                    	**type**\:  bool
                    
                    .. attribute:: outer_vlan
                    
                    	Outer VLAN Information
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pppoe_session_id
                    
                    	PPPoE Session ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: role_master
                    
                    	Master Role is Set
                    	**type**\:  bool
                    
                    .. attribute:: session_detailed_information
                    
                    	More Session Information
                    	**type**\: list of    :py:class:`SessionDetailedInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation>`
                    
                    .. attribute:: session_mac_address
                    
                    	Session MAC Address
                    	**type**\:  str
                    
                    .. attribute:: session_sync_error_information
                    
                    	Session Synchroniation Error Information
                    	**type**\: list of    :py:class:`SessionSyncErrorInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation>`
                    
                    .. attribute:: valid_mac_address
                    
                    	Holds a Valid MAC Address
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, self).__init__()

                        self.yang_name = "group-id"
                        self.yang_parent_name = "group-id-xr"

                        self.group_id = YLeaf(YType.str, "group-id")

                        self.group_id_xr = YLeaf(YType.uint32, "group-id-xr")

                        self.inner_vlan = YLeaf(YType.uint32, "inner-vlan")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.l2tp_tunnel_id = YLeaf(YType.uint32, "l2tp-tunnel-id")

                        self.negative_acknowledgement_update_all = YLeaf(YType.boolean, "negative-acknowledgement-update-all")

                        self.outer_vlan = YLeaf(YType.uint32, "outer-vlan")

                        self.pppoe_session_id = YLeaf(YType.uint16, "pppoe-session-id")

                        self.role_master = YLeaf(YType.boolean, "role-master")

                        self.session_mac_address = YLeaf(YType.str, "session-mac-address")

                        self.valid_mac_address = YLeaf(YType.boolean, "valid-mac-address")

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
                                        "inner_vlan",
                                        "interface_name",
                                        "l2tp_tunnel_id",
                                        "negative_acknowledgement_update_all",
                                        "outer_vlan",
                                        "pppoe_session_id",
                                        "role_master",
                                        "session_mac_address",
                                        "valid_mac_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId, self).__setattr__(name, value)


                    class SessionDetailedInformation(Entity):
                        """
                        More Session Information
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:   :py:class:`SrgShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowComp>`
                        
                        .. attribute:: marked_for_cleanup
                        
                        	Marked For Cleanup
                        	**type**\:  bool
                        
                        .. attribute:: marked_for_sweeping
                        
                        	Marked For Sweeping
                        	**type**\:  bool
                        
                        .. attribute:: operation_
                        
                        	Operation Code
                        	**type**\:   :py:class:`SrgShowSessionOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSessionOperation>`
                        
                        .. attribute:: tx_list_queue_fail
                        
                        	Tx List Queue Failed
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, self).__init__()

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
                                        super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation, self).__setattr__(name, value)

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
                        	**type**\:   :py:class:`SrgShowSessionError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSessionError>`
                        
                        .. attribute:: sync_error_count
                        
                        	No. of Errors occured during Synchronization
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, self).__init__()

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
                                        super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation, self).__setattr__(name, value)

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
                            self.inner_vlan.is_set or
                            self.interface_name.is_set or
                            self.l2tp_tunnel_id.is_set or
                            self.negative_acknowledgement_update_all.is_set or
                            self.outer_vlan.is_set or
                            self.pppoe_session_id.is_set or
                            self.role_master.is_set or
                            self.session_mac_address.is_set or
                            self.valid_mac_address.is_set)

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
                            self.inner_vlan.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.l2tp_tunnel_id.yfilter != YFilter.not_set or
                            self.negative_acknowledgement_update_all.yfilter != YFilter.not_set or
                            self.outer_vlan.yfilter != YFilter.not_set or
                            self.pppoe_session_id.yfilter != YFilter.not_set or
                            self.role_master.yfilter != YFilter.not_set or
                            self.session_mac_address.yfilter != YFilter.not_set or
                            self.valid_mac_address.yfilter != YFilter.not_set)

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
                        if (self.inner_vlan.is_set or self.inner_vlan.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inner_vlan.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.l2tp_tunnel_id.is_set or self.l2tp_tunnel_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.l2tp_tunnel_id.get_name_leafdata())
                        if (self.negative_acknowledgement_update_all.is_set or self.negative_acknowledgement_update_all.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.negative_acknowledgement_update_all.get_name_leafdata())
                        if (self.outer_vlan.is_set or self.outer_vlan.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.outer_vlan.get_name_leafdata())
                        if (self.pppoe_session_id.is_set or self.pppoe_session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pppoe_session_id.get_name_leafdata())
                        if (self.role_master.is_set or self.role_master.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.role_master.get_name_leafdata())
                        if (self.session_mac_address.is_set or self.session_mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_mac_address.get_name_leafdata())
                        if (self.valid_mac_address.is_set or self.valid_mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.valid_mac_address.get_name_leafdata())

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
                            c = SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation()
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
                            c = SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.session_sync_error_information.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "session-detailed-information" or name == "session-sync-error-information" or name == "group-id" or name == "group-id-xr" or name == "inner-vlan" or name == "interface-name" or name == "l2tp-tunnel-id" or name == "negative-acknowledgement-update-all" or name == "outer-vlan" or name == "pppoe-session-id" or name == "role-master" or name == "session-mac-address" or name == "valid-mac-address"):
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
                        if(value_path == "inner-vlan"):
                            self.inner_vlan = value
                            self.inner_vlan.value_namespace = name_space
                            self.inner_vlan.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "l2tp-tunnel-id"):
                            self.l2tp_tunnel_id = value
                            self.l2tp_tunnel_id.value_namespace = name_space
                            self.l2tp_tunnel_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "negative-acknowledgement-update-all"):
                            self.negative_acknowledgement_update_all = value
                            self.negative_acknowledgement_update_all.value_namespace = name_space
                            self.negative_acknowledgement_update_all.value_namespace_prefix = name_space_prefix
                        if(value_path == "outer-vlan"):
                            self.outer_vlan = value
                            self.outer_vlan.value_namespace = name_space
                            self.outer_vlan.value_namespace_prefix = name_space_prefix
                        if(value_path == "pppoe-session-id"):
                            self.pppoe_session_id = value
                            self.pppoe_session_id.value_namespace = name_space
                            self.pppoe_session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "role-master"):
                            self.role_master = value
                            self.role_master.value_namespace = name_space
                            self.role_master.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-mac-address"):
                            self.session_mac_address = value
                            self.session_mac_address.value_namespace = name_space
                            self.session_mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "valid-mac-address"):
                            self.valid_mac_address = value
                            self.valid_mac_address.value_namespace = name_space
                            self.valid_mac_address.value_namespace_prefix = name_space_prefix

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
                        c = SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId()
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
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancyAgent.Nodes.Node.Interfaces, self).__init__()

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
                                super(SubscriberRedundancyAgent.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriberRedundancyAgent.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    Specify interface name
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: client_status
                    
                    	Interface status for each client
                    	**type**\: list of    :py:class:`ClientStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus>`
                    
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
                    	**type**\:   :py:class:`InterfaceOper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper>`
                    
                    .. attribute:: interface_status
                    
                    	Interface Status
                    	**type**\:   :py:class:`InterfaceStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus>`
                    
                    .. attribute:: interface_synchronization_id
                    
                    	Interface Sync ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: role
                    
                    	SRG Role
                    	**type**\:   :py:class:`SrgShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRole>`
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface, self).__init__()

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

                        self.interface_oper = SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper()
                        self.interface_oper.parent = self
                        self._children_name_map["interface_oper"] = "interface-oper"
                        self._children_yang_names.add("interface-oper")

                        self.interface_status = SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus()
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
                                    super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)


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

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, self).__init__()

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
                                        super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper, self).__setattr__(name, value)

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

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, self).__init__()

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
                                        super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus, self).__setattr__(name, value)

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
                        	**type**\:   :py:class:`SrgShowComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowComp>`
                        
                        .. attribute:: session_count
                        
                        	session count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srg_show_idb_client_eoms_pending
                        
                        	SRG SHOW IDB CLIENT EOMS PENDING
                        	**type**\:  bool
                        
                        .. attribute:: srg_show_idb_client_sync_eod_pending
                        
                        	SRG SHOW IDB CLIENT SYNC EOD PENDING
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, self).__init__()

                            self.yang_name = "client-status"
                            self.yang_parent_name = "interface"

                            self.component = YLeaf(YType.enumeration, "component")

                            self.session_count = YLeaf(YType.uint32, "session-count")

                            self.srg_show_idb_client_eoms_pending = YLeaf(YType.boolean, "srg-show-idb-client-eoms-pending")

                            self.srg_show_idb_client_sync_eod_pending = YLeaf(YType.boolean, "srg-show-idb-client-sync-eod-pending")

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
                                            "session_count",
                                            "srg_show_idb_client_eoms_pending",
                                            "srg_show_idb_client_sync_eod_pending") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.component.is_set or
                                self.session_count.is_set or
                                self.srg_show_idb_client_eoms_pending.is_set or
                                self.srg_show_idb_client_sync_eod_pending.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.component.yfilter != YFilter.not_set or
                                self.session_count.yfilter != YFilter.not_set or
                                self.srg_show_idb_client_eoms_pending.yfilter != YFilter.not_set or
                                self.srg_show_idb_client_sync_eod_pending.yfilter != YFilter.not_set)

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
                            if (self.session_count.is_set or self.session_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_count.get_name_leafdata())
                            if (self.srg_show_idb_client_eoms_pending.is_set or self.srg_show_idb_client_eoms_pending.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.srg_show_idb_client_eoms_pending.get_name_leafdata())
                            if (self.srg_show_idb_client_sync_eod_pending.is_set or self.srg_show_idb_client_sync_eod_pending.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.srg_show_idb_client_sync_eod_pending.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "component" or name == "session-count" or name == "srg-show-idb-client-eoms-pending" or name == "srg-show-idb-client-sync-eod-pending"):
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
                            if(value_path == "srg-show-idb-client-eoms-pending"):
                                self.srg_show_idb_client_eoms_pending = value
                                self.srg_show_idb_client_eoms_pending.value_namespace = name_space
                                self.srg_show_idb_client_eoms_pending.value_namespace_prefix = name_space_prefix
                            if(value_path == "srg-show-idb-client-sync-eod-pending"):
                                self.srg_show_idb_client_sync_eod_pending = value
                                self.srg_show_idb_client_sync_eod_pending.value_namespace = name_space
                                self.srg_show_idb_client_sync_eod_pending.value_namespace_prefix = name_space_prefix

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
                            c = SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.client_status.append(c)
                            return c

                        if (child_yang_name == "interface-oper"):
                            if (self.interface_oper is None):
                                self.interface_oper = SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper()
                                self.interface_oper.parent = self
                                self._children_name_map["interface_oper"] = "interface-oper"
                            return self.interface_oper

                        if (child_yang_name == "interface-status"):
                            if (self.interface_status is None):
                                self.interface_status = SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus()
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
                        c = SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface()
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


            class GroupSummaries(Entity):
                """
                Subscriber data for a particular node
                
                .. attribute:: group_summary
                
                	Subscriber redundancy agent group summary
                	**type**\: list of    :py:class:`GroupSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancyAgent.Nodes.Node.GroupSummaries, self).__init__()

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
                                super(SubscriberRedundancyAgent.Nodes.Node.GroupSummaries, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriberRedundancyAgent.Nodes.Node.GroupSummaries, self).__setattr__(name, value)


                class GroupSummary(Entity):
                    """
                    Subscriber redundancy agent group summary
                    
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
                    	**type**\:   :py:class:`SrgPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgPeerStatus>`
                    
                    .. attribute:: pending_add_session_count
                    
                    	Pending Session Count for Synchornization
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: preferred_role
                    
                    	Preferred Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: role
                    
                    	SRG Role
                    	**type**\:   :py:class:`SrgShowImRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRole>`
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slave_mode
                    
                    	Slave Mode
                    	**type**\:   :py:class:`SrgShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveMode>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, self).__init__()

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
                                    super(SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary, self).__setattr__(name, value)

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
                        c = SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary()
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


            class GroupIds(Entity):
                """
                Data for particular subscriber group 
                
                .. attribute:: group_id
                
                	Group id for subscriber group
                	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberRedundancyAgent.Nodes.Node.GroupIds, self).__init__()

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
                                super(SubscriberRedundancyAgent.Nodes.Node.GroupIds, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriberRedundancyAgent.Nodes.Node.GroupIds, self).__setattr__(name, value)


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
                    
                    .. attribute:: core_tracking_object_name
                    
                    	Core Object Tracking Name
                    	**type**\:  str
                    
                    .. attribute:: core_tracking_object_status
                    
                    	Core Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: current_role
                    
                    	Current Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
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
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: interface
                    
                    	Interface List
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface>`
                    
                    .. attribute:: interface_count
                    
                    	No. of Configured Interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: l2tp_source_ip
                    
                    	L2TP Souce IP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: last_switchover_reason
                    
                    	Last Switchover Reason
                    	**type**\:   :py:class:`SrgShowSoReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSoReason>`
                    
                    .. attribute:: last_switchover_time
                    
                    	Last Switchover time
                    	**type**\:  str
                    
                    .. attribute:: negotiating_role
                    
                    	Negotiating Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: object_tracking_status
                    
                    	Object Tracking Status (Enabled/Disabled)
                    	**type**\:  bool
                    
                    .. attribute:: peer_current_role
                    
                    	Peer Current Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: peer_init_role
                    
                    	Peer Preferred Init Role
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
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
                    	**type**\:   :py:class:`SrgShowRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRole>`
                    
                    .. attribute:: peer_object_tracking_status
                    
                    	Peer Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: peer_status
                    
                    	Peer Status
                    	**type**\:   :py:class:`SrgPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgPeerStatus>`
                    
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
                    	**type**\:   :py:class:`SrgShowSlaveMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveMode>`
                    
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
                    
                    .. attribute:: tunnel_count
                    
                    	Tunnel Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: virtual_mac_address
                    
                    	Virtual MAC Address
                    	**type**\:  str
                    
                    .. attribute:: virtual_mac_address_disable
                    
                    	Virtual MAC Address Disable
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId, self).__init__()

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

                        self.l2tp_source_ip = YLeaf(YType.str, "l2tp-source-ip")

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

                        self.tunnel_count = YLeaf(YType.uint32, "tunnel-count")

                        self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                        self.virtual_mac_address_disable = YLeaf(YType.boolean, "virtual-mac-address-disable")

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
                                        "l2tp_source_ip",
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
                                        "switchover_revert_time",
                                        "tunnel_count",
                                        "virtual_mac_address",
                                        "virtual_mac_address_disable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId, self).__setattr__(name, value)


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

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, self).__init__()

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
                                        super(SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface, self).__setattr__(name, value)

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
                            self.l2tp_source_ip.is_set or
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
                            self.switchover_revert_time.is_set or
                            self.tunnel_count.is_set or
                            self.virtual_mac_address.is_set or
                            self.virtual_mac_address_disable.is_set)

                    def has_operation(self):
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
                            self.l2tp_source_ip.yfilter != YFilter.not_set or
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
                            self.switchover_revert_time.yfilter != YFilter.not_set or
                            self.tunnel_count.yfilter != YFilter.not_set or
                            self.virtual_mac_address.yfilter != YFilter.not_set or
                            self.virtual_mac_address_disable.yfilter != YFilter.not_set)

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
                        if (self.l2tp_source_ip.is_set or self.l2tp_source_ip.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.l2tp_source_ip.get_name_leafdata())
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
                        if (self.tunnel_count.is_set or self.tunnel_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tunnel_count.get_name_leafdata())
                        if (self.virtual_mac_address.is_set or self.virtual_mac_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.virtual_mac_address.get_name_leafdata())
                        if (self.virtual_mac_address_disable.is_set or self.virtual_mac_address_disable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.virtual_mac_address_disable.get_name_leafdata())

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
                            c = SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.interface.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface" or name == "group-id" or name == "access-tracking-object-name" or name == "access-tracking-object-status" or name == "core-tracking-object-name" or name == "core-tracking-object-status" or name == "current-role" or name == "description" or name == "disabled" or name == "group-id-xr" or name == "hold-timer" or name == "init-role" or name == "interface-count" or name == "l2tp-source-ip" or name == "last-switchover-reason" or name == "last-switchover-time" or name == "negotiating-role" or name == "object-tracking-status" or name == "peer-current-role" or name == "peer-init-role" or name == "peer-ipv4-address" or name == "peer-ipv6-address" or name == "peer-last-down-time" or name == "peer-last-negotiation-time" or name == "peer-last-up-time" or name == "peer-negotiating-role" or name == "peer-object-tracking-status" or name == "peer-status" or name == "pending-session-delete-count" or name == "pending-session-update-count" or name == "revertive-timer" or name == "session-count" or name == "slave-mode" or name == "slave-update-failure-count" or name == "switchover-count" or name == "switchover-hold-time" or name == "switchover-revert-time" or name == "tunnel-count" or name == "virtual-mac-address" or name == "virtual-mac-address-disable"):
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
                        if(value_path == "l2tp-source-ip"):
                            self.l2tp_source_ip = value
                            self.l2tp_source_ip.value_namespace = name_space
                            self.l2tp_source_ip.value_namespace_prefix = name_space_prefix
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
                        if(value_path == "tunnel-count"):
                            self.tunnel_count = value
                            self.tunnel_count.value_namespace = name_space
                            self.tunnel_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "virtual-mac-address"):
                            self.virtual_mac_address = value
                            self.virtual_mac_address.value_namespace = name_space
                            self.virtual_mac_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "virtual-mac-address-disable"):
                            self.virtual_mac_address_disable = value
                            self.virtual_mac_address_disable.value_namespace = name_space
                            self.virtual_mac_address_disable.value_namespace_prefix = name_space_prefix

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
                        c = SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId()
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

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.group_id_xr is not None and self.group_id_xr.has_data()) or
                    (self.group_ids is not None and self.group_ids.has_data()) or
                    (self.group_summaries is not None and self.group_summaries.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.group_id_xr is not None and self.group_id_xr.has_operation()) or
                    (self.group_ids is not None and self.group_ids.has_operation()) or
                    (self.group_summaries is not None and self.group_summaries.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-agent/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "group-id-xr"):
                    if (self.group_id_xr is None):
                        self.group_id_xr = SubscriberRedundancyAgent.Nodes.Node.GroupIdXr()
                        self.group_id_xr.parent = self
                        self._children_name_map["group_id_xr"] = "group-id-xr"
                    return self.group_id_xr

                if (child_yang_name == "group-ids"):
                    if (self.group_ids is None):
                        self.group_ids = SubscriberRedundancyAgent.Nodes.Node.GroupIds()
                        self.group_ids.parent = self
                        self._children_name_map["group_ids"] = "group-ids"
                    return self.group_ids

                if (child_yang_name == "group-summaries"):
                    if (self.group_summaries is None):
                        self.group_summaries = SubscriberRedundancyAgent.Nodes.Node.GroupSummaries()
                        self.group_summaries.parent = self
                        self._children_name_map["group_summaries"] = "group-summaries"
                    return self.group_summaries

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = SubscriberRedundancyAgent.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "group-id-xr" or name == "group-ids" or name == "group-summaries" or name == "interfaces" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-agent/%s" % self.get_segment_path()
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
                c = SubscriberRedundancyAgent.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-agent" + path_buffer

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
                self.nodes = SubscriberRedundancyAgent.Nodes()
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
        self._top_entity = SubscriberRedundancyAgent()
        return self._top_entity

