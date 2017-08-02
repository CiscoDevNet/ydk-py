""" Cisco_IOS_XR_infra_statsd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-statsd package configuration.

This module contains definitions
for the following management objects\:
  statistics\: Global statistics configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Statistics(Entity):
    """
    Global statistics configuration
    
    .. attribute:: period
    
    	Collection period for statistics polling
    	**type**\:   :py:class:`Period <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg.Statistics.Period>`
    
    

    """

    _prefix = 'infra-statsd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Statistics, self).__init__()
        self._top_entity = None

        self.yang_name = "statistics"
        self.yang_parent_name = "Cisco-IOS-XR-infra-statsd-cfg"

        self.period = Statistics.Period()
        self.period.parent = self
        self._children_name_map["period"] = "period"
        self._children_yang_names.add("period")


    class Period(Entity):
        """
        Collection period for statistics polling
        
        .. attribute:: service_accounting
        
        	Collection polling period for service accounting collectors
        	**type**\:   :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg.Statistics.Period.ServiceAccounting>`
        
        

        """

        _prefix = 'infra-statsd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Statistics.Period, self).__init__()

            self.yang_name = "period"
            self.yang_parent_name = "statistics"

            self.service_accounting = Statistics.Period.ServiceAccounting()
            self.service_accounting.parent = self
            self._children_name_map["service_accounting"] = "service-accounting"
            self._children_yang_names.add("service-accounting")


        class ServiceAccounting(Entity):
            """
            Collection polling period for service
            accounting collectors
            
            .. attribute:: polling_disable
            
            	Disable periodic statistics polling for service accounting collectors
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: polling_period
            
            	Collection polling period for service accounting collectors
            	**type**\:  int
            
            	**range:** 30..3600
            
            	**default value**\: 900
            
            

            """

            _prefix = 'infra-statsd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Statistics.Period.ServiceAccounting, self).__init__()

                self.yang_name = "service-accounting"
                self.yang_parent_name = "period"

                self.polling_disable = YLeaf(YType.empty, "polling-disable")

                self.polling_period = YLeaf(YType.uint32, "polling-period")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("polling_disable",
                                "polling_period") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Statistics.Period.ServiceAccounting, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Statistics.Period.ServiceAccounting, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.polling_disable.is_set or
                    self.polling_period.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.polling_disable.yfilter != YFilter.not_set or
                    self.polling_period.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "service-accounting" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-statsd-cfg:statistics/period/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.polling_disable.is_set or self.polling_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.polling_disable.get_name_leafdata())
                if (self.polling_period.is_set or self.polling_period.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.polling_period.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "polling-disable" or name == "polling-period"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "polling-disable"):
                    self.polling_disable = value
                    self.polling_disable.value_namespace = name_space
                    self.polling_disable.value_namespace_prefix = name_space_prefix
                if(value_path == "polling-period"):
                    self.polling_period = value
                    self.polling_period.value_namespace = name_space
                    self.polling_period.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.service_accounting is not None and self.service_accounting.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.service_accounting is not None and self.service_accounting.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "period" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-statsd-cfg:statistics/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "service-accounting"):
                if (self.service_accounting is None):
                    self.service_accounting = Statistics.Period.ServiceAccounting()
                    self.service_accounting.parent = self
                    self._children_name_map["service_accounting"] = "service-accounting"
                return self.service_accounting

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "service-accounting"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.period is not None and self.period.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.period is not None and self.period.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-statsd-cfg:statistics" + path_buffer

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

        if (child_yang_name == "period"):
            if (self.period is None):
                self.period = Statistics.Period()
                self.period.parent = self
                self._children_name_map["period"] = "period"
            return self.period

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "period"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Statistics()
        return self._top_entity

