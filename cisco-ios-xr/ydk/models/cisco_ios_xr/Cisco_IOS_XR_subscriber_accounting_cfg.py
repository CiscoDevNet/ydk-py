""" Cisco_IOS_XR_subscriber_accounting_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-accounting package configuration.

This module contains definitions
for the following management objects\:
  subscriber\-accounting\: Subscriber Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SubscriberAccounting(Entity):
    """
    Subscriber Configuration
    
    .. attribute:: prepaid_configurations
    
    	Subscriber Prepaid Feature Configuration
    	**type**\:   :py:class:`PrepaidConfigurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg.SubscriberAccounting.PrepaidConfigurations>`
    
    

    """

    _prefix = 'subscriber-accounting-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberAccounting, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-accounting"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-accounting-cfg"

        self.prepaid_configurations = SubscriberAccounting.PrepaidConfigurations()
        self.prepaid_configurations.parent = self
        self._children_name_map["prepaid_configurations"] = "prepaid-configurations"
        self._children_yang_names.add("prepaid-configurations")


    class PrepaidConfigurations(Entity):
        """
        Subscriber Prepaid Feature Configuration
        
        .. attribute:: prepaid_configuration
        
        	Prepaid configuration name or default
        	**type**\: list of    :py:class:`PrepaidConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg.SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration>`
        
        

        """

        _prefix = 'subscriber-accounting-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberAccounting.PrepaidConfigurations, self).__init__()

            self.yang_name = "prepaid-configurations"
            self.yang_parent_name = "subscriber-accounting"

            self.prepaid_configuration = YList(self)

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
                        super(SubscriberAccounting.PrepaidConfigurations, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubscriberAccounting.PrepaidConfigurations, self).__setattr__(name, value)


        class PrepaidConfiguration(Entity):
            """
            Prepaid configuration name or default
            
            .. attribute:: prepaid_config_name  <key>
            
            	Prepaid configuration name or default
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: accounting_method_list
            
            	Method list to be used when placing prepaid accounting requests
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: author_method_list
            
            	Method list to be used when placing prepaid (re)authorization requests
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: password
            
            	Password to be used when placing prepaid (re)authorization requests
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: time_hold
            
            	Idle Threshold for which prepaid quota is valid
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: time_threshold
            
            	Threshold at which to send prepaid time quota request
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: time_valid
            
            	Threshold for which prepaid quota is valid
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: traffic_direction
            
            	Prepaid quota traffic direction
            	**type**\:  str
            
            .. attribute:: volume_threshold
            
            	Threshold at which to send prepaid volume quota request
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'subscriber-accounting-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration, self).__init__()

                self.yang_name = "prepaid-configuration"
                self.yang_parent_name = "prepaid-configurations"

                self.prepaid_config_name = YLeaf(YType.str, "prepaid-config-name")

                self.accounting_method_list = YLeaf(YType.str, "accounting-method-list")

                self.author_method_list = YLeaf(YType.str, "author-method-list")

                self.password = YLeaf(YType.str, "password")

                self.time_hold = YLeaf(YType.int32, "time-hold")

                self.time_threshold = YLeaf(YType.int32, "time-threshold")

                self.time_valid = YLeaf(YType.int32, "time-valid")

                self.traffic_direction = YLeaf(YType.str, "traffic-direction")

                self.volume_threshold = YLeaf(YType.int32, "volume-threshold")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("prepaid_config_name",
                                "accounting_method_list",
                                "author_method_list",
                                "password",
                                "time_hold",
                                "time_threshold",
                                "time_valid",
                                "traffic_direction",
                                "volume_threshold") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.prepaid_config_name.is_set or
                    self.accounting_method_list.is_set or
                    self.author_method_list.is_set or
                    self.password.is_set or
                    self.time_hold.is_set or
                    self.time_threshold.is_set or
                    self.time_valid.is_set or
                    self.traffic_direction.is_set or
                    self.volume_threshold.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.prepaid_config_name.yfilter != YFilter.not_set or
                    self.accounting_method_list.yfilter != YFilter.not_set or
                    self.author_method_list.yfilter != YFilter.not_set or
                    self.password.yfilter != YFilter.not_set or
                    self.time_hold.yfilter != YFilter.not_set or
                    self.time_threshold.yfilter != YFilter.not_set or
                    self.time_valid.yfilter != YFilter.not_set or
                    self.traffic_direction.yfilter != YFilter.not_set or
                    self.volume_threshold.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "prepaid-configuration" + "[prepaid-config-name='" + self.prepaid_config_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting/prepaid-configurations/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.prepaid_config_name.is_set or self.prepaid_config_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prepaid_config_name.get_name_leafdata())
                if (self.accounting_method_list.is_set or self.accounting_method_list.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_method_list.get_name_leafdata())
                if (self.author_method_list.is_set or self.author_method_list.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.author_method_list.get_name_leafdata())
                if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.password.get_name_leafdata())
                if (self.time_hold.is_set or self.time_hold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.time_hold.get_name_leafdata())
                if (self.time_threshold.is_set or self.time_threshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.time_threshold.get_name_leafdata())
                if (self.time_valid.is_set or self.time_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.time_valid.get_name_leafdata())
                if (self.traffic_direction.is_set or self.traffic_direction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.traffic_direction.get_name_leafdata())
                if (self.volume_threshold.is_set or self.volume_threshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.volume_threshold.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "prepaid-config-name" or name == "accounting-method-list" or name == "author-method-list" or name == "password" or name == "time-hold" or name == "time-threshold" or name == "time-valid" or name == "traffic-direction" or name == "volume-threshold"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "prepaid-config-name"):
                    self.prepaid_config_name = value
                    self.prepaid_config_name.value_namespace = name_space
                    self.prepaid_config_name.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-method-list"):
                    self.accounting_method_list = value
                    self.accounting_method_list.value_namespace = name_space
                    self.accounting_method_list.value_namespace_prefix = name_space_prefix
                if(value_path == "author-method-list"):
                    self.author_method_list = value
                    self.author_method_list.value_namespace = name_space
                    self.author_method_list.value_namespace_prefix = name_space_prefix
                if(value_path == "password"):
                    self.password = value
                    self.password.value_namespace = name_space
                    self.password.value_namespace_prefix = name_space_prefix
                if(value_path == "time-hold"):
                    self.time_hold = value
                    self.time_hold.value_namespace = name_space
                    self.time_hold.value_namespace_prefix = name_space_prefix
                if(value_path == "time-threshold"):
                    self.time_threshold = value
                    self.time_threshold.value_namespace = name_space
                    self.time_threshold.value_namespace_prefix = name_space_prefix
                if(value_path == "time-valid"):
                    self.time_valid = value
                    self.time_valid.value_namespace = name_space
                    self.time_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "traffic-direction"):
                    self.traffic_direction = value
                    self.traffic_direction.value_namespace = name_space
                    self.traffic_direction.value_namespace_prefix = name_space_prefix
                if(value_path == "volume-threshold"):
                    self.volume_threshold = value
                    self.volume_threshold.value_namespace = name_space
                    self.volume_threshold.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.prepaid_configuration:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.prepaid_configuration:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "prepaid-configurations" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "prepaid-configuration"):
                for c in self.prepaid_configuration:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.prepaid_configuration.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "prepaid-configuration"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.prepaid_configurations is not None and self.prepaid_configurations.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.prepaid_configurations is not None and self.prepaid_configurations.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-subscriber-accounting-cfg:subscriber-accounting" + path_buffer

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

        if (child_yang_name == "prepaid-configurations"):
            if (self.prepaid_configurations is None):
                self.prepaid_configurations = SubscriberAccounting.PrepaidConfigurations()
                self.prepaid_configurations.parent = self
                self._children_name_map["prepaid_configurations"] = "prepaid-configurations"
            return self.prepaid_configurations

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "prepaid-configurations"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SubscriberAccounting()
        return self._top_entity

