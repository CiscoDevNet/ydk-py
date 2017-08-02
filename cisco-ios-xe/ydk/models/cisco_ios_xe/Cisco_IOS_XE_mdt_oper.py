""" Cisco_IOS_XE_mdt_oper 

This module contains a collection of YANG 
definitions for operational data of streaming telemetry.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MdtConState(Enum):
    """
    MdtConState

    Connection states.

    .. data:: con_state_active = 0

    	The connection is active and usable.

    .. data:: con_state_connecting = 1

    	An attempt is being made to set the connection up.

    .. data:: con_state_pending = 2

    	The connection is down, but between connection

    	attempts. It is in this state, for example, during

    	the idle time between retries.

    .. data:: con_state_disconnecting = 3

    	The connection is the process of being disconnected.

    """

    con_state_active = Enum.YLeaf(0, "con-state-active")

    con_state_connecting = Enum.YLeaf(1, "con-state-connecting")

    con_state_pending = Enum.YLeaf(2, "con-state-pending")

    con_state_disconnecting = Enum.YLeaf(3, "con-state-disconnecting")


class MdtReceiverState(Enum):
    """
    MdtReceiverState

    Receiver states.

    .. data:: rcvr_state_invalid = 1

    	The receiver configuration is invalid and

    	cannot be used.

    .. data:: rcvr_state_disconnected = 2

    	The receiver is disconnected and there is no

    	attempt being made to connect to it.

    .. data:: rcvr_state_connecting = 3

    	An attempt is being made to connect to the receiver.

    .. data:: rcvr_state_connected = 4

    	The receiver is connected, and update notifications

    	are being sent to the receiver when they occur

    """

    rcvr_state_invalid = Enum.YLeaf(1, "rcvr-state-invalid")

    rcvr_state_disconnected = Enum.YLeaf(2, "rcvr-state-disconnected")

    rcvr_state_connecting = Enum.YLeaf(3, "rcvr-state-connecting")

    rcvr_state_connected = Enum.YLeaf(4, "rcvr-state-connected")


class MdtSubState(Enum):
    """
    MdtSubState

    Subscription states

    .. data:: sub_state_valid = 0

    	The subscription is valid and may be sending updates.

    .. data:: sub_state_suspended = 1

    	The subscription has been suspended and is not

    	sending notifications even if there are updates.

    .. data:: sub_state_terminated = 2

    	The subscription is terminated. This state is valid

    	only for static subscriptions.

    .. data:: sub_state_invalid = 3

    	The subscription is invalid. This state is valid

    	only for static subscriptions.

    """

    sub_state_valid = Enum.YLeaf(0, "sub-state-valid")

    sub_state_suspended = Enum.YLeaf(1, "sub-state-suspended")

    sub_state_terminated = Enum.YLeaf(2, "sub-state-terminated")

    sub_state_invalid = Enum.YLeaf(3, "sub-state-invalid")


class MdtSubType(Enum):
    """
    MdtSubType

    Subscription types

    .. data:: sub_type_dynamic = 1

    	Dynamic subscriptions

    	-do not survive reboot

    	-existence tied to connection they are created on

    	-send updates only to peer that creates them

    .. data:: sub_type_static = 2

    	Static subscriptions

    	-created, (modified), and deleted by management operations

    	-survive reboot

    	-receivers are configured 

    """

    sub_type_dynamic = Enum.YLeaf(1, "sub-type-dynamic")

    sub_type_static = Enum.YLeaf(2, "sub-type-static")



class MdtOperData(Entity):
    """
    MDT operational data.
    
    .. attribute:: mdt_connections
    
    	MDT subscription connection operational data
    	**type**\: list of    :py:class:`MdtConnections <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtConnections>`
    
    .. attribute:: mdt_streams
    
    	MDT streams table. The list of supported streams
    	**type**\:   :py:class:`MdtStreams <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtStreams>`
    
    .. attribute:: mdt_subscriptions
    
    	MDT subscription operational data
    	**type**\: list of    :py:class:`MdtSubscriptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtSubscriptions>`
    
    

    """

    _prefix = 'mdt-oper'
    _revision = '2017-03-02'

    def __init__(self):
        super(MdtOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "mdt-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-mdt-oper"

        self.mdt_streams = MdtOperData.MdtStreams()
        self.mdt_streams.parent = self
        self._children_name_map["mdt_streams"] = "mdt-streams"
        self._children_yang_names.add("mdt-streams")

        self.mdt_connections = YList(self)
        self.mdt_subscriptions = YList(self)

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
                    super(MdtOperData, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(MdtOperData, self).__setattr__(name, value)


    class MdtStreams(Entity):
        """
        MDT streams table. The list of supported streams.
        
        .. attribute:: stream
        
        	Name of a supported stream
        	**type**\:  list of str
        
        

        """

        _prefix = 'mdt-oper'
        _revision = '2017-03-02'

        def __init__(self):
            super(MdtOperData.MdtStreams, self).__init__()

            self.yang_name = "mdt-streams"
            self.yang_parent_name = "mdt-oper-data"

            self.stream = YLeafList(YType.str, "stream")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("stream") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MdtOperData.MdtStreams, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MdtOperData.MdtStreams, self).__setattr__(name, value)

        def has_data(self):
            for leaf in self.stream.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return False

        def has_operation(self):
            for leaf in self.stream.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.stream.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mdt-streams" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-mdt-oper:mdt-oper-data/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            leaf_name_data.extend(self.stream.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stream"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "stream"):
                self.stream.append(value)


    class MdtSubscriptions(Entity):
        """
        MDT subscription operational data.
        
        .. attribute:: subscription_id  <key>
        
        	Unique subscription identifier
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: base
        
        	Common subscription information
        	**type**\:   :py:class:`Base <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtSubscriptions.Base>`
        
        .. attribute:: comments
        
        	Comments related to subcription state
        	**type**\:  str
        
        .. attribute:: mdt_receivers
        
        	List of MDT receivers
        	**type**\: list of    :py:class:`MdtReceivers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtSubscriptions.MdtReceivers>`
        
        .. attribute:: state
        
        	Subscription state
        	**type**\:   :py:class:`MdtSubState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtSubState>`
        
        .. attribute:: type
        
        	Subscription type
        	**type**\:   :py:class:`MdtSubType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtSubType>`
        
        .. attribute:: updates_dampened
        
        	Number of updates dropped due to dampening
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: updates_dropped
        
        	Number of updates dropped to other causes
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: updates_in
        
        	Number of updates received from sensors as candidates for notifications
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        

        """

        _prefix = 'mdt-oper'
        _revision = '2017-03-02'

        def __init__(self):
            super(MdtOperData.MdtSubscriptions, self).__init__()

            self.yang_name = "mdt-subscriptions"
            self.yang_parent_name = "mdt-oper-data"

            self.subscription_id = YLeaf(YType.uint32, "subscription-id")

            self.comments = YLeaf(YType.str, "comments")

            self.state = YLeaf(YType.enumeration, "state")

            self.type = YLeaf(YType.enumeration, "type")

            self.updates_dampened = YLeaf(YType.uint64, "updates-dampened")

            self.updates_dropped = YLeaf(YType.uint64, "updates-dropped")

            self.updates_in = YLeaf(YType.uint64, "updates-in")

            self.base = MdtOperData.MdtSubscriptions.Base()
            self.base.parent = self
            self._children_name_map["base"] = "base"
            self._children_yang_names.add("base")

            self.mdt_receivers = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("subscription_id",
                            "comments",
                            "state",
                            "type",
                            "updates_dampened",
                            "updates_dropped",
                            "updates_in") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MdtOperData.MdtSubscriptions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MdtOperData.MdtSubscriptions, self).__setattr__(name, value)


        class Base(Entity):
            """
            Common subscription information.
            
            .. attribute:: encoding
            
            	Update notification encoding
            	**type**\:  str
            
            	**default value**\: encode-xml
            
            .. attribute:: no_filter
            
            	Placeholder for unset value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**default value**\: 0
            
            .. attribute:: no_synch_on_start
            
            	If true, there is no initial update notification with the current value of all the data. NOT CURRENTLY SUPPORTED. If specified, must be false
            	**type**\:  bool
            
            .. attribute:: no_trigger
            
            	Placeholder for unset value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**default value**\: 0
            
            .. attribute:: period
            
            	Period of update notifications in 100ths of a second
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            	**units**\: centiseconds
            
            .. attribute:: stream
            
            	The name of the event stream being subscribed to
            	**type**\:  str
            
            	**default value**\: NETCONF
            
            .. attribute:: xpath
            
            	XPath expression describing the set of objects wanted as part of the subscription
            	**type**\:  str
            
            

            """

            _prefix = 'mdt-oper'
            _revision = '2017-03-02'

            def __init__(self):
                super(MdtOperData.MdtSubscriptions.Base, self).__init__()

                self.yang_name = "base"
                self.yang_parent_name = "mdt-subscriptions"

                self.encoding = YLeaf(YType.str, "encoding")

                self.no_filter = YLeaf(YType.uint32, "no-filter")

                self.no_synch_on_start = YLeaf(YType.boolean, "no-synch-on-start")

                self.no_trigger = YLeaf(YType.uint32, "no-trigger")

                self.period = YLeaf(YType.uint32, "period")

                self.stream = YLeaf(YType.str, "stream")

                self.xpath = YLeaf(YType.str, "xpath")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("encoding",
                                "no_filter",
                                "no_synch_on_start",
                                "no_trigger",
                                "period",
                                "stream",
                                "xpath") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MdtOperData.MdtSubscriptions.Base, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MdtOperData.MdtSubscriptions.Base, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.encoding.is_set or
                    self.no_filter.is_set or
                    self.no_synch_on_start.is_set or
                    self.no_trigger.is_set or
                    self.period.is_set or
                    self.stream.is_set or
                    self.xpath.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.encoding.yfilter != YFilter.not_set or
                    self.no_filter.yfilter != YFilter.not_set or
                    self.no_synch_on_start.yfilter != YFilter.not_set or
                    self.no_trigger.yfilter != YFilter.not_set or
                    self.period.yfilter != YFilter.not_set or
                    self.stream.yfilter != YFilter.not_set or
                    self.xpath.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "base" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.encoding.get_name_leafdata())
                if (self.no_filter.is_set or self.no_filter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.no_filter.get_name_leafdata())
                if (self.no_synch_on_start.is_set or self.no_synch_on_start.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.no_synch_on_start.get_name_leafdata())
                if (self.no_trigger.is_set or self.no_trigger.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.no_trigger.get_name_leafdata())
                if (self.period.is_set or self.period.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.period.get_name_leafdata())
                if (self.stream.is_set or self.stream.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stream.get_name_leafdata())
                if (self.xpath.is_set or self.xpath.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.xpath.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "encoding" or name == "no-filter" or name == "no-synch-on-start" or name == "no-trigger" or name == "period" or name == "stream" or name == "xpath"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "encoding"):
                    self.encoding = value
                    self.encoding.value_namespace = name_space
                    self.encoding.value_namespace_prefix = name_space_prefix
                if(value_path == "no-filter"):
                    self.no_filter = value
                    self.no_filter.value_namespace = name_space
                    self.no_filter.value_namespace_prefix = name_space_prefix
                if(value_path == "no-synch-on-start"):
                    self.no_synch_on_start = value
                    self.no_synch_on_start.value_namespace = name_space
                    self.no_synch_on_start.value_namespace_prefix = name_space_prefix
                if(value_path == "no-trigger"):
                    self.no_trigger = value
                    self.no_trigger.value_namespace = name_space
                    self.no_trigger.value_namespace_prefix = name_space_prefix
                if(value_path == "period"):
                    self.period = value
                    self.period.value_namespace = name_space
                    self.period.value_namespace_prefix = name_space_prefix
                if(value_path == "stream"):
                    self.stream = value
                    self.stream.value_namespace = name_space
                    self.stream.value_namespace_prefix = name_space_prefix
                if(value_path == "xpath"):
                    self.xpath = value
                    self.xpath.value_namespace = name_space
                    self.xpath.value_namespace_prefix = name_space_prefix


        class MdtReceivers(Entity):
            """
            List of MDT receivers.
            
            .. attribute:: address  <key>
            
            	IP address of the receiver
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            
            ----
            .. attribute:: port  <key>
            
            	Network port of the receiver
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**mandatory**\: True
            
            .. attribute:: comments
            
            	Comments related to receiver state
            	**type**\:  str
            
            .. attribute:: protocol
            
            	Receiver transport protocol
            	**type**\:  str
            
            .. attribute:: state
            
            	Receiver state
            	**type**\:   :py:class:`MdtReceiverState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtReceiverState>`
            
            

            """

            _prefix = 'mdt-oper'
            _revision = '2017-03-02'

            def __init__(self):
                super(MdtOperData.MdtSubscriptions.MdtReceivers, self).__init__()

                self.yang_name = "mdt-receivers"
                self.yang_parent_name = "mdt-subscriptions"

                self.address = YLeaf(YType.str, "address")

                self.port = YLeaf(YType.uint16, "port")

                self.comments = YLeaf(YType.str, "comments")

                self.protocol = YLeaf(YType.str, "protocol")

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
                    if name in ("address",
                                "port",
                                "comments",
                                "protocol",
                                "state") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MdtOperData.MdtSubscriptions.MdtReceivers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MdtOperData.MdtSubscriptions.MdtReceivers, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.address.is_set or
                    self.port.is_set or
                    self.comments.is_set or
                    self.protocol.is_set or
                    self.state.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.address.yfilter != YFilter.not_set or
                    self.port.yfilter != YFilter.not_set or
                    self.comments.yfilter != YFilter.not_set or
                    self.protocol.yfilter != YFilter.not_set or
                    self.state.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mdt-receivers" + "[address='" + self.address.get() + "']" + "[port='" + self.port.get() + "']" + path_buffer

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
                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port.get_name_leafdata())
                if (self.comments.is_set or self.comments.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.comments.get_name_leafdata())
                if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.protocol.get_name_leafdata())
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
                if(name == "address" or name == "port" or name == "comments" or name == "protocol" or name == "state"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "address"):
                    self.address = value
                    self.address.value_namespace = name_space
                    self.address.value_namespace_prefix = name_space_prefix
                if(value_path == "port"):
                    self.port = value
                    self.port.value_namespace = name_space
                    self.port.value_namespace_prefix = name_space_prefix
                if(value_path == "comments"):
                    self.comments = value
                    self.comments.value_namespace = name_space
                    self.comments.value_namespace_prefix = name_space_prefix
                if(value_path == "protocol"):
                    self.protocol = value
                    self.protocol.value_namespace = name_space
                    self.protocol.value_namespace_prefix = name_space_prefix
                if(value_path == "state"):
                    self.state = value
                    self.state.value_namespace = name_space
                    self.state.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mdt_receivers:
                if (c.has_data()):
                    return True
            return (
                self.subscription_id.is_set or
                self.comments.is_set or
                self.state.is_set or
                self.type.is_set or
                self.updates_dampened.is_set or
                self.updates_dropped.is_set or
                self.updates_in.is_set or
                (self.base is not None and self.base.has_data()))

        def has_operation(self):
            for c in self.mdt_receivers:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.subscription_id.yfilter != YFilter.not_set or
                self.comments.yfilter != YFilter.not_set or
                self.state.yfilter != YFilter.not_set or
                self.type.yfilter != YFilter.not_set or
                self.updates_dampened.yfilter != YFilter.not_set or
                self.updates_dropped.yfilter != YFilter.not_set or
                self.updates_in.yfilter != YFilter.not_set or
                (self.base is not None and self.base.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mdt-subscriptions" + "[subscription-id='" + self.subscription_id.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-mdt-oper:mdt-oper-data/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_id.get_name_leafdata())
            if (self.comments.is_set or self.comments.yfilter != YFilter.not_set):
                leaf_name_data.append(self.comments.get_name_leafdata())
            if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                leaf_name_data.append(self.state.get_name_leafdata())
            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.type.get_name_leafdata())
            if (self.updates_dampened.is_set or self.updates_dampened.yfilter != YFilter.not_set):
                leaf_name_data.append(self.updates_dampened.get_name_leafdata())
            if (self.updates_dropped.is_set or self.updates_dropped.yfilter != YFilter.not_set):
                leaf_name_data.append(self.updates_dropped.get_name_leafdata())
            if (self.updates_in.is_set or self.updates_in.yfilter != YFilter.not_set):
                leaf_name_data.append(self.updates_in.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "base"):
                if (self.base is None):
                    self.base = MdtOperData.MdtSubscriptions.Base()
                    self.base.parent = self
                    self._children_name_map["base"] = "base"
                return self.base

            if (child_yang_name == "mdt-receivers"):
                for c in self.mdt_receivers:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MdtOperData.MdtSubscriptions.MdtReceivers()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mdt_receivers.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "base" or name == "mdt-receivers" or name == "subscription-id" or name == "comments" or name == "state" or name == "type" or name == "updates-dampened" or name == "updates-dropped" or name == "updates-in"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "subscription-id"):
                self.subscription_id = value
                self.subscription_id.value_namespace = name_space
                self.subscription_id.value_namespace_prefix = name_space_prefix
            if(value_path == "comments"):
                self.comments = value
                self.comments.value_namespace = name_space
                self.comments.value_namespace_prefix = name_space_prefix
            if(value_path == "state"):
                self.state = value
                self.state.value_namespace = name_space
                self.state.value_namespace_prefix = name_space_prefix
            if(value_path == "type"):
                self.type = value
                self.type.value_namespace = name_space
                self.type.value_namespace_prefix = name_space_prefix
            if(value_path == "updates-dampened"):
                self.updates_dampened = value
                self.updates_dampened.value_namespace = name_space
                self.updates_dampened.value_namespace_prefix = name_space_prefix
            if(value_path == "updates-dropped"):
                self.updates_dropped = value
                self.updates_dropped.value_namespace = name_space
                self.updates_dropped.value_namespace_prefix = name_space_prefix
            if(value_path == "updates-in"):
                self.updates_in = value
                self.updates_in.value_namespace = name_space
                self.updates_in.value_namespace_prefix = name_space_prefix


    class MdtConnections(Entity):
        """
        MDT subscription connection operational data.
        
        .. attribute:: address  <key>
        
        	IP address
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: port  <key>
        
        	Network port
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: mdt_sub_con_stats
        
        	List of subscription specific statistics for this connection
        	**type**\: list of    :py:class:`MdtSubConStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtOperData.MdtConnections.MdtSubConStats>`
        
        .. attribute:: peer_id
        
        	Identity of the peer at the other end of the connection. May be empty, depending on connection state
        	**type**\:  str
        
        .. attribute:: state
        
        	Connection state
        	**type**\:   :py:class:`MdtConState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_oper.MdtConState>`
        
        .. attribute:: transport
        
        	Transport protocol on this connection See transport\-protocol from subscribed\-notifications for possible values
        	**type**\:  str
        
        

        """

        _prefix = 'mdt-oper'
        _revision = '2017-03-02'

        def __init__(self):
            super(MdtOperData.MdtConnections, self).__init__()

            self.yang_name = "mdt-connections"
            self.yang_parent_name = "mdt-oper-data"

            self.address = YLeaf(YType.str, "address")

            self.port = YLeaf(YType.uint16, "port")

            self.peer_id = YLeaf(YType.str, "peer-id")

            self.state = YLeaf(YType.enumeration, "state")

            self.transport = YLeaf(YType.str, "transport")

            self.mdt_sub_con_stats = YList(self)

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
                            "port",
                            "peer_id",
                            "state",
                            "transport") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MdtOperData.MdtConnections, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MdtOperData.MdtConnections, self).__setattr__(name, value)


        class MdtSubConStats(Entity):
            """
            List of subscription specific statistics for this
            connection.
            
            .. attribute:: sub_id  <key>
            
            	Subscription identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: updates_dropped
            
            	Number of dropped update notifications due to error or events not in other counters using this subscription
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: updates_sent
            
            	Number of update notifications sent to the receiver using this subscription
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'mdt-oper'
            _revision = '2017-03-02'

            def __init__(self):
                super(MdtOperData.MdtConnections.MdtSubConStats, self).__init__()

                self.yang_name = "mdt-sub-con-stats"
                self.yang_parent_name = "mdt-connections"

                self.sub_id = YLeaf(YType.uint32, "sub-id")

                self.updates_dropped = YLeaf(YType.uint64, "updates-dropped")

                self.updates_sent = YLeaf(YType.uint64, "updates-sent")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("sub_id",
                                "updates_dropped",
                                "updates_sent") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MdtOperData.MdtConnections.MdtSubConStats, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MdtOperData.MdtConnections.MdtSubConStats, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.sub_id.is_set or
                    self.updates_dropped.is_set or
                    self.updates_sent.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.sub_id.yfilter != YFilter.not_set or
                    self.updates_dropped.yfilter != YFilter.not_set or
                    self.updates_sent.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mdt-sub-con-stats" + "[sub-id='" + self.sub_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.sub_id.is_set or self.sub_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sub_id.get_name_leafdata())
                if (self.updates_dropped.is_set or self.updates_dropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.updates_dropped.get_name_leafdata())
                if (self.updates_sent.is_set or self.updates_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.updates_sent.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sub-id" or name == "updates-dropped" or name == "updates-sent"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "sub-id"):
                    self.sub_id = value
                    self.sub_id.value_namespace = name_space
                    self.sub_id.value_namespace_prefix = name_space_prefix
                if(value_path == "updates-dropped"):
                    self.updates_dropped = value
                    self.updates_dropped.value_namespace = name_space
                    self.updates_dropped.value_namespace_prefix = name_space_prefix
                if(value_path == "updates-sent"):
                    self.updates_sent = value
                    self.updates_sent.value_namespace = name_space
                    self.updates_sent.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mdt_sub_con_stats:
                if (c.has_data()):
                    return True
            return (
                self.address.is_set or
                self.port.is_set or
                self.peer_id.is_set or
                self.state.is_set or
                self.transport.is_set)

        def has_operation(self):
            for c in self.mdt_sub_con_stats:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.address.yfilter != YFilter.not_set or
                self.port.yfilter != YFilter.not_set or
                self.peer_id.yfilter != YFilter.not_set or
                self.state.yfilter != YFilter.not_set or
                self.transport.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mdt-connections" + "[address='" + self.address.get() + "']" + "[port='" + self.port.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-mdt-oper:mdt-oper-data/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.address.get_name_leafdata())
            if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                leaf_name_data.append(self.port.get_name_leafdata())
            if (self.peer_id.is_set or self.peer_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.peer_id.get_name_leafdata())
            if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                leaf_name_data.append(self.state.get_name_leafdata())
            if (self.transport.is_set or self.transport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.transport.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mdt-sub-con-stats"):
                for c in self.mdt_sub_con_stats:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MdtOperData.MdtConnections.MdtSubConStats()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mdt_sub_con_stats.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mdt-sub-con-stats" or name == "address" or name == "port" or name == "peer-id" or name == "state" or name == "transport"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "address"):
                self.address = value
                self.address.value_namespace = name_space
                self.address.value_namespace_prefix = name_space_prefix
            if(value_path == "port"):
                self.port = value
                self.port.value_namespace = name_space
                self.port.value_namespace_prefix = name_space_prefix
            if(value_path == "peer-id"):
                self.peer_id = value
                self.peer_id.value_namespace = name_space
                self.peer_id.value_namespace_prefix = name_space_prefix
            if(value_path == "state"):
                self.state = value
                self.state.value_namespace = name_space
                self.state.value_namespace_prefix = name_space_prefix
            if(value_path == "transport"):
                self.transport = value
                self.transport.value_namespace = name_space
                self.transport.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.mdt_connections:
            if (c.has_data()):
                return True
        for c in self.mdt_subscriptions:
            if (c.has_data()):
                return True
        return (self.mdt_streams is not None and self.mdt_streams.has_data())

    def has_operation(self):
        for c in self.mdt_connections:
            if (c.has_operation()):
                return True
        for c in self.mdt_subscriptions:
            if (c.has_operation()):
                return True
        return (
            self.yfilter != YFilter.not_set or
            (self.mdt_streams is not None and self.mdt_streams.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-mdt-oper:mdt-oper-data" + path_buffer

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

        if (child_yang_name == "mdt-connections"):
            for c in self.mdt_connections:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = MdtOperData.MdtConnections()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.mdt_connections.append(c)
            return c

        if (child_yang_name == "mdt-streams"):
            if (self.mdt_streams is None):
                self.mdt_streams = MdtOperData.MdtStreams()
                self.mdt_streams.parent = self
                self._children_name_map["mdt_streams"] = "mdt-streams"
            return self.mdt_streams

        if (child_yang_name == "mdt-subscriptions"):
            for c in self.mdt_subscriptions:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = MdtOperData.MdtSubscriptions()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.mdt_subscriptions.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mdt-connections" or name == "mdt-streams" or name == "mdt-subscriptions"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MdtOperData()
        return self._top_entity

