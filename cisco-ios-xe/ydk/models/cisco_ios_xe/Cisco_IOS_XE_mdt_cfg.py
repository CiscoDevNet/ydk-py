""" Cisco_IOS_XE_mdt_cfg 

This module contains a collection of YANG 
definitions for configuration of streaming telemetry.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MdtSubscriptions(Entity):
    """
    Subscription configuration
    
    .. attribute:: mdt_subscription
    
    	List of subscriptions
    	**type**\: list of    :py:class:`MdtSubscription <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtSubscription>`
    
    

    """

    _prefix = 'mdt-cfg'
    _revision = '2017-03-02'

    def __init__(self):
        super(MdtSubscriptions, self).__init__()
        self._top_entity = None

        self.yang_name = "mdt-subscriptions"
        self.yang_parent_name = "Cisco-IOS-XE-mdt-cfg"

        self.mdt_subscription = YList(self)

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
                    super(MdtSubscriptions, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(MdtSubscriptions, self).__setattr__(name, value)


    class MdtSubscription(Entity):
        """
        List of subscriptions
        
        .. attribute:: subscription_id  <key>
        
        	Unique subscription identifier
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: base
        
        	Common subscription information
        	**type**\:   :py:class:`Base <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtSubscription.Base>`
        
        .. attribute:: mdt_receivers
        
        	Configuration of receivers of configured subscriptions
        	**type**\: list of    :py:class:`MdtReceivers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mdt_cfg.MdtSubscriptions.MdtSubscription.MdtReceivers>`
        
        

        """

        _prefix = 'mdt-cfg'
        _revision = '2017-03-02'

        def __init__(self):
            super(MdtSubscriptions.MdtSubscription, self).__init__()

            self.yang_name = "mdt-subscription"
            self.yang_parent_name = "mdt-subscriptions"

            self.subscription_id = YLeaf(YType.uint32, "subscription-id")

            self.base = MdtSubscriptions.MdtSubscription.Base()
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
                if name in ("subscription_id") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MdtSubscriptions.MdtSubscription, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MdtSubscriptions.MdtSubscription, self).__setattr__(name, value)


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

            _prefix = 'mdt-cfg'
            _revision = '2017-03-02'

            def __init__(self):
                super(MdtSubscriptions.MdtSubscription.Base, self).__init__()

                self.yang_name = "base"
                self.yang_parent_name = "mdt-subscription"

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
                            super(MdtSubscriptions.MdtSubscription.Base, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MdtSubscriptions.MdtSubscription.Base, self).__setattr__(name, value)

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
            Configuration of receivers of configured subscriptions.
            
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
            
            .. attribute:: protocol
            
            	Receiver transport protocol
            	**type**\:  str
            
            	**default value**\: netconf
            
            

            """

            _prefix = 'mdt-cfg'
            _revision = '2017-03-02'

            def __init__(self):
                super(MdtSubscriptions.MdtSubscription.MdtReceivers, self).__init__()

                self.yang_name = "mdt-receivers"
                self.yang_parent_name = "mdt-subscription"

                self.address = YLeaf(YType.str, "address")

                self.port = YLeaf(YType.uint16, "port")

                self.protocol = YLeaf(YType.str, "protocol")

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
                                "protocol") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MdtSubscriptions.MdtSubscription.MdtReceivers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MdtSubscriptions.MdtSubscription.MdtReceivers, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.address.is_set or
                    self.port.is_set or
                    self.protocol.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.address.yfilter != YFilter.not_set or
                    self.port.yfilter != YFilter.not_set or
                    self.protocol.yfilter != YFilter.not_set)

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
                if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.protocol.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "address" or name == "port" or name == "protocol"):
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
                if(value_path == "protocol"):
                    self.protocol = value
                    self.protocol.value_namespace = name_space
                    self.protocol.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mdt_receivers:
                if (c.has_data()):
                    return True
            return (
                self.subscription_id.is_set or
                (self.base is not None and self.base.has_data()))

        def has_operation(self):
            for c in self.mdt_receivers:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.subscription_id.yfilter != YFilter.not_set or
                (self.base is not None and self.base.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mdt-subscription" + "[subscription-id='" + self.subscription_id.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-mdt-cfg:mdt-subscriptions/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_id.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "base"):
                if (self.base is None):
                    self.base = MdtSubscriptions.MdtSubscription.Base()
                    self.base.parent = self
                    self._children_name_map["base"] = "base"
                return self.base

            if (child_yang_name == "mdt-receivers"):
                for c in self.mdt_receivers:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MdtSubscriptions.MdtSubscription.MdtReceivers()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mdt_receivers.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "base" or name == "mdt-receivers" or name == "subscription-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "subscription-id"):
                self.subscription_id = value
                self.subscription_id.value_namespace = name_space
                self.subscription_id.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.mdt_subscription:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.mdt_subscription:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-mdt-cfg:mdt-subscriptions" + path_buffer

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

        if (child_yang_name == "mdt-subscription"):
            for c in self.mdt_subscription:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = MdtSubscriptions.MdtSubscription()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.mdt_subscription.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mdt-subscription"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MdtSubscriptions()
        return self._top_entity

